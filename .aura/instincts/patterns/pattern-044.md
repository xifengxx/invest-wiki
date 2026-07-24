---
id: pattern-044
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
function gs(ind){ if(!DATA) return []; return DATA.entities.filter(function(e){return e.type==='segment'&&e.industry===ind;}); }
function gn(n){ if(!DATA) return null; return DATA.entities.find(function(e){return e.name===n;}); }
function gl(s){ if(!DATA) return null; return DATA.entities.find(function(e){return e.slug===s;}); }
// View switching (nav items)
var currentView='chart';
function switchView(view){
  if(!DATA) return;
  currentView=view;
```

## 태그
