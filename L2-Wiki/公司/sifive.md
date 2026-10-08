---
name: SiFive
slug: sifive
country: 美国
ticker: ''
type: company
updated: 2026-10
data_freshness_date: 2026-10-09
segments:
- RISC-V AI芯片
one_liner: |
  全球商用 RISC-V 处理器 IP 龙头，以 IP 授权费加芯片出货版税的 Arm 式模式盈利，2026-04 完成 4 亿美元 G 轮、投后估值 36.5 亿美元，位于产业链L2设备与组件层——RISC-V 核心 IP 的主要供给方，对标 Arm。
  【2026.10.9更新】首轮 L0 归档（input_20261009_163）显示：G 轮由 Atreides Management 领投、NVIDIA 参投，累计融资逾 7.6 亿美元，公司称 G 轮为 IPO 前最后一轮私募；营收仅存第三方估算且区间冲突严重（$38.2M~$109.2M），不可直接使用。
chain_layer: L2
chain_role: 龙头
suppliers:
- company: TSMC / Samsung Foundry
  supplies: 晶圆代工
  note: SiFive 为 fabless IP 授权方、不自建产能；客户将 IP 集成进 SoC 后自行委托代工（口径来自 Sacra / FIRST CVC）
- company: Microsoft Azure
  supplies: 云基础设施托管
  note: Core Designer / Chip Designer / DesignShare 云授权与设计服务托管于 Azure
customers:
- company: Intel
  note: Intel Foundry 7nm Horse Creek 采用 P550 核心，Intel 亦为投资方（Intel Capital 参与 C/E/F 轮）
- company: Qualcomm
  note: Series D 领投方（Qualcomm Ventures），有来源称 Snapdragon 中采用 RISC-V，未获一手确认
- company: Google / Alphabet
  note: 定制蓝图用于内部设计，有来源称用于 TPU；此为 Sacra / FIRST CVC 口径
- company: Amazon
  note: 被列为采用其核心 IP 的巨头之一
- company: Microchip Technology
  note: 具名客户之一
- company: Renesas
  note: 2021-04 车规 RISC-V 战略合作，授权其核心 IP
- company: Samsung
  note: 代工合作，覆盖 SoC / 汽车 / 5G；Samsung Ventures 为投资方
- company: Western Digital / SK Telecom
  note: 早期采用方，同时为投资方
- company: NASA HPSC
  note: 高性能航天计算项目采用
- company: Tenstorrent Blackhole
  note: 据称采用其 IP，未见一手确认
partners:
- company: NVIDIA
  area: 互连技术
  note: 2026-01 集成 NVIDIA NVLink Fusion，为首家与英伟达在互连技术上合作的 RISC-V 芯片公司；NVIDIA 亦参与 2026-04 G 轮
- company: AMD / Xilinx
  area: 战略投资与生态
  note: 参与 2022-03 F 轮投资
competitors:
- company: Arm
  area: 处理器 IP
  note: 直接对标；Arm 自研 AGI CPU（客户含 Meta、OpenAI）与 Flexible Access 计划双向挤压 SiFive
- company: 晶心科技 Andes
  area: RISC-V 处理器 IP
  note: 台湾厂商，支持 RVA23，2024 年全球 RISC-V CPU 份额约 12%（单一分析口径）
- company: 芯来科技 Nuclei
  area: RISC-V 处理器 IP
  note: 中国厂商，2018-09 成立，全球授权客户 300+，车规/AI 领先；2024 年份额 10%+，2024 营收 7794.7 万元、剔除股份支付后净利 -761.74 万元、毛利率 90%+
- company: Tenstorrent
  area: RISC-V AI 芯片
  note: Jim Keller 任 CEO，RISC-V 通用核加自研张量单元，做成品芯片而非纯 IP
- company: Codasip
  area: RISC-V 处理器 IP
  note: 欧洲厂商，份额 <5%
- company: Synopsys
  area: EDA 与 IP
  note: 在 IP 核环节存在竞争
- company: MIPS / CAST / 苏州国芯
  area: 处理器 IP
  note: 同环节竞争者
- company: Rivos
  area: 自研 RISC-V CPU
  note: 创始团队含 Google / Intel / Apple 工程师，超大规模厂商自研 CPU 团队压缩外购 IP 空间
