#!/usr/bin/env python3
"""L2-Wiki MD → L3 wiki_data.json 编译脚本。

读取 L2-Wiki/ 下所有 .md 词条，通过 engine/parser.py 解析 YAML frontmatter
和 [[wikilink]]，结合 engine/graph.py 构建 ECharts 图数据，输出为
index.html 所需的 wiki_data.json。

用法:
    cd /path/to/invest_wiki
    python L3-网页产物/build_wiki_data.py

输出:
    L3-网页产物/wiki_data.json（474 条实体 + 图数据）
"""

import json
import os
import re
import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中，以便 import engine
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from engine.parser import WikiParser
from engine.graph import GraphBuilder


# ---------------------------------------------------------------------------
# 字段映射 & 正文解析
# ---------------------------------------------------------------------------

def parse_layer(raw) -> int:
    """将 'L3' 或 3 统一为 int。"""
    if isinstance(raw, int):
        return raw
    if isinstance(raw, str):
        m = re.match(r'L?(\d+)', raw.strip())
        if m:
            return int(m.group(1))
    return 0


def parse_body_sections(body: str) -> dict:
    """从 MD 正文中提取结构化字段。

    正文结构（以 gpu.md 为例）:
        # GPU
        > **AI算力** · L3 · ...

        <description text, possibly multi-paragraph with | separators>

        ---

        ## 核心数据
        | ... |

        ## 关联
        ...

        ## 竞争格局
        <competition text>

        ## 关键趋势
        <key_trends text>

        ## 价格传导
        <price_conduction text>

        ## 数据来源
        <sources text>
    """
    result = {
        'description': '',
        'competition': '',
        'key_trends': '',
        'price_conduction': '',
        'sources': '',
    }

    # 去掉开头的 "# Title" 和 "> **industry**..." 行，取描述
    # 描述 = 标题后的文本，直到 --- 或下一个 ## 标题
    cleaned = body.strip()

    # 跳过 # Title 行
    cleaned = re.sub(r'^#\s+.+?\n', '', cleaned, count=1)

    # 去掉标题行后的空白，再跳过 > blockquote 行（industry · layer · TAM ...）
    cleaned = cleaned.lstrip('\n')
    cleaned = re.sub(r'^>\s+.+?\n', '', cleaned, count=1)

    # 现在 cleaned 开头就是描述 + 后续 section
    # 找到第一个 --- 或 ## 的位置
    sec_match = re.search(r'\n---\s*\n|\n##\s', cleaned)
    if sec_match:
        desc_text = cleaned[:sec_match.start()].strip()
        remainder = cleaned[sec_match.start():]
    else:
        desc_text = cleaned.strip()
        remainder = ''

    result['description'] = desc_text

    # 从 remainder 中提取各 section
    sections = _split_sections(remainder)
    result['competition'] = sections.get('竞争格局', '')
    result['key_trends'] = sections.get('关键趋势', '')
    result['price_conduction'] = sections.get('价格传导', '')
    result['sources'] = sections.get('数据来源', '')

    return result


def _split_sections(text: str) -> dict:
    """将 MD 正文按 ## 标题拆分为 {标题: 内容} 字典。"""
    sections = {}
    # 匹配 ## 标题行
    pattern = re.compile(r'^##\s+(.+?)\s*$', re.MULTILINE)
    matches = list(pattern.finditer(text))

    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        # 去掉 section 内部的子标题（###）但保留文本
        sections[title] = content

    return sections


def _map_concept_sections(raw_sections: dict) -> dict:
    """将概念 MD 的 ## 标题映射到标准 body_ key。

    概念 MD 标题格式：「一、生活化类比：xxx」或「生活化类比」。
    去掉序号前缀和冒号后缀，匹配到标准 key。
    """
    mapping = {
        '生活化类比': 'body_analogy',
        '专业但通俗的定义': 'body_definition',
        '为什么市场会关注它': 'body_market_attention',
        '产业链位置': 'body_chain_position',
        '相关公司和板块': 'body_companies',
        '投资关注点': 'body_investment_focus',
        '风险提示': 'body_risks',
        '如何判断是真逻辑还是炒概念': 'body_real_vs_hype',
        '后续追踪指标': 'body_tracking',
        '相关概念链接': 'body_related_links',
    }
    result = {}
    for raw_title, content in raw_sections.items():
        # Strip 序号 prefix like "一、"
        cleaned = re.sub(r'^[一二三四五六七八九十]+、', '', raw_title).strip()
        # Strip subtitle after colon like "：快递驿站升级版..."
        cleaned = cleaned.split('：')[0].split(':')[0].strip()
        for pattern, key in mapping.items():
            if pattern in cleaned:
                result[key] = content.strip()
                break
    return result


