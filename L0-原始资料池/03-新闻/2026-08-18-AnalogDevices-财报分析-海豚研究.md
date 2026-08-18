---
input_id: input_20260818_014
date: 2026-08-18
source_type: Web调研
source_name: "Analog Devices Q2 FY2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Analog Devices, ADI, 模拟芯片, Q2 FY2026, 海豚研究, Tier1]
data_as_of: 2026-05-02
confidence: 高
---

# Analog Devices Q2 FY2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "Analog Devices Q3 FY2026 earnings revenue net income guidance"
- 搜索词: "Analog Devices Q2 fiscal 2026 results revenue $3.62 billion net income gross margin May 2026"
- 搜索词: "Analog Devices ADI stock price market cap August 2026 shares outstanding"
- 有效来源: PR Newswire 官方财报稿、Futurum Group 深度解读、Motley Fool 电话会纪要、GuruFocus/Investing.com 电话会亮点、Barchart、Benzinga、Yahoo Finance、stockanalysis

## 关键数据（Q2 FY2026，财季截至 2026-05-02，2026-05-20 发布）

> 说明：ADI 财年截至每年 10 月底。Q3 FY2026（截至 2026-08-01）尚未发布，财报电话会定于 2026-08-19 盘前；故「最新已发布」实际财报为 Q2 FY2026。

| 指标 | 数值 | 对比 |
|------|------|------|
| 总营收 | $3.62B（历史新高） | YoY +37%，QoQ +15%，超共识 $3.51B |
| GAAP 净利 | ~$1.18B | YoY +106%（上年同期 $569.8M） |
| Non-GAAP 稀释 EPS | $3.09（历史新高） | YoY +67%（上年 $1.85），QoQ +26%，超共识 ~$2.90 |
| Non-GAAP 毛利率 | 73% | YoY +360bps，QoQ +180bps |
| Non-GAAP 营业利润率 | 49% | YoY +780bps |
| 自由现金流 | $734M（单季）/ $4.6B（TTM） | — |
| 现金+短期投资 | $3.4B（季末） | — |

## 分终端市场（Q2 FY2026）

| 终端 | 营收 | 占比 | YoY |
|------|------|:--:|------|
| 工业 | $1.80B | 50% | +56% |
| 汽车 | $871.6M | 24% | +2% |
| 通信 | $554.7M | 15% | +79% |
| 消费 | $397.8M | 11% | +23% |

- 数据中心（现占通信收入 >75%）YoY 增长 >90%，由光通信 + 电源组合驱动。

## 指引（Q3 FY2026）

- 营收: $3.9B ± $100M（区间 $3.80-4.00B），共识 $3.00-3.33
- Non-GAAP 调整后 EPS: $3.30 ± $0.15（共识 ~$3.00-3.31）
- Non-GAAP 营业利润率: ~49% ± 100bps
- Non-GAAP 毛利率: 预期环比降 ~50bps 至 ~72.5%（Q2 一次性渠道重新定价收益消退）
- 税率: 12%-14%

## 其他关键事件

- 宣布以 **$1.5B 收购 Empower Semiconductor**，补强 AI 数据中心电源管理（功率技术）组合。

## 估值快照（2026-08-17 收盘）

- 股价: $390.28
- 市值: ~$190.10B
- 流通股: ~487.09M
- 52 周区间: ~$221.50 - $445.92

## 来源
- PR Newswire（Morningstar 转载）官方财报稿: https://dotcom-edge-prod.ind7f52b.eas.morningstar.com/news/pr-newswire/20260520ne63608/analog-devices-reports-record-fiscal-second-quarter-2026-financial-results
- Futurum Group 深度解读: https://futurumgroup.com/insights/analog-devices-q2-fy-2026-earnings-show-ai-linked-data-center-power-demand/
- Motley Fool 电话会纪要: https://www.fool.com/earnings/call-transcripts/2026/05/20/analog-devices-adi-q2-2026-earnings-transcript/
- GuruFocus / Investing.com 电话会亮点: https://ca.investing.com/news/company-news/analog-devices-inc-adi-q2-2026-earnings-call-highlights-record-revenue-and-strategic--4652012
- Barchart 财报解读: https://www.barchart.com/story/news/2043281/analog-devices-q2-earnings-beat-estimates-revenues-rise-y-y
- Benzinga: https://www.benzinga.com/markets/earnings/26/05/52699932/analog-devices-cashes-in-on-ai-infrastructure-boom
- Yahoo Finance: https://sg.finance.yahoo.com/news/analog-devices-q2-earnings-beat-153000996.html
- stockanalysis 统计: https://stockanalysis.com/stocks/adi/statistics/

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 总营收 $3.62B 创新高（YoY+37%） | analog-devices | latest_revenue | 高 |
| GAAP 净利 ~$1.18B（YoY+106%） | analog-devices | 财务状况表 | 高 |
| Non-GAAP 毛利率 73% | analog-devices | 财务状况表 | 高 |
| Non-GAAP 稀释 EPS $3.09 | analog-devices | 财务状况表 | 高 |
| 市值 ~$190.10B | analog-devices | market_cap | 高 |
| Q3 指引营收 $3.9B、EPS $3.30 | analog-devices | one_liner / 最新季度详情 | 高 |
| $1.5B 收购 Empower Semiconductor | analog-devices | one_liner / description | 高 |
