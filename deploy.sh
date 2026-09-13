#!/usr/bin/env bash
#
# invest-wiki 上线脚本 —— 推送本仓库 → 触发 kol-daily 同步 → 验证内容一致
#
# 背景：线上页面 https://xifengxx.github.io/kol-daily/industry-chain/index.html
#       由 kol-daily 仓库（gh-pages 分支）的 industry-chain/ 目录提供，
#       数据来自本仓库的 L3-网页产物/wiki_data.json。
#       同步由 kol-daily 的 sync-modules.yml 完成，但其 cron 被 GitHub 节流，
#       实际延迟 2-3 小时（配置写的是 30 分钟）。本脚本用 workflow_dispatch
#       立即触发，把延迟降到几十秒。
#
# 用法：
#   ./deploy.sh              # 推送 + 触发同步 + 验证
#   ./deploy.sh --no-push    # 不推送（已推送过），只触发同步 + 验证
#   ./deploy.sh --verify     # 只读验证，不推送也不触发
#
# 退出码：0 = 全部一致；1 = 失败或不一致

set -euo pipefail

KOL_REPO="xifengxx/kol-daily"
KOL_BRANCH="gh-pages"
WORKFLOW="sync-modules.yml"
MAX_WAIT_SEC=600        # 等待工作流完成的上限
RAW_SETTLE_SEC=45       # push 后等 raw CDN 刷新的时间

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

# ── 前置检查 ──────────────────────────────────────────────
command -v gh >/dev/null || { c_err "未安装 gh CLI"; exit 1; }
gh auth status >/dev/null 2>&1 || { c_err "gh 未登录（跑 gh auth login）"; exit 1; }

# ── 1. 推送 ──────────────────────────────────────────────
if [ "$MODE" = "full" ]; then
  step "1/4 推送到 origin/master"
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
    echo "等待 raw CDN 刷新（${RAW_SETTLE_SEC}s），否则同步会拉到旧内容…"
    sleep "$RAW_SETTLE_SEC"
  else
    c_ok "✓ 远程已是最新，无需推送"
  fi
else
  step "1/4 跳过推送（模式：${MODE}）"
fi

# ── 2. 触发同步 ──────────────────────────────────────────
if [ "$MODE" != "verify" ]; then
  step "2/4 触发 kol-daily 同步工作流"
  gh workflow run "$WORKFLOW" -R "$KOL_REPO" --ref "$KOL_BRANCH"
  echo "已触发，等待运行完成…"

  WAITED=0
  RUN_ID=""
  while [ "$WAITED" -lt 120 ]; do
    sleep 10; WAITED=$((WAITED+10))
    RUN_ID=$(gh run list -R "$KOL_REPO" --workflow="$WORKFLOW" --limit 1 \
             --json databaseId,status --jq '.[0].databaseId' 2>/dev/null || echo "")
    [ -n "$RUN_ID" ] && break
  done
  if [ -z "$RUN_ID" ]; then
    c_err "未取到工作流运行 ID"; exit 1
  fi

  WAITED=0
  while [ "$WAITED" -lt "$MAX_WAIT_SEC" ]; do
    STATUS=$(gh run view "$RUN_ID" -R "$KOL_REPO" --json status,conclusion \
             --jq '"\(.status) \(.conclusion)"' 2>/dev/null || echo "unknown ")
    case "$STATUS" in
      "completed success") c_ok "✓ 工作流成功 (run $RUN_ID)"; break ;;
      completed*) c_err "✗ 工作流失败：${STATUS}（run ${RUN_ID}）"; exit 1 ;;
    esac
    sleep 10; WAITED=$((WAITED+10))
  done

  echo
  echo "同步日志（关键行）："
  gh run view "$RUN_ID" -R "$KOL_REPO" --log 2>/dev/null \
    | grep -E "有变化|无变化|已提交|✓|✗" | sed 's/^.*Z //' | head -20 || true
