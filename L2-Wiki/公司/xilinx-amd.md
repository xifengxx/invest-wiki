---
name: Xilinx(AMD)
slug: xilinx-amd
country: US
ticker: AMD
type: company
updated: 2026-10
data_freshness_date: 2026-10-09
segments:
- FPGA
one_liner: |
  全球最大 FPGA 厂商、FPGA 的发明者，1984 年创立于圣何塞，2022 年 2 月被 AMD 以约 490 亿美元全股票收购，现为 AMD 的嵌入式分部（Adaptive and Embedded Computing Group）；凭 Versal 自适应 SoC 与 Alveo 加速卡守住 FPGA 赛道近半份额，位于产业链L2核心组件层。
  【2026.10.9更新】2026 Q2 AMD Embedded 分部营收 $9.77 亿（+19% YoY）、经营利润 $3.86 亿（率 40%）；FY2025 该分部 $35 亿（−3%），是 AMD 五大分部中唯一同比下滑者。
chain_layer: L2
chain_role: 龙头
suppliers:
- company: TSMC
  ticker: TSM
  supplies: 晶圆代工
  note: Versal 初代 N7、Premium/Prime Gen2 N6、UltraScale+ 16nm；中文来源称其 >70% 先进产能用于 Versal/Alveo（低置信）
- company: 封测 / 封装基板 / 内存 / IP 供应商
  note: ⚠️ 未找到——AMD 不披露产品线级供应链
customers:
- company: Microsoft Azure
  ticker: MSFT
  note: NP 系列 VM 基于 Alveo U250；该 VM 将于 2027-05-31 退役，预留实例销售已于 2026-04-02 终止；微软自述采用 5 代 FPGA 板卡、覆盖 60+ 区域，且为多供应商（含 Altera）
- company: 百度云
  note: 采用 UltraScale+（2017 年起）
- company: 腾讯云
  note: 采用 XCKU115 与 Virtex UltraScale+
- company: 终端市场
  note: 航空航天与国防、测试与测量、通信/网络、工业、汽车、医疗影像、数据中心；⚠️ AWS 与阿里云在本次来源中列的是 Intel Stratix，未见 Alveo 直接证据
partners:
- company: Mercury / Frontgrade / Alpha Data / iWave
  area: 板卡与模块生态
  note: 分别基于 Versal AI Core VC1902、RPMG1-SVPX 3U SpaceVPX、ADM-XA210/VA601/VB630、iG-G77M SoM
- company: AMD 内部组织
  area: 业务归属
  note: AECG 由原 Xilinx CEO Victor Peng 任总裁，其退休后由 Salil Raje 领导
competitors:
- company: Intel / Altera
  ticker: INTC
  area: FPGA
  note: 2025-04-14 宣布 Silver Lake 以 $87.5 亿收购 51%、2025-09 完成，成为全球最大独立纯 FPGA 公司（Intel 留 49% 被动股权）；FY2024 营收 $15.4 亿、GAAP 经营亏损 $6.15 亿；可自选代工（TSMC + Intel Foundry）
- company: Lattice Semiconductor
  ticker: LSCC
  area: 低功耗 FPGA / 边缘 AI
  note: FY2025 营收约 $5.23 亿
- company: Microchip Technology
  ticker: MCHP
  area: FPGA（军工航天耐辐照）
- company: Achronix Semiconductor
  area: 高速 data-plane / eFPGA IP
  note: 估值约 $1.8 亿
- company: 复旦微电
  ticker: 688385.SH
  area: FPGA（中国）
  note: 2025 年营收 30.24 亿元、净利 3.12 亿元
- company: 紫光同创
  ticker: 002049.SZ
  area: FPGA（中国）
  note: 紫光国微旗下，2025 年完成 IPO 辅导备案
- company: 安路科技
  ticker: 688107.SH
  area: FPGA（中国）
  note: 2025 年营收 5.2 亿元、未盈利、毛利率 43%
