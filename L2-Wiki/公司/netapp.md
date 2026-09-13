---
name: NetApp
slug: netapp
country: US
ticker: NTAP
type: company
updated: 2026-09
data_freshness_date: 2026-09-13
segments:
- 企业级存储
one_liner: |
  全球企业级数据管理软件与全闪存存储龙头之一，核心为ONTAP数据管理操作系统及AFF全闪存阵列、AFX分离式平台、StorageGRID对象存储与Keystone订阅服务，通过硬件+支持服务+云服务订阅实现盈利，位于AI算力L3核心产品层——FY2026营收$6,925M(+5%)、Non-GAAP营业利润率30.2%、自由现金流$1,869M(+40%)。
  【2026.9.13更新】FY2026营收$6,925M(+5%)、GAAP净利$1,276M(+8%)、Non-GAAP EPS $8.13(+12%)；FY2027 Q1营收$2,025M(+30%)、非GAAP EPS $2.58(+66%)、AFA收入$1,309M(+47%)；FY2027指引大幅上调至$7,975-8,225M(+17%)。**财年结束于每年4月下旬（FY2026=2025/4/26-2026/4/24），与自然年错位约1个季度。** 但Q1 FY27经营现金流−25%、自由现金流−35%、存货翻倍至$375M，财报后股价一度跌约8%。
chain_layer: L3
chain_role: 龙头
suppliers:
- company: NAND/SSD 原厂
  supplies: 企业级 SSD 与 NAND 颗粒
  note: 10-K 仅称"依赖有限数量供应商，部分为单一来源"，不点名；FRU 料号侧证涉及 Samsung PM1733a、Solidigm DC SN655（置信度低）
- company: HDD 供应商
  supplies: 大容量机械硬盘
  note: 10-K 提及"drives"依赖有限供应商，未点名
- company: AMD
  ticker: AMD
  supplies: AFX DX50 数据计算节点 CPU（Genoa 9554P）
- company: NVIDIA
  ticker: NVDA
  supplies: DX50 数据计算节点内 L4 GPU
- company: Cisco
  ticker: CSCO
  supplies: Nexus 9332D/9364D 交换机（AFX 400G fabric）
  note: 同时是 FlexPod 联合方案伙伴
customers:
- company: Samsung Electronics
  ticker: 005930.KS
  note: EDA 环境 + AI Center of Excellence（Q1 FY27 披露的 AI 大单）
- company: IFX Networks
  note: 拉美 CSP（18国27个数据中心），AFF C-Series + ONTAP Snapshots
- company: Banco Pan
  note: 巴西数字银行，Amazon FSx for NetApp ONTAP，存储成本降51%
- company: Healthix
  note: 美国医疗（1,600万患者），SolidFire 150TB 全闪存
- company: McKesson / Unilever / Honeywell
  ticker: MCK / UL / HON
  note: Cloud Volumes ONTAP
- company: Ameriprise Financial / Commerzbank
  ticker: AMP / CBK.DE
  note: 金融服务
- company: 两家未具名分销商
  revenue_pct: 43
  note: 合计占 FY2026 净营收 43%（渠道集中度，10-K Note 14）
partners:
- company: NVIDIA
  ticker: NVDA
  area: AI 数据平台
  note: DGX SuperPOD 认证、AI Data Platform 参考设计、AIDE 联合工程化、NVIDIA-Certified Storage、STX/Vera Rubin/BlueField-4 路线
- company: Microsoft Azure
  ticker: MSFT
  area: 一方云存储服务
  note: Azure NetApp Files（微软一方托管文件存储服务）
- company: Amazon AWS
  ticker: AMZN
  area: 一方云存储服务
  note: Amazon FSx for NetApp ONTAP（2012 年起合作）
- company: Google Cloud
  ticker: GOOGL
  area: 一方云存储服务
  note: Google Cloud NetApp Volumes；Google Distributed Cloud air-gapped 主权云（4年期企业协议）
