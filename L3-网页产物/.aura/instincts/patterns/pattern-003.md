---
id: pattern-003
category: api
language: unknown
score: 50
tags: [api]
---

## 컨텍스트
파일: DESIGN.md (Write 완료)

## 핵심 코드
```unknown
# Invest Wiki 知识库设计文档

> 版本 2.0 · 2026-07-20 · LLM-Wiki 四层架构

---

## 一、项目概述

### 1.1 定位

Invest Wiki 是一个基于 **LLM-Wiki 范式** 的 AI 产业链知识库。以 Markdown + YAML + `[[wikilink]]` 为数据模式，通过 LLM 采集管线持续更新，编译为交互式可视化网页。

### 1.2 对标设计

| Karpathy LLM-Wiki | Invest Wiki 实现 |
|-------------------|-----------------|
| Raw Sources（LLM 只读） | L0 原始资料层 |
| The Wiki（LLM 维护的 MD） | L2 结构化 Wiki 层 |
| The Schema（操作规范） | L1 Schema & Pipeline 层 |
| — | L3 网页产物层（Invest Wiki 特有） |

Invest Wiki 在标准三层之上增加了 **L2 结构化 Wiki 层**（因为产业链数据需要 25 个精确格式化字段）和 **L3 网页产物层**（编译 MD → 交互式 SPA）。

### 1.3 数据规模

| 类型 | 数量 |
|------|:--:|
| 产业 | 2（AI算力 / 半导体） |
| 赛道 | 74 |
| 公司 | 398 |
| 总词条 | 474 |

---

## 二、四层架构

```
invest_wiki/
├── CLAUDE.md                         ← 项目入口
│
├── L0-原始资料池/                     ← Raw Sources
│   ├── 01-研报/                       ← 券商/研究机构报告
│   ├── 02-财报/                       ← 季报/年报/Earnings Call
│   ├── 03-新闻/                       ← 行业新闻/公司公告
│   ├── 04-行业数据/                    ← TrendForce/IDC/Gartner 等
│   ├── 05-用户输入/                    ← 用户直接发送的内容
│   └── _attachments/                  ← 原始 PDF/Excel/图片
│
├── L1-Schema与Pipeline/               ← Schema & Pipeline
│   ├── CLAUDE.md                      ← LLM 操作宪法（每次操作前必读）
```

## 태그
- api