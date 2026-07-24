---
name: TSMC(台积电)
slug: tsmc
country: TW
ticker: TSM
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- Chiplet与异构集成
- GPU制造代工
- 先进封装(CoWoS/3D)
- 先进封装CoWoS
- 晶圆代工(先进制程)
one_liner: 全球最大晶圆代工厂和先进封装垄断者，提供3nm/2nm晶圆代工+CoWoS先进封装，通过代工费+封装费实现盈利，位于AI算力L2设备与零部件层——AI芯片制造不可替代
chain_layer: L2
chain_role: 龙头
suppliers:
- company: ASML
  ticker: ASML
  supplies: EUV光刻机
  note: 独家供应High-NA EUV
- company: 应用材料
  ticker: AMAT
  supplies: 沉积/刻蚀/检测设备
- company: 信越化学
  ticker: 4063.T
  supplies: 12寸硅晶圆
- company: 东京电子
  ticker: 8035.T
  supplies: 涂胶显影设备
- company: Applied Materials
  supplies: 薄膜沉积/刻蚀/检测设备，约15.1%份额
- company: Lam Research
  supplies: 等离子刻蚀/干法清洗设备，约9.2%份额
- company: Tokyo Electron
  supplies: 沉积/涂布显影/刻蚀设备，约5.4%份额
- company: KLA Corporation
  supplies: 过程控制/量测/缺陷检测设备，约6.1%份额
customers:
- company: NVIDIA
  ticker: NVDA
  revenue_pct: 25
  note: 4nm+CoWoS，最大客户
- company: Apple
  ticker: AAPL
  revenue_pct: 20
  note: 最新3nm制程独占首发
- company: AMD
  ticker: AMD
  revenue_pct: 10
  note: CPU+GPU代工+封装
- company: Qualcomm
  ticker: QCOM
  revenue_pct: 8
- company: Broadcom
  note: 网络交换芯片/定制AI ASIC晶圆
partners:
- company: NVIDIA
  ticker: NVDA
  area: CoWoS封装+4nm代工
  note: 独家伙伴关系
- company: ARM
  ticker: ARM
  area: IP授权+设计生态
competitors:
- company: 三星电子
  ticker: 005930.KS
  area: 晶圆代工
  note: 3nm GAA抢先量产但良率不足
- company: Intel
  ticker: INTC
  area: 晶圆代工
  note: IDM 2.0转型代工，Intel 18A对标台积电2nm
- company: Samsung Foundry
  note: 先进制程代工，全球份额仅7.2%，2nm GAA制程追赶中
- company: Intel Foundry
  note: IDM 2.0开放代工，18A先进制程竞争
- company: SMIC
  note: 成熟制程代工，聚焦中国市场+DUV受限
- company: GlobalFoundries
  note: 成熟/特殊制程代工，放弃7nm以下先进制程
core_business:
- 先进制程晶圆代工（3nm/5nm/2nm/1.6nm逻辑芯片量产）
- CoWoS/InFO/SoIC先进封装与3D-IC芯片堆叠集成
- AI/HPC加速器芯片专用制程（GPU/TPU/Trainium晶圆制造）
- 成熟特殊制程代工（车用电子/IoT/射频/嵌入式存储）
revenue_model: 纯晶圆代工模式，按晶圆数量与制程节点收取制造费用。HPC/AI平台占营收58%($71B)，先进制程(7nm以下)占晶圆收入74%。FY2025总营收$1224亿，毛利率59.9%，净利$552亿。
founded: 1987
headquarters: 台湾新竹
employees: ~77,000
latest_revenue: Q2 2026 $40.2B（FY2026E >$160B，+40% YoY）
market_cap: ~$2.2T（2026.7）
description: 台积电（TSMC）是全球最大、技术最先进的半导体代工厂，由张忠谋（Morris Chang）于1987年在台湾新竹创立，开创纯晶圆代工（Pure-Play Foundry）商业模式——只制造芯片、不设计芯片，绝不与客户竞争。公司市值约1.9万亿美元，2025年营收突破1,220亿美元，占全球先进芯片制造90%以上份额，客户包括苹果、英伟达、AMD和高通，是AI时代不可或缺的基础设施级企业。
website: https://www.tsmc.com
industry: 半导体
---

# TSMC(台积电)

全球半导体代工绝对霸主，从3nm到2nm持续定义摩尔定律前沿，以纯晶圆代工模式赋能苹果、英伟达等科技巨头，构筑AI算力世界的物理基石。

## 财务状况

