---
name: Micron
slug: micron
country: US
ticker: MU
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- HBM高带宽内存
- NVMe/存储芯片
- 功率半导体
- 存储芯片(DRAM/NAND)
one_liner: 美国最大存储芯片IDM(DRAM全球第三/HBM第三)，聚焦DRAM/HBM/NAND全品类半导体存储，通过千亿美元SCA长期战略协议锁定收入实现盈利，位于IDM制造中游——16份SCA覆盖50%+营收
chain_layer: L3
chain_role: 龙头
suppliers:
- company: ASML
  ticker: ASML
  supplies: EUV光刻机
- company: 应用材料
  ticker: AMAT
  supplies: 沉积/刻蚀设备
- company: 东京电子
  ticker: 8035.T
  supplies: 涂胶显影设备
- company: Applied Materials
  supplies: 材料工程与先进沉积设备，EPIC中心联合研发
- company: GlobalWafers
  supplies: 300mm硅晶圆，$5亿战略融资+10年供应长约
- company: Axcelis Technologies
  supplies: 离子注入系统
- company: Onto Innovation
  supplies: 计量检测设备Dragonfly系统
- company: Kulicke & Soffa
  supplies: 先进封装键合设备
customers:
- company: NVIDIA
  ticker: NVDA
  note: HBM3E供应商(份额10%)
- company: AMD
  ticker: AMD
- company: 数据中心/PC OEM
- company: Amazon/Microsoft/Google
  note: 北美三大云厂商数据中心DRAM/NAND
- company: General Motors
  note: 车规级内存长期供应协议
- company: Ford
  note: 车规级内存长期供应协议
partners:
- company: NVIDIA
  ticker: NVDA
  area: HBM3E供应
  note: HBM产能2025年释放
competitors:
- company: SK海力士
  ticker: 000660.KS
  area: HBM
  note: 落后SK海力士约2年(HBM3E)
- company: 三星电子
  ticker: 005930.KS
  area: HBM+DRAM
- company: Samsung Electronics
  note: DRAM/NAND/HBM全球份额第一，HBM4验证进度最快
- company: SK Hynix
  note: HBM全球第一市占56%，DRAM第二，NAND第二
- company: Kioxia/Western Digital
  note: NAND闪存日本合资厂，与Micron争夺第三
- company: 长江存储YMTC
  note: NAND
core_business:
- HBM4高带宽AI内存（2026全年产能售罄，供给NVIDIA及云厂商）
- 1γ(1-gamma)EUV节点DDR5/LPDDR5X DRAM（DRAM营收主力）
- 企业级PCIe Gen6 SSD与G9 245TB QLC NAND闪存
- 车规级内存与嵌入式工业存储(GM/Ford长期协议)
- 192GB LP SOCAMM2低功耗AI推理内存模组
revenue_model: FY2025营收$37.4B，DRAM占76%（其中HBM约15%），NAND占23%。FY2026 Q2营收$23.86B(同比+200%)，Non-GAAP毛利率75%，Q3指引约81%。16份SCA协议含$1000亿最低合同收入与$220亿客户预付款/保证金，floor price锁定毛利率高于历史峰值62%，预计最终覆盖总营收50%+
ticker: MU
description: 美光科技（Micron Technology）是全球领先的内存与存储解决方案供应商，总部位于美国爱达荷州博伊西。公司成立于1978年，产品覆盖DRAM（含HBM高带宽内存）、NAND闪存、SSD及多芯片封装，广泛应用于云计算、AI数据中心、移动设备、汽车电子和工业物联网。美光是全球第三大DRAM制造商（仅次于三星和SK海力士），在HBM市场正快速追赶。FY2025营收约373.8亿美元，市值约1万亿美元（2026年中）。公司在美、日、新加坡、马来西亚、中国大陆、台湾和印度拥有15座制造基地，受益于美国CHIPS法案约61亿美元补贴，正大规模扩建美国本土产能。
website: https://www.micron.com
industry: 半导体
founded: 1978
headquarters: 美国爱达荷州博伊西
employees: ~48,000
latest_revenue: Q2 FY2026 $23.86B（单季）
market_cap: ~$180B
---

# Micron

全球三大DRAM巨头之一，AI时代HBM高带宽内存核心供应商，CHIPS法案最大受益者，从内存周期股转型为AI算力基础设施关键玩家。

## 财务状况

FY2025（截至2025年8月）营收**373.8亿美元**，同比增长48.9%，从FY2023内存低谷（155.4亿）强劲复苏。毛利率随HBM占比提升大幅改善，FY2025全年毛利率约**40-45%**，FY2026 TTM已攀升至**72.6%**。经营利润率从前一年约25%跃升至FY2025约**40%+**。

