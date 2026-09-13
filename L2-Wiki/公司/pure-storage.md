---
name: Pure Storage (Everpure)
slug: pure-storage
country: US
ticker: P
type: company
updated: 2026-09
data_freshness_date: 2026-09-13
segments:
- 企业级存储
one_liner: |
  全球全闪存阵列挑战者与自研闪存模块的唯一规模化厂商，核心为FlashArray/FlashBlade全闪存平台与Evergreen订阅制存储服务，通过阵列销售+订阅服务（占营收42%）实现盈利，位于AI算力L3核心产品层——FY2027 Q2营收$1,185.9M(+38%)、订阅ARR $2.1B，连续8个季度加速。
  【2026.9.13更新】FY2027 Q2营收$1.1859B(+38%)、Non-GAAP EPS $0.70(+63%)、订阅ARR $2.1B(+20%)、Non-GAAP营业利润率19.4%；FY2027指引上调至$5.03-5.07B(+37-38%)。**公司已于2026-02-23更名Everpure, Inc.，2026-04-17起NYSE代码由PSTG变更为「P」，官网迁移至everpuredata.com**（赛道页 ticker 仍为 PSTG，需同步）。Q2经营现金流−$136M、自由现金流−$238M（战略囤积NAND），是财报后股价跌约9%的主因。
chain_layer: L3
chain_role: 直接相关
suppliers:
- company: Micron（美光）
  ticker: MU
  supplies: QLC NAND（G9）
  note: 已合作7代NAND，G9 QLC将用于未来DirectFlash Module
- company: Kioxia
  ticker: 285A.T
  supplies: QLC NAND（BiCS FLASH 第8代 2Tb，电荷陷阱CT结构）
  note: 2024-12 成为 DFM 用 QLC 伙伴
- company: SK Hynix
  ticker: 000660.KS
  supplies: QLC NAND
  note: 官方博客列为 DFM 的 QLC 伙伴之一
- company: 自研（垂直整合）
  supplies: DirectFlash Module（DFM）与控制器系统
  note: 公司自行设计并制造 DFM，容量效率宣称达通用 SSD 阵列约2.5倍
customers:
- company: Meta
  ticker: META
  note: 第一家超大规模客户，2024年底签约，DFM 供应
- company: 第二家 Top-5 超大规模客户（未具名）
  note: 2026-08-10 宣布 design win + 供货协议，承诺延续至2028自然年、涉及数十EB；FY27贡献极小、FY28起显著放量
- company: CoreWeave
  note: AI 云，FlashBlade//S 的 AI 负载案例
- company: 大型企业客户
  note: Q2 FY27 >$5M 交易 +59%、>$20M 交易 +385% YoY
partners:
- company: NVIDIA
  ticker: NVDA
  area: AI Factory / 参考架构
  note: FlashBlade//EXA 对齐 NVIDIA AI Factory 与 STX 参考架构（Vera Rubin + BlueField DPU）；DGX GB300/GB200/B300 SuperPOD、AIRI、NCP 认证
- company: Cisco
  ticker: CSCO
  area: 融合基础设施
  note: FlashStack（2014-12 联合发布，2021-07 推出 as-a-Service）；80+ Cisco Validated Designs
- company: Microsoft
  ticker: MSFT
  area: 主权云存储
  note: FlashArray with Azure Local；Everpure Cloud Azure Native（Azure VM + Azure VMware Solution）
- company: Amazon AWS
  ticker: AMZN
  area: 云数据服务
  note: Everpure Cloud 首发平台
- company: VMware（Broadcom）
  ticker: AVGO
  area: 虚拟化
  note: 十余年 Technology Alliance Partner；支持 VMware Cloud Foundation，可作 vSAN 替代
- company: Supermicro
  ticker: SMCI
  area: AI 数据管道
  note: 联合设计 Everpure Data Stream
- company: Databricks
  area: 数据湖
  note: OpenSharing Connector（直查 Iceberg/Delta 表）
competitors:
- company: Dell Technologies
  ticker: DELL
  area: 企业存储
  note: IDC 外部存储份额31.2%第一，超其余四家合计；PowerStore 定价介于 Pure 与 NetApp 之间
- company: NetApp
  ticker: NTAP
  area: 全闪存
  note: Gartner MQ Leader 但相对下滑；云原生整合强
- company: HPE
  ticker: HPE
  area: 企业存储
  note: Gartner MQ Leader，愿景完整度第2；定价比 Pure/Dell 高10-15%