core_business:
- FPGA（发明者，全系列产品线）
- 自适应 SoC / ACAP——Versal AI Core / AI Edge / Premium / Prime；Zynq、Spartan、Virtex / Kintex UltraScale+
- 数据中心加速卡——Alveo V80 / U55C / U50 / U50LV / U250 / U25 SmartNIC / U45N / UL3422
- 嵌入式模块——Kria SoM、Ryzen AI Embedded X100
- 软件栈——Vivado + Vitis AI（2026.1 起对 Alveo 客户改用新许可模式）
revenue_model: 无晶圆厂芯片设计（Fabless）+ 芯片销售 + 配套软件开发工具。业务呈多年期设计中标（design win）驱动的长周期模式，而非季度订单驱动——2025 年设计中标 170 亿美元创纪录（+近 20%），2026 年在途 超 180 亿美元，自 2022 年被 AMD 收购累计 超 500 亿美元。先进制程 FPGA 单片约 1 万美元级（Versal / Agilex，年涨 3~5%）。FY2025 该分部营收 $35 亿、同比 −3%，是 AMD 五大分部中唯一下滑者；2026 Q2 回升至 $9.77 亿（+19%），经营利润率 40%。⚠️ AMD 不按分部披露 Embedded 毛利率。
founded: 1984
headquarters: 美国加州圣何塞
employees: Xilinx 被收购前 4,890 人（2021-04）；第三方追踪站点列约 1,603 人（2026-09，低置信）；AMD 整体约 26,000 人
latest_revenue: AMD Embedded 分部 2026 Q2 $9.77 亿（YoY +19%）、经营利润 $3.86 亿（率 40%），占 AMD 总营收 $115.36 亿的约 8%
market_cap: 不适用（已并入 AMD，原 NASDAQ 代码 XLNX 于 2022-02-14 摘牌；交易价值约 490 亿美元）
description: Xilinx 1984 年创立于美国加州圣何塞，发明 FPGA，是全球第一家 Fabless 半导体公司。2020-10 宣布、2022-02-14 完成被 AMD 以约 490 亿美元全股票收购（1 股换 1.7234 股 AMD），创当时半导体史最大并购，随后成为 AMD 的 Adaptive and Embedded Computing Group，即 AMD 财报中的 Embedded 分部。该分部 FY2025 营收 35 亿美元（−3%），占 AMD 总收入约 10%，是其唯一同比下滑的分部；2026 Q2 回升至 9.77 亿美元（+19%）。产品覆盖 Versal 自适应 SoC、Alveo 数据中心加速卡与 Kria 嵌入式模块，全球 FPGA 份额约半数为第一。
website: https://www.xilinx.com
industries:
- 半导体
- AI算力
---

# Xilinx(AMD)

**FPGA 的发明者，如今是 AMD 的一个分部**。它的处境有一层特殊含义：FPGA 既没被 GPU 挤出 AI 服务器，天花板也很明确——它是 AMD 五大分部中**唯一在 FY2025 同比下滑**的那一个，但 2026 年已回升。

## 财务状况（AMD Embedded 分部）

| 期间 | 营收 | 同比 | 经营利润 |
|------|:--:|:--:|:--:|
| FY2025 全年 | **$35 亿** | **−3%** | — |
| 2026 Q1 | $8.73 亿 | +6% | $3.38 亿（39%） |
| **2026 Q2** | **$9.77 亿** | **+19%** | **$3.86 亿（40%）** |

FY2025 该分部占 AMD 总收入 $346 亿的约 **10%**，是其**唯一同比下滑**的分部；2026 Q2 占 $115.36 亿的约 8%。
> ⚠️ AMD 不按分部披露 Embedded 毛利率；FY2026 Q3 数据截至归档日未发布。

**2025 年季度路径**：Q1 $8.23 亿 / Q2 $8.23~8.24 亿 / Q3 $8.57 亿 / Q4 $9.50 亿。

## 业务模式：设计中标驱动的长周期

| 指标 | 数值 |
|------|:--:|
| 2025 年设计中标 | **$170 亿（创纪录，+近 20%）** |
| 2026 年在途 | **>$180 亿** |
| 自收购累计 | **>$500 亿** |

FPGA 的收入由多年前的设计中标逐步转化，而非当季订单——这是它与 GPU/ASIC 业务最不同的财务特征。先进制程 FPGA 单片约 **1 万美元级**（Versal / Agilex，年涨 3~5%）。

## 产品线详解

- **FPGA**：发明者，全系列
- **自适应 SoC / ACAP**：Versal AI Core / AI Edge / Premium / Prime；Zynq、Spartan、Virtex / Kintex UltraScale+
- **数据中心加速卡**：Alveo V80 / U55C / U50 / U50LV / U250 / U25 SmartNIC / U45N / UL3422
- **嵌入式模块**：Kria SoM、Ryzen AI Embedded X100
- **软件栈**：Vivado + Vitis AI

## 竞争格局（本词条最重要的变化）

