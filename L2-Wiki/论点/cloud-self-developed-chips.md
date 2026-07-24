---
name: "云厂商自研芯片从'补充'走向'替代'，2028年占AI推理>30%"
slug: "cloud-self-developed-chips"
type: "thesis"
thesis_status: "forming"
confidence: 6
created: "2026-07-20"
updated: "2026-07-20"
affected_segments: ["cloud-iaas", "asic-ai-chip", "gpu", "ai-inference-api"]
affected_companies: ["GOOGL", "AMZN", "MSFT", "NVDA"]
tags: ["cloud", "asic", "gpu", "inference"]
---

# 云厂商自研芯片从"补充"走向"替代"，2028年占AI推理份额>30%

## 核心主张

AWS Trainium/Microsoft Maia/Google TPU三路并进，从内部推理工作负载切入，逐步替代NVIDIA GPU在推理侧的份额。云厂商TCO优化诉求+定制化性能优势+不受制于NVIDIA供应的战略需求三重驱动。

## 支撑证据

1. 定制ASIC成结构性威胁——云厂商自研芯片占比提升
   ——来源: GPU赛道
   (L2-Wiki/赛道/AI算力/gpu.md)
2. Google TPU v5p推理能效优势
   ——来源: ASIC赛道
   (L2-Wiki/赛道/AI算力/asic-ai-chip.md)
3. GPU涨价加速云厂商自研芯片动机
   ——来源: GPU赛道
   (L2-Wiki/赛道/AI算力/gpu.md)

## 反对证据

1. NVIDIA CUDA生态锁定+全栈整合护城河
   ——来源: GPU赛道
   (L2-Wiki/赛道/AI算力/gpu.md)
2. ASIC开发成本$500M+，仅头部云厂商可承担
   ——来源: ASIC赛道
   (L2-Wiki/赛道/AI算力/asic-ai-chip.md)
3. ASIC灵活性差，不适合快速变化的模型架构
   ——来源: Wiki内部数据

## 待验证假设

- 假设1：如果2027年Amazon/Google/Microsoft AI推理工作负载中自研芯片占比超过50%，则NVIDIA推理收入承压
- 假设2：如果NVIDIA降价应对ASIC竞争，可能减缓自研芯片推进速度

## 关联赛道

- [[云计算IaaS]]
- [[ASIC/AI定制芯片]]
- [[GPU]]
- [[AI推理API服务]]

## 更新日志

- 2026-07-20: 论点创建，置信度6/10

## 来源

- GPU赛道
  NVIDIA CUDA生态锁定90%+AI开发者，GPU价格持续上涨加剧云厂商TCO优化和自研紧迫性
  (L2-Wiki/赛道/AI算力/gpu.md)
- ASIC赛道
  Google TPU v5p推理能效比GPU高2-3x，AWS Trainium/Microsoft Maia三路并进，开发成本$500M+仅头部云厂商可承担
  (L2-Wiki/赛道/AI算力/asic-ai-chip.md)
