---
name: NVIDIA
slug: nvidia
country: US
ticker: NVDA
type: company
updated: 2026-08
data_freshness_date: 2026-08-18
segments:
- AI服务器
- AI模型训练平台
- AI芯片设计(Fabless)
- CIS图像传感器
- CPU(服务器级)
- Chiplet与异构集成
- DPU/SmartNIC
- EDA与IP核
- GPU制造代工
- GPU架构设计
- 先进封装(CoWoS/3D)
- 先进封装CoWoS
- 数据中心IDC
- 网络交换芯片
- 自动驾驶
- 边缘AI
one_liner: |
  全球领先的AI全栈基础设施公司，核心为AI训练/推理GPU与数据中心系统（Blackwell、Rubin、DGX），通过GPU芯片与系统级解决方案销售实现盈利（数据中心收入占约90%），位于AI计算基础设施核心供应商——掌握约80%市场份额与CUDA生态壁垒的AI算力平台。
  【2026.8.18更新】Q1 FY2027营收$81.6B(+85%)历史新高，数据中心$75.2B占92%，净利$58.3B(+211%)；Q2指引$91B(8/26发布)，股息提高至$0.25/股。
chain_layer: L3
chain_role: 龙头
suppliers:
- company: SK海力士
  ticker: 000660.KS
  supplies: HBM3E
  note: HBM主力供应商
- company: 台积电
  ticker: TSM
  supplies: CoWoS封装+晶圆代工
  note: 独家先进制程+封装伙伴
- company: 三星电子
  ticker: 005930.KS
  supplies: HBM3
  note: HBM第二供应商
- company: 安费诺
  ticker: APH
  supplies: 高速连接器
- company: TSMC
  supplies: 4nm/3nm先进制程代工、CoWoS先进封装，占NVIDIA约70%以上产能配额
- company: SK Hynix
  supplies: HBM3/HBM3e高带宽内存，为主要HBM供应商
- company: ASE Group/Amkor
  supplies: 先进封装与测试服务
- company: Foxconn
  supplies: AI服务器系统组装与集成
- company: ASML
  supplies: EUV极紫外光刻设备，间接通过TSMC供应
customers:
- company: Microsoft Azure
  ticker: MSFT
  revenue_pct: 20
  note: AI训练集群GPU采购
- company: Meta
  ticker: META
  revenue_pct: 15
  note: 开源大模型训练
- company: Google Cloud
  ticker: GOOGL
  revenue_pct: 12
  note: Gemini训练+推理
- company: Amazon AWS
  ticker: AMZN
  revenue_pct: 10
  note: Trainium补充+GPU推理
- company: Oracle
  ticker: ORCL
  revenue_pct: 5
  note: 云GPU租赁
- company: OpenAI/Anthropic
  note: 前沿大模型训练GPU，OpenAI年采购量逾百万颗
partners:
- company: 台积电
  ticker: TSM
  area: CoWoS封装+4nm代工
  note: 独家先进封装+晶圆代工伙伴
- company: Arm
  ticker: ARM
  area: Grace CPU架构授权
- company: SK海力士
  ticker: 000660.KS
  area: HBM联合研发
competitors:
- company: AMD
  ticker: AMD
  area: AI GPU
  note: MI300X/350系列对标H100/B200
- company: Intel
  ticker: INTC
  area: AI加速器
  note: Gaudi3对标但生态差距大
- company: Broadcom
  ticker: AVGO
  area: ASIC定制芯片
  note: Google TPU+Meta ASIC间接竞争
- company: 华为
  area: AI芯片
  note: 昇腾系列国产替代
- company: Google
  note: TPU Ironwood自研AI芯片，已向Anthropic/Meta提供，TCO比GB200低44%
core_business:
- AI训练与推理GPU芯片设计（Blackwell B200、Rubin R100、Hopper H100/H200）
- 数据中心AI系统与平台（DGX B200、GB200 NVL72液冷机架系统、DGX SuperPOD集群）
- 高性能网络互联产品（NVLink 5、InfiniBand NDR400、Spectrum-X以太网交换机）
- AI软件平台与全栈生态（CUDA、cuDNN、TensorRT推理、NIM微服务、Dynamo推理OS）
- 边缘计算与自动驾驶平台（DRIVE Hyperion、Jetson嵌入式AI、GeForce消费GPU）
revenue_model: FY2026（截止2026年1月）营收$2159亿，其中数据中心Compute & Networking业务贡献$1935亿（占总营收约90%），毛利率71%；此外软件订阅（CUDA企业版、NIM）和DGX Cloud租赁提供经常性收入。FY2027 Q1营收达$816亿。
founded: 1993
headquarters: 美国加州圣克拉拉
employees: ~36,000
latest_revenue: Q1 FY2027 $81.6B（+85% YoY，历史新高）；Q2 指引$91B
market_cap: ~$4.8T（2026.7，全球第一）
description: 英伟达（NVIDIA）是全球AI算力芯片绝对龙头，1993年由黄仁勋、Chris Malachowsky和Curtis Priem创立于美国加州。1999年发明GPU，2006年推出CUDA并行计算平台，2016年后全面转型AI计算，市值从数百亿美元飙升至超4万亿美元。FY2026营收$2,159亿，数据中心业务占比超90%，是ChatGPT时代最大的基础设施赢家。
website: https://www.nvidia.com
industry: AI算力
---

