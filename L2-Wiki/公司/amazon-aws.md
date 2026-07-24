---
name: Amazon(AWS)
slug: amazon-aws
country: US
ticker: AMZN
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- AI Agent
- AI推理API服务
- AI模型训练平台
- AI训练集群/超算
- ASIC/AI定制芯片
- 云计算IaaS
one_liner: 全球最大云计算厂商，运营AWS云+自研Trainium AI训练芯片+Inferentia推理芯片，通过云计算+AI芯片+电商实现盈利，位于AI算力L4终端应用层
chain_layer: L4
chain_role: 龙头
suppliers:
- company: NVIDIA
  ticker: NVDA
  supplies: H100/B200 GPU
  note: AWS云GPU实例
- company: Marvell
  ticker: MRVL
  supplies: Trainium ASIC设计服务
  note: 联合设计Trainium
- company: 台积电
  ticker: TSM
  supplies: Trainium晶圆代工+CoWoS
- company: AMD
  supplies: EPYC服务器CPU、Instinct GPU，与AWS深度合作
- company: Intel
  supplies: Xeon服务器CPU，传统x86算力基础
- company: Broadcom
  supplies: 数据中心网络芯片、定制ASIC
- company: 台积电TSMC
  supplies: 为Trainium/Graviton自研芯片代工制造
customers:
- company: Anthropic
  note: Claude大模型训练, AWS投资$8B
- company: 全球企业AWS用户
  note: SageMaker AI+Bedrock平台
- company: OpenAI
  note: 7年$380亿算力合同，数十万NVIDIA GPU集群
- company: Netflix
  note: 长期AWS客户，流媒体全栈上云标杆
- company: Uber
  note: 核心工作负载迁移至AWS，采用Graviton/Trainium芯片
- company: Sony、Ericsson
  note: 首批采用AWS AgentCore AI智能体构建服务
partners:
- company: Anthropic
  area: Claude大模型
  note: 最大投资方+独占云服务商
- company: Marvell
  ticker: MRVL
  area: Trainium联合设计
competitors:
- company: Microsoft Azure
  ticker: MSFT
  area: 云计算
  note: AzurevsAWS
- company: Google Cloud
  ticker: GOOGL
  area: 云计算+AI芯片
  note: TPU vs Trainium
- company: 阿里云
  note: 全球份额4%，中国市场份额36%居首，亚太优势
- company: Oracle OCI
  note: 全球份额3%，增速66%，主打多云互联+数据库
core_business:
- 云计算IaaS/PaaS基础设施（EC2/S3/Lambda等200+服务）
- AI/ML平台与模型服务（Bedrock推理引擎、SageMaker训练平台）
- 自研AI芯片（Trainium2/3训练芯片、Graviton5 CPU，年化收入超$100亿）
- 数据库与分析（Aurora/Redshift/DynamoDB，云原生数据库生态）
- 企业级物联网与边缘计算（IoT Core、Wavelength 5G边缘节点）
revenue_model: 按用量付费的IaaS/PaaS模式，2025年全年营收$1287亿（同比+20%），贡献Amazon总利润的57%，AI年化营收超$150亿（同比三位数增长），积压合同$2440亿；自研芯片Trainium挑战NVIDIA性价比高30-40%。
founded: 1994
headquarters: 美国华盛顿州西雅图
employees: ~1,550,000
latest_revenue: Q1 2026 $181.5B（+28% YoY），AWS $37.6B（+28%）
market_cap: ~$2.3T
ticker: AMZN
description: 亚马逊（Amazon）是全球最大电商和云计算公司。AWS是全球第一大公有云，FY2025营收超$110B。自研Trainium/Inferentia AI芯片+Anthropic深度合作+Project Rainier超算集群，构成全栈AI基础设施能力。
website: https://www.amazon.com
industry: AI算力
---

# Amazon(AWS)

全球最大公有云AWS+自研Trainium AI芯片+Anthropic战略联盟，AI基础设施全栈巨头

## 财务状况

| 指标 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|
| 总营收($B) | 574 | 638 | 698 |
| AWS营收($B) | 91 | 105 | 122 |
| AWS营业利润($B) | 25 | 32 | 40 |
| 营业利润率 | 6.4% | 9.0% | 10.5% |

AWS贡献全公司约**65%的营业利润**，是利润核心。AI业务（Bedrock/SageMaker/Trainium）是AWS增长最快板块。FY2025 CapEx约**$85B**，绝大部分投向AI数据中心。

## 产品线详解

- **AWS云计算**：全球市占率约**32%**（领先Azure 23%、GCP 12%）。核心AI服务：Amazon Bedrock（多模型API）、SageMaker AI（ML训练推理）、Q Developer（AI编程助手）
- **自研AI芯片**：**Trainium2**（训练芯片，EC2 Trn2实例，对标H100）、**Trainium3**（2025年发布，3nm制程，性能3x提升）、**Inferentia3**（推理芯片，成本比GPU低40%）
- **Project Rainier**：与Anthropic合作的**10万+ Trainium芯片超算集群**（2025年上线），全球最大AI训练集群之一
- **Anthropic生态**：累计投资**$8B**，Claude 4系列模型通过Bedrock独家分发，深度绑定
- **电商+AI**：Rufus AI购物助手、AI仓储机器人（Sparrow/Proteus）、AI物流优化

## 技术路线图

- **Trainium3**：2025年发布，**3nm**制程，性能3x vs Trainium2，支持FP8/FP4混合精度训练，2026年大规模部署
- **Inferentia3**：2026年，推理延迟降低50%，成本比GPU方案低40%
- **Ultracluster**：2026-2027年，**20万+ Trainium3芯片**集群，面向AGI级训练（万亿参数模型）
- **Nova模型家族**：自研LLM，对标GPT-5/Gemini，2025年发布Nova Pro/Ultra
- **Graviton5**：ARM服务器CPU，2026年，数据中心能效比提升30%
- **Project Kuiper**：卫星互联网，对标Starlink，2026年商用，低延迟边缘AI推理节点


## 融资与现金流

- 详见财务状况章节
## 研发投入与专利

| 指标 | FY2023 | FY2024 | FY2025 |
|------|--------|--------|--------|
| R&D($B) | 73 | 82 | 90 |
| R&D占营收 | 12.7% | 12.9% | 12.9% |
| CapEx($B) | 53 | 68 | 85 |

- 全球专利组合超过**30,000项**（含AWS云计算+AI芯片+仓储机器人+卫星通信）
- **核心技术壁垒**：Trainium/Inferentia自研芯片降低对外部GPU依赖；AWS全球105个可用区+32个区域网络基础设施；Anthropic独家合作+自研Nova双轨AI策略；全球最大电商物流网络的AI优化数据飞轮
- AI/ML领域专利超过**8,000项**，集中在分布式训练架构、模型压缩推理、AI芯片互联拓扑

