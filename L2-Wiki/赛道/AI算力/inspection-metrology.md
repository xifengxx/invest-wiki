---
name: 检测量测设备
slug: inspection-metrology
industries:
- AI算力
- 半导体
layer: L2
tam_bn: 13.0
cagr_pct: 9.0
margin: 50-60%
cost_share_pct: 10
cost_share_context: 芯片制造成本（半导体口径：晶圆厂设备(WFE)支出12%）
profit_pool_pct: 8
profit_pool_context: 芯片制造利润池（半导体口径：半导体设备利润池15%，KLA垄断利润，毛利率~60%）
value_add: high
updated: 2026-09
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: KLA
    share: '>50%'
    note: 美国，检测量测绝对垄断（类似于ASML在光刻机地位），7x第二名份额，毛利率~60%，先进封装收入$635M→$1B
  - name: AMAT
    share: '-'
    note: 美国，电子束检测
  - name: Lasertec
    share: '-'
    note: 日本，EUV光罩检测全球垄断, Hitachi High-Tech
  - name: Camtek
    share: '-'
    note: 以色列
  china:
  - name: 中科飞测
    share: '-'
    note: 688361 无图形晶圆检测进入SMIC，光学检测国产龙头，成熟制程突破
  - name: 华峰测控
    share: '-'
    note: 688200 ATE测试设备龙头，国产测试设备#1
  barriers:
  - item: 光学/电子束核心技术
    detail: 先进制程需检测<1nm级别的缺陷；电子束检测存在高分辨率与高通量的矛盾（EBIC/EBI技术）
  - item: 深度学习缺陷分类算法
    detail: 替代人工Review，效率提升5-10x
  - item: 客户验证
    detail: 18-24个月
  tech_gap:
  - dimension: KLA垄断堪比ASML。中国检测设备2024年开始从0到1突破；中国差距7-10年，中科飞测在成熟制程(≥28nm)实现突破但先进制程空白，国产检测设备市占率<5%
    detail: ''
key_trends:
- title: EUV光罩检测随2nm量产需求剧增
  detail: Lasertec在EUV光罩缺陷检测领域全球垄断，是AI芯片检测的核心设备
- title: AI+检测成为新趋势
  detail: 深度学习缺陷分类可将检测效率提升3-5倍（另一口径5-10x），KLA和AMAT在AI检测领域领先，Onto Innovation为主要布局者之一
- title: 先进封装检测随HBM/CoWoS爆发
  detail: Onto Innovation和Camtek在先进封装检测领域增长最快，Onto Dragonfly获>$240M HBM采购协议至2027年，2026年营收>30%增长
- title: 中科飞测无图形晶圆检测已进入SMIC
  detail: 国产检测设备从0到1突破，国产市占率<5%但增速快，中科飞测+华峰测控在成熟制程突破
- title: KLA先进封装收入$635M(2025)→$1B(2026)
  detail: HBM/CoWoS/3D封装驱动检测需求暴增
price_conduction:
- 检测设备是良率管理核心
- KLA垄断~50%份额（堪比ASML在光刻机）
- 年涨5-10%
- 晶圆厂质量控制成本持续上升。检测设备仅占总设备投资约10%
- KLA涨价对晶圆厂总成本影响有限。中国中科飞测国产替代（国产化率<5%）
- 为国内晶圆厂提供第二选择
companies:
- ticker: '688361'
  name: 中科飞测
  role: 概念股
  rev: 70
- ticker: KLAC
  name: KLA Corporation
  role: 龙头
  rev: 60
- ticker: AMAT
  name: Applied Materials
  role: 二线弹性
  rev: 12
- ticker: TER
  name: Teradyne
  role: 龙头
  rev: 30
- ticker: 6857.T
  name: Advantest
  role: 龙头
  rev: 25
- ticker: 6920.T
  name: Lasertec Corporation
  role: 龙头
  rev: 85
- ticker: HITACHI-HIGHTECH
  name: Hitachi High-Tech
  role: 龙头
  rev: 15
- ticker: CAMT
  name: Camtek
  role: 二线弹性
  rev: 60
- ticker: NVMI
  name: Nova Ltd
  role: 二线弹性
  rev: 75
- ticker: '300567'
  name: 精测电子
  role: 国产二线
  rev: 45
- ticker: '688200'
  name: 华峰测控
  role: 国产替代
  rev: 50
