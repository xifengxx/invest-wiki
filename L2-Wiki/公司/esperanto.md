---
name: Esperanto
slug: esperanto
country: US
ticker: ''
type: company
updated: 2026-10
data_freshness_date: 2026-10-09
segments:
- RISC-V AI芯片
one_liner: |
  已实质停业的 RISC-V AI 推理芯片公司，2023 年量产出货千核 ET-SoC-1，2025-07 裁员约 90% 并关闭欧洲子公司，IP 于 2025-10 被 Ainekko 收购后开源，位于产业链L3核心产品与集成层——曾以成品 AI 推理加速器形式存在，现退化为开源 IP 供给。
  【2026.10.9更新】首轮 L0 归档（input_20261009_162）确认公司已 defunct：峰值约 140 人，未拿下任何具名商业客户是其失败主因（132 GB/s 带宽与不支持 FP8/FP4 使其无法承接 Transformer/LLM 负载）；ET-SoC-1 架构已由 Ainekko 以 Apache 2.0 开源并转向边缘 AI。
chain_layer: L3
chain_role: 已停业（IP 被 Ainekko 收购并开源）
suppliers:
- company: TSMC
  supplies: 7nm 晶圆代工
  note: ET-SoC-1 采用 TSMC 7nm，裸片面积 570 mm²
- company: Arteris
  supplies: SoC 集成软件（CSRCompiler）
  note: 2024-06 选用，用于下一代能效方案；PCIe 控制器等第三方授权 IP 未随开源一并释放
- company: NetSpeed
  supplies: AI SoC 互连
  note: 2018 年合作方（后并入 Cadence），属早期合作
- company: LPDDR4x DRAM 供应商
  supplies: 片外内存
  note: 每卡配 32 GB LPDDR4x；供应商未具名
customers:
- company: 具名商业客户
  note: 未找到——归档明确记载无任何具名超大规模/云客户端，多源指出未能拿下重量级客户是商业失败主因
- company: Penguin Solutions
  ticker: SGH
  area: 系统集成
  note: 2023-05 战略合作，ET-SoC-1 卡即双方合作形态；性质为系统厂/价值增值伙伴而非终端采购方
- company: GWDG（德国哥廷根大学计算中心）
  area: 科研托管
  note: 托管 4 个计算节点、每节点 8 张 ET-SoC-1 卡，供研究者评估边缘 AI 与能效小语言模型
partners:
- company: Penguin Solutions
  ticker: SGH
  area: AI/HPC 数据中心与边缘加速系统
  note: 2023-05 建立战略合作，联合开发
- company: Rapidus
  area: 先进制程与后 GPU 时代 AI 推理
  note: 2024-05-15 签署合作备忘录（MoC），聚焦 2nm 高能效 AI 推理/HPC；2025-07 日媒报道公司陷入财务困难后，合作实际难以为继
- company: E4 Computer Engineering / MEGWARE / Elematec
  area: 渠道分销
  note: 分别为意大利、德国、日本的价值增值伙伴，覆盖美/欧/日市场
- company: Ainekko
  area: IP 收购与开源承接
  note: 2025-10 收购其全部 IP 与部分资产（2025-11-19 正式公告），2025-11 将 ET-SoC-1 以 Apache 2.0 开源；2026-01-29 Ainekko 与 MRAM 初创 Veevx 合并
competitors:
- company: Tenstorrent
  area: RISC-V AI 芯片
  note: Jim Keller 任 CEO，RISC-V 通用核加自研张量单元，覆盖训练与推理
- company: SiFive
  area: RISC-V 处理器 IP
  note: 做处理器 IP 而非成品芯片；2026-04 完成 $400M Series G
- company: Ventana Micro Systems
  area: RISC-V IP 与芯粒
  note: RISC-V IP 与 chiplet，与 Imagination 合作
- company: NVIDIA
  area: AI 加速器
  note: 数据主权性能与带宽标杆；H100 内存带宽约 3 TB/s，为 ET-SoC-1 约 132 GB/s 的 25 倍，是其无法支撑大模型的直接对照
