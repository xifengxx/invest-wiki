---
name: Skyworks Solutions
slug: skyworks
country: 美国
type: company
website: "https://www.skyworksinc.com"
updated: 2026-09
data_freshness_date: 2026-09-13
industries:
- 半导体
segments:
- 模拟芯片
- 射频芯片
one_liner: |
  全球射频前端(RF FEM)#2，设计智能手机功率放大器/滤波器/开关及Sky5模组，通过向Apple等OEM销售RF前端芯片实现盈利，位于半导体L3核心产品层——iPhone射频链核心供应商（占营收65-70%），2025年10月宣布与Qorvo合并。
  【2026.9.13更新】FY2025营收$4.09B(-2%)；FQ3 2026营收$935M(-3% YoY)，盈利承压（营业利益率8.8%）。
chain_layer: L4
chain_role: 核心参与者
founded: 2002
headquarters: 美国加州尔湾
employees: "~8,000"
latest_revenue: "FY2025 $4.09B（-2% YoY，财年9月底止）；FQ3 2026 $935M（-3% YoY）"
market_cap: "~$13.3B（2026.9）"
description: Skyworks Solutions是全球第二大射频前端芯片公司，2002年由Alpha Industries与Conexant无线通信部门合并成立。公司以手机功率放大器和射频滤波器起家，深度绑定Apple供应链（占营收65-70%），同时拓展汽车、基础设施和工业物联网等非移动市场。2025年10月宣布与竞争对手Qorvo合并组建RF芯片新巨头。
core_business:
- 射频前端模组（Sky5平台：PA+滤波器+开关集成的FEMiD/PAMiD）
- 功率放大器（蜂窝4G/5G PA，手机主力产品）
- 射频滤波器（SAW/BAW/TC-SAW，频段滤波）
- 射频开关与LNA（天线调谐/接收链路）
- 广域市场芯片（车载信息娱乐RF、工业IoT连接、5G小基站）
revenue_model: "通过向OEM/ODM销售RF前端芯片与模组实现盈利（Apple占65-70%），移动业务~60%+广域市场~40%"
suppliers:
- company: 台积电
  ticker: TSM
  supplies: "RF SOI/CMOS晶圆代工（开关/LNA）"
  note: "射频SOI主力代工"
- company: GlobalFoundries
  ticker: GFS
  supplies: "RF SOI晶圆代工"
  note: "二线代工分散产能"
- company: 自有BAW滤波器产线（德州/墨西哥）
  supplies: "BAW滤波器自产"
  note: "垂直整合滤波器产能（收购NEC/松下滤波器资产）"
customers:
- company: Apple
  ticker: AAPL
  revenue_pct: 68
  note: "iPhone PA/滤波器/开关主力供应商（65-70%营收占比）"
- company: Samsung
  supplies: "RF前端芯片"
  note: "安卓旗舰机RF供应商"
- company: 其他安卓OEM（小米/OPPO/vivo等）
  supplies: "RF前端芯片"
  note: "通过ODM渠道供货"
partners:
- company: Apple
  area: "iPhone射频联合设计"
  note: "深度绑定，FEMiD模组定制"
competitors:
- company: Qorvo
  ticker: QRVO
  area: "RF前端"
  note: "全球#3 RF厂商，**2025.10宣布与Skyworks合并**"
- company: Broadcom
  ticker: AVGO
  area: "BAW滤波器/FEM"
  note: "BAW滤波器技术领先，Apple FEMiD竞争"
- company: Qualcomm
  ticker: QCOM
  area: "RF前端模组"
  note: "随SoC捆绑RF360模组"
- company: Murata村田
  area: "SAW滤波器/模组"
  note: "SAW滤波器龙头"
---
# Skyworks Solutions

从Alpha Industries的砷化镓PA到Sky5集成模组，Skyworks把iPhone的射频链做成了年入40亿美元的生意——而现在，它正与Qorvo走向合并，重划RF前端版图。

## 财务状况

Skyworks财年截至9月底。移动业务（主要是Apple）主导收入，行业受手机大盘与5G升级节奏影响。

### 年度核心财务指标

| 指标 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|
| **营收** | $4.77B | $4.18B | **$4.09B** |
| **同比** | -13% | -12% | -2.2% |
| **净利润** | $983M | $596M | **$477M** |
| **净利率** | 20.6% | 14.3% | 11.7% |

### FY2026季度趋势（截至2026年6月，跌幅收窄但盈利承压）

| 季度 | 营收 | 净利 | 备注 |
|------|------|------|------|
| FQ1 2026（12月止） | $1.04B | $79M | iPhone旺季 |
| FQ2 2026（3月止） | $944M | $36M | 淡季 |
| **FQ3 2026（6月止）** | **$935M** | **$34M** | -3.1% YoY，毛利率40.7%、营业利益率8.8% |

连续四年营收下滑（FY2022 $5.49B → FY2025 $4.09B），跌幅收窄但盈利大幅压缩（营业利润率从FY2022的~30%跌至8.8%），原因：安卓竞争+Apple份额被Broadcom/Qualcomm分食+价格压力。2025年10月宣布与Qorvo合并（新实体聚焦手机RF芯片，合计营收~$8B），以规模效应对抗下行周期，待监管审批。

## 产品线详解

| 产品线 | 营收占比 | 说明 |
|--------|---------|------|
| **移动（手机）** | ~60% | Apple占绝对主导（65-70%来自Apple整体），Sky5模组+分立PA/开关 |
| **广域市场** | ~40% | 车载（信息娱乐/连接）、5G基础设施、工业IoT、Wi-Fi 6E/7 |

移动业务核心产品：FEMiD（集成滤波器的前端模组，iPhone独供）、PAMiD（PA+滤波器集成模组）、分立PA/开关/LNA。广域市场增长点：车载DRM/连接模组（IATF 16949认证）、5G小基站RF、Wi-Fi前端。

## 技术路线图

- **BAW滤波器扩产**：德州Waco厂垂直整合BAW产能，对标Broadcom技术优势
- **5G毫米波/Sub-6GHz模组**：更高集成度的毫米波AiP（antenna-in-package）
- **与Qorvo合并**（2025.10宣布）：新实体聚焦手机RF芯片，合并后合计营收~$8B，规模效应对抗Broadcom/Qualcomm
- **车载射频**：IATF 16949车规认证完成（2024），车联网V2X RF模组布局

## 融资与现金流

- 年经营现金流~$1.2B，自由现金流~$1.0B
- 资产负债表稳健：净现金头寸，无重大杠杆
- 股东回报：持续回购（年化~$500M-1B）+小额股息

## 研发投入与专利

- 年研发投入~$600M（占营收~15%），RF设计工程师占全员约40%
- 专利储备5,000+件，覆盖BAW谐振器结构、PA Doherty架构、集成模组封装
- 核心壁垒：Apple深度协同设计（FEMiD定制）、BAW垂直整合产能、RF系统级know-how

## 动态更新记录

### 2026-09-13（D1批次：待深化龙头清单补全）
- **来源**：`L0-原始资料池/03-新闻/2026-09-13-D1批次-5家薄档龙头公司-数据溯源.md` (input_20260913_118)
- **核心更新**：由11字段骨架补全至25字段+5 body段，补入FY2023-2024财务、Apple依赖度、**与Qorvo合并事件（2025.10）**