| 财年 | 营收 | 同比增长 | 毛利率 | 净利率 |
|------|------|----------|--------|--------|
| FY2023 | $155.4亿 | -49.5% | ~5% | -37% |
| FY2024 | $251.1亿 | +61.6% | ~22% | ~9% |
| FY2025 | $373.8亿 | +48.9% | ~42% | ~25% |

**产品结构**：DRAM占比约**69%**（~$258亿），其中HBM收入约**$40-50亿**，占DRAM比重从FY2024的个位数跃升至~18%；NAND占比约**31%**（~$116亿）。AI驱动的HBM需求是毛利率结构性提升的核心驱动力。FY2026 TTM营收已突破**$902.7亿**，市值站上**$1.08万亿**（2026年7月）。

## 产品线详解

**核心DRAM产品线：**
- **HBM3E 12-Hi**（12层堆叠）：已通过NVIDIA认证，用于H200/B200 GPU，是当前AI服务器标配内存
- **HBM4 36GB 12-Hi**：2026年进入量产，引脚速度**>11Gb/s**，带宽**>2.8TB/s**，较HBM3E提升**2.3倍**，能效改善**>20%**，专为NVIDIA Vera Rubin平台设计
- **DDR5**：数据中心与PC主流内存标准，支持高容量DIMM
- **LPDDR5X**：移动端旗舰内存，1β工艺节点，用于高端智能手机和AI PC
- **GDDR6X**：图形内存，用于游戏显卡

**NAND/存储产品线：**
- **232层+ Replacement Gate NAND**：当前主力NAND技术，替代传统浮栅结构
- **数据中心SSD**（如9550系列）：PCIe Gen5，面向AI训练/推理工作负载
- **G9 NAND**：第九代NAND架构，持续推进层数到300+

**HBM竞争格局：** SK海力士仍居HBM市场份额**第一（~50%+）**，三星**第二（~30%）**，美光**第三（~15-20%）**但增速最快。美光凭借HBM3E 12-Hi在NVIDIA供应链中份额持续扩大，HBM4同步量产进度领先三星，目标2026年HBM份额提升至**20-25%**。

## 技术路线图

| 技术节点 | 时间窗口 | 关键特性 |
|----------|----------|----------|
| **1β (1-beta) DRAM** | 2023-2025 | DUV浸没式光刻，DDR5/LPDDR5X主力工艺 |
| **1γ (1-gamma) DRAM** | 2025-2026 | **首次引入EUV光刻**，位密度提升30%，功耗降低20% |
| **HBM4 12-Hi** | 2026 | 36GB容量，>2.8TB/s带宽，NVIDIA Vera Rubin |
| **1δ (1-delta) DRAM** | 2027+ | 全面EUV，进一步缩小单元尺寸 |
| **400+层 NAND** | 2026-2027 | 多层堆叠突破，存储密度倍增 |
| **HBM5** | 2028+ | 规划阶段，带宽有望突破4TB/s |

**制造布局优势：** 美国CHIPS法案拨款约**$61亿**支持本土扩建——爱达荷州博伊西新厂（2026投产）、纽约州Clay巨型晶圆厂群（4座、总投资**~$1000亿**）、弗吉尼亚州马纳萨斯扩产。海外：日本广岛DRAM厂（与日本政府合作）、印度古吉拉特邦Sanand封测厂（投资**$27.5亿**）、中国西安封测基地及上海研发中心。全球**15座制造基地**，美国本土产能占比正在快速提升。


## 融资与现金流

- 详见财务状况章节
## 研发投入与专利

**研发投入规模：** FY2025研发支出约**$38-40亿**（占营收~10%），FY2026 TTM已增至约**$50亿+**。美光持续维持行业领先的研发强度，远高于传统半导体公司平均水平。研发重点聚焦：**HBM堆叠架构**（混合键合Hybrid Bonding）、**EUV DRAM工艺**（1γ/1δ节点）、**3D NAND层数突破**（400+层）、**先进封装**（CoWoS配合）。

**专利护城河：** 全球专利组合超过**55,000项**，涵盖DRAM单元结构、NAND三维堆叠、内存控制器接口、先进封装和AI内存子系统。在HBM领域的专利布局近三年增长了**200%+**，迅速缩小与SK海力士的差距。

**技术壁垒：** 内存制造需要极深的工艺know-how、巨额资本开支（FY2026 TTM CapEx达**$253亿**）和长期客户认证周期。美光是全球仅有的三家具备先进DRAM制造能力的公司之一，HBM认证门槛极高（12-18个月），形成强大先发优势。美国本土制造+CHIPS法案支持构建了独特的地缘政治护城河——在中国供应链风险上升背景下，美光是“安全内存供应链”的首选供应商。

