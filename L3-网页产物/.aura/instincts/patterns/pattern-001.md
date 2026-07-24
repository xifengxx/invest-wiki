---
id: pattern-001
category: db
language: unknown
score: 50
tags: [db]
---

## 컨텍스트
파일: CLAUDE.md (Write 완료)

## 핵심 코드
```unknown
# Invest Wiki — LLM-Wiki 产业链知识库

## 定位

独立的 LLM-Wiki 知识库系统，采用 Markdown + YAML + [[wikilink]] 的数据模式。
对标 Karpathy LLM-Wiki 三层架构，扩展为四层以适应结构化产业链数据需求。

## 四层架构

```
L0-原始资料池/      ← Raw Sources（LLM 只读不写）
L1-Schema与Pipeline/ ← Schema & Pipeline（操作规范、Ingest/Lint Skill）
L2-Wiki/            ← The Wiki（结构化 YAML + MD 词条）
L3-网页产物/         ← Web Output（编译生成 index.html）
```

**操作规范**: 所有 Wiki 操作必须先读 `L1-Schema与Pipeline/CLAUDE.md`

## 数据规模

| 类型 | 数量 |
|------|:--:|
| 产业 | 2 |
| 赛道 | 74 |
| 公司 | 398 |
| 总词条 | 474 |

## 使用方式

```bash
cd ~/Claude_projects/5factor_system/invest_wiki

# 1. 从 invest_kg JSON 迁移（首次，已完成）
python seed_json_to_md.py

# 2. 测试 Wiki 引擎
python -c "
import sys; sys.path.insert(0, '.')
from engine.parser import WikiParser
wiki = WikiParser('L2-Wiki')
wiki.parse_all()
print(f'{len(wiki.entities)} 词条')
for e in wiki.get_hot(5):
    print(f'  {e.backlink_count:4d} ← {e.name}')
"

# 3. LLM 采集更新
# 见 L1-Schema与Pipeline/collector/执行指令-采集处理.md

# 4. 生成 HTML（L2 → L3 编译）
```

## 태그
- db