---
id: pattern-004
category: ui
language: python
score: 50
tags: [ui, python]
---

## 컨텍스트
파일: build_wiki_data.py (Write 완료)

## 핵심 코드
```python
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
```

## 태그
- ui
- python