---
input_id: input_20261010_004
date: 2026-10-10
source_type: Web调研
source_name: "Ultra Clean Holdings（UCT，NASDAQ: UCTT）分部结构、客户集中度、并购与资本结构、可转债与产能路线图（WebSearch + 10-K/8-K 多源）"
source_url: "https://www.uct.com/investors/financial-information/quarterly-results"
ingest_date: 2026-10-10
status: 已处理
tags: [UltraClean, UCT, UCTT, 半导体设备子系统, 气体输送模块, 洁净室, 服务业务, AppliedMaterials, LamResearch, 可转债, 商誉减值]
data_as_of: 2026-10-09
confidence: 高
---

# Ultra Clean Holdings (UCT) 调研（input_20261010_004）

## 归档目的

补齐 `L2-Wiki/公司/ultra-clean.md` 的正文缺口。该页正文薄弱，`## 产品线详解` 与 YAML `core_business` 逐字重复。本次调研定位在「YAML 卡片渲染不出来的维度」：分部结构（Products vs Services 及其毛利率差异）、客户集中度的历史趋势、六笔并购的金额与倍数、2025 年商誉减值、可转债与利息结构、产能路线图、中国 vs 欧洲营收迁移。

**⚠️ 本归档含一节「不要写入的（已排除项）」** —— 调研过程中出现若干看似合理但经核实站不住的说法，必须排除，不得进入 L2。

**可信度图例**：`[10-K]` = 年报；`[8-K]`/`[IR]` = 公司公告与投资者关系；`[电话会]` = 财报电话会；`[法人估]` = 分析师推算。

---

## 搜索记录

1. Ultra Clean Holdings UCTT 2026 Q2 results revenue
2. UCT 分部 Products Services revenue gross margin
3. UCT 大客户 Applied Materials Lam Research 占比
4. Ultra Clean customer concentration 10-K
5. Ultra Clean acquisitions Marchi Miconex QGT DMS Ham-Let HIS
6. Ultra Clean goodwill impairment 2025
7. UCT convertible notes 2031 interest rate
8. Ultra Clean Term Loan B repayment interest expense
9. Ultra Clean capacity roadmap Malaysia cleanroom
10. UCT China revenue Austria revenue shift
11. Ultra Clean 2026 CFO COO changes
12. UCT ATM equity program 400 million
13. Ultra Clean 2026 Q3 earnings date
14. UCT stock price target analyst
15. Ultra Clean non-semiconductor revenue

---

## 关键页面内容摘要

### 1. 分部结构（10-K，确切）

**UCT 只有 2 个报告分部**：

| 分部 | 收入占比 | 毛利率 |
|---|:--:|:--:|
| **Products** | 约 **88%** | **15.1%** |
| **Services** | 约 **12%** | **28.9%** |

- **Services 毛利率 28.9% 是 Products 的 1.9 倍**，但 Services 的 TAM 仅约 **US$2.0–2.5B**（相对 Products 的 TAM 小一个量级）
- 来源：10-K / 财报 `[10-K]`

**判断（核心矛盾）**：这是 UCT 的结构性困局——**高毛利的分部天花板低（Services TAM 20–25 亿），低毛利的分部占 88% 收入**。管理层反复强调 Services 增长，但它撑不起整体毛利率的重估。

### 2. 客户集中度（10-K，确切）

- **10-K 只点名 2 家 >10% 客户**：**Applied Materials** 与 **Lam Research**
- 两者合计 **58.7%**（FY2025）
- 公司自绘图趋势：**67%（2020）→ 59%（2025）**，即集中度在缓慢下降（但仍是极高集中）
- 来源：10-K `[10-K]`

### 3. 终端市场结构（电话会，确切）

- **非半导体仅占营收 4%**（Q1 2026）
- Q1 2026 终端结构：**Foundry & Logic WFE 52% / Memory 31% / Service 13% / Non-semi 4%**
- 来源：财报电话会 `[电话会]`

**判断**：非半导体只占 4%——任何「业务多元化」的叙事在数字上都不成立。UCT 是纯 WFE 周期股。

### 4. 营收地区结构迁移（10-K，确切）

- **中国**：US$214.7M → **US$143.1M**（**腰斩**）
- **奥地利**：US$98.5M → **US$221.5M**（**翻倍以上**）
- 来源：10-K `[10-K]`

### 5. 六笔并购（10-K / 公告，确切）

| 标的 | 对价 | EBITDA 倍数 |
|---|---|---|
| Marchi | US$43.6M | — |
| Miconex | US$22.8M | — |
| QGT | **US$342.0M** | — |
| DMS | US$30.0M | **5.4x** |
| Ham-Let | **US$351M** | **8.3x** |
| HIS | US$50M | **8.3x** |

- 来源：10-K `[10-K]`

### 6. 商誉减值与 2025 年业绩（10-K，确切）

- **2025 年商誉减值 US$151.1M**：Products/Fluid Solutions **US$77.6M** + Services **US$73.5M**
- 导致 **FY2025 营业亏损 US$107.4M**、**EPS -$4.00**
- 来源：10-K `[10-K]`

