---
name: 晶圆代工(先进制程)
slug: semi-foundry-advanced
industry: 半导体
layer: L3
tam_bn: 170.0
cagr_pct: 24.0
margin: 55-66%
cost_share_pct: 35
cost_share_context: 芯片制造成本（代工占芯片总成本35-40%）
profit_pool_pct: 30
profit_pool_context: 芯片制造利润池（TSMC毛利率66.2%，净利$40B+，占据晶圆代工行业80%+利润）
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: TSMC
    share: 72%
    note: 台湾，3nm/2nm独揽>90%先进制程份额，FY2025营收$122.5B(+36%)，毛利率66.2%，净利$40B+，2nm $30K/wafer满单至2028
  - name: 三星
    share: ~7%
    note: 韩国，2nm GAA良率40-60%落后TSMC(70-80%)，客户流失严重，Tesla FSD+Meta MTIA小量订单, Intel Foundry
  china:
  - name: SMIC
    share: 5.3%
    note: 7nm N+2受限于DUV无法进入5nm以下，是中国半导体最大瓶颈
  barriers:
  - item: 资本强度
    detail: 3nm工厂$300亿+，2nm更高$350亿+
  - item: EUV获取
    detail: ASML独家+荷兰/美国出口管制
  - item: GAA技术积累10年+
    detail: FinFET→GAA需要全新的晶体管架构知识
  tech_gap:
  - dimension: TSMC先进制程垄断>90%不可撼动。中国SMIC卡在7nm是中国半导体最大瓶颈。Intel 18A+RibbonFET+PowerVia是最有希望的替代方案但商业化仍需2-3年
    detail: ''
key_trends:
- title: TSMC 2nm(N2) $30K/wafer满单至2028
  detail: Apple锁定>50%初期产能，NVIDIA Vera Rubin/AMD Venice跟进
- title: 三星2nm GAA良率40-60%追赶中
  detail: 获Tesla FSD+Meta MTIA订单但量不大
- title: Intel 18A成地缘政治关键
  detail: Microsoft Maia/Amazon/NVIDIA $5B备选协议，但运营亏损$10.3B是重大拖累
- title: TSMC 2026 Capex $52-56B(+40%)
  detail: 10-20%投入CoWoS先进封装，先进制程「富人俱乐部」门槛持续提高
price_conduction:
- TSMC 3nm代工价格年涨10-15%
- 先进制程垄断赋予极强定价权
- 芯片设计公司(NVIDIA/AMD/Apple)被迫接受涨价
- 部分成本转嫁至AI服务器ODM和云厂商
- 最终推动AI算力总成本上升
- 长期加速云厂商自研芯片(Google TPU/AWS Trainium)趋势。2nm $30K/wafer
- 仅Apple/NVIDIA/AMD能负担
- 先进制程「富人俱乐部」
wikilinks:
- 高纯硅料与硅片
- 光刻胶与湿化学品
- 电子特气
- 光刻机
- 刻蚀设备
- 薄膜沉积设备
- 检测量测设备
- 清洗设备
- CMP设备
- 离子注入设备
- 先进封装(CoWoS/3D)
- 封装测试(OSAT)
- 成熟制程代工
- 存储芯片(DRAM/NAND)
- AI芯片设计(Fabless)
- CPU(服务器级)
- GPU
key_inputs:
- 硅晶圆
- 光刻胶
- 电子特气
- 光刻机
- 刻蚀设备
- 薄膜沉积设备
key_customers:
- AI芯片设计(Fabless)
- CPU(服务器级)
- GPU
- FPGA
- 存储芯片(DRAM/NAND)
companies:
- ticker: TSM
  name: 台积电(TSMC)
  role: 全球龙头
  rev: 85
- ticker: 005930.KS
  name: 三星电子
  role: 全球二线
  rev: 30
- ticker: INTC
  name: Intel
  role: 全球二线
  rev: 15
- ticker: '688981'
  name: 中芯国际
  role: 国产龙头
  rev: 60
sources:
- title: 头豹研究院《2026年中国晶圆代工行业概览》
  summary: 先进制程台积电一家独大，国产替代攻坚战进入决胜阶段
  url: https://data.eastmoney.com/report/zw_industry.jshtml
---

# 晶圆代工(先进制程)

> **半导体** · L3 · TAM **$170B** · CAGR **24%**

晶圆代工是芯片制造的**「工厂模式」**——无晶圆厂设计公司（NVIDIA/AMD/Qualcomm/Apple）将芯片版图交给代工厂在晶圆上刻出物理电路。|**TSMC在先进制程拥有绝对垄断**——全球份额72%(Q1 2026)，3nm/2nm独占>90%。FY2025营收$122.5B(+36% YoY)，毛利率66.2%，净利$40B+。2026 Capex $52-56B(+40% YoY)。2nm(N2) 2025Q4量产，$30K/wafer(比3nm贵50%)，Apple锁定>50%初期产能，**满单排到2028年**。|**三星2nm GAA良率40-60% vs TSMC 70-80%**，代工份额跌至~7%。Intel 18A(RibbonFET+PowerVia首创)HVM 2025年10月，良率65-75%，运营亏损$10.3B。SMIC受限于DUV光刻机停在7nm（N+2工艺），是中国半导体最大瓶颈。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $170B |
| 年复合增长率(CAGR) | 24% |
| 利润率区间 | 55-66% |
| 成本占比 | 35% (芯片制造成本（代工占芯片总成本35-40%）) |
| 利润池占比 | 30% (芯片制造利润池（TSMC毛利率66.2%，净利$40B+，占据晶圆代工行业80%+利润）) |
| 附加值 | high |

## 关联

（待补充）