- company: Cisco
  ticker: CSCO
  area: 融合基础设施
  note: FlexPod（25年联合创新）；2026-06 发布 FlexPod AI
- company: Nutanix
  ticker: NTNX
  area: VMware 替代栈
  note: ONTAP over NFS 集成 Nutanix Cloud Platform；与 Cisco 三方栈 GA 2026 Q3
- company: Lenovo
  ticker: 0992.HK
  area: AI 参考架构
  note: AIPod 联名架构，获 NVIDIA-Certified Storage
competitors:
- company: Dell Technologies
  ticker: DELL
  area: 企业存储
  note: IDC 外部 ESS 全球第一（31.2%，Q1 2026），超后四名之和；PowerStore Gen3 + ObjectScale
- company: Pure Storage（Everpure）
  ticker: P
  area: 全闪存
  note: IDC 外部 ESS 第三（8.9%，+37.9%）；Gartner MQ 2026 双轴最高；2026 年更名 Everpure、代码改 P
- company: HPE
  ticker: HPE
  area: 企业存储
  note: IDC 外部 ESS 第五（5.4%）；Alletra Storage MP / B10000
- company: 华为
  area: 企业存储
  note: IDC 外部 ESS 第四（6.7%）；北美以外 OceanStor
- company: IBM
  ticker: IBM
  area: 企业存储
  note: Gartner MQ Leader；唯一提供对标 DFM 的自研闪存模块
- company: VAST Data
  area: AI 存储
  note: DASE 架构；估值约$9.1B
- company: WEKA
  area: AI/HPC 存储
  note: WEKApod（56RU 1.1EB、10.2TB/s/机架）；KV-cache 卸载
- company: DDN
  area: HPC/AI 存储
  note: AI400X3；宣称 GPU 利用率99%
core_business:
- ONTAP 数据管理操作系统（全产品线软件底座，授权分层 ONTAP Base/One/One for SAN）
- AFF 全闪存阵列（A-Series 高性能 / C-Series QLC 容量型，FY2026 AFA 收入 $4,178M，+11%）
- AFX 分离式全闪存平台（2025-10 发布，性能与容量独立扩展，线性至 128 节点/EB 级）
- ASA 纯块 SAN 存储 + FAS 混合闪存 + E/EF-Series
- StorageGRID S3 兼容对象存储（Forrester Wave 对象存储 2026 Q2 Leader）
- 公有云一方服务（Azure NetApp Files / Amazon FSx for NetApp ONTAP / Google Cloud NetApp Volumes）
- Keystone 存储即服务 STaaS（FY2026 收入 +65%）
revenue_model: 以「硬件 + 支持服务 + 云服务」三线收入为主。FY2026 营收 $6,925M（**+5%**），其中产品 46.1%、支持服务 38.1%（毛利率约93%）、专业服务 5.9%、Public Cloud 9.9%——**服务类合计 53.9%**，是毛利率（GAAP 70.7%）与现金流（FCF $1,869M，+40%）的稳定来源。**Non-GAAP 营业利润率 30.2%**（+190bps）。FY2027 指引营收 $7,975–8,225M（**+17%**），并承诺返还**最高 100% 自由现金流**。
founded: 1992
headquarters: 美国加州圣何塞
employees: ~11,700（截至2026-04-24；其中销售与市场约5,000人）
latest_revenue: FY2026 $6,925M（+5%，截至2026-04-24）；FY2027 Q1 $2,025M（+30%）
market_cap: ~$391.4亿（$39.14B，2026.9.11）
description: NetApp, Inc.（NASDAQ 代码 NTAP）1992年4月成立于美国加州，1995年上市，是全球企业级数据管理与存储厂商。核心资产是 ONTAP 数据管理操作系统——一套 OS 横跨自研硬件（AFF/AFX/ASA/FAS）、公有云托管服务（Azure NetApp Files、Amazon FSx for NetApp ONTAP、Google Cloud NetApp Volumes，均为超大规模云的一方服务）与订阅制交付（Keystone）。FY2026（截至2026-04-24）营收 $6,925M（+5%）、GAAP 净利 $1,276M（+8%）、自由现金流 $1,869M（+40%）；全闪存阵列收入 $4,178M（+11%）。AI 战略以「Intelligent Data Infrastructure」为定位，与 NVIDIA 联合工程化 AIDE（AI Data Engine）与 AFX 平台，Q1 FY2027 AI/数据湖现代化订单约350笔。⚠️ 财年结束于每年4月下旬，与自然年错位约1个季度。
website: https://www.netapp.com
industries:
- AI算力
---