else
  step "2/4 跳过触发（模式：verify）"
fi

# ── 3. 等待 Pages 部署 ───────────────────────────────────
if [ "$MODE" != "verify" ]; then
  step "3/4 等待 Pages 部署"
  WAITED=0
  while [ "$WAITED" -lt 300 ]; do
    D_STATUS=$(gh run list -R "$KOL_REPO" --workflow=pages-build-deployment --limit 1 \
               --json status,conclusion --jq '.[0].status + " " + (.[0].conclusion // "running")' 2>/dev/null || echo "")
    case "$D_STATUS" in
      "completed success") c_ok "✓ Pages 部署完成"; break ;;
      completed*) c_warn "Pages 最近一次部署结束于：${D_STATUS}（继续验证仓库内容）"; break ;;
    esac
    sleep 10; WAITED=$((WAITED+10))
  done
else
  step "3/4 跳过部署等待（模式：verify）"
fi

# ── 4. 验证内容一致（git blob 哈希比对）──────────────────
step "4/4 验证：本地 vs kol-daily 仓库"

# 说明：不用 curl 抓 xifengxx.github.io 校验 —— 本机到该 CDN 很慢会截断，
#       会造成"文件损坏"的误判。blob 哈希是密码学级的等同证明。
FAIL=0
verify_one() {
  local local_path="$1" remote_path="$2"
  if [ ! -f "$local_path" ]; then
    printf '  %-34s %s\n' "$remote_path" "⚠️  本地缺文件，跳过"
    return
  fi
  local lsha rsha
  lsha=$(git hash-object "$local_path")
  rsha=$(gh api "repos/$KOL_REPO/contents/$remote_path?ref=$KOL_BRANCH" --jq .sha 2>/dev/null || echo "")
  if [ -z "$rsha" ]; then
    printf '  %-34s %s\n' "$remote_path" "❌ 远程取不到"
    FAIL=1
  elif [ "$lsha" = "$rsha" ]; then
    printf '  %-34s %s\n' "$remote_path" "✅ 一致  ${lsha:0:12}"
  else
    printf '  %-34s %s\n' "$remote_path" "❌ 不一致 本地 ${lsha:0:12} / 远程 ${rsha:0:12}"
    FAIL=1
  fi
}

# 从 kol-daily 的 sync-config.json 读取映射（config 驱动，与同步机制同源）
MAP=$(gh api "repos/$KOL_REPO/contents/sync-config.json?ref=$KOL_BRANCH" --jq .content 2>/dev/null \
      | base64 -d 2>/dev/null \
      | python3 -c "
import json,sys
c=json.load(sys.stdin)
for m in c.get('github_modules',[]):
    if m.get('repo')=='xifengxx/invest-wiki':
        print(m['path'], m['target'])
" 2>/dev/null || echo "")

if [ -z "$MAP" ]; then
  c_warn "取不到 sync-config.json，回退到内置映射"
  MAP="L3-网页产物/wiki_data.json industry-chain/wiki_data.json
L3-网页产物/index.html industry-chain/index.html"
fi

while read -r lpath rpath; do
  [ -n "$lpath" ] && verify_one "$lpath" "$rpath"
done <<< "$MAP"

echo
if [ "$FAIL" -eq 0 ]; then
  c_ok "✅ 全部一致 —— 线上已是本仓库的最新内容"
  echo "   页面：https://xifengxx.github.io/kol-daily/industry-chain/index.html"
  echo "   （浏览器若显示旧内容，强制刷新一次清缓存）"
else
  c_err "❌ 存在不一致 —— 可能原因："
  echo "   · 触发同步时 raw CDN 还没刷新到最新（本脚本已等 ${RAW_SETTLE_SEC}s；"
  echo "     若刚推送完立刻跑仍不一致，等 1 分钟重跑 ./deploy.sh --no-push）"
  echo "   · kol-daily 的 sync-config.json 未登记该文件"
  exit 1
fi
