# Invest Wiki 知识库设计文档

> 版本 2.4 · 2026-07-24 · LLM-Wiki 四层架构 + Phase 2-5 全部完成

---

## 一、背景与动机

### 1.1 项目起源

Invest Wiki 的前身是 `invest_kg`——一个基于 JSON → SQLite 的产业链知识图谱。数据通过 `engine/seed_json_to_md.py` 一次性迁移为 Markdown 词条后，暴露出三个问题：

1. **数据是快照，不是活系统**：种子导入后没有持续更新的机制，行业数据随时间过期。
2. **LLM 操作没有规范**：修改赛道字段全靠人工判断，复杂字段格式容易出错。
3. **没有健康检查**：无法自动发现数据矛盾、过期引用、孤立页面。

### 1.2 为什么是四层

标准 LLM-Wiki 是三层（Raw Sources / Schema / Wiki），但 Invest Wiki 的 Wiki 层包含 20+ 结构化 YAML 字段、需要编译为 JSON 再驱动前端——所以插入 L2 结构化层和 L3 编译输出层：

```
Karpathy 三层          Invest Wiki 四层
─────────────          ────────────────
Raw Sources      →     L0 原始资料层
The Schema       →     L1 Schema & Pipeline 层
The Wiki         →     L2 结构化 Wiki 层
  (无对应)       →     L3 网页产物层
```

### 1.3 设计目标

1. 从快照变成活系统——新研报/新闻按规范自动更新
2. LLM 操作有法可依——字段有精确的类型和格式约束
3. 数据健康可监控——Lint 定期扫描矛盾、过期、孤立
4. 前端交互式查询——7 页面 SPA + 4 图视图 + 全局搜索 + 排序/筛选

---

## 二、数据全景

### 2.1 规模（2026-07-24）

| 类型 | 数量 |
|------|:--:|
| 产业 | 2（AI算力 / 半导体） |
| 赛道（segment） | 74 |
| 公司（company） | 392（78家深度覆盖 + 312家骨架 + 2家中等） |
| 概念卡片（concept） | 10 |
| 投资论点（thesis） | 18 |
| **总词条** | **496** |
| 图谱节点 | 470 |
| 图谱边 | 249 |
| L0 归档文件 | 16 |

### 2.2 两大产业 · 四层结构

- **AI算力**（40 赛道）：L4 终端应用(8) / L3 核心产品(12) / L2 设备与组件(15) / L1 原材料(5)
- **半导体**（34 赛道）：L4 终端应用(7) / L3 核心产品(8) / L2 设备与组件(11) / L1 原材料(8)

层级逻辑：L1 原材料 → L2 设备/组件 → L3 核心产品 → L4 终端应用。下层为上层提供输入。

### 2.3 排序算法

```
综合分 = TAM_bn ÷ max(TAM) × 60 + backlink_count ÷ max(backlinks) × 40
```

---

## 三、完整目录结构

