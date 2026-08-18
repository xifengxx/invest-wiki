---
input_id: input_20260818_032
date: 2026-08-18
source_type: Web调研
source_name: "Advantest Q1 FY2027 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Advantest, 6857.T, 爱德万测试, Q1 FY2027, 海豚研究, Tier1]
data_as_of: 2026-07-29
confidence: 高
---

# Advantest Q1 FY2027 财报分析（海豚研究）

## 搜索记录
- 搜索词: "Advantest Q1 FY2027 earnings revenue net income guidance"
- 搜索词: "Advantest Q1 FY2027 gross margin June 2026 net sales 367.47 billion operating income"
- 有效来源: RTTNews、Smartkarma、The Elec、stockanalysis 财报电话会记录、japan-earnings.com、marketwatch

## 关键数据（Q1 FY2027，财季截至 2026-06-30，2026-07-29 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 净销售额 | ¥367.47B | YoY +39.3%（去年同期 ¥263.776B），超预测 ¥340.01B |
| 毛利率 | 69.5% | YoY +4.4pp |
| 营业利润 | ¥189.99B | YoY +53.3%（去年同期 ¥123.952B），超共识 ¥159.19B |
| 营业利润率 | 51.7% | YoY +4.7pp |
| 净利润 | ¥174.78B | YoY +93.8%（去年同期 ¥90.180B），超共识 ¥120.05B |
| 稀释 EPS | ¥239.89 | 去年同期 ¥122.80 |

## 指引（FY2027 全年，截至 2027-03-31，2026-07-29 上调）

| 指标 | 新指引 | 旧指引 | 变化 |
|------|--------|--------|------|
| 净销售额 | ¥1.714T | ¥1.420T | +20.7% |
| 营业利润 | ¥846.0B | ¥627.5B | +34.8% |
| 净利润 | ¥660.0B | ¥465.5B | +41.8% |
| 基本 EPS | ¥911.64 | ¥641.61 | — |

## 驱动因素与展望
- 增长驱动: AI 相关半导体与数据中心高性能存储器（HBM）测试需求激增，推理 AI 芯片测试需求「显著超出此前预期」
- 管理层指出全球半导体市场预计在 2026 日历年突破 $1 万亿美元
- 新指引超此前公司预测与市场共识（共识营业利润 ~¥708.5B、净利润 ~¥524.4B）
- 管理层强调 Q1 强劲表现、加速扩产、SoC 测试机市场份额提升为支撑，但对利润率可持续性保持审慎态度

## 对比上下文（FY2026，截至 2026-03-31）
- 上一财年净利润 ¥375.35B，净销售额 ¥1.128T

## 来源
- RTTNews: https://www.rttnews.com/3672020/advantest-q1-net-profit-surges-on-robust-ai-related-semiconductor-demand-lifts-annual-outlook.aspx
- Smartkarma: https://www.smartkarma.com/home/newswire/earnings-alerts/advantest-corp-6857-earnings-fy-operating-income-forecast-boosted-surpassing-estimates/
- The Elec: https://www.thelec.net/news/articleView.html?idxno=12645
- stockanalysis 财报电话会: https://stockanalysis.com/quote/tyo/6857/transcripts/655613-q1-2027/
- japan-earnings: https://japan-earnings.com/news/2026/07/6857-rev-20260728/

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 净销售额 ¥367.47B（YoY+39.3%） | advantest | latest_revenue | 高 |
| 毛利率 69.5% | advantest | 财务状况表 | 高 |
| 营业利润 ¥189.99B / 营业利润率 51.7% | advantest | 财务状况表 | 高 |
| 净利润 ¥174.78B | advantest | 财务状况表 | 高 |
| FY2027 全年指引 营收¥1.714T/营业利润¥846B/净利¥660B | advantest | one_liner / 最新季度详情 | 高 |
