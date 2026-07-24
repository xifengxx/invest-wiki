---
name: Intel
slug: intel
country: US
ticker: INTC
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- AI芯片设计(Fabless)
- CPU(服务器级)
- Chiplet与异构集成
- DPU/SmartNIC
- FPGA
- GPU架构设计
- 先进封装(CoWoS/3D)
- 晶圆代工(先进制程)
- 网络交换芯片
- 边缘AI
one_liner: 全球最大CPU制造商和IDM 2.0转型中的晶圆代工商，设计x86 CPU+Gaudi AI加速器+FPGA，通过芯片销售+晶圆代工+封装服务实现盈利，位于AI算力L3核心产品层
chain_layer: L3
chain_role: 龙头
suppliers:
- company: ASML
  ticker: ASML
  supplies: EUV光刻机
  note: Intel 18A制程关键设备
- company: 应用材料
  ticker: AMAT
  supplies: 沉积/刻蚀设备
- company: 台积电
  ticker: TSM
  supplies: 部分外包代工
  note: GPU tile等部分产品外包台积电
- company: TSMC
  supplies: 先进制程外包代工, Meteor Lake/Arrow Lake GPU模块
- company: SK海力士/三星
  supplies: 存储颗粒DRAM/NAND
customers:
- company: 全球PC OEM
  note: 消费/商用PC处理器
- company: 数据中心客户
  note: Xeon服务器CPU+Gaudi AI加速器
- company: 美国政府
  note: 国防/安全芯片CHIPS法案受益方
- company: 戴尔/惠普/联想/华硕
  note: PC酷睿处理器
- company: AWS/Azure/Google Cloud
  note: Xeon服务器CPU
- company: 亚马逊
  note: 定制AI芯片代工, 2026年数十亿美元签约
- company: 微软
  note: 定制AI芯片代工, 18A制程
- company: 美国国防部
  note: RAMP-C计划, 18A安全芯片
partners:
- company: Arm
  ticker: ARM
  area: 18A制程代工合作
- company: 微软
  ticker: MSFT
  area: Intel 18A芯片代工
  note: 微软自研芯片采用Intel 18A
- company: UMC
  ticker: UMC
  area: 12nm成熟制程合作
competitors:
- company: AMD
  ticker: AMD
  area: x86 CPU+AI加速器
- company: NVIDIA
  ticker: NVDA
  area: AI GPU/加速器
  note: Gaudi3性能落后H100约30%
- company: 台积电
  ticker: TSM
  area: 晶圆代工
  note: Intel代工业务挑战台积电
- company: TSMC
  note: 晶圆代工, 先进制程与封装
- company: 三星电子
  note: 晶圆代工, GAA制程
core_business:
- PC客户端处理器(酷睿Ultra, AI PC芯片, Panther Lake)
- 数据中心与AI芯片(Xeon服务器CPU, Gaudi加速器, 定制ASIC)
- 晶圆代工服务(Intel Foundry, 18A/14A制程, 先进封装EMIB)
- 网络与边缘计算芯片(Ethernet控制器, FPGA, IPU)
revenue_model: PC处理器占营收61%($322亿 FY2025)，数据中心与AI芯片占32%($169亿)，代工占34%($178亿含内部交付)，外部代工仅$1.74亿。向产品+代工双轨转型，代工目标2027年盈亏平衡。
ticker: INTC
description: 英特尔（Intel）成立于1968年，总部位于美国加州圣克拉拉，是全球最大的半导体IDM企业之一，主导x86架构CPU市场。产品覆盖PC、数据中心、网络边缘及AI加速。近年来推动IDM 2.0战略转型，大举投资晶圆代工（Intel Foundry），与台积电、三星竞争先进制程。尽管收入连年下滑、毛利率承压、代工持续亏损，公司凭借深厚技术积累、CHIPS法案资金及新任CEO Lip-Bu
  Tan的领导，力图在AI时代重振。
website: https://www.intel.com
industry: 半导体
founded: 1968
headquarters: 美国加州圣克拉拉
employees: ~125,000
latest_revenue: Q1 2026 $13.58B（净亏$3.73B），Q2 2026E $14.45B
market_cap: ~$170B
---

