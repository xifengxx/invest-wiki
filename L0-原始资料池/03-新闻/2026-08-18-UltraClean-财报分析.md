---
input_id: input_20260818_068
date: 2026-08-18
source_type: Web调研
source_name: "Ultra Clean Holdings Q2 2026 财报（简化归档）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Ultra Clean, UCTT, Q2 2026, 半导体设备子系统, 气体输送, Tier1]
data_as_of: 2026-06-26
confidence: 高
---

# Ultra Clean Holdings Q2 2026 财报（简化归档）

## 搜索记录
- 搜索词: "Ultra Clean Holdings UCTT Q2 2026 earnings revenue net income gross margin"
- 时间: 2026-08-18
- 有效来源: 官方新闻稿（Yahoo Finance/Barchart/6ix 转载）、GuruFocus

## 关键数据（Q2 2026，财季截至 2026-06-26，2026-08-03 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | $644.9M（创纪录） | 环比 +17%（Q1 $533.7M）；同比 +24.31% |
| 产品营收 | $572.7M | Q1 $465.7M |
| 服务营收 | $72.2M | Q1 $68.0M |
| 毛利率（GAAP） | 16.1% | Q1 15.8%（+0.3pp） |
| 毛利率（Non-GAAP） | 16.7% | Q1 16.5%（+0.2pp） |
| 净利（GAAP，归母） | $8.7M（$0.19/稀释股） | Q1 净亏 $(17.9)M（$(0.40)/股） |
| 净利（Non-GAAP） | $32.3M（$0.70/稀释股） | Q1 $14.5M（$0.31/股）；超预期 ~34.6% |
| Non-GAAP 营业利润率 | 7.0% | Q1 5.1% |

## 指引（Q3 2026）
- 营收 $700–750M；EPS $0.83–$1.03

## 数据提取清单
| 数据点 | 值 | 来源 URL | 置信度 |
|--------|-----|---------|:--:|
| Q2 2026 营收 | $644.9M（+24.31% YoY） | 官方新闻稿（Yahoo/Barchart 转载） | 高 |
| GAAP 净利 | $8.7M（$0.19/股） | GuruFocus / 官方新闻稿 | 高 |
| Non-GAAP 净利 | $32.3M（$0.70/股） | GuruFocus / 官方新闻稿 | 高 |
| 毛利率（GAAP） | 16.1%（Q1 15.8%） | GuruFocus / 官方新闻稿 | 高 |

## 来源
- Yahoo Finance（官方新闻稿转载）: https://ca.finance.yahoo.com/news/ultra-clean-reports-second-quarter-200500500.html
- Barchart: https://www.barchart.com/story/news/3619456/ultra-clean-reports-second-quarter-2026-financial-results
- GuruFocus: https://www.gurufocus.com/news/8999332/is-ultra-clean-holdings-inc-uctt-overvalued-after-q2-earnings-surprise-gf-score-61100-revenue-of-6449m-beats-estimates
- 6ix News: https://6ix.com/news/ultra-clean-reports-second-quarter-2026-financial-results

## Schema-Mapping
| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| Q2 2026 营收 $644.9M（环比+17%，同比+24.31%） | ultra-clean | latest_revenue / 财务状况表 | 高 |
| GAAP 净利 $8.7M（Non-GAAP $32.3M） | ultra-clean | 财务状况表 | 高 |
| 毛利率 GAAP 16.1%（Non-GAAP 16.7%） | ultra-clean | 财务状况表 / one_liner | 高 |
