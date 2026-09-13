---
name: Tenstorrent
slug: tenstorrent
country: US
type: company
updated: 2026-09
data_freshness_date: 2026-09-13
segments:
- RISC-V AI芯片
- AI芯片设计(Fabless)
one_liner: |
  RISC-V架构AI芯片与IP授权公司，由传奇芯片架构师Jim Keller领导，核心为Tensix AI核心与Ascalon RISC-V CPU核心，通过成品芯片销售与IP授权双轨实现收入，位于AI算力L3核心产品层——以"反NVIDIA"路线（避开HBM，用GDDR6+片上SRAM+标准以太网）寻求成本优势。
  【2026.9.13更新】2026年6月高通洽谈以$80-100亿收购（约为2024年底$26亿估值的4倍）；此前累计融资超$10亿（Fidelity领投），三星/LG/现代/起亚均为投资方；Galaxy Blackhole平台定价$110,000，据称为NVIDIA DGX的1/3-1/5成本。
chain_layer: L3
chain_role: 核心参与者
suppliers:
- company: 晶圆代工供应商
  supplies: 芯片代工
  note: 具体代工伙伴未在搜索中明确
- company: GDDR6 内存供应商
  supplies: GDDR6 显存
  note: 刻意避开昂贵的HBM
- company: 标准以太网生态
  supplies: 集群互联（替代InfiniBand）
customers:
- company: 现代/起亚
  ticker: 005380.KS
  note: 既是投资者也是合作伙伴（汽车AI芯片）
- company: AI 数据中心客户
  note: Galaxy Blackhole 平台面向的推理/训练客户
- company: IP 授权客户
  note: RISC-V CPU/AI 核心授权
partners:
- company: 三星
  ticker: 005930.KS
  area: 战略投资
- company: LG电子
  ticker: 003550.KS
  area: 战略投资
- company: Fidelity
  area: 领投方（2025年11月$8亿轮）
- company: Bezos Expeditions
  area: 投资方
- company: Hyundai / Kia
  ticker: 005380.KS
  area: 投资 + 汽车芯片合作
competitors:
- company: NVIDIA
  ticker: NVDA
  area: AI 加速器
  note: Tenstorrent 直接对标的行业霸主
- company: AMD
  ticker: AMD
  area: AI GPU
- company: Intel
  ticker: INTC
  area: AI加速器
  note: 2026年5月曾与Tenstorrent有早期收购接触
- company: 高通
  ticker: QCOM
  area: AI芯片（潜在收购方）
  note: 2026年6月洽谈以$80-100亿收购Tenstorrent
- company: Arm
  ticker: ARM
  area: CPU IP 授权
  note: TT-Ascalon 直接对标 Arm Neoverse V2/V3
core_business:
- RISC-V AI 加速器（Tensix AI 核心）
- RISC-V CPU 核心（Ascalon，TT-Ascalon 旗舰产品）
- AI 芯片 IP 授权业务
- Galaxy Blackhole 集群平台（32个加速器）
- 汽车 RISC-V CPU "Alexandria"（面向 ADAS）
revenue_model: 双轨模式——既销售成品芯片（如 Galaxy Blackhole 平台，定价$110,000），也对外授权 IP（Tensix AI核心与Ascalon RISC-V CPU核心）。**公司未上市，无公开财务数据**。核心理念是以成本优势切入：避开昂贵的HBM，改用GDDR6+片上SRAM，集群用标准以太网，据称成本仅为NVIDIA DGX的1/3到1/5而效率高数倍。
founded: 2016
headquarters: 美国（原加拿大多伦多，后迁册美国）
latest_revenue: 未公开（未上市公司）
market_cap: 收购报价 $80-100亿（2026.6 高通洽谈）；2025.11 融资投前估值 $32亿
description: Tenstorrent 2016年成立于加拿大（后迁册美国），是RISC-V架构AI芯片公司。传奇芯片架构师Jim Keller（曾主导Apple A系列、AMD Zen架构、Tesla自动驾驶芯片）约2020年加入任CTO、2023年任CEO。公司设计Tensix AI核心与Ascalon RISC-V CPU核心，同时销售成品芯片与授权IP。2026年6月，高通被报道正洽谈以$80-100亿收购该公司，为2024年底$26亿估值的约4倍。
website: https://tenstorrent.com
industry: AI算力
---

# Tenstorrent

Jim Keller 的"反 NVIDIA"实验——不用 HBM、不用 InfiniBand，靠 GDDR6 + 片上 SRAM + 标准以太网把成本压到 DGX 的 1/3。这条路线的商业价值，被高通 $80-100 亿的收购报价给出了定价。

## 财务状况

Tenstorrent 为**未上市公司**，无公开财报。采用「融资估值 + 收购报价」口径。

### 融资与估值历史

| 时间 | 事件 | 估值 |
|------|------|------|
| 2024-12 | Series D 完成 | **$26亿** |
| 2025-11 | 据报募资 **$8亿**（Fidelity 领投） | **$32亿**（投前） |
| 累计融资 | **超过 $10亿** | — |

