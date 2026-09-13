---
name: Cruise
slug: cruise
country: US
type: company
updated: 2026-09
data_freshness_date: 2026-09-13
segments:
- 自动驾驶
one_liner: |
  通用汽车（GM）旗下的自动驾驶技术公司，其Robotaxi业务已于2024年12月被GM停止资助、2025年2月完成全资收购，独立品牌实质退役——当前业务已转为在GM体系内专注高级驾驶辅助系统（ADAS）与个人车辆自动驾驶，不再运营无人驾驶出行服务。
  【2026.9.13状态修正】Cruise **已不再是Robotaxi运营商**。GM于2024-12宣布退出robotaxi并停止资助，2025-02完成100%收购并裁员约50%（~1,000人）；工程团队并入GM的ADAS组织，品牌转为Super Cruise产品线。GM累计投入超$100亿而Cruise收入不到$5亿，重组预计年省超$10亿。
chain_layer: L4
chain_role: 间接相关
suppliers:
- company: 通用汽车（GM）
  ticker: GM
  supplies: 母公司资源（100%持股）
  note: 2025年2月完成全资收购
- company: 激光雷达与传感器供应商
  supplies: LiDAR、摄像头、毫米波雷达
- company: 芯片供应商
  supplies: 自动驾驶计算芯片
customers:
- company: 通用汽车（GM）
  ticker: GM
  note: 技术输出至GM的Super Cruise驾驶辅助产品线
- company: GM 个人车辆用户
  note: 通过Super Cruise间接服务
partners:
- company: 通用汽车（GM）
  ticker: GM
  area: 母公司（100%持股），工程团队并入GM ADAS组织
competitors:
- company: Waymo
  ticker: GOOGL
  area: Robotaxi
  note: 同一时期Waymo周订单50万+、估值$1,260亿——成败分野明确
- company: Tesla
  ticker: TSLA
  area: FSD/自动驾驶
- company: Mobileye
  ticker: MBLY
  area: ADAS
  note: GM Super Cruise 的ADAS竞争领域
- company: 百度 Apollo Go
  ticker: 9888.HK
  area: Robotaxi（中国）
- company: Zoox（Amazon）
  ticker: AMZN
  area: Robotaxi
core_business:
- 高级驾驶辅助系统（ADAS）研发——在GM体系内
- 个人车辆自动驾驶技术
- 技术输出至 GM 的 Super Cruise 产品线
- 原 Robotaxi 业务（已于2024年12月终止）
revenue_model: 无独立的Robotaxi业务收入。Cruise 的工程能力现作为 GM 内部技术资产存在，不单独产生对外收入。历史上 GM 在 Cruise 上累计花费超过$100亿，而 Cruise 累计产生收入不到$5亿——投入产出比约 20:1 的倒挂。
founded: 2013
headquarters: 美国加州旧金山
latest_revenue: 不适用（Robotaxi业务已终止；历史累计收入不足$5亿）
market_cap: 不适用（GM 100%持股的全资子公司）
description: Cruise 2013年成立于旧金山，曾是通用汽车旗下最重要的自动驾驶子公司。2023年发生行人拖拽事件后，加州暂停其无人驾驶许可；2024年12月GM宣布停止资助Cruise的robotaxi部门并退出robotaxi业务，2025年2月完成100%股权收购并裁员约50%。公司独立品牌实质退役，工程团队并入GM的驾驶辅助组织，专注ADAS与个人车辆自动驾驶。
website: https://www.getcruise.com
industry: AI算力
---

# Cruise

**这是一家已经不存在 Robotaxi 业务的公司。** GM 花了超过 100 亿美元、换来不到 5 亿收入，最终在 2024 年 12 月退出 robotaxi，2025 年 2 月完成全资收购并裁掉一半员工。工程团队并入 GM 的 ADAS 组织，品牌转为 Super Cruise——从 L4 梦想退回 L2+ 现实。

> ⚠️ **词条状态修正说明**：本词条在骨架阶段被列为 Robotaxi 运营商。经核实，**Cruise 已于 2024年12月被 GM 停止资助、2025年2月完成全资收购、品牌实质退役，当前无活跃的 robotaxi 服务**。本次升级按实际情况重建。

## 财务状况

> **不再适用常规财务分析**——Cruise 的 Robotaxi 业务已终止，公司作为 GM 全资子公司在GM体系内运作，不单独披露财报。

### 历史财务代价

| 指标 | 值 |
|------|-----|
| GM 在 Cruise 上累计花费 | **超过 $100亿** |
| Cruise 累计产生收入 | **不到 $5亿** |
| **投入产出比** | **约 20:1 的倒挂** |
| 重组预计年节省 | **超过 $10亿** |

#### 财务特征

**这是自动驾驶行业最重要的失败案例之一**：$100亿的投入换来不到$5亿的收入，意味着 GM 在这项业务上的净损失可能接近 **$100亿量级**。GM 管理层最终选择将资源转向更务实的 L2+/L3 驾驶辅助，预计重组每年节省超$10亿。

