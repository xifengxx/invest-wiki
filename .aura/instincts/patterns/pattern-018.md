---
id: pattern-018
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: hbm.md (Write 완료)

## 핵심 코드
```unknown
---
name: "HBM高带宽内存"
slug: "hbm"
type: "concept"
category: "技术"
difficulty: "中级"
confidence: "高"
one_liner: "将多个DRAM芯片垂直堆叠封装，通过硅通孔连接，让GPU能更快读写数据的超高带宽内存"
fable_title: "快递驿站升级版——从1个窗口到12层楼同时装卸"
affected_segments: ["hbm-memory", "gpu", "cowos-advanced-packaging", "ai-server"]
affected_companies: ["sk-hynix", "samsung-elec", "micron", "tsmc"]
heat: "高热"
tags: ["AI芯片", "先进封装", "存储", "HBM", "GPU"]
related_concepts:
  - slug: "cowos"
    relation: "HBM通过CoWoS封装与GPU互联，是AI芯片的物理瓶颈"
  - slug: "chiplet"
    relation: "Chiplet架构依赖HBM提供高带宽内存池"
  - slug: "asic"
    relation: "ASIC同样依赖HBM解决内存带宽瓶颈"
  - slug: "tsv"
    relation: "TSV硅通孔是HBM的核心制造工艺"
updated: "2026-07"
wikilinks: ["CoWoS先进封装", "GPU", "Chiplet与异构集成", "ASIC/AI定制芯片", "AI服务器", "光模块"]
---

# HBM · 高带宽存储

> **将多个DRAM芯片垂直堆叠、通过硅通孔连接、封装在GPU旁的"超级内存"** | 技术 · 中级

---

## 一、生活化类比：快递驿站升级版——从1个窗口到12层楼同时装卸

村里老王开了个快递驿站,生意越做越大。最早只有一个窗口,货车来了只能一辆一辆排队卸货——这就是传统DRAM内存：单层芯片,64-bit数据通道,一次只能传一点数据。

后来老王把驿站改成了12层大楼,每层都有独立的收发窗口和电梯直达。货车(相当于GPU)直接开进装卸区,同时从12层楼装货卸货,速度提升了24倍——这就是HBM：**把8-12层DRAM芯片3D堆叠在一起,用硅通孔(TSV)像电梯一样垂直连接各层,1024-bit超宽数据通道让GPU能瞬间读写海量数据。**

**对应关系：**

| 比喻中的元素 | 对应的技术/产业元素 |
|-------------|------------------|
| 快递包裹 | DRAM存储颗粒(数据单元) |
| 12层大楼 | HBM的8-12层DRAM垂直堆叠 |
| 楼层之间的电梯 | TSV硅通孔(垂直互联通道) |
| 每层的收发窗口 | 1024-bit宽总线(一个时钟周期传1024位) |
| 收货卡车 | GPU(AI训练需要海量数据吞吐) |
| 24倍速度提升 | HBM3E带宽1.2TB/s vs DDR5约50GB/s |

---
```

## 태그
