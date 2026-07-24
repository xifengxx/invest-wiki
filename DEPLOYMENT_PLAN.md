# Invest Wiki 产业链知识库 — 部署与协作方案

> **文档用途**：供前端、后端、内容维护方三方对齐，明确分阶段实施方案。
> **更新日期**：2026-07-24

---

> **GitHub**：https://github.com/xifengxx/invest-wiki

## 一、系统概述

### 1.1 Invest Wiki 是什么

一个 **Markdown + YAML + [[wikilink]]** 驱动的产业链知识库，涵盖 AI 算力 / 半导体两大产业。

| 数据项 | 当前规模 |
|--------|:--:|
| 产业 | 2 |
| 赛道 | 74 |
| 公司 | 392（78 家深度覆盖） |
| 概念卡片 | 10 |
| 投资论点 | 18 |
| 总词条 | 496 |
| 图谱节点 | 470 |

### 1.2 四层架构

```
L0-原始资料池/      原始研报/财报/新闻（只读归档，含数据溯源）
    ↓ 人工 + AI 处理（按 L1 规范）
L1-Schema与Pipeline/  Schema 定义（5套）+ 采集/校验/增强 Skill
    ↓ 结构化写入
L2-Wiki/             MD + YAML 词条（496 实体，含 [[wikilink]] 关联）
    ↓ build_wiki_data.py 编译
L3-网页产物/          wiki_data.json（1.7MB）+ index.html（参考渲染）
```

### 1.3 交付物

**后端需要的唯一数据文件**：`L3-网页产物/wiki_data.json`

- 格式：JSON，UTF-8 编码
- 大小：~1.7MB（随内容增长）
- 结构：4 类实体（产业/赛道/公司/概念） + 图谱边 + 论点 + 索引元数据
- 字段 Schema 定义见 `L1-Schema与Pipeline/schemas/`（5 份 schema 文档）

**前端参考实现**：`L3-网页产物/index.html`

- 单文件 SPA，7 个页面（产业链图谱/赛道分析/个股关联/概念卡片/论点/知识库/可视化图谱）
- ECharts 力导向图 + Treemap + Sankey
- 全局搜索、排序、筛选、新鲜度可视化

---

## 二、三阶段路线图

```
Phase 1          Phase 2            Phase 3
GitHub 中转  →   直推服务器    →    多人协作 CMS
（立即可做）     （后端配合后）       （需要后台开发）
```

---

## 三、Phase 1 — GitHub 中转部署

**目标**：知识库上线，内容由单人（烟雨）通过 Claude Code 维护，GitHub 作为数据源，后端自动同步。

### 3.1 架构图

