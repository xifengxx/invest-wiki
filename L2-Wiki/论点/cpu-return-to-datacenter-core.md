---
name: "CPU重回AI数据中心核心——Agentic AI驱动CPU:GPU比从1:8转向1:1"
slug: "cpu-return-to-datacenter-core"
type: "thesis"
thesis_status: "active"
confidence: 8
created: "2026-07-22"
updated: "2026-07-23"
affected_segments: ["server-cpu", "ai-server", "gpu"]
affected_companies: ["INTC", "AMD", "NVDA", "688041"]
tags: ["cpu", "agentic-ai", "datacenter", "structural-shift"]
---

## 动态更新记录

### 2026-07-23: Q3审计 — 置信度 7→8

Meta Agentic AI工作负载推动CPU:GPU比从1:8转向1:1、Arm 2026年3月发布自研AGI CPU与Meta联合开发、NVIDIA Grace CPU出货量超预期、Google Axion/AWS Graviton ARM服务器CPU持续渗透。新证据显著增强。

---

# CPU重回AI数据中心核心

## 核心主张

Agentic AI时代（AI智能体自主执行多步骤任务）正在根本性地改变AI数据中心的CPU:GPU配比——从传统LLM推理的1:4~1:8转向接近1:1。这意味着服务器CPU在AI基础设施中的价值量将大幅提升，CPU赛道CAGR从10%级别进入20-30%区间。Intel/AMD/英伟达三方均将受益，但NVIDIA Grace CPU因与GPU紧耦合（NVLink-C2C）占据最有利位置。

## 支撑证据

1. CPU:GPU比例结构性变化——传统LLM推理以GPU为主，Agentic AI需要CPU承担大量编译+验证+Tool Use工作负载
   ——来源: 中原证券《电子行业2026年中期策略》
   (L0-原始资料池/01-研报/2026-06-23-电子行业2026年中期策略-中原证券.md)
2. 英伟达自身在强化CPU——Vera CPU+NVLink-C2C与GPU紧耦合，在AI服务器中占据独特位置
   ——来源: NVIDIA FY2026 Annual Report
   (https://investor.nvidia.com)
3. 北美四大云厂商2026Q1资本开支$1,288亿(+81% YoY)，Capex CAGR 46%直接拉动CPU需求
   ——来源: 中原证券《电子行业2026年中期策略》
   (L0-原始资料池/01-研报/2026-06-23-电子行业2026年中期策略-中原证券.md)
4. AMD EPYC在服务器CPU市场份额持续扩大（收入份额首破41.3%），Intel 18A制程力图逆转
   ——来源: Mercury Research Server CPU Share Q2 2025
5. ARM阵营快速增长——AWS Graviton已占新实例40%+，NVIDIA Grace 2025出货~2.5M颗
   ——来源: NVIDIA FY2026 Annual Report
   (https://investor.nvidia.com)

## 反对证据

1. CPU在AI服务器中的绝对成本占比仍然远低于GPU（10% vs 55%），CPU:GPU比例变化对总市场TAM的影响可能被高估
   ——来源: 当前Wiki CPU赛道数据（cost_share_pct: 10% vs GPU 55%）
2. 云厂商自研ARM CPU（AWS Graviton/谷歌Axion）可能不进入商用市场，限制独立CPU供应商的TAM
   ——来源: AWS re:Invent 2025 Graviton披露
3. Agentic AI仍处于早期阶段，CPU:GPU比例是否真的到达1:1尚需更多实际部署数据验证
   ——来源: 中原证券2026中期策略（该报告自身也标注此为趋势判断，非确定性结论）

## 待验证假设

- Agentic AI工作负载中CPU的实际利用率vs GPU利用率
- 英伟达Grace CPU是否会被云厂商广泛采用（或仅NVIDIA DGX系统内使用）
- Intel 18A量产后的实际性能/能效能否逆转份额下滑趋势

## 来源

- 中原证券《电子行业2026年中期策略》
  Agentic AI时代CPU:GPU比例从1:8转向1:1，云厂商Capex CAGR 46%，CPU重回数据中心核心
  (L0-原始资料池/01-研报/2026-06-23-电子行业2026年中期策略-中原证券.md)
- NVIDIA FY2026 Annual Report
  FY2026数据中心$193.7B，Grace CPU出货~2.5M颗
  (https://investor.nvidia.com)
- Mercury Research Server CPU Share Q2 2025
  AMD EPYC收入份额首破41.3%，ARM服务器份额13-16%
- AMD Data Center Revenue FY2025
  AMD EPYC Turin 192核+Venice 256核路线图
