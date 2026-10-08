---
name: Celestica
slug: celestica
country: CA
ticker: CLS
type: company
updated: 2026-10
data_freshness_date: 2026-10-08
segments:
- AI服务器
- 网络设备（交换机）
one_liner: |
  加拿大 EMS/ODM 厂商，1994 年自 IBM 分拆成立，为 Meta、Google、Amazon 等超大规模云厂商代工 800G/1.6T 数据中心以太网交换机与 AI 服务器机架；据 Dell'Oro，2026 Q1/Q2 在 AI 后端以太网交换机市场单独份额已列第一（与 NVIDIA 合计约占 50%），位于产业链L3核心产品与集成层。
  【2026.10.8更新】2026 Q2 营收 $47.0 亿（YoY +62%）、经调整 EPS $2.54（+83%）；2025 全年营收 $123.909 亿（+28%）、经调整 EPS $6.05；2026 全年指引营收 $205 亿（约 +65%）。
chain_layer: L3
chain_role: 龙头
suppliers:
- company: Broadcom
  ticker: AVGO
  supplies: 交换 ASIC（Tomahawk 系列）
  note: 核心芯片供应商——DS6000 系列 1.6TbE 交换机基于 Tomahawk 6（TH6）；博通占交换 ASIC 市场约 70%
- company: 其他上游（GPU、存储、PCB、光引擎、电源与散热）
  supplies: 服务器与交换机零组件
  note: 具体供应商名单未披露；公司称计算侧瓶颈在存储，网络侧瓶颈在 PCB 与芯片
customers:
- company: Meta Platforms
  note: 公司文件明确点名的 CCS 客户；2026 Q2 三家 CCS 客户各占营收 >10%（32%/17%/14%，未披露谁占多少）
- company: Alphabet / Google
  note: TPU 项目的首选制造伙伴（非独家）
- company: Amazon
  note: 公司文件点名（Amazon Fulfillment Services, Inc.）
- company: IBM / HPE / Dell / Ciena / Juniper
  note: 其他 CCS 客户（公司文件点名）
- company: Microsoft
  note: 仅见于市场与卖方评论，未见于 10-K 客户清单，置信度低
- company: Applied Materials / Lam Research / Honeywell
  note: ATS 分部（航空航天国防、工业、医疗科技、资本设备）客户
partners:
- company: Broadcom
  ticker: AVGO
  area: 交换平台联合开发
  note: 深度合作；博通高管称随 102.4T 交换时代到来合作「比以往更重要」
- company: AMD
  ticker: AMD
  area: 机架级 AI 平台（Helios）
  note: 机架级交换机 2026 年送样、2027 年量产，配套 MI450/MI455X GPU 与 Pensando Vulcano 800G NIC
- company: OpenAI
  area: 定制整机架（design-led）
  note: 管理层称 2027 年为数十亿美元级机会
- company: 生态标准组织
  area: SONiC / OCP / UEC / OCP ESUN / UALink-over-Ethernet
  note: 开放网络与开放计算标准
competitors:
- company: NVIDIA
  ticker: NVDA
  area: AI 后端以太网交换机
  note: 最直接对手（Spectrum-X、ConnectX-9 superNIC）；但也是生态驱动者——NVIDIA 推动带宽升级反而提升对 Celestica 高速交换机的需求。注意：NVIDIA 机架集成伙伴是富士康与广达，Celestica 不在其中
- company: Accton / Edgecore（智邦）
  ticker: 2345.TW
  area: 白盒交换机
  note: 白盒交换机双寡头——Accton 与 Celestica 合计约占 90%；主要服务 Google、Meta
- company: Arista Networks
  ticker: ANET
  area: 数据中心交换机（品牌）
  note: Dell'Oro 口径位居第三；若计入递延 AI 收入则与 Celestica/NVIDIA 非常接近
- company: Cisco
  ticker: CSCO
  area: 数据中心交换机（品牌）
  note: 份额增幅最大，Dell'Oro 口径列第四
- company: 广达电脑 (Quanta / QCT)
  ticker: 2382.TW
  area: 白盒交换机、AI 机架
  note: 为 AWS、Azure、Oracle、Meta 定制 ToR/spine 交换机与 OCP 设备；亦为 NVIDIA 机架集成方
- company: 纬颖 (Wiwynn)
  ticker: 6669.TW
  area: OCP 交换机与机架
  note: 服务 Microsoft、Meta
- company: 鸿海精密 (Foxconn)
  ticker: 2317.TW
  area: 大规模制造、AI 机架
  note: 服务 AWS、Google；NVIDIA 机架集成方