```
┌─────────────────────┐     git push      ┌──────────────────┐
│  烟雨（本地）         │ ───────────────→  │  GitHub Repo     │
│                      │                   │                  │
│  Claude Code 编辑     │                   │  invest_wiki/    │
│  L0 归档 → L2 词条   │                   │  ├─ L0-L2 源文件  │
│  build_wiki_data.py  │                   │  └─ L3/wiki_data │
│  → wiki_data.json    │                   │      .json       │
└─────────────────────┘                   └────────┬─────────┘
                                                   │
                                          Webhook / 定时 Pull
                                                   │
                                                   ↓
┌──────────────────────────────────────────────────────────────┐
│                        后端服务器                              │
│                                                              │
│  CI 监听 wiki_data.json 变更                                   │
│    → 下载 → 校验 Schema → 导入数据库（PostgreSQL/Mongo）        │
│    → 提供 REST API：                                           │
│        GET /api/wiki/entities?type=company&sector=AI芯片       │
│        GET /api/wiki/entity/:id                                │
│        GET /api/wiki/graph                                     │
│        GET /api/wiki/search?q=NVDA                             │
│        GET /api/wiki/stats                                     │
│                                                              │
└──────────────────────────┬───────────────────────────────────┘
                           │ REST API (JSON)
                           ↓
┌──────────────────────────────────────────────────────────────┐
│                   前端（design-v3）                             │
│                                                              │
│  industry-chain.html  ← 接入真实数据替换占位内容                │
│  knowledge-base.html  ← 接入真实数据替换占位内容                │
│  新增：公司详情模态 / 概念卡片 / 论点页                           │
│                                                              │
│  参考 invest_wiki/L3-网页产物/index.html 的渲染逻辑             │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 各方要做的事

#### 烟雨（内容）

| 任务 | 说明 |
|------|------|
| 初始化 git repo | `cd invest_wiki && git init && git add -A && git commit` |
| 推送到 GitHub | 创建 GitHub repo，关联 remote，push |
| 定稿 Schema 文档 | 确保 `L1-Schema与Pipeline/schemas/` 下 5 份 schema 是最新版 |
| 日常内容更新 | 本地 Claude Code 编辑 → `build_wiki_data.py` → `git commit && git push` |
| 版本标记 | 每次重大更新打 tag（如 `v1.0`, `v1.1`） |

#### 后端

| 任务 | 说明 |
|------|------|
| 理解数据结构 | 阅读 `L1-Schema与Pipeline/schemas/` 5 份 schema 文档 |
| 建同步管道 | GitHub Webhook 或定时任务（建议每 30 分钟 check 一次），监测 `L3-网页产物/wiki_data.json` 变更 |
| 导入数据库 | JSON → 关系表或文档存储（按 entity type 分表/集合） |
| 提供 REST API | 至少 5 个接口（列表/详情/图谱/搜索/统计），字段名与 wiki_data.json 保持一致 |
| 数据校验 | 导入前做基本校验（必填字段、枚举值范围） |
| 缓存 | 对高频接口（图谱、赛道列表）加 Redis 缓存 |

#### 前端

| 任务 | 说明 |
|------|------|
| 理解渲染逻辑 | 阅读 `L3-网页产物/index.html`，提取 ECharts 配置、卡片布局、交互模式 |
| 替换占位内容 | 将 `industry-chain.html` 和 `knowledge-base.html` 接入真实 API |
| 新增详情组件 | 公司详情（8 模块）、概念卡片（11 模块）、论点详情 |
| 搜索接入 | 全局搜索框对接 `GET /api/wiki/search` |

### 3.3 数据更新流程（日常）

```bash
# 烟雨本地操作，每次更新：
# 1. Claude Code 编辑 L2 词条
# 2. 编译
python L3-网页产物/build_wiki_data.py
# 3. 提交
git add L0-原始资料池/ L2-Wiki/ L3-网页产物/wiki_data.json
git commit -m "update: NVDA FY2026Q2 财报数据"
git push origin main
# 4. 后端 Webhook 自动触发 → 入库 → 网站更新
```

---

## 四、Phase 2 — 直推服务器

**目标**：去掉 GitHub 中转，内容更新直接同步到服务器，减少延迟。

### 4.1 架构图

```
┌─────────────────────┐
│  烟雨（本地）         │
│                      │
│  Claude Code 编辑     │
│  build_wiki_data.py  │
│  → wiki_data.json    │
└─────────┬───────────┘
          │
          │ rsync / SCP / HTTP Upload
          │
          ↓
┌──────────────────────────────────────────────┐
│                后端服务器                      │
│                                              │
│  接收 wiki_data.json → 校验 → 入库            │
│  → API → 前端                                │
└──────────────────────────────────────────────┘
```

### 4.2 后端需提供

只需要提供 **一个上传入口**，三选一：

**推荐 — SSH + rsync**（最稳定）
```bash
# 后端创建专用账号，限定目录权限
rsync -avz L3-网页产物/wiki_data.json wiki@server:/data/wiki/
```

**备选 — HTTP 上传接口**
```bash
curl -X POST https://api.xxx.com/admin/wiki/upload \
  -H "Authorization: Bearer <token>" \
  -F "file=@L3-网页产物/wiki_data.json"