# NetApp

企业存储里"软件锁定最深"的一家——ONTAP 是唯一同时横跨自研硬件与三大公有云一方服务的数据管理 OS。但 Q1 FY2027 的 +30% 营收增长里含额外一周（约 $65M）与需求前置，同期经营现金流 −25%、自由现金流 −35%、存货翻倍，增长质量需要打问号。

> ⚠️ **财年口径**：NetApp 财年**不按自然年**，**FY 结束于每年 4 月下旬**。**FY2026 = 2025-04-26 ~ 2026-04-24**；**FY2027 Q1 = 2026-05-01 ~ 2026-07-31**（2026-09-02 公布）。FY2026 约等于自然年 2025 年中至 2026 年中，**滞后自然年约 1 个季度**——跨公司横向比较时务必换算。

## 财务状况

财年结束于每年 4 月下旬。FY2026 营收温和增长但利润率与现金流显著改善；FY2027 Q1 营收加速但现金流恶化。

### FY2026 全年（截至 2026-04-24）

| 指标 | 值 | 同比 |
|------|-----|------|
| 营收 | **$6,925M** | **+5%**（不变汇率+4%） |
| Billings（订单额） | $7,206M | +6% |
| GAAP 毛利率 | **70.7%** | FY25 70.2% |
| Non-GAAP 毛利率 | 71.3% | FY25 71.1% |
| GAAP 营业利润率 | **24.2%** | FY25 20.3% |
| **Non-GAAP 营业利润率** | **30.2%** | FY25 28.3% |
| GAAP 净利润 | **$1,276M** | **+8%** |
| Non-GAAP 净利润 | $1,635M | +8% |
| GAAP EPS | **$6.35** | +12% |
| Non-GAAP EPS | **$8.13** | +12% |
| **经营现金流** | **$2,067M** | **+37%** |
| **自由现金流** | **$1,869M** | **+40%** |
| 递延收入 | $4,845M | FY25 $4,536M |
| 股东总回报 | **$1.36B**（回购 $950M + 分红 $413M） | — |

### FY2027 Q1（截至 2026-07-31，2026-09-02 公布）

| 指标 | 值 | 同比 |
|------|-----|------|
| 营收 | **$2,025M** | **+30%**（剔除额外一周 +26%） |
| GAAP 净利润 | **$375M** | **+61%** |
| Non-GAAP 净利润 | $515M | +64% |
| GAAP EPS | $1.88 | +63% |
| **Non-GAAP EPS** | **$2.58** | **+66%** |
| GAAP / Non-GAAP 毛利率 | 70.1% / 70.6% | — |
| GAAP / Non-GAAP 营业利润率 | 23.9% / **31.9%** | — |
| Billings | $2,057M | +36% |
| **经营现金流** | **$503M** | **−25%** |
| **自由现金流** | **$401M** | **−35%**（FCF率19.8%） |
| **全闪存阵列(AFA)收入** | **$1,309M** | **+47%** |
| Hybrid Cloud 分部 | $1,819M | +30% |
| Public Cloud 分部 | $206M | +28%（毛利率86.4%） |

> ⚠️ **Q1 FY27 增长含三项"水分"**：① 该季**多出 1 周**（贡献约 $65M，剔除后 +26%）；② 管理层承认部分大客户**需求前置（pulled-forward）**；③ 指引隐含下半年增速放缓。

