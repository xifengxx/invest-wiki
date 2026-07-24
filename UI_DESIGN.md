# Invest Wiki 网页设计规范

> 版本 3.0 · 2026-07-21 · 基于 L3-网页产物/index.html 实际实现（Design V3 布局）

---

## 一、设计系统概述

### 1.1 设计语言

采用 **Apple HIG 风格**（浅色、高对比、圆角卡片、微妙阴影）。参考 `deploy-gh-pages/design-v3/` 的设计系统，但本文件不依赖外部引用，所有规范直接来自实际 CSS 实现。

### 1.2 技术栈

| 层 | 选型 | 用途 |
|----|------|------|
| CSS 变量 | `:root` 内联 | 全局颜色/间距令牌 |
| 布局框架 | Tailwind CSS CDN | 原型的工具类，核心布局用自定义 CSS |
| 图表 | ECharts 5.6 CDN | Treemap / 力导向图 / Sankey / 因果图 |
| 图标 | Lucide Icons CDN | 16-18px 线框图标 |
| 字体 | 系统字体栈 | 无外部字体依赖 |

### 1.3 页面模型

单文件 SPA（`index.html`），内嵌全量 JSON 数据。无路由、无服务端、无构建步骤。部署方式：任意静态文件服务器。

---

## 二、CSS 设计令牌

### 2.1 颜色系统

```css
:root {
  /* 背景与表面 */
  --bg:      #F5F5F7;   /* 页面底色 */
  --card:    #FFFFFF;   /* 卡片/侧边栏/导航栏背景 */
  --border:  #E5E5EA;   /* 所有边框和分割线 */
  --hover:   #F5F5F7;   /* 悬停背景（与 --bg 同值） */
  --active:  rgba(0,113,227,0.10);  /* 选中态背景 */

  /* 文字 */
  --text:    #1D1D1F;   /* 主文字：标题、正文、重要信息 */
  --text2:   #86868B;   /* 次要文字：说明、标签、辅助信息 */

  /* 语义色 */
  --accent:  #0071E3;   /* 强调色：链接、选中态、主按钮、蓝色标签 */
  --up:      #FF3B30;   /* 警示色：上涨(A股)/下跌(美股)、删除、危险 */
  --down:    #34C759;   /* 正向色：下跌(A股)/上涨(美股)、成功、绿色标签 */

  /* 产业链层级色（用于 Treemap 和关系图节点着色） */
  --l1: #94a3b8;        /* L1 原材料：灰 */
  --l2: #60a5fa;        /* L2 设备/组件：蓝 */
  --l3: #4ade80;        /* L3 核心产品：绿 */
  --l4: #fb923c;        /* L4 终端应用：橙 */
}
```

| 变量 | 色值 | 使用场景 |
|------|------|---------|
| `--bg` | `#F5F5F7` | body 背景、搜索框、统计卡片、trend-card、传导链容器 |
| `--card` | `#FFFFFF` | 侧边栏、顶栏、卡片、图表容器、flow-step |
| `--border` | `#E5E5EA` | 边框、分割线、灰色标签背景 |
| `--text` | `#1D1D1F` | 标题、正文、粗体数据 |
| `--text2` | `#86868B` | 辅助说明、标签文字、面包屑、过期信息 |
| `--accent` | `#0071E3` | 选中态、链接、蓝色标签、关系点、证据编号 |
| `--up` | `#FF3B30` | 上涨/警示色标签 |
| `--down` | `#34C759` | 下跌/正向色标签、利润池进度条 |
| `--l1` | `#94a3b8` | L1 层级 Treemap/关系图着色 |
| `--l2` | `#60a5fa` | L2 层级 Treemap/关系图着色 |
| `--l3` | `#4ade80` | L3 层级 Treemap/关系图着色 |
| `--l4` | `#fb923c` | L4 层级 Treemap/关系图着色 |

### 2.2 字体系统

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
             'PingFang SC', 'Microsoft YaHei', sans-serif;
