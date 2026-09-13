---
name: Chiplet与异构集成
slug: chiplet
industries:
- AI算力
- 半导体
layer: L2
tam_bn: 14.0
cagr_pct: 50.0
margin: 40-50%
cost_share_pct: 5
cost_share_context: 芯片设计成本（半导体口径：芯片总成本（设计+制造+封装）10%）
profit_pool_pct: 8
profit_pool_context: 芯片设计利润池（半导体口径：8%，Chiplet降低设计成本→释放更多公司进入AI芯片→IP复用创造新利润池）
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: TSMC
    share: '~55%(封装产能)'
    note: 台湾，3D Fabric最完整方案(CoWoS/SoIC/InFO)，全品类先进封装，主导全球先进封装产能~55%
  - name: Intel
    share: ~20%
    note: 美国，EMIB硅桥+Foveros Direct直接键合+PowerVia，UCIe标准推动者
  - name: 三星
    share: '-'
    note: 韩国，X-Cube 3D IC
  - name: AMD
    share: '>50%'
    note: 美国，Chiplet商业化先驱（EPYC CCD+IOD架构，MI300X使用9颗Chiplet）
  china:
  - name: 长电科技(JCAP)
    share: '-'
    note: 600584 Chiplet封装XDFOI，AMD Chiplet核心封测伙伴
  - name: 通富微电
    share: '-'
    note: 002156 AMD Chiplet封测，FC-BGA基板封装
  - name: 芯原股份
    share: '-'
    note: 688521 Chiplet设计服务
  barriers:
  - item: UCIe标准
    detail: Intel/AMD/ARM/NVIDIA/TSMC联合制定UCIe 2.0，die-to-die 1.6TB/s互联，推动开放生态；高速SerDes设计极难
  - item: Thermal管理
    detail: 多Chiplet堆叠散热是巨大挑战
  - item: 不同工艺节点die混装测试
    detail: 5nm Compute Die + 12nm I/O Die混装良率控制极难
  tech_gap:
  - dimension: Chiplet从定制→标准化。设计成本从$500M降至$100M(IP复用)。2026年全球Chiplet市场$47B
    detail: ''
  - dimension: 中国Chiplet设计能力较弱，但封测端（长电/通富）通过承接AMD/Intel订单积累先进封装经验
    detail: ''
key_trends:
- title: UCIe 2.0标准推动Chiplet从私有方案走向开放生态
  detail: die-to-die互联标准化是行业转折点
- title: TSMC CoWoS/SoIC产能2026翻倍至120K wpm
  detail: 先进封装产能是Chiplet最大瓶颈
- title: AMD MI400 10颗Chiplet+Intel Foveros Direct+NVLink-C2C
  detail: 多Chiplet封装成AI芯片主流
- title: Chiplet+UCIe让创业公司以$100M设计AI芯片
  detail: 降低5x设计成本门槛，中国Chiplet绕过先进制程限制（华为「韬定律」路线：Chiplet+3D堆叠绕开光刻机封锁，性能提升55%，2031年等效1.4nm）
- title: 2026年全球Chiplet市场$47B
  detail: CAGR 50%+，从定制方案走向标准化生态
price_conduction:
- Chiplet架构将设计成本从$500M降至$100M（IP复用）
- 降低芯片设计门槛
- 更多创业公司进入AI芯片领域
- 竞争加剧
- 长期推动芯片价格下降
- 利好下游应用和消费者
- TSMC先进封装产能成新瓶颈
- 封装价值占比从15%→30%+，UCIe开放标准推动die-to-die互联IP标准化
- Chiplet从私有方案→开放生态，行业格局重塑
wikilinks:
- GPU
- 先进封装(CoWoS/3D)
- 封装测试(OSAT)
- 晶圆代工(先进制程)
- AI芯片设计(Fabless)
- CPU(服务器级)
- EDA与IP核
- FPGA
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
- ticker: '600584'
  name: 长电科技
  role: 国产龙头
  rev: 30
- ticker: '002156'
  name: 通富微电
  role: 国产龙头
  rev: 35
- ticker: '002185'
  name: 华天科技
  role: 国产二线
  rev: 25
- ticker: '688521'
  name: 芯原股份
  role: 国产替代
  rev: 40
key_inputs:
- EDA与IP核
- 先进封装CoWoS
- 晶圆代工(先进制程)
key_customers:
- GPU
- AI芯片设计(Fabless)
- CPU(服务器级)
- FPGA
sources:
- title: ResearchAndMarkets《Chiplet Market Jan 2026》
  summary: ''
  url: https://www.researchandmarkets.com
- title: UCIe Consortium / UCIe 2.0标准白皮书(2025)
  summary: Chiplet从私有方案走向开放生态，UCIe 2.0支持3D封装和更高带宽
  url: https://www.uciexpress.org
- title: AMD MI300X Architecture
  summary: ''
  url: ''
