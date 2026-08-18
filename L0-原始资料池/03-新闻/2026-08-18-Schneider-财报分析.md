---
input_id: input_20260818_060
date: 2026-08-18
source_type: Web调研
source_name: "Schneider Electric H1 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Schneider Electric, SU.PA, 施耐德电气, H1 2026, 海豚研究, Tier1]
data_as_of: 2026-07-30
confidence: 高
---

# Schneider Electric H1 2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "Schneider Electric H1 2026 earnings revenue net income"
- 搜索词: "Schneider Electric H1 2026 gross margin gross profit cost of sales half year results"
- 有效来源: Nasdaq、Yahoo Finance、MarketScreener、Quartr、stockanalysis、tedmag

## 关键数据（H1 2026，财季截至 2026-06-30，2026-07-30 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | €21.2B（€21,226M） | 有机 +14%，报告口径 +9.8%（去年同期 €19,336M） |
| Q2 2026 营收 | €11.46B | 有机 +16.5%，报告口径 +14.5% |
| 毛利 | €9,014M | 去年同期 €8,202M |
| 毛利率 | 42.5% | 有机 +10bps |
| 净利润（报告） | €2.5B | YoY +30% |
| 归母净利润 | €2.49B | YoY +30.1%（去年同期 €1.91B） |
| 调整后净利润 | €2.7B | YoY +21% |
| 调整后 EBITA | €4.09B | 报告 +16.6%，有机 +22.1% |

## 指引（FY2026 全年，上调）

- 营收有机增长: **10% - 13%**（上调）
- 调整后 EBITA 有机增长: **14% - 19%**（上调）

## 驱动因素与展望
- 强劲执行力 + 广泛需求，能源管理与工业自动化双增长，数据中心与基础设施终端市场尤为强劲
- 毛利率扩张温和（有机 +10bps），受系统业务高增长负面结构 + 原材料/关税通胀压力，但生产力提升支撑
- 数据中心 + 网络需求延续高景气，支撑营收与利润率上调

## 来源
- Nasdaq: https://www.nasdaq.com/articles/schneider-electric-h1-net-income-rises-upgrades-2026-financial-target
- Yahoo Finance（财报电话会亮点）: https://au.finance.yahoo.com/news/schneider-electric-se-sbgsf-h1-150055558.html
- MarketScreener（半年报）: https://in.marketscreener.com/news/schneider-electric-half-year-results-accounts-ce7f51d3d18df424
- Quartr（Q2 2026 摘要）: https://quartr.com/events/schneider-electric-s-e-su-q2-2026_3gmCZZyS
- stockanalysis（Q2 2026 电话会）: https://stockanalysis.com/quote/epa/SU/transcripts/626503-q2-2026/
- tedmag: https://tedmag.com/schneider-electric-delivers-strong-half-year-results/

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 营收 €21.2B（有机 +14%） | schneider | latest_revenue | 高 |
| 净利润 €2.5B（YoY +30%） | schneider | 财务状况表 | 高 |
| 毛利率 42.5%（有机 +10bps） | schneider | 财务状况表 | 高 |
| FY2026 指引 营收有机 +10-13% / 调整后 EBITA 有机 +14-19% | schneider | one_liner | 高 |
