# Invest Wiki — L1 操作规范

> **LLM 每次操作 Wiki 前必读此文件。**

## 核心规则

1. **查询前先读索引** — 回答任何涉及赛道/实体的问题前，先 Read `L2-Wiki/index.md` 定位相关页面
2. **原始资料只读** — 新来源归档到 `L0-原始资料池/`，LLM 只能创建、不能覆盖或删除
3. **先消化再更新** — 新信息先写消化笔记（`L2-Wiki/消化笔记/`），再更新赛道 MD
4. **修改赛道字段** — 必须对照 `schemas/segment-schema.md` 的字段规范
5. **新增赛道** — 使用 `templates/segment-template.md`
6. **修改公司字段** — 必须对照 `schemas/company-schema.md`（24个YAML字段 + 4个Body ##段）
7. **新增公司** — 使用 `templates/company-template.md`（YAML 24字段 + Body 4模块）
8. **新增概念卡片** — 使用 `concept-card/SKILL.md` 提示词 + `templates/concept-template.md`
8. **冲突处理** — 追加 `## 动态更新记录` 小节，不覆盖原数据
9. **新旧信息合并（强制）** — 新资料补充已有实体时，**禁止整字段覆盖**，必须按下方「新旧信息合并规则」执行追加+互补

## 新旧信息合并规则（强制）

> **核心原则**：新信息是对旧信息的**补充和更新**，不是替代。原有内容是经过多轮研究沉淀下来的，包含上下文和判断，不能简单丢弃。

### 规则一览

| 字段/区域 | 合并策略 | 说明 |
|----------|---------|------|
| `one_liner` | **保留原文 + 句末追加** | 格式：`{原文} 【{日期}更新】{新关键信息}` |
| `description` | **保留原文 + 段落追加** | 新资料的新分析维度作为独立段落追加在末尾，原文不删不改 |
| `latest_revenue` | **替换** | 最新数据覆盖，这是时间序列的当前值 |
| `market_cap` | **替换** | 同上 |
| `data_freshness_date` | **替换** | 记录最后一次更新时间 |
| 财务状况表格（多年度） | **新增列 + 表下追加季度详情** | 不删旧列，不替换整表 |
| 财务状况表格（单季度） | **新增行/列 + 追加新小节** | 如已有Q1 Q2单季度表，新增Q3列 |
| 产品线/技术路线图 | **更新现有条目 + 追加新条目** | 更新进度状态，不要整表覆盖 |
| Body `##` 段 | **段内追加 + 新增子节** | 保留原有段落，新增信息加 `### {日期}更新` 小节 |
| 新增独立分析模块 | **新增 `##` 段或 `###` 子节** | 如新增"存储周期风险"、"采购承诺分析"等 |
| `updated` | **替换** | 更新至当前月份 |

### one_liner 追加示例

```yaml
# ❌ 错误（覆盖）
one_liner: "Q2 FY2026营收79万亿(miss)，毛利率83%，HBM4出货..."

# ✅ 正确（保留+追加）
one_liner: "全球HBM存储龙头(市占~56%)，专注AI用HBM/DRAM/NAND全栈内存芯片，通过高端AI存储溢价及长期供应协议实现盈利，位于半导体IDM制造中游——HBM占营收42%且产能售罄至2026全年。【2026.7.29更新】Q2营收79万亿(miss)，HBM4 Q2出货+HBM4E送样，LTA首次确认含保证金，PE 4x历史底部。"
```

### description 追加示例

```markdown
# ❌ 错误（覆盖）
description: 最新财报miss，毛利率下滑...

# ✅ 正确（保留+追加）
description: 原有完整描述保持不变。

【2026.7.29 海豚研究分析】新增观点：Q2全面miss——收入/毛利率/经营利润均低于预期...
```

### 财务状况表格更新示例

