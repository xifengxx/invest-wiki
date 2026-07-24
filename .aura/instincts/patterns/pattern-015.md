---
id: pattern-015
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: ARCHITECTURE.md (Edit 완료)

## 핵심 코드
```unknown
#### 赛道详情页（11 个模块）

| # | 模块 | 数据来源 | 渲染形式 |
|---|------|---------|---------|
| 1 | 市场规模 | tam/cagr/margin/backlinks | 4 卡片统计 |
| 2 | 定位与定义 | description | Markdown 正文（`\|` → 段落分隔） |
| 2.5 | ⚠️ 已知矛盾 | contradictions | 琥珀色卡片（仅非空时显示） |
| 3 | 价值链分析 | cost_share / profit_pool | 双进度条（None=隐藏该列） |
| 4 | 上下游传导 | key_inputs / key_customers / price_conduction | 标签 + 流程箭头 + 全文字描述 |
| 5 | 竞争格局 | competition | 4 张表（全球/中国/壁垒/代差） |
| 6 | 关键趋势 | key_trends | 标题+描述卡片 |
| 7 | 关联关系 | wikilinks | 关系条目 + 类型标签 + clickable |
| 8 | 研报与证据 | sources | 编号 + 粗体标题 + 可点击链接 |
| 9 | 核心标的 | companies | 公司表格（代码/名称/角色/营收） |
| 10 | 投资论点 | thesis_index + related_theses | 论点卡片（status 标签 + confidence ★） |
```

## 태그
