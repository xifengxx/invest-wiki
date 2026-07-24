# 赛道字段规范（segment-schema）

每个赛道（segment）MD 文件的 YAML frontmatter 必须包含以下字段。字段值被直接编译到 `wiki_data.json`，驱动 L3 前端的 9 个 Detail 模块。

## 字段总表

| # | 字段 | 类型 | 必填 | 格式要求 | 对应模块 |
|---|------|------|:--:|---------|---------|
| 1 | name | str | ✅ | 中文全称 | 页面标题 |
| 2 | slug | str | ✅ | 英文短标识，与文件名一致 | URL 路由 |
| 3 | type | str | ✅ | 固定值 `"segment"` | 类型标识 |
| 4 | industry | enum | ✅ | `AI算力` / `半导体` | 产业标签 |
| 5 | layer | int | ✅ | 1-4，代表产业链层级 | 层级标签 |
| 6 | tam | float | ✅ | 亿美元，纯数字不带单位 | 模块1：市场规模 |
| 7 | cagr | float | ✅ | 百分比数值，纯数字不带 `%` | 模块1：市场规模 |
| 8 | margin | str/null | ✅ | `"X-Y%"` 格式，无数据用 `null` | 模块1：市场规模 |
| 9 | backlinks | int | ✅ | 引用次数，由 parser 自动计算 | 模块1：引用量 |
| 10 | wikilinks | list | ✅ | 赛道名称数组，用于关联关系 | 模块7：关联关系 |
| 11 | description | str | ✅ | ≤500字，用 `\|` 分段落 | 模块2：定位与定义 |
| 12 | cost_share_pct | float/null | - | 成本占比百分比数值 | 模块3：价值链-成本 |
| 13 | cost_share_context | str | - | 如 "AI服务器"、"数据中心TCO" | 模块3：价值链-成本 |
| 14 | profit_pool_pct | float/null | - | 利润池占比百分比数值 | 模块3：价值链-利润 |
| 15 | profit_pool_context | str | - | 如 "AI服务器利润池" | 模块3：价值链-利润 |
| 16 | key_inputs | list | - | 上游赛道名称数组，如 `["HBM高带宽内存","CoWoS先进封装"]` | 模块4：上游输入 |
| 17 | key_customers | list | - | 下游赛道名称数组，如 `["AI服务器","自动驾驶"]` | 模块4：下游客户 |
| 18 | price_conduction | list | - | 传导步骤字符串数组，如 `["步骤1","步骤2⇒步骤3"]` | 模块4：价格传导链 |
| 19 | competition | dict | - | `{global, china, barriers, tech_gap}`，见 field-formats.md | 模块5：竞争格局 |
| 20 | key_trends | list | - | `[{title, detail}]` 对象数组 | 模块6：关键趋势 |
| 21 | sources | list | - | `[{title, summary, url}]` 对象数组 | 模块8：研报与证据 |
| 22 | companies | list | - | `[{ticker,name,role,rev}]` 对象数组 | 模块9：核心标的 |
| 23 | key_inputs_detail | str | - | 预留：上游详细说明 | - |
| 24 | key_customers_detail | str | - | 预留：下游详细说明 | - |
| 25 | value_add | str | - | 附加值等级：high/medium/low | - |
| 26 | contradictions | list/null | - | 矛盾追踪列表，见下方 contradictions 格式 | 矛盾提示卡片 |
| 27 | related_theses | list | - | 关联论点 slug 数组 | 投资论点模块 |

## 字段填充优先级

新增赛道时，按以下优先级填充：
1. **必须有值** (1-11): name, slug, type, industry, layer, tam, cagr, margin, backlinks, wikilinks, description
2. **有则填** (12-18): 从研报/行业数据中提取的量化数据
3. **LLM 生成** (19-21): 需要综合多源信息的分析型字段
4. **自动计算** (9, 18): backlinks 由 parser 计算，wikilinks 从关联分析得出

## 示例

```yaml
---
name: "GPU"
slug: "gpu"
type: "segment"
industry: "AI算力"
layer: 3
tam: 130.0
cagr: 40.0
margin: "65-75%"
backlinks: 6
wikilinks: ["HBM高带宽内存", "AI服务器", "ASIC/AI定制芯片", "FPGA"]
description: "GPU因数千核心并行计算架构..."
cost_share_pct: 55.0
cost_share_context: "AI服务器"
profit_pool_pct: 65.0
profit_pool_context: "AI服务器利润池"
key_inputs: ["HBM高带宽内存", "CoWoS先进封装", "先进制程"]
key_customers: ["云厂商", "AI实验室", "企业AI"]
price_conduction:
  - "NVIDIA每代GPU涨价30-50%（H100 $30K→B200 $40K+）"
  - "AI服务器ASP持续上涨"
  - "云厂商TCO上升，但转嫁能力较强"
competition:
  global:
    - {name: "NVIDIA", share: "86%", note: "CUDA生态锁定"}
    - {name: "AMD", share: "8%", note: "MI300X追赶"}
  china:
    - {name: "华为昇腾", share: "-", note: "国产替代首选"}
  barriers:
    - {item: "CUDA生态锁定", detail: "90%+AI框架基于CUDA"}
  tech_gap:
    - {dimension: "芯片算力", detail: "国产与NVIDIA差距约35x"}
key_trends:
  - title: "NVIDIA Blackwell性能2x+30x推理吞吐"
    detail: "从H100到B200，数据中心营收$193.7B(+68% YoY)"
  - title: "推理市场增速超训练"
    detail: "FP4精度让单卡跑4个70B模型，推理成GPU增长新引擎"
sources:
  - title: "NVIDIA FY2026 Annual Report"
    summary: "数据中心营收$193.7B(+68% YoY)，Blackwell占计算收入88%"
    url: "https://investor.nvidia.com"
  - title: "IFP.org Blackwell Analysis"
    summary: "Blackwell架构深度分析"
    url: "https://ifp.org/..."
companies:
  - {ticker: "NVDA", name: "NVIDIA", role: "全球龙头", rev: 85}
  - {ticker: "AMD", name: "AMD", role: "二线厂商", rev: 35}
contradictions: []
related_theses: []
---
```