```markdown
# ❌ 错误：用单季度表替换多年度表
| 指标 | Q2 FY2026 |
|------|:------:|
| 营收 | 79万亿 |

# ✅ 正确：在多年度表上加一列 + 表下追加季度详情
| 指标 | FY2022 | FY2023 | FY2024 | FY2025 | Q1 FY2026 | Q2 FY2026 |
|------|--------|--------|--------|--------|-----------|-----------|
| 营收 | 44.62 | 32.77 | 66.19 | 97.15 | 52.58 | **79** |

### Q2 FY2026 详情
（新的季度分析内容放在这里）
```

### 硬检查（每次编辑前自检）

编辑任何已有实体的 MD 文件前，确认：
1. **one_liner**：是否保留了原文？（用 Edit 在句末追加，不要用 Write 整行覆盖）
2. **description**：是否保留了原文？
3. **财务状况表格**：是在旧表上添加列/行，还是替换了整表？
4. **正文段落**：是追加了新内容，还是覆盖了旧内容？
5. 操作完成后，`## 动态更新记录` 必须追加本次变更摘要
9. **特殊格式** — 修改 `competition`、`price_conduction`、`key_trends` 前必读 `schemas/field-formats.md`
10. **Web调研强制L0归档** — 所有 WebSearch/WebFetch 的搜索结果，**必须先完整写入 L0 归档文件，再转化到 L2 Wiki**。禁止跳过 L0 直接写入 L2。详见下方「Web调研 L0 归档规范」

## 四层信息流

```
Step 0: 完整读取原始资料全部页面 + 7项QA自检 → QA通过
  → Step 1: L0归档 + Schema-Mapping表（赛道/公司/概念/论点四层 + 无匹配内容）
  → Step 2: 实体提取（与L2已有实体精确匹配）
  → Step 3: 消化笔记（逐字段影响评估 + 置信度标记）
  → Step 4: 输出更新建议 → 等待用户确认
  → Step 5: 执行更新（YAML字段 + 动态更新记录 + 回写L0/消化笔记status）
  → Step 6: 更新 index.md 索引 + 维护记录
  → Step 7: 重新编译 wiki_data.json + 验证输出
  → Step 8: 前端验证

定期触发 L1/lint → 发现问题 → 触发重新 Ingest
```

## 格式规范（v1.1）

### sources（研报与证据）三段式
每条来源占**3行**：标题 / 1-2句摘要 / (链接)。YAML中使用 `|` block scalar。

### thesis_evidence（论点证据）三段式
每条证据占**3行**：证据内容 / `——来源: 来源标题` / `(链接)`。无链接省略第3行。

详细语法见 `schemas/field-formats.md` §4 和 §7。

## 禁止操作

- 直接修改 `L3-网页产物/wiki_data.json`（由编译脚本生成）
- 直接修改 `L3-网页产物/index.html` 中的数据部分
- 删除 L0 原始资料（只能标记 `status: 已处理`）
- 在未读 `schemas/field-formats.md` 的情况下修改竞争格局/传导链/趋势字段
- 在未读 `schemas/company-schema.md` 的情况下修改公司 MD
- 在未读 `schemas/concept-schema.md` 的情况下创建概念卡片
- **WebSearch/WebFetch 后跳过 L0 归档直接写入 L2**（违反即需回滚，先补 L0 再重做）
- **用 Write 整文件覆盖已有公司 MD**（会丢失 body 中的产品线/技术路线图/研发投入等章节）——更新已有公司数据必须用 Edit 逐段修改，只在新建公司时用 Write

## 公司 MD 更新规则（防数据丢失）

更新已有公司的 YAML frontmatter 或 body 内容时，**禁止** `Read` → 修改 → `Write` 整文件覆盖。必须用 `Edit` 定位到具体段落进行替换。原因：Write 容易误删 body 中已有的产品线详解、技术路线图、研发投入、财务状况等独立章节。

## 触发规则