```

| 层级 | 字号 | 字重 | 行高 | 字间距 | 使用场景 |
|------|:--:|:--:|:--:|:--:|---------|
| H1 | 28px | 700 | 1.2 | -0.02em | 详情页赛道名（`.detail-header h2`） |
| H2 | 18px | 600 | 1.4 | -0.01em | 卡片标题（`.card-title`） |
| H3 | 16px | 700 | — | — | 侧边栏 Logo |
| Body | 14px | 400 | 1.5-1.8 | — | 正文、详情描述 |
| Body-S | 13px | 400-600 | — | — | 关系名、表格内容、视图标签 |
| Caption | 12px | 400-500 | — | — | 树节点、热力榜、趋势描述、传导步骤 |
| Caption-S | 11px | 400-600 | — | 0.03-0.04em | 分组标题、统计标签、证据文本 |
| Label | 10px | 500-600 | — | — | 标签/徽章、关系标签、角色标签 |

### 2.3 圆角系统

| 尺寸 | 值 | 使用场景 |
|------|-----|---------|
| 大 | 12px | 卡片（`.card`）、图表容器（`.chart-box`） |
| 中 | 10px | 搜索框、视图标签容器、统计卡片（`.ds-card`）、趋势卡片 |
| 小 | 8px | 视图标签按钮、传导步骤、角色标签、统计子项 |
| 全圆角 | 16px / 10px | 产业切换按钮（16px）、标签/徽章（10px） |
| 圆 | 50% | 关系点、证据编号圈 |

### 2.4 间距系统

| 间距 | 值 | 使用场景 |
|------|-----|---------|
| xs | 4px | 标签/徽章的 padding、视图标签容器 gap |
| sm | 6-8px | 产业切换 gap、热力榜 gap、传导步骤 gap |
| md | 12px | 内容区 gap、统计卡片 gap、产业切换 padding |
| lg | 16px | 内容区 padding、侧边栏 padding、详情卡片 margin-bottom |
| xl | 20-24px | 侧边栏 Logo padding、卡片 padding、顶栏 padding |
| 2xl | 220px | 侧边栏宽度 |
| 3xl | 260px | 树形面板宽度（产业链图谱内） |
| 4xl | 480px | 搜索框最大宽度 |
| 5xl | 56px | 顶栏高度 |

---

## 三、页面布局

### 3.1 整体结构（Design V3 — 两栏布局）

```
┌──────────┬─────────────────────────────────────────┐
│ Sidebar  │  Topbar (56px): 面包屑 + 搜索 + 统计    │
│ (220px)  ├─────────────────────────────────────────┤
│          │  Content Row (flex:1)                   │
│ ┌──────┐ │  ┌─────────────┬──────────────────────┐ │
│ │ Logo │ │  │ Tree Panel  │  Chart / Detail      │ │
│ ├──────┤ │  │ (仅产业链    │  (ECharts 或详情页)   │ │
│ │7导航 │ │  │  图谱显示)   │                      │ │
│ │      │ │  │ 260px       │  flex:1              │ │
│ └──────┘ │  └─────────────┴──────────────────────┘ │
└──────────┴─────────────────────────────────────────┘
```

- **Sidebar**: 220px 固定宽度，7 个导航项（产业链图谱/赛道分析/个股关联/概念卡片/论点/知识库/可视化图谱）
- **Topbar**: 56px 高度，面包屑在左，搜索框居中，统计在右
- **Content Row**: `flex:1`，产业链图谱时左侧嵌入树形面板（260px），其他页面内容全宽
- **右栏已移除**：原热力图排行和知识库统计面板已删除
- **详情页/列表页**: 内边距 `20px 24px`，卡片间距 `16px`

---

## 四、组件规范

### 4.1 侧边栏 (`.sidebar`)

| 属性 | 值 |
|------|-----|
| 宽度 | 220px (min-width 同) |
| 定位 | sticky, top:0, height:100vh |
| 背景 | `var(--card)` |
| 边框 | 右边 `1px solid var(--border)` |
| 滚动 | overflow-y: auto |
| 层级 | z-index: 50 |

**Logo 区 (`.sidebar-logo`)**
- padding: 20px 16px，字号 16px 字重 700，底部边框分割

**导航项 (`.nav-item-side`)**
- 7 个导航：产业链图谱 / 赛道分析 / 个股关联 / 概念卡片 / 论点 / 知识库 / 可视化图谱
- padding 9px 16px，gap 8px，字号 13px 字重 500
- 左边 2px 透明边框，hover 变灰底，选中态蓝色左边框 + 浅蓝背景

### 4.2 顶栏 (`.topbar`)

| 属性 | 值 |
|------|-----|
| 高度 | 56px |
| 布局 | display:flex, align-items:center, gap:16px |
| 背景 | `var(--card)` |
| 边框 | 底部 `1px solid var(--border)` |
| 内边距 | 0 24px |

**面包屑 (`.bc`)**
- 字号 14px, 灰色
- 当前页: `.active`, 黑色, 字重 500
- 可点击项: `cursor:pointer`, 蓝色

**搜索框 (`.search`)**
- 位于 Topbar 居中，最大宽度 480px，高度 38px
- 背景 `var(--bg)`，圆角 20px（全圆角胶囊形），无边框
- 聚焦时白底 + 蓝色边框 + 3px 蓝色阴影
- 左侧 SVG 放大镜图标，下拉菜单居中弹出，最大高度 400px
- 支持中英文/代码搜索，200ms 防抖，键盘导航（↑↓ Enter Escape）
- 搜索结果带类型标签（赛道/公司/概念/论点）和颜色编码

### 4.3 卡片 (`.card`)

所有内容模块的基础容器。

| 属性 | 值 |
|------|-----|
| 背景 | `var(--card)` |
| 边框 | `1px solid var(--border)` |
| 圆角 | 12px |
| 内边距 | 24px |
| 下间距 | 16px |
| 过渡 | all 0.3s ease |
| 悬停 | `box-shadow: 0 8px 32px rgba(0,0,0,0.08)` |

**卡片标题 (`.card-title`)**
- 字号 18px, 字重 600, 行高 1.4
- 字间距 -0.01em
- margin-bottom: 12px

### 4.4 视图标签 (`.view-tabs`)

- 容器: `display:flex; gap:4px; background:var(--bg); border-radius:10px; padding:4px`
- 标签 (`.view-tab`): padding 7px 16px, 圆角 8px, 字号 13px 字重 500
  - 默认: 透明背景, 灰色文字
  - 悬停: 文字变黑
  - 选中: 白色背景 + 黑色文字 + `0 1px 3px rgba(0,0,0,0.08)` 阴影

### 4.5 图表区 (`.chart-box`)

- `flex:1`, 最小高度 440px
- 白色背景, 圆角 12px, 边框 `1px solid var(--border)`
- `overflow:hidden`
- 内部 div 100% 宽高承载 ECharts 实例

### 4.6 标签系统 (`.tag`)

| 属性 | 值 |
|------|-----|
| 布局 | inline-flex, align-items:center |
| 尺寸 | height:20px, padding:0 8px |
| 圆角 | 10px (全圆角) |
| 字号 | 10px, 字重 500 |

| Class | 背景 | 文字色 | 用途 |
|-------|------|--------|------|
| `.tag-blue` | `var(--accent)` | `#fff` | 产业标签、趋势技术类 |
| `.tag-green` | `var(--down)` | `#fff` | 趋势市场类（预留） |
| `.tag-purple` | `#AF52DE` | `#fff` | 利润率标签、趋势事件类 |
| `.tag-gray` | `var(--border)` | `var(--text)` | 层级标签、上游输入标签 |
| `.tag-orange` | `#FF9500` | `#fff` | 高难度/大差距标记 |

