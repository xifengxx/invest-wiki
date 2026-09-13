---
name: Groq
slug: groq
country: US
type: company
updated: 2026-09
data_freshness_date: 2026-09-13
segments:
- ASIC/AI定制芯片
- AI推理API服务
one_liner: |
  AI推理云服务商（原LPU推理芯片公司），核心为按token计费的AI推理服务与13个数据中心算力，通过推理服务销售实现盈利，位于AI算力L4应用与服务层——2025年底LPU技术被NVIDIA以约$200亿非独家授权，公司随之从芯片商转型为运行NVIDIA系统的推理"neocloud"。
  【2026.9.13更新】2025-12-24 NVIDIA以约$200亿非独家授权Groq的LPU技术并聘用其创始人Jonathan Ross及多数高管团队；Groq转型为AI推理neocloud，2026-08-17以$35亿估值募资$3.5亿（约为2025年9月$69亿估值的一半）；运营13个数据中心、服务500-600万开发者，收入未披露。
chain_layer: L4
chain_role: 直接相关
suppliers:
- company: NVIDIA
  ticker: NVDA
  supplies: AI 推理系统（Groq 转型后运行NVIDIA系统）
  note: 同时是LPU技术被授权方与生态伙伴
- company: 三星
  ticker: 005930.KS
  supplies: Groq 芯片制造（Groq 3 LPX 机架用）
- company: 数据中心建设与电力供应商
  supplies: IDC 与电力容量
customers:
- company: AI 开发者
  note: 500-600万开发者
- company: Fortune 500 企业
  note: 企业级推理需求
- company: AI 原生公司
  note: 推理API客户
- company: Nebius
  ticker: NBIS
  note: 确认部署 Groq 3 LPX 机架的云厂商
partners:
- company: NVIDIA
  ticker: NVDA
  area: LPU技术授权 + Groq 3 LPX 平台
  note: 2025-12-24 非独家授权（约$200亿）；Groq仍为NVIDIA Cloud Partner
- company: Disruptive
  area: 各轮领投方
  note: 其创始人 Alex Davis 任 Groq 董事会主席
- company: Nebius
  ticker: NBIS
  area: Groq 3 LPX 机架部署
competitors:
- company: NVIDIA
  ticker: NVDA
  area: AI 推理硬件与云
  note: 既是授权方又是平台方
- company: Cerebras
  area: 专用推理芯片
  note: OpenAI 的推理芯片合作方
- company: SambaNova
  area: AI 推理系统
- company: Fireworks AI / Together AI
  area: AI 推理云
core_business:
- AI 推理服务（按 token 计费，转型后核心业务）
- 13个数据中心算力（北美/欧洲/中东/亚太）
- Groq 3 LPX 推理平台（与NVIDIA合作，2026-08-24量产）
- 原 LPU 技术（已于2025年12月非独家授权给NVIDIA）
revenue_model: 转型后以**按token计费的AI推理服务**为主（neocloud模式），运行NVIDIA系统。**收入数据未披露**——所有搜索来源均无收入、付费客户规模、数据中心利用率或盈利能力的公开数字。公司行为特征显示高资本投入（目标2027年容量从54MW扩至200+MW）。
founded: 2016
headquarters: 美国加州山景城
latest_revenue: 未披露
market_cap: ~$35亿（2026-08-17 融资估值）；2025-09 曾达 $69亿
description: Groq 2016年成立，由前Google TPU工程师Jonathan Ross创立，开发LPU（Language Processing Unit）专用推理芯片。2025年12月24日，NVIDIA以约$200亿非独家授权其LPU技术，并聘用Ross及多数高管团队（被称"not-acqui-hire"）。Groq随之从芯片公司转型为AI推理"neocloud"，运行NVIDIA系统并按token销售推理服务，目前运营13个数据中心，服务500-600万开发者。
website: https://groq.com
industries:
- AI算力
---

# Groq

一家被"掏空"后又重新定义自己的公司。NVIDIA 用 $200 亿拿走了 LPU 技术授权与整个创始团队，Groq 只剩品牌与运营——估值从 $69 亿腰斩至 $35 亿是理性的。现在它是一家运行 NVIDIA 系统、按 token 卖推理的 neocloud。

## 财务状况

Groq 为**未上市公司**，采用「融资估值」口径。**收入数据完全未披露**。

### 2026 年融资

| 时间 | 金额 | 估值 | 领投 |
|------|------|------|------|
| 2026-06-22 | **$6.5亿** | 未披露 | Disruptive、Infinitum |
| **2026-08-17** | **$3.5亿**（称Series A） | **$35亿** | Disruptive；NVIDIA"计划参与" |

**关键对比**：$35亿估值约为 **2025年9月 $69亿投后估值的一半**。
- Groq 表示**不视为 down round**，而是**授权协议后公司的重新估值**
- 2026两轮合计约 **$10亿**；**公开股权融资总额超 $27.5亿**

#### 财务特征

