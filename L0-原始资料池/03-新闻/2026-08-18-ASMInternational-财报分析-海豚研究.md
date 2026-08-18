---
input_id: input_20260818_035
date: 2026-08-18
source_type: Web调研
source_name: "ASM International Q2 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, ASM International, ASM.AS, ASMI, 原子层沉积, Q2 2026, 海豚研究, Tier1]
data_as_of: 2026-06-30
confidence: 高
---

# ASM International Q2 2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "ASM International Q2 2026 earnings revenue net income guidance"
- 有效来源: Investing.com、GlobeNewswire 官方 press release、stockanalysis 电话会、Yahoo Finance、GuruFocus

## 关键数据（Q2 2026，2026-07-28 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 总营收 | €1,003M（€1.003B） | 历史新高，首次突破 €10亿；+20% YoY（固定汇率 +24%），环比 +15%；超指引中点 €980M（±5%） |
| 净利 | €285.4M | Q1 2026 €238.5M；Q2 2025 €202.4M |
| 调整后净利 | €292.9M | YoY +€120M（Q2 2025 €173.0M） |
| 调整后 EPS | $6.78（ADR 口径） | 超共识 $6.46 |
| 毛利率 | 51.9% | — |
| 调整后营业利润率 | 33.0% | Q1 2026 纪录 33.1% 基本持平 |
| 自由现金流 | €355M | 创纪录 |
| 现金 | €1.18B | 零负债 |
| CapEx | €63M | 全年预期上调（Scottsdale 新厂加速） |

## 指引

### Q3 2026
- 营收: 约 €1.1B（±5%，固定汇率）

### H2 2026
- 营收: 较 H1 增长 >20%（固定汇率），驱动为先进逻辑/代工（含 1.4nm 初始贡献）、存储增长、功率/模拟/晶圆复苏

### 全年 2026
- 营收: 超 €4B
- 毛利率指引: 约 51%（低于共识 51.5%，致财报后股价一度跌 8%）

### 2027 展望（上调）
- 营收: 超此前 €3.7-4.6B 区间上限（即 >€4.6B），受益于强劲订单与 WFE 支出预期上修

## 需求展望
- 增长驱动: 先进 AI 芯片制造设备、ALD 销售创新高、先进逻辑/代工（含 2nm）、HBM DRAM、中国成熟制程
- 管理层: 宣布 2026-2027 €150M 回购计划
- 风险: 中国能见度低（潜在出口管制影响）、供应链承压

## 来源
- Investing.com: https://www.investing.com/news/earnings/asm-beats-own-q2-revenue-guidance-sees-stronger-second-half-4817780
- GlobeNewswire 官方: https://www.globenewswire.com/de/news-release/2026/07/28/3334553/0/en/asm-reports-second-quarter-2026-results.html
- stockanalysis 电话会: https://stockanalysis.com/quote/ams/ASM/transcripts/549315-q2-2026/
- Yahoo Finance: https://ca.finance.yahoo.com/news/asm-international-nv-asmiy-q2-210122558.html
- Investing.com slides: https://www.investing.com/news/company-news/asm-q2-2026-slides-record-revenue-tops-1b-2027-outlook-raised-93CH-4820816
- GuruFocus: https://www.gurufocus.com/news/8987597/asm-international-nv-asmiy-q2-2026-earnings-call-highlights-record-revenue-and-strong-growth-amid-challenges

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 营收 €1,003M 首破 €10亿（+20% YoY） | asm-international | latest_revenue | 高 |
| 毛利率 51.9% | asm-international | 财务状况表 | 高 |
| 净利 €285.4M | asm-international | 财务状况表 | 高 |
| Q3 指引 €1.1B，FY2026 >€4B，2027 上调 >€4.6B | asm-international | one_liner / 最新季度详情 | 高 |