| 用户输入 | 应执行 |
|---------|--------|
| 发送研报/新闻/数据/文件 | **v1.1 完整 Collection 流程**：`collector/执行指令-采集处理.md`（Step 0→8，含QA自检+Schema-Mapping） |
| "采集" / "ingest" / "处理" / "归档" / "更新知识库" | 同上，进入 Collection 模式 |
| "检查知识库" / "lint" | `lint/执行指令-定期扫描.md` |
| "更新赛道X" | 先读 `schemas/segment-schema.md` + `schemas/field-formats.md`，再改 L2 文件 |
| "新建赛道" | 先读 `templates/segment-template.md`，再创建 |
| "重新编译" | 运行 `L3-网页产物/build_wiki_data.py` |
| "增强链接" / "enrich links" | `link-enrich/执行指令-链接增强.md` |
| "refine" / "提炼" / "审计" | 进入 Refinement 模式（见下方） |
| "科普XX" / "解释XX" / "什么是XX" / "概念卡片" | `concept-card/SKILL.md` → 按11模块生成概念卡片 |
| "新建公司" / "新增公司" | 使用 `templates/company-template.md`，填充 YAML 24字段 + Body 4模块 |
| "更新公司XX" / "个股关联" | 先读 `schemas/company-schema.md`，再改 L2 公司 MD |
| "dashboard" / "知识库仪表盘" | 打开 `L3-网页产物/index.html`（知识库页面已整合至主 SPA） |
| "调研XX赛道" / "research XX" / "补充XX数据" / "新建产业链XX" | Research 模式：多Agent Web调研 + Judge交叉验证（见下方 Research 模式章节） |
| "编译" | `Step 7`: 运行 build_wiki_data.py + 验证输出 |

## 维护模式

Invest Wiki 维护分两种模式，需交替执行：

```
  采集模式（Collection）           提炼模式（Refinement）
  ┌─────────────────┐          ┌─────────────────┐
  │  ingest 素材      │          │  完整 Lint 扫描  │
  │  实体提取         │          │  thesis 审核     │
  │  消化笔记         │          │  矛盾解决        │
  │  赛道更新         │          │  链接增强        │
  │  更新 index.md    │          │  更新 index.md   │
  └────────┬────────┘          └────────┬────────┘
           │                            │
           └──────── 交替执行 ──────────┘
```

### Collection 模式（采集）— v1.1 完整流程

- **触发**：用户发送新资料 / `ingest` / "处理" / "归档" / "更新知识库"
- **前置**：必读 `schemas/field-formats.md` + `schemas/segment-schema.md` + `schemas/company-schema.md` + `schemas/concept-schema.md` + `schemas/thesis-schema.md`
- **完整步骤**（详见 `collector/执行指令-采集处理.md`）：
  0. **完整读取 + QA自检**：覆盖原始资料全部页面，完成7项检查（页数/章节/图表/数字/实体/判断句），QA不通过禁止继续
  1. **L0归档 + Schema-Mapping**：识别来源类型，生成YAML头，填写四层映射表（原文原句→赛道/公司/概念/论点字段），QA自检结果附末尾
  2. **实体提取**：从Schema-Mapping表提取赛道/公司/概念名，与L2已有实体精确匹配
  3. **消化笔记**：逐字段影响评估（当前值 vs 建议值 vs 置信度），新增实体清单，论点影响分析，风险标记
  4. **更新建议 + 确认**：输出汇总表，等待用户确认
  5. **执行更新**：修改YAML frontmatter → 追加动态更新记录 → 回写L0 status: 已处理 → 回写消化笔记 status: 已应用
  6. **更新索引**：更新 index.md 统计/维护记录/QA版本号
  7. **重新编译**：运行 build_wiki_data.py，验证实体数和类型分布
  8. **前端验证**：打开 index.html 确认渲染正常
- **格式要求**：sources和thesis_evidence使用v1.1多行格式；Schema-Mapping第一列必须是原文原句
- **节奏**：每个素材独立处理，规模较大的可并行（多Agent同时处理多份报告）
- **产出**：L0归档文件（含QA+Schema-Mapping） / 消化笔记 / 赛道字段更新 / 新概念卡片 / 新论点 / index.md更新

### Refinement 模式（提炼）

