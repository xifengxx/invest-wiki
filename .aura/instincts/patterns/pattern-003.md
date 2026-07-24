---
id: pattern-003
category: general
language: unknown
score: 50
tags: []
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
  // 6. Trends — DeZine v3: title + 2-line description
  if(cs.key_trends){
    h+='<div class="card"><div class="card-title">关键趋势</div>';
    var allTrends=(cs.key_trends||'').split('|').filter(Boolean);
    allTrends.forEach(function(t){
      var txt=t.trim().replace(/^\d+\)\s*/,''); // remove leading "1) "
      // Split title from description by ——
      var sep=txt.indexOf('——');
      var title, desc;
      if(sep>0){
        title=txt.substring(0,sep).trim();
        desc=txt.substring(sep+2).trim();
      } else {
        // No ——: first sentence is title
        var dot=txt.search(/[。，,\.]/);
        if(dot>0&&dot<30){title=txt.substring(0,dot).trim();desc=txt.substring(dot+1).trim()||txt;}
        else{title=txt.substring(0,Math.min(30,txt.length)).trim();desc=txt;}
      }
      if(title.length>40) title=title.substring(0,40)+'…';
      if(desc.length>140) desc=desc.substring(0,140)+'…';
      h+='<div class="trend-card"><div class="trend-title">'+title+'</div><div class="trend-desc">'+desc+'</div></div>';
    });
    h+='</div>';
  }
```

## 태그
