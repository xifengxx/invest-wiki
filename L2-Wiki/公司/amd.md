---
name: AMD
slug: amd
country: US
ticker: AMD
type: company
updated: 2026-07
data_freshness_date: 2026-08-05
segments:
- AI芯片设计(Fabless)
- CPU(服务器级)
- Chiplet与异构集成
- DPU/SmartNIC
- FPGA
- GPU制造代工
- GPU架构设计
one_liner: |
  全球第二大x86处理器与AI GPU芯片设计公司，核心为数据中心CPU/GPU（EPYC Turin、Instinct MI350/MI450）、客户端PC芯片（Ryzen）及FPGA（Xilinx），通过无晶圆厂芯片设计与系统平台销售实现盈利，位于AI计算第二梯队挑战者——以开放生态（ROCm）和性价比重构AI基础设施竞争格局。
  【2026.8.5更新】Q2营收$115.4亿(+50%, beat)，数据中心$67.2亿(+107%)，核心经营利润$22.7亿(+29%)。MI455X/Helios机架平台Q3出货，已获OpenAI 6GW+Meta 6GW+Anthropic 2GW+微软订单(14GW+)，但管理层未上调全年AI GPU指引($140-150亿)，盘后承压。服务器CPU份额>20%，H2指引+80%。
chain_layer: L3
chain_role: 龙头
suppliers:
- company: 台积电
  ticker: TSM
  supplies: 4nm/3nm晶圆代工+CoWoS封装
  note: 唯一代工+封装伙伴
- company: SK海力士
  ticker: 000660.KS
  supplies: HBM3E
  note: MI300X搭载HBM
- company: 通富微电
  ticker: 002156.SZ
  supplies: 封测服务
  note: AMD CPU/GPU主要封测伙伴
- company: TSMC
  supplies: 4nm/3nm先进制程代工及CoWoS先进封装，为AMD最主要代工伙伴，占CoWoS约11%产能配额
- company: Samsung Foundry
  supplies: 潜在第二供应商，2nm制程Venice CPU谈判进行中
- company: GlobalFoundries
  supplies: 成熟制程代工，I/O芯片等辅助组件
- company: ASE Group/Amkor
  supplies: 先进封装与测试服务
- company: SK Hynix/Samsung/Micron
  supplies: HBM3e/HBM4高带宽内存，为Instinct GPU配套
customers:
- company: Microsoft Azure
  ticker: MSFT
  note: MI300X部署于Azure AI实例
- company: Meta
  ticker: META
  note: EPYC CPU用于基础设施
- company: Oracle Cloud
  ticker: ORCL
  note: MI300X GPU租赁
- company: OpenAI
  note: 6GW MI450优先合作伙伴协议，2026下半年首期1GW部署
- company: Oracle Cloud Infrastructure
  note: 全球首家提供Helios AI超级集群的公有云服务商
- company: Google/AWS/Alibaba
  note: EPYC CPU云实例大规模采用，全球超1,600个云实例类型
partners:
- company: 台积电
  ticker: TSM
  area: 制程+CoWoS封装
- company: Xilinx
  area: FPGA自适应计算
  note: AMD全资子公司
competitors:
- company: NVIDIA
  ticker: NVDA
  area: AI GPU
  note: MI300X推理性能接近H100，训练仍有差距
- company: Intel
  ticker: INTC
  area: x86 CPU
  note: EPYC在服务器CPU市占率持续提升
- company: Broadcom
  note: AI ASIC定制芯片设计商，间接收紧AI算力市场，控制超50% ASIC市场份额
- company: 云厂商自研芯片
  note: Google TPU Ironwood、AWS Trainium 2/3、Microsoft Maia 200，均为替代风险
