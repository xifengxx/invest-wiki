---
name: Together AI
slug: together-ai
country: US
ticker: TOGETHER   # 未上市；用公司专属非交易键，勿填估值当市值
type: company
updated: 2026-09
data_freshness_date: 2026-09-15
segments:
- AI推理API服务
one_liner: |
  美国AI原生云与开源模型推理平台，核心是开源及定制大模型推理、微调、训练和GPU集群服务，通过按token/API调用与算力服务收费，位于AI算力L4应用与平台层。2026年7月完成$800M Series C，投后估值$8.3B，Aramco Ventures领投；公告称上一季度年化订单额超过$1.15B。
chain_layer: L4
chain_role: 核心参与者
suppliers:
- company: NVIDIA
  ticker: NVDA
  supplies: AI GPU与数据中心计算平台
  note: NVIDIA参与本轮融资，是算力生态合作方
- company: 云数据中心与电力供应商
  supplies: GPU集群机房、电力与网络
  note: 公司计划未来五年把基础设施产能扩大约50倍
customers:
- company: Cursor
  note: AI编程应用客户，使用推理服务
- company: Cognition
  note: AI Agent与编程工具客户
- company: Decagon
  note: 客服Agent客户
- company: 数千家付费开发者与企业
  note: 官方口径为数千付费客户；服务超百万开发者不等于付费客户数
partners:
- company: Aramco Ventures
  area: Series C领投与战略资源
- company: NVIDIA
  ticker: NVDA
  area: 算力生态与参投
- company: 开源模型社区
  area: 开源模型部署、微调与推理优化
competitors:
- company: Fireworks AI
  ticker: FIREWORKS
  area: 开源模型推理平台
- company: Groq
  ticker: GROQ
  area: 低延迟推理专用云
- company: OpenAI
  note: 闭源模型API与开发者生态
- company: Anthropic
  area: 前沿模型API
- company: AWS / Azure / Google Cloud
  area: 云厂商托管推理服务
core_business:
- 开源模型推理API与快速推理优化
- 模型微调、定制训练与强化学习服务
- GPU集群与AI原生云基础设施
- 企业级模型部署、评测与效率研究
- 面向Agent、编程、客服等场景的托管推理
revenue_model: 收入主要来自按token/API调用计费的推理服务、微调与训练项目以及GPU算力服务。融资公告披露“上一季度年化订单额超过$1.15B”，该口径为bookings，不是已确认收入，需与GAAP营收区分。
founded: 2022
headquarters: 美国旧金山
employees: 未披露
latest_revenue: 未披露GAAP营收；2026年7月公告上一季度年化订单额>$1.15B
market_cap: 未上市；Series C投后估值$8.3B（2026.7）
description: |
  Together AI成立于2022年，定位“AI Native Cloud”，围绕开源与定制模型提供推理、微调、训练、GPU集群和效率研究服务。2026年7月，公司宣布完成$800M Series C，投后估值$8.3B，由Aramco Ventures领投，Vista Equity Partners、General Catalyst、NVIDIA、March Capital等参投。公告称其上一季度年化订单额超过$1.15B，客户包括Cursor、Cognition、Decagon等。公司还计划未来五年将基础设施产能扩大约50倍。
website: https://www.together.ai
industries:
- AI算力
---

# Together AI

Together AI把开源模型、推理优化和GPU云打包成一条开发路径：企业不必自己维护复杂推理栈，就能获得更低成本的token和可扩展算力。它的商业化证据是年化订单额，而不是已确认收入，判断时应区分这两个口径。

## 财务状况

公司未披露完整GAAP财务报表，当前最有信息量的经营指标来自2026年7月融资公告。

| 指标 | 数值 | 口径说明 |
|------|------|----------|
| Series C | $800M | 2026年7月宣布 |
| 投后估值 | $8.3B | 融资轮估值，非二级市场市值 |
| 领投方 | Aramco Ventures | Vista、General Catalyst、NVIDIA等参投 |
| 上一季度年化订单额 | >$1.15B | annual bookings，非已确认收入 |
| 客户类型 | Cursor、Cognition、Decagon等 | 官方列示的代表性客户 |
| 产能计划 | 未来五年约扩大50倍 | 计划目标，非已实现产能 |

## 产品与服务

- **推理API**：托管开源与定制模型，按token或调用计费，强调延迟、吞吐和单位成本。
- **微调与训练**：支持模型定制、偏好优化和强化学习工作流，服务企业自有数据与场景。
- **GPU集群**：为训练、微调和高并发推理提供集群资源，属于AI原生云基础设施。
- **效率研究**：围绕推理优化、量化、批处理和集群调度降低成本，官方称客户推理成本相对闭源模型可低6倍至60倍；该数字是宣传口径，实际节省取决于模型、负载与优化方式。

## 竞争定位

Together AI处在开源推理平台的增长带上：过去十二个月开源模型使用量增长约3倍，Agent、编程工具和客服场景又带来高频调用需求。与三大云厂商相比，它的优势是更专注的推理优化和模型工程服务；与Fireworks、Groq相比，三家路线不同，但都在争夺“高吞吐、低成本、易迁移”的开源推理市场。

风险也很直接：底层模型厂商可以通过价格战和专属API吸引开发者，云厂商可以复制托管推理能力，GPU供给与电力成本也会压缩利润。Together的年化订单额如果能转化成可持续GAAP收入，并证明推理优化能带来正毛利，商业模式才更稳。

## 融资与现金流

2026年7月的$800M Series C为其扩产提供资金支持，领投方Aramco Ventures也把中东资本和中东算力需求连接进来。NVIDIA、SentinelOne旗下S Ventures、Pegatron等生态投资方的参与，有助于GPU供应、端侧与企业安全生态协同。公司计划未来五年基础设施产能扩大约50倍，这意味着资本开支、GPU交付、电力合同和客户订单都需要同步扩张；在订单转化和现金流披露不足前，扩张速度本身不应直接等同于盈利能力。

## 动态更新记录

### 2026-09-15：薄档升级为全面档
- **来源**：`L0-原始资料池/03-新闻/2026-09-15-F4批次-AI算力与模拟组5家-数据溯源.md`（input_20260915_135）
- **核心更新**：补齐估值、融资、bookings、客户、产能计划和竞争格局。
- **关键区分**：annual bookings不是GAAP收入；$8.3B是投后估值，不是市值。

