#!/usr/bin/env python3
"""从赛道源文件生成 L2-Wiki/index.md 的赛道清单与统计数字。

**只重写"可派生"的部分**，人工内容原样保留：

  自动生成 → 两个产业分节（`## AI算力（N 赛道）` / `## 半导体（N 赛道）`）
             及其下的赛道登记行、`## 统计` 表的 6 个数字、顶部计数行
  人工保留 → `## 投资论点` 段（其中 6 条摘要是人工改写，L2 源文件里搜不到原文）、
             `## 维护记录` 表、`> 质量版本`、`> LLM 查询路由` 提示行、
             `## 统计` 表里"赛道总数"一行的长注释

背景：这些内容 100% 可从源文件派生（本脚本已对现有 67 个赛道逐条复现验证），
但一直手工维护，历史上至少漂移过 3 次（最近一次是 2026-09-13 覆铜板的 TAM/CAGR）。

用法：
    python3 L1-Schema与Pipeline/lint/gen_index.py            # dry-run，只打印差异
    python3 L1-Schema与Pipeline/lint/gen_index.py --write    # 落盘
"""
import glob
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'L3-网页产物'))

from build_wiki_data import parse_layer  # noqa: E402  复用编译器的 layer 归一化

WIKI_DIR = ROOT / 'L2-Wiki'
INDEX_MD = WIKI_DIR / 'index.md'

BEGIN = '<!-- GEN:SEGMENTS:BEGIN 由 gen_index.py 生成，勿手工编辑 -->'
END = '<!-- GEN:SEGMENTS:END -->'

INDUSTRIES = ['AI算力', '半导体']
LAYER_LABELS = {
    1: 'L1 基础与材料层 — 芯片IP/EDA/设备/材料/硅片等最上游',
    2: 'L2 核心组件层 — Chiplet/互联/封装/存储/电源等中间组件',
    3: 'L3 算力与平台层 — GPU/ASIC/服务器/网络/云平台等算力核心',
    4: 'L4 应用与方案层 — MCU/传感器/自动驾驶/AI应用等终端',
}
# 统计表里各行的标签 → 取值方式
STAT_ROWS = [
    ('赛道总数', 'sections'),   # 特殊：赛道清单的生成行数（含双归属重复）
    ('产业', 'industries'),
    ('公司', 'companies'),
    ('概念', 'concepts'),
    ('论点', 'theses'),
    ('消化笔记', 'digests'),
]


def num(v) -> str:
    """15.0 → '15'；19.1 → '19.1'（与 index.md 既有写法一致）"""
    return f"{float(v):g}"


def first_paragraph(body: str) -> str:
    """正文首段（跳过 `# 标题` 与 `> 引用` 行），去掉全部空白字符。"""
    for line in body.split('\n'):
        s = line.strip()
        if s and not s.startswith(('#', '>')):
            return re.sub(r'\s+', '', s)
    return ''


def load_segments():
    segs = []
    for path in glob.glob(str(WIKI_DIR / '赛道' / '*' / '*.md')):
        txt = Path(path).read_text(encoding='utf-8')
        parts = txt.split('---', 2)
        if len(parts) < 3:
            continue
        fm = yaml.safe_load(parts[1]) or {}
        if fm.get('type') != 'segment':
            continue
        inds = fm.get('industries') or ([fm['industry']] if fm.get('industry') else [])
        segs.append({
            'name': fm.get('name', ''),
            'slug': fm.get('slug', ''),
            'layer': parse_layer(fm.get('layer', 1)),
            'tam': float(fm.get('tam_bn', 0)),
            'cagr': float(fm.get('cagr_pct', 0)),
            'summary': first_paragraph(parts[2])[:40],
            'industries': inds,
        })
    return segs


def render_entry(s, industry) -> str:
    t, c = num(s['tam']), num(s['cagr'])
    title = (f"- **[[{s['name']}]]** ({s['slug']}) — > **{industry}** · "
             f"L{s['layer']} · TAM **${t}B** · CAGR **{c}%**")
    summary = f"{s['summary']}... [TAM ${t}B, CAGR {c}%]"
    return f"{title}\n{summary}"


