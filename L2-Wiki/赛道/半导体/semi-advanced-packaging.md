---
name: 先进封装(CoWoS/3D)
slug: semi-advanced-packaging
industry: 半导体
layer: L3
tam_bn: 30.0
cagr_pct: 40.0
margin: 55-65%
cost_share_pct: 15
cost_share_context: AI芯片总成本（CoWoS封装占15-20%）
profit_pool_pct: 20
profit_pool_context: 先进封装利润池（CoWoS毛利率~60%接近先进制程，TSMC封测业务从后端服务升级为核心利润引擎）
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: TSMC
    share: '>90%'
    note: 台湾，CoWoS绝对垄断，2026扩至~120K wpm，NVIDIA独占60%产能(700K wafers)，ASP $17K+毛利率~60%
  - name: Intel
    share: ~2%
    note: EMIB/Foveros+3D封装，SK Hynix+Google+AWS评估中，NVIDIA $5B备选协议，EMIB-T 2026量产
  - name: 三星
    share: ~3%
    note: 韩国，I-Cube/X-Cube+3D封装，HBM4用Hybrid Bonding差异化
  china:
  - name: 长电科技(JCAP)
    share: '-'
    note: 600584 XDFOI Chiplet先进封装，对标CoWoS
  - name: 通富微电
    share: '-'
    note: 002156 AMD Chiplet封测，Vision先进封装平台
  barriers:
  - item: 硅中介层+微凸块+C4工艺集成
    detail: 10年+技术积累
  - item: TSMC客户锁定
    detail: NVIDIA/AMD/Apple长期绑定
  - item: CoWoS-L良率挑战(CTE mismatch)
    detail: 反成护城河
  tech_gap:
  - dimension: 中国先进封装差距5-7年，但OSAT端(长电/通富)承接CoWoS溢出需求。Intel EMIB+三星Hybrid Bonding是有力替代方案但客户认证周期长
    detail: ''
key_trends:
- title: CoWoS产能2025~55K→2026~120K wpm(+118%)
  detail: NVIDIA独占60%仍供不应求，ASP $10K→$17K+
- title: CoWoS-L良率问题
  detail: CTE热膨胀不匹配导致Blackwell前三季产出减半→2026H2改善
- title: Intel EMIB+三星Hybrid Bonding挑战TSMC
  detail: SK Hynix测试EMIB、NVIDIA $5B备选协议
- title: TSMC封测从后端服务升级为核心利润引擎
  detail: CoWoS毛利率~60%接近先进制程
price_conduction:
- CoWoS产能是当前AI芯片供应链#1瓶颈，TSMC垄断>90%份额。CoWoS产能不足
- GPU出货受限（NVIDIA Blackwell交期18个月，积压3.6M units）
- AI服务器交付延迟
- 云厂商CAPEX计划被打乱
- 全链条AI算力短缺。TSMC CoWoS wafer ASP从$10K(2025)涨至$17K+(2026)直接传导至GPU成本。CoWoS-L良率问题(CTE mismatch)
- Blackwell产出2025前三季减半
- 加剧供给紧张。产能售罄至2027年中
wikilinks:
- GPU
- 封装基板材料
- 晶圆代工(先进制程)
- AI芯片设计(Fabless)
companies:
- ticker: TSM
  name: TSMC(台积电)
  role: 龙头
  rev: 15
- ticker: '600584'
  name: 长电科技
  role: 二线弹性
  rev: 20
- ticker: INTC
  name: Intel
  role: 二线弹性
  rev: 10
- ticker: NVDA
  name: NVIDIA
  role: 二线弹性
  rev: 10
- ticker: '2325'
  name: SPIL (矽品)
  role: 二线弹性
  rev: 50
key_customers:
- AI芯片设计(Fabless)
sources:
- title: TSMC FY2025 Earnings
  summary: ''
  url: https://investor.tsmc.com
- title: Morgan Stanley CoWoS Customer Allocation 2026
  summary: ''
  url: ''
- title: Wedbush TokenRing《The Silicon Squeeze》Jan 2026
  summary: ''
  url: ''
- title: 长电科技2025年报
  summary: ''
  url: ''
---

# 先进封装(CoWoS/3D)

> **半导体** · L3 · TAM **$30B** · CAGR **40%**

先进封装将多颗芯片（GPU+HBM+硅中介层）通过**2.5D/3D技术集成**在单一封装内——是当前AI芯片供应链的**#1瓶颈**。|**TSMC CoWoS（Chip-on-Wafer-on-Substrate）绝对垄断>90%份额**。产能从~55K wpm(2025)→~120K wpm(end 2026,+118%)。NVIDIA独占~60%产能(700K wafers/yr)。CoWoS wafer ASP从$10K(2025)→$17K+(2026)，毛利率~60%。产能售罄至2027年中。|**CoWoS-L良率问题（CTE热膨胀系数不匹配）导致2025年前三季Blackwell产出减半**。Intel EMIB+Foveros（NVIDIA $5B备选协议）和三星I-Cube+Hybrid Bonding是两大替代方案。中国长电科技XDFOI和通富微电Vision在先进封装承接溢出需求。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $30B |
| 年复合增长率(CAGR) | 40% |
| 利润率区间 | 55-65% |
| 成本占比 | 15% (AI芯片总成本（CoWoS封装占15-20%）) |
| 利润池占比 | 20% (先进封装利润池（CoWoS毛利率~60%接近先进制程，TSMC封测业务从后端服务升级为核心利润引擎）) |
| 附加值 | high |

## 关联

（待补充）
