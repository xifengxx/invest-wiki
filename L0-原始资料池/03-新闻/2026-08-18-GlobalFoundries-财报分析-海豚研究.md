---
input_id: input_20260818_021
date: 2026-08-18
source_type: Web调研
source_name: "GlobalFoundries Q2 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, GlobalFoundries, 格芯, GFS, Q2 2026, 海豚研究, Tier1]
data_as_of: 2026-06-30
confidence: 高
---

# GlobalFoundries Q2 2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "GlobalFoundries Q2 2026 earnings revenue net income guidance"
- 搜索词: "GlobalFoundries GFS stock price market cap August 2026 shares outstanding"
- 时间: 2026-08-18
- 有效来源: GF 官方 press release（investors.gf.com）、Nasdaq 电话会亮点、MarketBeat 快讯、Investing.com 电话会纪要/slides、DoNews、Yahoo Finance HK、stockanalysis

## 关键数据（Q2 2026，财季截至 2026-06-30，2026-08-05 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 总营收 | **$1.786B** | +6% YoY / +9% QoQ，超指引与共识（~$1.76B） |
| GAAP 净利 | **$167M**（稀释 EPS $0.30） | 上年同期 $228M（$0.41） |
| Non-IFRS 净利 | **~$256M**（稀释 EPS $0.46） | 超共识 ~$0.43-0.44 |
| Non-IFRS 毛利率 | **29.9%** | +470bps YoY，Q2 纪录 |
| Non-IFRS 营业利润 | $298M（营业利润率 16.7%） | — |
| 运营现金流 | $405M | — |
| 调整后自由现金流 | -$3M | — |
| 现金+有价证券 | $3.3B（总债务 $1.1B） | — |
| 晶圆出货量 | ~62.5 万片（300mm 等效） | +8% QoQ 与 YoY |

## 分终端市场（Q2 2026）

- 数据中心+通信终端 **+62% YoY**，占营收 **16%**，由硅光子（silicon photonics）与硅锗（SiGe）光网络产品驱动。
- 硅光子收入 2026 年预计**翻倍以上**（more than double）。

## 指引

### Q3 2026
- 营收: **$1.885B ± $25M**（中点 ~+6% QoQ）
- Non-IFRS EPS: **$0.51 ± $0.05**（中点 ~+11% QoQ）
- Non-IFRS 毛利率: **~30.5% ± 100bps**
- 运营费用: $260M ± $10M

### 全年 2026（上修）
- 数据中心+通信板块增速上修至 **+50~60% YoY**（原高30s%区间）
- 硅光子收入预计翻倍以上
- 全年毛利率 ~30%
- 收购带来的技术许可服务收入 **$100-120M**（原 $60-100M）
- CAPEX 占营收 15-20%；调整后 FCF 利润率 ~10%
- Q2 实施的提价预计 2027 年起贡献营收

## 其他关键事件

- AI pivot：加速 AI 数据中心需求，获 **$675M 政府支持**（CHIPS 相关）。
- 长期目标维持：2028 年毛利率 40% 退出率。

## 估值快照（2026-08-17 收盘）

- 股价: $53.44（-2.09%）
- 市值: ~$29.3B（stockanalysis，2026-08-17；Fidelity/CNBC ~$29.95B）
- 流通股: ~548.75M
- 52 周区间: $31.59 - $92.55
- 市盈率(TTM): ~41.7-42.6；EPS(TTM) ~$1.28

## 来源
- GF 官方财报稿: https://investors.gf.com/news-releases/news-release-details/globalfoundries-reports-second-quarter-2026-financial-results
- Nasdaq 电话会亮点: https://www.nasdaq.com/articles/globalfoundries-q2-earnings-call-highlights
- MarketBeat 快讯: https://www.marketbeat.com/instant-alerts/globalfoundries-q2-earnings-call-highlights-2026-08-05/
- Investing.com 电话会纪要: https://www.investing.com/news/transcripts/earnings-call-transcript-globalfoundries-tops-q2-2026-estimates-on-margins-93CH-4838036
- Investing.com slides（AI pivot + $675M 政府支持）: https://za.investing.com/news/company-news/globalfoundries-q2-2026-slides-ai-pivot-675m-in-government-support-93CH-4409008
- Nasdaq（Q2 GAAP 净利下滑）: https://www.nasdaq.com/articles/globalfoundries-inc-announces-retreat-q2-income
- DoNews（中文，营收超预期 $1.786B 毛利率近30%）: https://www.donews.com/news/detail/1/6660538.html
- Yahoo Finance HK（中文，硅光子带动 Q2 业绩）: https://hk.finance.yahoo.com/news/財報-格芯搭上ai順風車-矽光子需求帶旺第二季業績-183005979.html
- stockanalysis 统计（市值/流通股）: https://stockanalysis.com/stocks/gfs/statistics/

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| Q2 2026 营收 $1.786B（+6% YoY/+9% QoQ） | globalfoundries | latest_revenue | 高 |
| Non-IFRS 毛利率 29.9%（+470bps YoY，Q2纪录） | globalfoundries | 财务状况表 | 高 |
| GAAP 净利 $167M / Non-IFRS 净利 ~$256M（EPS $0.46） | globalfoundries | 财务状况表 | 高 |
| 数据中心+通信 +62% YoY，占16%营收 | globalfoundries | body（分终端） | 高 |
| Q3 指引营收 $1.885B、Non-IFRS EPS $0.51、毛利率~30.5% | globalfoundries | one_liner / body | 高 |
| 全年数据中心+通信 +50~60%、硅光子翻倍以上、毛利率~30% | globalfoundries | one_liner / body | 高 |
| 市值 ~$29.3B（2026.8.17） | globalfoundries | market_cap | 高 |