core_business:
- 数据中心以太网交换机 ODM（400G/800G/1.6T；HPS 业务单元 2025 年营收 $50 亿、+81%，占公司总营收约 41%；2026 Q2 约 $19 亿、+58%）
- AI/ML 计算平台（AI 服务器、存储、机架级集成；含 OpenAI 定制机架与 AMD Helios 平台）
- 企业服务器与存储（2026 Q2 同比 +167%，AI/ML 计算与存储驱动）
- ATS 先进技术解决方案（航空航天国防、工业、医疗科技、资本设备；2025 年 $32 亿、约 +1%）
- EMS 全流程服务（硬件设计开发、NPI/工程、供应链管理与物流、电子制造与组装、精密加工、系统集成与测试、ITAM/ITAD）
revenue_model: B2B 项目制代工（EMS/ODM），无自有品牌产品。ODM 业务（HPS）为设计主导（design-led manufacturing），含设计服务、IP 与软件授权、供应链管理；大客户长约/项目定价，收入随客户资本开支波动。盈利结构显著优于纯 EMS：经调整毛利率 11.5%（2026 Q2，−20bp，CCS 组合变化所致）、经调整经营利润率 8.2%（2026 Q2，历史新高，+80bp）、经调整 ROIC 约 55%。客户集中度为其首要结构性风险：2026 Q2 Top 10 客户占营收 83%（FY2024 73% → 2025Q1 78% → 2026Q2 83%），已超 EMS 行业惯例上限（单一客户不超 15~20%）。资本开支 2026 年约 $10 亿（2026 Q2 约占营收 5.6%）；自由现金流 2026 Q2 $1.47 亿（H1 合计 $2.85 亿），2026 全年指引 $6.0 亿。
founded: 1994
headquarters: 加拿大安大略省多伦多
employees: 29,591（永久+临时/合同，2025-12-31 年报口径，较 2024 年 26,865 人 +10.15%；⚠️ 分歧：Yahoo Finance 列 23,803、disfold 列 18,643）
latest_revenue: 2026 Q2 $47.0 亿（YoY +62%、QoQ +16%，超指引上沿与共识约 8.1%）；2026 Q3 指引 $52.5~55.5 亿（中值 YoY +69%）
market_cap: 约 $428.5 亿（2026-10-02，股本 1.1498 亿股；股价最近收盘 $383.32，分析师目标均价 $480.87）⚠️ 口径分歧大：$381.8 亿~390.3 亿（2026-08~09）
description: Celestica（NYSE 与 TSX 双重上市，代码 CLS）1994 年自 IBM 分拆成立，1998 年 IPO，总部多伦多，是全球领先的 EMS/ODM 厂商。按 CCS（连接与云解决方案，2026 Q2 占营收 81%）与 ATS（先进技术解决方案，19%）两大分部运营；其中 CCS 内的 HPS（硬件平台解决方案）即其 ODM 业务，2025 年营收 50 亿美元、同比 +81%。核心增长来自为超大规模云厂商设计制造 400G/800G/1.6T 数据中心以太网交换机与 AI/ML 计算平台，交换芯片依赖博通 Tomahawk 系列。据 Dell'Oro，2025 年其与 NVIDIA 合计约占 AI 后端以太网交换机市场 50%，2026 Q1/Q2 单独份额均列第一；客户高度集中，2026 Q2 Top 10 客户占营收 83%。
website: https://www.celestica.com
industries:
- AI算力
---

# Celestica

加拿大 EMS/ODM，1994 年自 IBM 分拆。定位独特：它不在 NVIDIA 的机架集成名单里（那是富士康与广达），却靠**白盒数据中心交换机**在 AI 后端以太网市场拿到份额第一——与 Accton 合计约占白盒交换机 90%。代价是客户集中度极高：2026 Q2 Top 10 客户占营收 83%。

## 财务状况

| 指标 | 2025 全年 | 2026 Q2 | 2026 全年指引 |
|------|:------:|:------:|:------:|
| **营收** | **$123.909 亿**（+28%） | **$47.0 亿**（YoY +62%） | **$205 亿**（约 +65%） |
| **经调整毛利率** | —（2025 Q4 为 11.3%） | **11.5%**（−20bp） | — |
| **GAAP 净利** | 8.325 亿（2024 为 4.280 亿） | 3.688 亿 | — |
| **GAAP 摊薄 EPS** | **$7.16** | $3.17 | — |
| **经调整 EPS** | **$6.05**（+56%） | **$2.54**（+83%） | **$11.30**（约 +87%） |
| **经调整经营利润率** | 7.5% | **8.2%**（历史新高，+80bp） | 8.4% |

