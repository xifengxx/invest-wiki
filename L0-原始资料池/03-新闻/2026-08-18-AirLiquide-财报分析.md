---
input_id: input_20260818_062
date: 2026-08-18
source_type: Web调研
source_name: "Air Liquide H1 2026 财报（官方 + 多源）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Air Liquide, AI.PA, 液化空气, H1 2026, 电子特气, Tier1]
data_as_of: 2026-07-28
confidence: 高
---

# Air Liquide H1 2026 财报分析（简化版）

## 搜索记录
- 搜索词: "Air Liquide H1 2026 earnings revenue net income"
- 时间: 2026-08-18
- 有效来源: 官方 airliquide.com、borsaitaliana（radiocor）、gasworld、edgen、chemxplore、marketscreener、investing.com

## 关键数据（H1 2026，2026-07-28 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | €13,827.9M（€13.83B ≈ €138.3亿） | YoY +0.8% 报告；+4.3% 排除汇率+能源；+2.6% 可比 |
| 气体与服务营收（占97%） | €13.41B | 可比 +2.6% |
| 报告净利润（归母） | €1,822.6M（≈€18.2亿） | YoY +1.2%（恒定汇率 +6.5%） |
| 经常性净利润 | €1.923B（≈€19.23亿） | YoY +4.4%（排除汇率+能源 +9.9%） |
| 经常性营业利润 | €2.89B | YoY +5.7% |
| 营业利润率 | 20.9% | +1pp |
| 基本 EPS | €2.86 | +1.1% |
| 经营性现金流 | €3.4B | +3.7% |

## 关键要点
- 效率增益近 €300M
- Q2 加速：可比增长 +3.5%
- 维持 2026 全年指引：营业利润率 2026 +100bp、2027 +100bp（2022–2027 累计 +560bp），恒定汇率下经常性净利润增长

## 数据提取清单
| 数据点 | 值 | 来源 URL | 置信度 |
|--------|-----|---------|:--:|
| H1 2026 营收 | €13,827.9M（+0.8%） | airliquide.com 官方 | 高 |
| 报告净利润 | €1,822.6M（+1.2%） | airliquide.com 官方 | 高 |
| 经常性净利润 | €1.923B（+4.4%） | borsaitaliana radiocor | 高 |
| 营业利润率 | 20.9%（+1pp） | edgen / marketscreener | 高 |

## 来源
- Air Liquide 官方: https://www.airliquide.com/group/press-releases-news/2026-07-28/h1-2026-results-acceleration-second-quarter-air-liquide-combines-growth-continuous-performance
- borsaitaliana radiocor: https://www.borsaitaliana.it/borsa/notizie/radiocor/finance/dettaglio/air-liquide-h1-recurring-net-profit-1923-bln-eur-up-44-up-99-excluding-forex-energy-nRC_28072026_0853_188124317.html?lang=en
- gasworld: https://www.gasworld.com/story/air-liquide-reports-higher-h1-2026-profits-as-semiconductor-demand-grows/2255502.article/#1
- edgen: https://www.edgen.tech/zh/news/post/air-liquide-backs-guidance-as-h1-margin-rises-1-point-to-209
- chemxplore: https://chemxplore.com/news/air-liquide-h1-results-growth-performance
- marketscreener: https://hk.marketscreener.com/news/air-liquide-backs-guidance-after-revenue-margin-improvements-ce7f51dddb8af624#1

## Schema-Mapping
| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| H1 2026 营收 €13,827.9M（+0.8%） | air-liquide | latest_revenue / 财务状况表 | 高 |
| 报告净利润 €1,822.6M（+1.2%） | air-liquide | 财务状况表 | 高 |
| 经常性净利润 €1.923B（+4.4%） | air-liquide | one_liner | 高 |
| 营业利润率 20.9%（+1pp） | air-liquide | 财务状况表 / one_liner | 高 |