```
invest_wiki/
├── CLAUDE.md                              ← 项目入口 + 路线图 + 当前状态
├── ARCHITECTURE.md                        ← 本文件（架构设计文档）
├── UI_DESIGN.md                           ← 前端设计规范（CSS令牌/组件/交互）
├── .gitignore                             ← 排除 .DS_Store/__pycache__/.bak/.aura/
│
├── L0-原始资料池/                          ← Raw Sources（LLM 只读不写）
│   ├── 01-研报/                            ← 券商/研究机构报告
│   ├── 02-财报/                            ← 季报/年报/Earnings Call
│   ├── 03-新闻/                            ← 行业新闻/公司公告/Web调研溯源
│   └── 04-行业数据/                        ← TrendForce/IDC/Gartner/市场报告
│
├── L1-Schema与Pipeline/                   ← Schema & Pipeline（操作规范层）
│   ├── CLAUDE.md                          ← LLM 操作宪法（每次操作前必读）
│   ├── schemas/                           ← 数据字段规范
│   │   ├── segment-schema.md              ← 赛道 22 字段
│   │   ├── company-schema.md              ← 公司 18 字段 + Body 5 模块
│   │   ├── concept-schema.md              ← 概念卡片 14 字段 + 11 模块
│   │   ├── thesis-schema.md               ← 投资论点 YAML + Body 6 模块
│   │   └── field-formats.md               ← 特殊字段格式规范（competition/key_trends/sources）
│   ├── templates/                         ← 新建实体模板
│   │   ├── segment-template.md            ← 赛道模板
│   │   ├── company-template.md            ← 公司模板（YAML 18字段 + Body 5模块）
│   │   ├── concept-template.md            ← 概念卡片模板
│   │   ├── thesis-template.md             ← 论点模板
│   │   └── digest-template.md             ← 消化笔记模板
│   ├── collector/                         ← Ingest 采集 Skill（Collection 模式）
│   │   ├── SKILL.md                       ← 技能规格说明
│   │   └── 执行指令-采集处理.md             ← LLM 执行指令（Step 0→8）
│   ├── lint/                              ← Lint 健康扫描 Skill（Refinement 模式）
│   │   ├── SKILL.md                       ← 技能规格说明
│   │   └── 执行指令-定期扫描.md             ← LLM 执行指令（四维扫描）
│   ├── link-enrich/                       ← 链接增强 Skill
│   │   ├── SKILL.md                       ← 技能规格说明
│   │   └── 执行指令-链接增强.md             ← LLM 执行指令
│   └── concept-card/                      ← 概念卡片科普 Skill
│       ├── SKILL.md                       ← 寓言提示法 + 11 模块科普
│       └── 功能说明.md                     ← 功能说明
│
├── L2-Wiki/                               ← 结构化 Wiki 层（核心数据层）
│   ├── index.md                           ← 74 赛道总索引（LLM 查询路由入口）
│   ├── 产业/                               ← AI算力.md / 半导体.md
│   ├── 赛道/                               ← AI算力/(40md) + 半导体/(34md)
│   ├── 公司/                               ← 392 个公司 MD（78深度+312骨架+2中等）
│   ├── 概念/                               ← 10 个概念卡片 MD
│   ├── 论点/                               ← 18 个投资论点 MD + 审计报告
│   └── 消化笔记/                           ← L0→L2 中间产物（逐字段影响评估）
│
├── L3-网页产物/                            ← Web Output（编译输出层）
│   ├── index.html                         ← 单文件 SPA（7页面 + 全局搜索）
│   ├── wiki_data.json                     ← 编译中间数据（~1.6MB）
│   ├── build_wiki_data.py                 ← L2→L3 编译脚本
│   ├── validate.py                        ← 格式验证（HTML/JSON/函数）
│   └── freshness_scan.py                  ← Phase 3 数据新鲜度扫描器
│
└── engine/                                ← Wiki 引擎库
    ├── __init__.py                        ← 包初始化
    ├── parser.py                          ← YAML + [[wikilink]] 解析引擎
    ├── graph.py                           ← ECharts 图数据构建（Treemap/Graph/Sankey）
    └── seed_json_to_md.py                 ← 一次性种子导入（已归档，不再使用）
```

### 各层职责

| 层 | 谁操作 | 做什么 | 工具 |
|----|--------|------|------|
| L0 | LLM（只读不写） | 存放原始研报/财报/新闻，收集入口 | Write 创建归档 |
| L1 | 人类 + LLM | 定义数据格式规范、采集/检查工作流、模板 | Read + Edit 维护规范 |
| L2 | LLM（按 Schema） | 结构化 YAML 词条，编译为 L3 的数据源 | Edit 逐段修改 |
| L3 | Python 脚本 | 编译 L2 → JSON → HTML，自动化验证 | python3 执行 |

---

## 四、L0 — 原始资料层

### 4.1 定位

LLM **只读不写**。所有外部来源先归档到这里，再进行后续处理。禁止删除，只能标记 `status: 已处理`。

### 4.2 目录映射

| 目录 | 来源类型 | 文件命名格式 |
|------|---------|------------|
| `01-研报/` | 券商/研究机构报告 | `YYYY-MM-DD-标题-机构.md` |
| `02-财报/` | 季报/年报/Earnings Call | `YYYY-MM-DD-公司-财务数据.md` |
| `03-新闻/` | 行业新闻/公司公告/Web调研 | `YYYY-MM-DD-主题-类型.md` |
| `04-行业数据/` | TrendForce/IDC/Gartner | `YYYY-MM-DD-主题.md` |

### 4.3 归档文件格式

