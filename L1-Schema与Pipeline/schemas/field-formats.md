# 字段格式规范（field-formats）

三个复杂字段的结构化 YAML 格式定义。LLM 填充时必须严格遵守，确保 L3 前端渲染正确。

> **v2.0 更新**：competition、key_trends、price_conduction、sources 已从字符串格式迁移为结构化 YAML。前端通过 `Array.isArray()` / `typeof === 'object'` 优先使用结构化数据。
> 旧字符串格式的 body 段（`## 竞争格局` / `## 关键趋势` 等）已移除，YAML 是唯一数据源。

---

## 1. competition（竞争格局）

### YAML 结构

```yaml
competition:
  global:
    - {name: "厂商名", share: "份额%", note: "备注说明"}
    - {name: "厂商名", share: "份额%", note: "备注说明"}
  china:
    - {name: "厂商名", share: "份额%", note: "备注说明"}
  barriers:
    - {item: "壁垒名称", detail: "壁垒详细说明"}
    - {item: "壁垒名称", detail: "壁垒详细说明"}
  tech_gap:
    - {dimension: "差距维度", detail: "差距详细说明"}
```

### 子字段说明

| 段 | 字段 | 含义 | 必填 |
|----|------|------|:--:|
| `global` | list | 全球市场竞争格局 | ✅ |
| `global[].name` | str | 厂商名称 | ✅ |
| `global[].share` | str | 市场份额，如 "86%"、"~35%" | ✅ |
| `global[].note` | str | 核心竞争力备注，≤80字 | ✅ |
| `china` | list | 中国市场竞争格局 | - |
| `china[].name` | str | 厂商名称 | ✅ |
| `china[].share` | str | 市场份额，如 "-"（未知时） | ✅ |
| `china[].note` | str | 备注说明 | ✅ |
| `barriers` | list | 进入壁垒 | - |
| `barriers[].item` | str | 壁垒名称，≤20字 | ✅ |
| `barriers[].detail` | str | 壁垒详细说明，≤100字 | ✅ |
| `tech_gap` | list | 技术代差 | - |
| `tech_gap[].dimension` | str | 差距维度，≤20字 | ✅ |
| `tech_gap[].detail` | str | 差距说明，≤100字 | ✅ |

### 前端渲染

- `global` / `china` → 表格（厂商/份额/备注三列）
- `barriers` → 表格（壁垒项/难度/说明三列，难度固定显示「高」）
- `tech_gap` → 表格（维度/差距/说明三列，差距固定显示「大」）

### 示例

```yaml
competition:
  global:
    - {name: "NVIDIA", share: "86%", note: "数据中心AI GPU绝对垄断，CUDA生态锁定90%+开发者"}
    - {name: "AMD", share: "8%", note: "MI300X $6-8B→MI350/MI400追赶，ROCm生态差距仍大"}
    - {name: "Intel", share: "<2%", note: "Gaudi/Habana→Falcon Shores基本退出AI GPU"}
  china:
    - {name: "华为昇腾", share: "-", note: "Ascend 910B国产替代首选，特定场景有应用"}
    - {name: "寒武纪", share: "-", note: "688256思元MLU云端推理"}
  barriers:
    - {item: "CUDA生态锁定", detail: "90%+AI框架基于CUDA，软件成熟度93%利用率vs AMD 45%，替代成本极高"}
    - {item: "架构迭代+全栈整合", detail: "GPU+NVLink+InfiniBand+CUDA形成完整护城河，新进入者无法在短期内复制"}
    - {item: "制程+HBM供应", detail: "先进制程和HBM产能受限，NVIDIA凭借规模优势优先获得产能"}
  tech_gap:
    - {dimension: "芯片算力", detail: "国产黑芝麻A1000(58 TOPS) vs NVIDIA Thor(2000 TOPS)差距~35x"}
    - {dimension: "软件生态", detail: "CUDA 300万+开发者 vs 国产生态<10万，软件栈差距>5年"}
```

---

## 2. key_trends（关键趋势）

### YAML 结构

```yaml
key_trends:
  - title: "趋势标题（≤40字）"
    detail: "趋势详细描述（≤140字）"
  - title: "趋势标题"
    detail: "趋势描述"
```

### 规则

- 每条趋势是一个 `{title, detail}` 对象
- `title`：≤40字，简洁概括趋势
- `detail`：≤140字，展开说明具体数据、影响
- 通常 5-10 条
- 按重要性排序

### 前端渲染

- 趋势列表项，标题粗体 + 描述正文
- 标题超长自动截断并加「…」

### 示例

