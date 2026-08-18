---
input_id: input_20260818_067
date: 2026-08-18
source_type: Web调研
source_name: "Advanced Energy Q2 2026 财报（官方新闻稿 + 多源）"
source_url: "https://www.morningstar.com/news/business-wire/20260803070780/advanced-energy-reports-second-quarter-2026-results"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Advanced Energy, AEIS, Q2 2026, 半导体电源, 等离子电源]
data_as_of: 2026-06-30
confidence: 高
---

# Advanced Energy Q2 2026 财报分析（简化版）

## 搜索记录
- 搜索词: "Advanced Energy Q2 2026 earnings revenue net income"
- 时间: 2026-08-18
- 有效来源: 官方新闻稿（Business Wire / Morningstar）、Yahoo Finance、Investing.com、GuruFocus、MarketBeat、SimplyWall.st

## 关键数据（Q2 2026，截止 2026-06-30，2026-08-03 发布）

| 指标 | 数值 | 同比 | 环比 |
|------|------|------|------|
| 营收 | $574.1M（创纪录） | +30%（$441.5M→$574.1M） | +12%（$511M→$574.1M） |
| 净利（GAAP） | $54.5M | +114%（$25.5M→$54.5M） | — |
| 毛利率 | 41.9% | +380bps（38.1%→41.9%） | — |
| 稀释EPS（GAAP） | $1.29 | +92.5% | — |
| non-GAAP EPS | $2.74 | +83% | — |
| 营业利润（non-GAAP） | $125M | — | — |
| 经营性现金流 | $86M（创纪录） | — | — |

## 关键要点
- 营收 $574.1M 创纪录，超市场共识 ~$542.8M
- 半导体板块营收 $278M（+33% YoY）创纪录；数据中心计算 $192M（+35% YoY）；工业与医疗 $80M（+17%）；电信与网络 $24M（+12%）
- 毛利率 41.9%（+380bps），含 IEEPA 关税退税 ~120bps 一次性收益（剔除后 40.7%）
- non-GAAP 净利 $112M，超共识 $85.67M
- Q3 2026 指引：营收 ~$640M（±$20M），non-GAAP EPS ~$3.00（±$0.25）
- 全年营收增速指引上调至 low-to-mid 30% 区间（原 low-to-mid 20%）
- 期末现金 $1.40B，净现金 $132M

## 数据提取清单
| 数据点 | 值 | 来源 URL | 置信度 |
|--------|-----|---------|:--:|
| Q2 2026 营收 | $574.1M（+30%） | Business Wire / Morningstar 官方新闻稿 | 高 |
| Q2 2026 净利（GAAP） | $54.5M（+114%） | 官方新闻稿 | 高 |
| Q2 2026 毛利率 | 41.9%（+380bps） | 官方新闻稿 | 高 |
| non-GAAP EPS | $2.74（+83%） | GuruFocus / Investing.com | 高 |

## Schema-Mapping
| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| Q2 2026 营收 $574.1M（+30%） | advanced-energy | latest_revenue / 财务状况表 | 高 |
| Q2 2026 净利 $54.5M（GAAP） | advanced-energy | 财务状况表 | 高 |
| Q2 2026 毛利率 41.9% | advanced-energy | 财务状况表 / one_liner | 高 |

## 来源
- Business Wire（官方新闻稿，Morningstar 转载）: https://www.morningstar.com/news/business-wire/20260803070780/advanced-energy-reports-second-quarter-2026-results
- Yahoo Finance: https://au.finance.yahoo.com/news/advanced-energy-reports-second-quarter-200100689.html
- Investing.com（Q2 2026 slides）: https://za.investing.com/news/company-news/advanced-energy-q2-2026-slides-record-results-guidance-raised-93CH-4403939
- GuruFocus（财报电话会）: https://www.gurufocus.com/news/9000371/advanced-energy-industries-inc-aeis-q2-2026-earnings-call-highlights-record-revenue-and-eps-fueled-by-semiconductor-and-data-center-momentum
- MarketBeat: https://www.marketbeat.com/instant-alerts/advanced-energy-industries-q2-earnings-call-highlights-2026-08-03/
