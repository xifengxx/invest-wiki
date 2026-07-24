---
id: pattern-008
category: security
language: unknown
score: 50
tags: [security]
---

## 컨텍스트
파일: index.html (Edit 완료)

## 핵심 코드
```unknown
.search{flex:1;max-width:480px;display:flex;align-items:center;background:var(--bg);border-radius:20px;padding:7px 16px;gap:8px;height:38px;border:1px solid transparent;transition:all .2s;}
.search:focus-within{background:var(--card);border-color:var(--accent);box-shadow:0 0 0 3px rgba(0,113,227,0.1);}
.search input{border:none;background:transparent;outline:none;flex:1;font-size:14px;color:var(--text);font-family:inherit;}
.search .s-icon-search{color:var(--text2);font-size:15px;flex-shrink:0;}
/* List view search */
.list-search-wrap{margin-bottom:20px;}
.list-search{width:100%;display:flex;align-items:center;background:var(--bg);border-radius:12px;padding:10px 16px;gap:10px;border:1px solid transparent;transition:all .2s;}
.list-search:focus-within{background:var(--card);border-color:var(--accent);box-shadow:0 0 0 3px rgba(0,113,227,0.08);}
.list-search input{border:none;background:transparent;outline:none;flex:1;font-size:14px;color:var(--text);font-family:inherit;}
.list-search .ls-icon{color:var(--text2);font-size:16px;flex-shrink:0;}
.hot-tags{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-top:10px;}
.hot-tag{padding:4px 12px;border-radius:12px;font-size:12px;font-weight:500;cursor:pointer;border:1px solid var(--border);background:var(--card);color:var(--text2);transition:all .15s;font-family:inherit;}
.hot-tag:hover{border-color:var(--accent);color:var(--accent);background:rgba(0,113,227,0.04);}
/* Knowledge dashboard */
.kb-two-col{display:flex;gap:16px;margin-bottom:16px;}
.kb-left{width:280px;flex-shrink:0;}
.kb-right{flex:1;}
.kb-tree-item{padding:7px 12px;cursor:pointer;border-radius:8px;font-size:12px;transition:all .15s;display:flex;align-items:center;gap:6px;}
.kb-tree-item:hover{background:var(--hover);}
.kb-tree-item.active{background:var(--active);color:var(--accent);font-weight:600;}
.kb-tree-folder{font-weight:600;color:var(--accent);font-size:13px;padding:5px 8px;}
.kb-tree-l1{padding-left:4px;}
.kb-tree-l2{padding-left:20px;font-size:12px;}
.kb-tree-l3{padding-left:36px;color:var(--text2);font-size:11px;}
.kb-tree-l4{padding-left:52px;color:#C7C7CC;font-size:10px;}
.quality-table{width:100%;border-collapse:collapse;font-size:13px;margin-top:10px;}
.quality-table th{text-align:left;padding:8px 12px;font-size:11px;font-weight:600;color:var(--text2);text-transform:uppercase;letter-spacing:0.03em;border-bottom:2px solid var(--border);background:var(--bg);}
.quality-table td{padding:8px 12px;border-bottom:1px solid var(--border);}
.quality-table tr:hover td{background:var(--bg);}
.status-dot{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:6px;}
.status-active{background:#0071E3;}
.status-forming{background:#86868B;}
.status-confirmed{background:#34C759;}
.status-invalidated{background:#FF3B30;}
```

## 태그
- security