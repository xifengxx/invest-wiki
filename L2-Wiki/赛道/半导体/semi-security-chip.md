---
name: 安全芯片
slug: semi-security-chip
industries:
- 半导体
layer: L3
tam_bn: 5.7
cagr_pct: 9.0
margin: 35-50%
cost_share_pct: 2
cost_share_context: 终端整机成本（手机/银行卡/车规模组）
profit_pool_pct: 3
profit_pool_context: 半导体利润池（金融级与车规认证壁垒带来高毛利）
value_add: high
updated: 2026-09
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: NXP
    share: '~12%'
    note: 荷兰，智能卡与安全芯片全球第一（前三NXP/英飞凌/三星合计约66%）；嵌入式安全口径约11-13%。NFC/UWB/安全芯片，Apple等手机客户（占其营收约13%）
  - name: Infineon
    share: '~14%'
    note: 德国，嵌入式安全全球第一（约13-15%）；**TPM安全芯片全球第一**（安全互联CSS板块约占其营收25%）；汽车HSM领先，AURIX累计出货超3.5亿颗
  - name: Thales
    share: '-'
    note: 法国HO.PA，银行业非接触智能卡全球份额第一(21.1%)、eSIM Provisioning 综合第一(连续6年)，2025-10 抗量子智能卡首家获 ANSSI EAL6+。⚠️ **口径澄清**：Thales 是智能卡/eSIM 平台与安全服务商，芯片主要外采——市场报告将其列入"安全芯片主要厂商"是按价值链口径，**与 NXP/Infineon 等芯片设计公司非同类比较对象**
  - name: STMicroelectronics
    share: '-'
    note: 意法，ST33系列eSE/安全MCU，手机与车规；安全加密芯片全球前五成员
  - name: Microchip
    share: '-'
    note: 美国，安全元件与加密认证IC
  china:
  - name: 紫光国微
    share: '-'
    note: 002049 智能安全芯片（SIM/金融IC/证件），国产特种安全IC龙头
  - name: 复旦微电
    share: '-'
    note: 688385 **国内首家获 WPC 认证**，金融NFC读写器芯片规模量产主要厂商，安全与识别芯片1H26收入4.72亿元(+20.1%)
  - name: 华大电子
    share: '-'
    note: 中国电子系，SIM/金融IC/Secure MCU
  - name: 国民技术
    share: '-'
    note: 300077 安全MCU与安全芯片
  - name: 大唐微电子
    share: '-'
    note: SIM卡与身份识别安全芯片
  barriers:
  - item: 金融级安全认证
    detail: 银行卡/金融IC需通过CC EAL5+/EAL6+认证（含侧信道攻击防护），认证周期长、门槛极高
  - item: WPC 与行业准入
    detail: 无线支付、运营商SIM、车规HSM各有独立认证体系（WPC/AEC-Q100/SHE+），逐个突破
  - item: 银行与运营商导入周期
    detail: 金融与电信客户切换安全芯片供应商需重新走完安全评估，粘性极强
  - item: 安全算法与抗攻击能力
    detail: 抗侧信道/抗故障注入等物理安全设计能力，是长期工艺积累而非单点技术
  tech_gap:
  - dimension: 中国在SIM卡、二代身份证、中低端金融IC已主导（成本优势+政策推动），但**最高安全等级(CC EAL6+)金融IC、车规HSM、高端TPM仍由NXP/Thales/Infineon主导**；数字人民币与信创是国产替代的主要推动力
    detail: 金融IC卡领域 CR5 达 74.2%、国际巨头占据高端市场约 70% 份额；中国本土厂商在金融IC卡、物联网模组等细分市占已超 60%，但集中在非最高安全等级产品。全球安全加密芯片前五（英飞凌/恩智浦/意法/瑞萨/三星LSI）合计约 67.4%
key_trends:
- title: 数字人民币推动金融IC国产化
  detail: 数字人民币硬钱包与受理终端需要国产安全芯片，是国产厂商切入金融级市场的最重要窗口
- title: eSE/iSE 随手机与车规普及
  detail: 安全元件从独立SE向集成eSE/iSE演进，手机NFC支付、数字车钥匙是主要增量场景
- title: 车规HSM需求随智能驾驶增长
  detail: 域控架构与OTA要求车规级硬件安全模块(HSM)，智能驾驶等级越高单车安全芯片用量越大
- title: TPM 2.0 随信创与Windows 11强制要求
  detail: PC与服务器的可信计算模块从可选变必需，信创整机放量直接拉动国产TPM需求
- title: 安全与AI融合
  detail: 端侧隐私计算需要"安全+算力"融合芯片，安全芯片厂商向安全MCU/安全AI方向延伸
