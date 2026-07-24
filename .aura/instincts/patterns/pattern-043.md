---
id: pattern-043
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
// Stats bar only (right panel removed)
(function(){
  var tc=DATA.by_type;
  var stEl=document.getElementById('st');
  if(stEl) stEl.innerHTML='<span>'+DATA.total+'词条</span> · <span>'+tc.segment+'赛道</span> · <span>'+tc.company+'公司</span> · <span>'+(tc.concept||0)+'概念</span> · <span>'+(tc.thesis||0)+'论点</span>';
})();
```

## 태그
