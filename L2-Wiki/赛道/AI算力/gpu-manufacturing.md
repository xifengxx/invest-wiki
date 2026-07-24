---
name: GPU制造代工
slug: gpu-manufacturing
industry: AI算力
layer: L3
tam_bn: 55.0
cagr_pct: 30.0
margin: 40-55%
cost_share_pct: 30
cost_share_context: GPU价值
profit_pool_pct: 20
profit_pool_context: GPU利润池
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: TSMC
    share: '>95%'
    note: 4nm/3nm制造所有NVIDIA/AMD/Intel GPU，2nm 2025H2量产
  - name: 三星
    share: <5%
    note: 2nm GAA良率爬坡中，落后TSMC 12-18个月, Intel Foundry
  china:
  - name: SMIC
    share: '-'
    note: 7nm N+2受限于DUV光刻机，无法进入5nm以下
  barriers:
  - item: 资本强度
    detail: 一座3nm工厂投资$300亿+
  - item: EUV获取
    detail: ASML独家供应，出口管制
  - item: 工艺积累
    detail: FinFET→GAA→CFET需10年+迭代
  tech_gap:
  - dimension: TSMC 2nm良率约90% vs 三星约50%。中国受限于EUV，先进制程代工差距10-15年
    detail: ''
key_trends:
- title: TSMC先进制程产能供不应求
  detail: 3nm产线2025年利用率100%+，NVIDIA/AMD/Apple抢产能，代工价格年涨10-15%
- title: 三星2nm GAA是关键翻身机会
  detail: 若良率达标(>80%)可为AMD/Intel提供第二供应源，降低TSMC独家依赖
- title: Intel 18A能否切入GPU代工
  detail: Intel与NVIDIA谈判代工合作，若成功将改变GPU代工双寡头格局
- title: CoWoS先进封装成为GPU制造的新瓶颈
  detail: GPU制造不再只是晶圆，先进封装产能决定最终出货量
price_conduction:
- TSMC 3nm代工价格年涨10-15%
- GPU芯片制造成本增加5-8%
- NVIDIA/AMD将部分成本转嫁给云厂商和消费者
- 剩余部分压缩自身毛利率（NVIDIA从76%向70%方向下滑）
- 长期推动寻找第二供应商（三星/Intel）和自研芯片
wikilinks:
- GPU架构设计
- GPU
companies:
- ticker: TSM
  name: TSMC(台积电)
  role: 龙头
  rev: 20
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 5
- ticker: AMD
  name: AMD
  role: 二线弹性
  rev: 5
sources:
- title: TSMC 2025 Q2 Earnings Call
  summary: ''
  url: https://www.tsmc.com
- title: Samsung Foundry SAFE Forum 2025
  summary: ''
  url: ''
- title: Intel Foundry Direct Connect 2025
  summary: ''
  url: https://www.intel.com

key_inputs: ["GPU架构设计", "HBM高带宽内存", "先进封装CoWoS", "晶圆代工(先进制程)"]
key_customers: ["AI服务器", "AI训练集群/超算", "云计算IaaS"]---

# GPU制造代工

> **AI算力** · L3 · TAM **$55B** · CAGR **30%**

GPU制造代工将GPU架构设计转化为物理芯片——晶圆制造(光刻/刻蚀/CMP等数百步)+CP测试+CoWoS封装+FT测试。|**TSMC绝对垄断——NVIDIA/AMD/Intel先进GPU全部由TSMC 4nm/3nm制造**。代工毛利率(40-55%)低于架构设计(65-72.7%)，但3nm/2nm产能稀缺→TSMC年涨10-15%。三星2nm GAA良率40-60%追赶中，Intel 18A仅65-75%，均远落后TSMC(70-80%)。|**TSMC AI相关收入预计2029年达46%总营收**。代工从「制造外包」→「战略稀缺资源」。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $55B |
| 年复合增长率(CAGR) | 30% |
| 利润率区间 | 40-55% |
| 成本占比 | 30% (GPU价值) |
| 利润池占比 | 20% (GPU利润池) |
| 附加值 | high |

## 关联

（待补充）