### 4.7 表格 (`.comp-table`)

- 全宽, border-collapse: collapse, 字号 13px
- 表头: padding 8px 12px, 11px 600 uppercase, 灰色文字, 底部 2px 边框, 背景 `var(--bg)`
- 单元格: padding 10px 12px, 底部 1px 边框
- 行悬停: 背景 `var(--bg)`

### 4.8 角色标签 (`.role-tag`)

用于公司表中的角色标识：

| Class | 背景 | 文字色 | 匹配规则 |
|-------|------|--------|---------|
| `.role-lead` | `#0071E3` | `#fff` | role 含"龙头" |
| `.role-second` | `rgba(0,113,227,0.12)` | `var(--accent)` | role 含"二线"或"弹性" |
| `.role-concept` | `rgba(255,149,0,0.12)` | `#FF9500` | 其他角色 |

---

## 五、详情页 11 模块规范

### 5.1 页面框架

```
┌─ 返回按钮 ──────────────────────────────┐
│ ← 返回产业链全景                           │
├─ 页面标题区 ──────────────────────────────┤
│ GPU                  [AI算力] [L3] [65-75%]│
├─ 模块1: 市场规模 ─────────────────────────┤
│ $130B    40%    65-75%    6              │
│  TAM     CAGR   利润率    引用量            │
├─ 模块2: 定位与定义 ───────────────────────┤
│ 描述正文（支持 Markdown 加粗 + | 分段）     │
├─ 模块2.5: ⚠️ 已知矛盾 ────────────────────┤
│ [琥珀色边框] 矛盾描述 | 来源A/B | 状态      │
│ 仅在 contradictions 非空时显示             │
├─ 模块3: 价值链分析 ───────────────────────┤
│ 成本占比 ████████░░ 55%                   │
│ 利润池比 ████████████ 65%  (None时隐藏)    │
├─ 模块4: 上下游与传导关系 ──────────────────┤
│ 上游输入: [HBM] [CoWoS] [先进制程]         │
│ 下游客户: [云厂商] [AI实验室] [企业]         │
│ 价格传导链: [步骤1]⇒[步骤2]⇒[步骤3]⇒[步骤4] │
│ 传导链文字描述                              │
├─ 模块5: 竞争格局 ─────────────────────────┤
│ 全球市场表 | 国内市场表 | 进入壁垒 | 技术代差 │
├─ 模块6: 关键趋势 ─────────────────────────┤
│ [趋势卡片1] [趋势卡片2] ...                 │
├─ 模块7: 关联关系 ─────────────────────────┤
│ ● HBM高带宽内存  上游供应                   │
│ ● AI服务器       下游应用                   │
├─ 模块8: 研报与证据 ───────────────────────┤
│ ① 粗体标题                               │
│   来源描述                                │
│   example.com (可点击)                    │
├─ 模块9: 核心标的 ─────────────────────────┤
│ 代码  公司  角色  营收占比                  │
│ NVDA NVIDIA 龙头  85%                     │
├─ 模块10: 投资论点 ────────────────────────┤
│ [论点卡片] 标题 | 🟢active | ★★★★☆ 8/10  │
│ 核心主张摘要，点击可定位关联赛道             │
└──────────────────────────────────────────┘
```

