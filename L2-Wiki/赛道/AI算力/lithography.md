---
name: 光刻机
slug: lithography
industry: AI算力
layer: L2
tam_bn: 33.0
cagr_pct: 12.0
margin: 50%+
cost_share_pct: 20
cost_share_context: 芯片制造成本（半导体口径：晶圆厂设备(WFE)支出，25%）
profit_pool_pct: 15
profit_pool_context: 芯片制造利润池（半导体口径：半导体设备利润池（ASML垄断利润，毛利率52.8%），35%）
value_add: high
updated: 2026-09
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: ASML
    share: 100%
    note: 荷兰，EUV垄断，High-NA EUV 2025交付$380M+/台；整体光刻机份额83%，FY2025营收€32.7B(+15% YoY)，净利€9.6B，毛利率52.8%，EUV出货48台(€11.6B,+39%)，订单积压€38.8B创纪录(EUV占66%)，2026E EUV出货60+台
  - name: Nikon
    share: ~10%
    note: 日本，DUV浸没式#2；DUV ArF/ArF浸没式为主，EUV已退出竞争
  - name: Canon
    share: ~8%
    note: 日本，纳米压印NIL 5nm已实现；i-line/KrF为主，Nanoimprint纳米压印布局
  china:
  - name: SMEE(上海微电子)
    share: '-'
    note: 90nm量产，28nm浸没式研发中，预计2027年验证
  - name: SiCarrier
    share: '-'
    note: 华为系，EUV光源+SAQP研发
  barriers:
  - item: EUV光源+光学系统
    detail: Cymer+Zeiss独家供应链；13.5nm等离子体光源全球唯一，反射式EUV光学镜片精度达原子级别
  - item: 整机整合
    detail: 超10万零部件
  - item: 出口管制
    detail: EUV对中国禁售
  - item: 精密工件台(纳米级运动控制)
    detail: 磁悬浮工件台加速度>20G
  tech_gap:
  - dimension: ASML领先全球至少15年。中国DUV从90nm→28nm突破中，SMEE 28nm浸没式预计2027年验证但量产路径漫长，EUV尚无时间表。美国/荷兰出口管制持续收紧
    detail: ''
key_trends:
- title: High-NA EUV(EXE:5200)2025年首批交付
  detail: 分辨率从13nm提升至8nm，单次曝光可实现2nm节点，单价$380M+/台；2025年首批交付，Intel为首家HVM采纳(18A)，TSMC推迟3-4年暂不采用
- title: 中国DUV光刻机从90nm→28nm突破
  detail: SMEE 28nm浸没式DUV处于研发后期，预计2027年验证，多重曝光可能实现14nm等效但量产良率与产能挑战巨大；SiCarrier/Yuliangsheng等华为系企业布局EUV光源和光学系统
- title: 纳米压印(NIL)作为EUV替代方案
  detail: Canon和Prinano(中国)推出5nm NIL设备，在NAND闪存和存储领域有应用前景；5nm分辨率已实现，但产能远低于EUV
- title: ASML垄断地位短期不可撼动
  detail: EUV光刻机需要Carl Zeiss光学系统、Cymer激光源等独家供应链，任何新进入者需要10年以上追赶期；ASML自身目标2030年营收€44-60B、毛利率56-60%，EUV出货量从48台向100+台/年扩张
- title: 电子束直写(EBDW)是EUV之外的补充路线
  detail: 无需掩模版即可直写图形，与纳米压印同属EUV补充技术，但产能远低于EUV，仅适用于掩模版制造和小批量特殊器件
price_conduction:
- EUV光刻机单价$300M+，ASML垄断全球供应(EUV 100%份额)。EUV涨价，每代光刻机涨价30-50%（NXE:3400→NXE:3800→EXE:5200）
- 晶圆代工成本增加（3nm工厂设备折旧占比高）；台积电毛利率从50%→66%也需涨价传导
- 芯片设计公司ASP被动上涨
- 最终转嫁至云厂商和消费者。High-NA EUV售价$380-400M/台
- 仅Intel/TSMC/Samsung能负担，先进制程竞争格局进一步固化
companies:
- ticker: ASML
  name: ASML
  role: 龙头
  rev: 95
- ticker: AFX.DE
  name: Zeiss (蔡司)
  role: 龙头
  rev: 25
- ticker: 7751.T
  name: Canon
  role: 全球二线
  rev: 30
- ticker: 7731.T
  name: Nikon
  role: 全球二线
  rev: 20
- ticker: '-'
  name: SMEE(上海微电子)
  role: 国产替代
  rev: 60
wikilinks:
- 光掩模版
- 半导体设备零部件
- 晶圆代工(先进制程)
- 涂胶显影设备(Track)
- 高纯硅料与硅片
- 光刻胶与湿化学品
- 刻蚀设备
- 薄膜沉积设备
- 检测量测设备
- 成熟制程代工
- 存储芯片(DRAM/NAND)
key_inputs:
- 光掩模版
- 涂胶显影设备(Track)
- 光刻胶与湿化学品
- 半导体设备零部件
key_customers:
- 晶圆代工(先进制程)
- 成熟制程代工
- 存储芯片(DRAM/NAND)
sources:
- title: ASML FY2025 Annual Report
  summary: ''
  url: https://www.asml.com
