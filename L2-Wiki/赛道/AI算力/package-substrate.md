---
name: 封装基板材料
slug: package-substrate
industries:
- AI算力
- 半导体
layer: L1
tam_bn: 5.0
cagr_pct: 12.0
margin: 25-35%
cost_share_pct: 6
cost_share_context: 芯片封装成本
profit_pool_pct: 4
profit_pool_context: 芯片封装利润池（半导体口径：封装基板材料利润池，4%）
value_add: medium
updated: 2026-09
type: segment
tags:
- AI算力
- L1
competition:
  global:
  - name: Unimicron
    share: ~22%
    note: 台湾，#1全球ABF载板
  - name: Ibiden
    share: '-'
    note: 日本，#2 Intel/NVIDIA核心供应商
  - name: AT&S
    share: '-'
    note: 奥地利，#3 欧洲最大IC载板厂
  - name: Nan Ya PCB
    share: '-'
    note: 台湾，IC载板/PCB大厂
  - name: Shinko
    share: '-'
    note: 日本，#5 Intel先进封装基板
  - name: 味之素(Ajinomoto)
    share: '>95%'
    note: 日本，ABF膜绝对垄断，FC-BGA产能最大瓶颈，AI芯片需求暴增受益者
  - name: 积水化学
    share: '-'
    note: 日本，ABF替代方案研发中
  china:
  - name: 深南电路
    share: '-'
    note: 002916 广州FC-BGA工厂2025量产月产能2万片
  - name: 鹏鼎控股
    share: '-'
    note: 002938 全球最大PCB厂淮安FC-BGA项目2026投产
  - name: 景硕科技
    share: '-'
    note: 3189 台湾FC-BGA
  - name: 沪电股份
    share: '-'
    note: 002463 AI服务器主板核心
  - name: 生益科技
    share: '-'
    note: 600183 ABF膜研发中，2027年目标小批量
  - name: 华正新材
    share: '-'
    note: 603186 ABF膜国产替代攻关
  barriers:
  - item: FC-BGA精度
    detail: 线宽/线距<8μm；20+层FC-BGA层间对位精度<5μm
  - item: ABF膜独家
    detail: 全球仅味之素供应；配方极复杂，味之素30年+经验积累，非简单的「膜」材料而是多层树脂复合材料
  - item: 客户验证
    detail: 12-18个月
  - item: 产线投资
    detail: 单条$500M+
  - item: 热膨胀系数(CTE)匹配
    detail: 芯片(3ppm)→基板(8-12ppm)→PCB(17ppm)需精确匹配
  tech_gap:
  - dimension: 日本/台湾20+层FC-BGA领先3-5年，中国FC-BGA从2025年开始从零建设；ABF膜仍高度依赖味之素，国产替代处于**验证转量产早期**——华正新材CBF积层绝缘膜一期300万㎡/年、良率超85%，已通过兴森科技/深南电路验证并向长电科技、华为昇腾**小批量供货**（2026-09 核实，原记"国产化率为零、2027年小批量"已过时）
    detail: CBF/ABF 膜的国产化进度是全赛道最关键的时点变量：若仅按「2027年小批量」的旧口径估值，会低估华正新材的先行卡位；但小批量 ≠ 规模替代，最高等级FC-BGA用ABF膜良率与批次一致性仍未有公开验证数据。**本字段口径已于 2026-09-13 由华正新材公司词条的新调研更正，原表述见本文件动态更新记录**
key_trends:
- title: AI芯片FC-BGA层数从14→20+层
  detail: 每增加2层约提升40%的设计复杂度，Unimicron和Ibiden在20+层领域领先；NVIDIA B200封装基板已20+层，直接带动ABF膜需求翻倍
- title: 中国FC-BGA产能从零到有
  detail: 深南电路广州FC-BGA工厂2025年量产(月产能2万片)，鹏鼎控股淮安FC-BGA项目2026年投产
- title: 玻璃基板为下一代技术方向
  detail: Intel和Samsung研发玻璃替代有机树脂作为封装基板，可提升信号完整性30%、降低翘曲50%；玻璃基板替代硅中介层可能改变材料需求，Intel/TSMC均已布局
