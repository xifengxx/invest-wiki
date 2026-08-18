---
input_id: input_20260818_050
date: 2026-08-18
source_type: Web调研
source_name: "Technoprobe H1 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Technoprobe, TPRO.MI, 探针卡, H1 2026, Q2 2026, 海豚研究, Tier1]
data_as_of: 2026-08-05
confidence: 高
---

# Technoprobe H1 2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "Technoprobe earnings revenue net income 2026"
- 搜索词: "Technoprobe H1 2026 results net profit August 2026 revenue 464 million"
- 有效来源: Investing.com、Seeking Alpha、Smartkarma、Technoprobe 官方 IR PDF、TipRanks、stockanalysis

## 关键数据（H1 2026，财季截至 2026-06-30，2026-08-05 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | €464.1M | YoY +42.4%（H1 2025 €325.9M），HoH +48.2%，超预期 €455.8M |
| 毛利润 | €249.6M | YoY +65.7% |
| 毛利率 | 53.8% | YoY +7.6pp（去年同期 46.2%） |
| EBITDA | €206.2M | YoY +93.8%，超预期 €192.8M |
| EBITDA 利润率 | 44.4% | YoY +11.8pp（去年同期 32.6%） |
| 净利润 | €125.7M | YoY ~3.8x（H1 2025 €33.2M） |
| 基本 EPS | €0.187 | 去年同期 €0.0513（~3.6x） |
| 净现金头寸 | €685.9M | 2026-06-30（2025 年末 €684.2M） |

## Q2 2026 单季数据（嵌入 H1 报告）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | €277.1M | YoY +64.3%，QoQ +48.2%，历史单季纪录 |
| 毛利率 | 57.2% | — |
| EBITDA 利润率 | 49.4% | — |

## Q1 2026 单季数据（2026-05-14 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | €187.0M | YoY +19%，QoQ +15.6% |
| 毛利润 | €91.1M | YoY +28.7%，毛利率 48.7% |
| EBITDA | €69.2M | YoY +44.2%，利润率 37.0% |
| 净利润 | €64.47M | 上季 €33.20M |
| 净现金头寸 | €660.5M | 2026-03-31 |

## 指引（FY2026 全年，2026-08 上调）

| 指标 | 新指引 | 备注 |
|------|--------|------|
| 全年营收 | €950M–€1.05B | 原为 2027 目标，加速至 2026 并上调 |
| 全年 EBITDA 利润率 | 44%–46% | — |
| Q3 2026 营收 | €314M | — |

## 驱动因素与展望
- 增长驱动: AI/数据中心相关晶圆测试需求激增，探针卡（Probe Card）ASP 与需求量双升，管理层称「长期 AI 投资周期持续加速」
- 汇率逆风: 对报表营收有 >6% 不利影响，固定汇率下 H1 营收约高 €30M
- 市场反应: 5 月 15 日 Q1 财报后股价单日暴涨 36%（创纪录业绩 + 指引加速）
- 毛利率改善主因: AI 高端 MEMS 探针卡占比提升 + 强经营杠杆

## 来源
- Technoprobe Q1 2026 Results（官方 IR）: https://www.technoprobe.com/wp-content/uploads/2026/05/Q1-2026-Results.pdf
- Technoprobe Q1 2026 CS: https://www.technoprobe.com/wp-content/uploads/2026/05/Q1-26-CS.pdf
- Investing.com（Q1 股价暴涨 36%）: https://za.investing.com/news/stock-market-news/technoprobe-shares-surge-36-as-q1-profit-jumps-targets-accelerated-4282913
- Investing.com（H1 2026 slides）: https://za.investing.com/news/company-news/technoprobe-h1-2026-slides-ai-surge-drives-record-margins-upgraded-outlook-93CH-4409686
- Seeking Alpha（Q2 2026 财报电话会文字记录）: https://seekingalpha.com/article/4931035-technoprobe-s-p-a-thnby-q2-2026-earnings-call-transcript
- Investing.com（Q2 2026 财报电话会文字记录）: https://www.investing.com/news/transcripts/earnings-call-transcript-technoprobe-posts-record-q2-2026-revenue-raises-outlook-93CH-4838882
- Smartkarma（H1 超预期）: https://www.smartkarma.com/home/newswire/earnings-alerts/technoprobe-tpro-earnings-1h-revenue-surpasses-estimates-with-strong-ebitda-performance/

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| H1 2026 营收 €464.1M（+42.4% YoY）/ Q2 单季 €277.1M（+64.3%） | technoprobe | latest_revenue | 高 |
| 毛利率 53.8%（H1）/ 57.2%（Q2） | technoprobe | 财务状况表 | 高 |
| 净利润 €125.7M（H1，YoY ~3.8x） | technoprobe | 财务状况表 / 最新季度详情 | 高 |
| EBITDA €206.2M / 利润率 44.4% | technoprobe | 最新季度详情 | 高 |
| FY2026 指引上调至营收 €950M-€1.05B、EBITDA 利润率 44-46% | technoprobe | one_liner / 最新季度详情 | 高 |