def _auto_derive_supply_chain(entities: list):
    """根据 wikilinks + layer 比较，为 segment 自动补全 key_inputs / key_customers。

    仅对 YAML 中未显式填写的 entity 生效（避免覆盖手工数据）。
    逻辑：linked layer < current layer → 上游；linked layer > current layer → 下游。
    """
    # 构建 name → entity dict 的快速 lookup
    name_lookup = {e['name']: e for e in entities if e.get('type') in ('segment', 'company')}

    for e in entities:
        if e.get('type') != 'segment':
            continue
        # 只补全未填写的字段
        has_inputs = bool(e.get('key_inputs'))
        has_customers = bool(e.get('key_customers'))
        if has_inputs and has_customers:
            continue

        current_layer = e.get('layer', 0)
        upstream = []
        downstream = []

        for wl_name in e.get('wikilinks', []):
            target = name_lookup.get(wl_name)
            if not target:
                continue
            target_layer = target.get('layer', 0)
            if target_layer <= 0 or current_layer <= 0:
                continue
            if target_layer < current_layer:
                upstream.append(wl_name)
            elif target_layer > current_layer:
                downstream.append(wl_name)

        if not has_inputs and upstream:
            e['key_inputs'] = upstream
        if not has_customers and downstream:
            e['key_customers'] = downstream


# ---------------------------------------------------------------------------
# 实体转换
# ---------------------------------------------------------------------------

def entity_to_dict(entity, max_tam: float, max_backlinks: int) -> dict:
    """将 WikiParser Entity 转换为前端所需的 dict 格式。"""
    fm = entity.frontmatter

    # 解析 body sections
    body_sections = parse_body_sections(entity.content)

    tam = float(fm.get('tam_bn', 0))
    cagr = float(fm.get('cagr_pct', 0))
    backlinks = entity.backlink_count
    layer = parse_layer(fm.get('layer', 0))

    # 计算综合热度分
    tam_score = (tam / max_tam * 60) if max_tam > 0 else 0
    bl_score = (backlinks / max_backlinks * 40) if max_backlinks > 0 else 0
    heat = round(tam_score + bl_score, 1)

    # 构建 content（简短预览，用于列表展示）
    desc = body_sections['description']
    content_preview = f"# {entity.name}\n\n> **{fm.get('industry', '')}** · L{layer} · TAM **${tam}B** · CAGR **{cagr}%**\n\n{desc[:200]}"

    # Handle thesis type differently
    if entity.entity_type == 'thesis':
        return thesis_to_dict(entity)

    # Handle concept type differently
    if entity.entity_type == 'concept':
        return concept_to_dict(entity)

    # Handle company type differently
    if entity.entity_type == 'company':
        return company_to_dict(entity)

    # Structured fields: prefer YAML structured format, fallback to body string parsing
    def get_structured(field_name):
        """Get field from YAML (new structured format) or body (old string format)."""
        yaml_val = fm.get(field_name)
        body_val = body_sections.get(field_name, '')
        if yaml_val is not None and yaml_val != '':
            return yaml_val
        return body_val

    result = {
        'name': entity.name,
        'slug': entity.slug,
        'type': entity.entity_type,
        'industry': fm.get('industry', ''),
        'layer': layer,
        'tam': tam,
        'cagr': cagr,
        'margin': fm.get('margin', ''),
        'backlinks': backlinks,
        'wikilinks': entity.wikilinks,
        'content': content_preview,
        '_heat': heat,
        'description': desc,
        'cost_share_pct': fm.get('cost_share_pct'),
        'cost_share_context': fm.get('cost_share_context', ''),
        'profit_pool_pct': fm.get('profit_pool_pct'),
        'profit_pool_context': fm.get('profit_pool_context', ''),
        'price_conduction': get_structured('price_conduction'),
        'competition': get_structured('competition'),
        'key_trends': get_structured('key_trends'),
        'sources': get_structured('sources'),
        'key_inputs': get_structured('key_inputs'),
        'key_customers': get_structured('key_customers'),
        'value_add': fm.get('value_add', ''),
        'companies': fm.get('companies', []),
        'contradictions': fm.get('contradictions', []),
        'related_theses': fm.get('related_theses', []),
        'updated': fm.get('updated', ''),
    }

    return result