### 5.2 模块1: 市场规模

**数据源**: `tam`, `cagr`, `margin`, `backlinks`

**布局**: 4 列 Grid (`.detail-stats`: `grid-template-columns: repeat(4,1fr)`, gap:12px)

**子组件 (`.ds-card`)**:
- 背景 `var(--bg)`, 圆角 10px, 内边距 16px, 文字居中
- 数值 (`.val`): 22px 700 黑色
- 标签 (`.lbl`): 11px 灰色 uppercase, letter-spacing 0.03em, margin-top 4px

| 卡片 | 值格式 | 空值处理 |
|------|--------|---------|
| TAM | `$130B` | `$?B` |
| CAGR | `40%` | `?%` |
| 利润率 | `65-75%` | `?` |
| 引用量 | `6` | 始终有值 |

### 5.3 模块2: 定位与定义

**数据源**: `description`

**渲染规则**:
- `**text**` → `<b class="hl">text</b>`（蓝色加粗高亮）
- `|` → `</p><p style="margin-top:12px;">`（管道符转为段落分隔）
- 最大 1500 字符截断

**样式**: 字号 14px, 行高 1.8

### 5.4 模块3: 价值链分析

**数据源**: `cost_share_pct`, `cost_share_context`, `profit_pool_pct`, `profit_pool_context`

**显示条件**: `cost_share_pct` 或 `profit_pool_pct` 任一非空即显示

**布局**: 
- 描述文字：`在{cost_share_context}中，{赛道名}的成本占比约 {cost_share_pct}%，利润池占比约 {profit_pool_pct}%。`（利润池缺失时省略利润池部分）
- 进度条 Grid：两个都有值时 `1fr 1fr`；只有一个值时 `1fr`

**进度条**:
- 轨道 (`.bar-track`): 高度 8px, 背景 `var(--border)`, 圆角 4px
- 填充 (`.bar-fill`): 高度 100%, 圆角 4px, 背景 `var(--accent)`, 过渡 width 0.6s ease
- 利润池填充色: `var(--down)` 绿色
- 空值处理: `profit_pool_pct` 为 `null` 时，整列不渲染

### 5.5 模块4: 上下游与传导关系

**数据源**: `key_inputs`, `key_customers`, `price_conduction`

**上游输入**:
- 标题 `上游输入`（13px 600）
- 标签列表: `key_inputs` 逗号分隔 → 每个为 `<span class="tag tag-gray">`
- 空值: 显示 `暂无数据`（12px 灰色）

**下游客户**:
- 标题 `下游客户`（13px 600）
- 标签列表: `key_customers` 逗号分隔 → 每个为 `<span class="tag tag-blue">`
- 空值: 显示 `暂无数据`

**价格传导链**:
- 流程图 (`.flow-arrow`): flex wrap, gap 8px, padding 14px 16px, 背景 `var(--bg)`, 圆角 10px
  - 步骤节点 (`.flow-step`): 白色背景, 边框, 圆角 8px, padding 7px 12px, 12px 字重 500
  - 箭头 (`.flow-arr`): 蓝色, 字重 700, 16px
  - **短标签提取逻辑**: 取每步逗号/句号前的首段，最长 18 字符
  - 节点 hover: 边框变蓝, `cursor:help`（完整文字在 title 属性中）
- 文字描述: margin-top 10px, 12px, 灰色, 行高 1.7
  - 显示完整传导文本（`⇒` 替换为 ` → `）

### 5.6 模块5: 竞争格局

**数据源**: `competition`

**解析规则**（按 `schemas/field-formats.md`）:
- `||` 分割全球/中国市场
- `🔒` 标记进入壁垒段
- `📐` 标记技术代差段
- 每个厂商行: `名称|份额%|备注`，`,` 分隔