wikilinks:
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
- 光刻机
- 封装设备
- 测试设备
key_inputs:
- 半导体设备零部件
- 电子特气
key_customers:
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
- 成熟制程代工
sources:
- title: Fortune Business Insights《Metrology Equipment Market 2025》
  summary: ''
  url: https://www.fortunebusinessinsights.com
- title: Nasdaq ONTO vs KLAC Comparison 2026
  summary: ''
  url: ''
- title: 中科飞测2025年报
  summary: ''
  url: ''
- title: KLA FY2025
  summary: ''
  url: ''
- title: QYResearch《全球半导体量测和检测市场2026》
  summary: 2024全球$152亿→2030$355亿(CAGR 10.8%), KLA份额>50%
  url: https://m.sohu.com/a/963182409_121172584
- title: 智研咨询《前道量检测设备分析报告》
  summary: 国产化率<10%, 中科飞测国内市占率2.84%领先, 国产替代空间巨大
  url: http://mp.weixin.qq.com/s?__biz=MzkzNjQ4MTk5Nw==&mid=2247584873&idx=2
- title: 《财经》中科飞测专题
  summary: 产品线覆盖70%市场种类, 累计出货超1000台, KLA核心挑战者
  url: https://www.mycaijing.com/article/detail/553847
---

# 检测量测设备

> **AI算力** · L2 · TAM **$13B** · CAGR **9%**

半导体检测量测是芯片制造的**「眼睛」**——在数百道工序后检查晶圆是否合格。分为**缺陷检测**(污染/划痕)和**量测**(膜厚/线宽/套刻精度)。|**全球$12.6B(2025)，KLA绝对垄断(~7x第二名份额)**，KLA+AMAT+Hitachi+ASML+Onto Innovation Top5占>57%。KLA先进封装收入从$635M(2025)→$1B(2026)。Onto Innovation Dragonfly获>$240M HBM采购协议至2027年，2026年营收>30%增长。|**一台先进检测设备$30-50M，AI+深度学习缺陷分类**是核心趋势。中国中科飞测+华峰测控在细分突破。**KLA毛利率~60%（垄断利润堪比ASML在光刻机）；中国差距7-10年——中科飞测(688361)已在成熟制程(≥28nm)突破但先进制程空白，华峰测控(688200)为国产测试设备第一，国产检测设备市占率<5%**。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $13B |
| 年复合增长率(CAGR) | 9% |
| 利润率区间 | 50-60% |
| 成本占比 | 10% (芯片制造成本)〔半导体口径：晶圆厂设备(WFE)支出12%〕 |
| 利润池占比 | 8% (芯片制造利润池)〔半导体口径：半导体设备利润池15%，KLA垄断利润，毛利率~60%〕 |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→7条

### 更新 2026-09-13（合并 semi-inspection-metrology 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-inspection-metrology.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$13B）。cagr 保留本方 9%（对方 8%）；cost_share 保留 10%（对方 WFE 口径 12%）；profit_pool 保留 8%（对方设备利润池口径 15%）
- **口径保留**: cost_share / profit_pool 的半导体口径（占晶圆厂设备(WFE)支出12% / 半导体设备利润池15%）并入 context 备注明细，两个视角并存
- **key_trends**: 4 → 5 条。新增对方独有的"KLA先进封装收入$635M(2025)→$1B(2026)"；将对方更具体的数字并入本方条目（AI检测效率补入 5-10x 口径、Onto Dragonfly $240M HBM 协议、国产市占率<5% 与华峰测控）
- **sources**: 4 → 7 条。并入 QYResearch《全球半导体量测和检测市场2026》、智研咨询《前道量检测设备分析报告》、《财经》中科飞测专题
- **companies**: 9 → 11 家。并入 精测电子(300567)、华峰测控(688200)；KLAC/AMAT/中科飞测三方共有，均用正本数值（60/12/70）
- **wikilinks**: 2 → 3 条。并入 光刻机；**key_inputs**: 1 → 2 条（并入 电子特气）；**key_customers**: 2 → 3 条（并入 成熟制程代工）
- **competition**: KLA 条目并入 7x第二名份额、毛利率~60%、先进封装收入$635M→$1B；中科飞测条目并入"光学检测国产龙头、成熟制程突破"；华峰测控条目并入"国产测试设备#1"。barriers 与 tech_gap 双方均非空，按规则合并（补入 <1nm 缺陷检测、EBIC/EBI 高通量矛盾、中国差距 7-10 年与国产市占率<5%）
- **修复**: 原正本 YAML 结尾 `key_inputs: [...]---` 缺少换行导致 frontmatter 分隔符粘连，本次一并修正
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
