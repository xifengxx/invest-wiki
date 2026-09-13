---
input_id: input_20260913_031
date: 2026-09-13
source_type: Web调研
source_name: "Tenstorrent 融资/估值/高通收购谈判与RISC-V路线（WebSearch 多源）"
source_url: "https://thenextweb.com/news/tenstorrent-intel-qualcomm-takeover-jim-keller-risc-v"
ingest_date: 2026-09-13
status: 已处理
tags: [Tenstorrent, RISC-V, Jim Keller, 高通收购, AI芯片, 未上市]
data_as_of: 2026-06
confidence: 中
---

# Tenstorrent 融资、估值与收购调研

> 归档说明：Tenstorrent 为**未上市公司**，无公开财报。采用「融资估值 + 收购报价」口径。**2026年的核心事件是高通收购谈判**。

## 搜索记录
搜索词「Tenstorrent 2026 funding valuation RISC-V AI chip Jim Keller」，2026-09-13。有效来源：The Information 转述 / TNW / 36氪 / EET China / DigitalToday / Gadgets Now / C114。

## 关键数据表

### 公司概况

| 项 | 内容 |
|----|------|
| 成立 | **2016年**（原加拿大多伦多，后迁册美国） |
| 创始人/CEO | **Jim Keller**——传奇芯片架构师，履历含 **Apple A系列、AMD Zen架构、Tesla 自动驾驶芯片**；约2020年加入任CTO，2023年任CEO |
| 技术路线 | **RISC-V 架构 AI 加速器**：**Tensix AI 核心** + **Ascalon RISC-V CPU 核心** |
| 商业模式 | 既卖成品芯片，也**授权 IP** |
| 旗舰 CPU | **TT-Ascalon**（含 Ascalon-X 核心），被评为**可与 Arm Neoverse V2/V3 竞争** |

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
| 时间 | **2026年6月**（The Information 于6月15-16日报道） |
| **报价** | **$80亿 ~ $100亿** |
| 溢价 | 约为 2024年底 $26亿估值的 **4倍** |
| 竞争方 | Bloomberg 早前（2026年5月）报道 **Intel 与 Qualcomm 均**与 Tenstorrent 有早期收购接触 |
| 状态 | **谈判进行中，可能变化或破裂**；两家公司均未确认 |
| 市场反应 | 高通股价盘后跌约1%（对高估值存疑） |

## 关键要点

| 要点 | 内容 |
|------|------|
| **"反NVIDIA"路线** | 避免昂贵的 **HBM 内存**，改用 **GDDR6 + 片上 SRAM**，集群用**标准以太网**（而非 InfiniBand） |
| 成本优势 | **Galaxy Blackhole 平台**（32个加速器）定价 **$110,000**，据称为 NVIDIA DGX 的 **1/3 到 1/5 成本**，效率高数倍 |
| 高通动机 | ①从手机芯片多元化到数据中心/云AI；②获得**非Arm的CPU路线图**，降低对Arm依赖（应对进行中的诉讼） |
| 汽车协同 | 汽车 RISC-V CPU **"Alexandria"**（面向ADAS）契合高通的 Snapdragon Digital Chassis 战略 |

## 风险

1. **收购谈判未获双方确认**，可能变化或破裂
2. **高估值引发投资者谨慎**（高通股价盘后跌1%）
3. 报道提示整合、团队留任、商业化风险，**可能采用 earn-out/里程碑付款结构**
4. **无2026年新融资轮估值**——当前讨论的$80-100亿是收购价而非融资估值
5. 以 GDDR6 替代 HBM 的路线，在超大模型训练场景的适用性存疑

## Schema-Mapping

| 原文内容 | 映射到 L2 公司 | 映射字段 | 冲突 |
|---------|---------------|---------|:--:|
| "高通洽谈$80-100亿收购" | Tenstorrent | market_cap | 否 |
| "2024.12 Series D $26亿、2025.11 $32亿投前" | Tenstorrent | 融资与现金流 | 否 |
| "Jim Keller 任CEO、Apple/AMD/Tesla履历" | Tenstorrent | description | 否 |
| "Tensix AI核心 + Ascalon RISC-V CPU" | Tenstorrent | core_business | 否 |
| "Galaxy Blackhole $110,000，1/3-1/5 NVIDIA成本" | Tenstorrent | 产品线详解 | 否 |
| "避免HBM，用GDDR6+片上SRAM+以太网" | Tenstorrent | 技术路线图 | 否 |
| "三星/LG/现代/起亚投资" | Tenstorrent | partners | 否 |

## QA 自检
| # | 检查项 | 结果 |
|---|--------|------|
| 1 | 来源 | 1 次搜索，7+ 来源 ✓ |
| 2 | 覆盖 | 公司概况/融资历史/收购事件/技术路线/风险 5 项 ✓ |
| 3 | 表格 | 3 张表全提取 |
| 4 | 数字 | 15+ 个 |
| 5 | 实体 | Tenstorrent、Jim Keller、高通、Intel、Arm、三星、LG、现代、起亚 ✓ |
| 6 | 判断句 | 收购动机/技术路线 ✓ |
| 7 | **口径标注** | 已明确"$80-100亿是收购价而非融资估值" ✓ |

自检结论：✅ 通过（置信度中等，收购未确认）