**投资方**：Fidelity、AFW Partners、Eclipse Ventures、**三星、LG电子**、Baillie Gifford、**Bezos Expeditions**、Healthcare of Ontario Pension Plan。**现代与起亚既是投资者也是合作伙伴**。

### 2026年核心事件：高通收购谈判

| 项 | 内容 |
|----|------|
| 时间 | **2026年6月**（The Information 6月15-16日报道） |
| **报价** | **$80亿 ~ $100亿** |
| 溢价 | 约为 2024年底 $26亿估值的 **4倍** |
| 竞争方 | Bloomberg 2026年5月报道 **Intel 与 Qualcomm 均**有早期收购接触 |
| 状态 | **谈判进行中，可能变化或破裂**；两家公司均未确认 |
| 市场反应 | 高通股价盘后跌约 **1%**（对高估值存疑） |

> ⚠️ **口径提示**：$80-100亿是**收购报价**，非融资估值。搜索未返回 2026 年新融资轮的估值。

## 产品线详解

### Tensix AI 核心 + Ascalon RISC-V CPU
公司的两大技术基石。**TT-Ascalon**（含Ascalon-X核心）被评为**可与 Arm Neoverse V2/V3 竞争**——这是RISC-V阵营向Arm主导的服务器CPU市场发起的直接挑战。

### Galaxy Blackhole 平台（旗舰系统）
**32个加速器**组成，定价 **$110,000**。据称为 **NVIDIA DGX 的 1/3 到 1/5 成本，而效率高数倍**——成本优势来源于架构选择而非规模效应。

### 汽车 RISC-V CPU "Alexandria"
面向 **ADAS**，契合高通的 Snapdragon Digital Chassis 战略——这也是高通收购动机之一。

### IP 授权业务
Tensix AI核心与Ascalon CPU核心均可对外授权，形成"卖芯片+卖IP"双轨。

## 技术路线图

| 方向 | 状态 | 时间 |
|------|------|------|
| **避开HBM路线** | 用 GDDR6 + 片上 SRAM 替代昂贵HBM | 已实施 |
| **标准以太网集群** | 替代 InfiniBand | 已实施 |
| TT-Ascalon CPU | 对标 Arm Neoverse V2/V3 | 2026 |
| Galaxy Blackhole | 32加速器，$110,000 | 2026 |
| 汽车 RISC-V（Alexandria） | 面向ADAS | 2026-2027 |
| **被收购整合** | 高通洽谈中（$80-100亿） | 待定 |

## 融资与现金流

- 累计融资 **超过 $10亿**，投资方含三星、LG、Bezos Expeditions、Fidelity 等
- **无公开财务数据**，未盈利状态不明
- 2026年6月的高通收购谈判若成行，将是近年来最大的AI芯片交易之一
- 报道提示可能采用 **earn-out/里程碑付款结构** 以对冲高估值风险

## 研发投入与专利

- 核心壁垒：
  1. **Jim Keller 本人的架构能力与行业号召力**——Apple A系列、AMD Zen、Tesla FSD 的履历是稀缺资产
  2. **"反NVIDIA"的成本路线**——避开HBM这一AI芯片最大的成本项与供应瓶颈，改用GDDR6+片上SRAM
  3. **RISC-V 开放性**——不依赖Arm授权，规避Arm诉讼与授权费风险
  4. TT-Ascalon 具备与 Arm Neoverse V2/V3 竞争的性能定位
- **主要风险**：
  1. **收购谈判未确认**，可能破裂
  2. **GDDR6替代HBM的路线存疑**——在超大模型训练场景，HBM带宽是刚需，成本优势可能以性能为代价
  3. **生态劣势**——NVIDIA 的CUDA生态是20年积累，RISC-V AI加速器的软件栈成熟度远不及
  4. **商业化验证不足**——Galaxy Blackhole 的实际客户与部署规模未公开
  5. 高估值引发投资者谨慎（高通股价盘后跌1%）；整合与团队留任风险

## 动态更新记录

### 2026-09-13（骨架词条升级）
> 来源: [[消化笔记/2026-09-13-骨架公司补全批次]]
> L0归档: `L0-原始资料池/03-新闻/2026-09-13-Tenstorrent-融资与收购调研.md` (input_20260913_031)
> 置信度: 中（未上市；收购谈判未获双方确认）

- **词条升级**：从骨架升级为完整词条，补齐 YAML 字段 + 6 个 Body 段
- **market_cap**：空 → 收购报价 $80-100亿（2026.6）；2025.11 融资投前 $32亿
- **latest_revenue**：空 → 未公开（未上市公司）
- **suppliers/customers/partners/competitors**：空数组 → 分别填充 3/3/5/5 条
- **新增关键信息**：Jim Keller 领导、反NVIDIA路线（GDDR6+SRAM+以太网）、高通$80-100亿收购洽谈
- **segments 扩充**：新增 `AI芯片设计(Fabless)`
- **口径标注**：已明确"$80-100亿是收购价而非融资估值"
