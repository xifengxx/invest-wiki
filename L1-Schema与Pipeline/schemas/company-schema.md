# 公司字段规范（company-schema）

每个公司（company）MD 文件的 YAML frontmatter 必须包含以下字段。

## 字段总表

| # | 字段 | 类型 | 必填 | 格式要求 |
|---|------|------|:--:|---------|
| 1 | name | str | ✅ | 公司全称 |
| 2 | slug | str | ✅ | 英文短标识，与文件名一致 |
| 3 | type | str | ✅ | 固定值 `"company"` |
| 4 | country | str | ✅ | 国家/地区 |
| 5 | ticker | str | - | 股票代码 |
| 6 | one_liner | str | ✅ | 一句话公司介绍，50~80字 |
| 7 | description | str | - | 公司简介，≤200字 |
| 7a | core_business | list | - | 核心业务/产品列表，每项20-40字，如 ["EUV光刻机设计制造","DUV光刻机","量测检测设备"] |
| 7b | revenue_model | str | - | 盈利模式，1-2句话，如 "通过设备销售(ASP 3-4亿欧元/台)+长期维护服务合约(年费15-20%)实现盈利" |
| 8 | website | str | - | 公司官网 URL |
| 8a | founded | int | - | 成立年份，如 1984 |
| 8b | headquarters | str | - | 总部所在地，如 "荷兰费尔德霍芬" |
| 8c | employees | str | - | 员工规模，如 "~45,000" |
| 8d | latest_revenue | str | - | 最新财年营收，如 "FY2025 €32.7B" |
| 8e | market_cap | str | - | 当前市值，如 "~$420B" |
| 9 | industry | str | - | 所属产业（AI算力 / 半导体） |
| 10 | segments | list | - | 关联赛道名称数组 |
| 11 | chain_layer | str | - | 产业链层级（L1/L2/L3/L4） |
| 12 | chain_role | str | - | 产业链角色：龙头/核心参与者/直接相关/间接相关 |
| 13 | suppliers | list | - | 上游供应商列表，见子字段 |
| 14 | customers | list | - | 下游客户列表，见子字段 |
| 15 | partners | list | - | 合作伙伴列表，见子字段 |
| 16 | competitors | list | - | 竞争对手列表，见子字段 |
| 17 | updated | str | ✅ | 更新日期，格式 `YYYY-MM` |
| 18 | data_freshness_date | str | ✅ | 数据新鲜度日期，格式 `YYYY-MM`，Phase 3 保鲜机制核心字段 |

---

## 字段详解

### 6. one_liner（一句话公司介绍）

**统一格式**，50~80字，必须覆盖四个要素：

```
{公司定位}，{核心业务}，通过{盈利模式}实现盈利，位于产业链{chain_layer}——{产业链位置描述}
```

**要素说明：**

| 要素 | 说明 | 示例 |
|------|------|------|
| 公司定位 | 公司在行业中的角色和地位 | "全球GPU和AI计算平台领导者" |
| 核心业务 | 公司主要做什么 | "设计AI训练/推理GPU芯片及CUDA软件生态" |
| 盈利模式 | 怎么赚钱 | "通过芯片销售+软件授权+系统方案" |
| 产业链位置 | 在哪个环节、什么角色 | "位于AI算力L3核心产品层" |

**反例（不满足要求）：**
- ❌ "NVIDIA是一家GPU公司" — 缺少盈利模式和产业链位置
- ❌ "全球领先的GPU和AI芯片公司，数据中心GPU市占率>80%" — 缺少盈利模式

**正例：**
```yaml
one_liner: "全球GPU和AI计算平台领导者，设计AI训练/推理GPU芯片及CUDA软件生态，通过芯片销售+软件授权+系统方案实现盈利，位于AI算力L3核心产品层——数据中心GPU市占率>80%"
```

---

### 11. chain_layer

公司在产业链中所处的层级。

| 值 | 含义 |
|----|------|
| L1 | 原材料与资源 |
| L2 | 设备与零部件 |
| L3 | 核心产品与集成 |
| L4 | 终端应用与服务 |

> 一家公司可能涉及多个层级，取**最主要**的层级。

### 12. chain_role

