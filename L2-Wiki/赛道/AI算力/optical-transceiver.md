---
name: 800G/1.6T光模块
slug: optical-transceiver
industry: AI算力
layer: L2
tam_bn: 26.0
cagr_pct: 50.0
margin: 35-50%
cost_share_pct: 8
cost_share_context: AI训练集群网络成本(GPU间互联)
profit_pool_pct: 5
profit_pool_context: 光模块双寡头(中际+新易盛)利润率高，但上游DSP/EML芯片拿走半数利润
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: 中际旭创
    share: 28-30%
    note: 300308全球#1，1.6T 50-70%垄断，FY2025营收382亿(+60%)净利108亿(+109%)，NVIDIA光引擎独家+微软1.6T独家
  - name: 新易盛
    share: 15-18%
    note: 300502全球#2，LPO独占75%份额，AWS占比60-65%，毛利率47-51%行业最高，FY2025净利94-99亿(+231-249%)
  - name: Coherent
    share: 12-15%
    note: COHR美国#1，200G EML芯片自研+InP/GaAs垂直整合,NVIDIA CPO数十亿$订单
  china:
  - name: 中国其他：光迅科技
    share: '-'
    note: 002281光模块+光芯片IDM
  - name: 华工正源
    share: '-'
    note: 000988
  - name: 剑桥科技
    share: '-'
    note: '603083'
  - name: 天孚通信
    share: '-'
    note: 300394光引擎器件Tier1
  - name: 索尔思(东山精密)
    share: '-'
    note: 国内唯一量产200G EML良率85-90%
  barriers:
  - item: 200G EML激光器芯片短缺20-30%
    detail: ''
  - item: 大客户认证周期18-24月，NVIDIA/微软/Google/Amazon四家决定格局
    detail: ''
  - item: 800G→1.6T迭代需重新认证，锁定先发优势
    detail: ''
  tech_gap:
  - dimension: 中国光模块全球份额>60%，中际+新易盛双寡头不可撼动。但上游DSP(Broadcom)和EML芯片(Lumentum/Coherent)仍被美国卡脖子，索尔思是国内唯一突破
    detail: ''
key_trends:
- title: 800G→1.6T迭代2026年爆发
  detail: 1.6T出货0→5-20M只，中际旭创独揽50-70%，ASP $900-1100是800G的2.2-2.8倍
- title: 新易盛LPO独占全球75%
  detail: AWS 60-65%份额靠LPO独家供应，毛利率47-51%行业最高，净利增速231-249%
- title: CPO 2026 Q4 NVIDIA量产
  detail: 光引擎与交换芯片共封装，功耗降30-50%，Coherent获数十亿$订单。德勤确认CPO/LPO 2026年广泛应用，缩短电气路径降低30-50%功耗，长期可能颠覆传统光模块格局
- title: 200G EML芯片成新卡脖子环节
  detail: 全球缺口20-30%，Lumentum/Coherent订单排至2028，索尔思(东山精密)国内唯一突破良率85-90%
- title: AI集群GPU:光模块比例从1:2升至1:6
  detail: 十万卡集群需要60万只光模块，光互联成本超过GPU成本的15%
price_conduction:
- 800G→1.6T迭代加速，1.6T ASP $900-1100是800G的2.2-2.8倍
- AI集群从万卡→十万卡，光模块数量超线性增长(GPU:光模块从1:2升至1:6)
- 光模块占集群网络成本50%+。200G EML芯片缺口20-30%+Coherent/Lumentum订单排至2028
- 芯片涨价传导至光模块ASP
- 中际/新易盛凭规模优势获得优先供货。CPO 2026 Q4 NVIDIA量产可能改变规则——光模块从独立器件变为封装内组件
wikilinks:
- GPU
- DSP与光芯片
- AI训练集群/超算
key_customers:
- GPU
companies:
- ticker: COHR
  name: Coherent
  role: 龙头
  rev: 35
- ticker: '300308'
  name: 中际旭创
  role: 龙头
  rev: 80
- ticker: '300502'
  name: 新易盛
  role: 二线弹性
  rev: 85
- ticker: '300394'
  name: 天孚通信
  role: 二线弹性
  rev: 30
- ticker: 002281
  name: 光迅科技
  role: 二线弹性
  rev: 40
- ticker: 000988
  name: 华工正源
  role: 二线弹性
  rev: 15
- ticker: SP
  name: Source Photonics
  role: 二线弹性
  rev: 10
- ticker: '603083'
  name: 剑桥科技
  role: 概念股
  rev: 10
key_inputs:
- DSP与光芯片
sources:
- title: LightCounting Optical Transceiver Market Q1 2026 Update
  summary: ''
  url: https://www.lightcounting.com
- title: Cignal AI 800G/1.6T Shipment Q3 2025
  summary: ''
  url: https://cignal.ai
- title: TrendForce Google Ironwood TPU Optical Demand Feb 2026
  summary: ''
  url: ''
- title: Goldman Sachs Optical Module Forecast Mar 2026
  summary: ''
  url: ''
- title: 中际旭创FY2025年报
  summary: ''
  url: ''
- title: 新易盛FY2025年报
  summary: ''
  url: ''
- title: AWS光模块供应商份额Apr 2026
  summary: ''
  url: ''
- title: OFWeek 1.6T光模块供应链分析Jun 2026
  summary: ''
  url: ''
---

# 800G/1.6T光模块

> **AI算力** · L2 · TAM **$26B** · CAGR **50%**

光模块将电信号转光信号在光纤中传输，是AI集群GPU间通信的**「数据高速公路」**——集群规模越大，光模块数量和速率需求指数增长。|**800G→1.6T迭代加速**：800G 2025出货~24M只→2026预计63M只，1.6T从0到5-20M只。AI光模块市场$16.5B(2025)→$26B(2026)。|**中国厂商全球主导**：中际旭创(全球28-30%份额,1.6T 50-70%垄断)和新易盛(全球15-18%,LPO独占75%)双寡头格局。核心瓶颈是200G EML激光器芯片——全球缺口20-30%，Lumentum/Coherent订单排至2028。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $26B |
| 年复合增长率(CAGR) | 50% |
| 利润率区间 | 35-50% |
| 成本占比 | 8% (AI训练集群网络成本(GPU间互联)) |
| 利润池占比 | 5% (光模块双寡头(中际+新易盛)利润率高，但上游DSP/EML芯片拿走半数利润) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22
> 来源: 消化笔记/2026-07-22-v1.1-德勤全球半导体趋势
> 置信度: 高

- **key_trends**: CPO/LPO趋势补充——德勤确认2026年广泛应用，降低30-50%功耗
- **sources**: +1 德勤2026全球半导体行业趋势报告
- **依据**: 德勤报告确认CPO/LPO缩短电气路径降低30-50%功耗，AI网络架构支出CAGR 38%
