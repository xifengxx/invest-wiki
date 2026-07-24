---
id: pattern-001
category: ui
language: unknown
score: 50
tags: [ui]
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
  // 3. Value chain
  if(cs.cost_share_pct||cs.profit_pool_pct){
    var hasCost=cs.cost_share_pct, hasProfit=cs.profit_pool_pct;
    var descParts=[];
    if(hasCost) descParts.push('成本占比约 <b class="hl">'+hasCost+'%</b>');
    if(hasProfit) descParts.push('利润池占比约 <b class="hl">'+hasProfit+'%</b>');
    h+='<div class="card"><div class="card-title">价值链分析</div><p class="detail-body" style=margin-bottom:12px;>在'+(cs.cost_share_context||'整个产品')+'中，<b class="hl">'+cs.name+'</b>的'+descParts.join('，')+'。</p>';
    var cols=(hasCost&&hasProfit)?'1fr 1fr':'1fr';
    h+='<div style=display:grid;grid-template-columns:'+cols+';gap:16px;>';
    if(hasCost) h+='<div><div style=font-size:11px;color:var(--text2);text-transform:uppercase;margin-bottom:4px;>成本占比</div><div class="bar-track"><div class="bar-fill" style=width:'+hasCost+'%></div></div><div style=font-size:12px;color:var(--text2);margin-top:2px;>'+hasCost+'%</div></div>';
    if(hasProfit) h+='<div><div style=font-size:11px;color:var(--text2);text-transform:uppercase;margin-bottom:4px;>利润池占比</div><div class="bar-track"><div class="bar-fill" style=width:'+hasProfit+'%;background:var(--down)></div></div><div style=font-size:12px;color:var(--text2);margin-top:2px;>'+hasProfit+'%</div></div>';
    h+='</div></div>';
  }
```

## 태그
- ui