---
name: Siemens EDA
slug: siemens-eda
country: DE
ticker: ''
type: company
updated: 2026-10
data_freshness_date: 2026-10-09
segments:
- EDA与IP核
one_liner: |
  全球第三大 EDA 厂商（份额约 13%），原 1981 年成立的美国 Mentor Graphics，2017 年被西门子以 45 亿美元收购、2021 年更名；凭 Calibre 物理验证签核（事实标准）与 Tessent DFT 立足，覆盖 IC 设计、验证、制造、PCB 与 3D IC 全流程，正以 agentic AI 重塑芯片设计，位于产业链L2核心组件层。
  【2026.10.9更新】第三方估算 2025 年 EDA 业务营收约 $22~25 亿；Calibre 已获台积电 N2/A16 与 3DFabric 认证，与 NVIDIA 合作推进自验证 agentic AI 工作流。
chain_layer: L2
chain_role: 龙头
suppliers:
- company: 自身软件与 IP 研发
  supplies: EDA 工具链
  note: EDA 为纯软件业务，无实体供应链；⚠️ 本次调研未涉及其云基础设施等间接供应商
customers:
- company: 晶圆代工厂 / IDM / Fabless 设计公司
  note: 客户结构未具名披露；⚠️ 中国区营收单独数字未找到
partners:
- company: TSMC
  ticker: TSM
  area: 制程与封装认证
  note: 合作最深——Calibre 获 N2/N3E/N3C/N2P/A16 与 3DFabric 认证；Aprisa 获 N3E 认证；另有 A14/COUPE
- company: Samsung Foundry
  ticker: 005930
  area: 先进封装与 AI
  note: HDAP/MDI 封装；Fuse AI 早期采用
- company: Intel Foundry
  ticker: INTC
  area: 代工生态
  note: 为 IFS EDA 联盟特许成员；14A/18A-P 认证
- company: UMC
  ticker: 2303.TW
  area: 成熟制程 PDK
  note: 110nm/180nm BCD PDK
- company: Arm Holdings
  ticker: ARM
  area: 硬件仿真与 SoC 方案
  note: Veloce 授权；SoC Compiler 联合方案
- company: AMD
  ticker: AMD
  area: 硬件仿真客户
- company: NVIDIA
  ticker: NVDA
  area: agentic AI 工作流
  note: 合作 EDA AI System、Fuse EDA AI Agent 与自验证 agentic AI（基于 NeMo Gym + OpenShell + Nemotron 3 Ultra + CUDA-X）
competitors:
- company: Synopsys
  ticker: SNPS
  area: EDA 全流程
  note: 全球第一（份额约 32%）；2025 年已并入 Ansys
- company: Cadence Design Systems
  ticker: CDNS
  area: EDA 全流程
  note: 全球第二（份额约 29%）
- company: Ansys
  ticker: ANSS
  area: 仿真
  note: 已并入 Synopsys（中国市场份额口径中仍单列约 5%）
- company: Keysight Technologies
  ticker: KEYS
  area: 设计与测试
- company: 华大九天（Empyrean）
  ticker: 301269.SZ
  area: EDA（中国）
  note: 中国份额约 6%，国产第一
- company: 概伦电子 / 广立微
  ticker: 688206.SH / 301095.SZ
  area: EDA（中国）
core_business:
- Calibre——IC 物理验证与制造签核，旗舰产品、行业「金标准」
- Tessent——DFT（可测性设计），市占领先
- Veloce——硬件仿真（Strato CS / Primo CS / proFPGA CS），与 Cadence 形成双寡头
- Aprisa——数字布局布线（P&R）
- Questa——功能验证
- Solido——变异感知与特征化（AI 底座）
- Xpedition / PADS / Innovator3D IC——PCB 设计，三大 EDA 厂中最完整的一条线
- Catapult——高层次综合（HLS）
- Analog FastSPICE——模拟仿真
revenue_model: 许可 + 维护订阅模式——浮动许可、1~3 年定期许可、永久许可加年维护、按量云计费、token/容量计费、企业级 ELA。同业机制参考：客户留存 >95%、年涨价 3~7%、毛利率 70~80%（西门子 EDA 不公开定价）。西门子财报不单列 EDA 分部——Siemens EDA 隶属 Siemens Digital Industries Software（DI SW），属 Siemens Xcelerator 组合；DI 分部 FY2025 营收 −4%、利润率由 18.9% 降至 14.9%，DI 软件可比营收 −5%，但软件 ARR +13%、云占 ARR 近 50%。
founded: 1981
headquarters: 美国俄勒冈州 Wilsonville
employees: 约 5,000 人 ⚠️ 口径分歧（Silicon Saxony ~5,000 / Crustdata ~4,931 / namu.wiki 6,000）；公司无官方口径
latest_revenue: 第三方估算 2025 年 EDA 业务营收约 $22~25 亿 ⚠️ 另有低口径 $15 亿，来源冲突；无官方披露
market_cap: 不适用（不独立上市）。母公司 Siemens AG（XETRA 代码 SIE）：FY2025 营收 €789 亿、净利 €104 亿（创纪录）、订单 €884 亿、自由现金流 €108 亿、约 31.8 万员工，2026 年市值约 €2,050~2,230 亿
description: Siemens EDA 原为 1981 年成立的美国 Mentor Graphics（自 Tektronix 分拆），2017 年 3 月被西门子以 45 亿美元企业价值收购、2021 年更名，现隶属西门子数字工业软件。2025 年 EDA 业务营收第三方估算约 22~25 亿美元，全球份额约 13%，居 Synopsys、Cadence 之后。Calibre 是 IC 物理验证与制造签核事实标准，与台积电最先进制程深度认证绑定；Tessent 领跑 DFT，Veloce 占硬件仿真寡头位，Xpedition 为三大厂最完整的 PCB 线。近年密集并购并推出 EDA AI System 与 Fuse EDA AI Agent，与 NVIDIA 合作自验证 agentic AI 工作流。
website: https://eda.sw.siemens.com
industries:
- 半导体
- AI算力
---