def _parse_thesis_evidence(text: str) -> list:
    """解析 thesis 证据文本为结构化数组。

    输入格式（field-formats.md §7）:
        1. 证据内容描述
           ——来源: 来源标题
           (URL或内部路径)

    输出: [{"content": "...", "source_title": "...", "source_url": "..."}, ...]
    若无法解析，返回原始文本包装的单元素数组。
    """
    if not text or not text.strip():
        return []
    results = []
    # Split by numbered items: "1. " or "1) " at line start
    parts = re.split(r'\n(?=\d+[.)]\s)', text.strip())
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Remove leading number
        part = re.sub(r'^\d+[.)]\s*', '', part)
        lines = part.split('\n')
        content = lines[0].strip()
        source_title = ''
        source_url = ''
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('——来源:') or line.startswith('——来源：') or line.startswith('--来源:') or line.startswith('--来源：'):
                source_title = line.split(':', 1)[-1].strip().lstrip('：')
            elif line.startswith('(') and line.endswith(')'):
                source_url = line[1:-1].strip()
        if content:
            results.append({'content': content, 'source_title': source_title, 'source_url': source_url})
    return results if results else [{'content': text.strip(), 'source_title': '', 'source_url': ''}]


def _parse_thesis_assumptions(text: str) -> list:
    """解析待验证假设为字符串数组。

    输入: "- 假设1：内容" 或 "1. 内容" 每行一条
    输出: ["假设1：内容", ...]
    """
    if not text or not text.strip():
        return []
    results = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        # Remove leading "- " or "1. " or "1) "
        line = re.sub(r'^[-•]\s*', '', line)
        line = re.sub(r'^\d+[.)]\s*', '', line)
        if line:
            results.append(line)
    return results


def _parse_thesis_sources(text: str) -> list:
    """解析 thesis 来源文本为结构化数组。

    输入格式（与赛道 sources 3行格式类似）:
        - 来源标题
          摘要内容
          (URL或内部路径)

    输出: [{"title": "...", "summary": "...", "url": "..."}, ...]
    """
    if not text or not text.strip():
        return []
    results = []
    # Split by "- " at line start (each source block)
    blocks = re.split(r'\n(?=- )', text.strip())
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        lines = block.split('\n')
        title = lines[0].strip().lstrip('- ').strip()
        summary = ''
        url = ''
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('(') and line.endswith(')'):
                url = line[1:-1].strip()
            elif line and not line.startswith('('):
                if summary:
                    summary += '\n' + line
                else:
                    summary = line
        if title:
            results.append({'title': title, 'summary': summary, 'url': url})
    return results


def thesis_to_dict(entity) -> dict:
    """将 thesis 类型的 Entity 转换为前端格式。"""
    fm = entity.frontmatter
    body_sections = _split_sections(entity.content)

    claim = body_sections.get('核心主张', '') or ''
    # Extract first paragraph of 核心主张 as one-liner
    claim_brief = claim.split('\n')[0].strip() if claim else ''

    # Parse evidence sections into structured arrays
    evidence_for_raw = body_sections.get('支撑证据', '')
    evidence_against_raw = body_sections.get('反对证据', '')
    assumptions_raw = body_sections.get('待验证假设', '')
    sources_raw = body_sections.get('来源', '')

    evidence_for = _parse_thesis_evidence(evidence_for_raw)
    evidence_against = _parse_thesis_evidence(evidence_against_raw)
    assumptions = _parse_thesis_assumptions(assumptions_raw)
    sources = _parse_thesis_sources(sources_raw)

    return {
        'name': entity.name,
        'slug': entity.slug,
        'type': 'thesis',
        'thesis_status': fm.get('thesis_status', 'forming'),
        'confidence': fm.get('confidence', 5),
        'created': fm.get('created', ''),
        'updated': fm.get('updated', ''),
        'affected_segments': fm.get('affected_segments', []),
        'affected_companies': fm.get('affected_companies', []),
        'tags': fm.get('tags', []),
        'claim': claim_brief,
        'claim_full': claim,
        'evidence_for': evidence_for,
        'evidence_against': evidence_against,
        'assumptions': assumptions,
        'update_log': body_sections.get('更新日志', ''),
        'sources': sources,
        'description': claim_brief,  # for compatibility
        'wikilinks': entity.wikilinks,
        'content': entity.content,  # full body for rendering
    }


