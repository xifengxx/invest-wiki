---
name: 高速连接器与铜缆
slug: high-speed-connector
industry: AI算力
layer: L2
tam_bn: 5.0
cagr_pct: 30.0
margin: 30-45%
cost_share_pct: 2
cost_share_context: AI服务器（半导体口径：AI服务器BOM成本，3%）
profit_pool_pct: 2
profit_pool_context: AI服务器利润池（半导体口径：连接器利润池，2%）
value_add: medium
updated: 2026-09
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: Amphenol
    share: ~20%
    note: 美国，2025年收入$231B超TE成全球新王，NVLink背板连接器独家供应商($10K/机柜), TE Connectivity
  - name: Molex
    share: ~10%
    note: 美国(Koch Industries)，数据中心连接器，NearStream PCIe 6.0
  - name: Samtec
    share: '-'
    note: 美国，112G PAM4
  china:
  - name: 立讯精密
    share: '-'
    note: 002475 224G高速铜缆，切入NVLink供应链；AI服务器连接器进入NVIDIA供应链，从消费电子→AI转型
  - name: 澜起科技
    share: '-'
    note: 688008 DDR5 RCD/MDB芯片，CXL互联
  - name: 中航光电
    share: '-'
    note: 002179 军工+通信连接器
  barriers:
  - item: 224G/448G信号完整性
    detail: 通道损耗/串扰/反射控制极难
  - item: NVLink独家认证
    detail: ''
  - item: 精密模具加工
    detail: μm级精度，连接器pin间距<0.5mm
  - item: AI服务器定制连接器
    detail: GB200 NVLink背板连接器价值$10,000+/rack
  tech_gap:
  - dimension: Amphenol凭NVLink独家供应跃升全球连接器新王。立讯精密224G领域快速追赶（AI服务器连接器已进入NVIDIA供应链），差距3-5年
    detail: ''
key_trends:
- title: NVLink背板连接器从112G→224G→448G
  detail: 每代速率翻倍，Amphenol独家供应GB200 NVLink背板($10K/机柜)；每台GB200连接器成本$15K+，ASP从$100→$1000+，AI服务器连接器价值量远超传统服务器
- title: PCIe 7.0(128 GT/s)连接器2027年
  detail: 速率相比PCIe 6.0翻倍，TE Connectivity和Molex同步推出适配产品
- title: 铜缆DAC/ACC/AEC替代光纤在短距互联
  detail: 铜缆在3米内成本仅为光纤的1/10，延迟更低
- title: 中国立讯精密切入NVLink供应链
  detail: 立讯在224G高速铜缆和背板连接器领域技术突破，从消费电子→AI服务器连接器转型，进入NVIDIA供应链是里程碑
- title: 共封装光学(CPO)长期可能替代部分铜连接
  detail: 但铜连接在<500Gbps/1m场景仍有成本优势，短期铜连接仍是主流（成本/可靠性优势）
price_conduction:
- NVLink带宽每代翻倍（112G→224G→448G），连接器用量和价值量同步增长。Amphenol独家供应GB200 NVLink背板连接器
- 议价能力强
- $10K+/机柜的定价权使得Amphenol利润丰厚
- 但NVIDIA正推动多供应商策略（引入TE Connectivity）以降低成本
- 224G→448G PAM4演进使连接器ASP从$100→$1000+
- Amphenol/TE年涨5-8%
- AI服务器网络成本增加
- 每台GB200连接器成本$15K+。共封装光学(CPO)长期可能替代部分铜连接，但短期铜连接仍是主流（成本/可靠性优势）
wikilinks:
- AI服务器
- 晶圆代工(先进制程)
key_customers:
- AI服务器
companies:
- ticker: AVGO
  name: Broadcom
  role: 概念股
  rev: 5
- ticker: APH
  name: Amphenol
  role: 龙头
  rev: 15
- ticker: TEL
  name: TE Connectivity
  role: 二线弹性
  rev: 12
- ticker: '002475'
  name: Luxshare Precision (立讯精密)
  role: 二线弹性
  rev: 5
- ticker: '002025'
  name: 中航光电
  role: 国产二线
  rev: 25