### AFA（全闪存阵列）年化运行率序列

| 季度 | AFA 收入 | 官方年化运行率 |
|------|---------|---------------|
| Q1 FY26 | $893M（+6%） | $3.6B |
| Q2 FY26 | $1.0B（+9%） | $4.1B |
| Q3 FY26 | $1.0B（+11%） | $4.2B |
| Q4 FY26 | $1.2B（+18%） | 未披露 |
| **FY2026 全年** | **$4,178M** | —（FY25 $3,763M，**+11%**） |
| Q1 FY27 | **$1,309M（+47%）** | 未披露（×4 约 $5.24B，为推算值） |

### 收入结构（FY2026）

| 科目 | 收入 | 占比 | 备注 |
|------|------|------|------|
| Product（硬件+软件捆绑） | $3,194M | **46.1%** | 软件不单独披露 |
| Support（支持服务） | $2,636M | **38.1%** | 毛利率约 **93%** |
| Professional & Other | $407M | 5.9% | — |
| Public Cloud | $688M | 9.9% | 毛利率 86.4%（Q1 FY27） |
| **服务类合计** | **$3,731M** | **53.9%** | 利润与现金流基本盘 |

分部：Hybrid Cloud $6,237M（90.1%，+6%）/ Public Cloud $688M（9.9%，+3%）。**AFA 占 Hybrid Cloud 比重 67%**（FY25 64%）。

### FY2027 指引（大幅上调）

| 指标 | 新指引 | 原指引 |
|------|--------|--------|
| FY2027 营收 | **$7,975M–$8,225M（+17%）** | $6,772M–$6,922M 区间量级 |
| FY2027 Non-GAAP EPS | **$9.73–$10.03** | — |
| FY2027 Non-GAAP 营业利润率 | 30.3%–31.3% | — |
| FY2027 Non-GAAP 毛利率 | 68.1%–69.1% | — |
| Q2 FY2027 营收 | $2,025M–$2,175M | — |
| 资本回报 | 拟返还**最高 100% FCF** | — |

### 资产负债与现金流（Q1 FY2027）

| 指标 | 值 |
|------|-----|
| 现金 + 短期投资 | $3,576M |
| 有息负债 | 约 $2,488M（短期$550M + 长期$1,938M） |
| **净现金** | **$1.09B** |
| 递延收入 | $4,846M |
| **存货** | **$375M**（FY26 末 $198M，**翻倍**，为需求提前备货） |
| 采购承诺 | $1.4B（其中 $1.1B 于 FY2027 到期） |

### 市占率（口径差异须注意）

| 口径 | 数据 | 期间 |
|------|------|------|
| **IDC 外部企业存储（external ESS）** | **NetApp #2，9.9%（+9.6% YoY）**；Dell #1 31.2%（+40.8%）、Everpure 8.9%、华为 6.7%、HPE 5.4% | **IDC Q1 2026** |
| IDC 全闪存全球第一 | NetApp 取得全闪存 #1（**仅 2025 自然年 Q1 一次声明，2026 年未复述**） | 2025 Q1 |
| Gartner MQ 企业存储平台 | Leader（执行力轴相对下滑，落后华为/HPE） | 2026 |
| Forrester Wave 对象存储 | Leader | 2026 Q2 |

> ⚠️ **"全闪存龙头"定位需谨慎引用**：可验证的仅是 **2025 自然年 Q1 的 IDC 全闪存第一**；在 **IDC Q1 2026 全球外部 ESS 总口径下 NetApp 是 #2（9.9%）**，落后 Dell（31.2%），且 Dell 增速（+40.8%）远快于 NetApp（+9.6%）。两口径不同（全闪存 vs 全部外部 ESS）。

### 市场数据（2026-09-11）

