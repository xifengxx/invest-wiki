---
name: RISC-V AI芯片
slug: riscv-ai
industry: AI算力
layer: L3
tam_bn: 2.5
cagr_pct: 60.0
margin: 30-50%
cost_share_pct: 1
cost_share_context: AI芯片设计成本（半导体口径：2% AI芯片总市场）
profit_pool_pct: 3
profit_pool_context: AI芯片设计利润池（半导体口径：1%，RISC-V降低授权成本→利润从ARM/x86向Fabless+Foundry转移）
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L3
competition:
  global:
  - name: Tenstorrent
    share: '-'
    note: 美国，#1 RISC-V AI芯片，Jim Keller领衔，$700M融资估值$5B+；RISC-V+Chiplet AI芯片，Blackhole/Ascalon架构
  - name: SiFive
    share: '-'
    note: 美国，RISC-V IP授权#1 Intel/高通投资
  - name: Esperanto
    share: '-'
    note: 美国，ET-SoC-1千核AI推理芯片
  - name: Ventana
    share: '-'
    note: 美国，RISC-V CPU IP数据中心级
  china:
  - name: 阿里平头哥
    share: '-'
    note: 玄铁系列已出货数十亿颗，全球最大RISC-V部署；玄铁C910/C920系列，中国RISC-V生态核心推动者
  - name: 中科院香山（包云岗团队）
    share: '-'
    note: 开源高性能RISC-V处理器流片成功，学术→产业转化
  - name: 芯来科技
    share: '-'
    note: RISC-V IP授权（Nuclei芯来），对标SiFive
  - name: 赛昉科技
    share: '-'
    note: VisionFive开发板
  barriers:
  - item: 软件生态
    detail: CUDA锁定是最大障碍；Toolchain/OS/Driver 仍有差距（GCC/LLVM/Linux支持日趋成熟）
  - item: AI编译器/算子库仍在早期
    detail: ''
  - item: 性能验证周期长
    detail: ''
  - item: 高性能RISC-V核设计
    detail: 超标量/乱序执行/OoO设计极复杂
  - item: AI加速扩展(RVV Vector 1.0)
    detail: RISC-V向量扩展是AI推理的核心竞争力
  tech_gap:
  - dimension: RISC-V在AI芯片份额从零→2025年2%→2030年预计10%+。中国RISC-V生态全球最活跃
    detail: ''
  - dimension: 中国RISC-V生态差距最小（同一代起跑线）。RISC-V是地缘政治格局下中国芯片最关键的「Plan B」
    detail: ''
key_trends:
- title: RISC-V从IoT向AI/服务器渗透
  detail: Tenstorrent获现代汽车/三星$700M投资，估值$5B+；以Chiplet+RISC-V打造AI芯片，Blackhole/Ascalon架构
- title: 开源ISA降低AI芯片设计门槛
  detail: 创业公司不再需要支付ARM数千万美元授权费（ARM架构许可+版税$10M+），RISC-V+ASIC推动AI芯片民主化
- title: Tenstorrent Blackhole芯片2025年量产
  detail: 基于RISC-V的AI加速器，性能对标NVIDIA H100（Jim Keller领衔）
- title: 中国RISC-V生态最活跃
  detail: 阿里平头哥玄铁系列已出货数十亿颗，中科院包云岗团队「香山」处理器流片成功
- title: RISC-V AI芯片份额2%→10%+(2030)
  detail: 开源ISA+AI推理需求+地缘政治三重驱动
- title: 中国受ARM授权限制→加速RISC-V替代
  detail: ARM不给中国公司授权v9架构→RISC-V成唯一选择
price_conduction:
- RISC-V开源免费，芯片设计授权成本从$10M+(ARM架构许可+版税)降至$0
- 降低AI芯片设计门槛（无需支付ARM数千万美元授权费）
- 更多创业公司/玩家进入
- 长期增加AI芯片供给多样性
- 推动竞争和降价。但RISC-V商业化收入模式不清晰，短期盈利能力弱
- 加速AI芯片商业化，推动推理芯片价格下降→AI推理成本持续降低
wikilinks:
- 边缘AI
- AI芯片设计(Fabless)
- CPU(服务器级)
- FPGA
- EDA与IP核
- 晶圆代工(先进制程)
- Chiplet与异构集成
key_inputs:
- EDA与IP核
- 晶圆代工(先进制程)
key_customers:
- 边缘AI
- AI芯片设计(Fabless)
- CPU(服务器级)
- FPGA
companies:
- ticker: '688521'
  name: 芯原股份
  role: 国产替代
  rev: 25
- ticker: BABA
  name: 阿里巴巴
  role: 国产龙头
  rev: 10
- ticker: '300223'
  name: 北京君正
  role: 国产替代
  rev: 20