# Intel

全球最大x86 CPU与半导体IDM巨头，以IDM 2.0战略全面转型，发力AI算力与先进制程代工，押注18A/14A工艺实现技术复兴。

## 财务状况

| 指标 | FY2022 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|--------|
| 营收（亿美元） | 631 | 542 | 531 | **529** |
| 毛利率 | 42.6% | 40.0% | 32.7% | **34.8%** |
| 营业利润（亿美元） | 23 | 0.9 | -117 | **-22** |
| 净利润（亿美元） | 80 | 17 | -188 | **-2.7** |

营收连续四年下滑，从FY2021峰值**790亿**降至FY2025的**529亿**（-33%）。毛利率从55%+降至34.8%，主因代工产能扩张折旧压力。FY2024计提大额减值后净亏188亿；FY2025亏损收窄至2.7亿。

**分部**（FY2024）：CCG **57%**、DCAI **24%**、NEX **11%**、Foundry仅**3.85亿**外部收入，经营亏损约**70亿**。已暂停派息、裁员约15,000人（15%+）、SG&A降16%。获CHIPS法案**79亿**补贴。

## 产品线详解

- **Core Ultra 200系列**：Meteor Lake（Intel 4，首款芯粒设计）、Lunar Lake（AI PC，NPU 48 TOPS）、Arrow Lake（桌面/高性能）
- **Xeon 6**：Granite Rapids（P-core）与Sierra Forest（E-core，最高288核），面向云与AI推理
- **Gaudi 3 AI加速器**：对标NVIDIA H100，市占有限；Falcon Shores（下一代AI GPU）据传已取消
- **Arc独显**：Battlemage架构，主攻中端游戏市场
- **Xeon 7 Diamond Rapids**：计划2027年

**代工**：Intel 3已量产对外代工；**18A**（2025，RibbonFET+PowerVia）已获Fortinet等ASIC订单。

**竞争**：x86 CPU与**AMD**激战（EPYC数据中心份额>25%）；AI被**NVIDIA**压制（数据中心收入千亿 vs Intel数十亿级）；代工远逊**台积电**，处客户拓展初期。

## 技术路线图

英特尔执行「5年4节点」（5N4Y）制程追赶计划，目标2025年前重夺领先地位。

| 节点 | 时间 | 关键技术 | 状态 |
|------|------|----------|------|
| Intel 7 | 2021 | Enhanced SuperFin | 已量产 |
| Intel 4 | 2023 | EUV + FinFET | 已量产 |
| Intel 3 | 2024 | 高密度FinFET | 已量产，对外代工 |
| **Intel 18A** | 2025 | **RibbonFET + PowerVia** | 首批流片 |
| Intel 14A | 2027+ | 二代GAA + High-NA EUV | 研发中 |

**核心技术**：RibbonFET（GAA纳米带晶体管，替代FinFET）；PowerVia（背面供电，释放正面布线空间）；High-NA EUV（全球首家安装ASML高NA光刻机）。

**IDM 2.0**：内部制造+外部代工+为第三方代工。亚利桑那新厂与俄亥俄基地在建。18A良率爬坡是核心风险。


## 融资与现金流

- 详见财务状况章节
## 研发投入与专利

| 年份 | 研发支出（亿美元） | 占营收比 |
|------|-------------------|----------|
| FY2022 | **175** | 27.8% |
| FY2023 | **160** | 29.5% |
| FY2024 | **165** | 31.2% |
| FY2025 | **138** | 26.1% |

FY2025研发支出降16.8%，但占营收比仍超**26%**，远超行业均值（~15%）。对比：NVIDIA约120亿（<5%）、AMD约60亿。

**专利护城河**：全球累计超**10万项**专利，覆盖x86指令集、先进制程、封装（EMIB/Foveros 3D堆叠）、AI加速、量子计算。与AMD共有x86交叉许可，构成PC与服务器CPU核心IP壁垒。ARM（Apple Silicon、AWS Graviton）侵蚀份额，但x86生态短期难撼。

**挑战**：制程落后台积电致设计优势难发挥；AI GPU专利远逊NVIDIA；代工缺乏大规模客户验证。