```yaml
---
input_id: input_YYYYMMDD_NNN
date: YYYY-MM-DD
source_type: 研报 | 财报 | Web调研 | WebFetch
source_name: "来源描述"
source_url: "URL 或 '多源（见正文）'"
ingest_date: YYYY-MM-DD
status: 待处理 | 已处理
tags: [标签列表]
data_as_of: YYYY-MM-DD
confidence: 高 | 中 | 低
---

# 标题

## 搜索记录 / 原文摘要
[Web调研: 搜索词 + 有效URL列表 / 研报: LLM提取的摘要]

## 数据提取清单
| 数据点 | 值 | 来源 URL | 置信度 |

## 被拦截/失败记录
| URL | 错误类型 | 时间 |

## Schema-Mapping（待处理）
| 原文 | L2目标 | 字段 | 置信度 |
```

### 4.4 内容抓取策略

| 场景 | 工具 | 说明 |
|------|------|------|
| 普通网页 | WebFetch(url) | 首选 |
| 微信公众号（mp.weixin.qq.com） | `web-content-fetcher` skill Scrapling 路径 | WebFetch/Jina/curl 均被拦截 |
| JS 渲染页面（富途等） | 浏览器 CDP | 如 Scrapling 也失败 |

### 4.5 L0 归档硬规则

- 调用 `Edit` 或 `Write` 修改任何 L2 MD 之前，必须先确认对应 L0 归档文件已存在磁盘
- L0 不存在 → **立即停止，先创建 L0，再继续 MD 编辑**
- 创建 L0 时必须对照目录映射表选择正确子目录，写错目录等同于未归档
- 禁止 WebSearch 后跳过 L0 直接写入 L2

---

## 五、L1 — Schema & Pipeline 层

### 5.1 操作宪法（CLAUDE.md）

LLM 每次操作 Wiki 前必读。包含 10 条核心规则、四层信息流 8 步骤、禁止操作清单、触发规则路由表、三种维护模式、L0 归档规范、内容抓取策略。

### 5.2 信息流（8 步骤）

```
Step 0: 完整读取原始资料 + 7项QA自检 → QA通过
  → Step 1: L0归档 + Schema-Mapping表
  → Step 2: 实体提取（与 L2 已有实体精确匹配）
  → Step 3: 消化笔记（逐字段影响评估 + 置信度标记）
  → Step 4: 输出更新建议 → 等待用户确认
  → Step 5: 执行更新（YAML 字段 + 动态更新记录 + 回写 L0/消化笔记 status）
  → Step 6: 更新 index.md 索引 + 维护记录
  → Step 7: 重新编译 wiki_data.json + 验证输出
  → Step 8: 前端验证
```

### 5.3 三种操作模式

#### Collection 模式（采集）

**触发**：用户发送新资料 / "处理" / "归档" / "更新知识库"

**8 步骤**（详见 `collector/执行指令-采集处理.md`）：
- Step 0: 完整读取原始资料全部页面 + 7项QA自检（页数/章节/图表/数字/实体/判断句），QA不通过禁止继续
- Step 1: L0归档 + Schema-Mapping（原文原句→赛道/公司/概念/论点字段）
- Step 2: 实体提取（与 L2 已有实体精确匹配，精确>模糊>新建候选）
- Step 3: 消化笔记（逐字段影响评估：当前值 vs 建议值 vs 置信度）
- Step 4: 更新建议 + 确认（输出汇总表，等待用户确认）
- Step 5: 执行更新（修改 YAML → 追加动态更新记录 → 回写 L0 status: 已处理 → 回写消化笔记 status: 已应用）
- Step 6: 更新 index.md 索引统计/维护记录/QA版本号
- Step 7: 重新编译 wiki_data.json + 验证
- Step 8: 前端验证

**产出**：L0归档文件（含QA+Schema-Mapping） / 消化笔记 / 赛道字段更新 / 新概念卡片 / 新论点 / index.md更新

**前置必读**：`schemas/field-formats.md` + `segment-schema.md` + `company-schema.md` + `concept-schema.md` + `thesis-schema.md`

#### Research 模式（多Agent Web调研）

**触发**："调研XX赛道" / "research XX" / "补充XX数据" / 赛道完整度<50%且无待处理研报