- title: ABF膜供应仍然紧张
  detail: 日本味之素是ABF膜全球唯一供应商，2026年产能扩张但需求增速更快；扩产周期长(2-3年)跟不上AI芯片迭代速度，供不应求预计持续至2028+
- title: 中国生益科技/华正新材2027年有望小批量
  detail: ABF膜从0到1突破将打开$1B+市场
price_conduction:
- FC-BGA载板占芯片封装成本约20%。ABF膜由味之素垄断>95%，供应紧张
- 载板涨价5-10%；ABF膜持续涨价(年5-8%)，FC-BGA基板ASP涨10-15%
- GPU/ASIC封装成本上升（封装基板成本上升）
- 芯片总成本增加1-2%（另一口径：0.5-1%）
- 传导影响温和
- AI芯片公司被迫接受。ABF供给短缺是FC-BGA扩产最大障碍
- 封装基板厂产能扩张受限于ABF供给
companies:
- ticker: '2802'
  name: 味之素 (Ajinomoto)
  role: 二线弹性
  rev: 8
- ticker: '3037'
  name: Unimicron (欣兴电子)
  role: 龙头
  rev: 60
- ticker: '4062'
  name: Ibiden
  role: 龙头
  rev: 55
- ticker: '6967'
  name: Shinko Electric (新光电气)
  role: 二线弹性
  rev: 45
- ticker: '8046'
  name: Nan Ya PCB (南亚电路板)
  role: 二线弹性
  rev: 40
- ticker: '002916'
  name: 深南电路
  role: 国产龙头
  rev: 40
- ticker: '002436'
  name: 兴森科技
  role: 国产二线
  rev: 50
wikilinks:
- 封装测试(OSAT)
- 先进封装(CoWoS/3D)
- Chiplet与异构集成
- PCB与IC载板
- 半导体设备零部件
- 覆铜板与高频材料
key_inputs:
- BT树脂
- ABF膜
- 铜箔
key_customers:
- 封装测试(OSAT)
- 先进封装(CoWoS/3D)
- Chiplet与异构集成
sources:
- title: 味之素ABF膜FY2025年报
  summary: ''
  url: ''
- title: 生益科技2025年报
  summary: ''
  url: ''
- title: Unimicron FY2025
  summary: ''
  url: ''
- title: Prismark《全球封装基板市场2025》
  summary: FC-BGA基板需求受AI芯片拉动3年3倍增长，全球Top4占70%
  url: https://www.prismark.com
- title: 深南电路/兴森科技2025年报
  summary: 国产IC载板进入放量期，深南电路无锡基地产能翻倍
  url: https://data.eastmoney.com
contradictions:
- desc: '华正新材 CBF 积层绝缘膜（对标味之素 ABF）的国产化进度：原记「中国国产化率为零、2027年小批量」，新调研显示「一期300万㎡/年、良率超85%，已通过兴森科技/深南电路验证并向长电科技、华为昇腾小批量供货」'
  source_a: '本赛道 tech_gap 原口径：国产化率为零，生益/华正预计 2027 年小批量'
  source_b: '华正新材公司词条（2026-09-13 调研，L0 归档 input_20260913_116）：已小批量供货'
  status: 'resolved_b'
  resolved_date: '2026-09-13'
  found_date: '2026-09-13'
---

# 封装基板材料

> **AI算力** · L1 · TAM **$5B** · CAGR **12%**

