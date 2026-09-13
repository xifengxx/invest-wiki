---
input_id: input_20260913_054
date: 2026-09-13
source_type: Web调研
source_name: "Databricks 融资/估值/ARR与AI数据平台战略（WebSearch 多源）"
source_url: "https://www.crn.com/news/ai/2026/databricks-raises-5b-in-latest-funding-round-discloses-latest-financial-performance-stats"
ingest_date: 2026-09-13
status: 已处理
tags: [Databricks, Lakehouse, Lakebase, Genie, 未上市, 估值, ARR]
data_as_of: 2026-08-13
confidence: 高
---

# Databricks 融资、估值与经营数据调研

> 归档说明：Databricks 为**未上市公司**（但有公开披露的融资与部分财务指标），采用「融资估值 + ARR」口径。

## 搜索记录
搜索词「Databricks 2026 valuation ARR revenue funding AI data platform」，2026-09-13。有效来源：Investing.com / CRN / Yahoo Finance / CMSWire / QZ / European Business Magazine / 100EC。

## 关键数据表

### 融资与估值

| 项 | 内容 |
|----|------|
| 时间 | **2026-08-13** |
| 金额 | **$50亿** 战略融资 |
| **投后估值** | **$1,900亿** |
| 领投 | **Coatue** |
| 参与方 | Blackstone、MGX、T. Rowe Price 顾问账户 |
| 新投资方 | **Sixth Street Growth**、BOND、Clearlake Capital、Point72、Premji Invest、TPG |
| 现有投资者 | a16z、Fidelity、Goldman Sachs Alternatives、GIC、Insight Partners、Morgan Stanley IM、NEA、Temasek、Thrive、Dragoneer、Franklin Templeton、Ontario Teachers'、J.P. Morgan Private Capital、WCM |
| 估值变化 | 7月曾以 **$1,880亿** term sheet 传出，最终以 **$1,900亿** 完成；较前一轮 **$1,340亿** 估值**上涨约42%** |
| **隐含倍数** | **约 27x 收入 run-rate** |

### 收入与经营指标

| 指标 | 值 |
|------|-----|
| **年化收入 run-rate** | **突破 $70亿**（Q2 FY2026，截至2026-07-31） |
| **同比增速** | **+80%以上** |
| **调整后自由现金流** | 过去12个月**为正** |
| **Lakehouse**（数据仓库） | 超 **$15亿** run-rate，**+100%以上 YoY** |
| **Lakebase**（2025推出，面向AI agent的serverless Postgres） | 超 **$1亿** run-rate |
| 大客户 | **超1,000家**客户年化支出 >$100万；**超100家** >$1,000万 |
| 平台覆盖 | **超20,000家组织**，含 **Fortune 500 的70%** |
| 净收入留存 | **>140%** |
| AI产品收入 | **$17亿** |

### AI 数据平台战略（三大产品）

| 产品 | 定位 |
|------|------|
| **Lakebase** | 面向AI agent工作负载的 serverless Postgres（实时运营数据） |
| **Genie** | "**AI coworker**"，将企业数据转化为答案与行动 |
| **Unity AI Gateway** | 多AI治理、模型路由与成本控制（据报道路由超**千万亿 tokens**） |

### 其他2026进展

- **扩展与微软的十年合作伙伴关系至2030年代**（含采用 Azure Cobalt，将 Genie 引入 Microsoft 工作流）
- 完成对安全SOC平台 **Panther** 的收购
- 推出营销/CDP产品 **CustomerLake**

## 关键判断

| 判断 | 依据 |
|------|------|
| **增长质量高但有隐忧** | ARR $70亿、+80%以上、净收入留存>140%、调整后FCF为正——但同时**毛利率在下降** |
| **毛利率下降是核心矛盾** | 欧洲商业杂志分析指出，**消费型AI的每次查询算力成本上升导致毛利率下降**——增长与成本同步上升，可能在结构上无法支撑软件式的27x倍数 |
| **IPO时点明确推后** | CEO Ali Ghodsi 称 Databricks "**极不可能**"在 Anthropic 或 OpenAI 之前 IPO |
| 战略契合客户痛点 | Ghodsi 称企业想要"记住上下文、给出准确答案、执行工作且不超预算"的agent；**token成本上升正推动客户寻求成本控制**（这是Unity AI Gateway的卖点） |

## ⚠️ 数据说明

- 前一轮估值$1,340亿的**时间口径不一**：一说2024年12月、一说2026年2月
- 毛利率下降幅度未在来源中给出具体数字

## Schema-Mapping

| 原文内容 | 映射到 L2 公司 | 映射字段 | 冲突 |
|---------|---------------|---------|:--:|
| "2026-08-13 募资$50亿 at $1,900亿估值" | Databricks | market_cap | 否 |
| "ARR突破$70亿、+80%以上" | Databricks | latest_revenue | 否 |
| "调整后自由现金流过去12个月为正" | Databricks | 融资与现金流 | 否 |
| "Lakehouse $15亿、Lakebase $1亿" | Databricks | 产品线详解 | 否 |
| "Genie/Unity AI Gateway/Lakebase三大产品" | Databricks | core_business | 否 |
| "毛利率因消费型AI成本下降" | Databricks | 关键风险 | 否 |
| "CEO称不太可能在OpenAI/Anthropic前IPO" | Databricks | 动态更新记录 | 否 |

## QA 自检
| # | 检查项 | 结果 |
|---|--------|------|
| 1 | 来源 | 1 次搜索，7+ 来源 ✓ |
| 2 | 覆盖 | 融资估值/收入/战略/其他进展 4 项 ✓ |
| 3 | 表格 | 4 张表全提取 |
| 4 | 数字 | 20+ 个 |
| 5 | 实体 | Databricks、Coatue、Blackstone、MGX、微软、Panther ✓ |
| 6 | 判断句 | 增长质量/毛利率矛盾/IPO时点 4 条 ✓ |
| 7 | **矛盾点标注** | "ARR高增但毛利率下降"已显式记录 ✓ |

自检结论：✅ 通过