```

**备选 — 对象存储（S3/OSS）**
```bash
# 后端给一个 S3 bucket 写入权限，awscli 或 rclone 上传
aws s3 cp L3-网页产物/wiki_data.json s3://invest-wiki/data/
```

### 4.3 烟雨要做的事

- 本地写一个 `sync.sh` 脚本，一行命令完成编译 + 上传
- GitHub 仍然保留，作为版本备份（不参与部署链路）

```bash
# sync.sh
#!/bin/bash
python L3-网页产物/build_wiki_data.py && \
git add L0-原始资料池/ L2-Wiki/ L3-网页产物/wiki_data.json && \
git commit -m "update: $(date +%Y-%m-%d)" && \
git push && \
rsync -avz L3-网页产物/wiki_data.json wiki@server:/data/wiki/ && \
echo "✅ 同步完成"
```

### 4.4 Phase 1 → Phase 2 变化

| | Phase 1 | Phase 2 |
|------|------|------|
| 数据链路 | 本地 → GitHub → 后端 | 本地 → 后端 |
| 更新延迟 | 后端轮询间隔 + 入库时间 | 上传即时生效 |
| 版本管理 | GitHub | GitHub（备份，不入链路） |
| 后端改动 | 需要同步管道 | 需要上传接口 |
| 前端改动 | 无变化 | 无变化（API 不变） |

---

## 五、Phase 3 — 多人协作 CMS

**目标**：多人共建知识库，非技术人员可通过 Web 上传资料，AI 自动处理，管理员审核后上线。

### 5.1 架构图

```
┌─────────────────────────────────────────────────────┐
│                    管理后台（Web）                     │
│                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │ 资料上传  │   │ AI 处理   │   │ 审核发布  │        │
│  │          │   │          │   │          │        │
│  │ 拖拽 PDF │→  │ LLM 提取 │→  │ 预览对比  │→ 发布   │
│  │ 粘贴链接  │   │ 按 Schema │   │ 修改/通过  │        │
│  │ 表单录入  │   │ 自动归档  │   │ /驳回     │        │
│  └──────────┘   └──────────┘   └──────────┘        │
│                                                     │
│   + 烟雨本地 Claude Code 编辑（管理员通道）            │
│     → 同样走上传接口，保持数据源一致                     │
└──────────────────────┬──────────────────────────────┘
                       │
                       ↓
┌──────────────────────────────────────────────────────┐
│                    后端服务器                          │
│                                                      │
│  数据库（wiki_data）← 审核通过自动写入                   │
│  API → 前端（不变）                                    │
└──────────────────────────────────────────────────────┘
```

### 5.2 核心流程

```
用户上传 PDF / 链接 / Markdown
      │
      ↓
后端接收 → 存原始文件 + 建处理任务
      │
      ↓
AI 管道（调 Claude API / LLM）：
  1. 按 L1 Schema 提取结构化信息
  2. 生成 L0 归档（带溯源）
  3. 生成消化笔记（字段影响评估）
  4. 生成 L2 更新建议
      │
      ↓
标记为 "AI 初稿" → 推送给管理员（烟雨）
      │
      ↓
管理员审核：
  - ✅ 通过 → 自动编译 → 入库 → 发布
  - ✏️ 修改 → 编辑后通过
  - ❌ 驳回 → 注明原因，退回提交者
```

### 5.3 烟雨本地工作流（保持可用）

Phase 3 不剥夺本地编辑能力。管理员通道：

```
烟雨本地 Claude Code
  → 和现在一样编辑 L2 词条
  → build_wiki_data.py
  → 通过上传接口同步到服务器（覆盖本地修改的实体）
  → 后台自动 merge（以更新时间戳为准，新覆盖旧）