| 指标 | 值 |
|------|-----|
| 股价 | **$199.28**（单日 +8.54%） |
| **市值** | **$39.14B** |
| **PE (TTM)** | **28.12** |
| Forward PE | 20.08 |
| 股息 / 股息率 | $2.08 年化（季度$0.52）/ 1.04%–1.14% |
| 52 周区间 | $93.69 – $209.06 |
| TTM 营收 / 净利 | $7.39B（+12.2%）/ $1.42B（+21.1%） |

> Q1 FY27 财报（9/2）后股价**一度跌约 8%**（现金流下滑+需求前置），9/11 单日 +8.54%。市值在不同日期为 $35.5B–$39.1B，**引用务必带日期**。

## 产品线详解

### ONTAP（核心护城河）
统一数据管理操作系统，NetApp 全部产品线的软件底座。授权分层：ONTAP Base / ONTAP One / ONTAP One for SAN。**迁移成本极高的软件锁定**是核心壁垒——Nutanix、Cisco 等第三方主动集成 ONTAP，反向验证其生态位。

### AFF 全闪存阵列（AFA，FY2026 $4,178M）
- **AFF A-Series**：高性能/关键业务混合负载（旗舰 AFF A90），**已通过 NVIDIA DGX SuperPOD 认证**
- **AFF C-Series**：QLC SSD 容量型，低成本/TB（50TB+），可替代大容量 SAS 盘
- **ASA（All SAN Array）**：纯块 SAN 存储，A-Series 与 C-Series 两档，成本低于同档 AFF

### AFX（2025-10 发布，最新平台）
**分离式（disaggregated）全闪存平台**，ONTAP 的新"人格"，**专为 AI 设计**：性能与容量独立扩展、400G 以太网 fabric、**线性扩展至 128 节点 / EB 级容量**；协议支持 NFS/SMB/S3（**不支持块**）。AFX 1K 控制器 2RU/11 个 PCIe Gen5 槽，NX224 NVMe 扩展柜，DX50 数据计算节点（AMD Genoa 9554P + NVIDIA L4 GPU）。

### 其他产品线
- **FAS** 混合闪存（HDD+SSD）阵列；**E/EF-Series** 吞吐优化型 SAN
- **StorageGRID** S3 兼容对象存储（Forrester Wave 对象存储 2026 Q2 Leader）
- **Cloud Volumes ONTAP** 公有云自管统一存储
- **三大云一方服务**：Azure NetApp Files（微软）、Amazon FSx for NetApp ONTAP、Google Cloud NetApp Volumes
- **Keystone**：存储即服务（STaaS），本地+云统一交付块/文件/对象，可与 AFX/AIDE 打包
- **AIPod**：与 Lenovo 联名 AI 参考架构，获 NVIDIA-Certified Storage

### 订阅业务经济性
**Keystone 收入 FY2026 同比 +65%**（公司未给绝对金额，CFO 明言"占业务比重仍小"）；未开票 RPO FY2026 $807M。**服务类收入占比 53.9%** 是毛利率与现金流稳定性的来源。

## 技术路线图

| 方向 | 内容 | 状态 |
|------|------|------|
| **全闪存** | AFF A/C-Series + ASA + **AFX 分离式架构**（性能/容量解耦，128 节点、EB 级） | AFX 已 GA |
| **AI 数据管理（AIDE）** | AI Data Engine：原地语义增强（不迁移数据）、全局元数据目录、语义搜索/向量化/RAG端点/guardrails | 2026 年初夏 GA；路线图为**嵌入全部 ONTAP 平台**并整合对象存储 |
| **存储邻近计算** | 收购 **DataPelago**，在存储侧做 AI 分析与推理加速 | Q1 FY27 完成交割 |
| **云集成** | ONTAP 作为跨本地/公有云/主权云的**一致数据平面**；Azure Object REST API、Global Namespace with FlexCache、Google Cloud 块存储 + Gemini Enterprise | 陆续发布 |
| **主权云/气隙** | Google Distributed Cloud air-gapped（政府/国防，零信任+数据主权） | 4 年期企业协议 |
| **VMware 替代栈** | 与 Cisco + Nutanix 三方栈（NetApp 存储 + Cisco 计算 + Nutanix 虚拟化） | GA 2026 Q3 |
| **KV-cache / DPU** | 支持 **NVIDIA STX**（Vera Rubin + BlueField-4）与专用 KV-cache 内存层 | 未来路线 |
| **安全** | Ransomware Resilience（AI 驱动入侵检测 + 隔离恢复）、SnapLock | 已发布 |
| **CXL** | **未查到**任何公开 CXL 路线图 | — |

