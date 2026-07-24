---
name: CPU(服务器级)
slug: semi-server-cpu
industry: 半导体
layer: L3
tam_bn: 40.0
cagr_pct: 10.0
margin: 55-70%
cost_share_pct: 25
cost_share_context: 服务器总成本
profit_pool_pct: 20
profit_pool_context: CPU利润池（Intel/AMD双寡头→ARM崛起，ASP $2K-10K/颗）
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L3
competition:
  global:
  - name: Intel Xeon
    share: 59-71%
    note: 美国，P-core+E-core混合架构，Granite Rapids 128核(Intel 3)，2026涨价8-10%, AMD EPYC
  china:
  - name: ARM阵营：NVIDIA Grace
    share: '-'
    note: 2025出货~2.5M颗，GB200中1 Grace配2 GPU, AWS Graviton
  - name: Ampere
    share: '-'
    note: SoftBank收购，云原生CPU
  barriers: []
  tech_gap: []
key_trends:
- title: AMD收入份额首破41%(Q4 2025)
  detail: 有望2026年收入超越Intel成为x86服务器CPU#1
- title: Agentic AI训练让CPU重回核心
  detail: RL训练需大量CPU做编译+验证，CPU:GPU从1:8→1:1
- title: ARM份额13%→2030目标40%
  detail: Graviton/Grace/Ampere三重驱动
- title: 2026年CPU涨价周期
  detail: Intel 8-10%+AMD 16-17%推动服务器成本上升
price_conduction:
- 服务器CPU市场竞争充分（Intel vs AMD vs ARM阵营）
- 任何厂商单方面涨价都会丢失份额
- 客户议价能力强。NVIDIA Grace因与GPU紧耦合（NVLink-C2C）拥有独特溢价能力
- ARM阵营（Graviton/Axion/Ampere）TCO优势
- 长期x86份额承压
- CPU价格总体下行
wikilinks:
- 晶圆代工(先进制程)
- 高纯硅料与硅片
- 先进封装(CoWoS/3D)
- 封装测试(OSAT)
- AI芯片设计(Fabless)
- GPU
- FPGA
- 存储芯片(DRAM/NAND)
- AI服务器
- 数据中心IDC
key_inputs:
- 晶圆代工(先进制程)
- 硅晶圆
- 先进封装(CoWoS/3D)
key_customers:
- AI服务器
- 数据中心IDC
companies:
- ticker: INTC
  name: Intel
  role: 全球龙头
  rev: 60
- ticker: AMD
  name: AMD
  role: 全球二线
  rev: 35
- ticker: ARM
  name: ARM Holdings
  role: 生态主导
  rev: 10
- ticker: NVDA
  name: NVIDIA(Grace)
  role: 新兴势力
  rev: 5
- ticker: '688047'
  name: 龙芯中科
  role: 国产替代
  rev: 30
- ticker: '688256'
  name: 寒武纪
  role: 概念相关
  rev: 10
sources:
- title: 瑞银 2026Q1服务器CPU市场报告
  summary: AMD收入份额46.2%首次超越Intel，ARM出货量份额17.7%加速扩张
  url: https://dxpress.gelonghui.com/live/2449244
- title: 美银证券 2030服务器CPU市场预测
  summary: CPU市场从300亿→1700亿美元，AI Agent节点700亿+传统云300亿
  url: http://www.eeo.com.cn/2026/0622/924791.shtml
- title: TechPowerUp AMD服务器CPU突破40%收入份额
  summary: AMD EPYC Q4 2025收入份额首次突破40%，高核数产品以更少芯片创更高收入
  url: https://www.techpowerup.com/346287/report-amd-breaks-40-server-revenue-share-for-the-first-time
---

# CPU(服务器级)

> **半导体** · L3 · TAM **$40B** · CAGR **10%**

服务器CPU是数据中心的**通用计算大脑**——运行OS、管理内存、调度任务、协调GPU/HBM/网络等加速器。**Agentic AI训练让CPU重回数据中心核心**：RL训练循环需大量CPU做编译+验证+Tool Use，CPU:GPU比例从1:8→1:1。|**x86双雄：Intel Xeon(~59-71%单位份额) vs AMD EPYC（收入份额首破41.3%，Q4 2025）**。AMD Turin 192核(Zen 5c/3nm)、Intel Granite Rapids 128核(Intel 3)。AMD ASP是Intel 2x。2026年双方均涨价(Intel 8-10%, AMD 16-17%)。|**ARM阵营快速增长（13-16%份额）**：AWS Graviton(2M+颗,30-40%性价比优势)、NVIDIA Grace(2025出货~2.5M颗, 2x perf/watt vs x86)、Ampere(SoftBank收购)。ARM目标2030年40%份额。中国CPU三路线：海光(x86 AMD授权)+飞腾(ARM)+鲲鹏(ARM)。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $40B |
| 年复合增长率(CAGR) | 10% |
| 利润率区间 | 55-70% |
| 成本占比 | 25% (服务器总成本) |
| 利润池占比 | 20% (CPU利润池（Intel/AMD双寡头→ARM崛起，ASP $2K-10K/颗）) |
| 附加值 | high |

## 关联

（待补充）
