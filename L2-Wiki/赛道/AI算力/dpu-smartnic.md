---
name: DPU/SmartNIC
slug: dpu-smartnic
industry: AI算力
layer: L3
tam_bn: 6.0
cagr_pct: 35.0
margin: 50-60%
cost_share_pct: 2
cost_share_context: AI服务器成本
profit_pool_pct: 3
profit_pool_context: AI服务器利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: NVIDIA BlueField
    share: '-'
    note: 美国，#1与GPU捆绑，AI服务器标配, Intel IPU
  china:
  - name: 自研DPU：AWS Nitro
    share: '-'
    note: 最早大规模部署, Microsoft Azure Boost
  barriers: []
  tech_gap: []
key_trends:
- title: DPU从可选→AI服务器标配
  detail: 卸载网络/存储/安全任务，释放CPU/GPU计算资源
- title: 云厂商自研DPU
  detail: AWS Nitro/Azure Boost/阿里CIPU，大型云厂商倾向自研而非外购
- title: DPU+GPU协同调度成AI训练优化
  detail: NVIDIA BlueField与GPU的紧密集成是差异化优势
- title: 中国DPU自研进展
  detail: 阿里CIPU/华为DataPU在国产替代中领先，但生态不如NVIDIA
price_conduction:
- DPU在AI服务器中占比<5%但增速快（每代GPU需配套升级DPU）。NVIDIA BlueField与GPU捆绑销售
- DPU利润率跟随GPU
- NVIDIA可承受DPU单独降价以维持GPU生态壁垒
wikilinks:
- AI服务器
- GPU
- FPGA
key_inputs:
- FPGA
companies:
- ticker: MRVL
  name: Marvell
  role: 龙头
  rev: 10
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 10
- ticker: AVGO
  name: Broadcom
  role: 二线弹性
  rev: 5
- ticker: INTC
  name: Intel
  role: 二线弹性
  rev: 10
- ticker: AMD
  name: AMD
  role: 二线弹性
  rev: 5
- ticker: MSFT
  name: Microsoft
  role: 概念股
  rev: 5
- ticker: FUNGIBLE
  name: Fungible
  role: 二线弹性
  rev: 10
- ticker: KALRAY
  name: Kalray
  role: 二线弹性
  rev: 10
key_customers:
- AI服务器
sources:
- title: NVIDIA BlueField 4 Roadmap 2025
  summary: ''
  url: ''
- title: AWS re:Invent Nitro Architecture 2025
  summary: ''
  url: ''
---

# DPU/SmartNIC

> **AI算力** · L3 · TAM **$6B** · CAGR **35%**

DPU/SmartNIC是AI服务器的**「协处理器」**——将网络/存储/安全任务从CPU卸载到专用硬件。GPU间通信量极大，DPU后台处理加解密/压缩/RDMA传输。|**NVIDIA BlueField市场领导者**(与GPU捆绑)，AWS Nitro+Azure Boost自研DPU，Marvell Octeon/Intel IPU竞争。DPU从「可选」→AI服务器「标配」，AI集群中每台服务器配1-2颗DPU。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $6B |
| 年复合增长率(CAGR) | 35% |
| 利润率区间 | 50-60% |
| 成本占比 | 2% (AI服务器成本) |
| 利润池占比 | 3% (AI服务器利润池) |
| 附加值 | high |

## 关联

- 上游: [[FPGA]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从2→7条