**执行步骤**：
1. 诊断缺口——运行数据完整度扫描
2. 启动 Workflow——3 个搜索 Agent 并行（行业报告/供应链/技术趋势不同角度）
3. L0 归档（强制）——每个搜索 Agent 的原始结果必须先行归档
4. Judge Schema 映射——交叉验证三方结果，取最可信来源，标记冲突
5. 质量检查——data_conflicts、sources 可追溯、confidence
6. 写入 Wiki——Judge 结果经格式化写入 L2 MD，引用 L0 input_id
7. 编译 + 验证

#### Refinement 模式（提炼/审计）

**触发**：每 5 次 Collection 后 / 用户说"提炼"/"审计" / Lint 发现≥5个严重问题

**执行步骤**：
1. 运行完整 Lint 四维扫描
2. 审核所有 thesis：status 变更 + confidence 调整
3. 解决所有 unresolved contradictions
4. 运行链接增强，目标平均链接数≥5/赛道
5. 检查孤立页面（backlinks=0）
6. 检查无匹配内容池（L0 Schema-Mapping 累积）
7. 更新 index.md 统计 + QA 版本号 + 维护记录
8. 重新编译 + 输出 Refinement 报告

### 5.4 Lint 健康检查

**四维扫描**：

| 维度 | 检测内容 | 示例 |
|------|---------|------|
| 矛盾 | TAM 冲突（差值>20%）、wikilink 指向不存在的页面、同公司角色矛盾 | `GPU.tam`: 值 vs 消化笔记中值不一致 |
| 过期 | sources 最新引用>12月、key_trends 含过时年份、文件>6月未更新 | 某赛道 sources 最新为 2025 年 |
| 孤立 | backlinks=0 的赛道、未出现在任何赛道 companies 中的公司 | 某赛道无人引用 |
| 格式 | competition 是否为 dict、key_trends 是否为 [{title,detail}] 数组 | 某赛道仍为旧格式 string |

**严重度分级**：🔴 严重（立即修复）/ 🟡 警告（近期处理）/ 🟢 提示（可选）

**矛盾持久化**：Lint 检测到的矛盾写回赛道 MD 的 `contradictions` YAML 字段，前端渲染琥珀色卡片。

### 5.5 Schema 体系

| Schema | 覆盖 | YAML字段 | Body模块 |
|------|------|:--:|:--:|
| segment-schema | 赛道 | 22 | — |
| company-schema | 公司 | 18 | 5（财务状况/融资与现金流/产品线详解/技术路线图/研发投入与专利） |
| concept-schema | 概念卡片 | 14 | 11（科普模块） |
| thesis-schema | 投资论点 | 10 | 6（核心主张/支撑证据/反对证据/待验证假设/关联赛道/关联论点） |
| field-formats | 特殊格式 | — | competition(key:dict) / key_trends(array) / price_conduction(array) / sources(array) |

**Segment Schema 22 字段**（驱动 L3 赛道详情页 11 模块）：

| # | 字段 | 类型 | 必填 | 对应 L3 模块 |
|---|------|------|:--:|------------|
| 1-3 | name / slug / type | str | ✅ | 页面标题/路由/类型标识 |
| 4 | industry | enum | ✅ | 产业标签（AI算力/半导体） |
| 5 | layer | int | ✅ | 层级标签（1-4） |
| 6-7 | tam_bn / cagr_pct | float | ✅ | 模块1：市场规模 |
| 8 | margin | str/null | ✅ | 模块1：利润率 |
| 9 | description | str | ✅ | 模块2：定位与定义 |
| 10-11 | cost_share_pct / cost_share_context | float/str | — | 模块3：成本占比 |
| 12 | profit_pool_pct | float | — | 模块3：利润池占比 |
| 13-14 | key_inputs / key_customers | list | — | 模块4：上下游 |
| 15 | price_conduction | list[string] | — | 模块4：传导链 |
| 16 | competition | dict | — | 模块5：竞争格局 |
| 17 | key_trends | list[{title,detail}] | — | 模块6：关键趋势 |
| 18 | sources | list[{title,summary,url}] | — | 模块8：研报证据 |
| 19 | companies | list | — | 模块9：核心标的 |
| 20 | contradictions | list | — | 模块2.5：已知矛盾 |
| 21 | wikilinks | list | ✅ | 模块7：关联关系 |
| 22 | related_theses | list | — | 模块10：投资论点 |

