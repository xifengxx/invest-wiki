---
name: AI芯片设计(Fabless)
slug: semi-ai-chip-design
industry: 半导体
layer: L4
tam_bn: 25.0
cagr_pct: 35.0
margin: 50-65%
cost_share_pct: 40
cost_share_context: AI芯片总成本（制造成本占60%，设计+软件栈占40%）
profit_pool_pct: 20
profit_pool_context: AI芯片设计利润池（NVIDIA垄断，毛利率72.7%，净利率50%+）
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L4
competition:
  global:
  - name: NVIDIA
    share: 86%
    note: 美国，#1 AI训练+推理GPU，CUDA生态锁定90%+开发者，FY2026 DC $193.7B，毛利率72.7%，1年迭代节奏
  - name: AMD
    share: 8%
    note: 美国，#2，MI300X/MI400追赶，ROCm生态，OpenAI 6GW+Meta 6GW大单, Broadcom/Google TPU
  china:
  - name: 寒武纪
    share: '-'
    note: 688256 思元MLU云端推理，受制裁限制制程
  - name: 海思(华为)
    share: '-'
    note: 昇腾910B国产替代首选，政府/运营商AI训练
  - name: 地平线
    share: '-'
    note: 征程自动驾驶AI芯片（J6 560 TOPS）
  barriers:
  - item: AI架构设计(Tensor Core/NPU/CUDA)
    detail: NVIDIA 20年+架构迭代积累
  - item: CUDA/ROCm软件生态
    detail: 17年CUDA积累，ROCm差距仍大
  - item: 先进制程+CoWoS+HBM三要素获取
    detail: 受美国制裁，中国AI芯片三要素全部受限
  tech_gap:
  - dimension: 中国AI芯片架构差距3-5年，但制造(先进制程)+封装(CoWoS)+存储(HBM)+IP/EDA四重锁死，实际可用水平差距7-10年
    detail: ''
key_trends:
- title: AI芯片从GPU→ASIC→定制化多路线并行
  detail: 训练GPU为主+推理ASIC崛起+FPGA在特定场景
- title: NVIDIA 1年迭代节奏→竞争壁垒持续提高
  detail: Blackwell→Rubin→Vera加速
- title: 中国AI芯片受限于先进制程
  detail: 只能做推理/边缘/特定场景，训练GPU差距仍在扩大
- title: Groq LPU+Cerebras Wafer Scale是差异化架构
  detail: LPU超高吞吐+Cerebras单晶圆级芯片是GPU之外有趣尝试
price_conduction:
- NVIDIA毛利率72.7%
- AI芯片设计利润极高
- 但先进制程流片成本$500M+(3nm)
- 只有大公司能持续迭代
- 行业集中度极高（NVIDIA 86%）。中国AI芯片受限于先进制程
- 只能做推理/边缘场景
- GPU算力差距3-5年且仍在扩大
wikilinks:
- GPU
- FPGA
- EDA与IP核
- CPU(服务器级)
- 晶圆代工(先进制程)
- RISC-V AI芯片
- 先进封装(CoWoS/3D)
- 存储芯片(DRAM/NAND)
key_inputs:
- GPU
- FPGA
companies:
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 95
- ticker: AMD
  name: AMD
  role: 二线弹性
  rev: 25
- ticker: AVGO
  name: Broadcom
  role: 二线弹性
  rev: 20
- ticker: INTC
  name: Intel
  role: 概念股
  rev: 10
- ticker: MRVL
  name: Marvell
  role: 二线弹性
  rev: 30
- ticker: IBM
  name: IBM
  role: 概念股
  rev: 5
sources:
- title: NVIDIA FY2026 Annual Report
  summary: ''
  url: https://investor.nvidia.com
- title: AMD FY2025 Earnings
  summary: ''
  url: ''
- title: 寒武纪2025年报
  summary: ''
  url: ''
- title: Groq/Cerebras
  summary: ''
  url: ''

key_customers: ["AI服务器", "AI推理API服务", "云计算IaaS", "边缘AI"]---

# AI芯片设计(Fabless)

> **半导体** · L4 · TAM **$25B** · CAGR **35%**

AI芯片设计专攻AI加速芯片架构——不制造芯片，只设计架构+软件栈，委托TSMC代工。**从「万能GPU(NVIDIA)」→「定制ASIC(Broadcom/Marvell/Google TPU)」+「通用GPU」+「FPGA」三路线并行**。|**NVIDIA绝对垄断86%数据中心AI芯片份额**，FY2026数据中心$193.7B(+68% YoY)，GPU计算$162.4B。CUDA生态锁定90%+AI开发者。AMD MI300X/MI400追赶(8%份额)，Groq LPU+Cerebras Wafer Scale差异化架构。|**中国寒武纪(688256思元MLU)+海思(昇腾910B)+地平线(征程)+燧原+壁仞+摩尔线程**在特定AI场景追赶，但受限于先进制程(无法获取TSMC 3nm/2nm)+CoWoS封装+HBM+EDA/IP，中国AI芯片设计「有心无力」。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $25B |
| 年复合增长率(CAGR) | 35% |
| 利润率区间 | 50-65% |
| 成本占比 | 40% (AI芯片总成本（制造成本占60%，设计+软件栈占40%）) |
| 利润池占比 | 20% (AI芯片设计利润池（NVIDIA垄断，毛利率72.7%，净利率50%+）) |
| 附加值 | high |

## 关联

（待补充）
