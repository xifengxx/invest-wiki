---
name: ASIC/AI定制芯片
slug: asic-ai-chip
industry: AI算力
layer: L3
tam_bn: 60.0
cagr_pct: 45.0
margin: 45-60%
cost_share_pct: 20
cost_share_context: AI推理总成本
profit_pool_pct: 15
profit_pool_context: AI推理利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Google TPU
    share: '-'
    note: 美国，最大规模部署，TPU v6 2026年, AWS Trainium
  - name: Broadcom
    share: '-'
    note: 美国，#1定制ASIC设计服务，Google/Meta/ByteDance客户$12B+ AI收入
  - name: Marvell
    share: '-'
    note: 美国，#2定制ASIC，AWS客户
  china:
  - name: 华为昇腾
    share: '-'
    note: Ascend 910B，国内AI训练#1
  - name: 寒武纪
    share: '-'
    note: 688256 思元MLU云端推理
  - name: 昆仑芯
    share: '-'
    note: 百度昆仑2代7nm
  barriers: []
  tech_gap: []
key_trends:
- title: ASIC在推理侧渗透率从20%向40%+
  detail: Google TPU v6/AWS Trainium2/Microsoft Maia2 2026年大规模部署
- title: Broadcom成最大受益者
  detail: Google/Meta/ByteDance三大客户驱动AI ASIC收入2025年$12B+
- title: Chiplet使定制ASIC开发周期缩短
  detail: 从24个月缩短至12-15个月，更多企业可以自研AI芯片
- title: 中国ASIC(华为昇腾/寒武纪)在国产替代中加速
  detail: 昇腾910B是国内AI训练市场替代NVIDIA的首选
price_conduction:
- ASIC在特定场景推理性价比超过GPU 3-10倍
- 推动AI推理成本大幅下降
- 利好AI应用大规模部署
- 降低对NVIDIA GPU的依赖。但ASIC开发周期18-24个月，灵活性差，适合大规模稳定工作负载
wikilinks:
- GPU
- 边缘AI
- AI Agent
- HBM高带宽内存
- 先进封装CoWoS
companies:
- ticker: AVGO
  name: Broadcom
  role: 龙头
  rev: 30
- ticker: MRVL
  name: Marvell
  role: 二线弹性
  rev: 20
- ticker: GOOGL
  name: Google(Alphabet)
  role: 龙头
  rev: 5
- ticker: AMZN
  name: Amazon(AWS)
  role: 二线弹性
  rev: 3
- ticker: HUAWEI
  name: 华为
  role: 龙头
  rev: 10
- ticker: '688256'
  name: 寒武纪
  role: 龙头
  rev: 90
- ticker: BABA
  name: 阿里巴巴
  role: 概念股
  rev: 3
- ticker: GROQ
  name: Groq
  role: 二线弹性
  rev: 95
- ticker: CBRS
  name: Cerebras
  role: 二线弹性
  rev: 95
- ticker: KUNLUN
  name: 昆仑芯
  role: 二线弹性
  rev: 85
- ticker: GRAPH
  name: Graphcore
  role: 二线弹性
  rev: 10
- ticker: SAMBA
  name: SambaNova
  role: 二线弹性
  rev: 10
key_inputs:
- HBM高带宽内存
- 先进封装CoWoS
sources:
- title: SemiAnalysis《ASIC vs GPU 2025》
  summary: ''
  url: ''
- title: Broadcom FY2025 AI Revenue
  summary: ''
  url: ''
- title: TrendForce《ASIC HBM Demand Surge 80% in 2026》
  summary: ''
  url: ''
---

# ASIC/AI定制芯片

> **AI算力** · L3 · TAM **$60B** · CAGR **45%**

ASIC是针对特定AI工作负载**定制的芯片**——在特定任务上性能和能效可超越GPU 3-10倍，TCO优势40-65%。Google TPU(Ironwood v7, 4,614 TFLOPS FP8, $13K vs B200 $35K)是最大规模部署。|**JPMorgan预计2027年ASIC出货量(12.5M颗)将超过GPU(10.9M颗)**。Broadcom主导80-85%高端ASIC市场，AI收入$20B(FY2025)→>$60B(FY2026)→>$150B(FY2027 tracking)，6大客户含Google/Meta/ByteDance/OpenAI/SoftBank/Anthropic。Marvell占10-12%，AWS Trainium 3(3nm)+Microsoft Maia。|ASIC劣势是开发周期18-24个月且灵活性差，但在推理侧渗透率正从20%→40%+快速增长。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $60B |
| 年复合增长率(CAGR) | 45% |
| 利润率区间 | 45-60% |
| 成本占比 | 20% (AI推理总成本) |
| 利润池占比 | 15% (AI推理利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从1→10条