### 7. 资本结构与可转债（8-K，确切）

- **US$600M 0.00% 可转债（2031 到期）**
- 同时**全额偿还 Term Loan B**，利息成本从约 **6.2% 降至约 1.4%**
- 可转债**公允价值在外 US$982.4M**
- **US$25.1M capped call**，行权价 **$84.75 / $104.0725**
- 来源：8-K `[8-K]`

### 8. 现金流与营运资本（10-K，确切）

- **H1 2026 经营现金流 -US$74.4M**，同期**存货增加 US$238.9M**
- **存货 US$629.9M = 总资产的 22.6%**
- **Q2 2026 GAAP 有效税率 60.3%**
- 来源：10-K `[10-K]`

### 9. 产能路线图（电话会，确切）

| 时点 | 产能目标 |
|---|---|
| 2026 年底 | US$3.5B |
| 2027 年中 | US$4B |
| 2028 H2 | US$5B |

- 含**马来西亚 +26,000 平方英尺洁净室**
- 来源：电话会 `[电话会]`

### 10. 季度营收序列（10-Q / 公告，确切）

| 季度 | 营收 |
|---|---|
| Q2 2025 | US$518.8M |
| Q3 2025 | US$510.0M |
| Q4 2025 | US$506.6M |
| Q1 2026 | US$533.7M |
| **Q2 2026** | **US$644.9M** |

- **Q2 2026 营收 US$644.9M，超出公司自身指引 US$565–605M**
- **⚠️ 数据更正**：另有一处来源写作 **US$552.1M** —— 该数字与上表任何一季都不吻合，**为错误数据，不得写入**。
- 来源：10-Q / 财报 `[10-Q]`

### 11. 管理层变动（2026，确切口径）

| 日期 | 事件 |
|---|---|
| 2026-03-23 | Wunar 任 COO |
| 2026-04-23 | Granger → Edman 接任董事长 |
| 2026-04-28 | Savage 宣布 CFO 退休 |
| 2026-08-05 | Keogh 正式接任 CFO |
| 2026-09-30 | Davern 加入董事会 |

- **US$400M ATM 于 2026-08-14 提交**
- **Q3 2026 财报预定 2026-10-27**
- 来源：8-K `[8-K]`

### 12. 股价与估值分歧（市场，确切）

- **2026-10-09 收盘 $68.59**，52 周区间 **$21.49–$144.22**
- 分析师共识目标价 **$132.83（strong buy）**
- **GuruFocus GF Value 仅约 $34.64**
- 来源：市场数据 `[确切]`

**⚠️ 写入要求**：两个方向必须同时保留（共识看多 $132.83 vs GF Value 看空 $34.64），不得只取一方。

---

## 数据提取清单

| 数据点 | 值 | 来源 | 置信度 |
|---|---|---|---|
| 报告分部数 | **2 个**（Products / Services） | 10-K | [10-K] |
| 分部占比 | Products 约 88% / Services 约 12% | 10-K | [10-K] |
| 分部毛利率 | Products 15.1% / **Services 28.9%** | 10-K | [10-K] |
| Services TAM | US$2.0–2.5B | 10-K/电话会 | [10-K] |
| >10% 客户数 | **2 家**（Applied Materials、Lam Research） | 10-K | [10-K] |
| 前二客户合计 | **58.7%**（FY2025） | 10-K | [10-K] |
| 前二客户趋势 | 67%（2020）→ 59%（2025） | 公司图表 | [10-K] |
| 非半导体占比 | **4%**（Q1 2026） | 电话会 | [电话会] |
| 终端结构 Q1 2026 | Foundry & Logic WFE 52% / Memory 31% / Service 13% / Non-semi 4% | 电话会 | [电话会] |
| 中国营收 | US$214.7M → US$143.1M | 10-K | [10-K] |
| 奥地利营收 | US$98.5M → US$221.5M | 10-K | [10-K] |
| 并购 Marchi | US$43.6M | 10-K | [10-K] |
| 并购 Miconex | US$22.8M | 10-K | [10-K] |
| 并购 QGT | US$342.0M | 10-K | [10-K] |
| 并购 DMS | US$30.0M @ 5.4x EBITDA | 10-K | [10-K] |
| 并购 Ham-Let | US$351M @ 8.3x EBITDA | 10-K | [10-K] |
| 并购 HIS | US$50M @ 8.3x EBITDA | 10-K | [10-K] |
| 2025 商誉减值 | US$151.1M（Products/Fluid Solutions 77.6M + Services 73.5M） | 10-K | [10-K] |
| FY2025 营业损益 | 营业亏损 US$107.4M，EPS -$4.00 | 10-K | [10-K] |
| 可转债 | US$600M 0.00%（2031 到期） | 8-K | [8-K] |
| 利息成本变化 | 约 6.2% → 约 1.4%（偿清 Term Loan B） | 8-K | [8-K] |
| 可转债在外公允价值 | US$982.4M | 8-K | [8-K] |
| Capped call | US$25.1M，$84.75 / $104.0725 | 8-K | [8-K] |
| H1 2026 经营现金流 | **-US$74.4M** | 10-K/10-Q | [10-K] |
| 存货变动 | 增加 US$238.9M | 10-K | [10-K] |
| 存货水平 | US$629.9M = 总资产 22.6% | 10-K | [10-K] |
| Q2 2026 有效税率 | GAAP 60.3% | 10-Q | [10-Q] |
| 产能路线图 | US$3.5B（2026 年底）→ US$4B（2027 中）→ US$5B（2028 H2） | 电话会 | [电话会] |
| 马来西亚洁净室 | +26,000 平方英尺 | 电话会 | [电话会] |
| Q2 2025 营收 | US$518.8M | 10-Q | [10-Q] |
| Q3 2025 营收 | US$510.0M | 10-Q | [10-Q] |
| Q4 2025 营收 | US$506.6M | 10-Q | [10-Q] |
| Q1 2026 营收 | US$533.7M | 10-Q | [10-Q] |
| **Q2 2026 营收** | **US$644.9M**（vs 公司指引 US$565–605M） | 10-Q | [10-Q] |
| 管理层变动 | Wunar COO 2026-03-23；Granger→Edman 董事长 2026-04-23；Savage CFO 退休 2026-04-28；Keogh CFO 2026-08-05；Davern 入董事会 2026-09-30 | 8-K | [8-K] |
| ATM | US$400M，2026-08-14 提交 | 8-K | [8-K] |
| Q3 2026 财报日 | 2026-10-27 | IR | [IR] |
| 股价 | 2026-10-09 收 $68.59；52 周 $21.49–$144.22 | 市场 | [确切] |
| 分析师共识目标价 | $132.83（strong buy） | 市场 | [法人估] |
| GuruFocus GF Value | 约 $34.64 | 市场 | [法人估] |

