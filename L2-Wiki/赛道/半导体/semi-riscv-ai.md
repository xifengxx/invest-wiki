---
name: RISC-V AI芯片
slug: semi-riscv-ai
industry: 半导体
layer: L4
tam_bn: 2.5
cagr_pct: 45.0
margin: 40-55%
cost_share_pct: 2
cost_share_context: AI芯片总市场
profit_pool_pct: 1
profit_pool_context: RISC-V降低授权成本→利润从ARM/x86向Fabless+Foundry转移
value_add: high
updated: 2026-07
type: segment
tags:
- 半导体
- L4
competition:
  global:
  - name: Tenstorrent
    share: 美国
    note: Jim Keller领衔，RISC-V+Chiplet AI芯片，Blackhole/Ascalon架构
  - name: Esperanto
    share: 美国
    note: 千核RISC-V AI推理芯片（ET-SoC-1）
  - name: 阿里平头哥
    share: 中国
    note: 玄铁C910/C920系列（RISC-V兼容），中国RISC-V生态核心推动者
  china:
  - name: 芯来科技
    share: 中国RISC-V IP厂商（Nuclei芯来），对标SiFive
    note: ''
  - name: 中科院包云岗团队
    share: 香山处理器（开源高性能RISC-V），学术→产业转化
    note: ''
  barriers:
  - item: RISC-V软件生态(Toolchain/OS/Driver)
    detail: GCC/LLVM/Linux支持日趋成熟但仍有差距
  - item: 高性能RISC-V核设计
    detail: 超标量/乱序执行/OoO设计极复杂
  - item: AI加速扩展(RVV Vector 1.0)
    detail: RISC-V向量扩展是AI推理的核心竞争力
  tech_gap:
  - dimension: 中国RISC-V生态全球最活跃，差距最小（同一代起跑线）。RISC-V是地缘政治格局下中国芯片最关键的「Plan B」
    detail: ''
key_trends:
- title: RISC-V AI芯片份额2%→10%+(2030)
  detail: 开源ISA+AI推理需求+地缘政治三重驱动
- title: 中国受ARM授权限制→加速RISC-V替代
  detail: ARM不给中国公司授权v9架构→RISC-V成唯一选择
- title: Tenstorrent用Chiplet+RISC-V打造AI芯片
  detail: Jim Keller的「前苹果/AMD/Tesla芯片之神」光环
- title: RISC-V+ASIC降低芯片设计门槛→更多创业公司进入→AI芯片民主化
  detail: ''
price_conduction:
- RISC-V免费开放
- 芯片设计授权成本从$10M+(ARM架构许可+版税)降至$0
- 大幅降低AI芯片创业门槛
- 更多玩家进入
- 加速AI芯片商业化
- 推动推理芯片价格下降
- AI推理成本持续降低
wikilinks:
- AI芯片设计(Fabless)
- CPU(服务器级)
- FPGA
- EDA与IP核
- 晶圆代工(先进制程)
- Chiplet与异构集成
key_inputs:
- 晶圆代工(先进制程)
- EDA与IP核
key_customers:
- AI芯片设计(Fabless)
- CPU(服务器级)
- FPGA
companies:
- ticker: '688521'
  name: 芯原股份
  role: 国产替代
  rev: 25
- ticker: '300223'
  name: 北京君正
  role: 国产替代
  rev: 20
- ticker: '603986'
  name: 兆易创新
  role: 国产替代
  rev: 15
- ticker: BABA
  name: 阿里巴巴(平头哥)
  role: 国产龙头
  rev: 10
sources:
- title: RISC-V International《2025生态报告》
  summary: 全球RISC-V SoC出货超50亿颗，AI推理与边缘计算成最大增量
  url: https://riscv.org
- title: 芯原股份2025年报
  summary: RISC-V IP授权国内第一，Chiplet+UCIe+RISC-V三合一平台
  url: https://www.verisilicon.com
---

# RISC-V AI芯片

> **半导体** · L4 · TAM **$2.5B** · CAGR **45%**

RISC-V是一个**开源指令集架构（ISA）**——任何人可以免费使用和修改，不像x86（Intel/AMD专有）或ARM（高昂授权费+地缘政治限制）。|在AI芯片领域，RISC-V让创业公司以极低成本设计AI加速器（无ISA授权费，$0 vs ARM $10M+）。**Tenstorrent（Jim Keller领衔，RISC-V+Chiplet AI芯片）和Esperanto（千核RISC-V AI推理）是两大标杆**。|**中国RISC-V生态全球最活跃**——阿里平头哥玄铁(C910/C920系列)、中科院包云岗团队（香山处理器）、芯来科技。RISC-V AI芯片份额从近乎零(2023)→~2%(2025)→预计10%+(2030)。中国受ARM授权限制（美国制裁）→加速RISC-V替代，地缘政治是最大催化剂。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $2.5B |
| 年复合增长率(CAGR) | 45% |
| 利润率区间 | 40-55% |
| 成本占比 | 2% (AI芯片总市场) |
| 利润池占比 | 1% (RISC-V降低授权成本→利润从ARM/x86向Fabless+Foundry转移) |
| 附加值 | high |

## 关联

（待补充）