- title: 金融IC卡进入存量替换期，国密算法成国产替代抓手
  detail: 2026 全球金融IC卡出货 46.8 亿张，双界面非接触占比 78%，金融卡领域 CR5 高达 74.2%；国内新发金融IC卡国密算法支持比例预计达 92%，政策推动下国产厂商在金融级认证上加速追赶
- title: 物理SIM受eSIM替代，安全芯片需求向嵌入式迁移
  detail: 物理SIM卡 2026 年出货预计 -3.2% 至 38.5 亿张，但内嵌安全芯片的 SIM/eSIM 出货达 14.2 亿颗(+11.5%)——载体在换、安全芯片用量不减；中国5G超级SIM卡逆势增至 2.1 亿张
price_conduction:
- 安全芯片占终端整机成本极低（约2%），但对安全性不可替代
- 金融级与车规认证壁垒带来显著溢价，毛利率35-50%远高于普通MCU（约35%以下）
- 中低端SIM卡芯片国产化充分，价格竞争激烈、传导受阻
- 高安全等级产品（EAL6+/车规HSM）供应集中，涨价传导顺畅
- 数字人民币与信创属政策驱动需求，价格敏感度低
- 认证周期长使新供应商难以通过降价切入
wikilinks:
- 模拟芯片
- FPGA
- IC设计服务(Fabless)
- 边缘AI
companies:
- ticker: '002049'
  name: 紫光国微
  role: 龙头
  rev: 50
- ticker: '688385'
  name: 复旦微电
  role: 核心参与者
  note: 国内首家获WPC认证，金融NFC读写器芯片规模量产
  rev: 40
- ticker: NXPI
  name: NXP Semiconductors
  role: 龙头
  rev: 55
- ticker: IFX.DE
  name: Infineon Technologies
  role: 龙头
  note: TPM安全芯片全球第一
  rev: 50
- ticker: 'HO.PA'
  name: Thales
  role: 龙头
  note: 银行业非接触智能卡全球份额第一(21.1%)、eSIM Provisioning 综合排名第一；⚠️为智能卡/eSIM平台与安全服务商，芯片主要外采，与NXP/Infineon非同类比较对象
  rev: 10
- ticker: '300077.SZ'
  name: 国民技术
  role: 直接相关
  note: 可信计算芯片国内商市占>85%、金融USB-Key约90%；⚠️1H26负极材料收入占比已达50.19%，超过芯片业务
  rev: 40
- ticker: ''
  name: 华大电子
  role: 直接相关
  note: 未上市（中电华大电子设计/CEC系）；安全芯片累计出货超250亿颗、SIM/eSIM全球份额超20%，CIU9872B_01 已过 CC EAL6+
  rev: 95
- ticker: '600198.SH'
  name: 大唐微电子
  role: 直接相关
  note: 未上市，ticker为母公司大唐电信；社保卡芯片市占超40%、身份证芯片累计出货超6亿枚，2025年收入5.10亿/净利2.77亿
  rev: 80
key_inputs:
- 晶圆代工(先进制程)
- 模拟芯片
key_customers:
- 金融/支付机构
- 智能手机
- 汽车电子
- 边缘AI
sources:
- title: 本仓库 Wiki 内证：复旦微电
  summary: 国内首家获WPC认证的安全芯片供应商，金融NFC读写器芯片规模量产主要厂商；安全与识别芯片1H26收入4.72亿元(+20.1%)
  url: L2-Wiki/公司/fudan-micro.md
- title: 本仓库 Wiki 内证：NXP
  summary: 移动支付与安全（NFC/UWB/安全芯片，Apple等手机客户，占其营收约13%）
  url: L2-Wiki/公司/nxp.md
- title: 本仓库 Wiki 内证：Infineon
  summary: 传感器与安全IC（MEMS麦克风、雷达、TPM安全芯片）；安全互联(CSS)板块约占其营收25%
  url: L2-Wiki/公司/infineon.md
- title: 本仓库 Wiki 内证：紫光国微
  summary: 国产FPGA/特种IC、智能安全芯片、存储器；国产特种安全IC龙头
  url: L2-Wiki/公司/guoxin-micro.md
- title: QYResearch《2026全球安全加密芯片市场投资分析报告》
  summary: 安全加密芯片口径 2026 年 $56.50 亿、2032 年 $94.76 亿，CAGR 9.0%（2026-2032）——本赛道 TAM/CAGR 的取值依据
  url: 'https://dxpress.gelonghui.com/p/6385009'
