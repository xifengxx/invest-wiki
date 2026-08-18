---
input_id: input_20260818_042
date: 2026-08-18
source_type: Web调研
source_name: "Astera Labs Q2 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Astera Labs, ALAB, Q2 2026, 海豚研究, Tier1]
data_as_of: 2026-06-30
confidence: 高
---

# Astera Labs Q2 2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "Astera Labs Q2 2026 earnings revenue net income guidance"
- 搜索词: "Astera Labs Q2 2026 GAAP net income gross margin non-GAAP EPS Scorpio X-Series record revenue $392 million"
- 有效来源: Astera Labs 官方 IR 财报稿、Yahoo Finance、GuruFocus 电话会亮点、Futurum Group 深度解读、Edgen、MarketBeat、Nasdaq、Business Insider

## 关键数据（Q2 2026，财季截至 2026-06-30，2026-08-04 发布）

> 说明：Astera Labs 财年 = 自然年（截至每年 12 月底）。最新已发布为 Q2 2026。

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | $392.4M（历史新高） | YoY +104%，QoQ +27%，超共识 ~$360.85M |
| GAAP 净利 | $153.1M | 稀释 EPS $0.83（上年同期净利 $51.2M / EPS $0.29） |
| Non-GAAP 净利 | $145.8M | 稀释 EPS $0.80，超共识 $0.69 |
| GAAP 毛利率 | 73.3% | — |
| Non-GAAP 毛利率 | 73.7% | 高于指引 73% |
| Non-GAAP 营业利润率 | 39.1% | — |

## 指引（Q3 2026）

| 指标 | 新指引 | 对比 |
|------|--------|------|
| 营收 | $540-560M | QoQ +~40%（中点），远超共识 ~$416.6M |
| Non-GAAP 稀释 EPS | $1.16-1.21 | 共识 ~$0.81 |
| Non-GAAP 毛利率 | ~72% | 产品结构向 Switch/模块收入倾斜所致 |
| Non-GAAP 营业利润率 | ~43% | — |

## 驱动因素与展望
- Scorpio X-Series 320 通道 Fabric Switch 进入大批量生产部署（lead customer 量产）
- Scorpio AI Fabric Switch 达量产，预计 Q3 成为最大产品线（比预期提前一个季度）
- >10 家客户处于量产/预生产/验证阶段，单加速器 content 潜在 >$1,000
- AI 基础设施互联需求持续强劲，Q3 指引营收跳增 ~40%

## 来源
- Astera Labs 官方 IR 财报稿: https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-second-quarter-2026-financial-results
- Yahoo Finance 财报稿: https://finance.yahoo.com/technology/articles/astera-labs-reports-second-quarter-200500111.html
- Yahoo Finance 电话会亮点: https://sg.finance.yahoo.com/news/astera-labs-inc-alab-q2-050348738.html
- GuruFocus 电话会亮点: https://www.gurufocus.com/news/9004348/astera-labs-inc-alab-q2-2026-earnings-call-highlights-record-revenue-and-scorpiox-ramp-drive-104-yearoveryear-growth
- Futurum Group 深度解读: https://futurumgroup.com/insights/astera-labs-q2-fy-2026-earnings-pull-scorpio-switch-leadership-forward/
- Edgen: https://www.edgen.tech/zh/news/post/astera-labs-revenue-jumps-104-as-scorpio-fabric-switches-ramp
- MarketBeat: https://www.marketbeat.com/instant-alerts/astera-labs-nasdaqalab-announces-earnings-results-2026-08-04/
- Nasdaq: https://www.nasdaq.com/articles/alab-q2-earnings-call-puts-scorpio-ramp-ahead-schedule
- Business Insider: https://markets.businessinsider.com/news/stocks/astera-labs-reports-second-quarter-2026-financial-results-1036408198

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 营收 $392.4M（YoY+104%，QoQ+27%） | astera-labs | latest_revenue | 高 |
| GAAP 净利 $153.1M / Non-GAAP 净利 $145.8M | astera-labs | 财务状况表 | 高 |
| Non-GAAP 毛利率 73.7% | astera-labs | 财务状况表 | 高 |
| Non-GAAP 稀释 EPS $0.80 | astera-labs | 财务状况表 | 高 |
| Q3 指引营收 $540-560M、EPS $1.16-1.21 | astera-labs | one_liner / 最新季度详情 | 高 |
| Scorpio X 进入大批量生产、Q3 成为最大产品线 | astera-labs | one_liner / 最新季度详情 | 高 |