**Company Schema 18 YAML 字段**（驱动 L3 公司详情页 8 模块）：

| # | 字段 | 类型 | 说明 |
|---|------|------|------|
| 1-5 | name / slug / country / ticker / type | str | 基础标识 |
| 6 | updated | str | 更新日期 YYYY-MM |
| 7 | data_freshness_date | str | Phase 3 数据新鲜度日期 |
| 8 | segments | list | 关联赛道名称数组 |
| 9 | one_liner | str | 50-80字公司定位介绍 |
| 10 | chain_layer | str | L1-L4 产业链层级 |
| 11 | chain_role | str | 龙头/核心参与者/直接相关/间接相关 |
| 12 | suppliers | list[{company,ticker,supplies,note}] | 上游供应商 |
| 13 | customers | list[{company,ticker,revenue_pct,note}] | 下游客户 |
| 14 | partners | list[{company,ticker,area,note}] | 合作伙伴 |
| 15 | competitors | list[{company,ticker,area,note}] | 竞争对手 |
| 16 | core_business | list[string] | 核心业务/产品列表 |
| 17 | revenue_model | str | 盈利模式描述 |
| 18 | founded / headquarters / employees / latest_revenue / market_cap / description / website / industry | 基本信息 |

**Thesis YAML 字段**：

| # | 字段 | 类型 | 说明 |
|---|------|------|------|
| 1-3 | name / slug / type | str | 基础标识 |
| 4 | thesis_status | enum | forming / active / confirmed / invalidated |
| 5 | confidence | int | 1-10 |
| 6-7 | created / updated | str | 日期 |
| 8-9 | affected_segments / affected_companies | list | 关联赛道/公司 |
| 10 | tags | list | 标签 |

**Thesis Body 6 模块**：## 核心主张 / ## 支撑证据 / ## 反对证据 / ## 待验证假设 / ## 关联赛道 / ## 关联论点

**证据格式规范**（`field-formats.md` §7）：
```
1. 证据内容描述
   ——来源: 来源标题
   (URL)
```
每条证据 3 行：内容 / `——来源:` 行 / `(链接)` 行。无链接省略第 3 行。

### 5.6 其他 L1 组件

**link-enrich（链接增强）**：逐赛道检查 wikilinks 遗漏（同层竞争、上下游依赖、技术替代、协同互补），补充缺失的双向链接。目标：平均链接数≥5/赛道，孤立赛道<10。

**concept-card（概念卡片）**：使用「寓言提示法（Fable Prompting）」将抽象概念转化为生活化叙事，输出 11 模块完整概念卡片（一句话解释→生活类比→专业定义→市场关注原因→产业链位置→相关公司→投资关注点→风险提示→真伪鉴别→追踪指标→关联概念）。

### 5.7 公司 MD 更新规则（防数据丢失）

更新已有公司的 YAML frontmatter 或 body 内容时，**禁止** `Read` → 修改 → `Write` 整文件覆盖。必须用 `Edit` 定位到具体段落进行替换。原因：Write 容易误删 body 中已有的产品线详解、技术路线图、研发投入等独立章节。仅新建公司时可用 Write。

### 5.8 设计借鉴：Obsidian 五要素

| # | 借鉴点 | Invest Wiki 落地 |
|:--:|------|------|
| 1 | Index 索引页 | `L2-Wiki/index.md` — 74 赛道按产业/层级排列 |
| 2 | 链接密度提升 | link-enrich Skill + 公司↔赛道双向链接 |
| 3 | 矛盾持久化 | YAML `contradictions` 字段 + L3 琥珀色卡片渲染 |
| 4 | 投资论点系统 | 18 条论点 + status/confidence + 季度审计闭环 |
| 5 | 双模式维护 | Collection ↔ Refinement 循环 + QA 版本追踪 |

### 5.9 与 AI投研助手 的关系

| 维度 | AI投研助手 | Invest Wiki |
|------|-----------|-------------|
| 研究对象 | 个股（公司档案、财务诊断、估值） | 产业链（赛道、上下游、竞争格局） |
| 知识粒度 | 定性为主 | 定量为主（TAM/CAGR/利润率/份额） |
| 信息流 | 管道式 | 管道式 + 编译管线（L2→JSON→HTML） |
| 输出形式 | 每日看板 / 股票分析卡 | 实时交互式 SPA（7页面+4图视图） |
| 维护模式 | Collection + 复盘 | Collection + Research + Refinement |