**AI 订单动能（可量化）**：Q2 FY2026 约 200 笔 AI/数据湖现代化订单 → **Q1 FY2027 约 350 笔**，且单笔规模上升（从 PoC 转向生产）。灯塔客户含 Samsung Electronics（EDA + AI Center of Excellence）。

### 并购
| 标的 | 时间 | 内容 |
|------|------|------|
| **DataPelago** | Q1 FY2027 | AI 数据基础设施，存储邻近的 AI 分析与推理加速 |
| **JetStream Software** | Q2 FY2027 初 | VMware 灾备/云迁移 |
| Spot（已剥离） | FY2025-26 | 云成本优化业务剥离 → 影响 Public Cloud 可比增速 |

## 融资与现金流

### 现金流与资本回报
| 指标 | FY2026 | Q1 FY2027 |
|------|--------|-----------|
| 经营现金流 | **$2,067M（+37%）** | $503M（**−25%**） |
| 资本开支 | 约 $198M（倒算） | $102M |
| **自由现金流** | **$1,869M（+40%）** | $401M（**−35%**） |
| 回购 | $950M / 900万股 / 均价$105.89 | $200M |
| 分红 | $413M（$2.08/股） | $102M |
| **股东总回报** | **$1.36B** | $302M |

- **新回购授权**：2026-05-21 董事会批准**新增 $1.0B**，无到期日
- **季度股息 $0.52/股，多年未变**（2024–2026 均为此数），**未查到加息**
- **FY2027 承诺**：拟返还**最高 100% 自由现金流**，股本数同比降低个位数百分比

### 资产负债表
- 现金+短期投资 $3,576M；有息负债约 $2,488M；**净现金 $1.09B**
- 股东权益仅 $1,495M（大额回购导致权益基数低）
- **存货从 $198M 翻倍至 $375M**——为需求提前备货，是 FCF 转负的直接原因
- 采购承诺 $1.4B（其中 $1.1B 于 FY2027 到期）

### 现金流恶化的原因与风险
Q1 FY27 经营现金流 −25%、自由现金流 −35%，主因：**战略备货（存货翻倍）+ 需求前置 + 重组费用 $56M（去年同期仅 $2M）**。公司指引 FY2027 FCF $600M–800M 区间（口径与"最高 100% FCF 返还"需区分）。

## 研发投入与专利

| 指标 | FY2024 | FY2025 | FY2026 |
|------|--------|--------|--------|
| R&D（GAAP） | $1,029M | $1,012M | **$991M** |
| R&D（Non-GAAP） | — | — | $877M |
| R&D 占营收比 | — | — | **14.3%** |
| 占总员工比（研发人员） | — | — | 未单独披露 |

> ⚠️ **R&D 连续两年下滑**（−2.1% YoY），公司解释为"薪酬成本下降 + 工程项目支出减少"。这与"AIDE 嵌入全部 ONTAP、AFX 全面铺开"的投入需求存在张力。

### 专利（多来源冲突）
| 来源 | 数字 | 口径 |
|------|------|------|
| GreyB Insights | **4,694 项全球专利，3,412 项已授权**，>67% 有效 | 全球 |
| PlainPatent | **1,774 项美国授权专利（2015–2025）**，近五年申请速度 **−13%** | 仅美国 |
| Dealroom | 1,872 个有效专利族，估值 $446M | 专利族 |
| NetApp 10-K | **不披露专利数量** | — |

