---
name: EDA与IP核
slug: eda-ip
industry: AI算力
layer: L2
tam_bn: 18.0
cagr_pct: 14.0
margin: 80%+
cost_share_pct: 3
cost_share_context: 芯片设计成本（半导体口径：5%）
profit_pool_pct: 15
profit_pool_context: 芯片设计利润池（半导体口径：20%，芯片设计工具利润池，Synopsys/Cadence双寡头，毛利率60-75%）
value_add: high
updated: 2026-07
type: segment
tags:
- AI算力
- L2
competition:
  global:
  - name: Synopsys
    share: ~32%
    note: 美国，#1 EDA，收购Ansys强化仿真；FY2025营收$9.56B(含Ansys)，积压$11.4B，100%先进节点份额，AgentEngineer用LLM/Agentic AI做设计
  - name: Cadence
    share: ~29%
    note: 美国，#2；营收$5.3B，积压$7.8B，硬件仿真55-60%份额
  - name: Siemens EDA
    share: '-'
    note: 美国/德国，#3，营收$2.2-2.5B
  china:
  - name: IP市场：ARM
    share: '-'
    note: 英国，处理器IP#1，99%手机使用
  - name: Synopsys
    share: '-'
    note: 接口IP#1，PCIe/DDR/USB, Alphawave Semi
  - name: 华大九天
    share: '-'
    note: 301269 国产EDA#1，模拟+平板显示全流程，数字EDA追赶中
  - name: 国微集团
    share: '-'
    note: 国产EDA，硬件仿真
  - name: 芯华章
    share: '-'
    note: 数字验证EDA
  barriers:
  - item: 全流程工具链完整性
    detail: 从RTL→GDSII全流程覆盖极难
  - item: Foundry认证IP库
    detail: TSMC/Samsung PDK认证周期2-3年
  - item: AI驱动设计效率5x提升
    detail: Synopsys AgentEngineer用LLM+Agentic AI自动化设计
  tech_gap:
  - dimension: 中国EDA国产化率~15%，全流程差距10年+。但点工具（华大九天模拟EDA）在成熟制程有突破。中国EDA并购整合加速
    detail: ''
key_trends:
- title: AI驱动芯片设计(Synopsys.ai)→效率提升5倍
  detail: AI辅助布局布线、时序优化、功耗分析正在改变芯片设计范式；Synopsys AgentEngineer用LLM/Agentic AI自动化设计，AI-EDA增速~20% CAGR
- title: Chiplet/UCIe标准→IP互联需求爆发
  detail: 异构集成需要标准化的die-to-die接口IP，Alphawave在UCIe IP领域领先
- title: RISC-V IP挑战ARM生态
  detail: SiFive和Andes的RISC-V IP在IoT和AI加速领域快速增长
- title: 中国EDA自给率从5%向15%提升
  detail: 华大九天(301269)国内#1，概伦电子进入台积电OIP联盟；并购整合加速补齐全流程，国产化率目标15%→30%+
- title: 超大规模客户(GPU/TPU/AI ASIC)贡献EDA 45%需求
  detail: 5年前几乎为零
- title: 3nm/2nm工具价格是28nm的3-5x
  detail: 先进制程设计成本$500M+→只有大公司能负担
price_conduction:
- EDA和IP核占芯片设计成本<5%但不可或缺。三巨头CR3>85%份额，95%+客户留存率，Synopsys/Cadence年涨价3-7%+AI溢价20%
- 芯片设计成本微增
- 对大型芯片公司（NVIDIA/Apple）影响极小
- 但对小型设计公司构成成本压力
- 芯片设计成本持续上升。3nm工具价格是28nm的3-5倍
- 先进芯片设计门槛急剧提高（$500M+流片成本），只有大公司能负担先进制程设计
- 行业集中度提升。中国EDA国产化率~15%
- 依赖进口+出口管制风险
wikilinks:
- GPU
- AI芯片设计(Fabless)
- IC设计服务(Fabless)
key_customers:
- GPU
companies:
- ticker: '301269'
  name: 华大九天
  role: 二线弹性
  rev: 95
- ticker: CDNS
  name: Cadence
  role: 龙头
  rev: 85
- ticker: SNPS
  name: Synopsys
  role: 龙头
  rev: 80
- ticker: NVDA
  name: NVIDIA
  role: 概念股
  rev: 5
- ticker: '688206'
  name: 概伦电子
  role: 国产替代
  rev: 45
key_inputs:
- 晶圆代工(先进制程)
- 成熟制程代工
sources:
- title: Synopsys FY2025 Annual Report
  summary: ''
  url: https://www.synopsys.com
- title: Cadence FY2025
  summary: ''
  url: https://www.cadence.com
- title: SemiAnalysis《EDA Market Primer 2025》
  summary: ''
  url: https://www.semianalysis.com
- title: 华大九天2025年报
  summary: ''
  url: ''
