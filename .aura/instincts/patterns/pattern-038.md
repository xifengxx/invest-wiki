---
id: pattern-038
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: smic.md (Edit 완료)

## 핵심 코드
```unknown
one_liner: "中国最大晶圆代工厂，提供14nm/7nm(N+2)制程代工服务，通过晶圆代工费实现盈利，位于半导体L2制造层——中国半导体制造自主可控核心"
chain_layer: L3
chain_role: 龙头
suppliers:
  - company: "ASML"
    ticker: "ASML"
    supplies: "DUV光刻机"
    note: "EUV受出口管制无法采购"
  - company: "应用材料"
    ticker: "AMAT"
    supplies: "沉积/刻蚀设备"
  - company: "北方华创"
    supplies: "国产刻蚀/沉积设备"
    note: "国产替代"
customers:
  - company: "华为"
    note: "昇腾/鲲鹏芯片代工(受制裁限制)"
  - company: "高通"
    ticker: "QCOM"
    note: "成熟制程PMIC代工"
  - company: "国产Fabless厂商"
    note: "WiFi/Bluetooth/MCU芯片"
partners:
  - company: "华为"
    area: "先进制程联合攻坚"
  - company: "北方华创"
    area: "国产设备验证导入"
competitors:
  - company: "台积电"
    ticker: "TSM"
    area: "晶圆代工"
    note: "制程落后5-7年(14nm vs 3nm)"
  - company: "UMC"
    ticker: "UMC"
    area: "成熟制程代工"
```

## 태그