- company: Cerebras
  area: AI 加速器
  note: 同为 AI 加速器初创阵营
- company: Graphcore
  area: AI 加速器
  note: 同为 AI 加速器初创阵营
core_business:
- ET-SoC-1 千核 RISC-V AI 推理加速器——1,088 个 ET-Minion 64 位顺序执行核（每核带向量与张量单元）加 4 个 ET-Maxion 64 位乱序核（跑 Linux 与管理）加 1 个服务处理器，合计约 1,093 核
- 硬件形态——低矮型 PCIe Gen 4 卡（PCIe 4.0 x8），配 2U 评估服务器，单服务器最高 16,000+ RISC-V CPU、20 服务器机架约 320,000 核
- 软件栈——ML SDK（支持 PyTorch、ONNX、Glow）、2023-05 发布的 General Purpose SDK（C/C++ 直接编程全部 1,000+ 核）、Primo AI/ML 与生成式 AI 软件栈（ONNX Runtime 编译、Torch Dynamo 导出、AWQ 量化、LoRA / Flash Attention 微调，宣称首个支持 Ollama 的 RISC-V 硬件）
- 现状——作为独立公司已停业，技术资产经 Ainekko 以 Apache 2.0 开源（GitHub 仓库 et-platform、et-man），转向机器人/无人机、工业自动化、安防、嵌入式 IoT、媒体处理与定制 SoC 等边缘场景
revenue_model: 停业前以 AI 推理加速卡与配套系统（PCIe 卡、2U 评估服务器）的硬件销售为主，叠加软件栈与 Primo 平台；未上市且无任何公开营收、毛利或盈亏数据。归档明确记载公司未找到任何具名商业客户，也无在线商店与公开定价（官网只提供评估申请表），营销与社区参与薄弱被视为失败原因之一。2025-07 关闭大部分运营后，仅留 CEO Art Swift 与少数工程师处理 IP 出售与授权。
founded: 2014
headquarters: 美国加州 Mountain View（800 W El Camino Real 或 67 E Evelyn Ave，两源不一致；无任何来源支持 Los Gatos）；另有巴塞罗那与塞尔维亚工程站点，均已于 2025-07 随欧洲子公司关闭
employees: 峰值约 140 人（EE Times 2025 口径；第三方档案区间 50~250 不等）。2025-07 Mountain View 总部裁员约 90%、关闭西班牙与塞尔维亚子公司，95% 前员工已找到新工作；部分来源显示 2026-08 员工约 23 人，属遗留/清算性质
market_cap: 未上市，无公开市值。未找到任何 post-money 估值——Dealroom 页面出现的 $232M~348M 未与轮次绑定，归档判定不可采信。累计融资口径不一（$58M / $63M / $65.1M / $124M），主口径为 Series B 后的 $63M
description: Esperanto Technologies 成立于 2014 年（法律实体登记 2014-09-17），由前 Transmeta 创始人 Dave Ditzel 创办、Art Swift 任 CEO，总部位于加州 Mountain View，是 RISC-V Foundation 创始 Gold 会员。核心产品是 ET-SoC-1 千核 RISC-V AI 推理加速器——1,088 个 ET-Minion 核加 4 个 ET-Maxion 核，TSMC 7nm、160 MB 片上 SRAM、32 GB LPDDR4x、PCIe 4.0 x8、约 40 W、峰值 100~200 TOPS，2021 采样、2023 量产。技术上有亮点，但商业上失败：未拿下任何具名商业客户，132 GB/s 带宽与不支持 FP8/FP4 使其无法承接从 CNN 转向 Transformer/LLM 的负载，团队又被大厂以 2~4 倍薪酬挖空。2025-07 关停大部分运营（裁员约 90%、关闭欧洲子公司），2025-10 IP 被 Ainekko 收购，2025-11 以 Apache 2.0 开源并转向边缘 AI。公司作为独立主体已实质停业（defunct）。
website: https://www.esperanto.ai
industries:
- AI算力
- 半导体
---

