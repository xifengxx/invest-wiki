#!/usr/bin/env python3
"""列出「被定位为龙头级、但词条深度未达全面标准」的公司，输出 Markdown 清单。

**用途**：把「哪些公司该像 NVIDIA 那样全面、但还没做到」变成一份可排期的工作清单。

**判据**（两个都可调，见下方常量）：
- 龙头级：赛道 `companies[].role` 含「龙头 / 第一 / 主导」，或公司自身 `chain_role == 龙头`
- 全面  ：`≥FULL_FIELDS` 个 YAML 字段 **且** `≥FULL_SECTIONS` 个 body `##` 段

**为什么用「实际 ## 段数」而不是模板的 5 个固定章节名**：词条普遍用了
`业务板块详解` / `产品技术路线` / `竞争护城河` 这类自定名，按固定名判会把这些
内容更丰富的词条误判为不全面（曾因此把 74 家虚报成未达标）。

用法：
    python3 L1-Schema与Pipeline/lint/list_deepening_targets.py            # 打印摘要
    python3 L1-Schema与Pipeline/lint/list_deepening_targets.py --write    # 写入 docs/
"""
import collections
import datetime
import glob
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / 'L2-Wiki'
OUT = ROOT / 'docs' / '待深化龙头清单.md'

FULL_FIELDS = 20      # 全面档：YAML 字段数下限
FULL_SECTIONS = 5     # 全面档：body ## 段数下限
THIN_FIELDS = 20      # 低于此判为「薄」（字段都没填齐）

LEAD_MARKERS = ('龙头', '第一', '主导')


def is_leader(role) -> bool:
    r = str(role or '')
    return any(m in r for m in LEAD_MARKERS)


def collect():
    depth = {}
    for p in glob.glob(str(WIKI / '公司' / '*.md')):
        t = Path(p).read_text(encoding='utf-8')
        parts = t.split('---', 2)
        if len(parts) < 3:
            continue
        d = yaml.safe_load(parts[1]) or {}
        depth[d.get('name')] = {
            'fields': len([k for k, v in d.items() if v not in (None, '', [], {})]),
            'sections': len(re.findall(r'^##\s+', parts[2], re.M)),
            'chain_role': d.get('chain_role'),
            'ticker': d.get('ticker') or '',
        }

    usage = {}
    for p in glob.glob(str(WIKI / '赛道' / '*' / '*.md')):
        d = yaml.safe_load(Path(p).read_text(encoding='utf-8').split('---')[1])
        if not d or d.get('type') != 'segment':
            continue
        for c in (d.get('companies') or []):
            if not isinstance(c, dict) or c.get('name') not in depth:
                continue
            u = usage.setdefault(c['name'], {'lead': [], 'segments': set(), 'rev': 0})
            u['segments'].add(d['name'])
            if c.get('rev'):
                u['rev'] = max(u['rev'], c['rev'])
            if is_leader(c.get('role')):
                u['lead'].append(f"{d['name']}（{c.get('role')}）")

    targets = {n: u for n, u in usage.items() if u['lead'] or depth[n]['chain_role'] == '龙头'}
    return depth, targets


def tier(depth, n) -> str:
    f, s = depth[n]['fields'], depth[n]['sections']
    if f >= FULL_FIELDS and s >= FULL_SECTIONS:
        return '全面'
    if f >= THIN_FIELDS:
        return '中等'
    return '薄'