- **触发条件**（满足任一）：
  1. 每 5 次完整 Collection 后，LLM 主动提示
  2. 用户说 `refine` / "提炼" / "审计"
  3. Lint 扫描发现 ≥5 个 🔴🔴 严重问题
- **执行步骤**：
  1. 运行完整 Lint 四维扫描（矛盾/过期/孤立/格式，`lint/执行指令-定期扫描.md`）
  2. 审核所有 thesis：检查 status 是否需要变更（forming→active→invalidated/confirmed）、confidence 是否需要基于新证据调整
  3. 解决所有 unresolved contradictions（标记为 resolved/superseded/wontfix）
  4. 运行链接增强（`link-enrich/执行指令-链接增强.md`），目标平均链接数≥5/赛道
  5. 检查孤立页面（backlinks=0），补充链接或标记原因
  6. 检查无匹配内容池（L0 Schema-Mapping中的"无匹配内容"表），判断是否有累积到需要新建赛道/概念的程度
  7. 更新 `L2-Wiki/index.md` 统计 + 质量版本号 + 维护记录
  8. 重新编译 + 输出 Refinement 报告（格式如下）

### Refinement 报告格式

```
🔍 Invest Wiki Refinement 报告 — {日期}

📊 当前状态
  赛道: N | 论点: N | 链接: N | 孤立: N

🔧 本次修复
  - 解决矛盾: N 项
  - 论点更新: N 项
  - 链接增强: N 条
  - 格式修复: N 项

📈 质量版本: QA v{X} → QA v{X+1}
```

### Research 模式（多Agent调研）— v1.0

当需要从零构建一个赛道/产业链的数据，或现有数据严重不足，且没有现成研报可用时，启动多 Agent Web 调研。

**触发条件**：
1. 用户说 "调研XX赛道" / "research XX" / "补充XX数据"
2. 新建产业链，需要批量填充多个赛道
3. 单个赛道字段完整度 < 50% 且无待处理研报

**核心原理**：
- 当前环境下所有 Agent 共享同一模型，**交叉验证来自搜索角度多样性，而非模型差异**
- 3 个 Agent 搜索不同来源类型（行业报告 / 供应链 / 技术趋势），自然形成数据三角测量
- Judge Agent 比对三方结果，取中位数/最可信来源，标记冲突并给出解决依据

**执行步骤**：

1. **诊断缺口** — 运行数据完整度扫描，确定目标赛道的薄弱字段
2. **启动 Workflow** — 使用 Workflow 工具，`parallel()` 启动 3 个搜索 Agent（不同搜索角度），`pipeline()` 或单 Agent 做 Judge 合并
3. **L0 归档（强制）** — **每个搜索 Agent 的原始搜索结果必须先行归档到 L0**，包含搜索词、返回的 URL 列表、关键页面内容摘要。格式见下方「Web调研 L0 归档规范」。未完成 L0 归档前，禁止进入下一步
4. **Judge Schema 映射** — Judge 输出必须用 `StructuredOutput`，Schema 对齐 Wiki YAML 字段。**关键：Schema 的 `description` 字段中必须内嵌 field-formats.md 的精确 YAML 结构规则**（competition 使用 `{global, china, barriers, tech_gap}` dict、key_trends 使用 `[{title, detail}]` 对象数组、sources 使用 `[{title, summary, url}]` 对象数组、price_conduction 使用 `[string]` 字符串数组），否则格式错误导致前端渲染崩溃
5. **质量检查** — 检查 data_conflicts（冲突必须标注来源和解决依据）、sources（每个数字可追溯到 URL）、confidence（基于来源质量和交叉一致性）
6. **写入 Wiki** — Judge 结果经 Python 脚本格式化写入 L2 MD 文件，追加 `## 动态更新记录` 条目。**写入时必须引用 L0 归档文件的 `input_id`**
7. **编译 + 验证** — 重新编译 wiki_data.json，验证实体数/Graph边数/字段完整度