- company: 华为
  area: 企业存储
  note: Gartner MQ 执行力第2；IDC 前五
- company: IBM
  ticker: IBM
  area: 企业存储
  note: 唯一提供对标 DFM 的自研模块（Flash Core Module 第5代）
- company: VAST Data
  area: AI 存储
  note: 未进入2026 Gartner MQ；靠单位TB经济性竞争，缺支持生态与多站点授权灵活性
- company: WEKA
  area: AI/HPC 存储
  note: 未进入2026 MQ；WEKApod 入选 NVIDIA DGX BasePOD/SuperPOD 生态
- company: DDN
  area: AI/HPC 存储
  note: 2026 年被 Gartner MQ 剔除；AI400X3 仍是重要玩家
core_business:
- FlashArray 家族（//X 高性能、//C QLC 容量型、//E、//XL、//ST R5，块与统一文件）
- FlashBlade 家族（//S 面向AI/分析、//E 容量优化、//EXA AI最强平台，单命名空间>10TB/s）
- Evergreen 订阅体系（//One STaaS、//Flex、//Forever，TCV 年化超$1B）
- DirectFlash Module（DFM）自研闪存模块（垂直整合，容量效率约通用SSD阵列2.5倍）
- Portworx（Kubernetes 数据管理）+ Pure1（AI 驱动云管理，AI Copilot）
- Everpure Cloud / Data Stream / Data Intelligence（AI 数据平台与编排）
revenue_model: 以「阵列硬件 + 订阅服务」双线收入为主。FY2027 Q2 营收 $1,185.9M（**+38%**），订阅服务收入 $499.1M（**占42%**、+20%）、订阅 ARR **$2.1B**（+20%）。**Non-GAAP 营业利润率 19.4%（+430bp）**，GAAP 营业利润率仅 5.3%——差异来自股权激励。**管理层刻意将产品毛利率运行在 65%–70% 区间下沿以换取份额**（Q2 产品毛利率 66.2%）。hyperscale 业务毛利率 75–85%，是未来结构改善的关键。
founded: 2009
headquarters: 美国加州圣克拉拉
employees: 约6,400（2026；另有5,100-6,000口径）
latest_revenue: FY2027 Q2 $1,185.9M（+38%，截至2026-08-02）；FY2026 全年 $3.66B（+16%）
market_cap: ~$327亿（$32.7B，2026.9.11）
description: Pure Storage（2026年2月更名 Everpure, Inc.，NYSE代码自2026-04-17由 PSTG 变更为「P」）2009年成立于美国加州，2015年10月上市，是全球全闪存阵列的挑战者与领导者之一，2026 Gartner 企业存储平台魔力象限执行力与愿景完整度双轴最高。公司的差异化在于垂直整合——自行设计并制造 DirectFlash Module（DFM）与控制器系统，绕过通用 SSD 的 FTL 层，宣称容量效率达通用 SSD 阵列约2.5倍。产品线含 FlashArray（块/统一文件，//X //C //E //XL）、FlashBlade（scale-out 非结构化，//S //E //EXA）与 Evergreen 订阅体系（//One //Flex //Forever）。FY2026 营收 $3.66B（+16%）、GAAP 净利 $188.2M；FY2027 Q2 营收 $1,185.9M（+38%），连续8个季度加速。⚠️ 官网为 everpuredata.com（原 purestorage.com）。
website: https://www.everpuredata.com
industry: AI算力
---

# Pure Storage (Everpure)

全闪存行业里唯一"自研闪存模块"规模化的挑战者——DFM 垂直整合让它敢把产品毛利率压到 66% 抢份额。但 FY2027 Q2 的 +38% 增长里约三分之一来自 NAND 涨价与客户提前拉货，同期经营现金流 −$136M、自由现金流 −$238M。

> 🔴 **名称与代码已变更（必读）**
> - **2026-02-23 宣布更名 Everpure, Inc.**，2026-03-05 起以 Everpure 名义交易
> - **2026-04-17 起 NYSE 代码由 PSTG 变更为「P」**（CUSIP 不变，股东无需操作）
> - 官网迁移至 **everpuredata.com**（原 purestorage.com 并存）
> - 本词条 `name` 保留 **Pure Storage** 以匹配赛道页引用名（维持图谱边），`ticker` 取现行 **P**
> - ⚠️ 赛道页 `enterprise-storage.md` 的 ticker 仍为 **PSTG**，需同步

