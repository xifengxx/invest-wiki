---
name: 封装测试(OSAT)
slug: semi-osat
industry: 半导体
layer: L3
tam_bn: 42.0
cagr_pct: 8.0
margin: 20-30%
cost_share_pct: 15
cost_share_context: 芯片总成本（封装+测试占15-25%）
profit_pool_pct: 5
profit_pool_context: 封测利润池（薄利多销，OSAT毛利率20-30% vs TSMC CoWoS 55-65%）
value_add: medium
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: 日月光(ASE)
    share: ~25%
    note: '台湾，全球OSAT #1，先进封装投资翻倍，SiP/Fan-out/FC-BGA'
  - name: Amkor
    share: ~15%
    note: 美国，#2全球，亚利桑那新厂服务Apple/TSMC
  - name: 长电科技(JCAP)
    share: ~10%
    note: 中国，#3全球(600584)，AMD Chiplet核心封测伙伴
  - name: 力成(PTI)
    share: ~6%
    note: 台湾，存储器封装#1
  china:
  - name: 通富微电
    share: '-'
    note: 002156 AMD Chiplet封测核心伙伴，FC-BGA扩产
  - name: 华天科技
    share: '-'
    note: 002185
  - name: 甬矽电子
    share: '-'
    note: 688362 SiP先进封装
  barriers:
  - item: 先进封装(FC-BGA/2.5D/3D)技术
    detail: 线宽/线距<5μm极难
  - item: 大客户绑定(AMD/Qualcomm/Apple)
    detail: 长期合约+联合研发
  - item: 产能规模和良率控制
    detail: 日产百万+颗芯片的良率管理
  tech_gap:
  - dimension: 中国封测差距最小(1-2代)，长电科技全球#3。OSAT是中国半导体最先达到国际水平的环节
    detail: ''
key_trends:
- title: 先进封装CAGR 15%+远高于传统封装3%
  detail: FC-BGA/SiP/Fan-out/2.5D推动OSAT升级
- title: TSMC切入封装(CoWoS/InFO/SoIC)挤压OSAT高端空间
  detail: OSAT需差异化竞争
- title: 中国长电/通富先进封装投资翻倍
  detail: XDFOI(长电)+Vision(通富)对标CoWoS
- title: Chiplet/UCIe推动OSAT从「外包」→「战略伙伴」
  detail: 先进封装成为芯片设计核心环节
- title: 传统OSAT模式面临商品化风险
  detail: 共设计芯片组(co-designed chiplet)减少独立封测需求，先进封装由代工厂主导，IDM+设计厂纵向整合挤压OSAT份额
price_conduction:
- 先进封装需求暴增
- ASE/Amkor/长电CAPEX翻倍
- 先进封装产能紧张
- 年涨5-8%
- 芯片总成本微涨。传统封装ASP平稳
- OSAT整体利润率稳定。TSMC CoWoS垄断>90%高端先进封装
- 利润大头留在Foundry而非OSAT
wikilinks:
- 成熟制程代工
- 封装基板材料
- 半导体设备零部件
- 晶圆代工(先进制程)
- Chiplet与异构集成
- 先进封装(CoWoS/3D)
- IC设计服务(Fabless)
key_inputs:
- 晶圆代工(先进制程)
- 成熟制程代工
key_customers:
- AI芯片设计(Fabless)
- CPU(服务器级)
- MCU与嵌入式处理器
- 存储芯片(DRAM/NAND)
companies:
- ticker: 3711.TW
  name: 日月光投控(ASE)
  role: 全球龙头
  rev: 70
- ticker: AMKR
  name: 安靠科技(Amkor)
  role: 全球二线
  rev: 60
- ticker: '600584'
  name: 长电科技(JCET)
  role: 国产龙头
  rev: 65
- ticker: '002156'
  name: 通富微电
  role: 国产二线
  rev: 50
- ticker: '688362'
  name: 甬矽电子
  role: 国产替代
  rev: 30
sources:
- title: 芯思想研究院 2025全球OSAT排名
  summary: 日月光26%/安靠14%/长电科技12.2%三分天下，先进封装占比均超45%
  url: https://cloud.tencent.cn/developer/article/2652873
- title: 东吴证券 2025Q3封测总结
  summary: AI带动先进封测需求，长电科技先进封装收入占比跃升至45%
  url: https://data.eastmoney.com/report/zw_industry.jshtml
---

# 封装测试(OSAT)

> **半导体** · L3 · TAM **$42B** · CAGR **8%**

封装测试（OSAT = Outsourced Semiconductor Assembly and Test）将晶圆切割、封装、测试为成品芯片——是芯片从晶圆到产品的**「最后一公里」**。封装从传统引线键合→FC-BGA→2.5D/3D先进封装演进。|**全球OSAT市场$42B+(2025)，日月光(ASE台湾#1，~25%份额)、Amkor(美国#2，~15%)、长电科技(JCAP中国#3，~10%)、SPIL(台湾)、力成(PTI台湾)**为五大龙头。|**先进封装（FC-BGA/SiP/Fan-out/2.5D/3D）CAGR 15%+远高于传统封装3%**。TSMC切入CoWoS/InFO/SoIC挤压传统OSAT高端空间。中国长电科技/通富微电先进封装投资翻倍。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $42B |
| 年复合增长率(CAGR) | 8% |
| 利润率区间 | 20-30% |
| 成本占比 | 15% (芯片总成本（封装+测试占15-25%）) |
| 利润池占比 | 5% (封测利润池（薄利多销，OSAT毛利率20-30% vs TSMC CoWoS 55-65%）) |
| 附加值 | medium |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: [[消化笔记/2026-07-22-v1.1-德勤全球半导体趋势]]
> 置信度: 高

- **key_trends**: +1条 "传统OSAT模式面临商品化风险——共设计芯片组减少独立封测需求"
- **sources**: +1 德勤2026全球半导体行业趋势报告
- **依据**: 德勤v1.1——OSAT传统模式面临商品化风险，共设计芯片组趋势使封测环节向设计+代工端整合
