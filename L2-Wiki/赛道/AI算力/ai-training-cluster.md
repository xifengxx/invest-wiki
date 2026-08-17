---
name: AI训练集群/超算
slug: ai-training-cluster
industry: AI算力
layer: L3
tam_bn: 80.0
cagr_pct: 50.0
margin: 20-30%
cost_share_pct: 60
cost_share_context: AI训练平台
profit_pool_pct: 15
profit_pool_context: AI训练利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: xAI Colossus
    share: '-'
    note: 美国，200,000 H100最大单集群2025投产122天建成, Meta Research SuperCluster
  china:
  - name: 华为Atlas集群
    share: '-'
    note: 昇腾生态
  - name: 中科曙光
    share: '-'
    note: 603019 国产HPC超算龙头，海光CPU/DCU
  - name: 百度昆仑集群
    share: '-'
    note: ''
  barriers:
  - item: 网络互联
    detail: InfiniBand/RoCE/Ultra Ethernet
  - item: 电力供应
    detail: '>100MW'
  - item: 液冷基础设施
    detail: ''
  - item: GPU供应
    detail: 出口管制
  tech_gap:
  - dimension: 集群规模1万→10万→30万卡。通信效率是核心瓶颈
    detail: ''
key_trends:
- title: 集群规模从1万→10万→30万卡
  detail: xAI Colossus(20万卡)和Meta新集群目标30万卡，对电力和散热提出极大挑战
- title: InfiniBand vs Ethernet竞争
  detail: NVIDIA Spectrum-X(以太)挑战自家InfiniBand，Ultra Ethernet Consortium标准加速
- title: GPU集群功耗>100MW→配套电力/散热是瓶颈
  detail: 10万卡集群功耗约150MW，需要专门的变电站和液冷系统
- title: 马斯克Colossus 10万H100集群2025年投产
  detail: 从签约到建成仅122天，创数据中心建设速度纪录
- title: 算力10万倍增长超级周期
  detail: 华为预测2035年全社会算力较2025年增长10万倍，后训练算力消耗可能超越预训练，超算集群从万卡向百万卡演进
price_conduction:
- GPU集群占AI训练成本55%。云厂商自研芯片（Google TPU/AWS Trainium）和集群效率优化（网络/存储/调度）
- 训练成本长期呈下降趋势。NVIDIA GPU涨价部分被集群规模效应和效率提升抵消
wikilinks:
- GPU
- AI服务器
- 网络交换芯片
- 数据中心IDC
- AI模型训练平台
- NVMe/存储芯片
- 800G/1.6T光模块
key_inputs:
- GPU
companies:
- ticker: TSLA
  name: Tesla
  role: 二线弹性
  rev: 5
- ticker: '603019'
  name: 中科曙光
  role: 龙头
  rev: 50
- ticker: GOOGL
  name: Google(Alphabet)
  role: 龙头
  rev: 10
- ticker: MSFT
  name: Microsoft
  role: 龙头
  rev: 10
- ticker: AMZN
  name: Amazon(AWS)
  role: 龙头
  rev: 10
- ticker: META
  name: Meta
  role: 龙头
  rev: 10
- ticker: ORCL
  name: Oracle
  role: 二线弹性
  rev: 15
- ticker: HUAWEI
  name: 华为
  role: 二线弹性
  rev: 15
key_customers:
- AI模型训练平台
sources:
- title: xAI Colossus Announcement 2025
  summary: ''
  url: ''
- title: Meta AI Research Cluster Architecture
  summary: ''
  url: ''
- title: Oracle OCI Supercluster Case Study 2025
  summary: ''
  url: ''
---

# AI训练集群/超算

> **AI算力** · L3 · TAM **$80B** · CAGR **50%**

AI训练集群将**数千到百万颗GPU通过网络互联**，作为整体训练超大模型的超级计算系统。**核心挑战是通信和电力**——十万卡集群需TB/s级互联带宽和100MW+供电。|**xAI Colossus是全球最大集群**：20万H100(122天建成)→2026年55.5万GPU/2GW→目标100万GPU；Anthropic以$1.25B/月租赁Colossus 1产能至2029年。|**Meta Prometheus 1GW/36万GPU(2026)→Hyperion 5GW/180万GPU(2027)；OpenAI Stargate $500B，Phase 1 40万GPU/1.2GW(2026中)**。2026年超大规模Capex总计~$725B。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $80B |
| 年复合增长率(CAGR) | 50% |
| 利润率区间 | 20-30% |
| 成本占比 | 60% (AI训练平台) |
| 利润池占比 | 15% (AI训练利润池) |
| 附加值 | high |

## 关联

- 上游: [[GPU]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: 消化笔记/2026-07-22-v1.1-华为智能世界2035
> 置信度: 高

- **key_trends**: +1条 "算力10万倍增长超级周期——华为预测2035年算力增长10万倍"
- **sources**: +1 华为《智能世界2035》
- **依据**: 华为2035报告——2035年全社会算力较2025年增长10万倍，后训练+推理算力超越预训练
