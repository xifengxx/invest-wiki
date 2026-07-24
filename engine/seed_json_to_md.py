"""一次性迁移：JSON种子 → Obsidian Markdown Wiki 词条
用法: python invest_kg/seed_json_to_md.py
"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
SEED = os.path.join(BASE, 'data', 'seed')
WIKI = os.path.join(BASE, 'data', 'wiki')

def load_json(name):
    with open(os.path.join(SEED, name)) as f:
        return json.load(f)

def slugify(text):
    return re.sub(r'[^\w一-鿿-]', '', text.replace(' ', '-').replace('/', '-'))

def write_md(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def segment_to_md(seg, industry_name, all_seg_names):
    """赛道JSON → Markdown词条"""
    slug = seg.get('slug', slugify(seg['name']))

    # 构建关联链接
    links = []
    if seg.get('key_inputs'):
        for item in seg['key_inputs'].split(','):
            item = item.strip()
            if item in all_seg_names:
                links.append(f"- 上游: [[{item}]]")
    if seg.get('key_customers'):
        for item in seg['key_customers'].split(','):
            item = item.strip()
            if item in all_seg_names:
                links.append(f"- 下游: [[{item}]]")

    md = f"""---
name: "{seg['name']}"
slug: "{slug}"
industry: "{industry_name}"
layer: L{seg.get('layer_level', '?')}
tam_bn: {seg.get('tAM_bn', 'N/A')}
cagr_pct: {seg.get('cagr_pct', 'N/A')}
margin: "{seg.get('margin_profile', 'N/A')}"
cost_share_pct: {seg.get('cost_share_pct', 'N/A')}
cost_share_context: "{seg.get('cost_share_context', '')}"
profit_pool_pct: {seg.get('profit_pool_pct', 'N/A')}
profit_pool_context: "{seg.get('profit_pool_context', '')}"
value_add: "{seg.get('value_add', '')}"
updated: "2026-07"
type: "segment"
tags: ["{industry_name}", "L{seg.get('layer_level', '?')}"]
---

# {seg['name']}

> **{industry_name}** · L{seg.get('layer_level', '?')} · TAM **${seg.get('tAM_bn', 'N/A')}B** · CAGR **{seg.get('cagr_pct', 'N/A')}%**

{seg.get('description', '无描述')}

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | ${seg.get('tAM_bn', 'N/A')}B |
| 年复合增长率(CAGR) | {seg.get('cagr_pct', 'N/A')}% |
| 利润率区间 | {seg.get('margin_profile', 'N/A')} |
| 成本占比 | {seg.get('cost_share_pct', 'N/A')}% ({seg.get('cost_share_context', '')}) |
| 利润池占比 | {seg.get('profit_pool_pct', 'N/A')}% ({seg.get('profit_pool_context', '')}) |
| 附加值 | {seg.get('value_add', '')} |

## 关联

{chr(10).join(links) if links else '（待补充）'}

## 竞争格局

{seg.get('competition_landscape', '（待补充）')}

## 关键趋势

{seg.get('key_trends', '（待补充）')}

## 价格传导

{seg.get('price_conduction', '（待补充）')}

## 数据来源

{seg.get('research_evidence', '（待补充）')}
"""
    return slug, md

def company_to_md(co, all_seg_names):
    """公司JSON → Markdown词条"""
    slug = co.get('slug', slugify(co['name']))
    md = f"""---
name: "{co['name']}"
slug: "{slug}"
country: "{co.get('country', '')}"
type: "company"
updated: "2026-07"
---

# {co['name']}

{co.get('description', '')}

## 基本信息
- 国家: {co.get('country', 'N/A')}
- 网站: {co.get('website', 'N/A')}
"""
    return slug, md

def migrate():
    print("=== JSON → MD 迁移 ===\n")
    stats = {'segments': 0, 'companies': 0, 'industries': 0}

    # 1. 产业定义
    industries = load_json('industries.json')
    for ind in industries:
        md = f"""---
name: "{ind['name']}"
slug: "{ind.get('slug', '')}"
type: "industry"
description: "{ind.get('description', '')}"
---

# {ind['name']}

{ind.get('description', '')}
"""
        write_md(os.path.join(WIKI, '产业', f"{ind['name']}.md"), md)
        stats['industries'] += 1

    # 2. 收集所有赛道名（用于wiki链接）
    all_segs = []
    for fname in ['ai_segments.json', 'semiconductor_segments.json']:
        all_segs.extend(load_json(fname))
    all_seg_names = {s['name'] for s in all_segs}

    # 3. 赛道
    print("迁移赛道...")
    for fname, industry in [('ai_segments.json', 'AI算力'), ('semiconductor_segments.json', '半导体')]:
        segs = load_json(fname)
        for seg in segs:
            slug, md = segment_to_md(seg, industry, all_seg_names)
            path = os.path.join(WIKI, '赛道', industry, f"{slug}.md")
            write_md(path, md)
            stats['segments'] += 1
        print(f"  {industry}: {len(segs)} 个赛道")

    # 4. 公司
    print("迁移公司...")
    for fname in ['ai_companies.json', 'semiconductor_companies.json']:
        companies = load_json(fname)
        for co in companies:
            slug, md = company_to_md(co, all_seg_names)
            path = os.path.join(WIKI, '公司', f"{slug}.md")
            write_md(path, md)
            stats['companies'] += 1
        print(f"  {fname}: {len(companies)} 家公司")

    print(f"\n=== 迁移完成 ===")
    print(f"  产业: {stats['industries']}")
    print(f"  赛道: {stats['segments']}")
    print(f"  公司: {stats['companies']}")
    print(f"  输出: {WIKI}")

if __name__ == '__main__':
    migrate()
