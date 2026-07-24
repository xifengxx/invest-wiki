---
name: Marvell Technology
slug: marvell
country: US
ticker: MRVL
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- AI芯片设计(Fabless)
- ASIC/AI定制芯片
- DPU/SmartNIC
- DSP与光芯片
- IC设计服务(Fabless)
- 网络交换芯片
one_liner: 全球第二大AI ASIC定制芯片设计商（与Broadcom双寡头，份额~20-25%），为Amazon定制Trainium/Inferentia、为Microsoft定制Maia AI加速器，通过ASIC设计服务+数据中心芯片（DSP/光互联/交换机）销售实现盈利，FY2026营收$8.2B（+42%），数据中心占76%，市值~$190B。
chain_layer: L3
chain_role: 龙头
suppliers:
- company: 台积电
  ticker: TSM
  supplies: 晶圆代工+CoWoS封装
  note: ASIC芯片制造，2nm/3nm制程
- company: SK海力士
  ticker: 000660.KS
  supplies: HBM3E
  note: 定制XPU使用HBM内存
customers:
- company: Amazon AWS
  ticker: AMZN
  revenue_pct: 20
  note: Trainium/Inferentia ASIC设计服务
- company: Microsoft Azure
  ticker: MSFT
  revenue_pct: 15
  note: Maia AI加速器 + 数据中心光互联芯片
- company: Google Cloud
  ticker: GOOGL
  revenue_pct: 5
  note: 洽谈2款定制AI芯片（内存处理单元+新一代TPU架构）
partners:
- company: NVIDIA
  ticker: NVDA
  area: NVLink Fusion平台
  note: $2B战略投资，Marvell XPU集成NVIDIA AI计算栈
- company: 台积电
  ticker: TSM
  area: 制程+先进封装
  note: 2nm/3nm制程+CoWoS封装+硅光子
- company: Amazon
  ticker: AMZN
  area: Trainium联合设计
  note: 多代ASIC芯片深度绑定
competitors:
- company: Broadcom
  ticker: AVGO
  area: AI ASIC设计服务
  note: 双寡头，Broadcom~50-60%份额 vs Marvell~20-25%
- company: NVIDIA
  ticker: NVDA
  area: AI加速器
  note: 互补>竞争（NVLink Fusion合作），GPU vs ASIC路线
- company: Intel
  ticker: INTC
  area: 网络芯片/FPGA
  note: 数据中心网络芯片
core_business:
- 定制AI ASIC/XPU设计（Amazon Trainium/Inferentia, Microsoft Maia — 占76%营收）
- 数据中心光互联DSP（800G/1.6T PAM4，光互联营收FY2027增长70%+）
- 数据中心以太网交换机（51.2T/102.4T，目标FY2028 $1B）
- 存储控制器/DPU/CXL/安全芯片（被AI业务稀释中，占比持续下降）
revenue_model: FY2026营收$8.195B（+42% YoY），Q1 FY2027 $2.418B（+28% YoY），FY2027E ~$11.5B（+40%）。Data Center 76%（$1.833B/Q1），光互联~70%增长，定制ASIC $10B FY2029目标。GAAP净利润受$332M对价费用和$208M股权激励压缩（Q1 GAAP净利润极低），Non-GAAP运营利润率~35-40%。
founded: 1995
headquarters: 美国加州Santa Clara
employees: ~13,000
latest_revenue: FY2026 $8.195B（+42% YoY），FY2027E ~$11.5B
market_cap: ~$190B（2026.7）
description: Marvell Technology是全球第二大AI定制芯片（ASIC）设计服务商，1995年成立于美国加州Santa Clara。公司从存储控制器和网络芯片起家，近年通过收购（Cavium/Aquantia/Inphi/Innovium/Celestial AI/XConn）和剥离非核心业务（汽车以太网→Infineon $2.5B），全面转型为AI基础设施核心供应商。数据中心业务占比从FY2022的~30%飙升至76%（FY2027 Q1），与Broadcom形成AI ASIC双寡头格局。2026年3月NVIDIA $2B战略投资+NVLink Fusion合作，确认Marvell作为AI计算生态关键互补角色。
website: https://www.marvell.com
industry: AI算力
---

# Marvell Technology

AI定制芯片双寡头之一（与Broadcom），Amazon Trainium + Microsoft Maia 核心设计商，数据中心营收占比76%且持续增长，NVIDIA $2B战略投资确认互补生态地位，目标FY2029定制芯片$10B。

## 财务状况

Marvell财年截至每年1月底。AI定制芯片和数据中心光互联双引擎推动营收高速增长。

### 年度核心财务指标

| 指标 | FY2025 | FY2026 | 同比变化 |
|------|--------|--------|----------|
| **总营收** | ~$5.8B | **$8.195B** | +42% |
| **Data Center占比** | ~55% | **~70%** | +15pp |
| **Non-GAAP运营利润率** | ~30% | **~35-38%** | +5-8pp |

### FY2027共识预测

| 指标 | 数据 |
|------|------|
| Q1实际营收 | **$2.418B**（+28% YoY） |
| FY2027E营收 | **~$11.5B**（+40% YoY） |
| Data Center占比（Q1） | **76%** |
| 定制ASIC Design Wins | **50+**个项目/**10+**个客户 |

## 业务板块

| 板块 | 产品 | 增长动力 |
|------|------|----------|
| **定制ASIC/XPU** | Amazon Trainium/Inferentia, Microsoft Maia | 50+ Design Wins, $10B FY2029目标 |
| **光互联** | 800G/1.6T PAM4 DSP, 硅光子 | FY2027 +70%增长，AI集群互联需求 |
| **以太网交换机** | 51.2T/102.4T Teralynx | 目标FY2028 $1B |
| **存储/DPU/CXL** | BRAVO NVMe, OCTEON DPU | 非核心，占比持续下降 |

## 战略转型路径

1. **收购Cavium (2018)** → 进入网络/DPU
2. **收购Aquantia/Avera/Inphi/Innovium (2019-2021)** → 构建数据中心完整技术栈
3. **剥离汽车以太网→Infineon $2.5B (2026)** → 聚焦AI基础设施
4. **收购Celestial AI + XConn (2026.2)** → 补强硅光子+Chiplet互联
5. **NVIDIA $2B投资 + NVLink Fusion (2026.3)** → 生态卡位


## 融资与现金流

- 详见财务状况章节
## 竞争分析

| 维度 | Marvell | Broadcom |
|------|---------|----------|
| 定制ASIC份额 | ~20-25% | ~50-60% |
| 光互联DSP | ✅ 领先 | ❌ 基本不参与 |
| 以太网交换机 | Teralynx 51.2T | Tomahawk 51.2T |
| 定制ASIC客户 | Amazon、Microsoft、Google（洽谈） | Google TPU、Meta MTIA |
| NVIDIA关系 | 合作伙伴（NVLink Fusion+$2B投资） | 竞争关系 |