core_business:
- RISC-V 处理器核心 IP 授权——Essential 系列（32 位 E 系列、64 位 S/T/U 系列，出货以十亿计）、Intelligence 系列（边缘 ML/AI，含 X100/X200/X300 向量核与 XM 矩阵引擎）、Performance 系列（P550/P570 Gen 3、数据中心级 P870-D）、Automotive 系列（车规）
- 定制 SoC 设计服务——约占 2023 年收入 30%
- 开发板与工具——约占 2023 年收入 10%
- 云端授权与设计服务——Core Designer、Chip Designer、DesignShare
revenue_model: fabless IP 授权模式，结构类似 Arm——前期收取 IP 授权费（license），再按客户芯片出货量抽取版税（royalty）；客户自行把核心集成进 SoC 后交 TSMC 或 Samsung 代工，SiFive 不承担制造与库存。2023 年第三方口径的收入结构约为 IP 授权 60%、定制 SoC 设计服务 30%、开发板与工具 10%。未上市，无官方营收披露；第三方数据库的估算区间冲突严重（2023 约 $38.2M，2026 约 $89.4M~$109.2M），不可直接引用。
founded: 2015
headquarters: 美国加州 Santa Clara（地址 2625 Augustine Drive）；口径冲突——Dealroom/MarketScreener 记 San Mateo，Multiples 记 San Francisco，另有来源记 San Jose
employees: 第三方估算约 480~516 人（PitchBook 502、Tracxn 516、fiisual 约 504、RocketReach 480/516、Growjo 502 且同比降约 7%）；官网称 85% 为工程师、180 名博士
latest_revenue: 无官方披露（未上市）。第三方估算区间冲突严重、不可直接使用——2023 约 $38.2M（Sacra）；2026 约 $89.4M（Growjo）/ $109.2M（RocketReach）；累计融资口径亦有 $766M / $795M / $970M 三说
market_cap: 未上市，无公开市值。最近一轮投后估值 $3.65B（2026-04-09 G 轮）；2022-03 F 轮投后超 $2.5B（投前 $2.33B）；Dealroom 记区间 $2.5B~5B
description: SiFive 成立于 2015 年，由 RISC-V 指令集原始设计者 Krste Asanović、Yunsup Lee、Andrew Waterman 在加州 Santa Clara 创办，是全球商用 RISC-V 处理器 IP 龙头，被官方新闻稿称为 RISC-V IP 的 gold standard。商业模式与 Arm 类似——前期收 IP 授权费、按客户出货量抽版税，客户自行集成 SoC 后委托 TSMC 或 Samsung 代工。产品分 Essential（嵌入式 MCU 与实时核）、Intelligence（边缘 ML/AI，含向量与矩阵引擎）、Performance（全系支持 RVA23，数据中心级 P870-D 最高 256 核）、Automotive（车规）四系列；2026-01 成为首家接入 NVIDIA NVLink Fusion 的 RISC-V 芯片公司。2026-04-09 完成 4 亿美元 G 轮（Atreides Management 领投、NVIDIA 参投），投后估值 36.5 亿美元，累计融资逾 7.6 亿美元。营收无官方披露，仅有第三方估算且区间冲突严重。
website: https://www.sifive.com
industries:
- AI算力
- 半导体
---

# SiFive

全球商用 RISC-V 处理器 IP 龙头。**它的投资逻辑不在当期利润，而在 RISC-V 生态从边缘向数据中心渗透的斜率**——所以本词条的重心是融资与估值轨迹、产品线代际，以及超大规模厂商自研 CPU 对外购 IP 空间的挤压。

## 财务状况

⚠️ **SiFive 未上市，无公开财报**。营收、净利、毛利率、现金流均无官方披露，仅有第三方数据库估算，且**口径冲突严重、不可直接使用**：

| 口径 | 数值 | 来源 | 置信度 |
|------|------|------|:--:|
| 2023 营收 | 约 $38.2M | Sacra | 中 |
| 2026 营收估算 | $89.4M | Growjo | 低（估算） |
| 2026 营收估算 | $109.2M | RocketReach | 低（估算） |
| 累计融资 | $766M | Tracxn / Multiples | 中 |
| 累计融资 | $795M | fiisual | 中 |
| 累计融资 | $970M | tech-insider | 低 |

**收入结构（2023，第三方口径）**：约 60% IP 授权 / 30% 定制 SoC 设计服务 / 10% 开发板与工具。

**净利润、毛利率、现金流**：**未找到**任何来源。

**经营性指标**（软性，但可交叉）：

- 设计中标（design wins）：2019 年 100+（前十大半导体客户占 6 家）→ 2026 年口径 400+（marketsandmarkets）/ 500+（部分来源）；IP 已用于超 500 种设计
- 累计出货：覆盖超 20 亿台设备（早期口径）→ 超 100 亿颗核心（2026 口径）
- 2023-10 曾裁员约 20%（约 140 人，原约 650 人）

## 产品线详解