core_business:
- 数据中心AI GPU（Instinct MI300X/MI350/MI450/MI500系列，对标NVIDIA GPU）
- 数据中心服务器CPU（EPYC Turin 5代/Venice 6代Zen架构，最高256核）
- 客户端PC处理器（Ryzen 9000桌面/AI 300/AI 400移动端、Ryzen AI Max开发平台）
- FPGA与嵌入式芯片（Versal AI Edge Gen2、Spartan UltraScale+，Xilinx收购后关键业务）
- 机架级AI基础设施（Helios平台，集成72x MI455X GPU+EPYC Venice CPU+Pensando网络）
revenue_model: FY2025全年营收$346亿（+34% YoY），Non-GAAP毛利率52%，净利润$25亿。其中数据中心业务$166亿（48%），客户端业务$146亿（42%），嵌入式$35亿（10%）。AI GPU预计2027年收入达数百亿美元级，公司目标数据中心收入未来3-5年保持60%+年均增长。
founded: 1969
headquarters: 美国加州圣克拉拉
employees: ~26,000
latest_revenue: Q2 FY2026 $115.4亿（+50% YoY），H1 ~$218亿
market_cap: ~$900B（2026.7）
description: AMD（Advanced Micro Devices）是一家全球领先的半导体公司，由Jerry Sanders于1969年创立，总部位于加州圣克拉拉。AMD在CEO苏姿丰博士的领导下完成史诗级逆转，凭借Zen架构CPU和Instinct系列AI GPU，成功从英特尔追赶者蜕变为横跨CPU、GPU、FPGA三大赛道的算力巨头。公司通过2022年收购赛灵思（Xilinx）补全自适应计算版图，2025财年营收突破346亿美元，数据中心业务成为第一大收入来源。AMD以chiplet芯粒设计、3D
  V-Cache堆叠和Infinity Fabric互连技术构筑差异化护城河，在AI训练与推理市场持续挑战NVIDIA霸主地位。
website: https://www.amd.com
industry: AI算力
---

# AMD

从濒临破产到市值超越英特尔，AMD凭借Zen架构CPU和Instinct AI GPU的双引擎战略，成为全球唯一横跨x86处理器、数据中心GPU和FPGA的算力平台公司。

## 财务状况

**2025财年核心指标（GAAP）：**
- 年收入：**346亿美元**（同比+34%）
- 毛利率：**50%**（同比+1ppt）
- 净利润：**43亿美元**（同比+164%）
- 摊薄EPS：**$2.65**（同比+165%）

**近三年财务趋势：**

| 指标 | FY2023 | FY2024 | FY2025 | Q1 FY2026 | Q2 FY2026 |
|------|--------|--------|--------|-----------|-----------|
| 营收 | ~$227亿 | $258亿 | **$346亿** | — | **$115.4亿** |
| 毛利率(GAAP) | ~50% | 49% | **50%** | — | **53.8%** |
| 净利润(GAAP) | ~$8.5亿 | $16.3亿 | **$43亿** | — | **$23亿** |
| 数据中心收入 | ~$65亿 | ~$126亿 | **$166亿** | — | **$67.2亿** |

### Q2 FY2026 详情（2026.8.5 海豚研究）

| 业务 | Q2收入 | YoY | 关键信息 |
|------|:------:|:--:|------|
| **数据中心** | $67.2亿 | **+107%** | AI GPU ~$27亿(MI355X) + 服务器CPU ~$40亿(+12% QoQ) |
| **客户端** | $30.6亿 | +22.5% | PC市场下滑中逆势增长，份额持续侵蚀Intel |
| **游戏** | $7.8亿 | -30.6% | 主机周期第7年，过渡期 |
| **嵌入式** | $9.8亿 | +18.6% | 测试测量/航空航天/网络通信驱动 |

**Q3指引**：营收$127-133亿（中值+13% QoQ），non-GAAP毛利率~56%。

### MI455X/Helios 机架平台

| 维度 | 详情 |
|------|------|
| 出货时间 | Q3 FY2026开始 |
| 核心变化 | 从"单芯片"转向"机架级集群"交付，对标NVIDIA Rubin |
| 已获订单 | OpenAI 6GW + Meta 6GW + Anthropic 2GW + 微软（合计14GW+） |
| Helios整合 | Venice CPU + MI455X GPU + Pensando网络 + ROCm软件 |
| 性价比 | 同等功耗吞吐量比竞品高15%，每美元Token数高30% |
| 全年AI GPU指引 | **$140-150亿（未上调）** — 管理层保守，市场失望 |
| 服务器CPU H2指引 | **+80% YoY**；2027年 **+70%+** |

**FY2025收入结构（按业务）：**
- 数据中心：**$166.4亿（48%）**
- 客户端（Ryzen）：**$106亿（31%）**
- 游戏（Radeon/半定制）：**$39亿（11%）**
- 嵌入式（Xilinx）：**$34.5亿（10%）**

截至2026年7月，AMD市值约**8700-9000亿美元**，较2024年初增长超270%。

## 产品线详解

**数据中心GPU（Instinct系列）：**
- **MI300X**（2023.12发布，2024.1出货）：CDNA3架构，192GB HBM3，显存带宽5.3TB/s，FP8算力2.61 PFLOPS，显存容量为H100的2.4倍
- **MI350系列**（2025年中量产）：3nm制程，CDNA4架构，288GB HBM3E，4倍AI算力代际提升，35倍推理性能跃升
- **MI400系列**（2026年）：CDNA5（CDNA-next），432GB HBM4，FP4算力40 PFLOPS，搭配Helios机架平台

