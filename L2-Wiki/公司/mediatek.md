---
name: MediaTek (联发科)
slug: mediatek
country: 台湾
ticker: 2454.TW
type: company
updated: 2026-08
data_freshness_date: 2026-08-18
segments:
- AI芯片设计(Fabless)
- ASIC/AI定制芯片
- 手机SoC
- 网络交换芯片
one_liner: |
  全球最大智能手机SoC供应商（出货量#1）和AI ASIC新兴主力，通过手机SoC+Smart Edge+AI定制芯片三大板块实现盈利，2026年AI ASIC营收目标$2B，拿下Google TPU v9主供地位（取代Broadcom），Fabless模式依赖TSMC先进制程代工，市值~$191B。
  【2026.8.18更新】Q2 2026营收NT$1,521.83亿(+1.2% YoY)、毛利率46.2%、归母净利NT$243.4亿(-12.6% YoY)、EPS NT$15.28；首颗AI加速器ASIC Q4量产、数据中心营收2026超$2B、2027市占目标上调至15-20%。
chain_layer: L3
chain_role: 龙头
suppliers:
- company: 台积电
  ticker: TSM
  supplies: 先进制程晶圆代工
  note: 2nm/3nm/4nm制程+CoWoS封装，TPU v9使用2nm+HBM4e
- company: Arm Holdings
  ticker: ARM
  supplies: CPU/GPU IP核授权
  note: 手机SoC和AI芯片均使用ARM架构
customers:
- company: Google
  ticker: GOOGL
  revenue_pct: 10
  note: TPU v9主供地位，预计2028年贡献$360B营收（SAM口径）
- company: 小米
  revenue_pct: 8
  note: 旗舰+中端手机SoC
- company: vivo
  revenue_pct: 7
  note: 天玑Dimensity系列
- company: 三星电子
  ticker: 005930.KS
  note: 争取中，天玑D9500竞标Galaxy S27 FE
partners:
- company: 台积电
  ticker: TSM
  area: 先进制程+先进封装
  note: 2nm制程HBM4e集成（TPU v9）
- company: Google
  ticker: GOOGL
  area: AI ASIC联合开发
  note: TPU v9项目（Humafish/A5922）
competitors:
- company: Qualcomm
  ticker: QCOM
  area: 手机SoC
  note: 高端旗舰市场份额领先
- company: Broadcom
  ticker: AVGO
  area: AI ASIC设计
  note: TPU v9被降级为辅角色
- company: NVIDIA
  ticker: NVDA
  area: AI加速器
  note: GPU vs ASIC长期竞争
- company: 紫光展锐（Unisoc）
  area: 中低端手机SoC
  note: 中国市场替代风险
core_business:
- 智能手机SoC设计（天玑Dimensity系列，全球出货量#1，占营收>50%）
- Smart Edge/IoT平台（平板/Chromebook/智能家居/车用，占~40%营收）
- AI ASIC定制芯片（Google TPU v9主供，2nm+HBM4e，2026年目标$2B）
- 电源管理IC（移动设备+数据中心）
revenue_model: 2026E营收~NT$6,376亿（~$19.5B USD），EPS NT$64.30。手机SoC >50% + Smart Edge >40% + Power IC。Fabless模式毛利率~45-48%，AI ASIC业务（Google TPU v9主导）预计贡献$8B+营收（2028年），有望大幅提升整体利润率。
founded: 1997
headquarters: 台湾新竹
employees: ~22,000
latest_revenue: Q2 2026 单季 NT$1,521.83亿（约$4.7B USD），+2.0% QoQ / +1.2% YoY，超财测高标
market_cap: ~NT$6.26T（~$192B USD）（2026.8）
description: 联发科（MediaTek）是全球最大的智能手机SoC供应商（按出货量计），1997年成立于台湾新竹，从DVD芯片起家发展为全球Fabless Top 5半导体设计公司。手机SoC（天玑Dimensity系列）覆盖小米/vivo/OPPO等安卓厂商，并正在争取三星旗舰机供应权。AI定制芯片（ASIC）业务成为第二增长曲线：拿下Google TPU v9项目主供地位（取代Broadcom），采用TSMC 2nm制程+HBM4e，预计2028年带来$8B+营收。AI ASIC可服务市场（SAM）预计2027年达$700-800B。
website: https://www.mediatek.com
industry: AI算力
---