# Esperanto

⚠️ **先看结论：这家公司已经死了。** Esperanto 是 RISC-V AI 芯片商业化的全球早期标杆之一，也是**唯一已量产出货**的那一档玩家，但它没能把技术转化为订单——2025-07 关停大部分运营，IP 被 Ainekko 收购后开源，业务重心从数据中心退到边缘 AI。本词条的价值不在估值，而在**一份完整的失败样本**：技术指标不差，却因带宽、精度格式与生态三处硬伤出局。

## 财务状况

⚠️ **未上市，无任何公开财务数据**。归档在营收、毛利、盈亏三项上均为「未找到」。

| 项 | 值 | 来源 |
|----|-----|------|
| Series A | 2017-11，金额未披露（Dealroom 记 Early VC $5.0M；Tracxn 记 $1.2M，数据存疑） | Dealroom / CB Insights |
| Series B | 2018-11，$58M | VentureBeat |
| PPP 贷款 | 2020-04，$1.5M（Paycheck Protection Program） | CB Insights |
| 累计总融资 | $63M（Series B 后口径，多源一致）；另有 $58M / $65.1M / $124M 等口径 | 各统计平台 |
| 估值 | 未找到 | — |
| 营收 / 毛利 / 盈亏 | 未找到 | — |

**投资方**（多源拼合，非单一来源确认）：Comet Labs、Western Digital Capital、Almaz Capital、R136 Ventures、Decent Capital、Paycheck Protection Program。投资方数量 Crunchbase/Tracxn 记 7 家，CB Insights 记 4~5 家。

**现金流事件**：唯一的外部资金注入除股权融资外，只有 2020 年 4 月的 $1.5M PPP 贷款。归档未找到公司获得 DARPA / DOE / 军方项目的任何证据。

## 产品线详解

### ET-SoC-1 千核 RISC-V 推理芯片

| 项目 | 值 |
|------|-----|
| 制程/代工 | TSMC 7nm；裸片面积 570 mm² |
| 核心总数 | 1,088 个 ET-Minion 64 位顺序执行核（每核带向量与张量单元）+ 4 个 ET-Maxion 64 位乱序核（跑 Linux/管理）+ 1 个服务处理器，合计约 1,093 |
| 片上 SRAM | 160 MB（部分源记 140 MB） |
| 片外内存 | 32 GB LPDDR4x（分布在卡上） |
| 内存带宽 | 约 132 GB/s（对照 NVIDIA H100 约 3 TB/s，低约 25 倍——无法支撑大模型的短板） |
| 互联 | 2D mesh Network-on-Chip（NoC） |
| 主机接口 | PCIe 4.0 x8 |
| 形态 | 低矮型 PCIe Gen 4 卡（与 Penguin Solutions 合作）；配套 2U 评估服务器，双 Xeon 主机 + 8 或 16 张卡（单服务器最高 16,000+ RISC-V CPU；20 服务器机架约 320,000 核） |
| 算力 | 峰值 100~200 TOPS |
| 功耗 | 单卡约 40 W（无需外接 PCIe 供电）；ML 推荐负载 <20 W；Meta OPT LLM 推理低至 25 W |
| 支持数据格式 | FP32 / FP16 / INT8（不支持 FP8 / FP4） |
| 关键节点 | 2021 采样；2023 量产 |

### 软件栈