def company_to_dict(entity) -> dict:
    """将 company 类型的 Entity 转换为前端格式。"""
    fm = entity.frontmatter
    body_sections = parse_body_sections(entity.content)

    one_liner = fm.get('one_liner', '')
    desc = body_sections.get('description', '') or fm.get('description', '')

    # Build content preview for search cards
    parts = [one_liner] if one_liner else []
    if desc:
        parts.append(desc[:150])
    content_preview = f"# {entity.name}\n\n> {' | '.join(parts)}" if parts else f"# {entity.name}"

    # Full MD body (去掉 YAML frontmatter 后) for detail page rendering
    full_body = entity.content if entity.content else content_preview

    return {
        'name': entity.name,
        'slug': entity.slug,
        'type': 'company',
        'country': fm.get('country', ''),
        'ticker': fm.get('ticker', ''),
        'one_liner': one_liner,
        'description': desc,
        'core_business': fm.get('core_business', []),
        'revenue_model': fm.get('revenue_model', ''),
        'founded': fm.get('founded'),
        'headquarters': fm.get('headquarters', ''),
        'employees': fm.get('employees', ''),
        'latest_revenue': fm.get('latest_revenue', ''),
        'market_cap': fm.get('market_cap', ''),
        'data_freshness_date': str(fm.get('data_freshness_date', '')),
        'industry': fm.get('industry', ''),
        'segments': fm.get('segments', []),
        'chain_layer': fm.get('chain_layer', ''),
        'chain_role': fm.get('chain_role', ''),
        'suppliers': fm.get('suppliers', []),
        'customers': fm.get('customers', []),
        'partners': fm.get('partners', []),
        'competitors': fm.get('competitors', []),
        'tags': fm.get('tags', []),
        'website': fm.get('website', ''),
        'backlinks': entity.backlink_count,
        'wikilinks': entity.wikilinks,
        'content': full_body,
        'content_preview': content_preview,
        'sources': body_sections.get('sources', '') or fm.get('sources', ''),
    }


def concept_to_dict(entity) -> dict:
    """将 concept 类型的 Entity 转换为前端格式。"""
    fm = entity.frontmatter
    body_sections = _map_concept_sections(_split_sections(entity.content))

    # Parse related_concepts from YAML
    related = fm.get('related_concepts', [])
    if isinstance(related, list):
        related_concepts = related
    else:
        related_concepts = []

    # Build content preview: one_liner
    one_liner = fm.get('one_liner', '')
    content_preview = f"# {entity.name}\n\n> {one_liner} | {fm.get('category', '')} · {fm.get('difficulty', '')}级"

    return {
        'name': entity.name,
        'slug': entity.slug,
        'type': 'concept',
        'category': fm.get('category', ''),
        'difficulty': fm.get('difficulty', ''),
        'confidence': fm.get('confidence', ''),
        'one_liner': one_liner,
        'fable_title': fm.get('fable_title', ''),
        'heat': fm.get('heat', ''),
        'tags': fm.get('tags', []),
        'affected_segments': fm.get('affected_segments', []),
        'affected_companies': fm.get('affected_companies', []),
        'related_concepts': related_concepts,
        'backlinks': entity.backlink_count,
        'wikilinks': entity.wikilinks,
        'content': content_preview,
        'description': one_liner,  # for compatibility
        # 11 body modules (keys already mapped by _map_concept_sections)
        'body_analogy': body_sections.get('body_analogy', ''),
        'body_definition': body_sections.get('body_definition', ''),
        'body_market_attention': body_sections.get('body_market_attention', ''),
        'body_chain_position': body_sections.get('body_chain_position', ''),
        'body_companies': body_sections.get('body_companies', ''),
        'body_investment_focus': body_sections.get('body_investment_focus', ''),
        'body_risks': body_sections.get('body_risks', ''),
        'body_real_vs_hype': body_sections.get('body_real_vs_hype', ''),
        'body_tracking': body_sections.get('body_tracking', ''),
        'body_related_links': body_sections.get('body_related_links', ''),
        'updated': fm.get('updated', ''),
    }


# ---------------------------------------------------------------------------
# 主编译流程
# ---------------------------------------------------------------------------

