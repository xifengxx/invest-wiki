---
name: 华为
slug: huawei
country: CN
ticker: 未上市
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- AI服务器
- AI训练集群/超算
- ASIC/AI定制芯片
- FPGA
- 晶圆代工(先进制程)
- 网络交换芯片
one_liner: 中国最大ICT和AI芯片厂商，自主研发昇腾AI芯片+鲲鹏CPU+5G基站芯片，通过芯片+设备+云服务实现盈利，位于AI算力L3核心产品层——中国AI芯片国产替代核心力量
chain_layer: L3
chain_role: 龙头
suppliers:
- company: 中芯国际
  ticker: 688981.SH
  supplies: 7nm制程代工
  note: 受美国制裁，制程受限
- company: 长电科技
  ticker: 600584.SH
  supplies: 先进封装
- company: 京东方、维信诺
  supplies: OLED/折叠屏面板
- company: 豪威科技、舜宇光学
  supplies: CIS图像传感器与镜头模组
- company: 长江存储、长鑫存储
  supplies: 3D NAND闪存与DRAM内存
- company: 欣旺达、比亚迪电子
  supplies: 电池与结构件/整机组装
customers:
- company: 中国运营商
  note: 5G基站+通信设备
- company: 中国企业AI客户
  note: 昇腾AI芯片+集群
- company: 全球运营商
  note: 5G基站与通信网络设备
- company: 企业客户
  note: 昇腾AI服务器、鲲鹏计算、华为云服务
- company: 消费者
  note: 手机、平板、PC、可穿戴等终端产品
- company: 车企OEM
  note: 乾崑智驾方案、鸿蒙座舱，合作超600家产业链伙伴
- company: 政府与公共事业
  note: 智慧城市、政务云、数字能源基础设施
partners:
- company: 中芯国际
  ticker: 688981.SH
  area: 国产制程联合攻坚
competitors:
- company: NVIDIA
  ticker: NVDA
  area: AI GPU
  note: 昇腾910B性能约A100 80%
- company: Intel
  ticker: INTC
  area: 服务器CPU
  note: 鲲鹏vs Xeon
- company: 苹果
  note: 高端手机与生态系统竞争
- company: 高通
  note: 手机SoC与通信芯片
- company: 英伟达
  note: AI训练芯片，中国市场仍占约55%份额
- company: 爱立信/诺基亚/思科
  note: 全球通信设备市场
core_business:
- ICT基础设施（5G/5G-A基站、昇腾AI芯片、鲲鹏CPU、服务器与数据中心，2025年收入3750亿元）
- 终端业务（麒麟芯片手机/平板/PC、鸿蒙智行汽车，2025年手机出货4670万台重登中国第一）
- 智能汽车解决方案（乾崑智驾、鸿蒙座舱、896线激光雷达，2025年收入450亿元同比增长72%）
- 数字能源（超快充网络覆盖200+城市、AI化数字能源方案，2025年收入773亿元）
- 华为云（中国AI云市场份额13.1%排名第三，2025年收入322亿元）
revenue_model: 坚持以硬件为核心盈利模式，收入主要来自ICT基础设施设备（42.6%）和终端产品（39.1%）销售。2025年总营收8809亿元、净利润680亿元，研发投入1923亿元占收入21.8%。汽车与数字能源为高增长引擎。
founded: 1987
headquarters: 中国深圳
employees: ~207,000
latest_revenue: FY2025 ¥8809亿
market_cap: 未上市
ticker: 未上市
description: 华为是全球领先的ICT基础设施和智能终端提供商，也是中国AI芯片国产替代的领军企业。昇腾（Ascend）AI芯片系列是国内唯一实现大规模数据中心部署的AI训练/推理芯片，通过Atlas服务器和华为云对外提供服务。受美国制裁下实现全栈自主可控，是中国AI算力自主化的核心底座。
website: https://www.huawei.com
industry: AI算力
---

# 华为

中国AI芯片国产替代绝对龙头，昇腾+鲲鹏+华为云+CANN全栈自主可控AI基础设施

## 财务状况

| 指标 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|
| 营收(亿元) | 7,042 | 7,750 | 8,621 |
| 净利润(亿元) | 870 | 980 | 1,120 |
| 研发投入(亿元) | 1,647 | 1,790 | 1,950 |
| 净利润率 | 12.4% | 12.6% | 13.0% |

2025年营收重返制裁前历史高位水平。**ICT基础设施**（含AI服务器/云计算）贡献约55%营收，**终端业务**（手机/PC/车BU）约35%，**云计算和数字能源**约15%。华为云在中国公有云市场排名第二，AI云服务增速超**80%**。

## 产品线详解

- **昇腾AI芯片**：**Ascend 910B**（7nm，256 TFLOPS FP16，对标A100）、**Ascend 910C**（2025年，性能2x vs 910B，对标H100）。推理芯片**Ascend 310**系列用于边缘和终端
- **Atlas AI服务器**：Atlas 900（训练集群，4000+卡互联）、Atlas 800（推理服务器），国内运营商/政府/金融AI基础设施主力
- **CANN异构计算架构**：对标NVIDIA CUDA的软件栈，支持PyTorch/TensorFlow/MindSpore，**MindSpore**自研AI框架生态
- **鲲鹏CPU**：Kunpeng 920（ARM架构，7nm），服务器CPU，与昇腾组成双引擎
- **华为云**：GaussDB云原生AI数据库、ModelArts AI开发平台、盘古大模型（Pangu 5.0，万亿参数，NLP/CV/多模态/科学计算）
- **鸿蒙OS**：HarmonyOS NEXT，全球第三大移动操作系统生态，终端设备超9亿

## 技术路线图

- **Ascend 910C**：2025年量产，5nm等效制程（中芯国际N+2/N+3），FP16算力500+ TFLOPS，HBM3E集成，对标NVIDIA H100
- **Ascend 920**：2026-2027年，chiplet设计，算力1000+ TFLOPS，面向万亿参数大模型训练
- **鲲鹏930**：2026年，5nm，ARM v9架构，128核，面向数据中心和AI推理
- **盘古大模型6.0**：2026年，多模态推理+科学计算（气象/药物/材料），行业定制化部署
- **鸿蒙PC**：2025-2026年，鸿蒙OS桌面版，鲲鹏+昇腾驱动的AI PC
- **5.5G/6G**：2025-2026年，5.5G基站AI芯片内置、6G AI原生网络架构
- **制裁应对**：先进制程受限，通过chiplet+先进封装+架构创新弥补

## 研发投入与专利

| 指标 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|
| R&D(亿元) | 1,647 | 1,790 | 1,950 |
| R&D占营收 | 23.4% | 23.1% | 22.6% |

- 全球专利组合超过**120,000项**（2025年底），连续8年PCT国际专利申请量全球第一
- **核心技术壁垒**：昇腾AI芯片+CANN软件栈是唯一可对标NVIDIA CUDA的国产AI计算生态；5G/5.5G标准必要专利全球第一（20%+份额）；鸿蒙OS全球第三大移动生态（9亿+设备）；ICT基础设施全栈能力（芯片->设备->网络->云->AI）
- 2025年研发人员约**114,000人**（占员工总数55%），全球设36个联合创新中心+14个研发中心
- 受美国制裁倒逼全栈自主：MetaERP（替换Oracle）、GaussDB（替换Oracle DB）、EDA工具（替换Synopsys/Cadence）均已完成国产替代

