# Invest Wiki — LLM-Wiki 产业链知识库

> **当前状态**：489 实体 / 18 论点 / 0 unknown / 全部验证通过（2026-08-17）

## 定位

独立的 LLM-Wiki 知识库系统，采用 Markdown + YAML + [[wikilink]] 的数据模式。
对标 Karpathy LLM-Wiki 三层架构，扩展为四层以适应结构化产业链数据需求。

## 四层架构

```
L0-原始资料池/      ← Raw Sources（LLM 只读不写）
L1-Schema与Pipeline/ ← Schema & Pipeline（操作规范、Ingest/Lint Skill）
L2-Wiki/            ← The Wiki（结构化 YAML + MD 词条）
L3-网页产物/         ← Web Output（编译生成 index.html）
```

**操作规范**: 所有 Wiki 操作必须先读 `L1-Schema与Pipeline/CLAUDE.md`
**查询路由**: 回答任何涉及赛道/实体的问题前，先读 `L2-Wiki/index.md` 定位相关页面
**L0 归档强制**: 所有 WebSearch/WebFetch 结果必须先写入 L0 归档文件，再转化到 L2。详见 L1 操作规范「Web调研 L0 归档规范」

## 数据规模

| 类型 | 数量 |
|------|:--:|
| 产业 | 2 |
| 赛道 | 81 |
| 公司 | 385（78家完整数据[Tier1:51 + Tier2:26 + 财报季新增:1]，305家骨架，2家中等） |
| 概念卡片 | 10 |
| 投资论点 | 18 |
| 总词条 | 489 |
| QA 版本 | v1.3 |

## 使用方式

```bash
cd ~/Claude_projects/5factor_system/invest_wiki

# 1. 从 invest_kg JSON 迁移（首次，已完成，脚本已归档至 engine/）
# python engine/seed_json_to_md.py

# 2. 测试 Wiki 引擎
python -c "
import sys; sys.path.insert(0, '.')
from engine.parser import WikiParser
wiki = WikiParser('L2-Wiki')
wiki.parse_all()
print(f'{len(wiki.entities)} 词条')
for e in wiki.get_hot(5):
    print(f'  {e.backlink_count:4d} ← {e.name}')
"

# 3. LLM 采集更新
# 见 L1-Schema与Pipeline/collector/执行指令-采集处理.md

# 4. 生成 HTML（L2 → L3 编译）
# python L3-网页产物/build_wiki_data.py

# 5. 预览
cd L3-网页产物 && python3 -m http.server 8760

# 6. Lint 健康检查
# 见 L1-Schema与Pipeline/lint/执行指令-定期扫描.md

# 7. 提炼模式（质量审计）
# 见 L1-Schema与Pipeline/CLAUDE.md 维护模式章节
```

## 目录结构

```
invest_wiki/
├── CLAUDE.md              ← 本文件（项目入口）
├── seed_json_to_md.py     ← 一次性迁移脚本
├── engine/                ← Wiki 引擎
│   ├── parser.py          ← YAML + [[wikilink]] 解析
│   └── graph.py           ← ECharts 图数据构建
├── L0-原始资料池/          ← 原始研报/财报/新闻
├── L1-Schema与Pipeline/    ← 操作规范 + Ingest/Lint Skill
│   ├── CLAUDE.md          ← L1 操作规范
│   ├── schemas/           ← 4套 Schema（segment/company/concept/thesis）
│   ├── templates/         ← 5套模板（segment/company/concept/thesis/digest）
│   ├── collector/         ← 采集 Skill
│   ├── lint/              ← Lint 健康扫描 Skill
│   ├── link-enrich/       ← 链接增强 Skill
│   └── concept-card/      ← 概念卡片科普 Skill
├── L2-Wiki/               ← 结构化知识词条
│   ├── index.md           ← 81赛道总索引
│   ├── 产业/ (2) / 赛道/ (81) / 公司/ (385)
│   ├── 概念/ (10)         ← 11模块概念卡片
│   ├── 论点/ (18)         ← 投资论点追踪
│   └── 消化笔记/           ← L0→L2 中间产物
└── L3-网页产物/            ← 网页输出
    ├── index.html          ← 单文件 SPA（7页面：全景/赛道/公司/概念/论点/知识库/可视化图谱）
    ├── wiki_data.json      ← 编译中间数据
    ├── build_wiki_data.py  ← L2→L3 编译脚本
    └── validate.py         ← 格式验证
```

## 排序算法

```
综合分 = TAM_bn ÷ max(TAM) × 60 + backlink_count ÷ max(backlinks) × 40
```

## 前端功能