**渲染为 4 张子表**（依数据存在性显示）:
1. **全球市场**: 表头 `厂商 | 份额 | 备注`
2. **国内市场**: 同上
3. **进入壁垒**: 表头 `壁垒项 | 难度 | 说明`（难度固定为 `高` 橙色标签）
4. **技术代差**: 表头 `维度 | 差距 | 说明`（差距固定为 `大` 橙色标签）

每个子表标题 13px 600，表格使用 `.comp-table`。

### 5.7 模块6: 关键趋势

**数据源**: `key_trends`（`[{title, detail}]` 对象数组）

**解析规则**: 优先使用结构化 YAML 数组，通过 `typeof` 检查是否对象；旧 string 格式（`|` 分隔项，`——` 分隔标题/内容）已经过 `Array.isArray()` 兼容处理

**渲染**: 每个趋势一个卡片 (`.trend-card`)：
- 标题 (`.trend-title`): 13px 600 黑色。取 `item.title`，最多 40 字符 + `…`
- 描述 (`.trend-desc`): 12px 灰色，行高 1.6。取 `item.detail`，最多 140 字符 + `…`
- 卡片背景 `var(--bg)`, 圆角 10px, padding 12px, margin-bottom 8px

**空值/边缘情况**:
- 无 `——` 时: 首句为标题（识别 `。，,.` 分隔符），其余为描述
- 文本 ≤ 80 字符时: 不显示标题行，仅显示描述
- 编号前缀 `N) ` 自动去除

### 5.8 模块7: 关联关系

**数据源**: `wikilinks`, `key_inputs`, `key_customers`

**关系类型自动推导**（前端 JS 逻辑）:

| 条件 | 标签 | 颜色 | 描述模板 |
|------|------|------|---------|
| linked.name 在 key_inputs 中 | 上游供应 | `#FF9F0A` | `{linked}是{current}的关键上游组件` |
| linked.name 在 key_customers 中 | 下游应用 | `#34C759` | `{linked}依赖{current}提供算力基础` |
| linked.layer < current.layer | 上游供应 | `#FF9F0A` | `{linked}位于{current}产业链上游` |
| linked.layer > current.layer | 下游应用 | `#34C759` | `{linked}位于{current}产业链下游` |
| linked.layer == current.layer | 协同互补 | `#5856D6` | `{current}与{linked}在产业链中协同互补` |

**渲染**: 每个关联为一个 `.relation-item`：
- 左侧彩色圆点 (`.relation-dot`): 10px, border-radius 50%, 颜色 = 关系色
- 中间: 名称 (`.relation-name`, 13px 600) + 描述 (`.relation-desc`, 11px 灰色)
- 右侧: 关系标签 (`.relation-tag`, 10px 600), 背景 = 关系色 10%透明度, 文字 = 关系色
- **可点击**: `cursor:pointer`, `onclick="openDetail(slug)"`
- **悬停**: 背景 `var(--hover)`, `padding-left: 12px`, 名称变蓝, 过渡 0.15s ease

**空值**: wikilinks 为空数组时显示 `暂无关联词条`（13px 灰色）

### 5.9 模块8: 研报与证据

**数据源**: `sources`

**解析规则**: `;` 分隔来源，`(URL)` 提取链接

**渲染**: 每个来源为一个 `.evidence-item`：
- 编号圈 (`.evidence-num`): 22px 直径, 圆形, 蓝色背景, 白色数字, 11px 700
- 内容区 (`.evidence-text`):
  - 标题: `<strong>` 粗体, 黑色, display:block。取 URL 前的文本
  - 描述: 可选，取去除 URL 后的文本（如与标题重复则省略）
  - 链接: `<a>` 蓝色, 11px, display:inline-block, margin-top 4px, padding 2px 6px, 圆角 4px。显示域名（去掉 `https://` 和路径）
  - 链接 hover: 浅蓝背景 `rgba(0,113,227,0.08)` + 下划线
  - 链接 target: `_blank`（新窗口打开）

### 5.10 模块9: 核心标的

**数据源**: `companies`

**渲染**:
- 有数据: 描述行（12px 灰色, 共N家公司） + `<table class="comp-table">`
  - 表头: `代码 | 公司 | 角色 | 营收占比`
  - 角色列: `.role-tag` 着色（龙头=蓝色, 二线/弹性=浅蓝, 其他=橙色）
  - 最多显示 15 条
- 无数据: 显示 `暂无核心标的`（13px 灰色）

---

### 5.12 模块 2.5: ⚠️ 已知矛盾

**数据源**: `contradictions`（YAML list，可选字段）