- ticker: '300602'
  name: 飞荣达
  role: 间接相关
  note: 电磁屏蔽材料（高速铜缆在机柜内产生强EMI），非铜缆连接器制造商；其AI逻辑实际在液冷
  rev: 15
key_inputs:
- 铜合金
- 精密制造
- PCB与IC载板
- 半导体设备零部件
sources:
- title: Amphenol FY2025 Annual Report
  summary: AI数据中心互连业务同比增长60%+，立讯精密收购莱尼加速全球化
  url: ''
- title: 立讯精密2025年报
  summary: ''
  url: ''
- title: Molex/ TE Connectivity FY2025
  summary: ''
  url: ''
- title: LightCounting《AI算力互联报告2025》
  summary: AI集群铜缆连接从DAC向AEC升级，800G/1.6T需求爆发
  url: https://www.lightcounting.com
---

# 高速连接器与铜缆

> **AI算力** · L2 · TAM **$5B** · CAGR **30%**

高速连接器是AI服务器内部**「神经系统」**——芯片间/板卡间传输超高速电信号。GB200 NVL72仅NVLink背板连接器价值$10,000+。信号速率112G→224G→448G演进。|**Amphenol(APH)凭NVLink独家供应成全球连接器龙头**，TE Connectivity+Tesla bot连接器,Molex。中国立讯精密(002475)AI服务器连接器份额快速上升，已进入NVIDIA供应链。|**价值量跃升**：连接器ASP随速率翻倍从$100→$1000+，每台GB200连接器成本$15K+，AI服务器连接器价值量远超传统服务器；信号完整性（SI/PI）成为核心设计挑战。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $5B |
| 年复合增长率(CAGR) | 30% |
| 利润率区间 | 30-45% |
| 成本占比 | 2% (AI服务器)〔半导体口径：3% AI服务器BOM成本〕 |
| 利润池占比 | 2% (AI服务器利润池)〔半导体口径：2% 连接器利润池〕 |
| 附加值 | medium |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从2→6条

### 更新 2026-09-13（合并 semi-high-speed-connector 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-high-speed-connector.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$5B）；本方 cagr 30% 保留（对方 12% 未采纳），margin 30-45% 保留（对方 30-40% 未采纳）
- **口径保留**: cost_share / profit_pool 的半导体口径（3% AI服务器BOM成本 / 连接器利润池）并入 context 备注明细，两个视角并存
- **key_trends**: 4 → 5 条。吸收对方"共封装光学(CPO)长期可能替代部分铜连接（<500Gbps/1m 场景铜仍有成本优势）"独有主题；对方 ASP($100→$1000+)、每台GB200连接器$15K+、"价值量远超传统服务器"并入本方 NVLink 速率条目；"立讯从消费电子→AI转型"并入立讯条目
- **sources**: 3 → 4 条。并入 LightCounting《AI算力互联报告2025》；Amphenol 年报两方同名，保留本方标题并吸收对方 summary（AI互连业务+60%、收购莱尼）
- **companies**: 4 → 6 家。并入 中航光电(002025)、飞荣达(300602)；共有标的（APH/TEL/002475）沿用本方 rev
- **key_inputs**: 2 → 4 条（并入 PCB与IC载板、半导体设备零部件）
- **wikilinks**: 2 条（对方仅 AI服务器，本方已含，无新增）；**key_customers**: 1 条（两方一致）
- **price_conduction**: 4 → 8 条（并入 ASP $100→$1000+、Amphenol/TE年涨5-8%、AI服务器网络成本增加、每台GB200连接器$15K+/CPO替代四条）
- **competition**: Amphenol 条目补入对方份额(~20%)与"独家供应商"，Molex 补入(~10%, Koch Industries)；立讯条目吸收"进入NVIDIA供应链、消费电子→AI转型"；新增 中航光电；**barriers**: 3 → 4 条（补全信号完整性/精密模具的 detail，并入 AI服务器定制连接器）；**tech_gap**: 1 条（将对方"进入NVIDIA供应链、差距3-5年"并入本方维度）
- **YAML 修复**: 原 `key_inputs` 与正文分隔符 `---` 同行，已恢复为标准块格式
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
