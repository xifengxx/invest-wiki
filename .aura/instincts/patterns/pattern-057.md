---
id: pattern-057
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: cpu-return-to-datacenter-core.md (Write 완료)

## 핵심 코드
```unknown
---
name: "CPU重回AI数据中心核心——Agentic AI驱动CPU:GPU比从1:8转向1:1"
slug: "cpu-return-to-datacenter-core"
type: "thesis"
thesis_status: "forming"
confidence: 7
created: "2026-07-22"
updated: "2026-07-22"
affected_segments: ["server-cpu", "ai-server", "gpu"]
affected_companies: ["INTC", "AMD", "NVDA", "688041"]
tags: ["cpu", "agentic-ai", "datacenter", "structural-shift"]
---

# CPU重回AI数据中心核心

## 核心主张

Agentic AI时代（AI智能体自主执行多步骤任务）正在根本性地改变AI数据中心的CPU:GPU配比——从传统LLM推理的1:4~1:8转向接近1:1。这意味着服务器CPU在AI基础设施中的价值量将大幅提升，CPU赛道CAGR从10%级别进入20-30%区间。Intel/AMD/英伟达三方均将受益，但NVIDIA Grace CPU因与GPU紧耦合（NVLink-C2C）占据最有利位置。

## 支撑证据

1. CPU:GPU比例结构性变化——传统LLM推理以GPU为主，Agentic AI需要CPU承担大量编译+验证+Tool Use工作负载（中原证券2026中期策略）
2. 英伟达自身在强化CPU——Vera CPU+NVLink-C2C与GPU紧耦合，在AI服务器中占据独特位置
3. 北美四大云厂商2026Q1资本开支$1,288亿(+81% YoY)，Capex CAGR 46%直接拉动CPU需求（黄仁勋预测2025-2030）
4. AMD EPYC在服务器CPU市场份额持续扩大（收入份额首破41.3%），Intel 18A制程力图逆转
5. ARM阵营快速增长——AWS Graviton已占新实例40%+，NVIDIA Grace 2025出货~2.5M颗

## 反对证据

1. CPU在AI服务器中的绝对成本占比仍然远低于GPU（10% vs 55%），CPU:GPU比例变化对总市场TAM的影响可能被高估
2. 云厂商自研ARM CPU（AWS Graviton/谷歌Axion）可能不进入商用市场，限制独立CPU供应商的TAM
3. Agentic AI仍处于早期阶段，CPU:GPU比例是否真的到达1:1尚需更多实际部署数据验证

## 待验证假设

- Agentic AI工作负载中CPU的实际利用率vs GPU利用率
- 英伟达Grace CPU是否会被云厂商广泛采用（或仅NVIDIA DGX系统内使用）
- Intel 18A量产后的实际性能/能效能否逆转份额下滑趋势

## 来源

- 中原证券《电子行业2026年中期策略》(2026-06-23)
- NVIDIA FY2026 Annual Report
- Mercury Research Server CPU Share Q2 2025
- AMD Data Center Revenue FY2025

```

## 태그