- title: Global Info Research《2026-2032全球与中国安全单元芯片市场》
  summary: 安全单元芯片(SE) 2025 年 $37.04 亿、2032 年 $66.93 亿，CAGR 8.8%（偏窄口径，用于校验区间下界）
  url: 'https://dxpress.gelonghui.com/p/6160252'
- title: 格隆汇《智能卡和安全芯片市场情报》
  summary: 智能卡和安全芯片 2026 年 $42.80 亿、2032 年 $68.90 亿，CAGR 8.3%；前三厂商恩智浦/英飞凌/三星合计约 66%
  url: 'https://dxpress.gelonghui.com/p/6052031'
- title: Global Growth Insights《Embedded Security Market》
  summary: 嵌入式安全市场中英飞凌份额约 13-15%（居首）、恩智浦约 11-13%；约 38% 嵌入式安全产品基于安全单元与 eSIM
  url: 'https://www.globalgrowthinsights.com/de/market-reports/embedded-security-market-122040'
- title: UTW《全球及中国智能卡行业价值链专项报告（2026）》
  summary: 2026 全球智能卡出货 118.6 亿张；金融IC卡 46.8 亿张，金融卡领域 CR5 达 74.2%；物理SIM受eSIM冲击 -3.2% 至 38.5 亿张
  url: 'https://www.utw.net.cn/2191/view-512142-1.html'
- title: 本仓库 L0 归档：2026-09-13 安全芯片 TAM/份额补验
  summary: 三条搜索词、全部返回 URL、数据提取清单与口径裁定过程（含 $9B 估算不成立的论证）
  url: 'L0-原始资料池/04-行业数据/2026-09-13-安全芯片-市场规模补验-调研笔记.md'
- title: 本仓库 L0 归档：Thales / 国民技术 / 华大电子 / 大唐微电子 公司调研
  summary: 本赛道 4 家核心成员的公司级调研归档（input_20260913_109~112），含各自财务、产品结构、认证壁垒与竞争地位
  url: 'L0-原始资料池/03-新闻/'
---

# 安全芯片

> **半导体** · L3 · TAM **$5.7B** · CAGR **9%**

