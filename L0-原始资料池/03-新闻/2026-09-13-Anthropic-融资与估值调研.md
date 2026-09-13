---
input_id: input_20260913_003
date: 2026-09-13
source_type: Web调研
source_name: "Anthropic 融资/估值/营收与 IPO 进展（WebSearch 多源）"
source_url: "https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation"
ingest_date: 2026-09-13
status: 已处理
tags: [Anthropic, Claude, 未上市, 估值, 融资, IPO, 企业级AI]
data_as_of: 2026-08
confidence: 中
---

# Anthropic 融资、估值与经营数据调研

> 归档说明：Anthropic 为**未上市公司**，采用「融资轮次 + 估值 + run-rate 收入」口径。官方来源（anthropic.com）与媒体报道互补，媒体口径存在分歧处已标注。

## 搜索记录

| 搜索词 | 时间 | 有效来源 |
|--------|------|---------|
| Anthropic funding round valuation 2026 revenue run rate | 2026-09-13 | Anthropic 官方 / MarketWatch / TNW / Pepperstone / beam.ai / KuCoin / 证券之星 |

有效 URL 列表：
- https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation （**官方来源**）
- https://www.marketwatch.com/story/anthropic-is-now-worth-380-billion-and-sharing-new-details-about-how-much-money-it-makes-182e6151
- https://thenextweb.com/news/anthropic-800-billion-valuation-revenue-30-billion-ipo
- https://beam.ai/agentic-insights/anthropic-ipo-965-billion-enterprise-ai-agent-buyers
- https://pepperstone.com/en/insights/market-analysis/equities/anthropic-s-ipo-looms-can-a-2-trillion-valuation-survive-the-profitability-test
- https://www.kucoin.com/zh-hant/news/flash/anthropic-s-ipo-gains-momentum-with-65b-revenue-run-rate-and-559m-profit-in-q2-2026

## 关键数据表

### 融资与估值路径

| 时间 | 事件 | 估值 | 当时 run-rate | 置信度 |
|------|------|------|--------------|:--:|
| 2026-02-12 | **Series G：$300亿**，GIC/Coatue 领投，微软、英伟达参投 | **$3,800亿**（投后） | $140亿 | 高（官方） |
| 2026-04 | 投资人报价（公司未接受） | ~$8,000亿 | $300亿 | 中 |
| **2026-05底** | **Series H：$650亿**（史上最大私募轮） | **$9,650亿**（投后） | ~$470亿 | 中 |
| 2026-08 | IPO 投资人预期 | **>$2万亿** | — | 低（前瞻） |

### 收入 run-rate 增长轨迹

| 时点 | run-rate |
|------|----------|
| 2024年底 | ~$10亿 |
| 2025年底 | ~$90亿 |
| 2026-02 | $140亿 |
| 2026-03 | $190-200亿 |
| 2026-04初 | $300亿 |
| 2026-05底 | ~$470亿 |
| 2026-07底 | **~$650亿** |
| 2026全年（预期） | **$1,000-1,200亿** |

### Q2 2026 财务（据报道）

| 指标 | 值 | 对比 |
|------|-----|------|
| 单季营收 | ~$115亿 | Q2 2025 为 $7.87亿，**约 14 倍** |
| 调整后经营利润 | **+$5.59亿（首次转正）** | 首个盈利季度 |

### IPO 进展

| 项 | 内容 |
|----|------|
| S-1 | **2026-06-01 保密提交草案** |
| 潜在时间 | 2026年10月（可能） |
| 估值预期 | 部分潜在投资人给到 >$2万亿 |

## Schema-Mapping

| 原文内容 | 映射到 L2 公司 | 映射字段 | 是否冲突 |
|---------|---------------|---------|:-------:|
| "Series H $650亿、投后$9,650亿" | Anthropic | market_cap | 否（原为空） |
| "run-rate ~$650亿（2026.7）" | Anthropic | latest_revenue | 否（原为空） |
| "Q2 2026 首次调整后经营利润转正 +$5.59亿" | Anthropic | 财务状况 | 否（新增） |
| "GIC/Coatue 领投，微软英伟达参投" | Anthropic | partners | 否（原为空数组） |
| "Claude 企业级/编码工具" | Anthropic | core_business | 否（新增） |
| "OpenAI/Google/xAI 竞争" | Anthropic | competitors | 否（原为空数组） |
| "2026-10 可能上市" | Anthropic | 融资与现金流 | 否（新增） |

## 数据分歧备注

1. 有来源写 "$96.5 billion" 应为 **$965 billion** 的笔误，已按官方口径修正
2. Q2 2026 营收有 "$109亿（预测）" 与 "$115亿" 两个口径，取较新的 $115亿并标注
3. 2026-04 的 $8,000亿为**投资人报价**（公司未接受），非实际成交估值
4. IPO 估值 >$2万亿 属**前瞻预期**，非事实

## QA 读取完整性自检

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | 来源数量 | 1 次 WebSearch，7 有效来源（含官方） ✓ |
| 2 | 章节覆盖 | 融资估值/收入轨迹/Q2财务/IPO 4 项 ✓ |
| 3 | 数据表格 | 4 张表，已全部提取 |
| 4 | 关键数字 | 估值/融资额/run-rate/Q2营收利润 等 20+ 个 |
| 5 | 实体清单 | Anthropic、GIC、Coatue、微软、英伟达、OpenAI、Google、xAI ✓ |
| 6 | 官方来源 | Series G 数据来自 anthropic.com 官方新闻稿，置信度高 ✓ |
| 7 | 数据性质 | 明确标注未上市、采用融资/估值口径 ✓ |

自检结论：✅ 通过
