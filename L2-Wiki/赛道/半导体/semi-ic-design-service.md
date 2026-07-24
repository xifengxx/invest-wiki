---
name: IC设计服务(Fabless)
slug: semi-ic-design-service
industry: 半导体
layer: L4
tam_bn: 15.0
cagr_pct: 15.0
margin: 40-55%
cost_share_pct: 25
cost_share_context: 芯片设计成本（制造成本占60%，设计工具+IP占25%）
profit_pool_pct: 15
profit_pool_context: Fabless芯片设计利润池（NVIDIA毛利率72.7%为天花板，MediaTek/Qualcomm毛利率40-55%）
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L4
competition:
  global:
  - name: NVIDIA
    share: 美国
    note: 'AI GPU #1($215.9B DC FY2026)，CUDA生态锁定，毛利率72.7%'
  - name: Qualcomm
    share: 美国
    note: '通信芯片+手机SoC #1($40B+)，Snapdragon'
  - name: Broadcom
    share: 美国
    note: 'ASIC定制+网络芯片 #1($39.7B)'
  - name: AMD
    share: 美国
    note: CPU+GPU双线
  - name: MediaTek
    share: 台湾
    note: 手机SoC全球出货量#1
  china:
  - name: 海思
    share: '-'
    note: 麒麟(手机)+昇腾(AI)+鲲鹏(CPU)，受制裁抑制
  - name: 紫光展锐
    share: '-'
    note: 手机芯片国产#2(仅次于海思)
  - name: 韦尔股份
    share: '-'
    note: '603501 收购OmniVision成全球CIS #3'
  barriers:
  - item: 先进制程获取(TSMC/Samsung)
    detail: 受美国制裁限制中国Fabless获取3nm/2nm
  - item: ARM/x86架构授权
    detail: ARM授权受限加速中国RISC-V替代
  - item: IP核获取成本
    detail: 高速SerDes/HBM PHY/DDR PHY IP费用极高
  tech_gap:
  - dimension: 中国Fabless设计能力差距3-5年，但受限于制造（TSMC断供）+IP（ARM授权受限）+EDA（国产化率15%），三重锁死
    detail: ''
key_trends:
- title: Chiplet+UCIe降低设计门槛
  detail: Fabless从巨头垄断→生态化竞争，创业公司以$100M设计AI芯片
- title: 云厂商自研芯片(AWS/Google/Microsoft)重塑Fabless格局
  detail: 最大客户变最大竞争对手
- title: AI辅助芯片设计→效率提升5x
  detail: Synopsys AgentEngineer+AI EDA让芯片设计民主化
- title: 中国Fabless从消费电子→汽车/AI芯片升级
  detail: 海思回归+紫光+韦尔+地平线多点开花
price_conduction:
- 先进制程流片成本$500M+(3nm)
- 只有超大芯片公司能负担
- Fabless行业集中度提升。Chiplet+UCIe将设计成本降至$100M
- 创业公司进入
- Fabless从巨头垄断→生态化竞争
companies:
- ticker: QCOM
  name: Qualcomm
  role: 龙头
  rev: 55
- ticker: AVGO
  name: Broadcom
  role: 龙头
  rev: 40
- ticker: MDTKF
  name: MediaTek (联发科)
  role: 龙头
  rev: 90
- ticker: AAPL
  name: Apple
  role: 概念股
  rev: 5
- ticker: MRVL
  name: Marvell
  role: 龙头
  rev: 40
- ticker: 3034.TW
  name: Novatek (联咏)
  role: 龙头
  rev: 90
- ticker: 2379.TW
  name: Realtek (瑞昱)
  role: 龙头
  rev: 70
wikilinks:
- 成熟制程代工
- EDA与IP核
- CIS图像传感器
- 封装测试(OSAT)
key_inputs:
- EDA与IP核
- 封装测试(OSAT)
sources:
- title: IC Insights《Fabless Top 25 2025》
  summary: ''
  url: ''
- title: NVIDIA FY2026 Annual Report
  summary: ''
  url: ''
- title: 海思/紫光展锐
  summary: ''
  url: ''
- title: 韦尔股份2025年报
  summary: ''
  url: ''

key_customers: ["AI芯片设计(Fabless)", "CPU(服务器级)", "FPGA", "模拟芯片"]---

# IC设计服务(Fabless)

> **半导体** · L4 · TAM **$15B** · CAGR **15%**

IC设计服务（Fabless模式）公司专攻芯片架构和设计——不建晶圆厂，委托TSMC/Samsung代工制造。**从「卖芯片」升级为「卖IP+卖设计+卖系统方案」**。|**全球Fabless市场$200B+(2025)，NVIDIA($215.9B数据中心FY2026)、Qualcomm($40B+)、Broadcom($39.7B)、AMD($25B+)、MediaTek(联发科$17B+)为五大Fabless巨头**。Fabless模式成就了美国芯片设计霸权。|**Chiplet+UCIe降低设计门槛（$500M→$100M）⇒更多创业公司进入AI芯片设计。中国海思(麒麟/昇腾)+紫光展锐+韦尔股份(CIS)+卓胜微(射频)**在特定领域追赶。受限于先进制程获取+EDA+IP授权，中国Fabless「大而不强」。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $15B |
| 年复合增长率(CAGR) | 15% |
| 利润率区间 | 40-55% |
| 成本占比 | 25% (芯片设计成本（制造成本占60%，设计工具+IP占25%）) |
| 利润池占比 | 15% (Fabless芯片设计利润池（NVIDIA毛利率72.7%为天花板，MediaTek/Qualcomm毛利率40-55%）) |
| 附加值 | high |

## 关联

（待补充）