> ⚠️ **财年口径**：财年结束于距 1 月 31 日最近的周日，**财年编号 = 结束所在自然年**（比发布时自然年提前一年）。**FY2027 = 2026 自然年 2 月至 2027 年 1 月**；**FY2027 Q2 = 2026-05~07（2026-08-02 结束，2026-08-26 发布）**。截至 2026-09-13 已进入 FY2027 Q3。

## 财务状况

财年结束于 1 月底附近。增长曲线连续 8 个季度加速，但现金流与毛利率承压。

### FY2027 Q2（截至 2026-08-02，最新季）

| 指标 | 值 | 同比 |
|------|-----|------|
| 营收 | **$1,185.9M** | **+38%** |
| 产品收入 | $686.8M | +54% |
| 订阅服务收入 | $499.1M（**占42%**） | +20% |
| **订阅 ARR** | **$2.1B** | **+20%** |
| RPO | $4.1B | +44% |
| GAAP 毛利率 | **68.4%** | 去年 70.2% |
| Non-GAAP 毛利率 | **69.9%** | 去年 72.1% |
| 产品毛利率 / 订阅毛利率 | 66.2% / 74.9% | — |
| GAAP 营业利润 | $63.2M（5.3%） | — |
| **Non-GAAP 营业利润** | **$229.6M（19.4%）** | **+430bp** |
| GAAP 净利 | $74.1M（去年 $47.1M） | — |
| Non-GAAP 净利 | $240.7M | — |
| GAAP EPS | $0.21（去年 $0.14） | — |
| **Non-GAAP EPS** | **$0.70**（去年 $0.43） | **超预期 $0.58~0.59** |
| **经营现金流** | **−$136.3M** | 去年 +$212.2M（**转负**） |
| **自由现金流** | **−$237.6M** | 去年 +$150.1M（**转负**） |
| 现金 + 证券 | $1.0B | −34.45% |
| 非美收入 | $498M（**占42%，历史新高**） | **+75%** |
| 大单动能 | >$5M 交易 **+59%**、>$20M 交易 **+385%** | — |

### FY2026 全年（截至 2026-02-01）

| 指标 | 值 | 同比 |
|------|-----|------|
| 营收 | **$3.66B** | **+16%** |
| Q4 营收 | $1.06~1.1B | +20%（**首个十亿美元季度**） |
| **GAAP 净利** | **$188.181M**（FY25 $106.739M） | — |
| GAAP EPS | $0.55（FY25 $0.31） | — |
| GAAP 营业利润率 | 3.1% | — |
| Non-GAAP 营业利润率 | **17.3%** | — |
| GAAP / Non-GAAP 毛利率 | 70.4% / 72.1% | — |
| **订阅 ARR** | **$1.9B** | +16% |
| RPO | $3.7B | +40% |
| **经营现金流 / 自由现金流** | **$880M / $616M** | — |
| 现金 + 证券 | $1.5B | — |

### 增长轨迹（连续 8 个季度加速）

| 期间 | 营收 | 同比 |
|------|------|------|
| FY2026 全年 | $3.66B | +16% |
| FY2027 Q1（截至 2026-05-03） | $1.053B | +35% |
| **FY2027 Q2（截至 2026-08-02）** | **$1.1859B** | **+38%** |

### FY2027 指引（2026-08-26 大幅上调）

| 项目 | 新指引 | 旧指引 |
|------|--------|--------|
| **FY27 全年营收** | **$5.03B–5.07B（+37%~38%）** | $4.41B–4.51B（+20%~23%） |
| **FY27 Non-GAAP 营业利润** | **$940M–960M（+48%~51%）** | $820M–860M |
| Q3 FY27 营收 | $1.325B–1.335B | — |
| FY27 自由现金流 | $600M–800M | — |

> 全年指引**一次性从 $4.4B 量级上调至 $5.0B 量级**，是本季最强烈的信号。

### 市占率（IDC Q1 2026）

| 厂商 | 外部企业存储份额 | 同比 |
|------|-----------------|------|
| Dell | **31.2%**（超其余四家合计） | +40.8% |
| NetApp | 9.9% | +9.6% |
| **Everpure（Pure）** | **8.9%** | **+37.9%（前五中增速最快）** |
| 华为 | 6.7% | — |
| HPE | 5.4% | — |

