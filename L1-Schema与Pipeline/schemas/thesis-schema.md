# 论点字段规范（thesis-schema）

每条论点（thesis）MD 文件的 YAML frontmatter 必须包含以下字段。

## 字段总表

| # | 字段 | 类型 | 必填 | 格式要求 |
|---|------|------|:--:|---------|
| 1 | name | str | ✅ | 论点标题，≤60字 |
| 2 | slug | str | ✅ | 英文短标识，与文件名一致 |
| 3 | type | str | ✅ | 固定值 `"thesis"` |
| 4 | thesis_status | enum | ✅ | `forming` / `active` / `invalidated` / `confirmed` |
| 5 | confidence | int | ✅ | 1-10，表示对该论点的置信程度 |
| 6 | created | str | ✅ | 创建日期，格式 `YYYY-MM-DD` |
| 7 | updated | str | ✅ | 更新日期，格式 `YYYY-MM-DD` |
| 8 | affected_segments | list | ✅ | 关联赛道 slug 数组 |
| 9 | affected_companies | list | - | 关联公司 ticker 数组 |
| 10 | tags | list | - | 标签，英文小写 |

## thesis_status 说明

| 状态 | 含义 |
|------|------|
| `forming` | 论点正在形成中，证据不完整 |
| `active` | 活跃论点，正在被跟踪验证 |
| `invalidated` | 已被反证推翻 |
| `confirmed` | 已被充分验证确认 |

## confidence 说明

- 1-3: 推测性质，证据薄弱
- 4-6: 有一定证据支持，需进一步验证
- 7-8: 多数证据支持，论点可信
- 9-10: 证据充分，论点确立

## 示例

```yaml
---
name: "NVIDIA GPU垄断地位在未来3年内不可撼动"
slug: "nvidia-gpu-monopoly-3yr"
type: "thesis"
thesis_status: "active"
confidence: 8
created: "2026-07-20"
updated: "2026-07-20"
affected_segments: ["gpu", "ai-server", "asic-ai-chip", "hbm"]
affected_companies: ["NVDA", "AMD", "INTC"]
tags: ["ai", "gpu", "competition"]
---
```
