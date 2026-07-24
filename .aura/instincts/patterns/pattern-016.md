---
id: pattern-016
category: security
language: unknown
score: 50
tags: [security]
---

## 컨텍스트
파일: ARCHITECTURE.md (Edit 완료)

## 핵심 코드
```unknown
---

## 十、Obsidian 知识库五要素借鉴（Phase 2）

2026-07 对比了 Obsidian 个人知识库（2,452 页 / 19,081 条链接 / thesis + contradiction + index 体系），将 5 个成熟模式落地到 Invest Wiki：

| # | 借鉴点 | Obsidian 做法 | Invest Wiki 落地 |
|:--:|------|------|------|
| 1 | **Index 索引页** | `wiki/index.md` 总索引，1924 行 | `L2-Wiki/index.md` — 74赛道按产业/层级排列，LLM 查询路由入口 |
| 2 | **链接密度提升** | 平均 7.8 链接/页，19,081 总链接 | link-enrich Skill + 公司↔赛道双向链接，链接从154→195，孤立赛道清零 |
| 3 | **矛盾持久化** | `⚠️ Contradiction` 一级公民，模板内置 | YAML `contradictions` 字段 + Lint 写回 + L3 琥珀色卡片 |
| 4 | **投资论点系统** | `theses/` 目录 + status + confidence 1-10 | `L2-Wiki/论点/` + 10条初始种子 + L3 第10模块（论点卡片） |
| 5 | **双模式维护** | Collection ↔ Refinement 循环 + QA 版本追踪 | L1 操作宪法新增维护模式章节 + QA v1.0 版本号 |

### Thesis 数据模型

```yaml
type: thesis
thesis_status: forming | active | invalidated | confirmed
confidence: 1-10
affected_segments: ["gpu", "ai-server"]
affected_companies: ["NVDA", "AMD"]
```

### 维护循环

```
Collection（采集）: ingest→提取→消化→更新→index
        ↕  交替
Refinement（提炼）: Lint→thesis审核→矛盾解决→链接增强→index→QA升级
```

---

## 十一、与 AI投研助手 的关系
```

## 태그
- security