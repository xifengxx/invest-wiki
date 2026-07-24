"""Wiki 图数据构建 — Entity → ECharts JSON。"""
from typing import Dict, List
from .parser import WikiParser, Entity

LAYER_COLORS = {
    1: '#94a3b8',
    2: '#60a5fa',
    3: '#4ade80',
    4: '#fb923c',
}

TYPE_COLORS = {
    'industry': '#1D1D1F',
    'segment': '#0071E3',
    'company': '#34C759',
    'concept': '#AF52DE',
    'person': '#FF9500',
    'event': '#FF3B30',
}

class GraphBuilder:
    """Wiki 词条 → ECharts 图数据"""

    def __init__(self, parser: WikiParser):
        self.parser = parser

    def build_treemap(self, industry: str = None) -> List[Dict]:
        """构建 Treemap 数据（按 TAM 面积）"""
        segments = [e for e in self.parser.entities.values()
                    if e.entity_type == 'segment']
        if industry:
            segments = [s for s in segments
                       if s.frontmatter.get('industry') == industry]

        return [{
            'name': s.name,
            'value': s.frontmatter.get('tam_bn', 1),
            'itemStyle': {
                'color': LAYER_COLORS.get(s.frontmatter.get('layer', 1), '#94a3b8')
            }
        } for s in segments]

    def build_graph(self) -> Dict:
        """构建力导向关系图"""
        nodes = []
        edges = []
        node_set = set()

        for entity in self.parser.entities.values():
            if entity.name not in node_set:
                node_set.add(entity.name)
                nodes.append({
                    'name': entity.name,
                    'symbolSize': max(12, min(50, entity.backlink_count * 2)),
                    'itemStyle': {'color': TYPE_COLORS.get(entity.entity_type, '#86868B')},
                })

            for link_text in entity.wikilinks:
                if link_text in node_set:
                    edges.append({'source': entity.name, 'target': link_text})

        return {'nodes': nodes, 'edges': edges}

    def build_sankey(self, industry: str = None) -> Dict:
        """构建价值链 Sankey 数据"""
        segments = [e for e in self.parser.entities.values()
                    if e.entity_type == 'segment']
        if industry:
            segments = [s for s in segments
                       if s.frontmatter.get('industry') == industry]

        nodes = [{'name': s.name} for s in segments]
        links = []
        for s in segments:
            for link in s.wikilinks:
                # 只保留 segment→segment 的供应关系
                target = self.parser.get_entity(link)
                if target and target.entity_type == 'segment':
                    links.append({
                        'source': s.name,
                        'target': target.name,
                        'value': 1
                    })

        return {'nodes': nodes, 'links': links}

    def build_heatmap(self) -> List[Dict]:
        """热力图：按引用量 + TAM 综合排序"""
        segments = [e for e in self.parser.entities.values()
                    if e.entity_type == 'segment']

        # 排序权重：TAM(60%) + 引用量(40%)
        max_tam = max((s.frontmatter.get('tam_bn', 0) for s in segments), default=1)
        max_bl = max((s.backlink_count for s in segments), default=1)

        for s in segments:
            tam = s.frontmatter.get('tam_bn', 0)
            tam_score = tam / max_tam * 60 if max_tam else 0
            bl_score = s.backlink_count / max_bl * 40 if max_bl else 0
            s._heat_score = tam_score + bl_score

        return sorted(segments, key=lambda s: s._heat_score, reverse=True)
