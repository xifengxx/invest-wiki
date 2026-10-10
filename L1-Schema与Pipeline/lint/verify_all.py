#!/usr/bin/env python3
"""Invest Wiki 统一校验入口。

把原先只存在于 `执行指令-定期扫描.md` 里的 Markdown heredoc 检查、以及散落在
文档里的"编译后手工跑一遍"，收敛成一个可被 pre-commit / deploy.sh 调用的脚本。

设计原则：**复用而非重写**。
- L2 解析用 engine/parser.py，图谱用 engine/graph.py（与编译器同源同代码路径）
- 新鲜度检查用「重新编译到临时文件再逐字节比对」，直接复用真编译器，
  而不是另写一套"L2 应该产生什么"的转换逻辑（那必然会与编译器漂移）
- index.html 结构检查复用 validate.py（子进程调用）

退出码：0 = 通过（可能有 warning）；1 = 有 hard error。
用法：
    python3 L1-Schema与Pipeline/lint/verify_all.py [--quiet] [--no-html]
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.parser import WikiParser          # noqa: E402
from engine.graph import GraphBuilder         # noqa: E402

sys.path.insert(0, str(ROOT / 'L3-网页产物'))
from build_chain_universe import market_guess, normalize_ticker  # noqa: E402
# 龙头级判定与分档复用 list_deepening_targets，避免双份实现漂移
from list_deepening_targets import is_leader, collect as _ld_collect, tier as _ld_tier  # noqa: E402

WIKI_DIR = ROOT / 'L2-Wiki'
L3_DIR = ROOT / 'L3-网页产物'
WIKI_JSON = L3_DIR / 'wiki_data.json'
UNIVERSE_JSON = L3_DIR / 'chain_universe.json'
INDEX_MD = WIKI_DIR / 'index.md'
BUILD_WIKI = L3_DIR / 'build_wiki_data.py'

# 图谱四检阈值（lint/执行指令-定期扫描.md 的定义）
MIN_EDGE_NODE_RATIO = 1.5
MIN_COMPANY_INEDGE_PCT = 70.0

errors, warnings = [], []


def hard(cond, ok_msg, bad_msg):
    if cond:
        print(f"  ✅ {ok_msg}")
    else:
        print(f"  ❌ {bad_msg}")
        errors.append(bad_msg)
    return cond


def soft(cond, ok_msg, bad_msg):
    if cond:
        print(f"  ✅ {ok_msg}")
    else:
        print(f"  ⚠️  {bad_msg}")
        warnings.append(bad_msg)
    return cond


# ── 1. L2 解析 ────────────────────────────────────────────────────────────
def check_dup_keys():
    """frontmatter 顶层键不得重复 —— PyYAML 静默取最后一个，前者被丢弃。

    2026-09-13 实测全库有 13 个公司词条重复了 `ticker` 键（模板遗留的镜像副本），
    其中 3 个两处取值不同（`002371.SZ` vs `'002371'`），前者被静默丢掉。
    """
    bad = []
    for p in WIKI_DIR.rglob('*.md'):
        parts = p.read_text(encoding='utf-8').split('---')
        if len(parts) < 3:
            continue
        keys = re.findall(r'^([A-Za-z_][A-Za-z0-9_]*):', parts[1], re.M)
        dups = sorted({k for k in keys if keys.count(k) > 1})
        if dups:
            bad.append(f"{p.relative_to(WIKI_DIR)}: {dups}")
    hard(not bad, "frontmatter 无重复顶层键",
         f"{len(bad)} 个文件有重复顶层键（PyYAML 静默取最后一个，前者丢失）: {bad[:5]}")


def check_l2(parser):
    print("1. L2 解析")
    total = len(parser.entities)
    unknown = [e for e in parser.entities.values() if e.entity_type == 'unknown']
    hard(total > 0, f"解析到 {total} 个词条", "L2 一个词条都没解析出来")
    check_dup_keys()
    if not hard(
        len(unknown) == 0,
        "unknown 实体 = 0",
        f"unknown 实体 {len(unknown)} 个（YAML frontmatter 解析失败，常见原因："
        f"值以 `**` 开头被当作 YAML alias）: "
        + ", ".join(e.path for e in unknown[:5]),
    ):
        pass
    return total


# ── 2. L3 产物存在且合法 ──────────────────────────────────────────────────
def load_json(path, label):
    if not path.exists():
        errors.append(f"{label} 不存在: {path}")
        print(f"  ❌ {label} 不存在")
        return None
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        errors.append(f"{label} 不是合法 JSON: {e}")
        print(f"  ❌ {label} 不是合法 JSON: {e}")
        return None


def check_artifacts():
    print("\n2. L3 产物")
    data = load_json(WIKI_JSON, 'wiki_data.json')
    universe = load_json(UNIVERSE_JSON, 'chain_universe.json')
    if data:
        print(f"  ✅ wiki_data.json 合法（{data.get('total')} 实体）")
    return data, universe


# ── 3. L2 → L3 新鲜度（堵「改了 L2 忘了重编译却照样上线」）────────────────
def canonical(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, ensure_ascii=False).encode('utf-8')
    ).hexdigest()


def check_freshness(data):
    print("\n3. L2 → L3 新鲜度")
    if not data:
        print("  ⏭  跳过（wiki_data.json 不可用）")
        return
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as tf:
        tmp = tf.name
    try:
        env = dict(os.environ, WIKI_DIR=str(WIKI_DIR), OUTPUT_JSON=tmp)
        proc = subprocess.run(
            [sys.executable, str(BUILD_WIKI)],
            cwd=str(L3_DIR), env=env, capture_output=True, text=True,
        )
        if proc.returncode != 0:
            errors.append(f"重新编译失败（rc={proc.returncode}）: {proc.stderr.strip()[:300]}")
            print(f"  ❌ 重新编译失败：{proc.stderr.strip()[:200]}")
            return
        fresh = json.loads(Path(tmp).read_text(encoding='utf-8'))
    finally:
        os.unlink(tmp)

    if canonical(fresh) == canonical(data):
        print("  ✅ 磁盘产物与 L2 当前状态一致（未过期）")
        return

    # 定位差异
    old = {e['slug']: e for e in data.get('entities', [])}
    new = {e['slug']: e for e in fresh.get('entities', [])}
    changed = [s for s in new if s in old and canonical(old[s]) != canonical(new[s])]
    added, removed = sorted(set(new) - set(old)), sorted(set(old) - set(new))
    detail = []
    if added:
        detail.append(f"新增 {len(added)}: {added[:5]}")
    if removed:
        detail.append(f"删除 {len(removed)}: {removed[:5]}")
    if changed:
        detail.append(f"内容变更 {len(changed)}: {changed[:5]}")
    msg = "wiki_data.json 已过期（L2 改了但没重编译）—— " + "；".join(detail)
    errors.append(msg)
    print(f"  ❌ {msg}")


# ── 4. 图谱完整性四检 ─────────────────────────────────────────────────────
def check_graph(parser, data):
    print("\n4. 图谱完整性")
    graph = GraphBuilder(parser).build_graph()
    nodes, edges = graph['nodes'], graph['edges']
    indeg = {}
    for e in edges:
        indeg[e['target']] = indeg.get(e['target'], 0) + 1

    segs = {e.name for e in parser.entities.values() if e.entity_type == 'segment'}
    comps = {e.name for e in parser.entities.values() if e.entity_type == 'company'}

    ratio = len(edges) / max(1, len(nodes))
    soft(ratio > MIN_EDGE_NODE_RATIO,
         f"边:节点 = {ratio:.2f} (> {MIN_EDGE_NODE_RATIO})",
         f"边:节点 = {ratio:.2f} 过低（< {MIN_EDGE_NODE_RATIO}），建边逻辑可能退化")

    iso = sorted(n for n in segs if indeg.get(n, 0) == 0)
    hard(not iso, "孤立赛道 = 0", f"孤立赛道 {len(iso)} 个（需补反向 wikilink）: {iso[:8]}")

    pct = sum(1 for c in comps if indeg.get(c, 0) > 0) / max(1, len(comps)) * 100
    soft(pct > MIN_COMPANY_INEDGE_PCT,
         f"公司有入边 {pct:.1f}% (> {MIN_COMPANY_INEDGE_PCT}%)",
         f"公司有入边仅 {pct:.1f}%（< {MIN_COMPANY_INEDGE_PCT}%），"
         f"可能是赛道→公司边的名称不匹配")

    # 产物里的图应与实时重算的一致
    if data and data.get('graph'):
        hard(len(data['graph']['edges']) == len(edges),
             f"产物图边数与实时重算一致（{len(edges)}）",
             f"产物图边数 {len(data['graph']['edges'])} ≠ 实时重算 {len(edges)}（产物过期）")
    return graph


# ── 5. wikilink ↔ edge 一致性 ─────────────────────────────────────────────
def check_link_edge(data, graph):
    """产物 JSON 里的每个 wikilink 都应对应一条边。

    抓的是已知隐患：build_wiki_data.py 对 wikilinks 做了别名清洗
    （如 `光模块` → `光模块(800G/1.6T)`），而 GraphBuilder 用的是原始 Entity，
    别名链接会在图里被当悬空引用丢弃 —— JSON 有链接、图无边的静默不一致。
    """
    print("\n5. wikilink ↔ 图边一致性")
    if not data:
        print("  ⏭  跳过")
        return
    node_set = {n['name'] for n in graph['nodes']}
    have = {(e['source'], e['target']) for e in graph['edges']}
    missing = []
    for e in data.get('entities', []):
        src = e['name']
        for tgt in (e.get('wikilinks') or []):
            if tgt == src or tgt not in node_set:
                continue
            if (src, tgt) not in have:
                missing.append(f"{src} → {tgt}")
    hard(not missing,
         f"产物中每条 wikilink 均有对应图边（{len(have)} 条边）",
         f"{len(missing)} 条 wikilink 在图中无边（别名清洗与建图不同源）: {missing[:6]}")


# ── 6. chain_universe 新鲜度 ──────────────────────────────────────────────
def check_universe(universe):
    print("\n6. chain_universe 新鲜度")
    if not universe or not WIKI_JSON.exists():
        print("  ⏭  跳过")
        return
    recorded = universe.get('source_sha256')
    actual = hashlib.sha256(WIKI_JSON.read_bytes()).hexdigest()
    hard(recorded == actual,
         f"source_sha256 与 wiki_data.json 一致（{actual[:12]}）",
         f"chain_universe.json 已过期：记录 {str(recorded)[:12]} ≠ 当前 {actual[:12]}")


# ── 7. index.md 与源文件一致性 ────────────────────────────────────────────
def _num(s):
    return s.rstrip('0').rstrip('.') if '.' in s else s


def check_index(parser):
    print("\n7. index.md 一致性")
    if not INDEX_MD.exists():
        hard(False, "", "index.md 不存在")
        return
    idx = INDEX_MD.read_text(encoding='utf-8')
    segs = [e for e in parser.entities.values() if e.entity_type == 'segment']
    drift, missing = [], []
    for s in segs:
        tam = _num(f"{float(s.frontmatter.get('tam_bn', 0)):g}")
        cagr = _num(f"{float(s.frontmatter.get('cagr_pct', 0)):g}")
        m = re.search(
            rf'\({re.escape(s.slug)}\)[^\n]*?TAM \*\*\$([0-9.]+)B\*\* · CAGR \*\*([0-9.]+)%\*\*', idx)
        if not m:
            missing.append(s.slug)
            continue
        if _num(m.group(1)) != tam or _num(m.group(2)) != cagr:
            drift.append(f"{s.name}: index=${m.group(1)}B/{m.group(2)}% vs 源=${tam}B/{cagr}%")
    hard(not missing, f"index.md 登记了全部 {len(segs)} 个赛道",
         f"index.md 缺失 {len(missing)} 个赛道: {missing[:6]}")
    soft(not drift, "index.md 的 TAM/CAGR 与源文件全部一致",
         f"index.md 数值漂移 {len(drift)} 处: {drift[:6]}")

    # 统计数字
    for label, actual in (
        ('公司总数', len(parser.get_by_type('company'))),
        ('概念总数', len(parser.get_by_type('concept'))),
        ('论点总数', len(parser.get_by_type('thesis'))),
    ):
        m = re.search(rf'{label}：(\d+)', idx)
        soft(m and int(m.group(1)) == actual,
             f"index.md {label} = {actual}",
             f"index.md {label} 记 {m.group(1) if m else '?'}，实际 {actual}")
    m = re.search(r'赛道总数：(\d+)', idx)
    soft(m and int(m.group(1)) == len(segs),
         f"index.md 赛道总数 = {len(segs)}",
         f"index.md 赛道总数记 {m.group(1) if m else '?'}，实际唯一数 {len(segs)}")


# ── 7b. 公司 one_liner 质量 ───────────────────────────────────────────────
def check_one_liner(parser):
    """`one_liner` 是公司详情页「定位与介绍」块的唯一数据源，为空则整块不渲染。

    2026-09-13 前有 227 家公司（56%）是 invest_kg 迁移残留骨架：`one_liner: ''`、
    描述只写在 body 的 `## 基本信息` 里，导致点进去像坏掉的空页面。
    """
    print("\n7b. 公司 one_liner")
    empty, broken = [], []
    for e in parser.entities.values():
        if e.entity_type != 'company':
            continue
        ol = (e.frontmatter.get('one_liner') or '').strip()
        if not ol:
            empty.append(e.name)
        elif re.search(r'位于产业链\s*[（(]|位于产业链\s*$', ol):
            broken.append(f"{e.name}: {ol[:40]}")
    # 新建骨架词条可能暂时为空，故只告警不硬拦；但要能看见规模
    soft(not empty, "所有公司词条都有 one_liner",
         f"{len(empty)} 家公司 one_liner 为空（详情页「定位与介绍」块不会渲染）: {empty[:8]}")
    hard(not broken, "one_liner 的「位于产业链」后带层级",
         f"{len(broken)} 家 one_liner 在「位于产业链」后缺层级（chain_layer 为空时拼接所致）: {broken[:5]}")


# ── 8. ticker 规范（chain_universe 的键）─────────────────────────────────
def check_tickers(parser):
    """ticker 会被 build_chain_universe 直接当作 companies 字典的键。

    两个真实踩过的坑：
    - 值无法被 market_guess 分类（如 `-`、`4185.T（已退市）`）→ 生成 UNKNOWN 条目，
      且退市股会被标 tradable=True
    - **同一赛道内 ticker 重复** → 后写入的条目覆盖先写入的，静默丢公司
      （曾发生：大模型赛道 4 家都填 `未上市`，只剩 1 家活下来）
    """
    print("\n8. ticker 规范")
    PLACEHOLDERS = {'未上市', '-', '无', 'N/A', 'NA', '--'}
    bad_unknown, dupes, placeholders = [], [], []
    for e in parser.entities.values():
        if e.entity_type == 'company':
            t = e.frontmatter.get('ticker')
            if t and str(t).strip() and market_guess(normalize_ticker(t)) == 'UNKNOWN':
                bad_unknown.append(f"{e.name}: {t!r}")
            if t and str(t).strip().upper() in PLACEHOLDERS:
                placeholders.append(f"公司词条 {e.name}: {t!r}")
        if e.entity_type == 'segment':
            seen = {}
            for c in (e.frontmatter.get('companies') or []):
                if not isinstance(c, dict):
                    continue
                t = c.get('ticker')
                if not t or not str(t).strip():
                    continue
                key = normalize_ticker(t)
                if market_guess(key) == 'UNKNOWN':
                    bad_unknown.append(f"{e.name} → {c.get('name')}: {t!r}")
                if key in seen:
                    dupes.append(f"{e.name}: {key!r} 同时用于 {seen[key]!r} 与 {c.get('name')!r}")
                else:
                    seen[key] = c.get('name')
                if str(t).strip().upper() in PLACEHOLDERS:
                    placeholders.append(f"{e.name} → {c.get('name')}: {t!r}")
    hard(not bad_unknown,
         "所有 ticker 均可被 market_guess 分类（或为已登记的非交易键）",
         f"{len(bad_unknown)} 个 ticker 无法分类，会让 chain_universe 生成 UNKNOWN 条目"
         f"（未上市/退市请用 build_chain_universe.PRIVATE_TICKERS 里的键）: {bad_unknown[:6]}")
    hard(not dupes,
         "同一赛道内 ticker 无重复",
         f"{len(dupes)} 处赛道内 ticker 重复，后写入者会静默覆盖前者: {dupes[:6]}")
    # 通用占位符虽然能通过分类（在 PRIVATE_TICKERS 里），但它不指向任何一家具体公司，
    # 跨赛道共用时会互相污染，所以只用告警。正确的做法是用公司专属的非交易键。
    soft(not placeholders,
         "未使用通用占位符作为 ticker",
         f"{len(placeholders)} 处使用了通用占位符（应用公司专属非交易键，见 "
         f"build_chain_universe.PRIVATE_TICKERS）: {placeholders[:6]}")


# ── 9. 根文档数字一致性 ───────────────────────────────────────────────────
def _leader_tier_counts():
    """龙头级公司按「全面/中等/薄」分档计数，直接复用待深化清单的 collect()+tier()（同口径）。

    只此一处实现——该分档逻辑若复制一份，必然与清单漂移。
    """
    depth, targets = _ld_collect()
    c = {'全面': 0, '中等': 0, '薄': 0}
    for n in targets:
        c[_ld_tier(depth, n)] += 1
    return c


def check_doc_numbers(parser, data):
    """核对 CLAUDE.md / ARCHITECTURE.md 散文里硬写的计数与实测是否一致。

    由来（2026-10-08）：一天内因数据变更（孤儿公司清零、重复页清理）连做了 4 轮
    根文档数字同步，每次都要人工发现哪几行过期。根因是同一组计数在
    CLAUDE.md / ARCHITECTURE.md / index.md 各抄一份，权威来源却只有实测——
    index.md 由 check_index 覆盖，本项补上两篇根文档的散文数字。

    数据一变就在这里报警，不必再靠人工回读文档。
    """
    print("\n9. 根文档数字一致性（CLAUDE.md / ARCHITECTURE.md）")
    n_comp = len(parser.get_by_type('company'))
    n_seg = len(parser.get_by_type('segment'))
    n_con = len(parser.get_by_type('concept'))
    n_the = len(parser.get_by_type('thesis'))
    n_total = len(parser.entities)
    g = (data or {}).get('graph') or {}
    n_node, n_edge = len(g.get('nodes') or []), len(g.get('edges') or [])
    n_l0 = sum(1 for p in (ROOT / 'L0-原始资料池').rglob('*') if p.is_file())
    _ltc = _leader_tier_counts()
    l_full, l_mid, l_thin = _ltc['全面'], _ltc['中等'], _ltc['薄']

    # 与「骨架」相关的三个计数（直接读文件，口径同 list_deepening_targets.py）
    n_nodate = n_unfilled = n_flat = 0
    for p in (WIKI_DIR / '公司').glob('*.md'):
        parts = p.read_text(encoding='utf-8').split('---', 2)
        if len(parts) < 3:
            continue
        fm = yaml.safe_load(parts[1]) or {}
        if not fm.get('data_freshness_date'):
            n_nodate += 1
        if len([k for k, v in fm.items() if v not in (None, '', [], {})]) < 20:
            n_unfilled += 1
        if not re.search(r'^##\s+', parts[2], re.M):
            n_flat += 1

    CHECKS = [
        ('CLAUDE.md', r'(\d+) 词条（', n_total, '状态行·词条数'),
        ('CLAUDE.md', r'^\| 公司 \| (\d+)（', n_comp, '数据规模表·公司'),
        ('CLAUDE.md', r'^\| 总词条 \| (\d+)（', n_total, '数据规模表·总词条'),
        ('CLAUDE.md', r'公司/ \((\d+)\)', n_comp, '目录树·公司'),
        ('CLAUDE.md', r'覆盖(\d+)家公司', n_comp, '前端功能·公司'),
        ('CLAUDE.md', r'其余 \*\*(\d+) 家\*\*公司无', n_nodate, 'Phase 3·无数据日期'),
        ('ARCHITECTURE.md', r'^\| 赛道（segment） \| (\d+)', n_seg, '规模表·赛道'),
        ('ARCHITECTURE.md', r'^\| 公司（company） \| (\d+)（', n_comp, '规模表·公司'),
        ('ARCHITECTURE.md', r'^\| 概念卡片（concept） \| (\d+)', n_con, '规模表·概念'),
        ('ARCHITECTURE.md', r'^\| 投资论点（thesis） \| (\d+)', n_the, '规模表·论点'),
        ('ARCHITECTURE.md', r'^\| \*\*总词条\*\* \| \*\*(\d+)\*\*', n_total, '规模表·总词条'),
        ('ARCHITECTURE.md', r'^\| 图谱节点 \| (\d+)', n_node, '规模表·图谱节点'),
        ('ARCHITECTURE.md', r'^\| 图谱边 \| (\d+)', n_edge, '规模表·图谱边'),
        ('ARCHITECTURE.md', r'^\| L0 归档文件 \| (\d+)', n_l0, '规模表·L0 文件'),
        ('ARCHITECTURE.md', r'(\d+) 个公司 MD', n_comp, '目录树·公司'),
        ('ARCHITECTURE.md', r'`entities`（(\d+)实体）', n_total, '编译说明·实体数'),
        ('ARCHITECTURE.md', r'(\d+) 家公司中 \*\*(\d+) 家字段未填齐\*\*', (n_comp, n_unfilled),
         '基线·公司数+未填齐'),
        ('ARCHITECTURE.md', r'\*\*(\d+) 家正文零', n_flat, '基线·零叙事'),
        ('CLAUDE.md', r'薄（(\d+) 家', l_thin, 'Tier 3 清单·龙头级薄档'),
        ('CLAUDE.md', r'中等（(\d+) 家', l_mid, 'Tier 3 清单·龙头级中等档'),
        ('ARCHITECTURE.md', r'全面 (\d+) / 中等 (\d+) / 薄 (\d+)',
         (l_full, l_mid, l_thin), '基线·龙头级分档'),
    ]
    stale, unmatched = [], []
    for rel, pat, actual, label in CHECKS:
        f = ROOT / rel
        m = re.search(pat, f.read_text(encoding='utf-8'), re.M) if f.exists() else None
        if not m:
            unmatched.append(f'{rel}·{label}')
            continue
        got = tuple(int(x) for x in m.groups()) if isinstance(actual, tuple) else int(m.group(1))
        if got != actual:
            stale.append(f'{rel}·{label}: 记 {got}，实际 {actual}')
    soft(not stale,
         f"根文档 {len(CHECKS)} 处计数与实测一致",
         f"根文档数字过期 {len(stale)} 处（数据变了但散文没跟上，改数字即可）: {stale}")
    # 匹配不到 = 有人改了措辞，检查已静默失效——必须报出来，否则会假绿
    soft(not unmatched,
         "根文档全部检查模式均匹配到",
         f"根文档 {len(unmatched)} 处检查模式失效（措辞已改，请同步更新本函数的正则）: {unmatched}")


# ── 10. 内容完整度 ────────────────────────────────────────────────────────
# 门槛与推导依据见 docs/内容完整度标准.md。改门槛必须同步该文档。
MIN_COMPANY_FIELDS = 20        # 沿用现有「全面档」定义
MIN_COMPANY_SECTIONS = 5
MIN_COMPANY_CHARS = 1000       # 现有 216 家全面档正文最低 1,111 字
MIN_TRACK_STRUCT = 500         # 回归守卫：现有最低 581
MIN_TRACK_SOURCES = 2          # 1 条等于几乎没有证据基础
MIN_TRACK_TRENDS = 3
MIN_CONCEPT_CHARS = 2000       # 现有最低 2,931
MIN_THESIS_CHARS = 600         # 现有最低 898
MIN_INDUSTRY_CHARS = 300       # 现为 44 字，正是它该被判未达标的原因

TRACK_CORE_FIELDS = ['tam_bn', 'cagr_pct', 'margin', 'cost_share_pct',
                     'profit_pool_pct', 'value_add', 'layer']
TRACK_COMPETITION_SUB = ['global', 'china', 'barriers', 'tech_gap']


def content_chars(body):
    """正文字数：**整节**剔除 `## 动态更新记录` 后，去掉全部空白字符的长度。

    必须整节移除而非从该标题处截断——有的论点把变更记录排在正文最前，
    截断会把真正的内容全部切掉（2026-10-08 用错口径，误判 4 篇论点为「空」）。
    """
    out, skip = [], False
    for line in body.split('\n'):
        if re.match(r'^##\s+动态更新记录', line):
            skip = True
            continue
        if skip and re.match(r'^##\s+(?!动态更新记录)', line):
            skip = False
        if not skip:
            out.append(line)
    return len(re.sub(r'\s+', '', '\n'.join(out)))


def _ylen(v):
    if isinstance(v, str):
        return len(v)
    if isinstance(v, list):
        return sum(_ylen(x) for x in v)
    if isinstance(v, dict):
        return sum(_ylen(x) for x in v.values())
    return 0


def _read_entry(p):
    parts = p.read_text(encoding='utf-8').split('---', 2)
    if len(parts) < 3:
        return None, ''
    try:
        return (yaml.safe_load(parts[1]) or {}), parts[2]
    except Exception:
        return None, ''


def _leader_names():
    """龙头级公司名集合：赛道 companies[].role 含龙头/第一/主导，或以下会补公司自身 chain_role。

    判定复用 list_deepening_targets.is_leader，与待深化清单同源。
    """
    out = set()
    for p in (WIKI_DIR / '赛道').glob('*/*.md'):
        fm, _ = _read_entry(p)
        if not fm:
            continue
        for c in (fm.get('companies') or []):
            if isinstance(c, dict) and is_leader(c.get('role')):
                out.add(c.get('name'))
    return out


def check_content_depth():
    """按 docs/内容完整度标准.md 统计各类型的内容达标率。全部为告警，不阻塞。

    存在意义：内容深度是长期唯一无人检查的维度，因此也是唯一持续漂移的维度。
    2026-10-08 之前没有任何一处写下「写多少才算完整」，导致「169 家薄档」这种
    数字既无法判断是缺陷还是常态。本项把标准变成可检验的数字。

    公司达标率**必须分重要性两层报**：只报总体会给出误导性的低数字——同一个库
    按条目数是 53%，按龙头级是 86%。待办是少数龙头级，不是那一百多家尾部。
    """
    print("\n10. 内容完整度（门槛依据见 docs/内容完整度标准.md）")

    # 概念卡片 / 投资论点
    for label, sub, thr, pat in (('概念卡片', '概念', MIN_CONCEPT_CHARS, '*.md'),
                                 ('投资论点', '论点', MIN_THESIS_CHARS, '*.md')):
        ok = bad = 0
        for p in (WIKI_DIR / sub).glob(pat):
            if 'audit' in p.name.lower():
                continue
            _, body = _read_entry(p)
            if content_chars(body) >= thr:
                ok += 1
            else:
                bad += 1
        soft(bad == 0, f"{label} {ok}/{ok + bad} 达标（正文 ≥{thr} 字）",
             f"{label} {ok}/{ok + bad} 达标，{bad} 篇正文 <{thr} 字")

    # 产业
    ok = bad = 0
    for p in (WIKI_DIR / '产业').glob('*.md'):
        _, body = _read_entry(p)
        (ok, bad) = (ok + 1, bad) if content_chars(body) >= MIN_INDUSTRY_CHARS else (ok, bad + 1)
    soft(bad == 0, f"产业 {ok}/{ok + bad} 达标（正文 ≥{MIN_INDUSTRY_CHARS} 字）",
         f"产业 {ok}/{ok + bad} 达标——{bad} 个产业页正文 <{MIN_INDUSTRY_CHARS} 字"
         f"（四级知识树顶层为空）")

    # 公司（必须分重要性两层）
    leaders = _leader_names()
    ok, bad, tiers = 0, 0, []
    l_ok = l_bad = 0
    for p in sorted((WIKI_DIR / '公司').glob('*.md')):
        fm, body = _read_entry(p)
        if fm is None:
            continue
        nk = len([k for k, v in fm.items() if v not in (None, '', [], {})])
        ns = len(re.findall(r'^##\s+', body, re.M))
        n = content_chars(body)
        is_lead = (fm.get('name') in leaders) or fm.get('chain_role') == '龙头'
        if nk >= MIN_COMPANY_FIELDS and ns >= MIN_COMPANY_SECTIONS and n >= MIN_COMPANY_CHARS:
            ok += 1
            l_ok += is_lead
        else:
            bad += 1
            l_bad += is_lead
            tiers.append('中等' if nk >= MIN_COMPANY_FIELDS else '薄')
    n_c, n_l, n_non = ok + bad, l_ok + l_bad, (ok + bad) - (l_ok + l_bad)
    thin_n = tiers.count('薄')
    soft(bad == 0,
         f"公司 {ok}/{n_c} 达标（字段≥{MIN_COMPANY_FIELDS} 且 ##≥{MIN_COMPANY_SECTIONS} 且 正文≥{MIN_COMPANY_CHARS}字）",
         f"公司 {ok}/{n_c} = {ok / n_c * 100:.0f}% 达标，{bad} 家未达标（薄档 {thin_n} + 中等档 {bad - thin_n}）；"
         f"分重要性看：龙头级 {l_ok}/{n_l} = {l_ok / n_l * 100:.0f}% 已达标，未达标的龙头级仅 {l_bad} 家，"
         f"其余 {bad - l_bad} 家为非龙头尾部——待办以那 {l_bad} 家龙头级为准，勿按条目总数管理"
         f"（清单见 docs/待深化龙头清单.md，标准见 docs/内容完整度标准.md）")

    # 赛道
    st_ok, ev_ok, n_s, weak_ev = 0, 0, 0, []
    for p in (WIKI_DIR / '赛道').glob('*/*.md'):
        fm, _ = _read_entry(p)
        if not fm or fm.get('type') != 'segment':
            continue
        n_s += 1
        comp = fm.get('competition') or {}
        if (all(fm.get(k) not in (None, '', []) for k in TRACK_CORE_FIELDS)
                and all(comp.get(k) not in (None, '', [], {}) for k in TRACK_COMPETITION_SUB)):
            st_ok += 1
        n_src = len(fm.get('sources') or [])
        struct = sum(_ylen(fm.get(k)) for k in
                     ['key_trends', 'sources', 'key_inputs', 'key_customers',
                      'price_conduction', 'competition'])
        if (n_src >= MIN_TRACK_SOURCES and len(fm.get('key_trends') or []) >= MIN_TRACK_TRENDS
                and struct >= MIN_TRACK_STRUCT):
            ev_ok += 1
        else:
            weak_ev.append(f"{fm.get('name')}(sources={n_src})")
    soft(st_ok == n_s, f"赛道结构 {st_ok}/{n_s} 达标（核心量化字段 + competition 四子字段）",
         f"赛道结构 {st_ok}/{n_s} 达标——{n_s - st_ok} 个缺字段")
    soft(ev_ok == n_s, f"赛道证据 {ev_ok}/{n_s} 达标（sources ≥{MIN_TRACK_SOURCES} 条）",
         f"赛道证据 {ev_ok}/{n_s} 达标——{n_s - ev_ok} 个证据单薄: {weak_ev[:6]}")


# ── 11. index.html 结构（复用 validate.py）───────────────────────────────
def check_html():
    print("\n11. index.html 结构")
    proc = subprocess.run(
        [sys.executable, str(L3_DIR / 'validate.py')],
        cwd=str(L3_DIR), capture_output=True, text=True,
    )
    ok = proc.returncode == 0
    hard(ok, "validate.py 全部通过（HTML结构/script/数据/JS函数）",
         f"validate.py 未通过:\n{proc.stdout.strip()[-500:]}")


# ── 12. frontmatter 风格 ──────────────────────────────────────────────────
def check_frontmatter_style():
    """L2 词条的 frontmatter 中不得出现 Markdown 加粗（`**`）。

    两条危害，一重一轻：
    - **致命**：值**以** `**` 开头时，YAML 会把首个 `*` 当作 alias 锚点，
      导致**整个 frontmatter 解析失败**，该实体在编译产物中退化为 `unknown`
      （本项目 2026-09-13 与 2026-10-08~09 多次踩到，单日最多七次）。
    - **轻微**：`**` 出现在值**中间**虽不破坏解析，但前端会把星号原样显示。

    项目规范（L1/CLAUDE.md「禁止操作」章节）统一禁止 frontmatter 使用加粗——
    正文不受限。2026-10-10 一次性清理了 87 个文件、550 处。
    """
    print("\n12. frontmatter 风格（禁 Markdown 加粗）")
    total = hit = 0
    for p in sorted(WIKI_DIR.rglob('*.md')):
        t = p.read_text(encoding='utf-8')
        if not t.startswith('---'):
            continue
        parts = t.split('---', 2)
        if len(parts) < 3:
            continue
        total += 1
        if '**' in parts[1]:
            hit += 1
    soft(hit == 0,
         f"{total} 个 L2 文件的 frontmatter 均无 Markdown 加粗",
         f"{hit} 个文件的 frontmatter 含 `**`——值以 `**` 开头会让整个 frontmatter 解析失败"
         f"（实体退化为 unknown）；清理方式：只对 frontmatter 段（首个 `---` 到第二个 `---`）"
         f"去掉 `**`，正文保留")


# ── 13. 证据链（公司 ↔ L0 溯源）────────────────────────────────────────────
L0_DIR = ROOT / 'L0-原始资料池'


def _name_variants(name):
    """把词条名拆成可匹配源文的变体。

    KB 里的名称常与源文写法不一致，精确匹配会**系统性高估缺口**：
      `环球晶圆 (GlobalWafers)` → 源文只写「环球晶圆」
      `SCREEN Semiconductor`    → 源文只写「SCREEN」/「迪恩士」
      `ON Semiconductor (onsemi)` → 源文只写「onsemi」/「安森美」

    2026-10-10 实测：不做变体拆分时判出「183 家无痕迹」，加入括号拆分与首词变体后
    真正的「有内容却无据」收敛到 0~1 家 —— 差两个数量级。故此处务必保留变体逻辑。
    """
    out = {name}
    for part in re.split(r'[（(）)]', name):
        part = part.strip()
        if len(part) >= 3:
            out.add(part)
    # 首词变体：`SCREEN Semiconductor` → `SCREEN`（≥4 字符才安全，避免 ON / 3M 之类误匹配）
    head = name.split()[0] if name.split() else ''
    if len(head) >= 4:
        out.add(head)
    return out


def check_evidence_chain():
    """核对每家公司能否追溯到 L0 原始资料。只把「有内容却无据」报为告警。

    三档判定（判据经 2026-10-10 四轮迭代验证）：
      A 有专档 —— 名称变体命中 L0 的文件名 / `source_name` / `tags`
      B 被覆盖 —— 名称变体只出现在 L0 正文里（含**批次归档**：一份 `{日期}-{批次}-数据溯源.md`
                  覆盖多家公司，公司名只在正文出现，故必须做正文匹配）
      C 无痕迹 —— 两者皆无

    只有 **C 档且有实质内容** 才是真问题（数据无出处）；C 档纯骨架属正常（尚未建档）。

    ⚠️ **已知偏差（有意保留）**：3~4 字符的 ASCII 简称（`AMD` / `Meta` / `SAP`）作为子串
    可能误命中无关文本（如 `AMD` 命中 `AMDOCS`），使本检查**倾向于"多算有据"**。
    这个方向是安全的——它会让告警偏保守，而不会虚报缺口。反过来（虚报缺口）才是要避免的：
    2026-10-10 用朴素精确匹配曾虚报「183 家无痕迹」，实际约 0 家。
    """
    print("\n13. 证据链（公司 ↔ L0 溯源）")
    if not L0_DIR.exists():
        hard(False, "", f"L0 目录不存在: {L0_DIR}")
        return
    meta_blobs, body_parts, n_l0 = [], [], 0
    for p in L0_DIR.rglob('*'):
        if not p.is_file() or p.suffix not in ('.md', '.txt'):
            continue
        n_l0 += 1
        t = p.read_text(encoding='utf-8', errors='ignore')
        body_parts.append(t)
        blob = p.name
        if t.startswith('---'):
            try:
                fm = yaml.safe_load(t.split('---', 2)[1]) or {}
                blob += ' ' + str(fm.get('source_name') or '') + ' ' + ' '.join(map(str, fm.get('tags') or []))
            except Exception:
                pass
        meta_blobs.append(blob)
    meta_all = '\n'.join(meta_blobs)
    body_all = '\n'.join(body_parts)

    a = b = 0
    orphan = []          # C 档且有实质内容 —— 唯一告警项
    skeleton_c = 0       # C 档纯骨架 —— 正常，只计数
    for p in sorted((WIKI_DIR / '公司').glob('*.md')):
        fm, body = _read_entry(p)
        if fm is None:
            continue
        name = fm.get('name')
        if not name:
            continue
        vs = _name_variants(str(name))
        tick = str(fm.get('ticker') or '')
        in_meta = any(v in meta_all for v in vs) or (len(tick) >= 3 and tick.upper() in meta_all.upper())
        if in_meta:
            a += 1
            continue
        if any(v in body_all for v in vs):
            b += 1
            continue
        nk = len([k for k, v in fm.items() if v not in (None, '', [], {})])
        if nk >= MIN_COMPANY_FIELDS or re.search(r'^##\s+', body, re.M):
            orphan.append(f"{name}(字段{nk})")
        else:
            skeleton_c += 1

    soft(not orphan,
         f"证据链完整：{a} 家有专档、{b} 家被批次/主题归档覆盖，无「有内容却无据」的公司"
         f"（另有 {skeleton_c} 家纯骨架尚未建档，不纳入）",
         f"{len(orphan)} 家公司已有内容但**追溯不到任何 L0 归档**"
         f"（数据无出处）：{orphan[:8]}——应为每家补 L0 归档，或降级其数据标注")


def main():
    args = sys.argv[1:]
    quiet = '--quiet' in args
    parser = WikiParser(str(WIKI_DIR))
    parser.parse_all()

    print("🔍 Invest Wiki 统一校验\n" + "=" * 56)
    check_l2(parser)
    data, universe = check_artifacts()
    check_freshness(data)
    graph = check_graph(parser, data)
    check_link_edge(data, graph)
    check_universe(universe)
    check_index(parser)
    check_one_liner(parser)
    check_tickers(parser)
    check_doc_numbers(parser, data)
    check_content_depth()
    if '--no-html' not in args:
        check_html()
    check_frontmatter_style()
    check_evidence_chain()

    print("\n" + "=" * 56)
    if warnings and not quiet:
        print(f"⚠️  {len(warnings)} 项告警（不阻塞）")
    if errors:
        print(f"❌ {len(errors)} 个硬错误——禁止提交/部署：")
        for e in errors:
            print(f"   • {e}")
        print("\n如确需绕过：SKIP_WIKI_CHECK=1 git commit ...")
        return 1
    print("✅ 全部硬检查通过")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