> 市场背景：IDC Q1 2026 外部 OEM 企业存储市场 $9.2B（+22.7%）；**AFA 首次突破 50% 占比**（$4.9B，+32.7%）；高端段（>$250K 系统）+60.7% 至 $2.4B。
> ⚠️ 赛道页现用 IDC Q3 2025 口径为 Pure 6.8%/+15.5%，**已被 Q1 2026 的 8.9%/+37.9% 取代**。

### 市场数据（2026-09-11）

| 指标 | 值 |
|------|-----|
| 股价 | **$98.18** |
| **市值** | **$32.7B**（区间 $32.34B–$33.62B，各源日期不同） |
| **PE (TTM)** | **约133–139** |
| PE (Forward) | 约32–41 |
| **PS (TTM)** | **约7.5–7.9** |
| PS (Forward) | 5.82 |
| EV/EBITDA | 83.14 |
| 52周区间 | $56.78 – $119.10 |
| TTM 营收 / 净利 | $4.26B / $253M |

> Q2 FY27 财报（8/26）后股价一度跌约 9%（现金流双转负）。**估值已 price in 极高增长预期**——TTM PE ~135x 而 Forward PE ~32x。

## 产品线详解

### FlashArray 家族（块存储/结构化数据）
| 产品 | 定位 |
|------|------|
| **FlashArray//X** | 关键业务高性能：更高 IOPS、超一致低延迟、更小机架占地 |
| **FlashArray//C** | 经济型企业全闪存，基于 **QLC**，最高 16.3PB 容量，99.9999% 可用性，含防勒索特性 |
| **FlashArray//E** | 容量优化型（Everpure//E 家族），主打全闪存低成本替代 HDD |
| **FlashArray//XL** | 家族顶配；//XL 190 with Turbo 支持第二控制器参与读操作，面向 Oracle/数据库等延迟敏感负载 |
| **FlashArray//ST R5** | 超低延迟一致性（OLTP、内存数据库、实时负载），随 Purity//FA 6.10.5 加入 |

### FlashBlade 家族（scale-out 非结构化）
| 产品 | 定位 |
|------|------|
| **FlashBlade//S** | 面向 AI / 分析的快速文件与对象存储 |
| **FlashBlade//E** | 容量优化的统一文件+对象平台 |
| **FlashBlade//EXA** | **AI 最强存储平台**：单命名空间 **>10 TB/s**，MLPerf/SPECstorage/IO500 多项第一，性能达最近竞品 2 倍；元数据/数据节点解耦架构；已验证 **192 节点无性能衰减**；创 SPECstorage AI_Image 记录（6,300 并发 AI 工作负载） |

### Evergreen 订阅体系（转型核心）
- **Evergreen//One**：SLA 保障的存储即服务（STaaS）；2026 新增 **//One for AI**（面向 GPU 密集负载，按容量计价），已扩展支持 FlashBlade//EXA；新增 **Overdrive** 应对性能尖峰。**TCV 年化运行率超 $1B**；Q2 STaaS TCV 同比 **+121% 至 $277M**；合同期通常 3–4 年
- **Evergreen//Flex**：车队级灵活模式；**Evergreen//Forever**：控制器/组件永久升级计划
- **Pure1**：AI 驱动云管理平台，**Pure1 AI Copilot** 正演进为主动运维者
- **Everpure Fusion**：SaaS 管控平面；**Portworx**：Kubernetes 数据管理
- **Everpure Cloud**：虚拟块存储阵列（Azure Native 支持 Azure VM / Azure VMware Solution）；**Data Stream** 为 AI 数据管道编排层

> **订阅经济性**：订阅服务收入占营收 42%、订阅 ARR $2.1B（+20%）。管理层测算：**剔除 Evergreen//One 加速带来的收入递延影响，底层增速显著高于 40% YoY**。

### 商业模式的关键取舍
**管理层刻意将产品毛利率运行在 65%–70% 区间下沿以换取市场份额**（1H FY27 为 66.2%），同时靠订阅服务（74.9% 毛利率）与 hyperscale 业务（75–85%）改善长期结构。

## 技术路线图

