---
name: Chiplet与异构集成
slug: semi-chiplet
industry: 半导体
layer: L2
tam_bn: 14.0
cagr_pct: 50.0
margin: 45-60%
cost_share_pct: 10
cost_share_context: 芯片总成本（设计+制造+封装）
profit_pool_pct: 8
profit_pool_context: Chiplet降低设计成本→释放更多公司进入AI芯片→IP复用创造新利润池
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L2
competition:
  global:
  - name: AMD
    share: '>50%'
    note: 美国，Chiplet商业化先驱，EPYC CCD+IOD/MI300X 9颗Chiplet
  - name: Intel
    share: ~20%
    note: 美国，Foveros直接键合+EMIB硅桥+UCIe标准推动者
  - name: TSMC
    share: ~55%(封装产能)
    note: 台湾，CoWoS/SoIC/InFO/3DFabric全品类先进封装
  china:
  - name: 长电科技(JCAP)
    share: '-'
    note: 600584 Chiplet封装XDFOI，AMD Chiplet核心封测伙伴
  - name: 通富微电
    share: '-'
    note: 002156 AMD Chiplet封测，FC-BGA基板封装
  barriers:
  - item: UCIe 2.0 die-to-die 1.6TB/s互联
    detail: 高速SerDes设计极难
  - item: Thermal管理
    detail: 多Chiplet堆叠散热是巨大挑战
  - item: 不同工艺节点die混装测试
    detail: 5nm Compute Die + 12nm I/O Die混装良率控制极难
  tech_gap:
  - dimension: 中国Chiplet设计能力较弱，但封测端（长电/通富）通过承接AMD/Intel订单积累先进封装经验
    detail: ''
key_trends:
- title: UCIe 2.0标准推动Chiplet从私有方案→开放生态
  detail: die-to-die互联标准化是行业转折点
- title: TSMC CoWoS/SoIC产能2026翻倍至120K wpm
  detail: 先进封装产能是Chiplet最大瓶颈
- title: AMD MI400 10颗Chiplet+Intel Foveros Direct+NVLink-C2C
  detail: 多Chiplet封装成AI芯片主流
- title: Chiplet+UCIe让创业公司以$100M设计AI芯片
  detail: 降低5x设计成本门槛
price_conduction:
- Chiplet将芯片设计成本从$500M→$100M（大幅降低）
- 更多创业公司进入AI芯片领域
- TSMC先进封装产能成新瓶颈
- 封装价值占比从15%→30%+。UCIe开放标准
- die-to-die互联IP标准化
- Chiplet从私有方案→开放生态
- 行业格局重塑
wikilinks:
- 先进封装(CoWoS/3D)
- 封装测试(OSAT)
- 晶圆代工(先进制程)
- AI芯片设计(Fabless)
- CPU(服务器级)
- GPU
- EDA与IP核
- FPGA
key_inputs:
- 晶圆代工(先进制程)
- 先进封装(CoWoS/3D)
- EDA与IP核
key_customers:
- AI芯片设计(Fabless)
- CPU(服务器级)
- GPU
- FPGA
companies:
- ticker: '600584'
  name: 长电科技
  role: 国产龙头
  rev: 30
- ticker: '002156'
  name: 通富微电
  role: 国产龙头
  rev: 35
- ticker: 002185
  name: 华天科技
  role: 国产二线
  rev: 25
- ticker: AMD
  name: AMD(Xilinx)
  role: 全球龙头
  rev: 20
- ticker: INTC
  name: Intel
  role: 全球龙头
  rev: 15
- ticker: '688521'
  name: 芯原股份
  role: 国产替代
  rev: 40
sources:
- title: UCIe 2.0标准白皮书(2025)
  summary: Chiplet从私有方案走向开放生态，UCIe 2.0支持3D封装和更高带宽
  url: https://www.uciexpress.org
- title: 集微半导体《先进封装企业分析》
  summary: 长电科技HBM3E良率98.5%，通富微电5nm Chiplet量产，CoWoS-L验证完成
  url: https://www.sina.cn/news/detail/5317250271415341.html
- title: 华为"韬定律"先进封装概念股分析
  summary: Chiplet+3D堆叠绕开光刻机封锁，性能飙升55%，2031年等效1.4nm
  url: https://mobile.aigupiao.com/lives/usermsg/id/5584213
---

# Chiplet与异构集成

> **半导体** · L2 · TAM **$14B** · CAGR **50%**

Chiplet将传统单一大芯片拆分为多个功能模块（Compute Die + I/O Die + Memory Die），分别在不同工艺节点制造后再通过先进封装集成——**「分而治之」**。AMD是Chiplet商业化先驱（EPYC的CCD+IOD架构，MI300X使用9颗Chiplet）。|**UCIe 1.0/2.0标准推动Chiplet从私有方案走向开放生态**——Intel/AMD/ARM/Qualcomm/NVIDIA/TSMC联合制定标准，实现1.6TB/s die-to-die带宽。Chiplet可将芯片设计成本从$500M降至$100M（IP复用）。|**市场$13.6B(2025)→$22.6B(2026)→$168.6B(2030)，CAGR 65%**。TSMC主导先进封装产能(~55%全球份额，CoWoS/SoIC/3DFabric)。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $14B |
| 年复合增长率(CAGR) | 50% |
| 利润率区间 | 45-60% |
| 成本占比 | 10% (芯片总成本（设计+制造+封装）) |
| 利润池占比 | 8% (Chiplet降低设计成本→释放更多公司进入AI芯片→IP复用创造新利润池) |
| 附加值 | high |

## 关联

（待补充）