- ticker: '603986'
  name: 兆易创新 (GigaDevice)
  role: 国产替代
  rev: 15
sources:
- title: RISC-V International 2025 Summit /《2025生态报告》
  summary: 全球RISC-V SoC出货超50亿颗，AI推理与边缘计算成最大增量
  url: https://riscv.org
- title: Tenstorrent Architecture
  summary: ''
  url: ''
- title: 阿里平头哥
  summary: ''
  url: ''
- title: 中科院计算所香山处理器
  summary: ''
  url: ''
- title: 芯原股份2025年报
  summary: RISC-V IP授权国内第一，Chiplet+UCIe+RISC-V三合一平台
  url: https://www.verisilicon.com
---

# RISC-V AI芯片

> **AI算力** · L3 · TAM **$2.5B** · CAGR **60%**

RISC-V是**开源指令集架构(ISA)**——任何人免费使用修改，不像x86(专有)或ARM(高昂授权)。**在AI芯片领域让创业公司以极低成本设计加速器**。Tenstorrent(Jim Keller)+Esperanto两大标杆。|**中国RISC-V生态最活跃**——阿里平头哥玄铁+中科院包云岗团队。RISC-V AI芯片份额从近乎零(2023)→~2%(2025)→预计10%+(2030)。RISC-V+ASIC降低AI芯片设计门槛→定制芯片成本下降→更多创业公司进入。中国受ARM授权限制（ARM v9不授权中国公司，叠加美国制裁）→加速RISC-V替代，地缘政治是最大催化剂；芯来科技（Nuclei）是国产RISC-V IP代表，对标SiFive。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $2.5B |
| 年复合增长率(CAGR) | 60% |
| 利润率区间 | 30-50% |
| 成本占比 | 1% (AI芯片设计成本)〔半导体口径：2% AI芯片总市场〕 |
| 利润池占比 | 3% (AI芯片设计利润池)〔半导体口径：1% 利润从ARM/x86向Fabless+Foundry转移〕 |
| 附加值 | high |

## 关联

- 下游: [[边缘AI]]

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从2→8条

### 更新 2026-09-13（合并 semi-riscv-ai 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-riscv-ai.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$2.5B）；本方 cagr 60% / margin 30-50% / layer L3 保留（对方 cagr 45% / margin 40-55% / layer L4）
- **口径保留**: cost_share / profit_pool 的半导体口径（2% AI芯片总市场 / 1% 利润从ARM/x86向Fabless+Foundry转移）并入 context 备注明细，两个视角并存
- **key_trends**: 4 → 6 条。将对方更具体的表述吸收进本方既有条目（Blackhole/Ascalon架构、ARM架构许可$10M+、AI芯片民主化）；对方独有主题新增2条：RISC-V AI芯片份额2%→10%+(2030)、中国受ARM授权限制加速替代
- **price_conduction**: 5 → 6 条。将对方"授权成本从$10M+降至$0"吸收进本方第1条、"更多玩家进入"并入第3条；并入对方独有主题：加速AI芯片商业化、推理芯片价格下降→AI推理成本持续降低
- **sources**: 4 → 5 条。RISC-V International 2025 Summit 与对方《2025生态报告》同源合并为一条并补入摘要（全球SoC出货超50亿颗）；并入 芯原股份2025年报（RISC-V IP授权国内第一，Chiplet+UCIe+RISC-V三合一平台）
- **companies**: 2 → 4 家。并入 北京君正(300223,20)、兆易创新(603986,15)；共有公司 芯原股份/BABA 沿用本方 rev
- **wikilinks**: 2 → 7 条。并入 AI芯片设计(Fabless)、CPU(服务器级)、FPGA、EDA与IP核、晶圆代工(先进制程)、Chiplet与异构集成；**key_inputs**: 2 → 2 条；**key_customers**: 1 → 4 条（并入 AI芯片设计(Fabless)、CPU(服务器级)、FPGA）
- **competition**: global 4 → 4 条（Tenstorrent 补入 Chiplet+Blackhole/Ascalon，Esperanto 补入 ET-SoC-1；对方把"阿里平头哥"列在 global，本方归位到 china）；china 4 → 4 条（阿里平头哥补入 C910/C920 与生态推动者定位、中科院香山并入包云岗团队/学术→产业转化、芯来科技补入 Nuclei/对标SiFive、赛昉科技沿用）
- **barriers**: 3 → 5 条（软件生态条目并入 Toolchain/OS/Driver 现状；并入 高性能RISC-V核设计、AI加速扩展(RVV Vector 1.0)）；**tech_gap**: 1 → 2 条（并入 中国差距最小/同一代起跑线、中国芯片的「Plan B」）
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
