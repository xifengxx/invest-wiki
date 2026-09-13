---
name: 覆铜板与高频材料
slug: ccl-high-freq-material
industry: AI算力
layer: L1
tam_bn: 16.0
cagr_pct: 9.0
margin: 15-25%
cost_share_pct: 35
cost_share_context: PCB制造成本（半导体口径：占PCB材料成本约40%）
profit_pool_pct: 8
profit_pool_context: PCB产业链利润池（高频高速CCL利润率显著高于中低端）
value_add: medium
updated: 2026-09
type: segment
tags:
- AI算力
- L1
competition:
  global:
  - name: 建滔积层板 (Kingboard)
    share: ~14%
    note: 港股01888，全球产能第一，中低端为主；2026年多次发涨价函
  - name: 生益科技
    share: ~12%
    note: A股600183，全球第二、中国大陆第一；高频高速材料持续追赶Rogers/松下
  - name: 松下电工 (Panasonic)
    share: '-'
    note: 日本，M6/M7以上超低损耗材料全球领先，AI服务器高速板主力
  - name: Rogers
    share: '-'
    note: 美国，高频(射频/毫米波)CCL全球龙头，车规雷达与基站市场主导
  - name: 台光电子 (EMC)
    share: '-'
    note: 台湾2383.TW，高速CCL切入NVIDIA AI服务器供应链
  china:
  - name: 生益科技
    share: '-'
    note: 600183 高频高速材料国内第一，M6/M7等级已量产
  - name: 华正新材
    share: '-'
    note: 603186 高速CCL国产二线
  - name: 金安国纪
    share: '-'
    note: 002636 中低端CCL规模厂商
  - name: 雅克科技
    share: '-'
    note: 002409 硅微粉等**功能填料**切入M8/M9高频覆铜板海外供应链（材料上游而非CCL本体）
  barriers:
  - item: 高频高速树脂配方
    detail: M6/M7以上等级需低介电常数(Dk)/低损耗因子(Df)树脂体系，配方与工艺长期由Rogers/松下垄断
  - item: 玻纤布与铜箔配套
    detail: 低介电玻纤布(如NE-glass)与HVLP超低粗糙度铜箔是高频CCL的必要配套，上游供应集中度高
  - item: 客户认证周期
    detail: PCB厂→终端(服务器/交换机/车厂)双级认证，周期2-3年，新进入者难切入
  - item: 等级跃迁的良率控制
    detail: 从M4到M6/M7需同时改善Dk/Df、耐热性与加工性，良率爬坡是核心难点
  tech_gap:
  - dimension: 中国在中低端CCL全球领先（建滔+生益合计份额超25%），但**高频高速(M6/M7以上)等级仍由Rogers/松下/台光主导**，AI服务器最高等级材料国产化率低；功能填料(硅微粉)环节国产厂商已切入海外供应链
    detail: ''
key_trends:
- title: AI服务器PCB层数与材料等级双升
  detail: PCB层数从12-16层升级至20-30层，材料从M4升级至M6/M7——层数与等级同升，单板CCL价值量成倍增长
- title: 覆铜板厂商密集涨价
  detail: 建滔2026年多次发涨价函；上游铜箔、玻纤布同步涨价，成本传导至PCB厂，2026年A股元器件板块+115%
- title: 高频高速CCL是国产替代最难环节
  detail: 中低端已实现国产主导，但最高等级(M7以上)仍依赖Rogers/松下——与"封装基板材料"中的ABF膜同属"卡脖子材料"
- title: 功能填料成为差异化赛道
  detail: 硅微粉等填料影响Dk/Df与热膨胀系数，雅克科技华飞电子切入M8/M9海外供应链、净利+超800%
- title: 玻璃基板为下一代技术方向
  detail: 与PCB/载板环节共享同一技术演进路径，长期可能改变高频材料的形态
price_conduction:
- 覆铜板占PCB制造成本约35%，是PCB最大单项成本
- 上游铜箔/玻纤布/树脂涨价→CCL厂发涨价函→PCB厂成本上升
- PCB厂对下游(服务器/交换机)议价能力取决于材料等级：高等级CCL供不应求，传导顺畅
- 高频等级(Rogers/松下主导)涨价传导能力最强
- 中低端CCL产能过剩，价格竞争激烈，传导受阻
- AI服务器需求拉动下，高等级CCL议价权显著提升
wikilinks:
- PCB与IC载板
- 封装基板材料
- AI服务器
- 高纯硅料与硅片
companies:
- ticker: '600183'
  name: 生益科技
  role: 龙头
  rev: 60
