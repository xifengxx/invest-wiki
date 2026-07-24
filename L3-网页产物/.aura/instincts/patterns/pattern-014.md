---
id: pattern-014
category: test
language: unknown
score: 50
tags: [test]
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
function updateStatsBar(){
  if(!DATA) return;
  var tc=DATA.by_type;
  var stEl=document.getElementById('st');
  if(stEl) stEl.innerHTML='<span>'+DATA.total+'词条</span> · <span>'+tc.segment+'赛道</span> · <span>'+tc.company+'公司</span> · <span>'+(tc.concept||0)+'概念</span> · <span>'+(tc.thesis||0)+'论点</span>';
  updateChartStats();
}
```

## 태그
- test