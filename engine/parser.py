"""Wiki 词条解析器 — 解析 YAML frontmatter + [[wikilink]] + Markdown 正文。"""
import os, re, yaml
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Entity:
    """Wiki 词条实体"""
    name: str
    slug: str
    entity_type: str       # industry/segment/company/concept/person/event
    path: str              # 文件路径
    frontmatter: Dict = field(default_factory=dict)
    content: str = ""      # Markdown 正文
    wikilinks: List[str] = field(default_factory=list)  # 本词条引用的其他词条
    backlinks: List[str] = field(default_factory=list)  # 被其他词条引用的列表
    backlink_count: int = 0                               # 引用量

class WikiParser:
    """解析 Wiki 词条目录"""

    def __init__(self, wiki_dir: str):
        self.wiki_dir = wiki_dir
        self.entities: Dict[str, Entity] = {}  # slug → Entity

    def parse_all(self):
        """解析所有 .md 文件"""
        self.entities = {}
        for root, dirs, files in os.walk(self.wiki_dir):
            # 排除非实体目录
            rel_root = os.path.relpath(root, self.wiki_dir)
            if rel_root.startswith('消化笔记') or '.aura' in root or '__pycache__' in root:
                continue
            for f in files:
                if not f.endswith('.md'):
                    continue
                # 排除索引文件和审计报告
                if f == 'index.md' and rel_root == '.':
                    continue
                if 'audit' in f.lower():
                    continue
                path = os.path.join(root, f)
                entity = self._parse_file(path)
                if entity:
                    self.entities[entity.slug] = entity

        # 计算反向引用
        self._compute_backlinks()
        return self.entities

    def _parse_file(self, path: str) -> Optional[Entity]:
        """解析单个 MD 文件"""
        with open(path) as f:
            content = f.read()

        # 解析 YAML frontmatter
        fm = {}
        body = content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                except Exception:
                    pass
                body = parts[2].strip()

        # 提取 wikilinks：优先从 YAML frontmatter，也合并 body [[link]]
        wl_yaml = fm.get('wikilinks', [])
        if isinstance(wl_yaml, str):
            wl_yaml = [w.strip() for w in wl_yaml.split(',') if w.strip()]
        if not isinstance(wl_yaml, list):
            wl_yaml = []
        wl_body = re.findall(r'\[\[([^\]]+)\]\]', body)
        seen = set()
        wikilinks = []
        for w in wl_yaml + wl_body:
            if w not in seen:
                wikilinks.append(w)
                seen.add(w)

        name = fm.get('name', os.path.basename(path).replace('.md', ''))
        slug = fm.get('slug', self._slugify(name))
        entity_type = fm.get('type', 'unknown')

        return Entity(
            name=name,
            slug=slug,
            entity_type=entity_type,
            path=path,
            frontmatter=fm,
            content=body,
            wikilinks=wikilinks,
        )

    def _compute_backlinks(self):
        """计算每个词条的反向引用（被哪些词条引用）。

        处理跨产业重名：AI算力/半导体存在同名赛道（如"晶圆代工(先进制程)"），
        单一 name→slug 映射会互相覆盖，导致部分赛道 backlink 被静默清零。
        这里改用 name→[entities] 多值映射，重名时按引用方的 industry 消歧，
        无法消歧（如 thesis 无 industry）时全部计入，宁可多算不漏算。
        """
        # name → [entities]（同名赛道会有多个）；slug → entity（唯一）
        name_to_entities: Dict[str, List[Entity]] = {}
        slug_to_entity: Dict[str, Entity] = {}
        for e in self.entities.values():
            name_to_entities.setdefault(e.name, []).append(e)
            slug_to_entity[e.slug] = e

        for entity in self.entities.values():
            entity.backlinks = []
            for other in self.entities.values():
                if other.slug == entity.slug:
                    continue
                # 检查 other 是否引用了 entity
                for link_text in other.wikilinks:
                    targets = self._resolve_link_targets(other, link_text, name_to_entities, slug_to_entity)
                    if any(t.slug == entity.slug for t in targets):
                        entity.backlinks.append(other.name)
                        break
            entity.backlink_count = len(entity.backlinks)

    @staticmethod
    def _resolve_link_targets(source: Entity, link_text: str,
                              name_to_entities: Dict[str, List[Entity]],
                              slug_to_entity: Dict[str, Entity]) -> List[Entity]:
        """把 wikilink 文本解析为目标实体列表（处理跨产业重名消歧）。"""
        # 优先 slug 精确匹配
        if link_text in slug_to_entity:
            return [slug_to_entity[link_text]]
        # name 匹配（可能重名）
        candidates = name_to_entities.get(link_text, [])
        if len(candidates) <= 1:
            return candidates
        # 重名消歧：优先同 industry
        src_ind = source.frontmatter.get('industry')
        if src_ind:
            same = [c for c in candidates if c.frontmatter.get('industry') == src_ind]
            if same:
                return same
        # 无法消歧（source 无 industry 或候选 industry 均不同）→ 全部返回
        return candidates

    def get_entity(self, slug: str) -> Optional[Entity]:
        return self.entities.get(slug)

    def get_by_type(self, entity_type: str) -> List[Entity]:
        return [e for e in self.entities.values() if e.entity_type == entity_type]

    def get_hot(self, limit: int = 20) -> List[Entity]:
        """按引用量排序（热度排行）"""
        return sorted(self.entities.values(), key=lambda e: e.backlink_count, reverse=True)[:limit]

    @staticmethod
    def _slugify(text: str) -> str:
        return re.sub(r'[^\w一-鿿-]', '', text.replace(' ', '-').replace('/', '-'))
