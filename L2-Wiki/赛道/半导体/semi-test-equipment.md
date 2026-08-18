---
name: 测试设备
slug: semi-test-equipment
industry: 半导体
layer: L2
tam_bn: 7.65
cagr_pct: 7.35
margin: 45-55%
cost_share_pct: 8
cost_share_context: 半导体后道测试设备投资
profit_pool_pct: 10
profit_pool_context: 半导体设备利润池（Teradyne/Advantest双寡头）
value_add: high
updated: 2026-08
type: segment
tags:
- 半导体
- L2
competition:
  global:
  - name: Teradyne
    share: ~38%
    note: 美国，数字ATE龙头，SoC/CPU/GPU测试领先（UltraFLEX/J750平台）
  - name: Advantest
    share: ~32%
    note: 日本，存储测试龙头（HBM/3D NAND，市占超50%），T2000/T3000系列
  - name: Cohu
    share: ~10%
    note: 美国，Handler/分选机龙头
  china:
  - name: 华峰测控
    share: '-'
    note: 688200 国产模拟/混合信号ATE龙头，成熟制程突破
  - name: 长川科技
    share: '-'
    note: 300604 国产测试设备，覆盖分选机/探针台
  barriers:
  - item: 高精度测试向量生成
    detail: 先进制程SoC测试需数千通道并行高速测试
  - item: HBM堆叠测试复杂度
    detail: HBM3e/HBM4多层堆叠的TSV互连测试难度极高
  - item: AI芯片测试成本占比上升
    detail: 大芯片测试时长与成本随复杂度飙升
  tech_gap:
  - dimension: 中国差距约5-8年，华峰测控在模拟测试突破但高端SoC/存储测试仍空白，国产测试设备市占率<10%
    detail: ''
key_trends:
- title: HBM测试需求爆发
  detail: HBM3e/HBM4多层堆叠测试时间与复杂度大幅提升，Advantest存储测试机供不应求
- title: AI芯片测试成本占比上升
  detail: 大芯片（如NVIDIA GPU）测试成本占芯片成本比例升至10-15%
- title: 探针卡/Handler配套需求增长
  detail: Technoprobe探针卡、Cohu分选机随ATE同步增长
price_conduction:
- 测试设备是芯片良率与质量的最后一道关口
- Teradyne/Advantest双寡头合计~70%份额
- AI芯片测试需求驱动测试设备量价齐升
- 测试成本占芯片成本比例持续上升
- 国产华峰测控/长川科技在成熟制程替代
wikilinks:
- 检测量测设备
- 封装测试(OSAT)
- 存储芯片(DRAM/NAND)
key_inputs:
- 半导体设备零部件
- 电子特气
key_customers:
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
- 封装测试(OSAT)
companies:
- ticker: '6857.T'
  name: Advantest
  role: 存储测试龙头
  rev: 60
- ticker: TER
  name: Teradyne
  role: 数字测试龙头
  rev: 55
- ticker: '688200'
  name: 华峰测控
  role: 国产龙头
  rev: 40
- ticker: '300604'
  name: 长川科技
  role: 国产二线
  rev: 35
sources:
- title: 雪球《半导体测试设备总览2025》
  summary: 2025全球测试设备约$85亿（ATE 63%/探针台22%/分选机15%），Teradyne+Advantest合计~70%
  url: https://xueqiu.com/4313629558/371788291
---

# 测试设备

半导体测试设备（ATE自动测试设备/探针台/分选机）是芯片出厂前的最后一道质量关口，覆盖晶圆探针测试（CP）和成品测试（FT），确保芯片功能与性能达标。AI芯片复杂度提升和HBM堆叠测试需求，驱动测试设备成为半导体设备中增速最快的细分之一。