### 核心技术壁垒
1. **ONTAP 的软件锁定**——一套 OS 横跨自研硬件、三大公有云一方服务、订阅制交付，迁移成本极高
2. **元数据引擎（AIDE）**——原地语义增强不迁移数据，避免成本与安全风险，是 RAG/agentic AI 的差异化点
3. **NVIDIA 深度认证链条**——DGX SuperPOD / NVIDIA-Certified Storage / AI Data Platform 参考设计 / STX 早期席位
4. **服务收入基本盘**——支持服务毛利率约 93%、占比 38.1%，提供穿越周期的利润稳定性

### 主要风险
1. **现金流恶化**——Q1 FY27 FCF −35%、存货翻倍、重组费用 $56M；若 Q2-Q3 未如指引恢复，FY2027"100% FCF 返还"承诺难以兑现
2. **客户/渠道集中度**——两家分销商合计占 FY2026 净营收 **43%**
3. **增长含前置需求**——Q1 FY27 +30% 中额外一周贡献 $65M，管理层承认部分客户加速采购，隐含 H2 放缓
4. **"全闪存龙头"定位与 IDC 口径不符**——外部 ESS 口径下为 #2，落后 Dell 且增速差距大
5. **R&D 连续两年下滑 + 专利申请速度 −13%**——与 AI 领先叙事存在张力
6. **NAND/内存成本压力**——10-K 承认 FY2026 下半年起内存与元件成本上升损害毛利率
7. **新战场落后**——Futuriom 2026 认为 DDN/VAST/WEKA 领跑 HPC→AI 数据平台转型，Dell/NetApp/IBM 属"加速追赶"；KV-cache 卸载与 MCP server 支持是下一竞争焦点

## 动态更新记录

### 2026-09-13（新建词条 + FY2026 年报 & FY2027 Q1）
> 来源: 新建（原为赛道页提及但无公司页）
> L0归档: `L0-原始资料池/03-新闻/2026-09-13-NetApp-调研.md` (input_20260913_103)
> 置信度: 高（官方 IR 新闻稿 + SEC 10-K 一手来源）

- **词条新建**：补齐 24 个 YAML 字段 + 6 个 Body 段
- **latest_revenue**：FY2026 $6,925M（+5%）；FY2027 Q1 $2,025M（+30%）
- **market_cap**：~$391.4亿（$39.14B，2026.9.11）
- **suppliers/customers/partners/competitors**：分别填充 5/7/7/8 条
- **新增关键信息**：FY2026 FCF $1,869M(+40%)、AFA 全年 $4,178M(+11%)、Q1 FY27 AFA $1,309M(+47%)、AI 订单 200→350 笔、Keystone 收入 +65%、FY2027 指引上调至 $8.10B 中值(+17%)并承诺返还最高 100% FCF
- **财年口径标注**：全文逐项标注 FY 口径；FY2026 = 2025-04-26~2026-04-24，**与自然年错位约 1 个季度**
- **⚠️ 定位校正**：赛道页「企业级存储」将 NetApp 列为**全闪存龙头**。IDC Q1 2026 全球**外部 ESS** 口径下 NetApp 为 **#2（9.9%）**，落后 Dell（31.2%）且增速（+9.6%）远低于 Dell（+40.8%）；"全闪存第一"仅有 2025 自然年 Q1 一次官方声明。**建议赛道页补充口径说明**
- **风险标注**：Q1 FY27 经营现金流 −25%、FCF −35%、存货翻倍至 $375M、两家分销商占净营收 43%、R&D 连续两年下滑
- **赛道页建议同步**：`L2-Wiki/赛道/AI算力/enterprise-storage.md` 的 sources 仍为 IDC Q3 2025（NetApp 9.4%）；已更新为 IDC Q1 2026（NetApp 9.9% #2 / Dell 31.2% / Everpure 8.9% / 华为 6.7% / HPE 5.4%）
