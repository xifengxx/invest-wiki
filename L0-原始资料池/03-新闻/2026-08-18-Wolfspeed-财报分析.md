---
input_id: input_20260818_069
date: 2026-08-18
source_type: Web调研
source_name: "Wolfspeed Q3 FY2026 财报（官方 + 多源）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Wolfspeed, WOLF, 碳化硅, SiC, Q3 FY2026, Tier1]
data_as_of: 2026-05-05
confidence: 高
---

# Wolfspeed Q3 FY2026 财报分析（简化版）

## 搜索记录
- 搜索词: "Wolfspeed Q4 FY2026 earnings revenue net income"
- 搜索词: "Wolfspeed Q3 FY2026 earnings May 2026 revenue gross margin net loss"
- 时间: 2026-08-18
- 有效来源: stockanalysis（income statement quarterly）、The Motley Fool 财报电话会、Nasdaq/Yahoo 官方新闻稿、marketscreener

## 重要说明：最新已发布财季为 Q3 FY2026
- 财年截至 6 月底，Q4 FY2026 财报**尚未发布**，定于 2026-08-19 盘后发布（指引营收 $140–$160M，non-GAAP 毛利率预计仍为负）。
- 因此「最新已发布」财报为 **Q3 FY2026**（财季截至 2026-03-29，2026-05-05 发布）。

## 关键数据（Q3 FY2026，2026-05-05 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | $150.2M | YoY -19%（去年同期 $185.4M），符合指引中值 $150M |
| GAAP 毛利率 | -26.63%（毛损 $40.0M） | 环比改善（Q2 FY2026 为 -46.47%） |
| Non-GAAP 毛利率 | -20.6% | 受 ~$46M 产能利用率不足拖累，环比改善双位数百分点 |
| GAAP 净利润（净亏损） | -$119.9M | 同比收窄（Q3 FY2025 亏损更大） |
| 调整后 EBITDA | -$62M | 为负 |
| 经营现金流 | -$84M | 为负 |

## 关键要点
- 营收构成：功率器件 ~$100M（约 90% 来自 Mohawk Valley 200mm 厂）+ 材料 ~$50M（环比持平）。
- 负毛利率主因 ~$46M 产能利用率不足费用；GAAP 毛利率环比由 -46.47% 大幅改善至 -26.63%。
- 净亏损 $119.9M，同比收窄；经营现金流仍为负。
- Q4 FY2026 指引：营收 $140–$160M，non-GAAP 毛利率预计仍为负。

## 数据提取清单
| 数据点 | 值 | 来源 URL | 置信度 |
|--------|-----|---------|:--:|
| Q3 FY2026 营收 | $150.2M（YoY -19%） | stockanalysis.com | 高 |
| GAAP 毛利率 | -26.63%（毛损 $40.0M） | stockanalysis.com / 官方新闻稿 | 高 |
| Non-GAAP 毛利率 | -20.6% | 官方新闻稿 | 高 |
| 净亏损 | -$119.9M | stockanalysis.com / 官方新闻稿 | 高 |

## 来源
- stockanalysis income statement: https://stockanalysis.com/stocks/wolf/financials/income-statement/?p=quarterly
- The Motley Fool Q3 2026 transcript: https://www.fool.com/earnings/call-transcripts/2026/05/05/wolfspeed-wolf-q3-2026-earnings-transcript/
- Nasdaq 官方新闻稿: https://www.nasdaq.com/press-release/wolfspeed-reports-financial-results-third-quarter-fiscal-2026-2026-05-05
- Yahoo Finance 官方新闻稿: https://au.finance.yahoo.com/news/wolfspeed-reports-financial-results-third-200500920.html
- marketscreener: https://www.marketscreener.com/news/wolfspeed-reports-financial-results-for-the-third-quarter-of-fiscal-2026-ce7f58dcd18ff725

## Schema-Mapping
| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| Q3 FY2026 营收 $150.2M（YoY -19%） | wolfspeed | latest_revenue / 财务状况表 | 高 |
| GAAP 毛利率 -26.63%（毛损 $40.0M） | wolfspeed | 财务状况表 / one_liner | 高 |
| 净亏损 $119.9M | wolfspeed | 财务状况表 / one_liner | 高 |