安全芯片是**用硬件保证"身份与交易不可伪造"的专用芯片**——金融IC、SIM卡、eSE/iSE、车规HSM、TPM。它的护城河不是制程而是**认证**：银行卡要过 CC EAL5+/EAL6+、车规要过 AEC-Q100 与 SHE+、无线支付要过 WPC。认证周期长、切换成本高，因此毛利率（35-50%）显著高于普通MCU。中国在SIM卡与身份证已主导，**最高安全等级与车规HSM仍是缺口**。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $5.7B（安全加密芯片口径，QYResearch 2026） |
| 年复合增长率(CAGR) | 9%（QYResearch 2026-2032） |
| 利润率区间 | 35-50% |
| 成本占比 | 2% (终端整机成本) |
| 利润池占比 | 3% (半导体利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-09-13（新建赛道）
> 来源: 本仓库 Wiki 内证（复旦微电 / NXP / Infineon / 紫光国微），见 sources
> 置信度: 中（结构与人证充分，**数值待外部验证**）

- **建赛道缘由**: 复旦微电（688385）被公司词条引用为 `segments: [FPGA, 安全芯片]`，但该赛道此前**从未创建**（属"幽灵赛道"）。本赛道建立以修复该悬空引用。此前复旦微电的"安全与识别芯片"业务（1H26 收入4.72亿元、+20.1%）在 Wiki 中**无赛道归属**。
- **定位**: 半导体 L3 芯片设计环节的独立品类——与「模拟芯片」「FPGA」并列，不重叠（模拟芯片覆盖信号链/电源，安全芯片覆盖身份认证与交易安全）
- **数据来源**: 结构性内容（竞争格局、壁垒、趋势、价格传导）取自本仓库已有的 复旦微电、NXP、Infineon、紫光国微 四个词条，可追溯
- **⚠️ 待验证项**: `tam_bn`(9.0) / `cagr_pct`(9.0) / 各厂商 `share` 均**未经外部来源核验**——本 session 的 WebSearch 配额已耗尽（400/400）。后续应补做 WebSearch（关键词如"安全芯片 市场规模 2026"、"CC EAL6+ 金融IC 份额"）并更新 sources。
- **companies 说明**: 收 紫光国微(002049)、复旦微电(688385)、NXP Semiconductors、Infineon 四家（均有公司页）
- **✅ 原「待建公司页」4 家已全部建成（2026-09-13 晚）**，见下方 2026-09-13（第二段）更新记录。

### 更新 2026-09-13（补建 4 家公司词条）
> 来源: 见 sources（各公司 L0 调研归档 input_20260913_109~112）
> 置信度: 中（公司层数据多来自公开报道与母公司口径，部分字段（供应商、单体财务）无公开披露）

- **`companies` 由 4 家扩至 8 家**：新增 Thales(HO.PA,龙头)、国民技术(300077.SZ,直接相关)、华大电子(未上市,直接相关)、大唐微电子(未上市/ticker取母公司600198.SH,直接相关)。**本赛道 `companies` 至此具备完整代表性**。
- **⚠️ Thales 定位纠正（重要）**：Thales 实为**智能卡 + eSIM 平台 + 安全服务商，芯片主要外采**，并非安全芯片设计公司。此前 `competition.global` 将其与 NXP/Infineon/STMicro 并列，容易被误读为同类竞争者。已在竞争格局 note 与 `chain_role` 说明中显式标注口径，其市场份额指标（银行业非接触智能卡 21.1%、eSIM Provisioning 第一）**属智能卡/平台口径，不等于芯片口径**。
- **⚠️ 国民技术结构提示**：1H26 营收 9.06 亿(+43.39%)、归母 441.49 万扭亏，但**扣非仍亏 2,356.87 万，扭亏全靠 2,674 万公允价值变动收益**，经营现金流 −2.73 亿。且**负极材料收入占比已达 50.19%，超过芯片业务**——作为"安全芯片"标的的代表性需打折看待。
- **华大电子**：未上市，`latest_revenue` 只能用母公司 00085.HK 合并口径代理（FY2025 收入 21.81 亿港元，−7.14%；量 +13.3% 但毛利率 −9.9pct 至 38.4%），已在字段内标注。安全芯片累计出货超 250 亿颗、SIM/eSIM 全球份额超 20%、CIU9872B_01 过 CC EAL6+。
- **大唐微电子**：社保卡芯片市占超 40%、身份证芯片累计出货超 6 亿枚；但 2026 H1 收入 +26.82% 而净利 −11.88%（净利率 34.7%→24.1%），经营现金流转负。**市占率与行业排名仅有个别历史口径（2019年社保卡），所有来源均未给出最新数字**。
- **已知缺口（诚实记录）**：4 家公司的 `suppliers` 全部留空——公开渠道均未披露晶圆代工与封测供应商名单，未作任何推测填充。

### 更新 2026-09-13（TAM/CAGR/厂商份额外部补验）
> 来源: 见 sources（QYResearch / Global Info Research / 格隆汇 / Global Growth Insights / UTW）
> L0 归档: `L0-原始资料池/04-行业数据/2026-09-13-安全芯片-市场规模补验-调研笔记.md`（input_20260913_107）
> 置信度: 中（口径交叉印证充分，但证据为搜索摘要级，未取得付费报告原文）

- **`tam_bn` 9.0 → 5.7（下修）**：原 $9B 为估算值，**没有任何来源支持该取值**。补验后按「安全加密芯片」口径（QYResearch 2026 年 $56.50 亿）修正为 **$5.7B**。该口径覆盖 SE + HSM + 加密芯片，与本赛道「金融IC/SIM/eSE/车规HSM/TPM」的定义最贴合；纯 SE 口径（$37.04 亿）与智能卡口径（$42.80 亿）偏窄，IIM 宽口径（$218.7 亿）不采信。
- **`cagr_pct` 9.0 维持不变，但由「估算」升为「有据」**：QYResearch 2026-2032 CAGR 9.0%，并获 GIR 8.8% / MMG 9.5% / 智能卡口径 8.3% 交叉印证。
- **厂商 `share` 首次填值**：NXP `~12%`、Infineon `~14%`（嵌入式安全口径，英飞凌居首）；Thales/ST/Microchip 维持 `-`（未检索到个别份额）。补充 CR3 = 66%（NXP/英飞凌/三星）、安全加密芯片 CR5 ≈ 67.4%、汽车安全单元 CR5 ≈ 68%。
- **新增 2 条 key_trends**：金融IC卡存量替换期与国密算法（CR5 74.2%、国密支持率 92%）；物理SIM受eSIM替代但安全芯片用量不减（SIM -3.2%，SIM/eSIM内嵌安全芯片 14.2 亿颗 +11.5%）。
- **`tech_gap.detail` 补实**：原为空字符串，补入 CR5 74.2%、国际巨头占高端约 70%、国产在细分市占超 60% 但集中于非最高安全等级。
- **口径敏感性提示**：本赛道全球规模因口径不同可从 $42.8 亿跨至 $218.7 亿（约 5 倍），**跨赛道比较 TAM 时需注意口径差异**。
