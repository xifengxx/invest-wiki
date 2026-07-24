---
id: pattern-020
category: test
language: unknown
score: 50
tags: [test]
---

## 컨텍스트
파일: cpo.md (Write 완료)

## 핵심 코드
```unknown
---
name: "CPO共封装光学"
slug: "cpo"
type: "concept"
category: "技术"
difficulty: "高级"
confidence: "中"
one_liner: "把光模块和交换芯片封装在同一基板上，让光信号直接进出芯片，数据中心互联功耗降低30%、带宽翻5倍"
fable_title: "把邮局搬到小区楼下——信件不用跑半个城去寄了"
affected_segments: ["optical-transceiver", "network-switch", "dsp-optical-chip", "gpu"]
affected_companies: ["broadcom", "nvidia", "marvell", "coherent", "lumentum"]
heat: "趋势"
tags: ["光通信", "数据中心", "CPO", "硅光", "AI基础设施"]
related_concepts:
  - slug: "optical-module"
    relation: "CPO是传统可插拔光模块的下一代替代方案"
  - slug: "silicon-photonics"
    relation: "硅光是CPO的核心使能技术——用硅基工艺生产光学器件"
  - slug: "gpu"
    relation: "GPU集群互联是CPO的首个规模化应用场景"
updated: "2026-07"
wikilinks: ["光模块", "网络交换芯片", "DSP光芯片", "GPU"]
---

# CPO · 共封装光学

> **将光学引擎与交换芯片/GPU封装在一起,让光信号不再通过铜线「绕远路」的下一代互联技术** | 技术 · 高级

---

## 一、生活化类比：把邮局搬到小区楼下

从前寄信,每家每户写好信要走10分钟到街口邮局(相当于传统光模块插在交换机面板上),邮局分拣后再发出去——信号从交换芯片→PCB铜线→光模块→光纤,中间多次"换乘",又慢又费电。

CPO就像在每个小区楼下建了一个微型邮局(把光引擎直接封装在交换芯片旁边),住户(芯片信号)下楼就能寄信——光信号直接从芯片封装体进出光纤,省掉了铜线"走路"环节,功耗降低30%,速度翻5倍。

**对应关系：**

| 比喻中的元素 | 对应的技术/产业元素 |
|-------------|------------------|
| 住户/写信人 | 交换芯片/GPU(数据发送方) |
| 街口的邮局 | 传统可插拔光模块(距离5-10cm) |
| 小区楼下的微型邮局 | CPO光引擎(距离<5mm) |
| 信件 | 光信号 |
| 寄信效率翻5倍 | 带宽密度提升5倍 |
| 物业费降低 | 功耗降低约30% |

---

## 二、专业但通俗的定义
```

## 태그
- test