# NVIDIA

从游戏显卡到AI基础设施，CUDA生态锁定400万开发者，Blackwell→Rubin→Feynman年更架构推动算力指数增长，全球85%+ AI训练跑在英伟达芯片上。

## 财务状况

英伟达财年截至每年1月底。AI训练和推理需求的指数级增长驱动公司营收连续两年翻倍后继续保持高速增长。

### 年度核心财务指标

| 指标 | FY2025（2025.1止） | FY2026（2026.1止） | 同比变化 |
|------|---------------------|---------------------|----------|
| **总营收** | $1,305亿 | **$2,159亿** | +65% |
| **数据中心收入** | ~$1,150亿 | **$1,937亿** | +68% |
| **营业利润** | $814.5亿 | **$1,303.9亿** | +60% |
| **净利润** | $728.8亿 | **$1,200.7亿** | +65% |
| **稀释每股收益** | $2.94 | **$4.90** | +67% |
| **毛利率** | ~72.7% | ~71-75% | — |
| **自由现金流** | — | **$490亿** | — |

### FY2027 Q1（2026年5月报告）

| 指标 | 数据 |
|------|------|
| 单季营收 | **$816.2亿**（+85% YoY，历史新高） |
| 数据中心收入 | **$752亿**（+92% YoY，占92%） |
| 净利（GAAP） | **$583.2亿**（+211% YoY） |
| 营业利润 | **$535亿**（+147% YoY） |
| 毛利率 | **74.9%**（GAAP）/ 75.0%（non-GAAP） |
| 摊薄 EPS（GAAP） | **$2.39**（+214% YoY） |
| 摊薄 EPS（non-GAAP） | **$1.87**（超预期$1.77） |

#### Q1 FY2027 详情（海豚研究）

**全面超预期**：营收 $81.6B（+85% YoY）历史新高，净利 $58.32B（+211%），毛利率 74.9%（+14.4pp）。数据中心 $75.2B（+92%）占 92%：计算 $60.4B（+77%）、网络 $14.8B（+199%）。边缘计算 $6.4B（+29%）。GAAP 净利含 ~$15.9B 非现金股权证券收益（故 GAAP EPS $2.39 远高于 non-GAAP $1.87）。

**Q2 FY2027 指引**（8/26 盘后发布）：营收 ~$91B（$89.2-92.8B），毛利率 GAAP 74.9% / non-GAAP 75.0%，不含中国数据中心计算收入。

**资本回报**：季度股息从 $0.01 提高至 $0.25/股，追加 $80B 回购授权，Q1 回购 ~$20B（单季纪录），自由现金流 $48.6B。FY2027 税率指引下调至 16-18%。

### 市值里程碑

- 2023年5月：突破**$1万亿**
- 2024年2月：突破**$2万亿**
- 2024年6月：突破**$3万亿**，超越苹果成为全球市值第二大公司
- 2026年3月：市值约**$4.45万亿**，位居全球最值钱公司之列

## 产品线详解

英伟达业务分为四大板块，数据中心为绝对核心，FY2025各板块营收如下：

| 板块 | FY2025营收 | 占比 | 同比 |
|------|-----------|------|------|
| **数据中心** | $1,151.9亿 | 88.3% | +142% |
| **游戏** | $113.5亿 | 8.7% | +9% |
| **专业可视化** | $18.8亿 | 1.4% | +21% |
| **汽车与机器人** | $16.9亿 | 1.3% | +55% |

### 数据中心（核心）
- **Blackwell B200**：192GB HBM3e，18 PFLOPS FP4算力，1000W TDP，面向万亿参数大模型训练
- **Blackwell B100**：192GB HBM3e，14 PFLOPS FP4，700W TDP，面向企业级AI训练和推理
- **B300（Blackwell Ultra）**：288GB HBM3e，30 PFLOPS FP4，~1.5倍B200性能，2025年主力出货产品
- **H100/H200（Hopper）**：前代主力，H200提供141GB HBM3e，仍占大量存量部署
- **DGX SuperPOD** + **GB300 NVL72**：机柜级AI超算系统，72颗GPU通过NVLink互联