def build(wiki_dir: str, output_path: str):
    """主编译：解析 Wiki → 构建图数据 → 输出 JSON。"""
    wiki_path = Path(wiki_dir)
    if not wiki_path.exists():
        print(f'❌ Wiki 目录不存在: {wiki_dir}')
        sys.exit(1)

    # 1. 解析所有词条
    print(f'📖 解析 Wiki 词条: {wiki_dir}')
    parser = WikiParser(str(wiki_path))
    parser.parse_all()
    print(f'   ✅ {len(parser.entities)} 个词条')

    # 按类型统计
    by_type = {}
    for e in parser.entities.values():
        by_type[e.entity_type] = by_type.get(e.entity_type, 0) + 1
    for t, c in sorted(by_type.items()):
        print(f'      {t}: {c}')

    # 2. 计算热度排序所需的最大值
    segments = [e for e in parser.entities.values() if e.entity_type == 'segment']
    max_tam = max((float(e.frontmatter.get('tam_bn', 0)) for e in segments), default=1)
    max_backlinks = max((e.backlink_count for e in segments), default=1)

    # 3. 转换实体
    entities = [entity_to_dict(e, max_tam, max_backlinks)
                for e in parser.entities.values()]

    # 3.5 自动推导 key_inputs / key_customers
    # 对于未在 YAML 中显式填写的 segment，根据 wikilinks + layer 比较自动推导
    _auto_derive_supply_chain(entities)

    # 3.6 清理 wikilinks：过滤非实体引用（消化笔记、别名等）
    _valid_names = {e['name'] for e in entities if e.get('type') in ('segment', 'company', 'concept', 'thesis')}
    # 名称映射：body 中可能使用简称
    _name_aliases = {
        '光模块': '光模块(800G/1.6T)',
        '晶圆代工': '晶圆代工(先进制程)',
        '先进封装': '先进封装(CoWoS/3D)',
    }
    for e in entities:
        wl = e.get('wikilinks', [])
        if not wl:
            continue
        cleaned = []
        for w in wl:
            # 过滤消化笔记、文件路径等非实体引用
            if '消化笔记' in w or w.startswith('L0-') or w.startswith('L2-'):
                continue
            # 映射别名到正式名称
            if w in _name_aliases:
                w = _name_aliases[w]
            # 只保留已知实体名
            if w in _valid_names:
                cleaned.append(w)
        if len(cleaned) != len(wl):
            e['wikilinks'] = cleaned

    # 4. 构建图数据
    gb = GraphBuilder(parser)

    treemap_ai = gb.build_treemap('AI算力')
    treemap_semi = gb.build_treemap('半导体')
    graph_data = gb.build_graph()
    sankey_ai = gb.build_sankey('AI算力')
    sankey_semi = gb.build_sankey('半导体')

    # 5. 热度排行榜
    hot_segments = gb.build_heatmap()
    hot = []
    for s in hot_segments[:30]:
        tam = float(s.frontmatter.get('tam_bn', 0))
        hot.append({
            'name': s.name,
            'score': round(s._heat_score, 1),
            'tam': tam,
            'backlinks': s.backlink_count,
        })

    # 6. 组装输出
    # Build thesis index: segment_slug → [thesis entities]
    thesis_index = {}
    for e in parser.entities.values():
        if e.entity_type == 'thesis':
            for seg_slug in e.frontmatter.get('affected_segments', []):
                thesis_index.setdefault(seg_slug, []).append(e.slug)

    # Build concept index: segment_slug → [concept entities]
    concept_index = {}
    for e in parser.entities.values():
        if e.entity_type == 'concept':
            for seg_slug in e.frontmatter.get('affected_segments', []):
                concept_index.setdefault(seg_slug, []).append(e.slug)

    output = {
        'total': len(entities),
        'by_type': by_type,
        'entities': entities,
        'treemap_ai': treemap_ai,
        'treemap_semi': treemap_semi,
        'graph': graph_data,
        'sankey_ai': sankey_ai,
        'sankey_semi': sankey_semi,
        'hot': hot,
        'thesis_index': thesis_index,
        'concept_index': concept_index,
    }

    # 7. 写入 JSON
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    file_size = out_path.stat().st_size
    print(f'\n✅ 编译完成 → {output_path}')
    print(f'   📦 {len(entities)} 实体, {file_size / 1024:.0f} KB')

    # 8. 简要统计
    print(f'\n📊 统计:')
    print(f'   Treemap AI: {len(treemap_ai)} 节点')
    print(f'   Treemap 半导体: {len(treemap_semi)} 节点')
    print(f'   Graph: {len(graph_data["nodes"])} 节点, {len(graph_data["edges"])} 边')
    print(f'   Hot Top30: {hot[0]["name"]}({hot[0]["score"]}分) ~ {hot[-1]["name"]}({hot[-1]["score"]}分)')


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    wiki_dir = os.environ.get('WIKI_DIR', str(PROJECT_ROOT / 'L2-Wiki'))
    output_path = os.environ.get('OUTPUT_JSON', str(PROJECT_ROOT / 'L3-网页产物' / 'wiki_data.json'))

    print(f'🔨 Invest Wiki Build — L2 → L3')
    print(f'   Wiki: {wiki_dir}')
    print(f'   输出: {output_path}')
    print()
    build(wiki_dir, output_path)
