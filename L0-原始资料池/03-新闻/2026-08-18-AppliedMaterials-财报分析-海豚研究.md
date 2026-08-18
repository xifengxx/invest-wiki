---
input_id: input_20260818_009
date: 2026-08-18
source_type: Web调研
source_name: "Applied Materials Q3 FY2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, Applied Materials, AMAT, 应用材料, Q3 FY2026, 海豚研究, Tier1]
data_as_of: 2026-07-26
confidence: 高
---

# Applied Materials Q3 FY2026 财报分析（海豚研究）

## 搜索记录
- 搜索词: "Applied Materials Q3 FY2026 earnings revenue net income guidance"
- 搜索词: "Applied Materials AMAT Q2 FY2026 earnings results revenue net income gross margin"
- 搜索词: "Applied Materials AMAT stock price market cap August 2026 shares outstanding"
- 有效来源: Nasdaq 财报电话会亮点、Futurum Group 深度解读、新浪财经跟踪报告、Yahoo Finance、stockanalysis、CNBC

## 关键数据（Q3 FY2026，财季截至 2026-07-26，2026-08-13 发布）

| 指标 | 数值 | 对比 |
|------|------|------|
| 总营收 | $9.12B（历史新高） | YoY +25%，QoQ +15%（史上最大环比增幅），超指引 $8.95B、超共识 $9.02B |
| 半导体系统 SSG | $7.04B | YoY +27% |
| AGS 服务 | $1.78B | YoY +22% |
| 其他 | $294M | 上季同期 $275M |
| Non-GAAP 净利 | $2.80B | YoY +41% |
| Non-GAAP 稀释 EPS | $3.50 | YoY +41%，QoQ +22%，超共识 ~$3.40 |
| Non-GAAP 毛利率 | 50.4% | YoY +150bps |
| Non-GAAP 营业利润率 | 34.0% | 历史新高，YoY +3.3pts |
| Non-GAAP 营业利润 | $3.10B | 上季同期 $2.25B |
| DRAM 收入（含 HBM） | — | YoY +52% |

## 指引（Q4 FY2026）

- 总营收: $10.25B ± $500M（区间 $9.75-10.75B），中点环比 +12.5%，超共识 $9.62B
- Non-GAAP 稀释 EPS: $4.02 ± $0.20，超共识 ~$3.71
- 半导体系统: ~$7.9B；AGS: ~$1.84B；其他: ~$510M
- Non-GAAP 毛利率: ~50.4%；Non-GAAP 营业费用: ~$1.58B

## 需求展望
- 增长驱动: AI 算力基础设施扩建，先进逻辑（GAA）、DRAM/HBM、先进封装（混合键合）
- 管理层上调 2026 日历年半导体系统增长展望（此前 >20% → >30%）
- 客户能见度异常延长至 2027 年（滚动 8 季度预测 + 更长交期订单），管理层预期 2027 年延续强劲增长

## 估值快照（2026-08-17 收盘）
- 股价: $535.31（当日 +5.55%）
- 市值: ~$425B
- 流通股: ~793.96M
- 52 周区间: $154.47 - $739.67

## 来源
- Nasdaq Q3 财报电话会亮点: https://www.nasdaq.com/articles/applied-materials-q3-earnings-call-highlights
- Nasdaq 利润率解读: https://www.nasdaq.com/articles/applied-materials-beat-everything-wall-streets-expectations-margins
- Futurum Group: https://futurumgroup.com/insights/applied-materials-q3-fy-2026-advanced-packaging-and-dram-accelerate-growth/
- Yahoo Finance: https://finance.yahoo.com/markets/stocks/articles/applied-materials-beat-everything-wall-150000742.html
- 新浪财经跟踪报告: http://stockfinance.sina.cn/stock/go.php/paper/reportid/840142860207/index.phtml
- stockanalysis 统计: https://stockanalysis.com/stocks/amat/statistics/

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| 总营收 $9.12B 创新高（YoY+25%） | applied-materials | latest_revenue | 高 |
| Non-GAAP 毛利率 50.4% | applied-materials | 财务状况表 | 高 |
| Non-GAAP 净利 $2.80B | applied-materials | 财务状况表 | 高 |
| Non-GAAP 稀释 EPS $3.50 | applied-materials | 财务状况表 | 高 |
| 市值 ~$425B | applied-materials | market_cap | 高 |
| Q4 指引营收 $10.25B、EPS $4.02 | applied-materials | one_liner / 最新季度详情 | 高 |
