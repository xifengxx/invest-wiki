---
name: HBM高带宽内存
slug: hbm-memory
industry: AI算力
layer: L2
tam_bn: 55.0
cagr_pct: 40.0
margin: 50-60%
cost_share_pct: 20
cost_share_context: AI服务器BOM(GPU+HBM)
profit_pool_pct: 15
profit_pool_context: HBM属于DRAM中利润率最高产品，三巨头垄断定价权强
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: SK Hynix
    share: 62%
    note: 韩国，HBM3E独家供NVIDIA，HBM4首批量产，2026年预订$17.1B售罄
  - name: Micron
    share: 21%
    note: 美国，2025放弃消费DRAM全力转HBM，12-high HBM3E通过验证，HBM4被Rubin排除
  - name: 三星
    share: 17%
    note: 韩国，HBM3E验证延迟从41%暴跌，2025年9月勉强通过验证仅获万颗订单，HBM4获Rubin独家二供资格
  china:
  - name: CXMT长鑫存储
    share: '-'
    note: DDR5量产，HBM研发中，差距5-7年
  barriers:
  - item: TSV硅通孔
    detail: 10μm级精度，仅三家掌握
  - item: 堆叠键合
    detail: 12→16层工艺跃迁，良率门槛极高
  - item: 客户认证
    detail: 2年+周期，NVIDIA主导认证标准
  - item: 散热管理
    detail: 堆叠越高散热越难，Hybrid Bonding是关键
  tech_gap:
  - dimension: SK Hynix在HBM3E领先三星至少1代。HBM4 2H26量产带宽>2TB/s。NVIDIA Vera Rubin选三星+SK Hynix独家供应HBM4，Micron被排除出初始分配
    detail: HBM4供应格局重大变化
key_trends:
- title: HBM4 2H26量产，三星获Rubin二供资格
  detail: NVIDIA Vera Rubin选定SK Hynix+三星独家供HBM4，Micron被排除，三星借HBM4逆袭机会
- title: HBM3E 2026年合约涨20%，三巨头全部售罄
  detail: SK Hynix 2026预订$17.1B(+39% YoY)，HBM占DRAM收入33%且持续提升
- title: ASIC客户驱动HBM需求多元化
  detail: Amazon Trainium/Google TPU/Broadcom ASIC 2026年占HBM需求33%(2025仅15%)，减少对NVIDIA单一客户依赖
- title: Micron放弃消费DRAM全面转AI/HBM
  detail: 2025年12月停产Crucial品牌，2026年$200B Capex，但HBM4被Rubin排除是重大打击
- title: 中国CXMT DDR5量产但HBM差距5-7年
  detail: TSV+混合键合技术壁垒极高，短期内无法自主供应HBM
price_conduction:
- HBM3E 2026合约涨20%+三巨头全部售罄
- GPU产能受HBM供给约束（NVIDIA单卡需6-8颗HBM）
- AI服务器交付延迟+ASP上涨
- 云厂商被迫提前1年锁定订单。HBM每涨10%
- AI服务器总成本增2%
- 云厂商转嫁（AI服务按Token涨价）。HBM4 2H26量产后三星加入供应
- 供给紧张可能边际缓解但初期良率低产能有限
wikilinks:
- GPU
- AI服务器
- AI模型训练平台
- 先进封装CoWoS
- ASIC/AI定制芯片
key_customers:
- GPU
- AI服务器
companies:
- ticker: MU
  name: Micron
  role: 二线弹性
  rev: 25
- ticker: '000660'
  name: SK Hynix
  role: 龙头
  rev: 35
- ticker: 005930
  name: Samsung
  role: 二线弹性
  rev: 10
- ticker: CXMT
  name: CXMT (长鑫存储)
  role: 概念股
  rev: 10
- ticker: '2344'
  name: Winbond (华邦)
  role: 概念股
  rev: 5
- ticker: '2408'
  name: Nanya(南亚科)
  role: 概念股
  rev: 10
key_inputs:
- 先进封装CoWoS
sources:
- title: Counterpoint Global HBM Market Share Q2 2025
  summary: ''
  url: https://counterpointresearch.com
- title: TrendForce HBM Demand from ASICs Jul 2025
  summary: ''
  url: https://www.trendforce.com
- title: SK Hynix FY2025 Earnings
  summary: ''
  url: ''
- title: Micron FY2025 Earnings
  summary: ''
  url: ''
- title: Bank of America HBM TAM Analysis 2026
  summary: ''
  url: ''
- title: KB Securities HBM4 Revenue Forecast 2026
  summary: ''
  url: ''
- title: NVIDIA Vera Rubin HBM4 Supplier Announcement Mar 2026
  summary: ''
  url: ''
- title: The Elec Samsung HBM3E Qualification Sep 2025
  summary: ''
  url: ''
---

# HBM高带宽内存

> **AI算力** · L2 · TAM **$55B** · CAGR **40%**

HBM通过**硅通孔（TSV）技术垂直堆叠多层DRAM芯片**，带宽比DDR5高10-20倍。NVIDIA H100使用6颗HBM3提供3.35TB/s带宽，B200升级至192GB HBM3E。|**全球仅三家供应商，2026年全部售罄**——SK Hynix(62%)2026年产能$17.1B预订(+39%)独家供应NVIDIA HBM3E；Micron(21%)2025年放弃消费DRAM全面转HBM；三星(17%)因HBM3E验证延迟从2024年41%份额暴跌。|**HBM4 2H26量产，NVIDIA Vera Rubin选定三星+SK Hynix独家供应，Micron被排除出初始分配**。HBM3E合约价2026涨20%。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $55B |
| 年复合增长率(CAGR) | 40% |
| 利润率区间 | 50-60% |
| 成本占比 | 20% (AI服务器BOM(GPU+HBM)) |
| 利润池占比 | 15% (HBM属于DRAM中利润率最高产品，三巨头垄断定价权强) |
| 附加值 | high |

## 关联

- 下游: [[GPU]]
- 下游: [[AI服务器]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→7条
