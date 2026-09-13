---
name: FPGA
slug: fpga
industry: AI算力
layer: L3
tam_bn: 9.0
cagr_pct: 12.0
margin: 60-70%
cost_share_pct: 3
cost_share_context: AI推理总成本（半导体口径：2% 半导体总市场）
profit_pool_pct: 5
profit_pool_context: AI推理利润池（半导体口径：1%，FPGA利润高度集中于AMD(Xilinx)/Intel(Altera)双寡头）
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: AMD(Xilinx)
    share: ~50%
    note: 美国，#1 Versal自适应SoC（Versal AI Edge整合AI引擎+FPGA），7nm/16nm先进制程，$490亿收购Xilinx
  - name: Intel(Altera)
    share: ~28%
    note: 美国，#2，Agilex系列7nm，独立运营后IPO计划
  - name: Lattice
    share: ~10%
    note: 美国，#3低功耗FPGA边缘AI领导者(LSCC)
  china:
  - name: 复旦微电
    share: '-'
    note: 688385 亿门级FPGA量产国内#1，28nm量产，14nm研发中
  - name: 安路科技
    share: '-'
    note: 688107 工业/通信FPGA国内#2，低功耗FPGA
  - name: 紫光国微
    share: '-'
    note: 002049 特种FPGA+智能安全芯片；紫光同创通信FPGA（国产FPGA#3）
  barriers:
  - item: 架构专利
    detail: Xilinx/Altera 30年+积累；可编程逻辑架构设计（LUT/CLB/DSP/Block RAM阵列）极复杂
  - item: 配套EDA
    detail: Vivado/Quartus；FPGA EDA比ASIC EDA更难
  - item: 28nm以下制程出口管制
    detail: 7nm FPGA需要TSMC先进制程，受制裁限制
  tech_gap:
  - dimension: 中国FPGA国产化率5%→15%。28nm量产但与国际7nm仍有代差
    detail: ''
  - dimension: 中国FPGA差距5-8年，复旦微电28nm量产但在<16nm先进制程FPGA完全空白
    detail: ''
key_trends:
- title: FPGA在AI推理低延迟场景有独特优势
  detail: 金融量化交易(纳秒级)、网络包处理、信号情报；在微软Azure/AWS规模化部署，超低延迟推理(微秒级)不可替代
- title: 自适应SoC(Xilinx Versal)融合FPGA+AI引擎
  detail: AMD Versal Premium在5G基站和网络加速领域快速增长；Versal AI Edge整合AI引擎+FPGA，是异构计算AI芯片的新方向
- title: 中国FPGA国产化率从5%向15%
  detail: 复旦微电(688385)亿门级FPGA量产，28nm→14nm爬坡，安路科技(688107)在工业/通信领域追赶
- title: RISC-V+FPGA融合成新方向
  detail: 开源指令集+可编程逻辑的组合降低芯片设计门槛，让更多创业公司进入
price_conduction:
- FPGA在特定场景（金融/网络/国防）推理性价比优于GPU（微秒级延迟）。但FPGA市场小（全球~$9B），AMD(Xilinx)和Intel(Altera)双寡头CR2>80%主导定价，走差异化路线
- 竞争有限
- 利润稳定但增长空间有限。中国FPGA国产化率提升可能带来价格下行压力
- 先进制程FPGA单片$10K+(Versal/Agilex)，年涨3-5%
wikilinks:
- GPU
companies:
- ticker: '688385'
  name: 复旦微电
  role: 概念股
  rev: 25
- ticker: INTC
  name: Intel
  role: 龙头
  rev: 5
- ticker: AMD
  name: AMD
  role: 龙头
  rev: 15
- ticker: LSCC
  name: Lattice Semiconductor
  role: 二线弹性
  rev: 95
- ticker: '688107'
  name: 安路科技
  role: 国产替代
  rev: 55
key_inputs:
- EDA与IP核
- 晶圆代工(先进制程)
key_customers:
- AI服务器
- 网络交换芯片
- 边缘AI
- 自动驾驶
- AI芯片设计(Fabless)
- CPU(服务器级)
- RISC-V AI芯片
sources:
- title: AMD/Xilinx FY2025 Earnings
  summary: ''
  url: ''
- title: Intel/Altera FY2025
  summary: ''
  url: ''
- title: 复旦微电2025年报
  summary: ''
  url: ''