---

## 不要写入的（已排除项）

以下说法在调研过程中出现，但经核实**站不住脚**，**严禁进入 L2 正文或 YAML**：

| 被排除的说法 | 排除理由 |
|---|---|
| **memsstar / SIMS / Chemcos 三笔收购** | **未证实**。memsstar 是苏格兰的 MEMS 设备商，与 UCT 无关；「SIMS」实为子公司 ChemTrace 提供的二次离子质谱 (SIMS) 检测服务，不是一家被收购的公司；「Chemcos」疑为 ChemTrace 的误写。三者均**不得写入**。 |
| **超纯水业务** | 已检索，**未找到** UCT 有此项业务 |
| **生命科学业务** | 已检索，**未找到** |
| **数据中心液冷业务** | 已检索，**未找到** |
| **「三大板块」** | UCT **只有 2 个报告分部**（Products / Services），「三大板块」为错误表述 |
| **「三个大客户」** | 10-K **只点名 2 家 >10% 客户**（Applied Materials、Lam Research），「三个大客户」为错误表述 |
| **RF 发生器（RF Generator）** | **不是 UCT 的产品** |
| **Q2 2026 营收 $552.1M** | **数据错误**。正确值为 **$644.9M**；上表五个季度中没有任何一季等于 $552.1M。**若 L2 或其他页面存在 $552.1M，须更正。** |

---

## 被拦截/失败记录

| 目标 | 状况 |
|---|---|
| UCT 官网部分投资者子页 | 需多路径尝试，部分数据取自 SEC 文件 |
| 超纯水 / 生命科学 / 数据中心液冷业务 | 检索未命中，已列为排除项 |

---

## 未找到 / 待补

1. QGT、Marchi、Miconex 三笔并购的 **EBITDA 倍数**（仅 DMS/Ham-Let/HIS 有）
2. **Services 分部的客户构成**
3. **各终端市场（Foundry & Logic / Memory / Service / Non-semi）的收入绝对值**（仅有占比）
4. **2026 Q3 实际业绩**（预定 2026-10-27 发布，晚于本次调研）

---

## Schema-Mapping

| L0 内容 | → ultra-clean.md 正文段落 | 处理方式 |
|---|---|---|
| 2 分部结构 + 毛利率差 + Services TAM | `## 产品线详解`（改写为分部表） | **替换**现有与 YAML core_business 逐字重复的 bullet 列表 |
| 客户集中度 + 终端结构 + 地区迁移 | `## 客户与收入结构` | 新增 `##` 段 |
| 六笔并购金额与倍数 + 2025 商誉减值 | `## 并购与商誉` | 新增 `##` 段 |
| 可转债 + 利息结构 + capped call | `## 资本结构与现金流` | 新增 `##` 段 |
| 产能路线图 + 马来西亚洁净室 | `## 产能路线图` | 新增 `##` 段 |
| 季度营收序列（含 $644.9M 更正） | `## 财务状况` | **追加/更正**（不替换现有表结构） |
| 管理层变动 + ATM + 财报日 + 股价与估值分歧 | `## 最新动态（2026）` | 新增 `##` 段 |
| 排除项清单 | 不入正文 | **仅归档**，作为负面约束 |
| 前端已渲染的 YAML 字段 | 不改 YAML 结构 | 仅 `one_liner`/`description` 追加更新段；`latest_revenue`/`data_freshness_date`/`updated` 替换 |
