---
name: 晶圆代工(先进制程)
slug: foundry-advanced
industry: AI算力
layer: L2
tam_bn: 170.0
cagr_pct: 24.0
margin: 55-66%
cost_share_pct: 35
cost_share_context: 芯片制造成本
profit_pool_pct: 30
profit_pool_context: 芯片制造利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: TSMC
    share: 72%
    note: 台湾，3nm/2nm独揽>90%先进制程份额，FY2025营收$122.5B(+36%)，2nm $30K/wafer满单至2028，毛利率66.2%
  - name: 三星
    share: 7%
    note: 韩国，2nm GAA良率40-60%落后TSMC(70-80%)，代工份额持续下滑，获Tesla FSD+Meta MTIA订单
  - name: Intel
    share: ~3%
    note: 18A(HVM Oct2025)良率65-75%，RibbonFET+PowerVia首创，Microsoft Maia/Amazon/NVIDIA $5B备选，但FY2025运营亏损$10.3B
  china:
  - name: SMIC
    share: 5.3%
    note: 中国，7nm N+2受限于DUV，无法进入5nm以下
  - name: UMC
    share: 4.4%
    note: 台湾成熟制程
  - name: GlobalFoundries
    share: 3.9%
    note: 美国成熟制程
  - name: 华虹半导体
    share: 2.6%
    note: 688347 中国成熟制程
  barriers:
  - item: 资本强度
    detail: 3nm工厂$300亿+，2nm更高
  - item: EUV获取
    detail: ASML独家+出口管制，High-NA EUV $350M+/台
  - item: 技术积累
    detail: FinFET→GAA需10年+，良率爬坡3-5年
  tech_gap:
  - dimension: TSMC先进制程垄断>90%不可撼动。中国SMIC卡在7nm是中国半导体最大瓶颈。Intel 18A+PowerVia是最有希望的替代方案但商业化仍需2-3年
    detail: ''
key_trends:
- title: TSMC 2nm满单至2028，$30K/wafer
  detail: Apple锁定>50%初期产能，NVIDIA Vera Rubin/AMD Venice跟进，N2P 2026下半年性能增强版
- title: 三星2nm GAA良率40-60%追赶中
  detail: 获Tesla FSD+Meta MTIA订单但量不大，SF2P→SF2Z roadmap推进
- title: Intel 18A成地缘政治关键
  detail: PowerVia首创背供电，Microsoft/Amazon客户，NVIDIA $5B备选协议，但运营亏损$10.3B是重大拖累
- title: TSMC 2026 Capex $52-56B(+40%)
  detail: 10-20%投入CoWoS先进封装，2026年毛利率66%+创新高
- title: 先进制程两极分化
  detail: 2nm $30K/wafer只有Apple/NVIDIA/AMD能负担，成熟制程(28nm+)中国大规模扩产
price_conduction:
- TSMC 3nm代工价格年涨10-15%，先进制程垄断赋予极强定价权
- 芯片设计公司（NVIDIA/AMD）被迫接受涨价
- 部分成本转嫁至AI服务器ODM和云厂商
- 最终推动AI算力总成本上升
- 长期加速云厂商自研芯片（Google TPU/AWS Trainium）趋势
companies:
- ticker: TSM
  name: TSMC(台积电)
  role: 龙头
  rev: 95
- ticker: SMIC
  name: 中芯国际
  role: 二线弹性
  rev: 100
- ticker: 005930.KS
  name: Samsung
  role: 二线弹性
  rev: 15
- ticker: INTC
  name: Intel
  role: 概念股
  rev: 10
wikilinks:
- 光刻机
- 溅射靶材
- 光掩模版
- 刻蚀设备
- 清洗设备
- 电子特气
- CMP设备
- 检测量测设备
- 薄膜沉积设备
- 离子注入设备
- 高纯硅料与硅片
- 高速连接器与铜缆
- 光刻胶与湿化学品
- CPU(服务器级)
- 封装测试(OSAT)
- CMP抛光液与抛光垫
- 涂胶显影设备(Track)
- 前驱体与ALD/CVD材料
- 先进封装(CoWoS/3D)
- 存储芯片(DRAM/NAND)
- AI芯片设计(Fabless)
key_inputs:
- 光刻机
- 清洗设备
- 溅射靶材
- 光掩模版
- 电子特气
- 刻蚀设备
- CMP设备
- 检测量测设备
- 薄膜沉积设备
- 离子注入设备
- 高纯硅料与硅片
- 光刻胶与湿化学品
- CMP抛光液与抛光垫
- 前驱体与ALD/CVD材料
- 涂胶显影设备(Track)
key_customers:
- CPU(服务器级)
- 封装测试(OSAT)
- AI芯片设计(Fabless)
sources:
- title: TrendForce《Foundry Revenue Q4 2025》
  summary: ''
  url: https://www.trendforce.com
- title: IDC《Foundry Market Shares 2025》
  summary: ''
  url: https://www.idc.com
- title: TSMC FY2025 Earnings
  summary: ''
  url: https://investor.tsmc.com
- title: Wedbush TokenRing《2nm Dawn》Jan 2026
  summary: ''
  url: ''
- title: Intel Foundry FY2025
  summary: ''
  url: ''
---

# 晶圆代工(先进制程)

> **AI算力** · L2 · TAM **$170B** · CAGR **24%**

晶圆代工是芯片制造的**「工厂模式」**——NVIDIA/AMD/Apple将芯片版图交给代工厂在晶圆上刻出物理电路。|**TSMC绝对垄断先进制程**——全球份额72%(Q1 2026)，3nm/2nm独占>90%。FY2025营收$122.5B(+36%)，毛利率66.2%，2026 Capex $52-56B。2nm(N2)Q4 2025量产，$30K/wafer(比3nm贵50%)，Apple锁定>50%初期产能，**满单排到2028**。|**三星2nm GAA良率40-60% vs TSMC 70-80%**，代工份额跌至7%。Intel 18A(RibbonFET+PowerVia)HVM 2025年10月良率65-75%，获Microsoft Maia/Amazon定制芯片订单，NVIDIA $5B备选协议。SMIC受限于DUV停在7nm。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $170B |
| 年复合增长率(CAGR) | 24% |
| 利润率区间 | 55-66% |
| 成本占比 | 35% (芯片制造成本) |
| 利润池占比 | 30% (芯片制造利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从14→24条
