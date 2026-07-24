---
name: Cerebras Systems
slug: cerebras
country: US
ticker: CBRS
type: company
updated: 2026-07
data_freshness_date: 2026-07-23
segments:
- ASIC/AI定制芯片
- AI芯片设计(Fabless)
- AI模型训练平台
one_liner: 全球唯一晶圆级AI芯片（WSE-3，整片300mm晶圆=单芯片，4万亿晶体管/900K核/125 PFLOPS）设计商，推理速度比GPU快15-20x，2026年5月Nasdaq IPO募资$5.5B，OpenAI 750MW推理合同（$10B+），AWS Bedrock部署，积压订单$24.6B，市值~$50B。
chain_layer: L3
chain_role: 核心参与者
suppliers:
- company: 台积电
  ticker: TSM
  supplies: 5nm晶圆级芯片制造
  note: 无长期供应协议（关键风险点）
customers:
- company: OpenAI
  revenue_pct: 50
  note: 750MW→2GW推理合同，$10-20B+，$1B数据中心贷款
- company: AWS
  ticker: AMZN
  revenue_pct: 10
  note: Bedrock推理部署，Trainium+CS-3混合架构
- company: G42/MBZUAI
  revenue_pct: 24
  note: 历史最大客户（2023-2024 85-97%），2025年降至24%
partners:
- company: AWS
  ticker: AMZN
  area: 云端推理部署
  note: Amazon Bedrock集成CS-3
- company: OpenAI
  area: AI推理基础设施
  note: 最大客户+$1B贷款+750MW合同
competitors:
- company: NVIDIA
  ticker: NVDA
  area: AI训练/推理GPU
  note: 70-80% AI芯片市场份额，CUDA生态壁垒
- company: AMD
  ticker: AMD
  area: AI GPU
  note: MI300X/350系列
- company: Google TPU/Broadcom ASIC
  area: 定制AI芯片
  note: 超大规模自研替代
core_business:
- 晶圆级AI推理芯片WSE-3设计（4T晶体管/900K核/125 PFLOPS/44GB SRAM/21 PB/s带宽，TSMC 5nm）
- CS-3系统销售（硬件收入~$358M FY2025）
- AI推理云服务（云收入~$152M FY2025，+167% YoY）
- 软件生态（AWS Marketplace/Microsoft Marketplace/IBM watsonx/Hugging Face/OpenRouter集成）
revenue_model: FY2025营收$510M（+76% YoY from $290M），GAAP净利润$238M（47%净利率），但GAAP运营亏损$146M（一次性非现金+股权激励后）。Q1 2026 $193.4M（+94% YoY）。硬件$358M + 云$152M（云+167% YoY）。Q1 2026调整后毛利率47%，Q2指引36-38%（权证稀释+数据中心投入）。RPO积压$24.6B提供多年收入可见性。IPO（2026.5.14）募资$5.5B（$185/股，超20倍认购），开盘$350，市值峰值~$95B。
founded: 2016
headquarters: 美国加州Sunnyvale
employees: ~800
latest_revenue: TTM ~$604M（FY2025 $510M + Q1 2026 $193.4M）
market_cap: ~$50B（2026.7，较IPO高点跌~47%）
description: Cerebras Systems是全球唯一实现晶圆级AI芯片（Wafer-Scale Engine）商业化的公司，2016年成立于加州Sunnyvale。其旗舰产品WSE-3将整片300mm硅晶圆作为单一巨型芯片（46,225 mm²，比NVIDIA B200大58倍），集成4万亿晶体管和900,000个AI优化核心，实现125 PFLOPS算力和21 PB/s内存带宽。在AI推理方面，第三方基准测试显示Llama 3.1 70B达到2,100 tokens/s——比主流GPU方案快12-18倍。2026年5月Nasdaq IPO（$185/股，募资$5.5B，开盘$350，市值~$95B）后回落至~$50B。最大客户OpenAI（750MW推理合同可扩展至2GW，合同价值$10-20B+）和AWS（Bedrock集成）提供关键需求锚定。核心风险：客户高度集中（OpenAI主导）、毛利率受权证+数据中心通过成本压缩（36-38%）、TSMC无长期供应协议、NVIDIA CUDA生态碾压。
website: https://www.cerebras.net
industry: AI算力
---

# Cerebras Systems

全球唯一晶圆级AI芯片（Wafer-Scale Engine），整片300mm晶圆=单芯片，推理比GPU快15-20x，2026.5 IPO $5.5B，OpenAI $10B+推理合同，积压$24.6B，但客户集中+毛利率压缩+TSMC供应风险三重挑战。

## 财务状况

| 指标 | FY2024 | FY2025 | Q1 2026 |
|------|--------|--------|---------|
| **营收** | $290M | **$510M** | $193.4M |
| **YoY增长** | — | +76% | **+94%** |
| **硬件收入** | — | $358M | — |
| **云服务收入** | — | $152M | +167% |
| **GAAP净利润** | — | $238M（47%净利率） | -$0.04/股 |
| **调整后毛利率** | — | — | 47%→Q2指引36-38% |
| **RPO积压** | — | — | **$24.6B** |

## WSE-3 vs GPU

| 维度 | Cerebras WSE-3 | NVIDIA B200 |
|------|:--:|:--:|
| **芯片面积** | 46,225 mm²（整片晶圆） | ~800 mm² |
| **晶体管** | 4万亿 | 2080亿 |
| **核心数** | 900,000 AI优化核 | 20,480 CUDA核 |
| **算力** | 125 PFLOPS | 18 PFLOPS (FP4) |
| **片上SRAM** | 44 GB | — |
| **内存带宽** | 21 PB/s | 8 TB/s (HBM3e) |
| **Llama 3.1 70B推理** | 2,100 tok/s | ~120-170 tok/s |


## 融资与现金流

- 近期融资: 5.5B
## 投资风险

- **客户集中度极高**：OpenAI（~50%）+ G42（24%）= ~74%，任一客户流失即为灾难
- **毛利率被压缩**：权证（OpenAI/G42稀释）+数据中心通过成本→Q2仅36-38%
- **TSMC无长期协议**：5nm晶圆级芯片制造无LT供应保障
- **IPO后腰斩**：开盘$350→当前约$150-200（跌47-57%），估值从$95B→$50B
