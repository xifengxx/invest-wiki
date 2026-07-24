---
name: CPU(服务器级)
slug: server-cpu
industry: AI算力
layer: L3
tam_bn: 40.0
cagr_pct: 20.0
margin: 50-65%
cost_share_pct: 10
cost_share_context: AI服务器
profit_pool_pct: 5
profit_pool_context: AI服务器利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Intel Xeon
    share: '>65%'
    note: 美国，#1 Clearwater Forest 288核2025年, AMD EPYC
  china:
  - name: ARM阵营：AWS Graviton
    share: 40%+
    note: 占AWS新实例40%+，自研自用
  - name: Ampere
    share: '-'
    note: 美国，192核Oracle部署, NVIDIA Grace
  barriers: []
  tech_gap: []
key_trends:
- title: ARM服务器CPU渗透率从10%向20%+
  detail: AWS Graviton已占亚马逊新实例40%+，NVIDIA Grace+NVLink在AI服务器中占据独特位置
- title: Intel 18A制程2025量产力图逆转颓势
  detail: Clearwater Forest(288核)和Diamond Rapids是Intel反击AMD的关键产品
- title: AMD EPYC Zen 5/Zen 6持续扩大份额
  detail: Turin(192核)和Venice(256核)在核心数上碾压Intel
- title: 中国信创CPU市场快速增长
  detail: 海光(688041,x86兼容)和飞腾(ARM)受益于国产替代政策
- title: Agentic AI驱动CPU:GPU比例从1:4~1:8转向接近1:1
  detail: CPU重回AI数据中心核心，英伟达Vera CPU+NVLink-C2C在AI服务器中占据独特位置，云厂商Capex CAGR 46%直接拉动CPU需求
price_conduction:
- 服务器CPU市场竞争充分（Intel vs AMD vs ARM阵营）
- 任何厂商单方面涨价都会丢失份额
- 客户议价能力强。NVIDIA Grace因与GPU紧耦合（NVLink-C2C）拥有独特溢价能力
- ARM阵营（Graviton/Axion/Ampere）TCO优势
- 长期x86份额承压
- CPU价格总体下行
wikilinks:
- GPU
- AI服务器
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
- AI芯片设计(Fabless)
companies:
- ticker: INTC
  name: Intel
  role: 龙头
  rev: 55
- ticker: AMD
  name: AMD
  role: 龙头
  rev: 30
- ticker: NVDA
  name: NVIDIA
  role: 二线弹性
  rev: 5
key_inputs:
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
sources:
- title: Mercury Research《Server CPU Q4 2025》
  summary: ''
  url: ''
- title: SemiAnalysis《CPUs are Back 2026》
  summary: ''
  url: https://www.semianalysis.com
- title: AMD FY2025 Earnings
  summary: ''
  url: ''
- title: Intel FY2025
  summary: ''
  url: ''
---

# CPU(服务器级)

> **AI算力** · L3 · TAM **$40B** · CAGR **20%**

服务器CPU是数据中心的**通用计算大脑**——运行OS、管理内存、调度任务和协调加速器。**Agentic AI训练让CPU重回数据中心核心**：RL训练循环需大量CPU做编译+验证+Tool Use。|**x86双雄：Intel Xeon(~59-71%单位份额,但AMD EPYC收入份额首破41.3%**)。AMD Turin 192核(3nm)vs Intel Granite Rapids 128核。AMD ASP是Intel 2x。2026双方均涨价(Intel 8-10%,AMD 16-17%)。|**ARM阵营快速增长(13-16%份额)**：AWS Graviton(2M+颗,30-40%性价比优势)、NVIDIA Grace(2025出货~2.5M颗,2x perf/watt vs x86)、Ampere(SoftBank收购)。ARM目标2030年40%份额。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $40B |
| 年复合增长率(CAGR) | 20% |
| 利润率区间 | 50-65% |
| 成本占比 | 10% (AI服务器) |
| 利润池占比 | 5% (AI服务器利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22
> 来源: [[消化笔记/2026-07-22-v1.1-中原证券电子行业中期策略]]
> 置信度: 高

- **cagr**: 10% → 20%
- **key_trends**: +1条 "Agentic AI驱动CPU:GPU比例从1:4~1:8转向接近1:1——CPU重回AI数据中心核心"
- **依据**: 中原证券2026中期策略——Agentic AI时代CPU承担相当比重工作负载，CPU:GPU比例从1:4~1:8转向接近1:1，云厂商Capex CAGR 46%
### 更新 2026-07-22 (v1.2)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→9条
