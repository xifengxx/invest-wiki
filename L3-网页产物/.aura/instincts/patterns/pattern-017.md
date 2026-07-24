---
id: pattern-017
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
    tooltip:{formatter:function(p){if(p.dataType==='node'){var d=p.data;return'<b>'+d.name+'</b><br>'+typeIcons[d.type]+' '+d.type+' · '+(nodes.find(function(n){return n.id===d.id;})||{}).symbolSize/3+' 关联';}return'';}},backgroundColor:'#fff',
```

## 태그