**渲染规则**:
- **仅在 `contradictions` 非空时渲染**，空数组或 null 不显示
- 卡片样式: `border-left: 3px solid #F59E0B`（琥珀色左边框），渐变背景
- 标题: `⚠️ 已知矛盾 (N项)`，颜色 `#B45309`（深琥珀）
- 每条矛盾: 圆角 8px 内框，12px 字号，1.6 行高
  - 状态着色:
    - `unresolved`: 琥珀色（`#D97706` 文字 + 半透明琥珀背景）
    - `resolved_a` / `resolved_b`: 绿色（`#059669` + 半透明绿背景）
    - `superseded`: 灰色（`#86868B` + 浅灰背景）
  - 显示: 矛盾描述（bold）+ 来源A/B + 发现日期 + 状态

**数据源例子**:
```javascript
[{
  desc: "TAM可能存在低估...",
  source_a: "L0-原始资料池/.../2026-TrendForce.md",
  source_b: "当前值",
  status: "unresolved",
  found_date: "2026-07-20"
}]
```

---

### 5.13 模块 10: 投资论点

**数据源**: `DATA.thesis_index[slug]`（segment→thesis映射）+ entities 中 `type==='thesis'` 的实体

**渲染规则**:
- 仅在有关联论点时显示（`thesis_index[slug]` 非空）
- 标题: `投资论点 (N条)`，12px 灰色副标题
- 每条论点卡片: 12px padding，10px 圆角，`1px solid var(--border)`，下方 10px margin
- 点击可触发 `highlightInChart(thesisSlug)` 定位关联赛道
- 卡片结构:
  1. 标题行: **论点名**（14px bold）+ status 标签（10px，2/6px padding，4px 圆角）
     - `active`: 蓝底蓝字（`#0071E3`）
     - `forming`: 灰底灰字（`#86868B`）
     - `confirmed`: 绿底绿字（`#059669`）
     - `invalidated`: 红底红字（`#DC2626`）
  2. 核心主张摘要: 12px 灰色文字
  3. Confidence ★评分: `★`×5 `☆`×5（金色 `#F59E0B`，11px）+ 数字 `N/10`

**CSS 新增**:
```css
/* 矛盾卡片 */
.contradiction-item{font-size:12px;line-height:1.6;padding:10px 12px;border-radius:8px;margin-bottom:8px;}
/* 论点卡片 */
.thesis-card{padding:12px;border-radius:10px;border:1px solid var(--border);margin-bottom:10px;cursor:pointer;}
.thesis-status{font-size:10px;padding:2px 6px;border-radius:4px;}
```

---

## 六、图表视图规范

### 6.1 图表切换

4 个视图标签: `全景Treemap | 关系网络 | 价值链流转 | 因果传导`

点击标签切换 `cv` 变量，调用 `renderView()` 重新渲染 ECharts。

### 6.2 Treemap 全景图

- **数据**: 按产业过滤的 segments，value = TAM(B)
- **颜色**: 按 layer 着色（`var(--l1)` ~ `var(--l4)`）
- **标签**: 名称 + TAM 值，字号 10 bold，色 `#1D1D1F`
- **面包屑**: 底部显示，高度 24px
- **交互**: 点击 → 触发详情页；选中节点蓝边框（3px）高亮
- **Tooltip**: `<b>名称</b><br/>TAM:$值B`

### 6.3 关系网络（力导向图）

- **节点**: 赛道名，大小 = `max(10, min(50, TAM*0.3))`，颜色 = layer 色
- **边**: wikilink 关联，蓝色 `#60a5fa`，curveness 0.2
- **力参数**: repulsion 250, edgeLength [80,220], gravity 0.1
- **标签**: 9px，名称 > 8 字符截断加 `…`

### 6.4 价值链流转（Sankey）

- **节点**: 赛道名，按 layer 层次排列
- **边**: wikilink 关联（仅 segment-to-segment）
- **颜色**: 按源节点 layer 着色

### 6.5 因果传导

- **节点**: 较小 (20px)，黄色边框 (`#F59E0B`)，浅黄填充 (`#FEF9E7`)
- **边**: 金黄色 `#F59E0B`，2.5px 线宽
- **力参数**: repulsion 400, edgeLength [120,300], gravity 0.06

### 6.6 节点高亮联动

侧边栏点击树节点 → 图表中对应节点高亮（调用 `highlightInChart(slug)`）。图表节点点击 → 跳转详情页（`openDetail(slug)`）。底部显示提示文字 `已选中XXX，点击图表中对应节点查看详情`。

### 6.7 公司详情视图（v2.1 新增）

入口：搜索框输入公司名 → `openDetail(slug)` → 自动路由到 `renderCompany()`