- title: ASML Q4 2025 Earnings Call Jan 2026
  summary: ''
  url: ''
- title: SK Hynix $8B EUV Order 2025
  summary: ''
  url: ''
- title: Nikon/Canon FY2025
  summary: ''
  url: ''
- title: CINNO Research 2025全球半导体设备排名
  summary: ASML光刻份额94.1%垄断EUV，2025年出货580台(EUV 162台)
  url: https://m.cnpowder.com.cn/new87965.html
- title: 浙商证券《2026年半导体设备策略》
  summary: 光刻机国产化有望实现0到1突破，子系统及零部件公司受益
  url: https://stock.finance.sina.com.cn/stock/view/paper.php
- title: 中商产业研究院《2026年半导体设备产业链》
  summary: 光刻机国产化率<1%，是国产设备最低环节
  url: http://wap.seccw.com/Document/detail/id/42146.html
---

# 光刻机

> **AI算力** · L2 · TAM **$33B** · CAGR **12%**

光刻机是芯片制造中**最核心、最昂贵的设备**——通过光学系统将电路图案投影到硅片上。一台EUV售价>$3亿，重180吨，超10万个零部件。|**ASML垄断全球EUV(100%)和整体光刻机市场83%**。FY2025营收€32.7B(+15%)，净利€9.6B，毛利率52.8%。EUV出货48台(€11.6B,+39%)。订单积压€38.8B创纪录(EUV占66%)。**2026年预计出货60+台EUV**，营收€34-40B。SK Hynix下单$8B(30台EUV至2027)。|**High-NA EUV(EXE:5200,$380-400M/台)2025首批交付**，Intel首家HVM采纳(18A)，TSMC推迟3-4年暂不采用。ASML 2030目标€44-60B营收，毛利率56-60%。|**Nikon和Canon在DUV中低端/i-line/KrF市场仍有一定份额**，Canon纳米压印(NIL)5nm已实现但产能远低于EUV。中国SMEE 90nm量产、28nm浸没式研发中，整体差距约15年。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $33B |
| 年复合增长率(CAGR) | 12% |
| 利润率区间 | 50%+ |
| 成本占比 | 20% (芯片制造成本)〔半导体口径：25% 晶圆厂设备(WFE)支出〕 |
| 利润池占比 | 15% (芯片制造利润池)〔半导体口径：35% 半导体设备利润池〕 |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从1→7条

### 更新 2026-09-13（合并 semi-lithography 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-lithography.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$33B）；本方 cagr 12% / margin 50%+ 保留（对方为 16% / 50-55%）
- **口径保留**: cost_share / profit_pool 的半导体口径（25% 晶圆厂设备(WFE)支出 / 35% 半导体设备利润池）并入 context 备注明细，两个视角并存
- **key_trends**: 4 → 5 条。吸收对方更具体的数字/事实（Intel首家HVM采纳18A、TSMC推迟3-4年、SMEE 2027年验证、14nm等效多重曝光、ASML 2030目标€44-60B及EUV出货48→100+台/年、NIL产能远低于EUV）；追加对方独有主题"电子束直写(EBDW)是EUV之外的补充路线"
- **barriers / tech_gap**: barriers 3 → 4 条（并入对方"精密工件台(纳米级运动控制)"，并将13.5nm等离子体光源/反射镜原子级精度并入本方条目）；tech_gap 保留本方维度并并入对方"SMEE 2027验证""美国/荷兰出口管制收紧"
- **price_conduction**: 4 → 5 条（并入对方"每代涨价30-50%（NXE:3400→NXE:3800→EXE:5200）""台积电毛利率50%→66%传导""仅Intel/TSMC/Samsung能负担High-NA，先进制程格局固化"）
- **sources**: 4 → 7 条。并入 CINNO Research 2025设备排名、浙商证券《2026年半导体设备策略》、中商产业研究院《2026年半导体设备产业链》
- **companies**: 2 → 5 家。并入 佳能(Canon)、尼康(Nikon)、上海微电子(SMEE)；ASML 沿用本方 rev 95
- **wikilinks**: 4 → 11 条。并入 高纯硅料与硅片、光刻胶与湿化学品、刻蚀设备、薄膜沉积设备、检测量测设备、成熟制程代工、存储芯片(DRAM/NAND)
- **key_inputs**: 2 → 4 条（并入 光刻胶与湿化学品、半导体设备零部件）；**key_customers**: 1 → 3 条（并入 成熟制程代工、存储芯片(DRAM/NAND)）
- **competition**: 补齐 ASML 更具体的财务与出货数据；Nikon/Canon 条目并入对方"EUV已退出竞争""i-line/KrF""Nanoimprint布局"；中国侧 SMEE 条目并入"预计2027年验证"
- **数据修正**: 原对方档案中 佳能(Canon) ticker 误写为 7731.T（实为尼康），已按 L2-Wiki/公司/canon.md 修正为 7751.T；上海微电子（SMEE，未上市）ticker 由误写的 688012（实为中微公司AMEC）改为 '-'
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
