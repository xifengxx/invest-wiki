---
id: pattern-026
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: amd.md (Edit 완료)

## 핵심 코드
```unknown
one_liner: "全球第二大x86 CPU和AI GPU厂商，设计EPYC服务器CPU+MI300系列AI加速器+FPGA，通过芯片销售实现盈利，位于AI算力L3核心产品层——挑战NVIDIA GPU垄断"
chain_layer: L3
chain_role: 龙头
suppliers:
  - company: "台积电"
    ticker: "TSM"
    supplies: "4nm/3nm晶圆代工+CoWoS封装"
    note: "唯一代工+封装伙伴"
  - company: "SK海力士"
    ticker: "000660.KS"
    supplies: "HBM3E"
    note: "MI300X搭载HBM"
  - company: "通富微电"
    ticker: "002156.SZ"
    supplies: "封测服务"
    note: "AMD CPU/GPU主要封测伙伴"
customers:
  - company: "Microsoft Azure"
    ticker: "MSFT"
    note: "MI300X部署于Azure AI实例"
  - company: "Meta"
    ticker: "META"
    note: "EPYC CPU用于基础设施"
  - company: "Oracle Cloud"
    ticker: "ORCL"
    note: "MI300X GPU租赁"
partners:
  - company: "台积电"
    ticker: "TSM"
    area: "制程+CoWoS封装"
  - company: "Xilinx"
    area: "FPGA自适应计算"
    note: "AMD全资子公司"
competitors:
  - company: "NVIDIA"
    ticker: "NVDA"
    area: "AI GPU"
    note: "MI300X推理性能接近H100，训练仍有差距"
  - company: "Intel"
    ticker: "INTC"
    area: "x86 CPU"
    note: "EPYC在服务器CPU市占率持续提升"
```

## 태그
