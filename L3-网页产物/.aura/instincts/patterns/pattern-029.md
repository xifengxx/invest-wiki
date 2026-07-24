---
id: pattern-029
category: general
language: python
score: 50
tags: [python]
---

## 컨텍스트
파일: parser.py (Edit 완료)

## 핵심 코드
```python
    def parse_all(self):
        """解析所有 .md 文件"""
        self.entities = {}
        for root, dirs, files in os.walk(self.wiki_dir):
            # 排除非实体目录
            rel_root = os.path.relpath(root, self.wiki_dir)
            if rel_root.startswith('消化笔记') or rel_root.startswith('.'):
                continue
            for f in files:
                if not f.endswith('.md'):
                    continue
                # 排除索引文件
                if f == 'index.md' and rel_root == '.':
                    continue
                path = os.path.join(root, f)
                entity = self._parse_file(path)
                if entity:
                    self.entities[entity.slug] = entity
```

## 태그
- python