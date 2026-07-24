---
name: FPGA
slug: semi-fpga
industry: 半导体
layer: L3
tam_bn: 9.0
cagr_pct: 12.0
margin: 55-70%
cost_share_pct: 2
cost_share_context: 半导体总市场
profit_pool_pct: 1
profit_pool_context: FPGA利润高度集中于AMD(Xilinx)/Intel(Altera)双寡头
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: AMD(Xilinx)
    share: ~55%
    note: 美国，#1全球FPGA，Versal AI Edge整合AI引擎+FPGA，7nm/16nm先进制程
  - name: Intel(Altera)
    share: ~28%
    note: 美国，#2，Agilex系列7nm，独立运营后IPO计划, Lattice Semiconductor
  china:
  - name: 复旦微电
    share: '-'
    note: 688385 国产FPGA#1，28nm量产，14nm研发中
  - name: 安路科技
    share: '-'
    note: 688107 国产FPGA#2，低功耗FPGA
  - name: 紫光同创
    share: '-'
    note: 国产FPGA#3，通信FPGA
  barriers:
  - item: 可编程逻辑架构设计
    detail: LUT/CLB/DSP/Block RAM阵列设计极复杂
  - item: 先进制程代工获取
    detail: 7nm FPGA需要TSMC先进制程（受制裁限制）
  - item: EDA软件生态(Vivado/Quartus)
    detail: FPGA EDA比ASIC EDA更难
  tech_gap:
  - dimension: 中国FPGA差距5-8年，复旦微电28nm量产但在<16nm先进制程FPGA完全空白
    detail: ''
key_trends:
- title: AI推理FPGA在微软Azure/AWS规模化部署
  detail: FPGA在超低延迟推理场景(微秒级)不可替代
- title: AMD Versal AI Edge整合AI引擎+FPGA
  detail: 异构计算AI芯片的新方向
- title: 中国FPGA国产化率<10%→快速增长
  detail: 复旦微电28nm→14nm爬坡
- title: RISC-V+FPGA组合降低设计门槛
  detail: 开源硬件+可编程逻辑让更多创业公司进入
price_conduction:
- 先进制程FPGA单片$10K+(Versal/Agilex)
- AI推理FPGA在特定场景比GPU经济（微秒级延迟）
- 差异化路线。双寡头CR2>80%
- 年涨3-5%
- 但FPGA市场规模相对较小（$9B），利润绝对值有限
wikilinks:
- GPU
key_inputs:
- 晶圆代工(先进制程)
- EDA与IP核
key_customers:
- AI芯片设计(Fabless)
- CPU(服务器级)
- RISC-V AI芯片
companies:
- ticker: AMD
  name: AMD(Xilinx)
  role: 全球龙头
  rev: 30
- ticker: INTC
  name: Intel(Altera)
  role: 全球二线
  rev: 20
- ticker: LSCC
  name: Lattice Semi
  role: 全球二线
  rev: 60
- ticker: '688385'
  name: 复旦微电
  role: 国产替代
  rev: 35
- ticker: '688107'
  name: 安路科技
  role: 国产替代
  rev: 55
sources:
- title: 集微半导体《全球FPGA市场2025》
  summary: AMD+Intel占72%, 前4占88%+, 全球$125亿, 国内332亿人民币
  url: https://jiweipreview.laoyaoba.com/html/share/news/960531
- title: 安路科技/复旦微电2025年报分析
  summary: 国产FPGA研发占比77%, 但<500K逻辑单元vs Xilinx 18,507K差距仍大
  url: https://www.laoyaoba.com/html/share/news/960587
---

# FPGA

> **半导体** · L3 · TAM **$9B** · CAGR **12%**

FPGA（Field-Programmable Gate Array）是制造后可通过软件**重新配置其逻辑电路**的芯片——介于ASIC（固定功能）和CPU/GPU（通用计算）之间。核心优势：**硬件级可编程性+微秒级超低延迟**——金融量化交易、网络包处理、信号情报和AI推理中不可替代。|**AMD(Xilinx，#1，~55%份额，Versal AI Edge)和Intel(Altera，#2，~28%份额，Agilex)**主导CR2>80%。Lattice(~8%)在低功耗FPGA领先。全球市场$9B(2025)。|**中国复旦微电(688385)28nm FPGA量产**，安路科技(688107)和紫光同创快速追赶。国产化率从<5%→15%+。RISC-V+FPGA组合降低硬件设计门槛。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $9B |
| 年复合增长率(CAGR) | 12% |
| 利润率区间 | 55-70% |
| 成本占比 | 2% (半导体总市场) |
| 利润池占比 | 1% (FPGA利润高度集中于AMD(Xilinx)/Intel(Altera)双寡头) |
| 附加值 | high |

## 关联

（待补充）