**估值腰斩的原因清晰**：公司在2025年12月失去了两样核心资产——**LPU技术的独占性**（非独家授权给NVIDIA）与**创始团队**（CEO及多数高管被NVIDIA聘用）。剩下的是一家运营NVIDIA系统的推理云服务商。

## 核心事件：NVIDIA 授权协议（2025-12-24）

| 项 | 内容 |
|----|------|
| 性质 | **非独家技术授权**——**不是收购** |
| 金额 | 报道约 **$200亿** |
| **关键条款** | **NVIDIA 聘用了创始人/CEO Jonathan Ross（前Google TPU工程师）、总裁 Sunny Madra 及大部分高管团队** |
| 定性 | 被描述为 "**not-acqui-hire**"（非收购式挖角） |
| 后续 | NVIDIA 推出 **LPX / NVIDIA Groq 3 LPX 推理平台**（2026-03 GTC）；**机架于2026-08-24全面量产**，计划年底前在 **Nebius** 部署 |
| 技术规格 | 每个液冷机架搭载 **256颗Groq芯片（三星制造）**；NVIDIA 称 **3,400 tokens/秒**（对比 OpenAI 为其 Cerebras 模式承诺的 750 tokens/秒），**每兆瓦吞吐量最高35倍** |
| 部署 | **Nebius 是唯一确认部署该机架的云厂商** |

## 产品线详解

### AI 推理服务（转型后核心）
**按token计费**的推理服务，运行NVIDIA系统。运营 **13个数据中心**（北美/欧洲/中东/亚太），服务 **500-600万开发者** + Fortune 500 + AI原生公司，**每周处理数万亿 AI tokens**。

### Groq 3 LPX 推理平台
与NVIDIA合作的产品线，2026年8月24日全面量产。NVIDIA 将其定位为对标超低延迟推理场景的方案。

### 原 LPU 技术
已于2025年12月**非独家授权**给NVIDIA——Groq 不再拥有独家差异化。

## 技术路线图

| 方向 | 状态 | 时间 |
|------|------|------|
| **容量扩张** | 从 **54MW 扩至 200+MW** | 2027 |
| **Groq 3 LPX 机架** | 2026-08-24 全面量产，Nebius 部署 | 2026 |
| 数据中心网络 | 13个（北美/欧洲/中东/亚太） | 2026 |
| 生态位 | 仍为 **NVIDIA Cloud Partner** | 2026+ |

## 融资与现金流

- 2026年两轮合计约 **$10亿**（$6.5亿 + $3.5亿）
- 公开股权融资总额超 **$27.5亿**
- 估值从2025年9月的$69亿降至2026年8月的 **$35亿**
- **NVIDIA"计划参与"**$3.5亿轮（部分报道称仍待交割）
- 高资本投入：容量从54MW扩至200+MW需要巨额数据中心投资

## 研发投入与专利

- 核心壁垒（**已被大幅削弱**）：
  1. ~~LPU 推理芯片的技术领先~~ ——**已于2025年12月非独家授权给NVIDIA**
  2. ~~创始团队与核心研发人才~~ ——**Jonathan Ross 及多数高管已被NVIDIA聘用**
  3. **剩余资产**：13个数据中心的运营能力、500-600万开发者关系、NVIDIA Cloud Partner 身份
  4. **NVIDIA 生态的深度绑定**（客户+供应商+股东三重关系）
- **主要风险**：
  1. **技术差异化已丧失**——LPU 不再独家，公司只是运行NVIDIA系统的服务商
  2. **收入完全不透明**——无公开收入、客户或盈利数据
  3. **估值腰斩**（$69亿→$35亿），且管理层称"不是down round"的解释缺乏说服力
  4. **CEO 身份报道不一致**（Simon Edwards / Doug Wightman / Adam Winter）——治理信息混乱
  5. 董事会主席 Alex Davis 的 Disruptive 同时是各轮领投方——**关联交易与治理风险**
  6. neocloud 赛道竞争激烈（CoreWeave、Nebius 等规模更大）

## 动态更新记录

### 2026-09-13（骨架词条升级）
> 来源: [[消化笔记/2026-09-13-骨架公司补全批次]]
> L0归档: `L0-原始资料池/03-新闻/2026-09-13-Groq-融资与转型调研.md` (input_20260913_051)
> 置信度: 中（未上市；收入数据未披露）

- **词条升级**：从骨架升级为完整词条，补齐 YAML 字段 + 6 个 Body 段
- **chain_role 调整**：`龙头` → `直接相关`（**技术与团队已流失，不再是推理芯片龙头**）
- **market_cap**：空 → ~$35亿（2026-08-17）；2025-09 曾达$69亿
- **latest_revenue**：空 → **未披露**
- **suppliers/customers/partners/competitors**：空数组 → 分别填充 3/4/3/4 条
- **重大事件**：**2025-12-24 NVIDIA以约$200亿非独家授权LPU技术并聘用创始人及多数高管**；公司转型为AI推理neocloud
- **新增风险标注**：技术差异化丧失、收入不透明、估值腰斩、CEO身份报道不一致、董事会主席与领投方关联