**Workflow 脚本模板**：
```
Phase 1: Research — 3 agents in parallel
  Agent A: 搜索行业报告（TrendForce/IDC/Gartner/Mordor/艾瑞等）
  Agent B: 搜索供应链（上下游公司财报/供应商公告/客户名单）
  Agent C: 搜索技术趋势（技术路线图/法规/投资逻辑/竞争动态）
Phase 2: Cross-validate — Judge agent
  输入：三方原始报告
  输出：StructuredOutput（Schema = Wiki YAML字段映射 + data_conflicts + new_thesis_candidates）
```

**成本参考**：1 个赛道 ~200K tokens / 20 分钟；10 个赛道 ~2M tokens。建议先跑 1 个赛道验证效果，再决定是否铺开。

**与 Collection 模式的区别**：
- Collection：有现成研报 PDF → 读取全部页面 → QA → Schema-Mapping → 消化更新
- Research：无现成资料 → Web 搜索 → **L0归档（强制）** → 多角度交叉验证 → Judge 合并 → 写入 L2（引用 L0 input_id）

**触发规则表补充**：

| 用户输入 | 应执行 |
|---------|--------|
| "调研XX赛道" / "research XX" / "补充XX数据" | Research 模式：多Agent Web调研 + Judge交叉验证 |
| "新建产业链XX" | 先用 Research 模式批量调研，再用 segment-template.md 逐个创建 |

### Web调研 L0 归档规范（强制）

> **规则**: 所有 WebSearch/WebFetch 的结果，必须先完整归档到 L0，再转化到 L2 Wiki。禁止跳过 L0 直接写入 L2。

> **硬检查（每次执行前自检）**: 在调用 `Edit` 或 `Write` 修改任何 L2 MD 文件之前，必须确认对应的 L0 归档文件已经创建并写入磁盘。如果 L0 归档文件不存在 → **立即停止，先创建 L0 归档文件，再继续 MD 编辑**。这个检查不是"做完MD再补"，而是"不做完L0就不许动MD"。

> **目录自检**: 创建 L0 归档文件时，必须对照下方目录映射表选择正确的子目录。
> - 公司财务数据 → `02-财报/`
> - 公司新闻/产品 → `03-新闻/`
> - 行业数据/市场报告 → `04-行业数据/`
> - 文件名格式：`{日期}-{公司/主题}-{类型}.md`
> 写错目录等同于未归档——事后发现需立即移动修正。

#### 内容抓取策略（统一调度）

**所有网页抓取统一使用 web-fetch 调度引擎**：

```bash
python3 ~/.claude/skills/web-fetch/dispatch.py <url> [--max-chars 30000]
```

五级自动降级：Scrapling → browser-act stealth → browser-act full → requests → curl。
路由学习（routes.json）自动记住每个域名的最佳工具，避免重复踩坑。

**微信公众号文章**（`mp.weixin.qq.com`）——已预配置 Scrapling 直通，自动跳过 WebFetch/Jina/curl。

> **不要手动选择工具**——dispatch.py 会根据历史成功率自动选择最佳方案。全部失败的 URL 记录到 routes.json 供后续分析。

#### 归档范围

以下所有产出均需归档：
- WebSearch 的搜索词和返回的 URL 列表
- **WebFetch 抓取的完整页面内容**（Markdown 原文，**必须**另存为独立文件到 `_attachments/`，见下方「原文保存规范」）
- 从页面中提取的关键数据点（带来源 URL）
- 被拦截/失败的请求记录（URL + 错误码，供后续重试）

#### 原文保存规范（强制）

> **规则**：通过链接（微信公众号、网页等）采集的文章，**必须将 WebFetch 抓取的完整 Markdown 原文保存到 `_attachments/` 目录**，作为不可篡改的原始备份。链接可能失效，原文备份是唯一可追溯的原始证据。

**操作步骤**：

```bash
# 抓取全文 + 自动下载图片到本地（强制使用 save_article.py）
python3 engine/save_article.py "<url>" \
  --output-dir L0-原始资料池/_attachments/ \
  --max-chars 100000

# 输出：
#   - L0-原始资料池/_attachments/{日期}-{标题}-原文.md  （Markdown，图片已替换为本地路径）
#   - L0-原始资料池/_attachments/images/               （全部下载的图片）
```