- **7 个导航页面**: 产业链图谱 / 赛道分析 / 个股关联 / 概念卡片 / 论点 / 知识库 / 可视化图谱
- **4 个图视图**: Treemap 规模 / 关系网络 / Sankey 流向 / 因果传导，左侧产业链树 + 右侧图表
- **全局搜索**: Topbar 居中搜索框，支持中英文/代码搜索，实时下拉匹配
- **赛道详情页**: 11 个模块（市场规模、定位定义、价值链、上下游、竞争格局、关键趋势、关联关系、研报证据、核心标的、矛盾追踪、投资论点）
- **公司详情页**: 覆盖385家公司，8个模块 — Header(名称/代码/国家/角色/层级) → 公司介绍(定位+核心业务+盈利模式) → 详细信息(YAML概览网格+Body 4段深度资料) → 产业链定位 → 上下游关系图谱+供应链关系链 → 竞争格局对比 → 关联赛道 → 关联论点
- **概念卡片详情页**: 11模块科普（HBM/CoWoS/CPO/Chiplet/ASIC），含寓言类比+真伪鉴别
- **投资论点详情页**: 核心主张 + 支撑证据/反对证据 + 待验证假设 + 关联赛道/公司
- **知识库仪表盘**: 内嵌于 index.html — 统计面板 + 四级知识树 + 内容面板 + 知识流水线 + 复盘验证引擎（六维质量 + 论点状态分布 + 论点列表）
- **可视化图谱**: ECharts 力导向图，节点按类型着色，连线展示实体关联，点击跳转详情
- 产业切换: AI算力 / 半导体

---

## 路线图

### Phase 2: 公司深化 ✅ 完成（2026-07-23）

| 批次 | 范围 | 数量 | 状态 |
|------|------|:--:|:--:|
| Tier 1 | 市值前 50 的半导体/AI 公司 | 51（含3家新建） | ✅ 完成 |
| Tier 2 | 产业链关键环节龙头 | 26 | ✅ 完成 |
| Tier 3 | 其余骨架公司 | 256 | ⏳ 按需补充 |

Tier 1 完成详情：7 批次（A1-A7），遵循 Research 模式（WebSearch → L0归档 → MD更新 → 编译 → 验证），覆盖全球半导体/AI市值前50强 + 3家新建（Astera Labs/Credo/Technoprobe），每家公司13-14/14字段完整填充。L0归档文件：`L0-原始资料池/03-新闻/2026-07-23-B5批次-5家半导体公司-数据溯源.md` + `B6批次-30家半导体公司-数据溯源.md`。

Tier 2 完成详情：5 批次（B1-B5），26家产业链关键环节龙头（硅片/光刻胶/特气/设备子系统/封测/EDA/数据中心基础设施/化合物半导体/特色代工），同样遵循 Research 模式。L0归档文件：`L0-原始资料池/03-新闻/2026-07-23-B7批次-26家产业链公司-数据溯源.md`。

### Phase 3: 数据保鲜 ✅ 完成（2026-07-23）

- 78 家深度覆盖公司全部添加 `data_freshness_date` 字段（Phase 3完成时77家，后续新增1家）
- 公司 Schema 新增第 18 号字段 `data_freshness_date`（必填）
- `L3-网页产物/freshness_scan.py` 扫描器：月度检测，90 天阈值过期标记
- 财报季（1/4/7/10月）自动提醒刷新
- 使用方式：`python L3-网页产物/freshness_scan.py [--days 60] [--json]`

### Phase 4: 论点闭环 ✅ 完成（2026-07-23 Q3审计）

- Q3审计（16条时）：3 confirmed / 9 active / 4 forming / 0 invalidated。审计后新增2条（五红灯框架+证据鸿沟），当前18条
- Active→Confirmed: AI推理增速>训练、NVIDIA GPU垄断3年、TSMC先进制程独大
- CPU重回数据中心核心: 置信度 7→8（Agentic AI新证据）
- 审计报告: `L2-Wiki/论点/2026-Q3-audit.md`
- 机制: 每季度审计（1/4/7/10月），parser.py 自动排除 `*audit*` 文件

### Phase 5: 前端可用性 ✅ 完成（2026-07-23）

- 公司列表排序：市值↓↑ / 名称 A-Z / 引用数↓
- 公司列表筛选：国家（美/台/中/日/韩/荷/德/英/瑞/以）+ 产业链层级（L1-L4）
- 数据新鲜度可视化：卡片标题旁绿点(≤30天)/橙点(31-90天)/红点(>90天)，图例在筛选栏右侧
- 市值直接在 Ticker 行显示（如 `NVDA $4.80T`）
- 移动端适配延后（性价比低）
