---
name: Chiplet与异构集成
slug: chiplet
industry: AI算力
layer: L2
tam_bn: 14.0
cagr_pct: 50.0
margin: 40-50%
cost_share_pct: 5
cost_share_context: 芯片设计成本
profit_pool_pct: 8
profit_pool_context: 芯片设计利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: TSMC
    share: '-'
    note: 台湾，3D Fabric最完整方案(CoWoS/InFO/SoIC)
  - name: Intel
    share: '-'
    note: 美国，EMIB/Foveros/PowerVia
  - name: 三星
    share: '-'
    note: 韩国，X-Cube 3D IC
  - name: AMD
    share: '-'
    note: 美国，Chiplet商业化先驱(EPYC CCD+IOD, MI300)
  china:
  - name: 长电科技
    share: '-'
    note: 600584 Chiplet封装
  - name: 通富微电
    share: '-'
    note: '002156'
  - name: 芯原股份
    share: '-'
    note: 688521 Chiplet设计服务
  barriers:
  - item: UCIe标准
    detail: Intel/AMD/ARM/NVIDIA/TSMC联合制定UCIe 2.0，推动开放生态
  tech_gap:
  - dimension: Chiplet从定制→标准化。设计成本从$500M降至$100M(IP复用)。2026年全球Chiplet市场$47B
    detail: ''
key_trends:
- title: UCIe 2.0标准推动Chiplet从私有方案走向开放生态
  detail: die-to-die互联标准化是行业转折点
- title: TSMC CoWoS/SoIC产能2026翻倍至120K wpm
  detail: 先进封装产能是Chiplet最大瓶颈
- title: AMD MI400 10颗Chiplet+Intel Foveros Direct+NVLink-C2C
  detail: 多Chiplet封装成AI芯片主流
- title: Chiplet+UCIe让创业公司以$100M设计AI芯片
  detail: 降低5x设计成本门槛，中国Chiplet绕过先进制程限制
- title: 2026年全球Chiplet市场$47B
  detail: CAGR 50%+，从定制方案走向标准化生态
price_conduction:
- Chiplet架构将设计成本从$500M降至$100M（IP复用）
- 降低芯片设计门槛
- 更多创业公司进入AI芯片领域
- 竞争加剧
- 长期推动芯片价格下降
- 利好下游应用和消费者
wikilinks:
- GPU
key_customers:
- GPU
companies:
- ticker: TSM
  name: TSMC(台积电)
  role: 龙头
  rev: 20
- ticker: INTC
  name: Intel
  role: 龙头
  rev: 15
- ticker: AMD
  name: AMD
  role: 龙头
  rev: 30
- ticker: NVDA
  name: NVIDIA
  role: 二线弹性
  rev: 10
sources:
- title: ResearchAndMarkets《Chiplet Market Jan 2026》
  summary: ''
  url: https://www.researchandmarkets.com
- title: UCIe Consortium
  summary: ''
  url: https://www.uciexpress.org
- title: AMD MI300X Architecture
  summary: ''
  url: ''
- title: TSMC 3DFabric
  summary: ''
  url: ''

key_inputs: ["EDA与IP核", "先进封装CoWoS", "晶圆代工(先进制程)"]---

# Chiplet与异构集成

> **AI算力** · L2 · TAM **$14B** · CAGR **50%**

Chiplet将传统单一大芯片拆分为多个功能模块分别制造后集成——**「分而治之」，将设计成本从$500M降至$100M**。AMD是商业化先驱(EPYC CCD+IOD,MI300X 9颗Chiplet,>50%份额)。|**UCIe 1.0/2.0标准推动开放生态**——Intel/AMD/ARM/Qualcomm/NVIDIA/TSMC联合制定，1.6TB/s die-to-die带宽。TSMC主导先进封装产能(~55%全球份额，CoWoS/SoIC)，AMD MI400+Intel Foveros/EMIB+NVIDIA NVLink-C2C各有方案。|**市场$13.6B(2025)→$22.6B(2026)→$168.6B(2030),CAGR 65%**。AI加速器+服务器CPU+HBM驱动，先进封装产能翻倍扩张。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $14B |
| 年复合增长率(CAGR) | 50% |
| 利润率区间 | 40-50% |
| 成本占比 | 5% (芯片设计成本) |
| 利润池占比 | 8% (芯片设计利润池) |
| 附加值 | high |

## 关联

- 下游: [[GPU]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从1→9条