# Siemens EDA

全球第三大 EDA 厂商（份额约 13%），**Calibre 是 IC 物理验证的事实标准**——这也是它与台积电绑定最深的原因。近两年的主线是用 agentic AI 重做芯片设计流程。

## 财务状况

⚠️ **Siemens EDA 不独立上市、西门子财报也不单列 EDA 分部**，因此没有官方营收数字：

| 口径 | 数值 | 备注 |
|------|:--:|------|
| EDA 业务营收（第三方估算，2025） | 约 **$22~25 亿** | 另有低口径 $15 亿，**来源冲突** |
| 全球 EDA 份额 | **约 13%（第三）** | Synopsys 约 32%、Cadence 约 29% |

**母公司 Siemens AG（XETRA 代码 SIE）**：FY2025 营收 €789 亿、净利 €104 亿（创纪录）、订单 €884 亿、FCF €108 亿、约 31.8 万员工；2026 年市值约 €2,050~2,230 亿。
**所属分部 DI SW**：DI 分部 FY2025 营收 −4%、利润率 18.9%→14.9%，软件可比营收 −5%；但**软件 ARR +13%、云占 ARR 近 50%**。

## 产品线详解

| 产品 | 定位 |
|------|------|
| **Calibre** | IC 物理验证与制造签核——**旗舰，行业「金标准」** |
| **Tessent** | DFT（可测性设计），市占领先 |
| **Veloce** | 硬件仿真（Strato CS / Primo CS / proFPGA CS），与 Cadence 双寡头 |
| **Aprisa** | 数字布局布线（P&R） |
| **Questa** | 功能验证 |
| **Solido** | 变异感知与特征化（**AI 底座**） |
| **Xpedition / PADS / Innovator3D IC** | PCB 设计——三大 EDA 厂中**最完整**的一条线 |
| **Catapult** | 高层次综合（HLS） |
| **Analog FastSPICE** | 模拟仿真 |

## 技术路线图：agentic AI

| 时间 | 进展 |
|------|------|
| 2025-06（DAC） | **EDA AI System** |
| 2026-03（GTC） | **Fuse EDA AI Agent**（MCP 架构） |
| 2026-07（DAC） | **自验证 agentic AI 工作流**（随 NVIDIA 升级） |

宣称效果：最多缩短设计时间 **10x**；Solido 特征化提速 **>10x**、token 成本降 **5~10x**；Aprisa AI PPA **+10%**。

## 生态绑定

| 合作方 | 内容 |
|------|------|
| **TSMC**（最深） | Calibre 获 **N2/N3E/N3C/N2P/A16** 与 **3DFabric** 认证；Aprisa 获 N3E 认证；另有 A14/COUPE |
| Samsung Foundry | HDAP/MDI 封装；Fuse AI 早期采用 |
| Intel Foundry | IFS EDA 联盟**特许成员**；14A/18A-P 认证 |
| UMC | 110nm/180nm BCD PDK |
| Arm | Veloce 授权；SoC Compiler 联合方案 |
| AMD | Veloce 客户 |
| **NVIDIA** | EDA AI System、Fuse EDA AI Agent、自验证 agentic AI（NeMo Gym + OpenShell + Nemotron 3 Ultra + CUDA-X） |

## 近年并购（均未披露金额）

Insight EDA（2023-11，可靠性验证→Calibre PERC）· DownStream（2025-04，PCB 制造数据）· Excellicon（2025-05，时序约束）· ASTER（2026-01，PCB 测试 TestWay）· Precision Innovations（2026-07，OpenROAD AI 芯片规划）· Defacto（2026-07，SoC 组装自动化）

## 竞争格局

| 公司 | 全球份额 | 说明 |
|------|:--:|------|
| Synopsys (SNPS) | 约 **32%** | 第一；**2025 年已并入 Ansys** |
| Cadence (CDNS) | 约 **29%** | 第二 |
| **Siemens EDA** | **约 13%** | 第三 |
| Ansys | — | 已并入 Synopsys |
| 华大九天 (301269.SZ) | 中国约 6% | 国产第一 |
| 概伦电子 / 广立微 | — | 中国 |
| Keysight | — | 设计与测试 |

**中国市场**：Siemens EDA **17%**（Synopsys 32% / Cadence 29% / 华大九天 6% / Ansys 5%）。三巨头合计约 74%（部分口径 85%+）。
**市场总规模**：2024 年 $157.1 亿（ESD Alliance 2025 口径行业收入约 $213 亿）。

## 研发投入与专利

- **存量指标（同业口径）**：客户留存 >95%、年涨价 3~7%、毛利率 70~80%
- ⚠️ Siemens EDA 自身的研发费用率与专利数量未获取到

## 动态更新记录

- 2026-10-09：**骨架升级为完整词条**（原为 11 字段、0 章节的骨架页）。来源 L0 归档 `input_20261009_161`（含西门子官方口径与第三方 EDA 市场报告交叉）。
  **已知数据缺口**：① **现任全球 CEO 姓名未找到**——Mike Ellow 于 2024-06 至 2025-11 任 CEO，2025-11-20 转任 Synopsys CRO，公开搜索无继任者记录；② 独立营收的官方披露（西门子不单列 EDA 分部）；③ 精确员工数（第三方 4,931~6,000 不一）；④ 各产品线单独市占率；⑤ 中国区营收单独数字。
  **置信度**：中——份额/收购/产品线为高置信；营收规模为第三方估算且冲突；CEO 为未找到。