| 方向 | 内容 | 状态 |
|------|------|------|
| **DirectFlash Module（DFM）** | 自研闪存模块，直接对接 NAND 芯片，与 Purity 软件深度协同；管理粒度在**系统级而非盘级**；同时支持 TLC 与 QLC | 量产中 |
| **DFM 密度路线** | **75TB → 150TB（2025）→ 300TB（2026 计划）→ 目标 5x 密度优势**（对比最大 HDD 约 32TB） | 推进中 |
| **HDD 替代时间表** | 借 Micron 232 层 QLC，**2028 年前完成数据中心 HDD 全替代**（高管 Bill Cerreta 口径） | 目标 2028 |
| **全 QLC 路线** | FlashArray//C 与 //E、FlashBlade//E 均基于 QLC，主打低成本容量层 | 量产中 |
| **AI 存储** | FlashBlade//EXA + Data Stream + Data Intelligence + **Data Primacy 架构** | //Accelerate 2026 发布 |
| **hyperscale 分层** | DFM 切入 hyperscaler 存储层级的**高容量闪存层**（原由 HDD 服务的"大规模、相对冷"数据），**非**低延迟高性能层 | FY28 起放量 |
| **CXL** | **未查到**任何官方 CXL 路线图或产品声明 | — |
| **下一节点** | **2026-09-23 Financial Analyst Meeting**（将披露长期战略、增长路径与财务框架） | 待举行 |

### AI 战略：从"全闪存黑马"到"企业数据云"
提出 **Data Primacy（数据首要性）架构**，主张 AI 时代存储须从被动容量层转为统一智能数据平台，而非孤岛式存储。

**NVIDIA 合作的深度与具体性**：FlashBlade//EXA 对齐 NVIDIA **AI Factory** 架构（含模块化 **STX** 参考架构与下一代 **Vera Rubin** 平台），采用 **BlueField DPU 存储控制器** + 上下文内存架构；已完成 **NVIDIA-Certified Storage (NVCS)** 认证。认证/参考架构清单含 DGX GB300/GB200/B300 SuperPOD with FlashBlade、**AIRI（Everpure + NVIDIA DGX BasePOD）**、NVIDIA Run:ai + Portworx + FlashBlade、NVIDIA MONAI NIM。内部验证大型 Hopper/H100 集群 **GPU 利用率 >90%**。

> ⚠️ 注意：**Q2 FY27 官方新闻稿正文完全未提及 NVIDIA**——AI 合作主要在技术文档/博客层面，不在财报口径内。

### 结构性亮点：hyperscale 突破
| 客户 | 内容 |
|------|------|
| **Meta** | 第一家大客户，2024 年底签约，DFM 供应 |
| **第二家 Top-5 超大规模客户（未具名）** | 2026-08-10 宣布 design win + 供货协议；**累计承诺延续至 2028 自然年，涉及数十 EB**；FY27 收入贡献 de minimis，**FY28 起显著放量** |

> CTO Rob Lee 已明确表示**今后不再披露单个 hyperscaler 客户或 design win 时点**，统一以"hyperscale solutions"口径披露。

## 融资与现金流

### 资产负债表（截至 2026-08-02）
| 项目 | 值 |
|------|-----|
| 长期债务 | **无报告**（长期借款与流动部分均为空） |
| 总债务 | $225.31M（**主要为租赁负债，非借款**） |
| **净现金** | **$782.58M** |
| 现金 + 等价物 | $385.69M |
| 短期投资 | $622.20M |
| 现金+投资合计 | $1.0B（同比 −34.45%） |

> **零借款**是全闪存同业中罕见的资产负债结构，也是公司在 NAND 涨价周期中能"战略囤货"的底气。

### 现金流：Q2 FY27 双转负
| 指标 | FY2026 | Q1 FY2027 | Q2 FY2027 |
|------|--------|-----------|-----------|
| 经营现金流 | $880M | $180M | **−$136.3M** |
| 自由现金流 | $616M | $112M | **−$237.6M** |
| 回购 | $343M | $84M（1.3M股） | $69M（0.9M股） |

**现金流恶化的原因**：**战略性囤积 NAND 与其他元器件**（CFO 强调为核心业务而非 hyperscaler 业务）。CFO 称定价已大致追上原材料成本涨幅，**预计现金流未来两季恢复正常**；FY27 FCF 指引维持 $600M–800M。市场对此反应负面：财报后股价一度跌约 9% 至约 $99。

### 股东回报
- **2026-01 新批 $400M 回购授权**（公司史上最大）+ 旧计划剩余 $20M
- 无股息；回购为主要回报方式

## 研发投入与专利

| 项目 | 值 | 口径 |
|------|-----|------|
| FY2026 R&D | 约 **$960M（+20%）**，占营收 **25%→26%** | 二手解析，置信度低 |
| TTM R&D | $907.01M（+15.33%） | TTM 至 2026-01-31 |
| FY2025 R&D | **$804M**，约占 $3.2B 营收的 **25%** | 公司博客 |
| 长期承诺 | 公司称长期保持 **>20% 营收投入 R&D** | 官方博客 |
| **专利数量** | **超过 2,500 项已授权专利与专利申请**（美国及海外） | 2024 10-K 口径；**2026 10-K 计数未查到** |

