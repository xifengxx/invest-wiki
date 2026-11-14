#!/usr/bin/env bash
#
# invest-wiki 上线脚本 —— 校验 → 推送 → 等 GitHub Actions 发布 → 验证线上版本
#
# 线上页面：https://xifengxx.github.io/invest-wiki/
# 由本仓库 .github/workflows/pages.yml 发布（actions/deploy-pages），不经中转仓库。
#
# 用法：
#   ./deploy.sh              # 校验 + 推送 + 等发布 + 验证
#   ./deploy.sh --no-push    # 不推送（已推过），只等发布 + 验证
#   ./deploy.sh --verify     # 只读验证，不推送、不等待
#
# 退出码：0 = 线上版本 == 本地 HEAD；1 = 失败或不一致

set -euo pipefail

REPO="xifengxx/invest-wiki"
WORKFLOW="pages.yml"
SITE="https://xifengxx.github.io/invest-wiki"
MAX_WAIT_SEC=600        # 等 Actions 跑完的上限
CDN_WAIT_SEC=90         # 等 Pages 生效的上限

cd "$(dirname "$0")"

MODE="full"
case "${1:-}" in
  --no-push) MODE="nopush" ;;
  --verify)  MODE="verify" ;;
  "")        MODE="full" ;;
  *) echo "未知参数：${1}（可用：--no-push / --verify）" >&2; exit 1 ;;
esac

c_ok()   { printf '\033[32m%s\033[0m\n' "$*"; }
c_warn() { printf '\033[33m%s\033[0m\n' "$*"; }
c_err()  { printf '\033[31m%s\033[0m\n' "$*" >&2; }
step()   { printf '\n\033[36m▸ %s\033[0m\n' "$*"; }

command -v gh >/dev/null || { c_err "未安装 gh CLI"; exit 1; }
gh auth status >/dev/null 2>&1 || { c_err "gh 未登录（跑 gh auth login）"; exit 1; }

HEAD_SHA=$(git rev-parse HEAD)

# ── 0. 上线前校验 ─────────────────────────────────────────
# 覆盖面最全的一闸：能抓到「改了 L2 但忘了重编译」——那时工作树是干净的，
# 只推送的话 Actions 会忠实地把过期产物发上线（工作流里也会再跑一次同样的校验）。
if [ "$MODE" != "verify" ]; then
  step "0/3 上线前校验（L2/L3 一致性 + 图谱 + 索引）"
  if ! python3 L1-Schema与Pipeline/lint/verify_all.py; then
    c_err "❌ 校验未通过，已中止上线。修好后重跑本脚本。"
    exit 1
  fi
  c_ok "✓ 校验通过"
fi

# ── 1. 推送 ──────────────────────────────────────────────
if [ "$MODE" = "full" ]; then
  step "1/3 推送到 origin/master"
  if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
    c_warn "⚠️  有未提交的改动，先提交再跑本脚本："
    git status --short --untracked-files=no
    exit 1
  fi
  AHEAD=$(git rev-list --count origin/master..master 2>/dev/null || echo 0)
  if [ "$AHEAD" -gt 0 ]; then
    echo "本地领先远程 $AHEAD 个提交，推送中…"
    git push origin master
    c_ok "✓ 已推送"
  else
    c_ok "✓ 远程已是最新，无需推送"
  fi
else
  step "1/3 跳过推送（模式：${MODE}）"
fi

# ── 2. 等 Actions 发布完成 ────────────────────────────────
if [ "$MODE" != "verify" ]; then
  step "2/3 等待 GitHub Actions（$WORKFLOW）"
  WAITED=0
  RUN_ID=""
  while [ "$WAITED" -lt 180 ]; do
    RUN_ID=$(gh run list -R "$REPO" --workflow="$WORKFLOW" --limit 20 \
             --json databaseId,headSha \
             --jq "[.[] | select(.headSha==\"$HEAD_SHA\")][0].databaseId // empty" 2>/dev/null || true)
    [ -n "$RUN_ID" ] && break
    sleep 10; WAITED=$((WAITED+10))
  done
  if [ -z "$RUN_ID" ]; then
    c_err "找不到 $HEAD_SHA 的 $WORKFLOW 运行记录"
    echo "  · 工作流文件是否已推送？  ls .github/workflows/pages.yml"
    echo "  · 仓库是否已开启 Pages（Source = GitHub Actions）？"
    echo "  · 也可以去 Actions 页手动 Run workflow"
    exit 1
  fi

  WAITED=0
  while [ "$WAITED" -lt "$MAX_WAIT_SEC" ]; do
    STATUS=$(gh run view "$RUN_ID" -R "$REPO" --json status,conclusion \
             --jq '"\(.status) \(.conclusion)"' 2>/dev/null || echo "unknown ")
    case "$STATUS" in
      "completed success") c_ok "✓ 发布成功 (run $RUN_ID)"; break ;;
      completed*) c_err "✗ 发布失败：${STATUS}（run ${RUN_ID}）"; exit 1 ;;
    esac
    sleep 10; WAITED=$((WAITED+10))
  done
else
  step "2/3 跳过等待（模式：verify）"
fi

# ── 3. 验证线上版本 == 本地 HEAD ─────────────────────────
# 用 _site/version.txt（内容就是提交 SHA）比对。比抓 4MB 的 wiki_data.json 便宜，
# 也不会因为 CDN 截断而误判。
step "3/3 验证线上版本"
GOT=""
WAITED=0
while [ "$WAITED" -lt "$CDN_WAIT_SEC" ]; do
  GOT=$(curl -fsS --max-time 15 "$SITE/version.txt?ts=$(date +%s)" 2>/dev/null | tr -d '[:space:]' || true)
  [ "$GOT" = "$HEAD_SHA" ] && break
  sleep 5; WAITED=$((WAITED+5))
done

if [ "$GOT" = "$HEAD_SHA" ]; then
  c_ok "✅ 线上已是本地 HEAD（${HEAD_SHA:0:12}）"
  echo "   页面：$SITE/"
  echo "   （浏览器若显示旧内容，强制刷新一次清缓存）"
  exit 0
fi

c_err "❌ 线上版本与本地 HEAD 不一致"
echo "   本地 HEAD：${HEAD_SHA:0:12}"
echo "   线上报告：${GOT:-（取不到 version.txt）}"
echo "   可能原因："
echo "   · Pages 首次启用/首次部署，还没生效（去 Actions 或 Settings → Pages 看状态）"
echo "   · 部署仍在进行：gh run list -R $REPO --workflow=$WORKFLOW --limit 3"
echo "   · 上一步推送后忘记跑 Actions？push 本身就会触发，工作流需已存在于 master"
exit 1