| 区域 | 内容 | CSS |
|------|------|-----|
| Header | name + ticker（16px bold） + country tag + chain_layer tag + chain_role（龙头=金色） | `.detail-header` |
| One-liner | 蓝色左边框卡片，14px 正文 | `border-left:4px solid #0071E3` |
| 关联赛道 | 可点击tag（border-radius:8px），hover变蓝 | `onclick=openDetail(seg_slug)` |
| 供应链 | 3个子区：上游/下游/合作，ticker（600 weight）+ 物资/说明 | 虚线分隔 `border-bottom:1px dotted var(--border)` |
| 竞争格局 | 竞品列表，红色area tag | `.tag-red` |
| 关联论点 | thesis卡片（status着色 + ★评分），clickable | 复用 `.thesis-card` |

### 6.8 概念卡片详情视图（v2.1 新增）

入口：搜索框输入概念名 → `renderConcept()`

| 区域 | 内容 | CSS |
|------|------|-----|
| Header | name + category（蓝tag）+ difficulty（灰tag）+ heat + confidence | `.detail-header` |
| One-liner | 蓝色左边框卡片，引用格式 | `border-left:4px solid #0071E3` |
| 11模块正文 | 按 body_analogy~body_related_links 逐模块渲染（截断2000字符） | `.card` |
| 关联赛道 | affected_segments → tag链接 | clickable |
| 关联概念 | related_concepts（slug+relation说明） | 虚线分隔，clickable |

### 6.9 知识库仪表盘

内嵌于 `index.html`（原 `dashboard.html` 已废弃整合）。

**布局**：顶部 6 统计卡片 → 知识库结构 + 内容面板（550px 固定高度，滚动）→ 知识流水线 → 复盘验证引擎 → 维护模式 → 快捷入口

| 区域 | 内容 |
|------|------|
| 统计卡片 | 6个 card（总词条/赛道/公司/概念/论点/链接），32px 蓝色数字，2行网格 |
| 知识库结构 | 左栏 280px，四级可折叠树（产业▸层级▸赛道▸公司），点击展开/折叠 |
| 内容面板 | 右栏 flex:1，根据树节点点击动态展示对应表格（赛道列表/TAM/CAGR） |
| 知识流水线 | L0→L1→L2→L3 四步链式卡片，箭头分隔 |
| 复盘验证引擎 | 六维知识质量表 → 论点状态分布堆叠条（单条4色）→ 论点列表（8条/页，翻页） |
| 维护模式 | 双栏（采集 vs 提炼）+ 触发规则说明 |
| 快捷入口 | 5个导航链接（产业链/赛道/公司/概念/论点） |

---

### 6.10 可视化图谱

ECharts 力导向图，展示全知识库实体关联网络。

| 属性 | 值 |
|------|-----|
| 节点类型 | 赛道（绿）、公司（蓝）、概念（紫）、论点（橙） |
| 节点大小 | sqrt(关联数)×14+6，范围 6-55px，去重（同名只保留一个） |
| 连线来源 | wikilinks + segment→company 关系 + thesis→company 关系 |
| 连线样式 | 直线（curveness:0），颜色 #B0B8C0，透明度 0.5 |
| 交互 | 滚轮缩放、拖拽节点、拖拽平移、悬停高亮邻接节点 |
| 点击 | 跳转对应实体详情页 |
| 布局 | 力导向（repulsion:350, gravity:0.1），底部图例 + 操作提示 |

## 七、交互规范

### 7.1 过渡动画

| 元素 | 属性 | 时长 | 缓动 |
|------|------|:--:|------|
| 产业按钮 | all | 0.15s | ease |
| 树节点 | all | 0.15s | ease |
| 视图标签 | all | 0.2s | ease |
| 卡片悬停 | all | 0.3s | ease |
| 进度条 | width | 0.6s | ease |
| 关系条目 | background, padding-left | 0.15s | ease |
| 关系名称 | color | 0.15s | ease |
| 传导步骤 | border-color | 0.15s | ease |
| 证据链接 | background | 0.15s | ease |

### 7.2 悬停 (Hover)

| 元素 | 效果 |
|------|------|
| 产业按钮 | 边框变蓝 + 文字变蓝 |
| 树节点 | 文字变黑 + 背景 `#F5F5F7` |
| 视图标签 | 文字变黑 |
| 卡片 | `box-shadow: 0 8px 32px rgba(0,0,0,0.08)` |
| 热力榜条目 | 文字变蓝 |
| 返回按钮 | opacity 0.7 |
| wikilink 文字 | 下划线 |
| 表格行 | 背景 `var(--bg)` |
| 关系条目 | 背景变灰 + 右移 4px + 名称变蓝 |
| 传导步骤 | 边框变蓝 |
| 证据链接 | 浅蓝背景 + 下划线 |

