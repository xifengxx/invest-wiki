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
    note: 法国，金融IC与eSIM/eSE全球龙头，CC EAL6+最高安全等级；多份报告列为SE主要厂商但未披露个别份额
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
- **⚠️ 待建公司页（本赛道重要成员但 Wiki 无词条，故未列入 companies 以免造成悬空引用）**: Thales(HO.PA，金融IC与eSIM全球龙头，CC EAL6+)、国民技术(300077)、华大电子、大唐微电子。补齐后本赛道 companies 才具备完整代表性。

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