- title: ESD Alliance《全球EDA市场2025》
  summary: Synopsys+Cadence占全球70%+，华大九天国内市占率第一，AI驱动EDA效率革命
  url: https://www.semi.org
---

# EDA与IP核

> **AI算力** · L2 · TAM **$18B** · CAGR **14%**

**EDA是芯片设计的「操作系统」**——从架构设计到物理验证全流程自动化。没有EDA，设计千亿晶体管AI芯片不可能。|**全球EDA+IP市场~$18B(2025)，三巨头CR3>85%**：Synopsys(FY2025含Ansys $9.56B,积压$11.4B,100%先进节点份额)、Cadence($5.3B,积压$7.8B,硬件仿真55-60%份额)、Siemens EDA($2.2-2.5B)。3nm工具价格是28nm的3-5x，95%+客户留存，3-7%年涨价+AI溢价20%。|**AI-EDA增速~20% CAGR**——Synopsys AgentEngineer用LLM/Agentic AI将设计效率提升5倍。超大规模客户(GPU/TPU/AI ASIC)贡献EDA 45%需求，5年前几乎为零。**IP核是预先设计好、经过验证的可复用电路模块**——现代SoC设计越来越像「搭乐高」，CPU核(ARM)、GPU核、DDR/HBM PHY、PCIe SerDes都是可购买的IP模块。中国华大九天(301269)国产EDA#1，但全流程差距10年+。

---

## 核心数据

| 指标 | 数值 |
|------|------|
| 市场规模(TAM) | $18B |
| 年复合增长率(CAGR) | 14% |
| 利润率区间 | 80%+ |
| 成本占比 | 3% (芯片设计成本)〔半导体口径：5%〕 |
| 利润池占比 | 15% (芯片设计利润池)〔半导体口径：20% 芯片设计工具利润池，双寡头毛利率60-75%〕 |
| 附加值 | high |

## 关联

（待补充）

## 动态更新记录

### 更新 2026-07-22 (v1.1)
> 来源: Refinement链接增强
> 置信度: 高

- **wikilinks**: 增强 — wikilinks从5→10条

### 更新 2026-09-13（合并 semi-eda-ip 重复档案）
> 来源: 重复赛道合并（原 L2-Wiki/赛道/半导体/semi-eda-ip.md）
> 置信度: 高

- **指标**: 以本方（有变更记录的正本）为准；tam_bn 双方一致（$18B）；本方 cagr 14% / margin 80%+ / value_add high 保留（对方 cagr 13% / margin 60-75% / value_add very high）
- **口径保留**: cost_share / profit_pool 的半导体口径（5% / 20% 芯片设计工具利润池，Synopsys-Cadence双寡头毛利率60-75%）并入 context 备注明细，两个视角并存
- **key_trends**: 4 → 6 条。将对方"AI-EDA 20% CAGR + AgentEngineer"的具体表述吸收进本方第1条；将对方"国产化率目标15%→30%+、并购整合"吸收进本方第4条；对方独有主题新增2条：超大规模客户(GPU/TPU/AI ASIC)贡献EDA 45%需求、3nm/2nm工具价格是28nm的3-5x
- **price_conduction**: 4 → 8 条。将对方"三巨头CR3>85%、95%+客户留存率、年涨价3-7%+AI溢价20%"吸收进本方第1条；并入对方独有主题：芯片设计成本持续上升(3nm=28nm的3-5x)、先进设计门槛提高($500M+流片成本)、行业集中度提升/中国国产化率~15%、依赖进口+出口管制风险
- **sources**: 4 → 5 条。并入 ESD Alliance《全球EDA市场2025》（含 Synopsys+Cadence 占全球70%+ 摘要）
- **companies**: 4 → 5 家。并入 概伦电子(688206,45)；共有公司 SNPS/CDNS/华大九天 沿用本方 rev
- **wikilinks**: 3 → 3 条（对方仅 GPU，本方已覆盖）；**key_inputs**: 1 → 2 条（并入 成熟制程代工）；**key_customers**: 1 → 1 条
- **competition**: global 2 → 3 条（补齐 Siemens EDA 独立条目；Synopsys 并入 FY2025 $9.56B/积压$11.4B/100%先进节点/AgentEngineer、Cadence 并入 $5.3B/积压$7.8B/硬件仿真55-60%份额）；china 2 → 5 条（IP市场：ARM、接口IP Synopsys 之外，并入 华大九天(301269)、国微集团、芯华章）
- **barriers**: 0 → 3 条（并入 全流程工具链完整性、Foundry认证IP库、AI驱动设计效率5x提升）；**tech_gap**: 0 → 1 条（并入 中国国产化率~15%、全流程差距10年+、点工具突破、并购整合加速）
- **依据**: 两份档案自 init 起独立演进，本方为维护中的正本；对方含本方缺失的研究内容，按"保留原文+追加"规则合并
