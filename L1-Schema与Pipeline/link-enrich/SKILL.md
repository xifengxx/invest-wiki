---
name: invest-wiki-link-enrich
description: |
  Invest Wiki 链接增强 Skill。逐赛道检查 wikilinks 是否遗漏了明显关联
  （同层竞争、上下游依赖、技术替代、协同互补），补充缺失的双向链接。

  核心目标：
  1. 将平均链接数从 2.1 提升到 5+ 条/赛道
  2. 将孤立赛道（backlinks=0）数量从 37 降到 <10
  3. 确保每条链接都是真实的产业链关联，不是人为填充

  触发条件：用户说 "增强链接" / "补充关联" / "enrich links" 时。
  建议频率：每次新增赛道后运行一次。
version: "1.0.0"
author: "Invest Wiki"
trigger_keywords:
  - "增强链接"
  - "补充关联"
  - "enrich links"
  - "链接优化"
---

# Invest Wiki 链接增强 Skill

## 一、核心定位

Lint 扫描发现 37/74 赛道 backlinks=0，平均链接数 2.1 条/赛道。需要系统性地丰富 wikilinks，提升关系图谱密度。

## 二、链接类型

| 类型 | 说明 | 示例 |
|------|------|------|
| **上游供应** | A 是 B 的关键输入 | HBM → GPU, CoWoS → GPU |
| **下游应用** | B 是 A 的关键客户 | GPU → AI服务器, GPU → 自动驾驶 |
| **同层竞争/替代** | A 和 B 在同一层，可能替代或互补 | GPU ↔ ASIC, FPGA ↔ ASIC |
| **技术依赖** | A 依赖 B 的技术或标准 | Chiplet ↔ 先进封装CoWoS |
| **协同互补** | A 和 B 一起工作，各自不可替代 | GPU ↔ HBM, 光模块 ↔ 交换芯片 |

## 三、执行流程

1. Read `L2-Wiki/index.md` 建立全局视图
2. 对每个赛道（特别是 backlinks < 3 的），Read 其 MD 文件
3. 基于以下信号判断是否缺少链接：
   - `key_inputs` 和 `key_customers` 中提到的赛道名
   - `competition` 中提到的竞争赛道
   - `description` 中提到的其他赛道
   - 同层（layer）的其他赛道 → 可能的竞争/互补关系
4. 对每个发现的缺失链接，追加到 wikilinks YAML 字段
5. 确保双向链接（如果 A 链接了 B，B 也应链接 A）
6. 更新 `L2-Wiki/index.md` 的统计数字

## 四、质量要求

- 每条新增链接必须能在赛道描述或关键趋势中找到依据
- 不要为了凑数而添加虚假链接
- 优先补强孤立赛道（backlinks=0）
- 竞争关系标记为 wikilink（与供应关系同样重要）
