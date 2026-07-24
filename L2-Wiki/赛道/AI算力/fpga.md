---
name: FPGA
slug: fpga
industry: AI算力
layer: L3
tam_bn: 9.0
cagr_pct: 12.0
margin: 60-70%
cost_share_pct: 3
cost_share_context: AI推理总成本
profit_pool_pct: 5
profit_pool_context: AI推理利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: AMD Xilinx
    share: ~50%
    note: 美国，#1 Versal自适应SoC，$490亿收购, Intel Altera
  - name: Lattice
    share: ~10%
    note: 美国，#3低功耗FPGA边缘AI领导者LSCC
  china:
  - name: 复旦微电
    share: '-'
    note: 688385 亿门级FPGA量产国内#1
  - name: 安路科技
    share: '-'
    note: 688107 工业/通信FPGA国内#2
  - name: 紫光国微
    share: '-'
    note: 002049 特种FPGA+智能安全芯片
  barriers:
  - item: 架构专利
    detail: Xilinx/Altera 30年+积累
  - item: 配套EDA
    detail: Vivado/Quartus
  - item: 28nm以下制程出口管制
    detail: ''
  tech_gap:
  - dimension: 中国FPGA国产化率5%→15%。28nm量产但与国际7nm仍有代差
    detail: ''
key_trends:
- title: FPGA在AI推理低延迟场景有独特优势
  detail: 金融量化交易(纳秒级)、网络包处理、信号情报
- title: 自适应SoC(Xilinx Versal)融合FPGA+AI引擎
  detail: AMD Versal Premium在5G基站和网络加速领域快速增长
- title: 中国FPGA国产化率从5%向15%
  detail: 复旦微电(688385)亿门级FPGA量产，安路科技(688107)在工业/通信领域追赶
- title: RISC-V+FPGA融合成新方向
  detail: 开源指令集+可编程逻辑的组合降低芯片设计门槛
price_conduction:
- FPGA在特定场景（金融/网络/国防）推理性价比优于GPU。但FPGA市场小（全球~$8B），AMD(Xilinx)和Intel(Altera)双寡头定价
- 竞争有限
- 利润稳定但增长空间有限。中国FPGA国产化率提升可能带来价格下行压力
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

key_inputs: ["EDA与IP核", "晶圆代工(先进制程)"]
key_customers: ["AI服务器", "网络交换芯片", "边缘AI", "自动驾驶"]---

# FPGA

> **AI算力** · L3 · TAM **$9B** · CAGR **12%**

FPGA是制造后可通过软件**重新配置逻辑电路**的芯片，介于ASIC和CPU/GPU之间。核心优势：硬件级可编程+微秒级超低延迟——金融交易/网络包处理/信号情报/AI推理不可替代。|**AMD(Xilinx)#1、Intel(Altera)#2主导全球FPGA市场**，CR2>80%。AI推理FPGA在微软Azure/AWS有规模化部署。**中国复旦微电(688385)+安路科技(688107)+紫光同创**快速追赶，国产化率从<5%→15%+。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $9B |
| 年复合增长率(CAGR) | 12% |
| 利润率区间 | 60-70% |
| 成本占比 | 3% (AI推理总成本) |
| 利润池占比 | 5% (AI推理利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→8条
