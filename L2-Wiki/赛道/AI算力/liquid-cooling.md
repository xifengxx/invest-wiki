---
name: 散热液冷系统
slug: liquid-cooling
industry: AI算力
layer: L2
tam_bn: 5.0
cagr_pct: 33.0
margin: 25-35%
cost_share_pct: 3
cost_share_context: AI服务器
profit_pool_pct: 2
profit_pool_context: AI服务器利润池
value_add: medium
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: Vertiv
    share: 23%
    note: 美国，#1全球精密冷却，CoreWeave合作伙伴，250kW/机架, Schneider Electric
  - name: Eaton
    share: '-'
    note: 爱尔兰，#3收购Boyd $9.5B，AWS部署PUE<1.10, Johnson Controls
  china:
  - name: 液冷专精：CoolIT Systems
    share: '-'
    note: 美国，2MW CDU
  - name: nVent
    share: '-'
    note: 美国，纯液冷方案
  - name: Iceotope
    share: '-'
    note: 英国，KUL AI平台
  - name: ZutaCore
    share: '-'
    note: 以色列，两相液冷900W/GPU
  barriers: []
  tech_gap: []
key_trends:
- title: 液冷从选配变标配(GB200强制)
  detail: GPU功耗从700W→1500W+，风冷上限约30kW/机架，液冷可支持120kW+
- title: CDU从1MW→2.5MW+
  detail: CoolIT和Schneider/Motivair推出2MW+级别CDU，匹配超大规模AI集群需求
- title: 浸没式液冷渗透率提升
  detail: Submer和LiquidStack在浸没式领域领先，更适合高密度GPU集群
- title: 两相液冷(900W/GPU)2026年量产
  detail: ZutaCore与Vertiv合作，制冷效率是冷板式的2倍
- title: AI耗电激增驱动液冷长期超级成长
  detail: 华为预测2035年数据中心耗电1.5万亿度（2025年约0.04万亿度），HVDC架构+PUE<1.1成为标配，电力密度指数级增长，液冷需求将随之爆发
price_conduction:
- 液冷从选配变为标配（GB200强制液冷），需求爆发式增长。产能不足
- 短期液冷CDU涨价
- 但传统HVAC巨头（Schneider/Eaton/Johnson Controls）大举进入
- 中长期竞争加剧
- 价格回归理性。冷板式液冷标准化程度高，降价空间大
wikilinks:
- GPU
- AI服务器
- 数据中心IDC
key_customers:
- AI服务器
companies:
- ticker: VRT
  name: Vertiv
  role: 龙头
  rev: 30
- ticker: 002837
  name: 英维克
  role: 龙头
  rev: 40
- ticker: '300499'
  name: 高澜股份
  role: 二线弹性
  rev: 35
- ticker: '601138'
  name: 工业富联
  role: 二线弹性
  rev: 10
- ticker: COOLIT
  name: CoolIT Systems
  role: 二线弹性
  rev: 15
- ticker: NVT
  name: nVent
  role: 二线弹性
  rev: 20
- ticker: ICEOTOPE
  name: Iceotope
  role: 二线弹性
  rev: 10
- ticker: SUBMER
  name: Submer
  role: 二线弹性
  rev: 10
- ticker: ZUTACORE
  name: ZutaCore
  role: 二线弹性
  rev: 10
- ticker: JCI
  name: Johnson Controls
  role: 二线弹性
  rev: 15
sources:
- title: ABI Research《Top Data Center Cooling Companies 2025》
  summary: ''
  url: https://www.abiresearch.com
- title: MarketsandMarkets《Liquid Cooled Server Market 2025》
  summary: ''
  url: https://www.marketsandmarkets.com

key_inputs: ["冷却组件", "泵阀管件", "冷板"]---

# 散热液冷系统

> **AI算力** · L2 · TAM **$5B** · CAGR **33%**

数据中心液冷通过液体替代空气冷却高功耗IT设备。三大路线：**冷板式(D2C,占47%份额)、浸没式、两相液冷**。|**GB200 NVL72强制液冷——GPU从700W→1500W+，风冷已无法满足，液冷从选配变标配**。100-130kW/rack为液冷基线，Aligned DeltaFlow支持300kW/rack。液冷将DC冷却能耗从~40%降至<10%。|**Vertiv(23%全球份额,$6.9B营收)、Schneider($34.2B,收购Motivair)、Eaton($23.2B)**三巨头+CoolIT/nVent。CDU市场$1.05B(2025)→$7.74B(2032),CAGR 33%。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $5B |
| 年复合增长率(CAGR) | 33% |
| 利润率区间 | 25-35% |
| 成本占比 | 3% (AI服务器) |
| 利润池占比 | 2% (AI服务器利润池) |
| 附加值 | medium |

## 关联

- 下游: [[AI服务器]]

## 动态更新记录

### 更新 2026-07-22
> 来源: 消化笔记/2026-07-22-v1.1-华为智能世界2035
> 置信度: 中

- **key_trends**: +1条 "AI耗电激增驱动液冷长期超级成长——华为预测2035年数据中心耗电1.5万亿度"
- **sources**: +1 华为智能世界2035
- **依据**: 华为报告——2035年全球数据中心耗电1.5万亿度，新能源发电占比突破50%，为液冷长期超级成长提供上层愿景支撑

### 更新 2026-07-22 (v1.1)
> 来源: 消化笔记/2026-07-22-v1.1-华为智能世界2035
> 置信度: 高

- **key_trends**: 趋势#5增强——增加HVDC架构+PUE<1.1细节，丰富能源转型与液冷联动逻辑
- **依据**: 华为2035报告——HVDC架构+PUE<1.1，数据中心从电力消费者转型为能源路由器，进一步强化液冷长期需求确定性
