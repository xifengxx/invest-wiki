---
name: 网络设备（交换机）
slug: network-equipment
industry: AI算力
layer: L3
tam_bn: 16.2
cagr_pct: 8.3
margin: 60-65%
cost_share_pct: 15
cost_share_context: AI集群网络成本
profit_pool_pct: 20
profit_pool_context: 数据中心网络利润池
value_add: high
updated: 2026-08
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Cisco
    share: ~29.8%
    note: 美国，整体交换机龙头，但企业园区收入占比高、数据中心增速慢(16.9%)
  - name: Arista
    share: ~19.2%
    note: 美国，数据中心交换机龙头，AI后端网络份额第三，同比增长29%
  - name: NVIDIA Spectrum-X
    share: ~25.9%
    note: AI后端网络挑战者，Spectrum-X以太网平台，Q2 2025收入飙升647%
  china:
  - name: 华为
    share: '-'
    note: 数据中心交换机，中国份额领先
  - name: 锐捷网络
    share: '-'
    note: 国产数据中心交换机
  barriers:
  - item: 高速交换芯片与系统协同
    detail: 800G/1.6T端口需芯片、光模块、系统级协同优化
  - item: 大规模集群流量调度
    detail: 十万卡集群的拥塞控制与负载均衡（NVIDIA Spectrum-X优势）
  - item: 无损网络（RoCE/IB）
    detail: AI训练对丢包零容忍，需无损以太网
  tech_gap:
  - dimension: 中国交换机硬件追平，但高速交换芯片依赖Broadcom，AI集群级调度软件落后于NVIDIA Spectrum-X
    detail: ''
key_trends:
- title: AI后端网络以太网化
  detail: 2025以太网超InfiniBand两倍成AI首选架构，AI后端以太网销售翻倍
- title: 800G→1.6T升级
  detail: 800G主导2025，1.6T交换机2026下半年出货
- title: NVIDIA挑战传统双雄
  detail: Spectrum-X凭借GPU捆绑切入，Celestica+NVIDIA占AI后端~50%
price_conduction:
- 交换机是AI集群Scale-out互联核心
- AI后端网络需求爆发，800G/1.6T端口量价齐升
- NVIDIA Spectrum-X捆绑GPU销售，冲击Cisco/Arista
- 交换机成本占AI集群网络成本大头
wikilinks:
- 网络交换芯片
- 800G/1.6T光模块
- AI服务器
- AI训练集群/超算
key_inputs:
- 网络交换芯片
- 800G/1.6T光模块
- DSP与光芯片
key_customers:
- 云计算IaaS
- AI训练集群/超算
- 数据中心IDC
companies:
- ticker: CSCO
  name: Cisco
  role: 整体龙头
  rev: 55
- ticker: ANET
  name: Arista
  role: 数据中心龙头
  rev: 60
- ticker: NVDA
  name: NVIDIA
  role: AI后端挑战者
  rev: 50
- ticker: '000063'
  name: 中兴通讯
  role: 国产厂商
  rev: 40
sources:
- title: Dell'Oro《AI后端网络2025》
  summary: 2025数据中心交换机$162亿(CAGR 8.3%)，AI后端以太网翻倍超InfiniBand两倍，Celestica+NVIDIA占~50%
  url: https://www.delloro.com/news/ethernet-more-than-doubles-size-of-infiniband-as-the-leading-fabric-for-ai-scale-out-networks-in-2025/
---

# 网络设备（交换机）

数据中心交换机是AI集群Scale-out互联的核心系统级设备，负责GPU服务器之间的高速数据传输。AI训练推动后端网络从InfiniBand向以太网迁移，800G端口主导当前、1.6T即将量产，NVIDIA Spectrum-X凭借GPU捆绑切入，冲击Cisco/Arista传统格局。