```yaml
key_trends:
  - title: "NVIDIA FY2026数据中心$193.7B(+68% YoY)，Blackwell占88%"
    detail: "从H100到B200性能2x训练+30x推理吞吐(GB200)，迭代加速到1年，Vera Rubin平台进入全面量产"
  - title: "推理市场增速(60%+)超过训练(30%+)，FP4精度让单卡跑4个70B模型"
    detail: "NVIDIA Rubin架构2.3kW TDP/22.2TB/s带宽/40%能效提升，推理成为GPU增长新引擎"
  - title: "AMD MI400+Helios平台2026年挑战"
    detail: "OpenAI 6GW多年度部署，目标推理20%份额，但软件利用率45% vs NVIDIA 93%"
```

---

## 3. price_conduction（价格传导）

### YAML 结构

```yaml
price_conduction:
  - "步骤1的完整描述"
  - "步骤2的完整描述"
  - "步骤3的完整描述"
```

### 规则

- 数组元素按传导链路顺序排列
- 每个元素是一个完整的因果环节描述（一句话）
- 通常 3-7 个步骤
- 步骤内部可使用 `→` 表示比较关系，如 "H100 $30K→B200 $40K+"

### 前端渲染

- 提取每个步骤的逗号前首段作为短标签，横向排列 → 箭头连接
- 下方显示完整传导链文本（用 ` → ` 拼接）

### 示例

```yaml
price_conduction:
  - "NVIDIA每代GPU涨价30-50%（H100 $30K→B200 $40K+）"
  - "AI服务器ASP持续上涨"
  - "云厂商TCO上升。但云厂商转嫁能力较强（AI服务按Token/小时定价可灵活调价）"
  - "最终成本部分由AI应用开发者和终端用户承担。GPU涨价加速云厂商自研芯片和ASIC替代趋势"
```

---

## 4. sources（研报来源）

### YAML 结构

```yaml
sources:
  - title: "机构名+报告名+日期"
    summary: "1-2句与该赛道相关的关键内容摘要"
    url: "https://..."
  - title: "机构名+报告名"
    summary: "摘要"
    url: "(内部路径)"
```

### 规则

- 每条来源是一个 `{title, summary, url}` 对象
- `title`：机构名+报告名+日期（如有），≤120字
- `summary`：与本赛道/页面相关的1-2句关键内容，≤200字
- `url`：完整 URL 或内部路径，无链接时为空字符串
- 内部路径：`L0-原始资料池/...` 格式
- 通常 3-8 条来源

### 前端渲染

- 编号列表，标题粗体 + 摘要正文 + 链接可点击
- 链接显示域名简写

### 示例

```yaml
sources:
  - title: "NVIDIA FY2026 Annual Report"
    summary: "FY2026数据中心营收$193.7B(+68% YoY)，Blackwell GPU出货2.97M颗占计算收入88%"
    url: "https://investor.nvidia.com"
  - title: "中原证券《电子行业2026年中期策略》"
    summary: "Agentic AI时代CPU:GPU比例从1:8转向1:1，云厂商Capex CAGR 46%"
    url: "L0-原始资料池/01-研报/2026-06-23-电子行业2026年中期策略-中原证券.md"
```

---

## 5. wikilinks（关联词条）

### 格式

```yaml
wikilinks:
  - "HBM高带宽内存"
  - "AI服务器"
  - "ASIC/AI定制芯片"
```

### 规则

- 数组元素为赛道/公司的**完整中文名称**，不是 slug
- 名称必须与 L2-Wiki 中已存在的实体精确匹配
- Parser 自动计算反向引用（backlinks）
- 前端根据 key_inputs/key_customers 和层级差自动推导关系类型（上游供应/下游应用/协同互补）

---

## 6. companies（核心标的）

### 格式

```yaml
companies:
  - ticker: "NVDA"
    name: "NVIDIA"
    role: "全球龙头"
    rev: 85
  - ticker: "688041"
    name: "寒武纪"
    role: "国产替代"
    rev: 15
```

### 规则

- `ticker`: 美股用字母代码，A股用 6 位数字代码
- `name`: 公司中文/英文全称
- `role`: 角色标签（全球龙头/国产替代/二线厂商/弹性标的/概念相关）
- `rev`: 该赛道营收占比（百分比，纯数字）
- 前端根据 role 自动着色

---

## 7. thesis_evidence（论点证据项）

### 格式

论点 MD 的 body 中，证据使用 3 行格式：

```markdown
1. 证据内容描述
   ——来源: 来源标题
   (URL或内部路径)
```

### 规则

- 第1行：编号 + 证据内容描述
- 第2行：`——来源: ` + 来源标题（3空格缩进）
- 第3行：`(URL或路径)`（3空格缩进），无链接时省略
- 支撑证据（`## 支撑证据`）和反对证据（`## 反对证据`）使用相同格式
- build 脚本的 `_parse_thesis_evidence()` 自动解析为 `[{content, source_title, source_url}]` 结构化数组
- 前端渲染：证据内容正文 + 来源标题蓝色小字 + 链接可点击