def render(depth, targets) -> str:
    rows = []
    for n, u in targets.items():
        rows.append((n, u, tier(depth, n)))
    counts = collections.Counter(t for _, _, t in rows)
    thin = sorted([r for r in rows if r[2] == '薄'],
                  key=lambda r: (-r[1]['rev'], -len(r[1]['segments']), depth[r[0]]['fields']))
    mid = sorted([r for r in rows if r[2] == '中等'],
                 key=lambda r: (-r[1]['rev'], -len(r[1]['segments'])))

    L = []
    L.append('# 待深化龙头清单')
    L.append('')
    L.append(f'> 生成日期：{datetime.date.today().isoformat()}　·　'
             f'由 `L1-Schema与Pipeline/lint/list_deepening_targets.py` 生成，勿手工编辑')
    L.append('')
    L.append('## 这份清单是什么')
    L.append('')
    L.append('产业链赛道里被定位为**龙头级**的公司，其词条深度应当达到 NVIDIA 那一档')
    L.append('（结构化字段齐全 + 多章节叙事）。本清单列出**尚未达标**的。')
    L.append('')
    L.append('**判据**')
    L.append('')
    L.append(f'- **龙头级**：赛道 `companies[].role` 含「龙头 / 第一 / 主导」，'
             f'或公司自身 `chain_role == 龙头`')
    L.append(f'- **全面**：YAML 字段 ≥ {FULL_FIELDS}/25 **且** body `##` 段 ≥ {FULL_SECTIONS}')
    L.append(f'- **薄**：YAML 字段 < {THIN_FIELDS}/25（结构性空缺，需要补数据）')
    L.append('- **中等**：字段齐全但叙事薄（数据都在，只需展开成章节）')
    L.append('')
    L.append('> 用「实际 `##` 段数」而非模板的 5 个固定章节名：词条普遍使用')
    L.append('> `业务板块详解` / `产品技术路线` / `竞争护城河` 等自定名，'
             '按固定名判会把内容更丰富的词条误判为不全面。')
    L.append('')
    L.append('## 总览')
    L.append('')
    L.append('| 档位 | 数量 |')
    L.append('|------|:--:|')
    L.append(f'| ✅ 全面（达标） | {counts.get("全面", 0)} |')
    L.append(f'| ⚠️ 中等（叙事待展开） | {counts.get("中等", 0)} |')
    L.append(f'| 🔴 薄（数据待补） | {counts.get("薄", 0)} |')
    L.append(f'| **龙头级合计** | **{len(rows)}** |')
    L.append('')
    L.append(f'## 🔴 薄 —— {len(thin)} 家（优先处理，字段都还没填齐）')
    L.append('')
    L.append('按赛道内营收占比（`rev`）降序。')
    L.append('')
    L.append('| 公司 | 字段 | body段 | rev | 赛道数 | 龙头定位 |')
    L.append('|------|:--:|:--:|:--:|:--:|------|')
    for n, u, _ in thin:
        d = depth[n]
        lead = u['lead'][0] if u['lead'] else f"chain_role={d['chain_role']}"
        L.append(f"| **{n}** | {d['fields']}/25 | {d['sections']} | {u['rev']} | "
                 f"{len(u['segments'])} | {lead} |")
    L.append('')
    L.append(f'## ⚠️ 中等 —— {len(mid)} 家（字段齐全，需补叙事章节）')
    L.append('')
    L.append('| 公司 | 字段 | body段 | rev | 赛道数 |')
    L.append('|------|:--:|:--:|:--:|:--:|')
    for n, u, _ in mid:
        d = depth[n]
        L.append(f"| {n} | {d['fields']}/25 | {d['sections']} | {u['rev']} | {len(u['segments'])} |")
    L.append('')
    L.append('## 推进方式')
    L.append('')
    L.append('- **薄**：属于「Research 模式」——多源 Web 调研 → L0 归档 → 补 24 字段')
    L.append('  + 5 body 段。参考 `L1-Schema与Pipeline/collector/` 的流程，'
             '可参照此前「骨架补全批次」的做法分批并行。')
    L.append('- **中等**：字段已在，只需把已有信息展开成章节（`业务板块详解` /')
    L.append('  `技术路线图` / `竞争护城河` / `研发投入` 等），不必重新调研。')
    L.append('')
    L.append('---')
    L.append('')
    L.append('## 复现方式')
    L.append('')
    L.append('```bash')
    L.append('python3 L1-Schema与Pipeline/lint/list_deepening_targets.py          # 摘要')
    L.append('python3 L1-Schema与Pipeline/lint/list_deepening_targets.py --write  # 重新生成本文件')
    L.append('```')
    L.append('')
    L.append('判据可通过脚本顶部的 `FULL_FIELDS` / `FULL_SECTIONS` / `THIN_FIELDS` /')
    L.append('`LEAD_MARKERS` 调整。')
    L.append('')
    return '\n'.join(L)


def main():
    depth, targets = collect()
    text = render(depth, targets)
    counts = collections.Counter(tier(depth, n) for n in targets)
    print(f"龙头级公司 {len(targets)} 家："
          f"全面 {counts.get('全面',0)} / 中等 {counts.get('中等',0)} / 薄 {counts.get('薄',0)}")
    if '--write' in sys.argv:
        OUT.parent.mkdir(exist_ok=True)
        OUT.write_text(text, encoding='utf-8')
        print(f"✅ 已写入 {OUT.relative_to(ROOT)}")
    else:
        print("（未写入。加 --write 落盘）")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