## 关键时间线

| 时间 | 事件 |
|------|------|
| **2023** | **行人拖拽事件** + **加州暂停 Cruise 无人驾驶许可**——关键转折 |
| **2024-12** | **GM 宣布停止资助 Cruise 的 robotaxi 部门并退出 robotaxi**，理由是规模化所需的时间、资源与竞争 |
| **2025-02** | GM 完成对 Cruise 剩余股份的收购，取得 **100% 所有权**；**裁员约50%（~1,000个岗位）**，保留多数技术岗位并并入 GM 驾驶辅助组织 |
| **截至2026** | Cruise **不再运营 robotaxi 服务**；**独立品牌已实质退役**，转为 GM 的 **Super Cruise** 产品线 |

## 当前实际业务

| 项 | 内容 |
|----|------|
| Cruise 工程团队 | 继续在 **GM 旗下**，专注 **高级驾驶辅助系统（ADAS）与个人车辆自动驾驶**，**而非 robotaxi 运营** |
| GM 战略方向 | 转向**个人车辆的部分自动驾驶辅助系统**（如 Super Cruise） |
| **时间表** | 计划 **2028年实现 eyes-off（脱眼）高速公路驾驶** |
| 未来可能性 | GM 首席产品官称个人车辆自动驾驶技术**最终可能与 robotaxi 应用融合**；已重新聘用部分前 Cruise 员工，但**目前无活跃的 robotaxi 服务** |
| **本田退出** | 已退出与 GM/Cruise 原定的 **2026年东京 robotaxi 合资项目** |

## 行业对照

| 公司 | 状态（2026） |
|------|-------------|
| **Waymo** | 周付费订单50万+，估值 **$1,260亿**，覆盖美国10+城市并进军伦敦/东京 |
| **Cruise** | **robotaxi业务关闭**，品牌退役，技术并入GM的ADAS |
| Tesla | FSD 持续迭代，Robotaxi 计划推进中 |

**两家公司在同一时期、同一技术赛道上的分野，是"重资产自建运营"与"渐进式技术输出"两种路线成败的直接检验。**

## 技术路线图

| 方向 | 状态 | 时间 |
|------|------|------|
| **ADAS（在GM体系内）** | 工程团队已并入 | 2026+ |
| **Super Cruise** | GM 的L2+驾驶辅助产品线 | 2026+ |
| **eyes-off 高速公路驾驶** | GM 计划 | **2028** |
| Robotaxi | **已终止** | — |

## 融资与现金流

- **无独立融资能力**——GM 100%持股的全资子公司
- GM 的历史投入超过 **$100亿**，收入不到 **$5亿**
- 重组（裁员50%）预计年节省 **超过$10亿**
- 本田退出东京robotaxi合资项目，相关投入终止

## 研发投入与专利

- **剩余价值**：
  1. **工程团队与自动驾驶技术积累**——并入GM后继续服务ADAS开发
  2. 部分专利与数据资产（但2023年事故严重损害了其数据的公信力）
  3. GM 已重新聘用部分前 Cruise 员工
- **失败的核心原因**：
  1. **2023年行人拖拽事件**——直接导致加州暂停许可，摧毁了监管与公众信任
  2. **重资产自建运营模式的成本失控**——$100亿投入对应不到$5亿收入
  3. **规模化难度被严重低估**——GM 明确表示规模化所需的时间、资源与竞争超出预期
  4. **与Waymo的竞争劣势**——Waymo 在技术成熟度与运营规模上全面领先

## 动态更新记录

### 2026-09-13（骨架词条升级 + 状态修正）
> 来源: [[消化笔记/2026-09-13-骨架公司补全批次]]
> L0归档: `L0-原始资料池/03-新闻/2026-09-13-Cruise-业务关闭状态核实.md` (input_20260913_055)
> 置信度: 高

- **⚠️ 状态修正（重要）**：**该词条骨架阶段将 Cruise 列为 Robotaxi 运营商，与实际情况不符**。Cruise 已于 **2024-12 被 GM 停止资助、2025-02 完成全资收购、品牌实质退役**，当前**无活跃的 robotaxi 服务**。本次升级按实际状态重建。
- **chain_role 调整**：`核心参与者` → `间接相关`（不再是独立的 robotaxi 运营商）
- **one_liner 重写**：明确说明业务已终止、当前专注 ADAS
- **latest_revenue**：空 → 不适用（历史累计收入不足$5亿）
- **market_cap**：空 → 不适用（GM 100%持股的全资子公司）
- **suppliers/customers/partners/competitors**：空数组 → 分别填充 3/2/1/5 条
- **新增关键数据**：GM累计投入超$100亿 / 收入不到$5亿、裁员约50%、重组年省超$10亿、GM计划2028年eyes-off高速驾驶
- **新增行业对照**：与 Waymo（周订单50万+、估值$1,260亿）的成败分野
