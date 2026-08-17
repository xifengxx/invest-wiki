---
name: GPU
slug: gpu
industry: AI算力
layer: L3
tam_bn: 130.0
cagr_pct: 40.0
margin: 65-75%
cost_share_pct: 55
cost_share_context: AI服务器
profit_pool_pct: 65
profit_pool_context: AI服务器利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: NVIDIA
    share: 86%
    note: 数据中心AI GPU绝对垄断，FY2026 GPU计算$162.4B，Blackwell 2.97M颗
  - name: AMD
    share: 8%
    note: MI300X $6-8B→MI350/MI400追赶，ROCm生态差距仍大
  - name: Intel
    share: <2%
    note: Gaudi/Habana→Falcon Shores基本退出AI GPU
  china:
  - name: 华为昇腾
    share: '-'
    note: Ascend 910B国产替代首选，特定场景有应用
  - name: 寒武纪
    share: '-'
    note: 688256思元MLU云端推理
  - name: 海光信息
    share: '-'
    note: 688041深算DCU，ROCm兼容
  - name: 壁仞科技
    share: '-'
    note: BR100 7nm未上市
  - name: 摩尔线程
    share: '-'
    note: MTT S系列未上市
  - name: 天数智芯
    share: '-'
    note: 天垓100未上市
  barriers:
  - item: CUDA生态锁定
    detail: 90%+AI框架基于CUDA，软件成熟度93%利用率vs AMD 45%
  - item: 架构迭代+全栈整合
    detail: GPU+NVLink+InfiniBand+CUDA形成完整护城河
  - item: 制程+HBM供应
    detail: 先进制程和HBM产能受限，NVIDIA凭借规模优势优先获得产能
  tech_gap:
  - dimension: 中国GPU硬件差距约3-5年，软件生态差距>5年。NVIDIA加速迭代后差距扩大。AMD MI400+ROCm开源可能成为第二选择
    detail: ''
key_trends:
- title: NVIDIA FY2026数据中心$193.7B(+68% YoY)，Blackwell占88%，Vera Rubin平台进入全面量产
  detail: 从H100到B200性能2x训练+30x推理吞吐(GB200)，迭代加速到1年
- title: 推理市场增速(60%+)超过训练(30%+)，FP4精度让单卡跑4个70B模型
  detail: NVIDIA Rubin架构2.3kW TDP/22.2TB/s带宽/40%能效提升
- title: AMD MI400+Helios平台2026年挑战
  detail: OpenAI 6GW多年度部署，目标推理20%份额，但软件利用率45% vs NVIDIA 93%
- title: 定制ASIC(Google TPU/AWS Trainium/微软Maia)成结构性威胁
  detail: 云厂商自研芯片占比提升，但CUDA生态短期不可替代
- title: 中国GPU在特定场景突破
  detail: 昇腾910B在政府/运营商AI训练有窗口期，但美国制裁持续限制先进制程获取
- title: AI芯片高集中度系统性风险
  detail: 前三大占全球芯片市值80%，AI芯片贡献50%收入但产量<0.2%，若AI CapEx回调链式反应从GPU→CoWoS→HBM→设备→材料
price_conduction:
- NVIDIA每代GPU涨价30-50%（H100 $30K→B200 $40K+）
- AI服务器ASP持续上涨
- 云厂商TCO上升。但云厂商转嫁能力较强（AI服务按Token/小时定价可灵活调价）
- 最终成本部分由AI应用开发者和终端用户承担。GPU涨价加速云厂商自研芯片（Google TPU/AWS Trainium）和ASIC替代趋势
wikilinks:
- FPGA
- AI服务器
- HBM高带宽内存
- 先进封装CoWoS
- ASIC/AI定制芯片
key_inputs:
- HBM高带宽内存
- 先进封装CoWoS
key_customers:
- AI服务器
sources:
- title: NVIDIA FY2026 Annual Report
  summary: ''
  url: https://investor.nvidia.com
- title: IFP.org Blackwell Revenue Analysis 2025
  summary: ''
  url: https://ifp.org/should-the-US-sell-blackwell-chips-to-china.pdf
- title: Visual Capitalist AI Data Center Revenue 2021-2025
  summary: ''
  url: https://www.visualcapitalist.com/charted-the-battle-for-ai-data-center-revenue-2021-2025/
- title: Jon Peddie Research GPU Market Share Q3 2025
  summary: ''
  url: https://www.jonpeddie.com
- title: Silicon Analysts AMD vs NVIDIA AI GPU 2026
  summary: ''
  url: https://siliconanalysts.com/analysis/amd-vs-nvidia-ai-gpu-market-share-2026
- title: Moor Insights NVIDIA Competitive Position 2025
  summary: ''
  url: https://moorinsightsstrategy.com
companies:
- ticker: NVDA
  name: NVIDIA
  role: 全球龙头
  rev: 95
- ticker: AMD
  name: AMD
  role: 全球二线
  rev: 35
- ticker: INTC
  name: Intel
  role: 全球二线
  rev: 5
---

# GPU

> **AI算力** · L3 · TAM **$130B** · CAGR **40%**

GPU因数千核心并行计算架构天然适合AI矩阵运算，成为深度学习训练和推理的**主力芯片**。FY2026 NVIDIA数据中心营收$193.7B(占总额89.7%)，其中GPU计算$162.4B，网络$31.4B。|**Blackwell占FY2026计算收入88%**（2.97M颗，均价$45,796），H100降至12%。NVIDIA从2年迭代加速到1年（Hopper→Blackwell→Rubin→Vera）。|**CUDA生态锁定90%+AI开发者**——工具链+模型库+优化算子形成强大网络效应。推理市场(增速60%+)超过训练(30%+)成为新增长极。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $130B |
| 年复合增长率(CAGR) | 40% |
| 利润率区间 | 65-75% |
| 成本占比 | 55% (AI服务器) |
| 利润池占比 | 65% (AI服务器利润池) |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22
> 来源: 消化笔记/2026-07-22-v1.1-中原证券电子行业中期策略, 消化笔记/2026-07-22-v1.1-德勤全球半导体趋势
> 置信度: 高

- **key_trends**: 趋势#1更新——Vera Rubin平台进入全面量产
- **sources**: +2 中原证券2026中期策略 + 德勤2026全球半导体趋势
- **依据**: 中原证券——英伟达Vera Rubin平台已进入全面量产阶段；德勤——2026年AI芯片$5,000亿，GPU作为核心品类受益

### 更新 2026-07-22 (v1.1)
> 来源: 消化笔记/2026-07-22-v1.1-德勤全球半导体趋势
> 置信度: 高

- **contradictions**: 新增矛盾——AI芯片高集中度风险（前三大占市值80%）
- **key_trends**: +1条 "AI芯片高集中度系统性风险"
- **依据**: 德勤v1.1完整QA——前三大芯片公司占全球市值80%，行业"所有鸡蛋放AI篮子"
