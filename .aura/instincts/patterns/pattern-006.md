---
id: pattern-006
category: general
language: python
score: 50
tags: [python]
---

## 컨텍스트
파일: parser.py (Edit 완료)

## 핵심 코드
```python
        # 提取 wikilinks：优先从 YAML frontmatter 读取，fallback 到 body [[link]]
        wikilinks = fm.get('wikilinks', [])
        if not wikilinks:
            wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)
```

## 태그
- python