**EPYC服务器CPU：**
- **第五代"Turin"**：最高192核Zen 5C，当前旗舰，贡献Q4服务器收入过半
- **第六代"Venice"**（2026年）：Zen 6架构，最高256核，首款2nm制程CPU

**Ryzen客户端CPU：**持续蚕食英特尔份额，FY2025客户端收入**$106亿（+51%）**

**赛灵思FPGA/自适应SoC：**
- Versal系列（7nm ACAP）：AI Core/AI Edge/Premium/Prime子系列
- Virtex UltraScale+：旗舰高端FPGA，最高380万逻辑单元，HBM集成
- Kintex UltraScale+：中端性价比之选

竞争定位：CPU领域技术已反超英特尔，AI GPU领域以开放生态（ROCm）挑战NVIDIA CUDA壁垒。

## 技术路线图

**GPU路线图：**
- **2025：MI350系列**（CDNA4 + 3nm），288GB HBM3E，推理性能比MI300X提升35倍
- **2026：MI400系列**（CDNA5），432GB HBM4，搭配EPYC Venice + Pensando Vulcano 800G网卡组成**Helios机架平台**，单机架72颗GPU，FP4总算力2.9 EFLOPS。Meta已签约2026下半年部署，OpenAI签下MI450多代订单
- **2027：MI500系列**（CDNA6 + 2nm），HBM4E内存

**CPU路线图：**
- **2026：Zen 6**（2nm N2），CCD从8核升级12核，3D V-Cache总缓存突破200MB。服务器端EPYC Venice达256核512线程；桌面端Ryzen "Olympic Ridge"最高32核
- **2027-2028：Zen 7**，全新矩阵引擎，定位"真正的次世代架构"

**架构融合：UDNA**将消费级RDNA与数据中心CDNA合并为统一GPU架构，简化开发者生态

**核心技术栈：**
- **Chiplet芯粒设计**：异构集成，突破摩尔定律限制
- **3D V-Cache**：三维缓存堆叠，游戏与HPC性能倍增器
- **第五代Infinity Fabric**：节点到机架的统一互联，带宽224GB/s，支持PCIe 7.0
- **硅光子研发**：自2017年布局，目标突破铜互连的功耗-带宽瓶颈


## 融资与现金流

- 详见财务状况章节
## 研发投入与专利

**研发投入：**
- FY2025全年研发支出约**87.6亿美元**（TTM），同比增长31.55%，显著高于半导体行业均值（约21.9亿）
- Q1 2026单季研发支出**24亿美元**，同比增长38.72%
- 研发投入占收入比约25%，体现了AMD以技术驱动增长的坚定战略

**专利组合：**
- 全球专利总量**15,449件**，其中**9,827件已授权**，**12,040件活跃专利**
- 覆盖**7,467个独特专利族**，78%以上为活跃状态
- 2025年全年新增授权专利246件

**核心技术护城河：**
- **Chiplet芯粒专利**：AMD是multi-die架构的先驱，在2.5D/3D先进封装领域拥有30+专利族
- **Infinity Fabric互连**：已迭代至第五代，从单芯片互联演化为跨节点/机架的统一数据网络，是全球最快超算（Frontier、El Capitan）的核心互连架构
- **Zen架构IP**：经历Zen 1到Zen 5五代迭代，累计研发投入数百亿美元，构筑x86 CPU领域最强竞争壁垒
- **硅光子技术**：自2017年起布局，目标实现光互连对铜互连的替代

AMD以"架构优先"策略最大化IP杠杆效应——同一Zen/CDNA架构横跨服务器、桌面、笔记本、嵌入式，实现全场景覆盖。

## 动态更新记录

### 2026-08-05（海豚研究Q2财报分析）

- **来源**：`L0-原始资料池/03-新闻/2026-08-05-AMD-Q2-2026-财报分析-海豚研究.md` (input_20260805_001)
- **新增/更新**：
  - Q2 FY2026财务数据：营收$115.4亿(+50%, beat)，数据中心$67.2亿(+107%)，核心经营利润$22.7亿(+29%)
  - 分业务：AI GPU ~$27亿(MI355X) + 服务器CPU ~$40亿(份额>20%)
  - MI455X/Helios平台Q3出货，已获14GW+ CSP订单(OpenAI/Meta/Anthropic/微软)
  - Q3指引：营收$127-133亿，non-GAAP毛利率~56%
  - 服务器CPU H2指引+80%，2027年+70%+
  - 管理层未上调全年AI GPU指引($140-150亿)，市场失望
  - 海豚研究核心判断：CPU强势托底，MI455X/Helios破局是关键，管理层展望偏保守
- **冲突标记**：无冲突