| 系列 | 定位 | 关键内容 |
|------|------|---------|
| **Essential** | 低功耗嵌入式 MCU / 实时核 | E 系列（32 位，最高 8 级流水、双发射）、S 系列（64 位）、T 系列（多核、WorldGuard、MMU/SV32）、U 系列（64 位，支持 Linux）；出货以十亿计 |
| **Intelligence** | 边缘 ML/AI，软件优先 | 标量加宽向量计算引擎；SiFive Intelligence Extensions（XSfVector、XSfvqmaccdod、XSfvqmaccqoq 量化 MAC 指令，单指令完成 4×4 int8 外积 16 MAC）；XSfVcp 协处理器接口（客户可挂自家 AI 加速器）。子系列 X100（128-bit 向量）、X200（512-bit）、X300（1024-bit，VCIX 2048-bit）、XM 矩阵引擎（4 个 X300 每簇，1 簇 = 16 TOPS INT8） |
| **Performance** | 高性能乱序标量核，全系支持 RVA23 | P550 / P570 已到 Gen 3（2026-05 发布，P570 Gen 3 集成 128-bit 向量引擎）；数据中心级 P870-D 已在客户芯片中，支持最高 256 核服务器 CPU；第四代 Performance IP 在开发中 |
| **Automotive** | 车规 | 面向汽车可靠性场景 |

**互联与生态**：2026-01 集成 NVIDIA NVLink Fusion，成为首家与英伟达在互连技术上合作的 RISC-V 芯片公司。2026-07 WAIC 上围绕 AI / 机器人 / 物理 AI 展示产品体系，P570 Gen 3 可让轻量 AI 任务直接在 CPU 上跑而无需独立 NPU。

## 技术路线图

- **RVA23 全系覆盖**：Performance 系列全系支持 RVA23，直接对标 Arm Cortex-A 系列
- **向量宽度阶梯**：Intelligence 的 X100（128-bit）→ X200（512-bit）→ X300（1024-bit、VCIX 2048-bit）→ XM 矩阵引擎（每簇 16 TOPS INT8）
- **数据中心路径**：P870-D 支持最高 256 核服务器 CPU，已在客户芯片中；第四代 Performance IP 在开发中
- **互连**：NVLink Fusion 接入（2026-01），为 RISC-V 阵营首例
- **云端设计**：Core Designer / Chip Designer / DesignShare（托管于 Microsoft Azure）

## 融资与现金流

| 时间 | 轮次 | 金额 | 估值 | 主要投资方 |
|------|------|------|------|-----------|
| 2015-09 | Series A | $5.06M | — | Sutter Hill Ventures |
| 2017-05 | Series B | $8.5M | — | Spark Capital、Osage University Partners、Sutter Hill |
| 2018-04/05 | Series C | $50.6M | — | Osage、Spark、Sutter Hill、Intel Capital、Samsung Ventures、SK Telecom、Chengwei、Huami、Western Digital、Berkeley SkyDeck |
| 2019-06 | Series D | $65.4M | — | Qualcomm Ventures 领投；Sutter Hill、Chengwei、Spark、Osage、Huami |
| 2020-08 | Series E | $61M | — | SK hynix 领投；Qualcomm Ventures、Intel Capital、Prosperity7、Osage、Spark、Sutter Hill、Western Digital |
| 2022-03 | Series F | $175M | 投后超 $2.5B（投前 $2.33B） | Coatue 领投；Intel Capital、Qualcomm Ventures、Samsung Ventures、AMD/Xilinx、SK hynix、Prosperity7、Aramco Ventures 等 |
| **2026-04-09** | **Series G** | **$400M**（超额认购） | **投后 $3.65B** | **Atreides Management 领投**；**NVIDIA**、Apollo Global、D1 Capital、Point72 Turion、T. Rowe Price、Prosperity7、Capital Group、Sutter Hill |

- **累计融资**：约 $760M~$795M（Tracxn/Multiples $766M；fiisual $795M；tech-insider $970M——口径冲突）
- **估值轨迹**：2022-03 超 $2.5B → 2026-04 $3.65B；**2024、2025 年无新融资轮**，故这两年无新估值
- **收购事件**：2021 年 Intel 曾出价超 $2B 收购 SiFive，因估值分歧告吹（雷峰网、EEWorld、Sacra）
- **IPO**：官方口径称 Series G 为 IPO 前最后一轮私募、无时间表。第三方分析师的预测（2026 Q4 或 2027 Q1、NASDAQ、估值超 $5B）为**非官方**信息，归档中未找到交易所、承销商等任何已确认细节
- ⚠️ 本次调研未获取到负债水平、自由现金流与股东回报数据

## 研发投入与专利

⚠️ **本项在本次调研中未获取到可靠数据**：归档未披露研发费用率、研发投入金额与专利数量，仅有官网口径的「85% 为工程师、180 名博士」这类人员结构表述。按 L1「不推测原则」留空，不以推测填空。

## 竞争格局

**市场地位**：2024 年全球 RISC-V CPU 份额约 15.3%（单一分析口径，低置信），为 RISC-V IP 环节名义第一。

