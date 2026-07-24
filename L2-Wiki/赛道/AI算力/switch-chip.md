---
name: 网络交换芯片
slug: switch-chip
industry: AI算力
layer: L3
tam_bn: 12.0
cagr_pct: 38.0
margin: 55-65%
cost_share_pct: 4
cost_share_context: AI集群总成本
profit_pool_pct: 6
profit_pool_context: AI集群利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Broadcom
    share: '>65%'
    note: 美国，#1 Tomahawk/Jericho，Tomahawk 6 102.4T 2025量产
  - name: NVIDIA
    share: '-'
    note: 美国，#2 Spectrum/Quantum，InfiniBand独家AI训练事实标准
  - name: Cisco
    share: '-'
    note: 美国，#3 Silicon One自研自用
  - name: Marvell
    share: '-'
    note: 美国，#4 Innovium
  - name: Intel
    share: '-'
    note: 美国，#5 Barefoot Tofino
  china:
  - name: 盛科通信
    share: '-'
    note: 国产交换芯片
  - name: 华为
    share: '-'
    note: 自研交换芯片
  barriers:
  - item: 51.2T/102.4T交换容量设计
    detail: ''
  - item: SerDes IP 112G/224G
    detail: ''
  - item: InfiniBand/RoCE协议栈
    detail: ''
  tech_gap:
  - dimension: InfiniBand在AI训练占主导。Ultra Ethernet Consortium推动开放以太替代IB
    detail: ''
key_trends:
- title: 51.2T→102.4T交换芯片
  detail: Broadcom Tomahawk 6(102.4T)2025年量产，支持64x800G端口
- title: InfiniBand vs RoCE之争
  detail: AI训练倾向IB(低延迟/无损)，推理场景以太份额上升
- title: Ultra Ethernet Consortium挑战InfiniBand
  detail: AMD/Intel/微软/博通等联合推动开放以太标准替代IB
- title: 中国自研交换芯片替代Cisco/Broadcom
  detail: 盛科通信和华为自研交换芯片在国产替代中受益
- title: AI网络架构支出2024-2029 CAGR 38%
  detail: 东西向流量(GPU-to-GPU)爆发驱动高速交换芯片+全光交换演进，交换容量向150Tbps迈进
price_conduction:
- 交换芯片占AI集群成本<5%但决定网络性能。Broadcom垄断>65%商用市场
- 年涨价3-5%
- 云厂商采购成本上升
- 加速自研交换芯片（AWS/Google/华为）和Ultra Ethernet开放标准推动
wikilinks:
- GPU
- AI训练集群/超算
companies:
- ticker: AVGO
  name: Broadcom
  role: 龙头
  rev: 10
- ticker: CSCO
  name: Cisco
  role: 龙头
  rev: 25
- ticker: ANET
  name: Arista
  role: 二线弹性
  rev: 30
- ticker: 000938
  name: 紫光股份
  role: 二线弹性
  rev: 20
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 15
- ticker: HUAWEI
  name: 华为
  role: 二线弹性
  rev: 10
- ticker: JNPR
  name: Juniper
  role: 二线弹性
  rev: 10
- ticker: MRVL
  name: Marvell
  role: 二线弹性
  rev: 10
- ticker: INTC
  name: Intel
  role: 二线弹性
  rev: 10
key_customers:
- AI训练集群/超算
sources:
- title: Broadcom FY2025 Networking
  summary: ''
  url: ''
- title: Crehan Research Data Center Switch 2025
  summary: ''
  url: ''

key_inputs: ["EDA与IP核", "晶圆代工(先进制程)"]---

# 网络交换芯片

> **AI算力** · L3 · TAM **$12B** · CAGR **38%**

网络交换芯片是数据中心的**「交通调度中心」**——决定数据包路由、优先级和拥塞控制。AI集群要求51.2Tbps→102.4Tbps交换容量+纳秒级延迟。|**Broadcom Tomahawk/Jericho是商用芯片#1**，NVIDIA Spectrum/Quantum+InfiniBand在AI训练是事实标准，垄断GPU集群互联。Ultra Ethernet Consortium(UEC)试图用标准以太替代InfiniBand。|**AI集群推动交换机ASIC升级**：GPU:交换机比例从1:0.5升至1:2，800G→1.6T端口驱动下一代51.2T芯片。NVIDIA Spectrum-X以太网平台直接挑战Broadcom。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $12B |
| 年复合增长率(CAGR) | 38% |
| 利润率区间 | 55-65% |
| 成本占比 | 4% (AI集群总成本) |
| 利润池占比 | 6% (AI集群利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: [[消化笔记/2026-07-22-v1.1-德勤全球半导体趋势]]
> 置信度: 高

- **cagr_pct**: 20% → 38%（更新为AI网络架构支出CAGR）
- **key_trends**: +1条 "AI网络架构支出CAGR 38%——东西向流量爆发驱动高速交换芯片演进"
- **sources**: +1 德勤2026全球半导体行业趋势报告
- **依据**: 德勤v1.1——AI网络架构支出2024-2029 CAGR 38%，东西向流量(GPU-to-GPU)爆发驱动