| 值 | 含义 |
|----|------|
| 龙头 | 该环节市占率第一或技术绝对领先 |
| 核心参与者 | 市占率前3或关键技术持有者 |
| 直接相关 | 业务直接覆盖该环节 |
| 间接相关 | 通过供应链间接参与 |

---

### 13. suppliers（上游供应商）

```yaml
suppliers:
  - company: "SK海力士"       # 供应商名称
    ticker: "000660.KS"       # 股票代码（可选）
    supplies: "HBM3E存储芯片"  # 供应的物料/服务
    note: "NVIDIA主力HBM供应商" # 补充说明
```

### 14. customers（下游客户）

```yaml
customers:
  - company: "Microsoft Azure"
    ticker: "MSFT"
    revenue_pct: 20           # 收入占比%，可选
    note: "GPU采购用于AI训练集群"
```

### 15. partners（合作伙伴）

```yaml
partners:
  - company: "台积电"
    ticker: "TSM"
    area: "CoWoS封装"         # 合作领域
    note: "独家先进封装伙伴"
```

### 16. competitors（竞争对手）

```yaml
competitors:
  - company: "AMD"
    ticker: "AMD"
    area: "AI GPU"            # 竞争领域
    note: "MI300X对标H100"
```

---

## 完整示例

```yaml
---
name: "NVIDIA"
slug: "nvidia"
type: "company"
country: "US"
ticker: "NVDA"
one_liner: "全球GPU和AI计算平台领导者，设计AI训练/推理GPU芯片及CUDA软件生态，通过芯片销售+软件授权+系统方案实现盈利，位于AI算力L3核心产品层——数据中心GPU市占率>80%"
description: "全球领先的GPU和AI芯片公司，CUDA生态构建者"
core_business: ["AI训练/推理GPU芯片设计", "CUDA软件生态与AI平台", "数据中心网络互联(NVLink/InfiniBand)", "自动驾驶与边缘AI芯片"]
revenue_model: "通过GPU芯片销售(数据中心占85%)+软件授权(CUDA企业版)+DGX系统方案实现盈利"
founded: 1993
headquarters: "美国加州圣克拉拉"
employees: "~36,000"
latest_revenue: "FY2026 $215.9B"
market_cap: "~$3.3T"
website: "https://www.nvidia.com"
industry: "AI算力"
segments: ["GPU架构设计", "AI服务器", "AI模型训练平台", "自动驾驶", "边缘AI"]
chain_layer: "L3"
chain_role: "龙头"
suppliers:
  - company: "SK海力士"
    ticker: "000660.KS"
    supplies: "HBM3E"
    note: "HBM主力供应商"
  - company: "台积电"
    ticker: "TSM"
    supplies: "CoWoS封装+晶圆代工"
    note: "独家先进制程+封装伙伴"
customers:
  - company: "Microsoft Azure"
    ticker: "MSFT"
    revenue_pct: 20
    note: "AI训练集群GPU采购"
  - company: "Meta"
    ticker: "META"
    revenue_pct: 15
partners:
  - company: "台积电"
    ticker: "TSM"
    area: "CoWoS封装"
    note: "独家先进封装伙伴"
competitors:
  - company: "AMD"
    ticker: "AMD"
    area: "AI GPU"
    note: "MI300X系列对标H100/H200"
  - company: "Intel"
    ticker: "INTC"
    area: "AI加速器"
    note: "Gaudi3对标，但生态差距大"
updated: "2026-07"
---
```

---

## Body 正文模块（4 个 ## 段）

公司 MD 的 YAML 结束后，body 由 4 个可选 `##` 段组成。无数据时保留标题 + `（待补充）`。

### 正文结构

```
# {公司名}

{一句话定位，与 one_liner 互补不重复}

## 财务状况
（最新财年营收、净利、毛利率、市值、近3年趋势）

## 产品线详解
（各产品线收入占比、ASP、主要客户、竞争力分析）

## 技术路线图
（下一代产品时间线、制程迭代计划、研发方向）

## 研发投入与专利
（R&D占比、专利数量、核心技术壁垒）
```

### 渲染规则

- YAML 标量（founded/headquarters/employees/latest_revenue/market_cap）作为快速概览网格显示在「详细信息」卡片顶部
- Body `##` 段经 renderMD() 渲染在网格下方，支持表格、列表、粗体等 Markdown 语法
- 无 body 内容时显示占位卡片，列出待填充的方向
