---
input_id: input_20260818_013
date: 2026-08-18
source_type: Web调研
source_name: "Texas Instruments Q2 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Texas Instruments, 德州仪器, TXN, Q2 2026, 海豚研究, Tier1]
data_as_of: 2026-06-30
confidence: 高
---

# Texas Instruments Q2 2026 财报分析（海豚研究）

## 搜索记录
- 搜索词1: "Texas Instruments Q2 2026 earnings revenue net income guidance"
- 搜索词2: "Texas Instruments TXN market cap August 2026 stock price"
- 有效来源: TI 官方/电话会转录（stockanalysis）、Futurum、Seeking Alpha、TipRanks、Morningstar、stockanalysis statistics

## 关键数据（Q2 2026，2026-07-22 发布，截止 2026-06-30）

| 指标 | 数值 | 同比 | 环比/对比 |
|------|------|------|-----------|
| 营收 | $5.46B | +23% | +13%（超预期$5.24B） |
| 净利 | $1.98B | +53% | — |
| EPS | $2.14 | +52% | 超指引上限（预期~$1.95） |
| 毛利率 | 61% | — | 环比+340bps |
| 营业利润 | $2.31B | +48% | 营业利润率42% |
| 经营现金流 | $2.7B | — | — |

营收、净利、EPS 全面超预期，毛利率环比大幅回升。

## 分板块数据

| 板块 | 营收 | 同比 |
|------|------|------|
| Analog | $4.37B | +26% |
| Embedded Processing | $788M | +16% |
| Other | $310M | -2% |

## 分终端市场

| 终端市场 | YoY增长 |
|----------|---------|
| 工业 | +30% |
| 汽车 | 中双位数 |
| 数据中心 | 翻倍 |
| 消费电子 | 持平 |
| 通信设备 | 增长 |

## 指引

### Q3 2026
- 营收: $5.65-6.15B（中值 $5.9B，超预期 $5.62B）
- EPS: $2.23-2.57（中值 $2.40，超预期 $2.18）
- 有效税率: ~13%

### 资本开支 / 现金流
- 2026 capex: $2-3B（偏向高端）
- CHIPS Act 补贴使 H1 净资本开支接近零
- TTM 自由现金流: $6.5B（去年同期 $1.8B）
- TTM 回购: $5.8B
- Q3 起对模拟产品执行客户逐个调价

## 市值（2026.8）
- ~$258B（stockanalysis/Morningstar，8月17日收盘）；股价约 $283，52周区间 $152.73–$334.03
- 年初至今 +65.8%（vs S&P 500 +13.1%）

## 来源
- stockanalysis 电话会转录: https://stockanalysis.com/stocks/txn/transcripts/653170-q2-2026/
- Futurum（分板块/毛利率/指引详表）: https://futurumgroup.com/insights/texas-instruments-q2-fy-2026-earnings-climb-on-broad-based-analog-growth/
- Seeking Alpha: https://seekingalpha.com/news/4616849-earnings-snapshot-texas-instruments-q2-revenue-jumps-23-yoy-q3-tops-views
- TipRanks Q2 2026 报告: https://www.tipranks.com/stocks/mx:txn/earnings/q2-2026-report
- stockanalysis statistics（市值）: https://stockanalysis.com/stocks/txn/statistics/
- Morningstar: https://www.morningstar.com/stocks/xnas/TXN/quote

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 营收 $5.46B（+23% YoY）超预期$5.24B | texas-instruments | latest_revenue | 高 |
| 净利 $1.98B（+53% YoY） | texas-instruments | 财务状况表 | 高 |
| 毛利率 61%（环比+340bps） | texas-instruments | 财务状况表 | 高 |
| EPS $2.14（+52% YoY） | texas-instruments | 财务状况表 | 高 |
| 分板块 Analog $4.37B / Embedded $788M / Other $310M | texas-instruments | 业务板块 | 高 |
| Q3 指引营收 $5.65-6.15B、EPS $2.23-2.57 | texas-instruments | 指引 | 高 |
| 市值 ~$258B（2026.8） | texas-instruments | market_cap | 中 |
