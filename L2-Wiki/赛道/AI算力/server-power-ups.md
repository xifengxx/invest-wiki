---
name: 服务器电源与UPS
slug: server-power-ups
industry: AI算力
layer: L2
tam_bn: 5.0
cagr_pct: 20.0
margin: 20-30%
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
  - name: Schneider Electric
    share: ~24%
    note: 法国，#1全球UPS，Galaxy VXL 500-1250kW，NVIDIA合作伙伴
  - name: Vertiv
    share: '-'
    note: 美国，#2 Trinergy/OneCore 5MW+，Ballard氢燃料合作
  - name: Eaton
    share: '-'
    note: 爱尔兰，#3 Brightlayer AI平台，收购Fibrebond/Resilient
  - name: ABB
    share: '-'
    note: 瑞士，MegaFlex AI-ready UPS
  - name: Delta
    share: '-'
    note: 台湾，高密度DC-DC/AC-DC
  china:
  - name: 华为数字能源
    share: '-'
    note: 锂电UPS+AI能源管理
  - name: 科华数据
    share: '-'
    note: 国内UPS龙头
  barriers:
  - item: 大功率UPS定制
    detail: 10MW+
  - item: SiC/GaN功率半导体
    detail: ''
  - item: NVIDIA认证
    detail: ''
  - item: 800V HVDC技术
    detail: ''
  tech_gap:
  - dimension: 锂电替换铅酸成标配。800V HVDC替代传统AC。氢燃料电池UPS 2026试点
    detail: ''
key_trends:
- title: AI机柜从40kW→120kW+，UPS从MW→10MW+
  detail: 传统UPS架构无法满足AI需求，模块化UPS(Schneider Galaxy VXL/Vertiv OneCore)成标配
- title: 锂电替换铅酸成标配
  detail: 锂电池能量密度3倍、寿命2倍，全生命周期成本已低于铅酸
- title: 800V HVDC为下一代方向
  detail: 减少AC-DC转换级数，效率提升3-5%，Schneider与NVIDIA联合推800V标准化
- title: 氢燃料电池UPS(Vertiv+Ballard)
  detail: 零碳排放，2026年试点项目，长期替代柴油发电机
- title: HVDC高压直流架构+PUE<1.1成为新建AIDC标配
  detail: 数据中心供电从AC向DC革新，新能源直供模式占比>30%，全链能源利用>70%
price_conduction:
- 服务器功耗从700W→1500W，对高功率PSU和UPS的需求升级。但UPS行业供应商分散（Schneider/Vertiv/Eaton/ABB/Delta/华为等）
- 竞争压制涨价空间
- AI带来的量增是主要收益来源，非价格提升
wikilinks:
- GPU
- AI服务器
- 功率半导体
- 数据中心IDC
key_inputs:
- 功率半导体
key_customers:
- AI服务器
- 功率半导体
- GPU
companies:
- ticker: VRT
  name: Vertiv
  role: 龙头
  rev: 40
- ticker: SU
  name: Schneider Electric
  role: 龙头
  rev: 20
- ticker: ETN
  name: Eaton
  role: 二线弹性
  rev: 18
- ticker: ABBN
  name: ABB
  role: 二线弹性
  rev: 15
- ticker: '2308'
  name: Delta Electronics
  role: 二线弹性
  rev: 20
- ticker: HUAWEI-POWER
  name: Huawei Digital Power
  role: 二线弹性
  rev: 15
- ticker: '6503'
  name: Mitsubishi Electric
  role: 二线弹性
  rev: 10
- ticker: RIELLO
  name: Riello UPS
  role: 二线弹性
  rev: 10
sources:
- title: MarketsandMarkets《Data Center Power Market 2025》
  summary: ''
  url: ''
- title: GIR《Data Center Power Supply 2025》
  summary: ''
  url: ''
---

# 服务器电源与UPS

> **AI算力** · L2 · TAM **$5B** · CAGR **20%**

服务器电源和UPS是数据中心的**「心脏」**——任何电力中断都可能导致数亿美元的GPU集群损毁。|**AI机柜功耗从10kW飙升至120kW+**——GB200单机架超120kW，需要HVDC 800V供电架构。UPS从铅酸电池向锂电池转型。|Schneider Electric(#1)、Vertiv和Eaton是数据中心电力的三大全球巨头。**SiC/GaN功率半导体**提升UPS效率至99%+。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $5B |
| 年复合增长率(CAGR) | 20% |
| 利润率区间 | 20-30% |
| 成本占比 | 3% (AI服务器) |
| 利润池占比 | 2% (AI服务器利润池) |
| 附加值 | medium |

## 关联

- 上游: [[功率半导体]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: [[消化笔记/2026-07-22-v1.1-华为智能世界2035]]
> 置信度: 高

- **key_trends**: +1条 "HVDC高压直流架构+PUE<1.1成为新建AIDC标配"
- **sources**: +1 华为《智能世界2035》
- **依据**: 华为2035报告——HVDC架构+PUE<1.1，绿电直供>30%，碳排放减少>80%
