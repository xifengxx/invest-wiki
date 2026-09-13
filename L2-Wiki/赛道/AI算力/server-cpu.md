---
name: CPU(服务器级)
slug: server-cpu
industries:
- AI算力
- 半导体
layer: L3
tam_bn: 40.0
cagr_pct: 20.0
margin: 50-65%
cost_share_pct: 10
cost_share_context: AI服务器（半导体口径：占服务器总成本25%）
profit_pool_pct: 5
profit_pool_context: AI服务器利润池（半导体口径：CPU利润池20%，Intel/AMD双寡头→ARM崛起，ASP $2K-10K/颗）
value_add: high
updated: 2026-09
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Intel Xeon
    share: 59-71%
    note: 美国，#1，P-core+E-core混合架构，Granite Rapids 128核(Intel 3)与Clearwater Forest 288核(18A)双线反击，2026涨价8-10%
  - name: AMD EPYC
    share: ~41%
    note: 美国，#2但收入份额首破41.3%(Q4 2025)，Turin 192核(Zen 5c/3nm)与Venice 256核在核心数上碾压Intel，ASP为Intel 2x，2026涨价16-17%
  china:
  - name: ARM阵营：AWS Graviton
    share: 40%+
    note: 占AWS新实例40%+，自研自用，2M+颗，30-40%性价比优势
  - name: ARM阵营：NVIDIA Grace
    share: '-'
    note: 2025出货~2.5M颗，2x perf/watt vs x86，GB200中1 Grace配2 GPU，因NVLink-C2C紧耦合拥有独特溢价能力
  - name: Ampere
    share: '-'
    note: 美国，192核Oracle部署，已被SoftBank收购，云原生CPU定位
  barriers:
  - item: x86 软件生态
    detail: 数十年积累的企业软件栈与开发者习惯锁定 x86，迁移成本极高
  - item: 指令集授权
    detail: x86 授权仅 Intel/AMD/海光持有；ARM 需架构授权且受地缘限制
  - item: 制程与核心数
    detail: 高端服务器 CPU 依赖先进制程，核心数竞赛需制程支撑
  tech_gap:
  - dimension: 中国 CPU 三路线（海光 x86 授权/飞腾 ARM/鲲鹏 ARM）中，海光性能最接近国际水平但受授权约束；整体在单核性能、软件生态与量产规模上差距约 5-8 年
    detail: ''
key_trends:
- title: ARM服务器CPU渗透率从10%向20%+
  detail: AWS Graviton已占亚马逊新实例40%+，NVIDIA Grace+NVLink在AI服务器中占据独特位置；整体ARM份额13-16%，目标2030年达40%（Graviton/Grace/Ampere三重驱动）
- title: Intel 18A制程2025量产力图逆转颓势
  detail: Clearwater Forest(288核)和Diamond Rapids是Intel反击AMD的关键产品
- title: AMD EPYC Zen 5/Zen 6持续扩大份额
  detail: Turin(192核)和Venice(256核)在核心数上碾压Intel；Q4 2025收入份额首破41.3%，有望2026年收入超越Intel成为x86服务器CPU #1
- title: 中国信创CPU市场快速增长
  detail: 三条路线并进——海光(688041,x86 AMD授权)、飞腾(ARM)、鲲鹏(ARM)，受益于国产替代政策
- title: Agentic AI驱动CPU:GPU比例从1:4~1:8转向接近1:1
  detail: CPU重回AI数据中心核心，英伟达Vera CPU+NVLink-C2C在AI服务器中占据独特位置，云厂商Capex CAGR 46%直接拉动CPU需求
- title: 2026年CPU涨价周期
  detail: Intel涨价8-10%、AMD涨价16-17%，共同推动服务器成本上升
price_conduction:
- 服务器CPU市场竞争充分（Intel vs AMD vs ARM阵营）
- 任何厂商单方面涨价都会丢失份额
- 客户议价能力强。NVIDIA Grace因与GPU紧耦合（NVLink-C2C）拥有独特溢价能力
- ARM阵营（Graviton/Axion/Ampere）TCO优势
- 长期x86份额承压
- CPU价格总体下行
wikilinks:
- GPU
- AI服务器
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
- AI芯片设计(Fabless)
- 高纯硅料与硅片
- 先进封装(CoWoS/3D)
- 封装测试(OSAT)
- FPGA
- 数据中心IDC
companies:
- ticker: INTC
  name: Intel
  role: 龙头
  rev: 55