> **Intel/Altera 已于 2025 年 9 月独立**——Silver Lake 以 **$87.5 亿收购 51%** 股权（2025-04-14 宣布），成为**全球最大独立纯 FPGA 公司**，Intel 保留 49% 被动股权。它可自选代工（TSMC + Intel Foundry），FY2024 营收 $15.4 亿、GAAP 经营亏损 $6.15 亿。

| 厂商 | H1 2026 份额 |
|------|:--:|
| **AMD（Xilinx）** | **49.0%** |
| Intel / Altera | 31.1% |
| Lattice | 9.9% |
| 复旦微电 | 8.5% |
| 安路科技 | 1.6% |

> ⚠️ **份额口径分歧**：2025 全年口径为 AMD 约 58% / Altera 约 25%；H1 2026 口径如上表（大东时代智库）。历史 2021 年：Xilinx 51% / Altera 29% / Lattice 7% / Microchip 6%。**FPGA 市场 2025 年规模有 $114.1 亿 / $117.3 亿 / $125.8 亿 / $138 亿四个口径**，中国国产化率有 15% / 29% / 35% 三个口径——均未裁定，两存。

**中国厂商**：复旦微电（688385.SH，2025 年营收 30.24 亿元、净利 3.12 亿元）、紫光同创（紫光国微 002049.SZ 旗下，2025 年完成 IPO 辅导备案）、安路科技（688107.SH，2025 年营收 5.2 亿元、未盈利、毛利率 43%）。

## 融资与现金流

- **被收购交易**：2020-10 宣布、**2022-02-14 完成**，AMD 以约 **490 亿美元**全股票收购（1 股换 1.7234 股 AMD），创当时半导体史最大并购；原 NASDAQ 代码 **XLNX 同日摘牌**
- **股权**：已并入 AMD，不独立上市，无独立市值与现金流披露
- ⚠️ 本次调研未获取到该分部的资本开支与自由现金流数据

## 研发投入与专利

⚠️ **本项在本次调研中未获取到可靠数据**。按 L1「不推测原则」留空。

## FPGA 赛道的两个关键行业事实

**① FPGA 未被 GPU/ASIC 挤出，但天花板明确**：GPU 仍占 AI 服务器 70%+、ASIC 2026 年约 27%；FPGA 切入碎片化低延迟推理与网络卸载，2026 年 AI 服务器 FPGA 需求预计 >350 万颗、渗透率 27%。反方观点（nextpcb）认为 FPGA 到 2027 年仍「停留在细分市场」。

**② 2026 年 FPGA 供应链是卖方市场**：进口 FPGA 交期升至**约 52 周**（正常 8~12 周），AMD/Xilinx 报价 40~50+ 周，部分军工/工业料号 300~364 天；证券时报报道头部厂自 **2026 年 3 月起提价 10~20%+**。
> ⚠️ **一条来源严重污染已弃用**：中文涨价报道把 Stratix V / Arria II / Agilex / Stratix 10（**Intel/Altera 产品**）列为 Xilinx 提价型号，内部矛盾，故「Xilinx 具体涨价幅度与型号」判定为低置信不予采信，仅保留方向性事实。另有「NVIDIA GTC 2026 Groq3 LPX 机架每 tray 1 颗 FPGA」仅见于中文行业媒体，未获官方证实。

## 动态更新记录

- 2026-10-09：**骨架升级为完整词条**（原为 23 行骨架，`suppliers`/`customers`/`partners`/`competitors` 全空）。来源 L0 归档 `input_20261009_151`（26 组搜索词）。
  **本词条的焦点是 FPGA 业务**（即 AMD 的 Embedded 分部），而非 AMD 整体；`ticker` 取 AMD（原 XLNX 已于 2022-02-14 摘牌）。
  **已知数据缺口**：① 该业务的封测/封装基板/内存/IP 供应商名单（AMD 不披露产品线级供应链）；② Embedded 分部的客户集中度与产品线级收入拆分；③ Xilinx 被收购前最后一个完整独立财年的官方营收（`$36.76 亿`经查为 LTM 而非 FY2022 全年，无确证值）；④ 该分部毛利率；⑤ 2026 Q3 实际数据（未发布）。
  **口径提示**：全文共记录 **12 项口径分歧**（份额 58%/25% vs 49%/31%、FPGA 市场 2025 年规模四个口径、中国国产化率三个口径、收购金额 $490 亿/$500 亿/$600 亿等），未做裁定、两存。整体置信度**中**（官方财务为高，市场份额与规模类为第三方且分歧大）。