| 项目 | 值 |
|------|-----|
| ML SDK | RISC-V 神经网络编译器，支持 PyTorch、ONNX、Glow |
| General Purpose SDK | 2023-05 发布，用标准 C/C++ 直接编程全部 1,000+ RISC-V 核及其向量/张量单元，扩展到通用 HPC 与混合 HPC+AI |
| Primo 平台 | Primo AI/ML 模型开发 SDK + Primo Generative AI Software Stack，含模型优化、微调、编排 |
| 编译/推理 | ONNX Runtime 编译；Jupyter + Torch Dynamo 导出；AWQ 量化；LoRA / Flash Attention 微调 |
| LLM 框架 | 宣称首个支持 Ollama 的 RISC-V 硬件，模型发布到 HuggingFace |
| 支持模型 | LLaMA 2、Vicuna、StarCoder、OpenJourney、Stable Diffusion、Meta OPT；Generative AI Appliance 2U 机架可同时跑最多 4 个 LLM |
| MLIR | 未找到任何关于 MLIR 支持的来源 |
| 开源现状 | 2025-10 后被 Ainekko 以 Apache License v2 开源 RTL/参考设计/工具/文档（排除 PCIe 控制器等第三方授权 IP）；GitHub 仓库 et-platform、et-man 已发布 |

## 技术路线图

- **已验证的路线**：千核众核 + 超低功耗（40 W 单卡、ML 负载 <20 W）+ 大容量片上 SRAM（160 MB），走「能效优先」而非「绝对性能优先」
- **路线中断点**：市场从 CNN 推荐系统转向 Transformer/LLM，132 GB/s 带宽与不支持 FP8/FP4 成为硬伤；能效卖点在「电力预算无上限」的数据中心项目中不被重视
- **开源后的演进（由 Ainekko 承接，不再属 Esperanto）**：2025-11 Apache 2.0 开源并转向边缘计算（机器人/无人机、工业自动化、安防、嵌入式 IoT、媒体处理、学术研发、定制 SoC）；2026-01-29 Ainekko 与 MRAM 存储初创 Veevx 合并；2026-02 参加 FOSDEM'26，定位为「可组合构建块的开源平台」而非芯片公司，计划 2026 Q2 在 TSMC 16nm shuttle 流片首颗芯片（8 个 Esperanto Minion 核 + Veevx MRAM）

## 融资与现金流

见「财务状况」表。补充事项：

- **2021 年**：ET-SoC-1 采样，进入技术验证期
- **2023 年**：量产；同年 5 月发布 General Purpose SDK、与 Penguin Solutions 建立战略合作
- **2024 年**：1 月发布 RISC-V Generative AI Appliance（2U，评估用）；5 月与 Rapidus 签 MoC；6 月选用 Arteris CSRCompiler
- **2025-07**：**关闭大部分运营**——Mountain View 总部裁员约 90%，关闭西班牙与塞尔维亚欧洲子公司；仅留 CEO Art Swift 与少数工程师处理 IP 出售/授权
- **2025-10**：**Ainekko 收购其全部 IP 与部分资产**（芯片设计、软件工具、开发框架），2025-11-19 正式公告
- ⚠️ 归档未找到公司在任何时间点的自由现金流、负债或股东回报数据

**失败根因（多源归纳）**：① 人才被大厂以 2~4 倍薪酬挖空（CEO Art Swift 观点，称「基本上摧毁了我们的团队」）；② 未拿下重量级超大规模客户，市场从 CNN 推荐系统转向 Transformer/LLM，其 132 GB/s 带宽与不支持 FP8/FP4 成为硬伤；③ 能效卖点在「电力预算无上限」的数据中心项目中不被重视（Art Swift 观点）；④ 营销与社区运营薄弱（部分媒体观点，指官网只提供评估申请表，无在线商店与定价）。

## 研发投入与专利

⚠️ **本项在本次调研中未获取到可靠数据**：归档未披露研发费用率、研发投入金额与专利数量。可确认的只有 IP 资产流向——2025-10 全部 IP 与部分资产被 Ainekko 收购，2025-11 以 Apache License v2 开源 RTL/参考设计/工具/文档（排除 PCIe 控制器等第三方授权 IP）。按 L1「不推测原则」留空，不以推测填空。

## 竞争格局

