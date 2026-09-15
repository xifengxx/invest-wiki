---
name: Lambda Labs
slug: lambda-labs
country: US
ticker: LAMBDA   # 未上市；用公司专属非交易键，勿填估值当市值
type: company
updated: 2026-09
data_freshness_date: 2026-09-15
industries:
- AI算力
segments:
- 云计算IaaS
one_liner: |
  美国私有GPU云和AI基础设施公司，提供按需实例、预留算力、私有AI工厂和Superclusters服务，位于AI算力L4基础设施层。2026年8月关闭$926M高级担保定期贷款B，用于为投资级客户部署GPU；2025年11月披露$1.5B融资，投后估值$5.43B。
chain_layer: L4
chain_role: 核心参与者
suppliers:
- company: NVIDIA
  ticker: NVDA
  supplies: AI GPU与集群平台
  note: Lambda基于NVIDIA GPU提供云服务和AI工厂
- company: 数据中心与电力供应商
  supplies: GPU集群机房、电力、制冷与网络
- company: 摩根士丹利
  supplies: 定期贷款B主承销
  note: 属于融资服务机构，不是传统生产资料供应商
customers:
- company: 投资级客户
  note: 官方2026-08公告称$926M贷款用于为其部署GPU，未披露客户名称
- company: Microsoft
  note: TechCrunch引Bloomberg报道，JPMorgan安排$1B私募债购入GB300并租给Microsoft；该报道为交易背景，不是Lambda官方财报数据
- company: 企业、政府与研究机构
  note: 通过实例、预留容量和私有集群采购训练与推理算力
partners:
- company: 摩根士丹利
  area: $926M定期贷款B主承销
- company: JPMorgan
  area: TechCrunch引Bloomberg报道的私募债安排；口径需与Lambda公告区分
- company: NVIDIA
  ticker: NVDA
  area: AI算力生态与GPU平台
competitors:
- company: CoreWeave
  ticker: CRWV
  area: GPU专用云与AI基础设施
- company: Nebius
  area: AI云与GPU算力
- company: Oracle / AWS / Microsoft Azure
  area: 通用云厂商的AI算力与托管实例
- company: Together AI
  ticker: TOGETHER
  area: AI原生云与推理/训练算力服务
core_business:
- 按需GPU实例与长期预留算力
- 私有AI工厂、Superclusters与1-Click Clusters
- 训练与推理集群运维、调度和GPU资产管理
- 企业与政府AI基础设施交付
revenue_model: 收入主要来自GPU云服务费、预留容量和私有AI工厂/Superclusters交付与运维。公司未在本轮核验中披露GAAP营收；$926M、$1B等融资额是债务工具，不是收入。
founded: 2012
headquarters: 美国加州圣何塞
employees: 未披露
latest_revenue: 未披露GAAP营收；可用财务信号为2026-08 $926M定期贷款B和2025-11 $1.5B融资
market_cap: 未上市；2025-11 PitchBook口径投后估值$5.43B，2026-08媒体报道拟$3B pre-IPO、估值约$12B（未经确认）
description: |
  Lambda Labs成立于2012年，定位“Superintelligence Cloud”，业务从GPU工作站和云实例延伸到私有AI工厂、1-Click Clusters和大型Superclusters。2026-08-27公司宣布关闭$926M高级担保定期贷款B，由摩根士丹利主承销，用于为投资级客户部署GPU。此前2025-11以$5.43B投后估值完成$1.5B融资，2026-08另有约$12B估值的pre-IPO融资报道，但后者未经公司确认。
website: https://www.lambdalabs.com
---

# Lambda Labs

Lambda的看点不是简单的“GPU租售”，而是把NVIDIA平台、机房电力、金融工具和集群交付绑成一条AI基础设施供给链。私有公司口径下，最可靠的信息是债务条款、融资轮次和客户部署事件，而不是未经披露的营收推算。

## 财务状况与融资结构

Lambda未披露完整GAAP财务报表，当前可用数据集中在融资与债务。

| 指标 | 数值 | 口径说明 |
|------|------|----------|
| 定期贷款B | **$926M** | 2026-08-27关闭，高级担保 |
| 到期日 | 2030-12-31 | Moody's Baa2评级口径 |
| 利率 | SOFR + 3.00% | 99.5%发行 |
| 抵押与用途 | GPU资产SPV；为投资级客户部署GPU | 官方公告 |
| 主承销 | 摩根士丹利 | 官方公告 |
| 2026-05信贷额度 | 约$1.0B | 担保信贷额度 |
| 2025-11融资 | $1.5B；投后$5.43B | PitchBook口径 |
| pre-IPO报道 | 约$3B、投后约$12B | 2026-08媒体报道，未经确认 |

债务融资的好处是比稀释股权更快锁定GPU产能，但AI服务器折旧快、机型更新频繁，若租约期限、上电进度或客户续约不及预期，资产回收周期会显著影响现金流。判断Lambda时，应跟踪租约覆盖倍数、债务摊销、GPU代际转换成本和客户集中度。

## 产品与技术路线

- **按需实例**：面向训练和推理的单卡/多卡GPU实例，强调快速获取NVIDIA算力。
- **预留容量**：为长期训练任务锁定集群资源，适合大模型预训练、微调和持续推理。
- **1-Click Clusters与Superclusters**：把GPU节点、网络、存储、调度和运维模板化，缩短大规模集群交付时间。
- **私有AI工厂**：为企业和政府交付专属基础设施，兼顾数据主权、容量规划和长期运维。

## 竞争定位

Lambda处在“超大规模云厂商”和“AI原生云”之间的空白带：Oracle、AWS、Azure有企业客户和全球资源，但高需求机型供给和价格弹性未必灵活；CoreWeave、Nebius等AI云同样专注GPU规模，直接争夺长期租约。Lambda的差异化在于长期AI基础设施交付经验、私有集群产品和金融化GPU扩张。风险也很直接：GPU厂商供给节奏、电力交付、客户集中度和债务成本都会放大经营波动。

## 客户与生态

官方2026-08公告只称$926M贷款用于投资级客户，没有披露客户名。TechCrunch引Bloomberg报道，JPMorgan安排$1B私募债购买GB300并租给Microsoft，这解释了当前AI云中“金融机构出资、GPU资产SPV、AI云运营、大客户承租”的结构。这个事件与Lambda官方公告的$926M贷款是不同口径，正文不把二者合并成一笔资金。NVIDIA参与生态合作，摩根士丹利和JPMorgan则是资金安排方。

## 动态更新记录

### 2026-09-15：薄档升级为全面档
- **来源**：Lambda官网2026-08-27公告、TechCrunch 2026-08-28报道，归档于`L0-原始资料池/03-新闻/2026-09-15-F5批次-AI云与模拟组4家-数据溯源.md`（input_20260915_136）。
- **核心更新**：补齐$926M定期贷款B条款、$1.5B融资与$5.43B投后估值、pre-IPO报道、GPU云产品线和竞争格局。
- **关键区分**：公司未披露GAAP营收；$12B估值报道未经确认；私募债租赁交易不与官方定期贷款混同。