---

## 六、L2 — 结构化 Wiki 层

### 6.1 定位

Invest Wiki 的核心数据层。每个文件包含 YAML frontmatter + Markdown 正文 + 动态更新记录。Parser 引擎解析这些文件 → 编译为 wiki_data.json → 驱动 L3 前端渲染。

### 6.2 动态更新记录

每次 Collection/Research 更新后，追加到文件末尾确保审计可追踪：

```markdown
## 动态更新记录

### 更新 YYYY-MM-DD
> 来源: [[消化笔记/YYYY-MM-DD-主题]]
> 置信度: 高

- **字段名**: 旧值 → 新值
- **依据**: 来源描述
```

### 6.3 排名算法

```
综合分 = TAM_bn ÷ max(TAM) × 60 + backlink_count ÷ max(backlinks) × 40
```

---

## 七、L3 — 网页产物层

### 7.1 编译管线

```
L2-Wiki/**/*.md
  → engine/parser.py（解析 YAML frontmatter + 提取 [[wikilink]] + 计算 backlinks）
  → engine/graph.py（构建 Treemap / Graph / Sankey 数据）
  → build_wiki_data.py（合并所有实体 → wiki_data.json，~1.6MB）
  → index.html（fetch wiki_data.json → 前端 SPA 渲染）
```

### 7.2 build_wiki_data.py

编译脚本，读取 L2-Wiki 下所有 MD 文件，调用 engine/parser.py 解析，调用 engine/graph.py 构建图数据。按 entity_type 分派到 `company_to_dict()` / `segment_to_dict()` / `concept_to_dict()` / `thesis_to_dict()` 四个序列化函数。输出 `wiki_data.json` 包含：`entities`（496实体）/ `by_type` / `treemap_ai` / `treemap_semi` / `graph` / `sankey_ai` / `sankey_semi` / `hot` / `thesis_index`。

### 7.3 validate.py

格式验证脚本，检查：HTML 结构（div 平衡/script 平衡）、数据完整性（词条数/赛道数/热力图/unknown 实体）、JS 关键函数存在性（buildTree/renderView/openDetail/closeDetail/doSearch）。

### 7.4 freshness_scan.py

Phase 3 数据新鲜度扫描器。读取 wiki_data.json，检查所有公司的 `data_freshness_date` 字段，按 90 天阈值标记过期，按 60 天阈值标记预警。支持 `--days` 自定义阈值、`--json` 输出。财报季（1/4/7/10月）自动提醒。

### 7.5 前端功能

**7 个导航页面**：产业链图谱 / 赛道分析 / 个股关联 / 概念卡片 / 论点 / 知识库 / 可视化图谱

**个股关联页面（Phase 5）**：
- 排序：市值↓↑ / 名称 A-Z / 引用数↓
- 筛选：国家（10个选项）+ 产业链层级（L1-L4）
- 数据新鲜度可视化：卡片标题旁绿点(≤30天)/橙点(31-90天)/红点(>90天)
- 市值直接在 Ticker 行显示

**4 个图表视图**：Treemap（面积=TAM，颜色=层级）/ 关系网络（力导向图，节点=赛道，连线=wikilink）/ Sankey（价值链流转）/ 因果传导

**赛道详情页**：11 个模块（市场规模/定位定义/已知矛盾/价值链/上下游传导/竞争格局/关键趋势/关联关系/研报证据/核心标的/投资论点）

**公司详情页**：8 个模块（Header→公司介绍→详细信息→产业链定位→上下游关系图谱→竞争格局→关联赛道→关联论点）。Title 右侧显示 `data_freshness_date` 绿点徽章。

**论点详情页**：核心主张（蓝框）+ 支撑证据（绿标）+ 反对证据（红标）+ 待验证假设（黄标）+ 来源。

**知识库仪表盘**：统计面板 + 四级知识树 + 内容面板 + 知识流水线 + 复盘验证引擎（六维质量+论点状态分布+论点列表）。

**全局搜索**：Topbar 居中胶囊搜索框，200ms 防抖，实时下拉匹配，键盘导航。

**7.6 单文件部署**：`index.html` 零依赖，Tailwind CSS CDN + ECharts CDN + `fetch('wiki_data.json')`。

