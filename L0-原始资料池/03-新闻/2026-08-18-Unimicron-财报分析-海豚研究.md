---
input_id: input_20260818_052
date: 2026-08-18
source_type: Web调研
source_name: "欣兴电子 Unimicron (3037.TW) Q2 2026 财报（海豚研究）"
source_url: "多源（见正文）"
ingest_date: 2026-08-18
status: 已处理
tags: [财报, 欣兴电子, Unimicron, 3037.TW, ABF载板, Q2 2026, 海豚研究, Tier1]
data_as_of: 2026-06-30
confidence: 高
---

# 欣兴电子 Unimicron Q2 2026 财报分析（海豚研究）

> 口径说明：欣兴电子财年=自然年，Q2 2026 = 2026年4-6月（截止 2026-06-30），2026-07-29 法说会发布，为当前「最新已发布」财报。Q3 2026 财报预计 2026年10月底发布。

## 搜索记录
- 搜索词 1: "欣兴电子 Unimicron Q2 2026 earnings revenue net income"
- 搜索词 2: "欣興 3037 Q2 2026 毛利率 24.08% 淨利 131億 EPS 8.45 營收 428.9億"
- 有效来源: CMoney、工商時報 CTEE、中時新聞網、優分析 UAnalyze、永豐金證券（Sinotrade）、MarketScreener、BigGo Finance
- 被拦截: ctee.com.tw / api.cmoney.tw / finance.biggo.com 直接抓取连接被拒（ECONNREFUSED），改用 WebSearch 摘要 + 優分析（uanalyze.com.tw）正文成功

## 关键数据（Q2 2026，2026-07-29 发布，截止 2026-06-30）

| 指标 | 数值 | 环比 | 同比 |
|------|------|------|------|
| 合并营收 | NT$428.90亿 | +14.54% | +32.11%（创单季历史新高） |
| 毛利率 | 24.08%（部分媒体报24.80%） | +6.84pp | +11.72pp |
| 归母净利 | NT$131.15亿 | +160%（+1.6倍） | +441倍（去年同期仅NT$0.30亿） |
| EPS | NT$8.45 | — | 创历史新高 |

## 上半年累计（H1 2026）

- 合并营收 NT$803.36亿
- 税后净利 NT$181.58亿（YoY +1,823%）〔注：另有来源报193.56亿，与「Q2季增1.6倍」矛盾，采用181.58亿（与EPS 11.70×股本一致）〕
- EPS NT$11.70

## 结构数据与展望

- **AI产品营收占比**：上半年已超60%，下半年可望提升至65%~70%
- **ABF载板**：营收占比由Q1的49%升至Q2的52%；营收QoQ +22%、YoY +51%，为Q2成长最强产品线；ABF/BT/HDI/PCB各线稼动率均达9成以上
- **毛利率提升主因**：售价调涨、产能利用率提升、良率改善
- **Q3 2026 展望**：营收及毛利率均可望续扬；7月营收 NT$162.54亿（MoM +9.11%、YoY +43.69%），续创单月新高
- **资本开支**：2026全年CAPEX由NT$340亿上调至约NT$537亿，80%以上投入ABF载板扩产；杨梅二厂Q2已动土、三厂预计2026年底动土

## 来源
- CMoney（26Q2財報公告：Q2營收428.8982億創歷史新高，季增14.54%、年增32.11%）: https://api.cmoney.tw/notes/note-detail.aspx?nid=1242040
- 工商時報 CTEE（欣興Q2每股賺8.45元寫新高）: https://www.ctee.com.tw/news/20260729700220-430502
- 中時新聞網（欣興Q2每股賺8.45元寫新高）: https://www.chinatimes.com/newspapers/20260729000330-260206
- 優分析 UAnalyze（Q2毛利率24.08%、稅後純益131.15億、EPS8.45；AI產品營收占比已達6成）: https://uanalyze.com.tw/articles/1516352408
- 永豐金證券 Sinotrade（欣興Q2純益131億元創高，上半年純益193.56億元EPS11.7元）: https://scm.sinotrade.com.tw/Article/Inner/9d5e991a-25a1-4f0d-bcd1-4ebce8a88bcf
- MarketScreener（Q2 sales TWD 42,889.82M vs TWD 32,466.05M a year earlier）: https://sa.marketscreener.com/news/unimicron-technology-corp-reports-earnings-results-for-the-second-quarter-and-six-months-ended-june-ce7f51ddd08bf127
- BigGo Finance（Earnings Call 2026-07-29）: https://finance.biggo.com/quote/3037.TW/earnings-call/TW_3037.TW_2026-07-29
- CMoney（法說會：Blackwell訂單塞爆，ABF缺貨到後年）: https://api.cmoney.tw/notes/note-detail.aspx?nid=1242412

## Schema-Mapping

| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
| Q2 2026 合并营收 NT$428.90亿 +14.54% QoQ / +32.11% YoY 创单季历史新高 | unimicron | latest_revenue | 高 |
| 毛利率 24.08% +6.84pp QoQ / +11.72pp YoY | unimicron | 财务状况表 | 高 |
| 归母净利 NT$131.15亿 +160% QoQ / +441倍 YoY；EPS NT$8.45 创历史新高 | unimicron | 财务状况表 | 高 |
| 上半年营收 NT$803.36亿，税后净利 NT$181.58亿，EPS NT$11.70 | unimicron | 财务状况表 | 高 |
| AI产品营收占比上半年超6成，H2看65-70% | unimicron | body Q2详情 | 高 |
| ABF载板占比Q1 49%→Q2 52%，QoQ+22%/YoY+51% | unimicron | body Q2详情 | 高 |
| 2026 CAPEX NT$340亿→NT$537亿，80%+投ABF | unimicron | body Q2详情 | 高 |
| Q3营收及毛利率续扬；7月营收NT$162.54亿续创单月新高 | unimicron | body Q2详情 | 高 |