- ticker: AMD
  name: AMD
  role: 龙头
  rev: 30
- ticker: NVDA
  name: NVIDIA
  role: 二线弹性
  rev: 5
- ticker: ARM
  name: Arm Holdings
  role: 生态主导
  rev: 10
- ticker: '688047'
  name: 龙芯中科
  role: 国产替代
  rev: 30
- ticker: '688256'
  name: 寒武纪
  role: 概念相关
  rev: 10
key_inputs:
- 晶圆代工(先进制程)
- 存储芯片(DRAM/NAND)
- 高纯硅料与硅片
- 先进封装(CoWoS/3D)
key_customers:
- AI服务器
- 数据中心IDC
sources:
- title: Mercury Research《Server CPU Q4 2025》
  summary: ''
  url: ''
- title: SemiAnalysis《CPUs are Back 2026》
  summary: ''
  url: https://www.semianalysis.com
- title: AMD FY2025 Earnings
  summary: ''
  url: ''
- title: Intel FY2025
  summary: ''
  url: ''
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

> **AI算力** · L3 · TAM **$40B** · CAGR **20%**

服务器CPU是数据中心的**通用计算大脑**——运行OS、管理内存、调度任务和协调加速器。**Agentic AI训练让CPU重回数据中心核心**：RL训练循环需大量CPU做编译+验证+Tool Use。|**x86双雄：Intel Xeon(~59-71%单位份额,但AMD EPYC收入份额首破41.3%**)。AMD Turin 192核(3nm)vs Intel Granite Rapids 128核。AMD ASP是Intel 2x。2026双方均涨价(Intel 8-10%,AMD 16-17%)。|**ARM阵营快速增长(13-16%份额)**：AWS Graviton(2M+颗,30-40%性价比优势)、NVIDIA Grace(2025出货~2.5M颗,2x perf/watt vs x86)、Ampere(SoftBank收购)。ARM目标2030年40%份额。中国CPU三路线：海光(x86 AMD授权)+飞腾(ARM)+鲲鹏(ARM)。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $40B |
| 年复合增长率(CAGR) | 20% |
| 利润率区间 | 50-65% |
| 成本占比 | 10% (AI服务器)〔半导体口径：25% 服务器总成本〕 |
| 利润池占比 | 5% (AI服务器利润池)〔半导体口径：20% CPU利润池〕 |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22
> 来源: 消化笔记/2026-07-22-v1.1-中原证券电子行业中期策略
> 置信度: 高

- **cagr**: 10% → 20%
- **key_trends**: +1条 "Agentic AI驱动CPU:GPU比例从1:4~1:8转向接近1:1——CPU重回AI数据中心核心"
- **依据**: 中原证券2026中期策略——Agentic AI时代承担相当比重工作负载，CPU:GPU比例从1:4~1:8转向接近1:1，云厂商Capex CAGR 46%

### 更新 2026-07-22 (v1.2)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从3→9条

### 更新 2026-09-13（合并 semi-server-cpu 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-server-cpu.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$40B）；本方 cagr 20% / margin 50-65% 保留
- **口径保留**: cost_share / profit_pool 的半导体口径（25% 服务器总成本 / 20% CPU利润池）并入 context 备注明细，两个视角并存
- **key_trends**: 5 → 6 条。吸收对方的"2026年CPU涨价周期"（本方缺）；将对方更具体的数字并入本方既有条目（AMD 收入份额首破41.3%、ARM 2030目标40%、中国CPU三路线）
- **sources**: 4 → 7 条。并入瑞银2026Q1报告、美银证券2030预测、TechPowerUp 40%份额报告
- **companies**: 3 → 6 家。并入 ARM Holdings、龙芯中科(688047)、寒武纪(688256)
- **wikilinks**: 5 → 10 条。并入 高纯硅料与硅片、先进封装(CoWoS/3D)、封装测试(OSAT)、FPGA、数据中心IDC
- **key_inputs**: 2 → 4 条（并入 高纯硅料与硅片、先进封装(CoWoS/3D)）；**key_customers**: 新增（AI服务器、数据中心IDC）
- **competition**: 补齐 AMD EPYC 独立条目（share ~41%），Intel 条目并入更具体的制程与涨价信息，ARM 阵营拆为 Graviton / NVIDIA Grace / Ampere 三条
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