- 自由现金流：2026 Q2 $1.47 亿（H1 合计 $2.85 亿）；2026 全年指引 $6.0 亿
- 资本开支：2026 年约 $10 亿（Q2 约占营收 5.6%）
- 经调整 ROIC 约 55%；现金及等价物 $5.36 亿（净债务 $2.04 亿）
- ⚠️ **GAAP EPS 含一次性因素**：2025 年含总收益互换（total return swap）带来的每股 $2.18 正向影响（2024 为 $0.77），对比时需剔除
- 2026 指引多次上调：营收 $170 亿 → $190 亿 → **$205 亿**；经调整 EPS $10.15 → **$11.30**

## 产品线详解

| 业务 | 内容 | 规模 |
|------|------|------|
| **HPS（ODM，CCS 内）** | 400G/800G/1.6T 数据中心以太网交换机 | 2025 年 $50 亿（+81%）；2026 Q2 约 $19 亿（+58%）；占公司营收约 41% |
| **AI/ML 计算平台** | AI 服务器、存储、机架级集成 | 2026 Q2 企业分部同比 **+167%** |
| **企业服务器与存储** | 传统企业级 | — |
| **ATS** | 航空航天国防、工业、医疗科技、资本设备 | 2025 年 $32 亿（约 +1%）；2026 Q2 $8.88 亿（+8%） |

**分部结构（2026 Q2）**：CCS 81% / ATS 19%。⚠️ HPS 不是独立报告分部，而是 CCS 内部的业务单元（公司自述「HPS is characterized as our ODM business」）；2026 年无分部重组。

## 技术路线图

- **交换机产品**：**DS6000 系列 1.6TbE** —— 基于博通 Tomahawk 6（TH6），单机 102.4 Tbps 无阻塞交换容量、64 个 1.6TbE（OSFP224）端口；风冷 3RU 版与混合液冷 2OU 版 DS6001（21 吋 OCP ORv3）；支持 SONiC 开放网络，符合 UEC 与 OCP ESUN 标准
- **速率节点**：800G 为当前出货主力（占 AI 后端以太网交换机出货与营收绝大多数）；1.6T 于 2026 Q3 起在两家超大规模客户量产爬坡，公司共有约 10 个在研 1.6T 项目，2027 年放量
- **新项目**：已中标一个 CPO（共封装光学）以太网交换机项目（1.6T 交换芯片、液冷，2027 年爬坡），以及第三个超大规模客户的 1.6T 项目
- **设计主导项目**：为 OpenAI 定制整机架；为 AMD 做 Helios scale-up 机架级平台（2026 送样、2027 量产）
- **2027 展望**：管理层称营收增速将**进一步加速**，经调整盈利增速快于营收；供应端「已为 2026 与 2027 适当对冲」，但 AI 数据中心基础设施供应链仍存约束

## 融资与现金流

- **自由现金流**：2026 Q2 $1.47 亿；H1 合计 $2.85 亿；2026 全年指引 $6.0 亿（前值 $5.0 亿）
- **资本开支**：2026 年约 $10 亿（未上调）
- **资产负债表**：现金及等价物 $5.36 亿，净债务 $2.04 亿
- **回报率**：经调整 ROIC 约 55%
- **上市**：NYSE: CLS + TSX: CLS 双重主要上市（另法兰克福 FSX: CTW / CTW0）

## 研发投入与专利

⚠️ **本项在本次调研中未获取到可靠数据**：搜索来源未披露 Celestica 的研发费用率、研发投入金额与专利数量（EMS/ODM 模式下研发多以客户项目工程费形式体现）。按 L1「不推测原则」留空，不以推测填空。

## 动态更新记录

- 2026-10-08：新建词条。来源 L0 归档 `input_20261008_142`（`L0-原始资料池/03-新闻/2026-10-08-Celestica-调研.md`，15 组 WebSearch，官方新闻稿 + Dell'Oro + 10-K 片段交叉验证）。
  **调研修正了两处初始假设**：① HPS 不是取代 ATS/CCS 的新分部，而是 CCS 内的 ODM 业务单元；② Dell'Oro 的「约 50%」是 Celestica 与 NVIDIA **合计**份额，而 Celestica **单独份额自 2026 Q1 起已列第一**。
  **已知数据缺口**：① FY2025 全年 GAAP 毛利率具体百分比（仅有 2025 Q4 的 11.8%）；② 客户姓名与营收占比的对应关系（公司只披露百分比）；③ Microsoft 是否为客户（未证实）；④ Jabil / Flex 在 AI 数据中心 ODM 的具体竞争关系（未获证据）。
  **时效提醒**：2026 Q3 财报定于 2026-10-26 盘后发布（10-27 电话会 + Investor and Analyst Day）；若入库时间接近该日期，应届时刷新 `data_freshness_date`。
  **被拦截记录**：官方 IR 新闻稿与 Nasdaq 稿件的 WebFetch 均超时 60000ms，改用 WebSearch 摘要取数。
