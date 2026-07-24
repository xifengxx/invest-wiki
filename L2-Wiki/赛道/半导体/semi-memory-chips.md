---
name: 存储芯片(DRAM/NAND)
slug: semi-memory-chips
industry: 半导体
layer: L3
tam_bn: 200.0
cagr_pct: 18.0
margin: 30-50%
cost_share_pct: 30
cost_share_context: 全球半导体总市场
profit_pool_pct: 15
profit_pool_context: 存储芯片利润高度集中于三巨头（三星+SK Hynix+Micron占DRAM 95%利润）
value_add: commodity
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: Samsung
    share: ~38%
    note: 韩国，DRAM+NAND双#1，HBM3E验证延迟致份额从41%→17%，2nm GAA赶超中, SK Hynix
  - name: Micron
    share: ~25%
    note: 美国，DRAM#3，放弃消费DRAM全面转AI/HBM，$200B Capex 2026
  china:
  - name: CXMT(长鑫存储)
    share: '-'
    note: DRAM 17nm DDR5 2026量产，国产DRAM从0→1
  - name: YMTC(长江存储)
    share: '-'
    note: NAND 232层量产，国产NAND从0→1
  barriers:
  - item: 先进制程DRAM(1a/1b nm)
    detail: 需要EUV光刻，受美国出口管制
  - item: 3D NAND 300+层堆叠
    detail: 层数越高对ALD/CVD/蚀刻设备要求越高
  - item: HBM TSV堆叠+混合键合
    detail: DRAM堆叠12-16层极难
  tech_gap:
  - dimension: 中国DRAM差距约3-5年(CXMT 17nm vs 三星12nm)，NAND差距约2-3年(YMTC 232层 vs 三星300+层)
    detail: ''
key_trends:
- title: HBM需求分流DRAM产能
  detail: 传统DRAM供给减少+涨价，HBM 2026合约涨20%
- title: 3D NAND堆叠从300→400→500层
  detail: 每100层新增需要全新的蚀刻/沉积设备
- title: CXMT DDR5 2026量产
  detail: 中国DRAM从0→1，全球份额<5%但增长迅速
- title: AI推理驱动存储需求
  detail: 推理需要大量KV Cache存储（HBM+DRAM+NAND三级）
- title: 存储器超级周期来临
  detail: WSTS预测2026存储器同比+249.5%，德勤预测存储器价格2026H1再涨50%，消费级内存短缺可能持续十年，DRAM CapEx+14%至$610亿
price_conduction:
- DRAM周期性极强——每2-3年一轮价格暴涨暴跌。HBM需求分流DRAM产能
- 传统DRAM供给减少
- DDR5上涨60%+。CXMT/YMTC量产
- 中国存储自给率从0→5%
- 但全球供给仍高度集中于韩/美三家
- 供给端垄断定价权极强。存储涨价
- 服务器/手机BOM成本上升
- OEM利润率受挤压
companies:
- ticker: 005930.KS
  name: Samsung
  role: 龙头
  rev: 25
- ticker: 000660.KS
  name: SK Hynix
  role: 龙头
  rev: 90
- ticker: CXMT
  name: CXMT (长鑫存储)
  role: 概念股
  rev: 95
- ticker: YMTC
  name: YMTC (长江存储)
  role: 概念股
  rev: 95
- ticker: MU
  name: Micron
  role: 龙头
  rev: 85
- ticker: KIOXIA
  name: Kioxia
  role: 二线弹性
  rev: 95
- ticker: WDC
  name: Western Digital
  role: 二线弹性
  rev: 35
- ticker: 2337.TW
  name: Macronix (旺宏)
  role: 二线弹性
  rev: 85
- ticker: 2344.TW
  name: Winbond (华邦)
  role: 二线弹性
  rev: 70
- ticker: '8299'
  name: Phison (群联)
  role: 二线弹性
  rev: 70
- ticker: '2408'
  name: Nanya Technology (南亚科)
  role: 二线弹性
  rev: 80
- ticker: '2344'
  name: Winbond (华邦)
  role: 二线弹性
  rev: 50
wikilinks:
- 光掩模版
- 电子特气
- 刻蚀设备
- 检测量测设备
- 高纯硅料与硅片
- CPU(服务器级)
- CMP抛光液与抛光垫
- 晶圆代工(先进制程)
- AI芯片设计(Fabless)
key_inputs:
- 光掩模版
- 电子特气
- 检测量测设备
- 高纯硅料与硅片
- CMP抛光液与抛光垫
key_customers:
- CPU(服务器级)
- AI芯片设计(Fabless)
sources:
- title: TrendForce《DRAM/NAND Industry Q4 2025》
  summary: ''
  url: https://www.trendforce.com
- title: SK Hynix FY2025 Earnings
  summary: ''
  url: ''
- title: Samsung FY2025
  summary: ''
  url: ''
- title: CXMT长鑫存储
  summary: ''
  url: ''
- title: YMTC长江存储
  summary: ''
  url: ''
---

# 存储芯片(DRAM/NAND)

> **半导体** · L3 · TAM **$200B** · CAGR **18%**

存储芯片是半导体产业中**最大的单一品类**（占全球半导体市场30%+）。DRAM（动态随机存取存储器）和NAND Flash（闪存）为两大核心产品。|**DRAM市场三巨头垄断>95%：三星(~38%)、SK Hynix(~34%)、Micron(~25%)**。HBM是DRAM中最高端品类——HBM3E 2026合约价涨20%，三巨头全部售罄。DDR5价格涨60%+(Samsung 32GB $149→$239)。NAND由三星+Kioxia+WDC+Micron+SK Hynix+YMTC六家主导。|**中国CXMT(长鑫存储)DRAM 17nm DDR5 2026量产**，YMTC(长江存储)NAND 232层量产。国产存储芯片从零到一突破，但全球份额仍<5%，且受美国制裁持续限制先进制程设备获取。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $200B |
| 年复合增长率(CAGR) | 18% |
| 利润率区间 | 30-50% |
| 成本占比 | 30% (全球半导体总市场) |
| 利润池占比 | 15% (存储芯片利润高度集中于三巨头（三星+SK Hynix+Micron占DRAM 95%利润）) |
| 附加值 | commodity |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22
> 来源: [[消化笔记/2026-07-22-v1.1-德勤全球半导体趋势]], [[消化笔记/2026-07-22-v1.1-中原证券电子行业中期策略]]
> 置信度: 高

- **tam**: $120B → $200B
- **cagr**: 10% → 18%
- **key_trends**: +1条 "存储器超级周期来临——WSTS预测+249.5%，德勤预测价格再涨50%"
- **依据**: 德勤预测2026存储器$~2,000亿；WSTS预测存储器同比+249.5%；消费级内存短缺可能持续十年