> R&D 占营收 25%+ 在全闪存同业中属极高水平（对比 NetApp 约 14%），是 DFM 垂直整合与 FlashBlade//EXA 性能领先的投入来源。

### 核心技术壁垒
1. **DirectFlash Module（DFM）**——自研闪存模块绕过通用 SSD 的 FTL 层，与 Purity 直接协同，宣称容量效率为通用 SSD 阵列约 **2.5 倍**，密度目标领先竞品 **5 倍**；**全闪存行业中仅 IBM（Flash Core Module）有对标能力**
2. **Purity 软件**——统一块/文件/对象，常在线数据缩减与保护
3. **Evergreen 架构**——控制器与介质解耦、永久升级，形成订阅锁定与低流失率
4. **自研控制器系统**——软硬协同设计能力

### 主要风险
1. **增长质量**——约**三分之一**的 Q2 FY27 增长来自 NAND 涨价与客户提前拉货；产品毛利率被压至 66.2%
2. **现金流风险**——OCF/FCF 双转负，若 NAND 成本未如预期回落，FY27 FCF 指引面临下修
3. **估值极端**——TTM PE ~135x、PS ~7.7x；任何增速放缓都引发剧烈重估
4. **价格竞争**——Dell 以 31.2% 份额（超后四家之和）与价格优势压制；Pure 有效定价通常比 NetApp 低 5%–12%
5. **hyperscale 收入确认节奏**——第二家 Top-5 客户 FY27 贡献 de minimis，FY28 才显著放量，短期无法对冲企业市场波动
6. **NAND 双刃剑**——DRAM/NAND 历史性涨价既推动收入（提价）又压缩毛利（成本），且促使客户提前拉货透支后续需求
7. **公司不再披露 hyperscaler 细节**——信息披露颗粒度下降，跟踪难度上升

## 动态更新记录

### 2026-09-13（新建词条 + FY2027 Q2 & FY2026 年报）
> 来源: 新建（原为赛道页提及但无公司页）
> L0归档: `L0-原始资料池/03-新闻/2026-09-13-Pure-Storage-调研.md` (input_20260913_104)
> 置信度: 高（SEC Ex-99.1 原文 + 公司 IR）

- **词条新建**：补齐 24 个 YAML 字段 + 6 个 Body 段
- **latest_revenue**：FY2027 Q2 $1,185.9M（+38%）；FY2026 全年 $3.66B（+16%）
- **market_cap**：~$327亿（$32.7B，2026.9.11）
- **suppliers/customers/partners/competitors**：分别填充 4/4/7/8 条
- **新增关键信息**：连续8个季度加速、订阅 ARR $2.1B、Evergreen//One TCV 年化超$1B、第二家 Top-5 hyperscaler（承诺至2028、数十EB）、DFM 密度 75→150→300TB 路线、FY27 指引上调至 $5.0B 量级
- **⚠️ 重大变更（必须回写赛道页）**：
  - **公司已更名 Everpure, Inc.**（2026-02-23 宣布，2026-03-05 起交易），**NYSE 代码 2026-04-17 由 PSTG 变更为「P」**，官网迁移至 **everpuredata.com**
  - 本词条 `name` 保留 **Pure Storage** 以匹配赛道页 `companies` 引用名（维持图谱边），`ticker` 取现行 **P**
  - **建议赛道页 `enterprise-storage.md` 同步**：`ticker: PSTG` → `P`，并在 note 中补"2026-02 更名 Everpure"
- **⚠️ 市占率更新（必须回写赛道页）**：赛道页 sources 仍为 **IDC Q3 2025**（Pure 6.8%、+15.5%）；最新 **IDC Q1 2026 为 8.9%、+37.9%、排名第3**（前五中增速最快）。同口径下 Dell 31.2%、NetApp 9.9%、华为 6.7%、HPE 5.4%
- **风险标注**：Q2 FY27 经营现金流−$136M/自由现金流−$238M（战略囤货NAND）、产品毛利率压至66.2%、TTM PE约135倍、约1/3增长来自涨价与前置拉货
- **后续跟踪**：**2026-09-23 Financial Analyst Meeting**（将披露长期财务框架，届时需更新）
