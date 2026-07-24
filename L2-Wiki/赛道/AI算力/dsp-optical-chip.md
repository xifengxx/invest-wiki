---
name: DSP与光芯片
slug: dsp-optical-chip
industry: AI算力
layer: L2
tam_bn: 3.0
cagr_pct: 40.0
margin: 50-70%
cost_share_pct: 15
cost_share_context: 光模块
profit_pool_pct: 35
profit_pool_context: 光模块利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: Marvell
    share: ~25%
    note: 美国，#1数据中心DSP，AWS Trainium定制
  - name: Broadcom
    share: ~20%
    note: 美国，#2 Tomahawk/Jericho+DSP双线
  - name: Macom
    share: '-'
    note: 美国，EML激光器/射频芯片
  - name: Semtech
    share: '-'
    note: 美国，TIA跨阻放大器
  china:
  - name: 源杰科技
    share: '-'
    note: 688498 国产EML/DML激光器
  - name: 长光华芯
    share: '-'
    note: 688048 高功率激光芯片
  - name: 仕佳光子
    share: '-'
    note: 688313 PLC/AWG芯片
  barriers:
  - item: 224G PAM4高速SerDes设计
    detail: ''
  - item: InP/SiPh工艺代工资源
    detail: ''
  - item: 硅光技术替代传统方案
    detail: ''
  tech_gap:
  - dimension: Marvell/Broadcom双寡头>70%。中国光芯片国产化率从5%→20%
    detail: ''
key_trends:
- title: 224G PAM4 DSP成1.6T标配
  detail: Marvell和Broadcom率先推出224G DSP，每通道速率从112G翻倍
- title: 硅光I/O替代铜连接
  detail: Ayar Labs与NVIDIA合作开发硅光I/O，可将GPU间通信功耗降低90%
- title: CPO(共封装光学)2026量产
  detail: 光引擎与交换ASIC合封，Marvell/Broadcom/Cisco布局
- title: Linear Drive(LPO)绕过DSP降功耗
  detail: 去除DSP可实现30%+功耗降低，是800G成本敏感场景的重要方案
price_conduction:
- DSP是光模块中价值最高环节（~30%成本）。Marvell/Broadcom双寡头垄断>70%份额
- 议价能力极强
- DSP芯片涨价直接压缩光模块厂（中际旭创/新易盛）利润
- 光模块厂被迫向上游自研DSP或寻找第二供应商
companies:
- ticker: AVGO
  name: Broadcom
  role: 二线弹性
  rev: 15
- ticker: MRVL
  name: Marvell
  role: 龙头
  rev: 25
- ticker: COHR
  name: Coherent
  role: 龙头
  rev: 15
- ticker: LITE
  name: Lumentum
  role: 二线弹性
  rev: 20
- ticker: '688498'
  name: 源杰科技
  role: 二线弹性
  rev: 70
- ticker: MTSI
  name: Macom
  role: 二线弹性
  rev: 20
- ticker: SMTC
  name: Semtech
  role: 二线弹性
  rev: 15
- ticker: '688313'
  name: 仕佳光子
  role: 概念股
  rev: 15
- ticker: '688048'
  name: 长光华芯
  role: 概念股
  rev: 10
wikilinks:
- 800G/1.6T光模块
key_customers:
- 800G/1.6T光模块
sources:
- title: LightCounting《Optical DSP and Silicon Photonics 2025》
  summary: ''
  url: ''
- title: Marvell AI Optics Day 2025
  summary: ''
  url: ''
- title: Yuanjie Semi IPO Prospectus 2025
  summary: ''
  url: ''

key_inputs: ["EDA与IP核", "晶圆代工(先进制程)"]---

# DSP与光芯片

> **AI算力** · L2 · TAM **$3B** · CAGR **40%**

**DSP是光模块的「大脑」**——负责信号调制解调、前向纠错、色散补偿和均衡。没有高性能DSP，800G/1.6T光信号无法在2公里以上光纤中可靠传输。|**光芯片（激光器/探测器）是光模块的「心脏」**——EML是800G主流方案，硅光（Silicon Photonics）是下一代方向。|Marvell和Broadcom在DSP领域**双寡头垄断**（合计>70%），Coherent和Lumentum在光芯片领域领先。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $3B |
| 年复合增长率(CAGR) | 40% |
| 利润率区间 | 50-70% |
| 成本占比 | 15% (光模块) |
| 利润池占比 | 35% (光模块利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从2→7条
