---
name: 先进封装CoWoS
slug: cowos-advanced-packaging
industry: AI算力
layer: L2
tam_bn: 30.0
cagr_pct: 40.0
margin: 55-65%
cost_share_pct: 15
cost_share_context: AI芯片总成本(GPU+HBM+封装)
profit_pool_pct: 20
profit_pool_context: CoWoS毛利率~60%接近先进制程，TSMC封测业务从后端服务升级为核心利润引擎
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: TSMC
    share: '>90%'
    note: CoWoS绝对垄断，2026年扩至~120K wpm，NVIDIA独占60%产能(700K wafers)，ASP $17K+毛利率~60%
  - name: Intel
    share: ~2%
    note: EMIB/Foveros获SK Hynix+Google+AWS评估，NVIDIA签$5B备选协议，EMIB-T 2026量产
  - name: 三星
    share: ~3%
    note: I-Cube/X-Cube+3D封装，HBM4用Hybrid Bonding差异化，2026年$73B投资
  china:
  - name: 长电科技
    share: '-'
    note: 600584国内#1 SiP/Fan-out
  - name: 通富微电
    share: '-'
    note: 002156 AMD核心封测伙伴
  - name: 华天科技
    share: '-'
    note: 002185
  - name: 甬矽电子
    share: '-'
    note: 688362 SiP
  barriers:
  - item: 硅中介层+微凸块+C4工艺集成难度极高
    detail: ''
  - item: TSMC 10年+技术积累+客户生态锁定
    detail: ''
  - item: CoWoS-L良率挑战(CTE mismatch)反成护城河
    detail: ''
  tech_gap:
  - dimension: CoWoS产能2026翻倍仍售罄至2027中。中国先进封装占比<10%，但OSAT(ASE/Amkor/长电)承接CoWoS溢出需求。Intel EMIB+三星Hybrid Bonding是有力替代方案但客户认证周期长
    detail: ''
key_trends:
- title: CoWoS产能2025~55K->2026~120K wpm(+118%)
  detail: 但NVIDIA独占60%仍供不应求，ASP $10K->$17K+|CoWoS-L良率爬坡——CTE热膨胀不匹配导致Blackwell前三季产出减半，但2026H2改善|Intel EMIB+三星Hybrid Bonding挑战TSMC——SK Hynix测试EMIB、NVIDIA签$5B备选协议、三星HBM4用Hybrid Bonding
- title: TSMC封测从后端服务升级为核心利润引擎
  detail: CoWoS毛利率~60%接近先进制程，封测占TSMC收入2026年将超10%|中国OSAT承接溢出机会——ASE/Amkor/长电/通富微电受益CoWoS产能紧缺，但高端封装(CoWoS-L级)差距5-7年
- title: 华为韬定律开辟后摩尔时代
  detail: 通过逻辑折叠+2.5D/3D集成+混合键合+TSV+Chiplet实现芯片性能突破，先进封装从后端工艺升级为芯片性能核心环节
price_conduction:
- CoWoS是当前AI芯片供应链#1瓶颈，TSMC垄断>90%份额。CoWoS产能不足
- GPU出货受限(NVIDIA Blackwell交期18个月，积压3.6M units)
- AI服务器交付延迟
- 云厂商CAPEX计划被打乱。TSMC CoWoS wafer ASP从$10K(2025)涨至$17K+(2026)直接传导至GPU成本。CoWoS-L良率问题(CTE mismatch)
- Blackwell产出2025前三季减半
- 加剧供给紧张。产能售罄至2027年中
wikilinks:
- GPU
- HBM高带宽内存
- ASIC/AI定制芯片
key_customers:
- GPU
companies:
- ticker: TSM
  name: TSMC(台积电)
  role: 龙头
  rev: 15
- ticker: '600584'
  name: 长电科技
  role: 龙头
  rev: 25
- ticker: '002156'
  name: 通富微电
  role: 二线弹性
  rev: 20
- ticker: 002185
  name: 华天科技
  role: 二线弹性
  rev: 15
- ticker: NVDA
  name: NVIDIA
  role: 龙头
  rev: 5
- ticker: '3711'
  name: 日月光 (ASE)
  role: 龙头
  rev: 25
- ticker: ASX
  name: 日月光 (ASE)
  role: 龙头
  rev: 25
- ticker: AMKR
  name: Amkor Technology
  role: 二线弹性
  rev: 30
- ticker: '6239'
  name: 力成科技
  role: 二线弹性
  rev: 20
- ticker: '2449'
  name: 京元电子
  role: 二线弹性
  rev: 15
- ticker: '688362'
  name: 甬矽电子
  role: 概念股
  rev: 15
sources:
- title: TSMC FY2025 Earnings & Technology Symposium
  summary: ''
  url: https://www.tsmc.com
- title: TrendForce CoWoS Capacity Analysis Apr 2026
  summary: ''
  url: https://www.trendforce.com
- title: Fusion Worldwide AI Bottleneck Analysis 2026
  summary: ''
  url: https://info.fusionww.com
- title: Morgan Stanley CoWoS Customer Allocation 2026
  summary: ''
  url: ''
- title: Wedbush Token Ring 'The Silicon Squeeze' Jan 2026
  summary: ''
  url: https://investor.wedbush.com
- title: Intel EMIB NVIDIA $5B Partnership May 2026
  summary: ''
  url: ''
- title: Goldman Sachs TSMC Target Raise 2026
  summary: ''
  url: ''

key_inputs: ["封装基板材料", "HBM高带宽内存", "晶圆代工(先进制程)"]---

# 先进封装CoWoS

> **AI算力** · L2 · TAM **$30B** · CAGR **40%**

CoWoS是TSMC开发的**2.5D先进封装技术**，将GPU/ASIC+HBM放在硅中介层通过微凸块连接，实现极高带宽密度。**是当前AI芯片供应链的#1瓶颈**——CoWoS产能决定全球GPU出货量。|**2026年CoWoS产能扩至~120K wpm**(2025年~55K wpm)，但NVIDIA锁定~60%产能(700K wafers/yr)，Blackwell B200 CoWoS-L良率因CTE热膨胀不匹配一度减半。TSMC CoWoS wafer ASP从$10K(2025)升至$17K+(2026)，毛利率~60%。**产能售罄至2027年中**。|**Intel EMIB获SK Hynix/Google/AWS评估**作为CoWoS替代方案，NVIDIA也签了$5B Intel封装备选协议。三星HBM4用Hybrid Bonding差异化。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $30B |
| 年复合增长率(CAGR) | 40% |
| 利润率区间 | 55-65% |
| 成本占比 | 15% (AI芯片总成本(GPU+HBM+封装)) |
| 利润池占比 | 20% (CoWoS毛利率~60%接近先进制程，TSMC封测业务从后端服务升级为核心利润引擎) |
| 附加值 | high |

## 关联

- 下游: [[GPU]]

## 动态更新记录

### 更新 2026-07-22
> 来源: 消化笔记/2026-07-22-v1.1-中原证券电子行业中期策略
> 置信度: 高

- **key_trends**: +1条 "华为韬定律——逻辑折叠+先进封装开辟后摩尔时代，先进封装从后端升级为芯片性能核心环节"
- **依据**: 中原证券2026中期策略——华为发布韬定律，逻辑折叠需基于2.5D/3D集成、混合键合、TSV、Chiplet等先进封装技术
