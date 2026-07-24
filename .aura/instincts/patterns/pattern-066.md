---
id: pattern-066
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: cpu-return-to-datacenter-core.md (Edit 완료)

## 핵심 코드
```unknown
## 支撑证据

1. CPU:GPU比例结构性变化——传统LLM推理以GPU为主，Agentic AI需要CPU承担大量编译+验证+Tool Use工作负载 ——来源: 中原证券《电子行业2026年中期策略》 (L0-原始资料池/01-研报/2026-06-23-电子行业2026年中期策略-中原证券.md)
2. 英伟达自身在强化CPU——Vera CPU+NVLink-C2C与GPU紧耦合，在AI服务器中占据独特位置 ——来源: NVIDIA FY2026 Annual Report (https://investor.nvidia.com)
3. 北美四大云厂商2026Q1资本开支$1,288亿(+81% YoY)，Capex CAGR 46%直接拉动CPU需求 ——来源: 中原证券《电子行业2026年中期策略》 (L0-原始资料池/01-研报/2026-06-23-电子行业2026年中期策略-中原证券.md)
4. AMD EPYC在服务器CPU市场份额持续扩大（收入份额首破41.3%），Intel 18A制程力图逆转 ——来源: Mercury Research Server CPU Share Q2 2025
5. ARM阵营快速增长——AWS Graviton已占新实例40%+，NVIDIA Grace 2025出货~2.5M颗 ——来源: NVIDIA FY2026 Annual Report (https://investor.nvidia.com)

## 反对证据

1. CPU在AI服务器中的绝对成本占比仍然远低于GPU（10% vs 55%），CPU:GPU比例变化对总市场TAM的影响可能被高估 ——来源: 当前Wiki CPU赛道数据（cost_share_pct: 10% vs GPU 55%）
2. 云厂商自研ARM CPU（AWS Graviton/谷歌Axion）可能不进入商用市场，限制独立CPU供应商的TAM ——来源: AWS re:Invent 2025 Graviton披露
3. Agentic AI仍处于早期阶段，CPU:GPU比例是否真的到达1:1尚需更多实际部署数据验证 ——来源: 中原证券2026中期策略（该报告自身也标注此为趋势判断，非确定性结论）
```

## 태그