| 公司 | 国别/地区 | 2024 全球 RISC-V CPU 份额（单一分析口径） | 备注 |
|------|----------|:--:|------|
| **SiFive** | 美国 | 约 15.3% | 生态发起者之一，P550/P650 被视为挑战 Arm Cortex-A |
| Andes 晶心科技 | 台湾 | 约 12% | 支持 RVA23 |
| 芯来科技 Nuclei | 中国 | 10%+ | 2018-09 成立，全球授权客户 300+，车规/AI 领先 |
| 赛昉科技 StarFive | 中国 | 约 8% | 平头哥生态合作方，全栈方案 |
| 平头哥玄铁 | 中国 | 未单列份额 | C910/C906 累计出货超 40 亿颗 |
| Cortus、Codasip | 欧洲 | 各 <5% | — |

**赛道规模**：2024 年全球 RISC-V 多核处理器 IP 内核市场（QYResearch），2025 年约 13.49 亿元人民币，预计 2032 年 18.9 亿元，CAGR 约 5.0%。

**市场结构风险**：① 超大规模厂商自研 CPU 团队（如 Rivos，创始团队含 Google/Intel/Apple 工程师）压缩外购 IP 空间；② Arm 自研芯片（AGI CPU，客户含 Meta、OpenAI）与 Flexible Access 计划双向挤压；③ 收入规模与 $3.65B 估值之间的匹配度存疑（第三方营收估算区间过大）。

## 客户与生态

**具名客户与合作方**：Intel（Intel Foundry 7nm Horse Creek 用 P550，亦为投资方）、Qualcomm（投资方）、Google/Alphabet（定制蓝图，有来源称用于 TPU；与芯原合作 Coral NPU IP 系芯原信息）、Amazon、Microchip Technology、Renesas（2021-04 车规战略合作）、Samsung（代工合作）。其他采用方含 Western Digital、SK Telecom、NASA HPSC、Tenstorrent Blackhole（据称）。

**中国 RISC-V 生态**：三大生态联盟为 ① 中科院主导的 CRVA 联盟（倪光南牵头，20+ 高校院所 + 阿里/百度/中芯国际）；② 芯原主导的 CRVIC 联盟（300+ 会员，商业化 IP 广场）；③ 平头哥主导的无剑联盟（60+ 签约伙伴）。2026 年车规趋势中，芯来、国芯、阿里玄铁、晶心、SiFive、高通被列为可复用芯片内核供应商；RISC-V 汽车渗透率预计从 2025-2026 约 10% 升至 2031 年 31%。

> ⚠️ 芯原股份收购芯来科技事件存在口径冲突：2025-08-28 签意向、2025-09-12 披露预案（收购 97.01% 股权），**2025-12-12 公告终止**；但 dramx.com（2026-05-21）称 2026 年 3 月完成收购，与多数来源矛盾。以官方公告为准。

## 动态更新记录

- 2026-10-09：**骨架升级为完整词条**（原为 11 字段、0 章节的骨架页，`chain_layer` 原记 L4「终端应用与服务」）。来源 L0 归档 `input_20261009_163`（`L0-原始资料池/03-新闻/2026-10-09-SiFive-调研.md`，confidence 中）。
  **调研纠正**：`chain_layer` 由 **L4 改为 L2**——归档明确定位「处于半导体产业链最上游的 EDA 与 IP 核环节」，与同环节的 Arm（L2）、Synopsys（L2）一致；`chain_role` 由「核心参与者」改为「龙头」（RISC-V IP 环节名义第一，与赛道文件 `riscv-ai.md` 的 role 登记一致）。
  **已知数据缺口**：① **官方营收 / ARR / 净利润 / 毛利率 / 现金流**全部未找到，仅有第三方估算且区间 $38M~$109M 冲突严重；② IPO 具体时间、交易所、承销商未找到（仅有分析师预测，非官方）；③ 2024、2025 年无新融资轮故无新估值；④ 中国区营收占比与中国客户名单未找到；⑤ 2026 年被收购传闻、裁员与领导层变动均未找到（CEO 仍为 Patrick Little）；⑥ 研发费用与专利数量未找到。
  **口径冲突**：① 总部四说并存（Santa Clara / San Mateo / San Francisco / San Jose），以 Santa Clara 为主口径；② 累计融资三说（$766M / $795M / $970M）；③ 设计中标数 400+ 与 500+ 两说；④ 2024 年全球 RISC-V CPU 份额 15.3% 系单一分析口径，置信度低；⑤ 芯原收购芯来科技的完成与否存在来源矛盾，以官方公告为准。
  **时效提醒**：若公司启动 IPO 或再度融资，需重新刷新 `data_freshness_date`；G 轮已于 2026-04-09 完成，本词条估值数据时点即该轮。