- title: TSMC 3DFabric
  summary: ''
  url: ''
- title: 集微半导体《先进封装企业分析》
  summary: 长电科技HBM3E良率98.5%，通富微电5nm Chiplet量产，CoWoS-L验证完成
  url: https://www.sina.cn/news/detail/5317250271415341.html
- title: 华为"韬定律"先进封装概念股分析
  summary: Chiplet+3D堆叠绕开光刻机封锁，性能飙升55%，2031年等效1.4nm
  url: https://mobile.aigupiao.com/lives/usermsg/id/5584213
---

# Chiplet与异构集成

> **AI算力** · L2 · TAM **$14B** · CAGR **50%**

Chiplet将传统单一大芯片拆分为多个功能模块分别制造后集成——**「分而治之」，将设计成本从$500M降至$100M**。AMD是商业化先驱(EPYC CCD+IOD,MI300X 9颗Chiplet,>50%份额)。|**UCIe 1.0/2.0标准推动开放生态**——Intel/AMD/ARM/Qualcomm/NVIDIA/TSMC联合制定，1.6TB/s die-to-die带宽。TSMC主导先进封装产能(~55%全球份额，CoWoS/SoIC)，AMD MI400+Intel Foveros/EMIB+NVIDIA NVLink-C2C各有方案。|**市场$13.6B(2025)→$22.6B(2026)→$168.6B(2030),CAGR 65%**。AI加速器+服务器CPU+HBM驱动，先进封装产能翻倍扩张。细分上，芯片被拆为 Compute Die + I/O Die + Memory Die，各自在不同工艺节点制造后再通过先进封装集成；封测端中国长电科技(XDFOI)与通富微电是AMD Chiplet核心封测伙伴；华为「韬定律」路线以Chiplet+3D堆叠绕开光刻机封锁，性能提升55%，2031年等效1.4nm。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $14B |
| 年复合增长率(CAGR) | 50% |
| 利润率区间 | 40-50% |
| 成本占比 | 5% (芯片设计成本)〔半导体口径：10% 芯片总成本（设计+制造+封装）〕 |
| 利润池占比 | 8% (芯片设计利润池)〔半导体口径：8% IP复用创造的新利润池〕 |
| 附加值 | high |

## 关联

- 下游: [[GPU]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从1→9条

### 更新 2026-09-13（合并 semi-chiplet 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-chiplet.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$14B）；本方 cagr 50% / margin 40-50% / value_add high 保留（对方 margin 45-60%）
- **口径保留**: cost_share / profit_pool 的半导体口径（10% 芯片总成本（设计+制造+封装） / 8% IP复用创造的新利润池）并入 context 备注明细，两个视角并存
- **key_trends**: 5 → 5 条。对方4条均为本方既有条目的同主题复述，未新增；将对方"华为韬定律"路线的具体数字（性能提升55%、2031年等效1.4nm）吸收进本方第4条 detail
- **price_conduction**: 6 → 9 条。并入对方独有主题：TSMC先进封装产能成新瓶颈、封装价值占比15%→30%+、Chiplet从私有方案走向开放生态/行业格局重塑
- **sources**: 4 → 6 条。UCIe Consortium 与对方"UCIe 2.0标准白皮书(2025)"同源（同 url）合并为一条并补入摘要；并入集微半导体《先进封装企业分析》、华为"韬定律"先进封装概念股分析
- **companies**: 4 → 8 家。并入 长电科技(600584,30)、通富微电(002156,35)、华天科技(002185,25)、芯原股份(688521,40)；共有公司 TSM/INTC/AMD/NVDA 沿用本方 rev，对方"AMD(Xilinx)"统一为本方名称 AMD
- **wikilinks**: 1 → 8 条。并入 先进封装(CoWoS/3D)、封装测试(OSAT)、晶圆代工(先进制程)、AI芯片设计(Fabless)、CPU(服务器级)、EDA与IP核、FPGA
- **key_inputs**: 3 → 3 条（对方 3 条均已被本方覆盖，对方"先进封装(CoWoS/3D)"归一到本方"先进封装CoWoS"）；**key_customers**: 1 → 4 条（并入 AI芯片设计(Fabless)、CPU(服务器级)、FPGA）
- **competition**: global 4 → 4 条。TSMC 补入 share（~55%封装产能）与全品类封装信息；Intel 补入 share（~20%）与 Foveros 直接键合/EMIB 硅桥；AMD 补入 share（>50%）与 MI300X 9颗Chiplet；china 3 → 3 条，长电补 XDFOI+AMD核心封测伙伴、通富补 FC-BGA 基板封装
- **barriers**: 1 → 3 条（并入 Thermal管理、不同工艺节点die混装测试，并把 1.6TB/s SerDes 难度并入 UCIe 条目）；**tech_gap**: 1 → 2 条（并入中国Chiplet设计弱/封测端积累经验）
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