台积电2025财年营收与盈利均创历史新高，AI与高性能计算（HPC）需求为核心增长引擎。

| 指标 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|
| 营收（亿美元） | 708 | 901 | **1,224** |
| 营收同比增速 | -4.5% | +27.3% | **+35.9%** |
| 净利润（亿美元） | 278 | 353 | **541** |
| 毛利率 | 54.4% | 56.1% | **59.9%** |
| 营业利润率 | 42.6% | 45.7% | **50.8%** |
| 净利率 | 38.8% | 39.2% | **45.1%** |
| 每股收益（新台币） | 32.34 | 45.25 | **66.25** |
| 资本支出（亿美元） | 305 | 298 | **409** |

**2025年Q4制程收入占比**：3nm占**28%**，5nm占**35%**，7nm占**14%**，先进制程（≤7nm）合计贡献晶圆收入的**74%**。按应用平台，HPC占比**58%**，智能手机约35%，AI加速器贡献总营收的**15%**。市值截至2026年中约**1.9万亿美元**，位列全球市值前五。

## 产品线详解

**先进制程（N3家族）**：涵盖N3、N3E、N3P、N3X、N3A节点，覆盖移动端、HPC及汽车应用。相较N5，基础性能提升**18%**或功耗降低**32%**。N3E于2023年Q4量产，逻辑密度为N5的1.6倍。N3P为性能增强版，是2025-2026年主流节点，英伟达下一代**Rubin GPU**将采用。3nm产能已被苹果、英伟达等客户全额预订至2026年。

**3D Fabric先进封装平台**：
- **SoIC**（系统整合芯片）：3D芯片堆叠技术，AMD MI300系列全球首发采用，苹果M5及英伟达Rubin跟进，预计2026年底前30个客户完成流片
- **CoWoS**（晶圆基板上芯片）：AI芯片核心封装方案，英伟达Blackwell GPU使用CoWoS-L版本，英伟达独占约**50%**产能；AMD、博通、亚马逊次之
- **InFO**（整合扇出型）：面向移动与系统级晶圆整合

**主要客户**：**苹果**（A/M系列处理器）、**英伟达**（GPU/AI加速器）、**AMD**（CPU/GPU）、**高通**（Snapdragon平台）、英特尔、博通。

## 技术路线图

台积电首次从FinFET转向**GAA（环绕栅极）纳米片晶体管**架构，并引入背面供电技术，形成双轨制创新路线。

| 节点 | 晶体管类型 | 背面供电 | 量产时间 |
|------|-----------|----------|----------|
| **N2** | 第1代GAA纳米片 | 无 | 2025年H2 |
| **N2P** | GAA增强版 | 无 | 2026年 |
| **N2X** | GAA性能极速版 | 无 | 2027年 |
| **A16** | GAA + **SPR** | **有（第1代）** | 2026年末/2027年 |
| **A14** | 第2代GAA | 无（2029年增SPR版） | 2028年 |
| **A12** | 第2代GAA + SPR | **有（第2代）** | 2029年 |

核心性能提升：N2比N3E性能提升**15%**、功耗降低**30%**；A16首次采用**Super Power Rail背面供电**（BSPDN），将电源线路移至晶圆背面，性能再提升**8-10%**；A14比N2逻辑密度提升超**20%**。关键战略差异化：台积电明确表示**至少在2029年前无需High-NA EUV光刻机**（单台成本约4亿美元），依靠设计工艺协同优化（DTCO）和设计规则创新保持成本竞争力与迭代速度。


## 融资与现金流

- 详见财务状况章节
## 研发投入与专利

**研发投入规模**：2024年研发支出**63.55亿美元**（占营收7.1%），十年间增长3.1倍。2025年研发预算约占总营收的**7%**，长期目标为**7%-9%**。2nm、A16、A14及下一代晶体管、新材料等前沿项目占总研发预算的**83%**，研发周期跨越8-10年。

**专利护城河**：截至2024年底——
- 全球累计专利申请超**10.4万件**（2024年新增9,100件），累计授权专利超**6.9万件**
- 连续三年位列**美国专利申请人第2名**（仅次于三星），台湾专利申请**第1名**
- 美国专利授权率接近**100%**（全美平均仅61%），位列前十大专利持有者之首
- 专利前向引用超**35,000次**，专利质量极高
- 累计注册超**100万件**营业秘密，2024年新增13.1万件

台积电采用**“专利+商业秘密”双轨保护策略**：制程配方、设备参数等核心know-how以商业秘密保护，结构设计与工艺创新以专利壁垒防御，形成竞争对手极难逾越的技术护城河。

