---
id: pattern-023
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
  nodes.forEach(function(n){var c=connCount[n.id]||0;n.symbolSize=c===0?6:Math.max(8,Math.min(55,Math.sqrt(c)*14+6));});
```

## 태그