### 7.3 点击 (Click)

| 元素 | 行为 |
|------|------|
| 产业切换按钮 | `ci = 产业名` → `buildTree()` → `renderView()` |
| 树节点 | `highlightInChart(slug)` — 图表高亮 + 底部提示 |
| 图表节点 | `openDetail(slug)` — 进入详情页 |
| 返回按钮 | `closeDetail()` — 回到图表视图，恢复右侧栏 |
| 关系条目 | `openDetail(slug)` — 跳转关联赛道详情 |
| 视图标签 | 切换图表类型 → `renderView()` |
| 证据链接 | 新窗口打开 URL |

### 7.4 光标 (Cursor)

| 元素 | cursor |
|------|--------|
| 产业按钮 | pointer |
| 树节点 | pointer |
| 视图标签 | pointer |
| 热力榜条目 | pointer |
| wikilink | pointer |
| 关系条目 | pointer |
| 返回按钮 | pointer |
| 传导步骤 | help（有 tooltip） |
| 链接 | pointer |

### 7.5 搜索

输入框 `keyup` 事件（隐式）：匹配 `name.lower().includes(query)`，最多显示 15 条结果。清空搜索框时恢复完整树。

### 7.6 详情页/图表视图切换

- `openDetail(slug)`: 隐藏 `.chart-view`，显示 `.detail-view.active`，隐藏 `.right-col`，更新面包屑
- `closeDetail()`: 恢复 `.chart-view`，隐藏 `.detail-view`，恢复 `.right-col`，重置面包屑

---

## 八、数据嵌入格式

### 8.1 JavaScript 数据对象

```javascript
var DATA = {
  "total": 496,
  "by_type": {"industry": 2, "segment": 74, "company": 392, "concept": 10, "thesis": 18},
  "entities": [
    {
      "name": "GPU",
      "slug": "gpu",
      "type": "segment",
      "industry": "AI算力",
      "layer": 3,
      "tam": 130.0,
      "cagr": 40.0,
      "margin": "65-75%",
      "backlinks": 6,
      "wikilinks": ["HBM高带宽内存", "AI服务器", ...],
      "description": "GPU因数千核心并行计算架构...",
      "cost_share_pct": 55.0,
      "cost_share_context": "AI服务器",
      "profit_pool_pct": 65.0,
      "profit_pool_context": "AI服务器利润池",
      "price_conduction": ["NVIDIA每代GPU涨价30-50%...", "AI服务器ASP持续上涨", "云厂商TCO上升..."],
      "competition": {"global": [{"name": "NVIDIA", "share": "86%", "note": "CUDA生态锁定"}], "china": [], "barriers": [], "tech_gap": []},
      "key_trends": [{"title": "NVIDIA Blackwell性能2x+30x推理吞吐", "detail": "从H100到B200..."}],
      "sources": [{"title": "NVIDIA FY2026 Annual Report", "summary": "数据中心营收$193.7B", "url": "https://investor.nvidia.com"}],
      "key_inputs": ["HBM高带宽内存", "CoWoS先进封装", "先进制程"],
      "key_customers": ["云厂商", "AI实验室", "企业AI"],
      "companies": []
    }
    // ... 495 more
  ]
}
```

### 8.2 数据嵌入方式

`build_wiki_data.py` 编译 L2 MD 文件生成 `wiki_data.json`，然后手动嵌入或脚本嵌入 index.html 的 `<script>var DATA = ...</script>` 标签中。

---

## 九、响应式（当前状态）

当前为桌面端优化设计（≥1280px），未实现移动端断点适配。已知限制：
- 侧边栏固定 260px，小屏会挤压内容区
- 右侧栏固定 280px，无折叠机制
- 4 列统计卡片在小屏不会自动折叠
- 图表最小高度 440px

---

## 十、前端依赖

| 依赖 | 版本/URL | 用途 |
|------|---------|------|
| Tailwind CSS | CDN latest | 原型工具类（核心布局用自定义 CSS） |
| ECharts | 5.6.0 CDN | 4 个图表的渲染引擎 |
| Lucide Icons | CDN latest | 图标（当前未大量使用，预留） |

---

## 十一、部署

1. 确保 `L3-网页产物/wiki_data.json` 为最新编译（`python build_wiki_data.py`）
2. 部署到任意静态文件服务器（index.html + wiki_data.json）
3. 无需构建、无需 Node.js、无需数据库

```bash
cd invest_wiki/L3-网页产物
python3 -m http.server 8760
# 浏览器打开 http://localhost:8760/index.html
# 7 个页面均通过左侧导航切换，无需独立 URL
```