**图片处理**：`save_article.py` 自动完成：
- 提取 Markdown 中所有 `![](远程URL)` 图片链接
- 逐张下载到 `images/` 子目录
- 替换原文中的远程 URL 为 `images/xxx.jpeg` 本地路径

**文件名**：脚本自动从文章标题或 URL 生成，格式 `{YYYY-MM-DD}-{标题}-原文.md`。

**文件命名**：`{YYYY-MM-DD}-{公司/主题}-{来源}-原文.md`
- 例：`2026-07-22-特斯拉Q2财报-海豚研究-原文.md`

**L0 归档文件引用**：在 YAML frontmatter 中新增 `raw_attachment` 字段，指向原文备份路径。

**禁止行为**：
- ❌ 仅保存链接 URL 而不保存原文（链接可能失效）
- ❌ 仅保存"关键内容摘要"而不保存完整原文（摘要可能遗漏重要信息）
- ❌ 在 L0 归档文件中内嵌全文（导致归档文件过长，分离存储便于管理）

#### 目录映射

| 数据性质 | L0 目录 | 文件命名 |
|---------|---------|---------|
| 公司财务数据 | `02-财报/` | `{日期}-{公司名}-财务数据.md` |
| 公司新闻/产品/技术 | `03-新闻/` | `{日期}-{公司名}-调研笔记.md` |
| 行业数据/市场报告 | `04-行业数据/` | `{日期}-{主题}-调研笔记.md` |
| 批量多公司调研 | `03-新闻/` | `{日期}-{批次名}-数据溯源.md` |

#### 文件格式

每个 L0 归档文件必须包含：

```yaml
---
input_id: input_{YYYYMMDD}_{序号}
date: {资料日期或调研日期}
source_type: Web调研
source_name: "{描述}"
source_url: "{主要URL或'多源（见正文）'}"
ingest_date: {归档日期}
status: 待处理 | 已处理
tags: [标签列表]
data_as_of: {数据截止日期}
confidence: {高/中/低}
---

# {标题}

## 搜索记录
- 搜索词: "{query}"
- 时间: {timestamp}
- 返回结果数: N
- 有效 URL: [列表]

## 关键页面内容摘要
### URL 1: {url}
- 来源: {网站名}
- 提取数据: [数据点列表，每个带原文引用]
- ...

## 数据提取清单
| 数据点 | 值 | 来源 URL | 置信度 |
|--------|-----|---------|:--:|
| FY2025营收 | $XXX | {url} | 高 |

## 被拦截/失败记录
| URL | 错误类型 | 时间 |
|-----|---------|------|
| {url} | HTTP 403 | {time} |

## Schema-Mapping（待处理）
（如数据将用于更新 L2，填写此表）
| 原文 | L2目标 | 字段 | 置信度 |
|------|--------|------|:--:|
```

#### 与 Collection 模式的关系

- **Collection 模式**（有现成研报 PDF）：使用 `collector/执行指令-采集处理.md` 的完整流程（Step 0-8）
- **Research 模式 + L0 归档**（Web调研）：使用上述归档规范 + Research 模式的执行步骤
- 两种模式产出同一格式的 L0 归档文件

#### 禁止行为

- ❌ WebSearch 后直接将结果写入 L2 Wiki，不经过 L0
- ❌ 仅在对话上下文中使用搜索结果，不归档
- ❌ 归档时省略来源 URL（每个数据点必须可追溯到具体 URL）
- ❌ 用 "WebSearch" 作为来源而不记录具体搜索词和返回 URL
- ⚠️ 对于 403/404 的页面，仍需记录 URL 和错误码（供后续切换数据源或更换 User-Agent 重试）

### 质量版本追踪

- `L2-Wiki/index.md` 顶部维护 QA 版本号
- 每次 Refinement 后版本号递增（如 QA v1.0 → v1.1）
- 重大架构变更升级大版本，常规维护升级小版本
