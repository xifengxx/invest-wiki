---
name: Fireworks AI
slug: fireworks-ai
country: US
ticker: FIREWORKS   # 未上市；用公司专属非交易键，勿填估值当市值
type: company
updated: 2026-09
data_freshness_date: 2026-09-15
industries:
- AI算力
segments:
- AI推理API服务
one_liner: |
  美国AI推理与特化模型平台，提供开源及企业专属模型的高吞吐推理、微调与训练服务，位于AI算力L4应用与平台层。2026-07完成$1.505B Series D，投后估值$17.5B；公告称年化收入run rate超$1B、日处理超40万亿token。
chain_layer: L4
chain_role: 核心参与者
suppliers:
- company: NVIDIA
  ticker: NVDA
  supplies: AI GPU与推理基础设施
  note: NVIDIA参与Series D，双方在推理生态协同
- company: 云数据中心与基础设施供应商
  supplies: GPU集群、电力与网络
customers:
- company: Cursor
  note: AI编程应用，训练专用代码模型
- company: Harvey
  note: 法律AI应用，构建专用智能
- company: Samsung
  note: 企业级特化模型场景客户
- company: GitLab
  note: 开发者工作流与AI功能客户
- company: 企业客户
  note: 使用开源模型微调、专有数据特化与托管推理
partners:
- company: Atreides Management
  area: Series D领投
- company: Index Ventures
  area: Series D领投
- company: TCV
  area: Series D领投
- company: NVIDIA
  ticker: NVDA
  area: Series D参投与推理算力生态
- company: Microsoft Foundry
  area: 官方博客披露Fireworks接入Microsoft Foundry提供开源模型推理
competitors:
- company: Together AI
  ticker: TOGETHER
  area: 开源模型推理、微调与AI原生云
- company: Groq
  ticker: GROQ
  area: 低延迟专用推理云
- company: OpenAI / Anthropic
  area: 前沿闭源模型API
- company: AWS / Azure / Google Cloud
  area: 云厂商托管推理与企业AI平台
core_business:
- 高吞吐开源与定制模型推理API
- 企业专有数据模型特化、微调与训练
- 推理优化、量化、批处理与集群调度
- Training API与企业级模型托管
- Agent、代码、法律、搜索和RAG等场景模型服务
revenue_model: 收入主要来自按token/API调用计费的推理服务、模型微调与训练订阅。2026-07公告口径为年化收入run rate超$1B；该指标强调年化速度，不等同于经审计GAAP收入或净利润。
founded: 2022
headquarters: 美国旧金山
employees: 未披露
latest_revenue: 年化收入run rate超$1B（2026-07公司公告口径）
market_cap: 未上市；Series D投后估值$17.5B（2026.7）
description: |
  Fireworks AI由前Meta PyTorch团队相关人才创办，CEO为Lin Qiao，定位是把通用开源模型改造成企业可拥有的“specialized intelligence”。2026-07-15，公司宣布完成$1.505B Series D，投后估值$17.5B，Atreides Management、Index Ventures和TCV领投，NVIDIA、Lightspeed、Bessemer、Menlo等参投。官方称当时年化收入run rate超过$1B，每日处理超40万亿token，其中超过95%来自使用客户专有数据特化的模型。
website: https://fireworks.ai
---

# Fireworks AI

Fireworks AI的商业命题是“企业不要只租通用智能，而要拥有围绕自己数据训练的专属智能”。它把开源模型、推理优化、微调和Training API组合起来，让模型能力绑定在企业工作流和专有数据上，从而提高迁移成本。

## 财务状况与融资

公司未披露完整GAAP报表，最新公开经营指标来自2026-07-15融资公告。

| 指标 | 数值 | 口径说明 |
|------|------|----------|
| Series D | **$1.505B** | 2026-07-15宣布 |
| 投后估值 | **$17.5B** | 私募轮估值，非二级市场市值 |
| 领投方 | Atreides Management、Index Ventures、TCV | Evantic、Lightspeed、NVIDIA、20VC、Bessemer、Menlo等参投 |
| 年化收入run rate | >$1B | annualized revenue run rate，非经审计GAAP收入 |
| 日处理token | >40万亿 | 公司公告运营口径 |
| 专有数据特化模型token占比 | >95% | 公司公告口径，反映工作负载结构 |
| Training API | 2026-08-31 GA | 官方相关更新 |

$1B ARR说明商业化速度很快，但AI推理平台的核心不是把模型调起来，而是在客户模型、吞吐、延迟、成本和稳定性之间持续保持帕累托优势。后续要看ARR的留存率、推理毛利率、GPU采购节奏和Training API能否带来更高的客单价。

## 产品与技术路线

- **托管推理**：对开源与定制模型提供高吞吐、低延迟API，按token/调用计费。
- **模型特化**：使用企业客户关系、工作流、文档和专有数据微调模型，让输出贴合业务规则。
- **Training API**：2026-08-31正式GA，把训练、评测和部署从项目服务推进到可自动化平台能力。
- **推理优化**：通过量化、批处理、调度和专用运行时提升单位GPU产出，这是和通用云竞争的关键。
- **场景落地**：Cursor的代码模型、Harvey的法律AI、GitLab的开发者工作流和Samsung的企业场景构成参考客户群。

## 竞争定位

Fireworks与Together AI最接近，都在争夺开源模型推理和企业定制训练；与Groq相比，Fireworks更侧重模型工程和专用数据，而不是单一路径的低延迟硬件；与OpenAI、Anthropic相比，它让企业拥有特化模型而非完全依赖闭源API；与三大云相比，它的优势是更新快、优化更深、客户专属模型更容易绑定。风险是云厂商复制托管能力、开源模型快速演进导致技术溢价缩短，以及NVIDIA/GPU供给的价格波动。

## 客户与生态

NVIDIA参与D轮并保持算力生态协同；Microsoft Foundry接入Fireworks，说明开源模型推理能力已被主流云平台吸纳，这既是渠道，也带来合作与竞争边界。Cursor、Harvey、Samsung、GitLab覆盖编程、法律、企业运营和开发者工具，客户类型分散，比单一AI应用客户更能验证平台化需求。

## 动态更新记录

### 2026-09-15：薄档升级为全面档
- **来源**：Fireworks官方2026-07-15 Series D公告和Training API GA更新，归档于`L0-原始资料池/03-新闻/2026-09-15-F5批次-AI云与模拟组4家-数据溯源.md`（input_20260915_136）。
- **核心更新**：补齐$17.5B投后估值、$1B ARR、日token量、专有模型占比、领投方、客户与Training API进展。
- **关键区分**：ARR是年化收入run rate，不是经审计GAAP收入；$17.5B是私募估值，不是市值。