| 阵营 | 公司 | 说明 |
|------|------|------|
| RISC-V 芯片设计 | Tenstorrent | Jim Keller 任 CEO；RISC-V 通用核 + 自研张量单元；Wormhole/Blackhole（含 16 个 RV64 应用核）；Ascalon CPU；Galaxy 6U 服务器（32 加速器互联）；训练+推理 |
| RISC-V IP | SiFive | RISC-V 界的 Arm，做处理器 IP 而非成品芯片；2026-04 完成 $400M Series G |
| RISC-V IP/芯粒 | Ventana Micro Systems | RISC-V IP 与 chiplet；与 Imagination 合作 |
| GPU 阵营 | NVIDIA | 数据主权性能与带宽标杆；H100 带宽约 3 TB/s |
| ASIC/AI 加速器 | Cerebras、Graphcore 等 | 同为 AI 加速器初创阵营 |

**定位差异**：Esperanto 是当时**少数已量产出货**的 RISC-V AI 芯片公司（竞争对手多为 IP/芯粒阶段），但选择低功耗边缘推理而非与 NVIDIA 拼绝对性能，最终因带宽与生态局限未能规模化。

## 产业链定位

- 在「RISC-V AI 芯片」赛道中，Esperanto 处于**成品 AI 推理加速器**环节（SoC + PCIe 卡 + 服务器系统 + 软件栈），是 RISC-V 高性能计算商业化的全球早期标杆之一
- **上游依赖**：TSMC 7nm 代工；LPDDR4x DRAM；PCIe 控制器等第三方授权 IP（Arteris、NetSpeed）；自研 ET-Minion/ET-Maxion 核
- **下游**：数据中心/边缘 AI 推理与 HPC 加速；系统集成商（Penguin Solutions、MEGWARE、E4、Elematec）
- **现状**：公司停业后，其架构被 Ainekko 开源并转向边缘 AI/机器人/IoT，**产业链位置由「商用加速器供应商」退化为「开源 IP 供给」**（经 Ainekko/AI Foundry + OpenHW Foundation 治理）

## 动态更新记录

- 2026-10-09：**骨架升级为完整词条**（原为 11 字段、0 章节的骨架页，`chain_role` 原记「核心参与者」）。来源 L0 归档 `input_20261009_162`（`L0-原始资料池/03-新闻/2026-10-09-Esperanto-调研.md`，confidence 中）。
  **状态变更（核心）**：`chain_role` 由「核心参与者」改为 **`已停业（IP 被 Ainekko 收购并开源）`**——归档结论为「Esperanto Technologies 作为独立公司已实质停业（defunct），业务不再正常运营」。`chain_layer` 由 L4「终端应用与服务」改为 **L3「核心产品与集成」**（成品 AI 推理加速器环节）。
  **必须与产品规格同写的一条**：归档明确记载公司**未找到任何具名商业客户**——无任何具名超大规模/云客户，多源明确指出未能拿下重量级客户是商业失败主因。技术指标（1,088 核、160 MB SRAM、约 40 W、100~200 TOPS）成立，但商业侧为零，两者不可分开引用。
  **已知数据缺口**：① 总融资额的唯一权威值（$58M / $63M / $65.1M / $124M 冲突）；② 公司估值与 post-money valuation（无来源）；③ 营收 / 毛利 / 盈亏数据（未上市，无披露）；④ 具名商业客户（无）；⑤ 与 DOI / DARPA / DOE / 军方的项目关系（无，仅 2020 年 PPP $1.5M 贷款）；⑥ CEO Art Swift 在 2026 年的去向未找到；⑦ Esperanto 实体最终法律状态（是否正式注销）未找到，部分档案仍记 active；⑧ 研发费用与专利数量未找到。
  **总部口径核实**：归档专门核实过「总部 Los Gatos」的说法，未发现任何来源支持，多源一致指向 **Mountain View**；Los Altos 为 Ditzel / Stephen Lee 个人住址所在地，疑被误记。本词条以 Mountain View 为准。
  **时效提醒**：公司已停业，财务字段无刷新必要；若 Ainekko 的开源平台后续产生可引用数据，应记入 Ainekko 词条而非本条目。