- ticker: '002409'
  name: 雅克科技
  role: 直接相关
  note: 硅微粉功能填料，非CCL本体
  rev: 15
key_inputs:
- 铜箔
- 玻纤布
- 树脂
- 硅微粉等功能填料
key_customers:
- PCB与IC载板
- AI服务器
sources:
- title: 本仓库 Wiki 内证：PCB与IC载板
  summary: AI服务器PCB层数12-16→20-30层、材料M4→M6/M7、覆铜板厂商密集涨价（建滔2026年多次发涨价函）、2026年A股元器件板块+115%
  url: L2-Wiki/赛道/AI算力/pcb-ic-substrate.md
- title: 本仓库 Wiki 内证：雅克科技
  summary: 华飞电子硅微粉切入M8/M9高频覆铜板海外供应链，1H26净利+超800%
  url: L2-Wiki/公司/yoke-technology.md
- title: 本仓库 Wiki 内证：深南电路
  summary: 上游为覆铜板(CCL)供应商，采购高频高速覆铜板(M6/M7/M8等级)
  url: L2-Wiki/公司/shennan-circuits.md
- title: ⚠️ 待验证：TAM/CAGR 为估算值
  summary: 本赛道建立时 WebSearch 配额已耗尽（400/400），TAM $16B、CAGR 9%、份额数字均未经外部来源核验，需后续用 WebSearch 补验
  url: ''
---

# 覆铜板与高频材料

> **AI算力** · L1 · TAM **$16B** · CAGR **9%**

覆铜板（CCL）是PCB的**核心基材**——由铜箔、玻纤布浸渍树脂后压合而成，决定PCB的电气性能上限。AI服务器把PCB从12-16层推到20-30层、材料从M4推到M6/M7，**单板CCL价值量成倍增长**。中低端中国已主导（建滔+生益份额超25%），但**最高等级材料仍是卡脖子环节**——与封装基板材料中的ABF膜同属一类。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $16B（⚠️估算，待验证） |
| 年复合增长率(CAGR) | 9%（⚠️估算，待验证） |
| 利润率区间 | 15-25% |
| 成本占比 | 35% (PCB制造成本)〔半导体口径：占PCB材料成本约40%〕 |
| 利润池占比 | 8% (PCB产业链利润池) |
| 附加值 | medium |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-09-13（新建赛道）
> 来源: 本仓库 Wiki 内证（PCB与IC载板 / 封装基板材料 / 雅克科技 / 深南电路），见 sources
> 置信度: 中（结构与人证充分，**数值待外部验证**）

- **建赛道缘由**: 生益科技（600183，全球CCL第二）被公司词条引用为 `segments: [覆铜板与高频材料]`，但该赛道此前**从未创建**（属"幽灵赛道"）。本赛道建立以修复该悬空引用，并补齐"PCB上游材料"这一缺口——原 PCB与IC载板($12B) 赛道把PCB与载板混在一起，未单列CCL环节。
- **定位**: 与「封装基板材料」并列的上游材料环节；上下游为 铜箔/玻纤布/树脂/硅微粉 → CCL → PCB
- **数据来源**: 结构性内容（竞争格局、壁垒、趋势、价格传导）取自本仓库已有的 PCB与IC载板、封装基板材料、雅克科技、深南电路四个词条，可追溯
- **⚠️ 待验证项**: `tam_bn`(16.0) / `cagr_pct`(9.0) / 各厂商 `share` 均**未经外部来源核验**——本 session 的 WebSearch 配额已耗尽（400/400）。后续应补做 WebSearch（关键词如"覆铜板 市场规模 2026"、"高频CCL Rogers 份额"）并更新 sources。
- **companies 说明**: 仅收 生益科技(600183,CCL本体) 与 雅克科技(002409,硅微粉功能填料上游)；雅克 role 标 `直接相关` 并加注"非CCL本体"
- **⚠️ 待建公司页（本赛道重要成员但 Wiki 无词条，故未列入 companies 以免造成悬空引用）**: 建滔积层板(01888.HK，全球产能第一)、Rogers(ROG，高频CCL全球龙头)、台光电子(2383.TW)、华正新材(603186)、金安国纪(002636)。补齐这 5 家后本赛道 companies 才具备完整代表性。