# MediaTek (联发科)

全球手机SoC出货量冠军，Fabless Top 5，天玑Dimensity系列AI芯片全线出击，AI ASIC成为第二增长曲线——Google TPU v9主供地位有望复制Broadcom的AI定制芯片成功路径。

## 财务状况

2026年联发科受益于手机市场复苏+AI ASIC业务爆发双引擎驱动。

### 核心财务指标

| 指标 | 2025A（估计） | 2026E | Q2 2026（实际） | 同比变化 |
|------|:-----------:|:-----:|:--------------:|:------:|
| **营收** | ~NT$5,500亿 | **NT$6,376亿** | NT$1,521.83亿（单季） | +16% |
| **毛利率** | ~45% | ~46-48% | **46.2%** | -2.9pp |
| **EPS** | ~NT$50 | **NT$64.30** | NT$15.28（单季） | +29% |
| **AI ASIC营收** | ~$1B | **$2B** | 2026E >$2B（数据中心） | +100% |

### 业务构成

| 板块 | 占比 | 关键客户/产品 |
|------|:--:|------|
| **Mobile（手机SoC）** | >50% | 天玑D9500，小米/vivo/OPPO，三星竞选 |
| **Smart Edge（智能边缘）** | >40% | 平板/Chromebook/IoT/车用 |
| **Power IC（电源管理）** | <10% | 移动+数据中心PMIC |

### Q2 2026 详情（海豚研究）

> 数据来源：2026-07-31 法说会，Q2 2026 = 2026年4-6月（截止 2026-06-30），为当前最新已发布财报。L0 归档 `input_20260818_016`。

- **营收**：NT$1,521.83亿（约$4.7B USD），+2.0% QoQ / +1.2% YoY，超财测高标。
- **毛利率**：46.2%，环比-0.1pp、同比-2.9pp（去年同期含一次性利益垫高基期）。
- **归母净利润**：NT$243.4亿（税后净利 NT$246.05亿），同比-12.6%，EPS NT$15.28（上季15.17、去年同期17.50）。
- **净利率**：16.2%（上季16.3%、去年同期18.7%）；上半年累计税后净利 NT$489.81亿（-15% YoY）。
- **细分**：Smart Edge 平台升至 53% 营收（+19% QoQ / +26% YoY，跃居最大板块），手机降至 41%（-14% QoQ / -20% YoY，需求疲软+成本上升），Power IC 6%（+11% QoQ）。

**AI ASIC 第二增长曲线加速**：
- 首颗 AI 加速器 ASIC（Google TPU v9）**Q4 2026 进入量产**；数据中心营收 2026 年预计**超 $2B**。
- 2027 数据中心 TAM 上调至 $80B，市占目标 10-15% → **15-20%**；第二颗 AI 加速器 ASIC 目标 2028 年量产，ASIC 第二客户落地。
- 董事会通过 **$50亿美元** discretionary 融资预算，锁定供应链产能，从 ASIC 芯片扩展至完整数据中心系统。

**Q3 2026 指引**：营收 NT$1,522-1,598亿（环比持平至+5% / 同比+7-12%），毛利率 46%±1.5pp；全年营收达目标高标，美元口径高个位数增长。


## 融资与现金流

- 详见财务状况章节
## 投资亮点

- **AI ASIC第二曲线**：Google TPU v9+另外2~3个Hyperscaler项目在谈，SAM 2027E $700-800B
- **2nm率先采用**：TPU v9采用TSMC 2nm+HBM4e，与博通/英伟达同步推进先进节点
- **手机市场复苏**：5G SoC ASP提升，三星旗舰机供应突破有望
- **Fabless轻资产**：无需晶圆厂资本支出，ROE持续维持在25%+

## 动态更新记录

- 2026-08-18：归档 Q2 2026 财报（input_20260818_016）。更新 data_freshness_date→2026-08-18、updated→2026-08、latest_revenue（Q2 单季 NT$1,521.83亿）、market_cap（~NT$6.26T）；one_liner 追加【2026.8.18更新】；财务表加 Q2 2026 列；body 追加「Q2 2026 详情（海豚研究）」。
