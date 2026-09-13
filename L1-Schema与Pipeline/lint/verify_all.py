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

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.parser import WikiParser          # noqa: E402
from engine.graph import GraphBuilder         # noqa: E402

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
def check_l2(parser):
    print("1. L2 解析")
    total = len(parser.entities)
    unknown = [e for e in parser.entities.values() if e.entity_type == 'unknown']
    hard(total > 0, f"解析到 {total} 个词条", "L2 一个词条都没解析出来")
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


# ── 8. index.html 结构（复用 validate.py）─────────────────────────────────
def check_html():
    print("\n8. index.html 结构")
    proc = subprocess.run(
        [sys.executable, str(L3_DIR / 'validate.py')],
        cwd=str(L3_DIR), capture_output=True, text=True,
    )
    ok = proc.returncode == 0
    hard(ok, "validate.py 全部通过（HTML结构/script/数据/JS函数）",
         f"validate.py 未通过:\n{proc.stdout.strip()[-500:]}")


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
    if '--no-html' not in args:
        check_html()

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
