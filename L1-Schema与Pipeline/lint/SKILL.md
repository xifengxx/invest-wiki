---
name: invest-wiki-lint
description: |
  Invest Wiki 健康检查 Skill。扫描 L2-Wiki 的 511 个词条，检测矛盾、过期、孤立、格式违规四类问题，
  生成结构化健康报告。

  核心目标：
  1. 检测数据矛盾（不同文件中同一赛道 TAM 冲突等）
  2. 检测信息过期（引用过时、年份过旧）
  3. 检测孤立页面（无引用、无关联）
  4. 检测格式合规（competition/price_conduction/key_trends 格式）

  触发条件：用户说"检查知识库" / "lint" / "健康检查" / "扫描" 时。
  也可作为定期 cron 任务自动触发（建议每月一次）。
version: "1.0.0"
author: "Invest Wiki"
trigger_keywords:
  - "检查知识库"
  - "lint"
  - "健康检查"
  - "扫描"
  - "audit"
  - "质量检查"
---

# Invest Wiki Lint 健康检查 Skill

## 一、核心定位

Lint 是 Invest Wiki 的"免疫系统"——定期扫描 L2-Wiki，确保数据新鲜、一致、完整。

## 二、四维扫描

### 维度 1: 矛盾检测

**检测规则**：

| 检测项 | 方法 | 严重度 |
|--------|------|:--:|
| 同名赛道 TAM 冲突 | 对比消化笔记中建议的 TAM 与 L2 中的当前值，差值 > 20% | 🔴 高 |
| 关联链断裂 | wikilinks 指向的名称在 L2-Wiki 中不存在 | 🔴 高 |
| 公司所属赛道矛盾 | 同一公司在不同赛道中出现但描述的角色不一致 | 🟡 中 |
| 层级分类冲突 | 同一赛道在不同产业中 layer 不同但应为同一层 | 🟡 中 |

### 维度 2: 过期检测

**检测规则**：

| 检测项 | 方法 | 严重度 |
|--------|------|:--:|
| 引用过期 | sources 中最新年份 < 当前年份-1（即来源超过 12 个月） | 🟡 中 |
| 年份陈旧 | description 或 key_trends 中包含已过去的年份（如 2025） | 🟢 低 |
| 判断窗口已过 | 消化笔记中的判断句验证时间窗口已过但未标记 | 🟡 中 |
| 长期未更新 | 文件 updated 字段超过 6 个月 | 🟢 低 |

### 维度 3: 孤立检测

**检测规则**：

| 检测项 | 方法 | 严重度 |
|--------|------|:--:|
| 孤立赛道 | backlinks = 0（无其他赛道引用） | 🟡 中 |
| 孤立公司 | 未出现在任何赛道的 companies 列表中 | 🟢 低 |
| 孤立消化笔记 | 未被任何赛道引用（动态更新记录中无链接） | 🟢 低 |

### 维度 4: 格式合规

**检测规则**（基于 `schemas/field-formats.md` v2.0 结构化 YAML 格式）：

| 检测项 | 方法 | 严重度 |
|--------|------|:--:|
| competition 类型 | 检查 competition 是否为 dict（`{global, china, barriers, tech_gap}`），非 dict 则为格式错误 | 🔴 高 |
| competition 旧格式残留 | 检查 competition 值是否为字符串且包含旧分隔符（`⚔️` / `\|\|` / `🔒` / `📐`），出现即未迁移 | 🔴 高 |
| competition 子字段完整性 | 检查 dict 中 global/china/barriers/tech_gap 的 list item 是否包含必填字段（name/share/note, item/detail, dimension/detail） | 🔴 高 |
| key_trends 类型 | 检查 key_trends 是否为 list，非 list 则为格式错误 | 🔴 高 |
| key_trends 旧格式残留 | 检查数组中元素是否为字符串（如 `1)——` 或 `——` 分隔符），而非 `{title, detail}` 对象 | 🟡 中 |
| price_conduction 类型 | 检查 price_conduction 是否为 list of strings，单个 string 为旧格式 | 🟡 中 |
| price_conduction 旧格式残留 | 检查元素是否为使用 `⇒` 作为步骤分隔符的单一长字符串 | 🟡 中 |
| sources 类型 | 检查 sources 是否为 list，非 list 则为格式错误 | 🔴 高 |
| sources 旧格式残留 | 检查元素是否为字符串（`;` 分隔或 URL 在括号内），而非 `{title, summary, url}` 对象 | 🔴 高 |
| key_inputs 类型 | 检查 key_inputs 是否为 list of strings，逗号分隔的单一 string 为旧格式 | 🟡 中 |
| key_customers 类型 | 检查 key_customers 是否为 list of strings，逗号分隔的单一 string 为旧格式 | 🟡 中 |
| YAML 必要字段 | 检查 name/slug/industry/layer/tam/cagr/description 非空 | 🔴 高 |

## 三、扫描流程

```
Step 1: 遍历 L2-Wiki/赛道/**/*.md，解析 YAML frontmatter
Step 2: 四维扫描，逐项检查
Step 3: 按严重度排序输出报告
Step 4: 对 🔴高 严重度项生成修复建议
```

## 四、输出格式

```
🔍 Invest Wiki 健康检查报告 — {日期}
扫描范围: L2-Wiki/ (74 赛道, 401 公司, 2 产业, 10 概念, 16 论点)

═══════════════════════════════════
🔴 严重 (需立即处理): {N} 项
═══════════════════════════════════

🔗 关联链断裂 (2)
  - [[FPGA]] ← GPU.wikilinks: FPGA 实际在 L2-Wiki/赛道/半导体/ 中
  - [[某不存在的赛道]] ← AI服务器.wikilinks: 目标页面不存在

═══════════════════════════════════
🟡 警告 (建议近期处理): {N} 项
═══════════════════════════════════

⏰ 引用过期 (3)
  - MCU与嵌入式处理器: sources 最新为 2025年
  - FPGA: key_trends 包含 "2025年..."
  - 半导体设备零部件: updated: 2026-01 (6个月未更新)

🔗 孤立赛道 (1)
  - 高速连接器与铜缆: backlinks = 0

📐 格式问题 (2)
  - 模拟芯片: price_conduction 为单一 string（应改为 list of strings）
  - RISC-V AI芯片: key_trends 中 2/4 项为 string 而非 {title, detail} 对象

═══════════════════════════════════
🟢 提示 (可选处理): {N} 项
═══════════════════════════════════

  - 8 家公司未关联到任何赛道
  - 3 份消化笔记超过 3 个月未处理

───────────────────────────────────
✅ 格式合规率: 70/74 赛道 (94.6%)
📊 数据新鲜度: 平均更新日期 2026-07
```

## 五、与 collector 的协同

```
采集管线的判断句  →  Lint 追踪池  →  定期验证  →
标记 已兑现/证伪/过期  →  回写赛道文件  →  触发重新采集
```
