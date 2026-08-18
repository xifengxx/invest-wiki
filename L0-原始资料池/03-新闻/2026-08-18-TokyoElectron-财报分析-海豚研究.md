---
input_id: input_20260818_012
date: 2026-08-18
source_type: Web调研
source_name: "Tokyo Electron Q1 FY2027 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Tokyo Electron, 东京电子, 8035.T, TEL, Q1 FY2027, 海豚研究, Tier1]
data_as_of: 2026-06-30
confidence: 高
---

# Tokyo Electron Q1 FY2027 财报分析（海豚研究）

## 搜索记录
- 搜索词1: "Tokyo Electron Q1 FY2027 earnings revenue net income guidance April-June 2026"
- 搜索词2: "東京エレクトロン 2027年3月期 第1四半期 決算 売上高 純利益"
- 时间: 2026-08-18
- 有效来源: BigGo Finance 财报电话会摘要、Investing.com Q1 FY2027 幻灯片、SEMI 中国转载、东京电子 IR、乐天证券決算レポート

## 关键数据（Q1 FY2027，财季截至 2026-06-30，2026-07-30 发布）

> 财年截至 3 月底，Q1 FY2027 = 2026 年 4-6 月。

| 指标 | 数值 | 对比 |
|------|------|------|
| 营收 | ¥732.3B（约 $4.6B，单季历史新高） | YoY +33.3% |
| 营业利润 | ¥211.4B | YoY +46.1%，营业利润率 28.9% |
| 毛利润 | ¥342.7B | YoY +34.9%，毛利率 46.8% |
| 归母净利润 | ¥164.3B（¥164.341B） | YoY +39.5% |
| 现场解决方案（Field Solutions）营收 | ¥188B | — |

增长驱动：AI 数据中心/半导体设备需求旺盛，先进逻辑（GAA）、DRAM/HBM、NAND 各段全面增长，现场解决方案收入强劲。

## 指引（上修）

### 上半年 FY2027（2026 年 4-9 月）上修
- 营收: **¥1.62T**（上修，创历史半年纪录）
- 营业利润: **¥458B**
- 净利润: **¥349B**（约 $2.2B，YoY +44.4%）

### Q2 FY2027（2026 年 7-9 月）预测
- 营收: **¥887.6B**（YoY +40.9%）
- 营业利润: **¥246.6B**（YoY +55.6%）

### WFE（晶圆厂设备）市场展望
- CY2026 上调至 **$150B 以上**
- CY2027 上调至 **$190B 以上**（AI 投资加速驱动）

## 来源
- BigGo Finance 财报电话会摘要（2026-07-30）: https://finance.biggo.com/news/JP_8035.T_2026-07-30
- BigGo Finance 上修净利润指引报道: https://finance.biggo.com/news/2d60aaf6-c7b1-4ef1-a03e-2e8307b8db6e
- Investing.com Q1 FY2027 幻灯片: https://au.investing.com/news/company-news/tokyo-electron-q1-fy2027-slides-ai-boom-drives-record-sales-outlook-93CH-4567305
- SEMI 中国转载（归母净利润 ¥1643.41 亿日元）: https://www.semi.org.cn/site/semi/article/f4033729040544bb91a319256c129b1d.html
- 东京电子 IR 财报发布页: https://www.tel.com/ir/library/report/index.html
- 乐天证券決算レポート: https://media.rakuten-sec.net/articles/-/53215

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| Q1 FY2027 营收 ¥732.3B（YoY +33.3%，单季历史新高） | tokyo-electron | latest_revenue | 高 |
| 归母净利润 ¥164.3B（YoY +39.5%） | tokyo-electron | 财务状况表 | 高 |
| 营业利润 ¥211.4B（YoY +46.1%），营业利润率 28.9% | tokyo-electron | 财务状况表 | 高 |
| 毛利润 ¥342.7B，毛利率 46.8% | tokyo-electron | 财务状况表 | 高 |
| 上半年 FY2027 营收 ¥1.62T、净利润 ¥349B 上修 | tokyo-electron | one_liner / body | 高 |
| Q2 FY2027 预测营收 ¥887.6B、营业利润 ¥246.6B | tokyo-electron | body（最新季度详情） | 高 |
| WFE 展望 CY2026 >$150B、CY2027 >$190B | tokyo-electron | body（最新季度详情） | 高 |
| 现场解决方案营收 ¥188B | tokyo-electron | body（最新季度详情） | 高 |