封装基板连接芯片与PCB的**「桥梁」**——承担电气连接+机械支撑+散热。ABF(Ajinomoto Build-up Film)是FC-BGA核心绝缘材料，日本味之素独家供应。|**AI芯片驱动封装基板层数14→20+层，线宽/线距15/15→8/8μm**。封装基板是仅次于硅片的第二大半导体材料市场。**味之素ABF膜是FC-BGA产能最大瓶颈**。|日本Shinko/Ibiden+台湾Unimicron(#1)主导全球FC-BGA产能。中国深南电路(002916)+鹏鼎控股(002938)从传统PCB向FC-BGA转型。|**味之素ABF膜全球份额>95%**，扩产周期长(2-3年)跟不上AI芯片迭代速度，供给短缺预计持续至2028+。中国ABF膜国产化率为零，生益科技(600183)/华正新材(603186)攻关中，2027年目标小批量。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $5B |
| 年复合增长率(CAGR) | 12% |
| 利润率区间 | 25-35% |
| 成本占比 | 6% (芯片封装成本，双方口径一致) |
| 利润池占比 | 4% (芯片封装利润池)〔半导体口径：4% 封装基板材料利润池〕 |
| 附加值 | medium |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→7条

### 更新 2026-09-13（合并 semi-package-substrate 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-package-substrate.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn（$5B）与 cagr（12%）双方一致；本方 margin 25-35% / value_add medium 保留（对方为 45-60% / high，予以保留在对方档案）
- **口径保留**: profit_pool 的半导体口径（4% 封装基板材料利润池）并入 context 备注明细；cost_share_context 双方完全一致（芯片封装成本 / 6%），无双口径可并存，故未做标注
- **key_trends**: 4 → 5 条。将对方更具体的数字并入本方既有条目（NVIDIA B200已20+层、ABF扩产周期2-3年、供不应求持续至2028+、玻璃基板替代硅中介层）；追加对方独有主题"中国生益科技/华正新材2027年有望小批量"
- **barriers**: 4 → 5 条（"FC-BGA精度"并入对方"20+层层间对位精度<5μm"；"ABF膜独家"并入对方"配方极复杂/多层树脂复合材料"；追加对方独有"热膨胀系数(CTE)匹配"）；**tech_gap** 保留本方维度并并入对方"ABF膜100%依赖味之素、国产化率为零、差距7-10年、2027年小批量"
- **price_conduction**: 5 → 7 条（并入对方"ABF膜垄断>95%""持续涨价年5-8%、FC-BGA基板ASP涨10-15%"；追加对方独有"ABF供给短缺是FC-BGA扩产最大障碍""封装基板厂产能扩张受限于ABF供给"）；对方"芯片总成本增加0.5-1%"与本方"1-2%"口径冲突，以括注并存
- **sources**: 3 → 5 条。并入 Prismark《全球封装基板市场2025》、深南电路/兴森科技2025年报
- **companies**: 5 → 7 家。并入 深南电路(002916)、兴森科技(002436)；Unimicron/Ibiden 沿用本方 rev（60 / 55）
- **wikilinks**: 2 → 5 条。并入 Chiplet与异构集成、PCB与IC载板、半导体设备零部件
- **key_inputs**: 3 条不变（双方完全一致）；**key_customers**: 1 → 3 条（并入 先进封装(CoWoS/3D)、Chiplet与异构集成）
- **competition**: global 并入对方独有的 ABF 材料视角（味之素>95%、积水化学替代方案研发中）；china 并入 生益科技(600183)、华正新材(603186)
- **数据修正**: 原正本 AT&S 条目 note 末尾误粘 "Nan Ya PCB"，已拆出为独立条目（台湾，IC载板/PCB大厂，与本方 companies 中的 8046 对应）
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并

### 更新 2026-09-13（ABF/CBF 国产化进度口径更正）
> 来源: `L2-Wiki/公司/huazheng-new-material.md`（2026-09-13 新建，L0 归档 input_20260913_116）
> 置信度: 中（公司层调研来自公开报道，未取得一手产线验证数据）

- **原文（已更正）**: `tech_gap` 记「ABF膜100%依赖味之素，中国国产化率为零（差距7-10年），生益科技/华正新材预计2027年小批量」
- **冲突发现**: 新建的华正新材公司词条记载其 CBF 积层绝缘膜（对标味之素 ABF）**一期 300 万㎡/年、良率超 85%，已通过兴森科技/深南电路验证，并向长电科技、华为昇腾小批量供货** —— 与「国产化率为零、2027年小批量」直接矛盾。
- **处理**: 以 2026 年新调研为准更正 `tech_gap`，同时保留「小批量 ≠ 规模替代」的风险提示；**原口径是本条记录的历史，不是仍有争议的选项**。
- **未决**: 最高等级 FC-BGA 用 ABF 膜良率与批次一致性无公开数据；生益科技的 ABF 膜进度仍未核实，`companies` 中其 note 暂保留「2027年目标小批量」旧口径，待补验。
