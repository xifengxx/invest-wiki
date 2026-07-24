# 概念卡片字段规范（concept-schema）

每个概念（concept）MD 文件的 YAML frontmatter 必须包含以下字段。

## 字段总表

| # | 字段 | 类型 | 必填 | 格式要求 |
|---|------|------|:--:|---------|
| 1 | name | str | ✅ | 概念名称，如 "HBM高带宽内存" |
| 2 | slug | str | ✅ | 英文短标识，如 "hbm" |
| 3 | type | str | ✅ | 固定值 `"concept"` |
| 4 | category | str | ✅ | 技术 / 商业模式 / 行业术语 / 政策 / 市场 |
| 5 | difficulty | str | ✅ | 入门 / 中级 / 高级 |
| 6 | confidence | str | - | 知识置信度：高 / 中 / 低 |
| 7 | one_liner | str | ✅ | 一句话解释，20~30字 |
| 8 | fable_title | str | - | 生活化类比标题 |
| 9 | affected_segments | list | - | 关联赛道 slug 数组 |
| 10 | affected_companies | list | - | 关联公司 slug 数组（核心参与者） |
| 11 | heat | str | - | 热度：高热 / 趋势 / 稳定 / 冷却 |
| 12 | tags | list | - | 标签 |
| 13 | related_concepts | list | - | 关联概念列表，见子字段 |
| 14 | updated | str | ✅ | 更新日期，格式 `YYYY-MM` |

---

## 字段详解

### 4. category（概念分类）

| 值 | 含义 | 示例 |
|----|------|------|
| 技术 | 具体技术/工艺/架构 | HBM、CoWoS、CPO、Chiplet、TSV |
| 商业模式 | 商业逻辑/盈利方式 | Fabless、SaaS、平台经济 |
| 行业术语 | 行业专有名词 | CAGR、TAM、ASP |
| 政策 | 政策/法规概念 | CHIPS法案、出口管制、大基金 |
| 市场 | 市场现象/周期 | 存储周期、半导体周期 |

### 5. difficulty（难度等级）

| 值 | 含义 |
|----|------|
| 入门 | 不需要专业知识即可理解 |
| 中级 | 需要一定行业背景 |
| 高级 | 需要专业领域知识 |

### 6. confidence（知识置信度）

- 高：数据来源明确，多方验证
- 中：基于公开信息推断，存在不确定性
- 低：领域变化快或信息不完整

### 7. one_liner（一句话解释）

20~30字，大白话定义，让完全不懂的人一眼看懂。

```yaml
one_liner: "将多个DRAM芯片垂直堆叠封装，用硅通孔连接，让GPU能更快读写数据的超高带宽内存"
```

### 9. affected_segments（关联赛道）

概念所涉及的产业链赛道 slug 列表。

```yaml
affected_segments: ["gpu", "cowos", "ai-server", "hbm"]
```

### 10. affected_companies（关联公司）

概念最直接相关的公司 slug 列表（核心参与者，非沾边概念股）。

```yaml
affected_companies: ["sk-hynix", "samsung-elec", "micron"]
```

### 13. related_concepts（关联概念）

```yaml
related_concepts:
  - slug: "cowos"          # 关联概念 slug
    relation: "HBM通过CoWoS封装与GPU互联"  # 一句话关联说明
  - slug: "cxl"
    relation: "可能的替代技术路线"
```

---

## 正文模块（11 个模块）

概念卡片的 MD 正文遵循固定的 11 模块结构（详见 `concept-card/SKILL.md`）：

```
# {name}

> **{one_liner}** | {category} · {difficulty}级

## 一、生活化类比：{fable_title}
## 二、专业但通俗的定义
## 三、为什么市场会关注它
## 四、产业链位置
## 五、相关公司和板块
## 六、投资关注点
## 七、风险提示
## 八、如何判断是真逻辑还是炒概念
## 九、后续追踪指标
## 十、相关概念链接

> ⚠️ 免责声明：本内容仅作概念科普和产业认知框架搭建，不构成任何投资建议。
```

---

## 完整示例

```yaml
---
name: "HBM高带宽内存"
slug: "hbm"
type: "concept"
category: "技术"
difficulty: "中级"
confidence: "高"
one_liner: "将多个DRAM芯片垂直堆叠封装，通过硅通孔连接，让GPU能更快读写数据的超高带宽内存"
fable_title: "快递驿站升级版"
affected_segments: ["gpu", "hbm", "cowos", "ai-server"]
affected_companies: ["sk-hynix", "samsung-elec", "micron"]
heat: "高热"
tags: ["AI芯片", "先进封装", "存储", "HBM"]
related_concepts:
  - slug: "cowos"
    relation: "HBM通过CoWoS封装与GPU互联"
  - slug: "tsv"
    relation: "HBM的核心技术——硅通孔垂直互联"
  - slug: "cxl"
    relation: "可能的替代技术路线，内存池化共享"
  - slug: "gpu"
    relation: "HBM的直接下游，GPU的核心瓶颈组件"
updated: "2026-07"
---
```