def render_sections(segs) -> tuple:
    """返回 (生成文本, 每个产业的赛道行数)。"""
    out, counts = [], {}
    for industry in INDUSTRIES:
        in_ind = [s for s in segs if industry in s['industries']]
        counts[industry] = len(in_ind)
        out.append(f"## {industry}（{len(in_ind)} 赛道）")
        out.append('')
        for layer in sorted(LAYER_LABELS):
            layer_segs = sorted([s for s in in_ind if s['layer'] == layer],
                                key=lambda x: -x['tam'])
            if not layer_segs:
                continue
            # 版面约定：每个标题后恰好一个空行；`### ` 前**不**留空行
            out.append(f"### {LAYER_LABELS[layer]}")
            out.append('')
            for s in layer_segs:
                out.append(render_entry(s, industry))
        if industry != INDUSTRIES[-1]:
            out.append('---')
            out.append('')
    while out and out[-1] == '':
        out.pop()
    return '\n'.join(out), counts


def count_files(sub: str) -> int:
    return len([f for f in os.listdir(WIKI_DIR / sub)
                if f.endswith('.md') and 'audit' not in f.lower()])


def update_numbers(text: str, segs, counts) -> str:
    total_unique = len({s['name'] for s in segs})
    vals = {
        '赛道总数': total_unique,   # 统计表记唯一数；分节内的 44/39 已含双归属重复
        '产业': len(INDUSTRIES),
        '公司': count_files('公司'),
        '概念': count_files('概念'),
        '论点': count_files('论点'),
        '消化笔记': count_files('消化笔记'),
    }
    for label, _ in STAT_ROWS:
        text = re.sub(rf'(\| {label} \| )\d+', rf'\g<1>{vals[label]}', text, count=1)
    # 顶部计数行
    text = re.sub(r'赛道总数：\d+', f'赛道总数：{total_unique}', text, count=1)
    text = re.sub(r'公司总数：\d+', f'公司总数：{vals["公司"]}', text, count=1)
    text = re.sub(r'概念总数：\d+', f'概念总数：{vals["概念"]}', text, count=1)
    text = re.sub(r'论点总数：\d+', f'论点总数：{vals["论点"]}', text, count=1)
    text = re.sub(r'最后更新：\d{4}-\d{2}-\d{2}',
                  f'最后更新：{__import__("datetime").date.today().isoformat()}', text, count=1)
    return text


def regenerate(text: str, segs):
    block, counts = render_sections(segs)
    body = f"{BEGIN}\n{block}\n{END}"

    if BEGIN in text and END in text:
        new = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END), lambda _: body,
                     text, count=1, flags=re.DOTALL)
    else:
        # 首次运行：用结构锚点定位（`## AI算力` 到 `## 统计` 前）
        m = re.search(r'^## AI算力.*?(?=^## 统计)', text, re.DOTALL | re.MULTILINE)
        if not m:
            raise SystemExit('❌ 无法在 index.md 中定位赛道清单区（找不到 "## AI算力" 到 "## 统计"）')
        new = text[:m.start()] + body + '\n\n---\n\n' + text[m.end():]
    return update_numbers(new, segs, counts), counts


def main():
    write = '--write' in sys.argv
    segs = load_segments()
    if not segs:
        raise SystemExit('❌ 没读到任何赛道源文件')
    old = INDEX_MD.read_text(encoding='utf-8')
    new, counts = regenerate(old, segs)

    print(f"📋 读到 {len(segs)} 个唯一赛道；生成行数 "
          f"{counts['AI算力']}(AI算力) + {counts['半导体']}(半导体) = {sum(counts.values())}")

    if new == old:
        print("✅ index.md 已是最新，无需改动")
        return 0

    import difflib
    diff = list(difflib.unified_diff(old.split('\n'), new.split('\n'),
                                     'index.md(现有)', 'index.md(生成)', lineterm='', n=1))
    print(f"\n{'─'*56}\n差异 {len([d for d in diff if d.startswith(('+','-')) and not d.startswith(('+++','---'))])} 行：")
    for line in diff[:60]:
        print('  ' + line)
    if len(diff) > 60:
        print(f"  … 还有 {len(diff)-60} 行")

    if write:
        INDEX_MD.write_text(new, encoding='utf-8')
        print(f"\n✅ 已写入 {INDEX_MD}")
    else:
        print("\n（dry-run，未写入。加 --write 落盘）")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