```

**数据一致性规则**：

| 场景 | 处理方式 |
|------|---------|
| 后台 AI 处理了一个公司，你本地也改了同一个公司 | 以 `updated_at` 时间戳为准，新覆盖旧。冲突时后台告警通知管理员人工 merge |
| 你本地新建了一个公司，后台没有 | 上传后正常新增 |
| 后台上传了资料但未处理 | 你本地可以看到队列，认领处理 |

### 5.4 后台页面清单

| 页面 | 功能 |
|------|------|
| 上传入口 | 拖拽 PDF / 粘贴 URL / 填写表单 |
| 任务队列 | 待处理 / AI 处理中 / 待审核 / 已发布 |
| 审核页 | 并排展示：原始资料 vs AI 提取结果 vs 当前数据库值，一键通过/修改/驳回 |
| 实体管理 | 搜索/浏览/手动编辑所有词条 |
| 同步状态 | 查看最近同步记录、冲突告警 |
| 统计面板 | 内容增量趋势、字段完整度、新鲜度 |

### 5.5 各方要做的事

#### 后端（主要工作量）

| 任务 | 说明 |
|------|------|
| 后台系统 | 用户认证、角色权限（管理员/编辑/访客） |
| 上传接口 | 支持 PDF / URL / Markdown，文件存储 |
| AI 管道 | 调 LLM API，Prompt 模板基于 L1 collector skill 改造 |
| 审核工作流 | 状态机：待处理→AI初稿→已审核→已发布 |
| 冲突检测 | 多源写入时的 merge 策略 |
| API（不变） | 与 Phase 1/2 相同的 REST 接口 |

#### 烟雨

| 任务 | 说明 |
|------|------|
| 改造 Prompt | 将 L1 collector skill 转化为 LLM API 可用的 Prompt 模板 |
| 定义审核标准 | 什么情况自动通过、什么情况必须人工 |
| 测试 AI 管道 | 用已有数据验证 AI 提取准确率 |
| 日常审核 | 审核后台的 AI 初稿 |

#### 前端

| 任务 | 说明 |
|------|------|
| 后台 UI | 开发上述 6 个页面 |
| 前端展示（不变） | 与 Phase 1 相同 |

---

## 六、各阶段对比总结

| | Phase 1 | Phase 2 | Phase 3 |
|------|:--:|:--:|:--:|
| 上线时间 | 1-2 周 | 1 周（Phase1 基础上） | 4-8 周 |
| 内容维护人 | 烟雨一人 | 烟雨一人 | 多人 + AI |
| 数据链路 | 本地→GitHub→后端 | 本地→后端 | Web上传+本地→后端 |
| 后端开发量 | 中（同步+API+入库） | 小（加上传接口） | 大（完整后台） |
| 前端开发量 | 中（接入真实数据） | 无变化 | 大（后台 UI） |
| 版本管理 | GitHub（主链路） | 本地 git（备份） | 后端数据库 |
| 更新延迟 | 分钟级（轮询） | 秒级（即时） | 分钟级（审核后） |
| AI 自动化 | 无（Claude Code 手动） | 无 | LLM API 自动处理 |

---

## 七、当前行动（Phase 1 启动清单）

### 烟雨（本周）

- [ ] 在 GitHub 创建 `invest-wiki` repo
- [ ] `invest_wiki/` 初始化 git，首次 push
- [ ] 确认 `wiki_data.json` Schema 稳定，字段不再大改
- [ ] 写一份 `SCHEMA.md`（字段名/类型/枚举值/示例，方便后端对照）

### 后端（收到本文档后）

- [ ] 阅读 `L1-Schema与Pipeline/schemas/` 5 份 schema 文档
- [ ] 确认数据导入方案（关系型 or 文档型）
- [ ] 搭建 GitHub Webhook → 入库 → API 管道
- [ ] 给出 API 文档草稿（至少包含 entity list / detail / graph / search / stats）

### 前端（收到本文档后）

- [ ] 阅读 `L3-网页产物/index.html` 渲染参考
- [ ] 确认接入方案：直接改造 design-v3 现有页面，还是新增页面
- [ ] 列出需要的 API 字段，与后端对齐