### 游戏（GeForce）
- **GeForce RTX 50系列**（Blackwell架构）：面向消费级游戏和创作者，支持DLSS 4和光线追踪
- **GeForce RTX 40系列**（Ada Lovelace）：FY2025游戏营收增长的主要驱动力

### 专业可视化
- **RTX Ada工作站GPU**：面向工程设计、影视渲染、科学模拟等专业领域
- **DGX Spark**：AI开发桌面超算，推动ProVis板块Q3 FY2026同比+56%增长

### 汽车与机器人
- **NVIDIA DRIVE Orin**：已量产的车规级自动驾驶SoC，广泛应用于主流车企
- **NVIDIA DRIVE Thor**：下一代2000 TOPS算力的集中式车载计算平台
- Uber自动驾驶L4合作项目，汽车板块FY2025同比增长55%

## 技术路线图

英伟达已确立**年度迭代**的产品节奏，每一代均以传奇科学家命名：

### 已发布 & 量产
| 平台 | 时间 | 制程 | 内存 | 关键参数 |
|------|------|------|------|----------|
| **Hopper（H100/H200）** | 2022-2024 | TSMC 4nm | 141GB HBM3e | 3958 TFLOPS FP8 |
| **Blackwell（B100/B200）** | 2024-2025 | TSMC 4NP | 192GB HBM3e | 18 PFLOPS FP4 |
| **Blackwell Ultra（B300）** | 2025-2026 | TSMC 4NP | 288GB HBM3e | 30 PFLOPS FP4 |

### 即将到来
| 平台 | 时间 | 关键参数 | 亮点 |
|------|------|----------|------|
| **Vera Rubin NVL144** | 2026 H2 | TSMC 3nm, 288GB HBM4, 3.6 EFLOPS FP4 | 全新Vera CPU（88核ARM），100%液冷，模块化无电缆设计 |
| **Rubin Ultra NVL576** | 2027 H2 | TSMC 3nm, 1TB HBM4e, 15 EFLOPS FP4 | 4颗retical-size die拼装，~600kW/机柜，800VDC供电 |
| **Feynman GPU + Rosa CPU** | 2028 | — | 下一代架构，光学NVLink互联 |

### 互联技术路线
- **NVLink 6**：260 TB/s互联带宽，随Vera Rubin同步上市
- **NVLink 7**：随Rubin Ultra在2027年推出
- **ConnectX-9 SuperNIC**：28.8 TB/s
- **Spectrum-6**：共封装光学（CPO）200G以太网交换机
- **Groq LPU**：2026年推出Groq 3，面向低延迟推理场景


## 融资与现金流

- 自由现金流: 490亿
## 研发投入与专利

### R&D投入
- **FY2025**：研发支出 **$129.1亿**（同比+48.9%，占营收约9.9%）
- **FY2026**：研发支出 **$184.97亿**（同比+43.2%，占营收约8.6%）
- Q4 FY2026单季研发支出达**$55.1亿**（同比+48.4%），创历史最高
- 有外部估算认为英伟达实际全口径研发预算（含芯片流片、软件生态等）接近**$300亿/年**

### CUDA生态护城河
- 全球**400万+**开发者依赖CUDA平台进行GPU编程
- 超过**3,000个**GPU加速应用已深度集成CUDA
- CUDA全面覆盖PyTorch、TensorFlow、JAX等所有主流AI框架
- 全球高校普遍将CUDA作为GPU编程和AI课程的标准教学环境
- 90%+ AI研究论文使用的软件栈引用CUDA优化
- 构建时间超过20年，切换成本极高——竞争对手（AMD ROCm、Intel oneAPI）难以在短期内复制

### 生态系统防御投资
- 2026年3月宣布**5年$260亿**投资开发开源AI模型，锁住开发者、收集反馈数据、拓展软件生态护城河
- 战略收购构建完整技术堆栈：Mellanox（网络）、Cumulus Networks（网络操作系统）、DeepMap（地图）、Arm（尝试）、Groq（LPU推理加速）

### 专利资产
- 拥有**超过2万项**已授权和申请中的全球专利
- 核心专利覆盖GPU架构、并行计算、光线追踪、AI推理加速、互联技术（NVLink/NVSwitch）、内存子系统等关键技术领域

