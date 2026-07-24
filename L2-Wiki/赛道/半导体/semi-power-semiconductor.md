---
name: 功率半导体
slug: semi-power-semiconductor
industry: 半导体
layer: L3
tam_bn: 42.0
cagr_pct: 12.0
margin: 30-45%
cost_share_pct: 10
cost_share_context: 新能源车BOM（主驱逆变器+OBC+DC/DC占整车BOM 8-12%）
profit_pool_pct: 8
profit_pool_context: 功率半导体利润池（新能源车+光伏+数据中心驱动，SiC利润率最高）
value_add: medium
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: Infineon
    share: ~20%
    note: 德国，功率半导体全球#1，SiC/GaN/IGBT全品类，汽车+工业双线, ON Semiconductor
  - name: STMicroelectronics
    share: ~10%
    note: '意法/瑞士，SiC #1（Tesla Model 3/Y主驱供应商）'
  - name: Wolfspeed
    share: '-'
    note: 美国，SiC衬底#1（全球最大SiC晶圆厂）
  china:
  - name: 时代电气
    share: '-'
    note: 688187 中车旗下IGBT龙头，高铁+新能源车双线
  - name: 斯达半导
    share: '-'
    note: 603290 IGBT模块国产#1，新能源车主驱突破
  - name: 比亚迪半导体
    share: '-'
    note: 自供IGBT+SiC，全球唯一垂直整合新能源车企半导体
  barriers:
  - item: SiC衬底缺陷控制（微管密度<0.1/cm²）
    detail: SiC晶体生长极慢极难
  - item: 车规认证(AEC-Q101)
    detail: 汽车级可靠性验证2-3年
  - item: 8寸SiC衬底量产
    detail: 6→8寸是降本关键（成本降30%+）
  tech_gap:
  - dimension: 中国IGBT差距2-3年（时代电气/斯达半导已达国际水平），SiC差距3-5年（衬底/外延/器件全方位追赶）
    detail: ''
key_trends:
- title: SiC在800V电动车平台渗透率从20%→50%+
  detail: Tesla Cybertruck/比亚迪仰望/保时捷Taycan全线采用
- title: GaN在数据中心UPS/快充爆发
  detail: 2026年GaN功率市场$1B+，CAGR 50%+
- title: 中国IGBT国产化率~25%→目标50%
  detail: 时代电气/斯达半导/比亚迪半导体三驾马车
- title: 8寸SiC衬底量产是降本关键
  detail: Wolfspeed/天科合达/天岳先进积极扩产
price_conduction:
- SiC衬底供给紧张
- 6寸→8寸转型中
- SiC MOSFET价格年降15-20%（规模效应+良率提升）
- SiC在800V电动车渗透率从20%→50%+。IGBT供给宽松
- 价格稳定。GaN在快充+数据中心UPS爆发
- ASP下降中
- 用量指数增长抵消降价
wikilinks:
- 高纯硅料与硅片
- 模拟芯片
- 成熟制程代工
- 离子注入设备
- 半导体设备零部件
- MCU与嵌入式处理器
- 封装测试(OSAT)
- 晶圆代工(先进制程)
key_inputs:
- 硅晶圆
- 成熟制程代工
key_customers:
- MCU与嵌入式处理器
- 半导体设备零部件
companies:
- ticker: IFX.DE
  name: 英飞凌(Infineon)
  role: 全球龙头
  rev: 40
- ticker: 'ON'
  name: 安森美(onsemi)
  role: 全球二线
  rev: 30
- ticker: STM
  name: 意法半导体(ST)
  role: 全球二线
  rev: 25
- ticker: '688396'
  name: 华润微电子
  role: 国产替代
  rev: 35
- ticker: '600460'
  name: 士兰微
  role: 国产替代
  rev: 30
- ticker: '600745'
  name: 闻泰科技(安世)
  role: 国产替代
  rev: 25
sources:
- title: Yole Group《2026年电力电子行业现状》
  summary: 全球电力电子市场CAGR 7.1%至2031年达413亿美元，英飞凌全产品组合遥遥领先，中国5家进入TOP20
  url: https://ee.ofweek.com/2026-07/ART-8420-2803-30694100.html
- title: Global Market Insights 功率半导体市场报告
  summary: 2025年全球557亿美元，前五占45.5%份额，SiC/GaN至2031年占31%
  url: https://www.gminsights.com/zh/industry-analysis/power-semiconductor-market
---

# 功率半导体

> **半导体** · L3 · TAM **$42B** · CAGR **12%**

功率半导体是管理和转换电能的**「电力电子心脏」**——MOSFET/IGBT/SiC/GaN四大品类。新能源车（主驱逆变器+OBC+DC/DC）、光伏逆变器、充电桩、数据中心UPS四大增长引擎。|**全球$42B+(2025)，Infineon(德国#1，~20%份额，SiC/GaN/IGBT全品类)、ON Semi(~12%，汽车+工业)、STMicroelectronics(~10%，SiC #1/Tesla供应商)、Wolfspeed(SiC衬底#1)**主导。SiC增速>30%（Tesla/比亚迪主驱逆变器800V平台驱动），GaN在快充+数据中心UPS爆发。|**中国时代电气(688187，中车旗下IGBT龙头)、斯达半导(603290，IGBT模块#1)、士兰微(600460)**在IGBT和SiC领域快速追赶。比亚迪半导体自供IGBT。中国IGBT国产化率~25%→目标50%。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $42B |
| 年复合增长率(CAGR) | 12% |
| 利润率区间 | 30-45% |
| 成本占比 | 10% (新能源车BOM（主驱逆变器+OBC+DC/DC占整车BOM 8-12%）) |
| 利润池占比 | 8% (功率半导体利润池（新能源车+光伏+数据中心驱动，SiC利润率最高）) |
| 附加值 | medium |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从1→6条
