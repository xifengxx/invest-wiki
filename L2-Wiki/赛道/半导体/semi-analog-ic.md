---
name: 模拟芯片
slug: semi-analog-ic
industry: 半导体
layer: L4
tam_bn: 95.0
cagr_pct: 8.0
margin: 45-65%
cost_share_pct: 15
cost_share_context: 电子系统BOM成本
profit_pool_pct: 10
profit_pool_context: 模拟芯片利润池（TI毛利率65%+为行业天花板，ADI 60%+）
value_add: medium
updated: 2026-07
type: segment
tags:
- 半导体
- L4
competition:
  global:
  - name: Texas Instruments(TI)
    share: ~20%
    note: 美国，#1全球模拟芯片，65%+毛利率，12寸RFAB/ LFAB成本优势，80,000+料号, Analog Devices(ADI)
  - name: Infineon
    share: ~8%
    note: 德国，汽车模拟(MOSFET/IGBT驱动)
  - name: STMicroelectronics
    share: ~7%
    note: 意法/瑞士，汽车+工业模拟
  china:
  - name: 圣邦股份
    share: '-'
    note: 300661 国产模拟#1（3,000+料号），电源管理+信号链
  - name: 思瑞浦
    share: '-'
    note: 688536 高性能信号链(ADC/DAC/放大器)
  - name: 纳芯微
    share: '-'
    note: 688052 隔离+传感器+驱动
  barriers:
  - item: BCD/高压/射频工艺积累
    detail: 模拟芯片设计极度依赖工艺经验
  - item: 产品料号广度
    detail: TI 80,000+料号 vs 圣邦3,000+，巨大差距
  - item: 车规/工规认证(AEC-Q100)
    detail: 汽车模拟芯片验证2-3年
  tech_gap:
  - dimension: 中国模拟芯片差距5-8年，料号数和工艺积累差距巨大，但在隔离/驱动/消费PMIC特定品类有突破
    detail: ''
key_trends:
- title: AI服务器PMIC需求暴增
  detail: 每台GB200 NVL72需200+颗PMIC（GPU+CPU+HBM+NVSwitch全需要独立供电）
- title: TI 12寸厂成本优势→价格战压缩中国企业利润
  detail: 8寸→12寸迁移是行业大趋势
- title: 中国模拟料号从3K→10K+快速扩张
  detail: 圣邦/思瑞浦/纳芯微密集发布新产品
- title: 汽车电动化+智能化→模拟芯片用量翻倍
  detail: 单车模拟芯片价值从$150→$300+
price_conduction:
- 模拟芯片产品生命周期长(5-10年)
- 价格稳定（年降3-5%）
- 供给约束时涨价（TI 2021-22涨价30%+）。AI服务器PMIC需求暴增
- 结构性增长
- TI/ADI/Infineon受益。TI 12寸厂成本优势(比8寸低40%)
- 对中国厂商进行价格战
- 压缩中国模拟芯片利润空间
wikilinks:
- AI服务器
- 成熟制程代工
key_customers:
- AI服务器
companies:
- ticker: '300661'
  name: 圣邦股份
  role: 二线弹性
  rev: 85
- ticker: '688536'
  name: 思瑞浦
  role: 二线弹性
  rev: 80
- ticker: TXN
  name: Texas Instruments
  role: 龙头
  rev: 80
- ticker: ADI
  name: Analog Devices (ADI)
  role: 龙头
  rev: 80
- ticker: SWKS
  name: Skyworks Solutions
  role: 二线弹性
  rev: 85
- ticker: QRVO
  name: Qorvo
  role: 二线弹性
  rev: 85
- ticker: MPWR
  name: Monolithic Power Systems (MPS)
  role: 龙头
  rev: 75
- ticker: CRUS
  name: Cirrus Logic
  role: 二线弹性
  rev: 75
- ticker: PI
  name: Impinj
  role: 二线弹性
  rev: 85
- ticker: SMTC
  name: Semtech
  role: 二线弹性
  rev: 60
- ticker: SITM
  name: SiTime
  role: 二线弹性
  rev: 90
key_inputs:
- 成熟制程代工
sources:
- title: IC Insights《Analog IC Market 2025》
  summary: ''
  url: ''
- title: Texas Instruments FY2025
  summary: ''
  url: ''
- title: 圣邦股份2025年报
  summary: ''
  url: ''
- title: 思瑞浦2025年报
  summary: ''
  url: ''
- title: ADI FY2025
  summary: ''
  url: ''
---

# 模拟芯片

> **半导体** · L4 · TAM **$95B** · CAGR **8%**

模拟芯片处理真实世界的连续信号（声音/光/温度/压力/电压）——是**数字世界与物理世界的「接口」**。电源管理芯片（PMIC）和信号链（放大器/ADC/DAC/接口）为两大品类。|全球$95B+(2025)，**TI(美国#1，~20%，65%+毛利率，12寸厂成本优势，80,000+料号)、ADI(#2，~12%，高性能信号链)、Infineon、ST主导**。PMIC在AI服务器中需求暴增——每台GB200 NVL72需要200+颗PMIC。|中国圣邦股份(300661，国产模拟#1，3000+料号)、思瑞浦(688536，信号链)、纳芯微(688052，隔离+传感器)追赶。TI 12寸厂成本优势⇒对中国模拟芯片进行价格战。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $95B |
| 年复合增长率(CAGR) | 8% |
| 利润率区间 | 45-65% |
| 成本占比 | 15% (电子系统BOM成本) |
| 利润池占比 | 10% (模拟芯片利润池（TI毛利率65%+为行业天花板，ADI 60%+）) |
| 附加值 | medium |

## 关联

- 下游: [[AI服务器]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从2→7条