- title: Lattice Semiconductor FY2025
  summary: ''
  url: ''
- title: 集微半导体《全球FPGA市场2025》
  summary: AMD+Intel占72%, 前4占88%+, 全球$125亿, 国内332亿人民币
  url: https://jiweipreview.laoyaoba.com/html/share/news/960531
- title: 安路科技/复旦微电2025年报分析
  summary: 国产FPGA研发占比77%, 但<500K逻辑单元vs Xilinx 18,507K差距仍大
  url: https://www.laoyaoba.com/html/share/news/960587
---

# FPGA

> **AI算力** · L3 · TAM **$9B** · CAGR **12%**

FPGA是制造后可通过软件**重新配置逻辑电路**的芯片，介于ASIC和CPU/GPU之间。核心优势：硬件级可编程+微秒级超低延迟——金融交易/网络包处理/信号情报/AI推理不可替代。|**AMD(Xilinx)#1、Intel(Altera)#2主导全球FPGA市场**，CR2>80%。AI推理FPGA在微软Azure/AWS有规模化部署。**中国复旦微电(688385)+安路科技(688107)+紫光同创**快速追赶，国产化率从<5%→15%+。FPGA全称 Field-Programmable Gate Array；按份额 AMD(Xilinx)~55%、Intel(Altera)~28%，Lattice(~8%)在低功耗FPGA领先；复旦微电28nm已量产，RISC-V+FPGA组合进一步降低硬件设计门槛。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $9B |
| 年复合增长率(CAGR) | 12% |
| 利润率区间 | 60-70% |
| 成本占比 | 3% (AI推理总成本)〔半导体口径：2% 半导体总市场〕 |
| 利润池占比 | 5% (AI推理利润池)〔半导体口径：1% FPGA利润高度集中于AMD(Xilinx)/Intel(Altera)双寡头〕 |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→8条

### 更新 2026-09-13（合并 semi-fpga 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-fpga.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$9B）；本方 cagr 12% / margin 60-70% / value_add high 保留（对方 margin 55-70%）
- **口径保留**: cost_share / profit_pool 的半导体口径（2% 半导体总市场 / 1% FPGA利润高度集中于双寡头）并入 context 备注明细，两个视角并存
- **key_trends**: 4 → 4 条。对方4条与本方同主题，未新增；将对方更具体的数字/事实吸收进对应条目（微软Azure/AWS规模化部署与微秒级不可替代、Versal AI Edge、28nm→14nm爬坡、更多创业公司进入）
- **price_conduction**: 3 → 4 条。将对方"AI推理FPGA比GPU经济（微秒级延迟）、双寡头CR2>80%、市场规模$9B"吸收进本方第1条；对方独有主题"先进制程FPGA单片$10K+(Versal/Agilex)、年涨3-5%"新增为第4条
- **sources**: 4 → 6 条。并入 集微半导体《全球FPGA市场2025》（AMD+Intel占72%、前4占88%+、全球$125亿）、安路科技/复旦微电2025年报分析（国产FPGA研发占比77%、<500K逻辑单元 vs Xilinx 18,507K）
- **companies**: 4 → 5 家。并入 安路科技(688107,55)；共有公司 AMD/INTC/LSCC/复旦微电 沿用本方 rev（对方分别为 30/20/60/35）
- **wikilinks**: 1 → 1 条（对方同样仅 GPU，无新增）；**key_inputs**: 2 → 2 条；**key_customers**: 4 → 7 条（并入 AI芯片设计(Fabless)、CPU(服务器级)、RISC-V AI芯片）
- **competition**: global 2 → 3 条。将 Intel(Altera) 从 AMD 条目 note 中拆出为独立条目（share ~28%，Agilex 7nm、独立运营后IPO计划）；AMD 补入 share ~50%、Versal AI Edge、7nm/16nm；Lattice 补入 share ~10% 与 LSCC；china 3 → 3 条（复旦微电补 28nm量产/14nm研发中，安路补 低功耗FPGA，紫光国微并入紫光同创通信FPGA）
- **barriers**: 3 → 3 条（将对方"可编程逻辑架构设计"并入架构专利条目、"FPGA EDA比ASIC EDA更难"并入配套EDA条目、"7nm需TSMC先进制程"并入出口管制条目）；**tech_gap**: 1 → 2 条（并入 中国FPGA差距5-8年、<16nm完全空白）
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
