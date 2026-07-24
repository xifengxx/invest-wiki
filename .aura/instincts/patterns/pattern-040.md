---
id: pattern-040
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
    h+='</div></div>';
  }

  // 供应链明细（详细列表视图，补充图谱）
  var hasDetailRelations = (c.suppliers&&c.suppliers.length>0)||(c.customers&&c.customers.length>0)||(c.partners&&c.partners.length>0);
  if(hasDetailRelations){
    h+='<div class="card"><div class="card-title">供应链明细</div>';
```

## 태그