---

## 八、Engine — Wiki 引擎库

### 8.1 parser.py

`WikiParser` 类：遍历 L2-Wiki 目录 → `_parse_file()` 逐文件解析 YAML frontmatter → 提取 `[[wikilink]]` → 创建 `Entity` 对象 → `_compute_backlinks()` 计算反向引用。自动排除：`消化笔记/`、`.aura/`、`__pycache__/`、`index.md`（根目录）、`*audit*` 文件名。

### 8.2 graph.py

`GraphBuilder` 类：从 entities 构建 Treemap（按 layer 着色、TAM 值算面积）、力导向图（节点=实体，边=wikilinks+company→segment+thesis→company）、Sankey 图（segment→segment 流向）。

---

## 九、完整信息流

```
用户发送新资料（PDF / URL / 文本）
  → L0：LLM 识别格式 → 判断目录 → 归档到 L0 → 生成 YAML 头
  → L1 collector Step 2：LLM 提取实体 → 与 L2 已有匹配
  → L1 collector Step 3：LLM 写消化笔记 → 逐字段评估 → 置信度标记
  → L1 collector Step 4：LLM 列出建议更新表格 → 等待用户确认
  → 用户确认
  → L2：LLM 更新 YAML 字段 → 追加 ## 动态更新记录 → 回写 L0 status
  → L3 编译：Python parser → graph → wiki_data.json → index.html
  → 用户浏览器：7 页面 + 4 图视图 + 全局搜索 + 排序筛选
  → 定期触发 L1/lint → 发现问题 → 触发重新 Ingest
```

三种操作模式闭环：

| 操作 | 触发方式 | 执行者 | 产出 |
|------|---------|--------|------|
| **Collection** | 用户发资料 / "处理" | LLM 按 collector 执行指令（Step 0→8） | L0归档 + 消化笔记 + L2更新 |
| **Research** | "调研XX" / "补充数据" | LLM 多Agent Web调研 + Judge | L0归档 + L2 MD + 验证 |
| **Lint/Refinement** | "检查知识库" / 5次Collection后 | LLM 按 lint 执行指令 | 健康报告 + 矛盾解决 + 论点审计 |

---

## 十、路线图

| Phase | 内容 | 状态 |
|-------|------|:--:|
| Phase 2 Tier 1 | 51 家半导体/AI 龙头 + 3 家新建 | ✅ 完成（2026-07-23） |
| Phase 2 Tier 2 | 26 家产业链关键环节龙头 | ✅ 完成（2026-07-23） |
| Phase 3 | 数据保鲜机制（freshness_scan + schema 字段 + UI 徽章） | ✅ 完成（2026-07-23） |
| Phase 4 | 论点闭环审计（18 条：3 confirmed + 9 active + 4 forming + 2 新） | ✅ 完成（2026-07-24） |
| Phase 5 | 前端可用性（排序/筛选/新鲜度可视化） | ✅ 完成（2026-07-24） |
| Tier 3 | 其余 312 家骨架公司 | 按需补充 |

---

## 十一、设计决策

| 决策 | 理由 |
|------|------|
| 四层而非三层 | 产业链数据需要独立的 Schema 层 + 编译输出层 |
| YAML frontmatter 而非纯 MD | 20+ 字段需要机器可解析格式直接驱动前端渲染 |
| 追加式更新 + 动态更新记录 | 保持审计轨迹，不覆盖原文 |
| 单文件 SPA（index.html） | 零服务器依赖，可直接部署到 GitHub Pages |
| Edit 禁止 Write 覆盖（更新已有公司） | 防止丢失 body 中的产品线/技术路线图/研发投入等章节 |
| 先 L0 后 MD 的硬约束 | 保证原始资料可追溯，防止跳过归档 |
| Parser 排除 audit 文件 | 避免审计报告被当作实体解析 |

---

## 十二、部署

```bash
cd ~/Claude_projects/5factor_system/invest_wiki

# 编译
python3 L3-网页产物/build_wiki_data.py

# 验证
python3 L3-网页产物/validate.py

# 数据新鲜度扫描
python3 L3-网页产物/freshness_scan.py

# 启动本地服务
cd L3-网页产物 && python3 -m http.server 8760
# 浏览器打开 http://localhost:8760/index.html
```
