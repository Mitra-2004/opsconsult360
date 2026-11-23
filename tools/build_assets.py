#!/usr/bin/env python3
"""Rebuild six synthetic CSV tables and the offline HTML dashboard from SQLite."""
import csv
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "sql" / "opsconsult.db"
TABLES = ("projects", "tasks", "financials", "employees", "timesheets", "actions")
assert DB.exists(), "Expected sql/opsconsult.db"
(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "dashboard").mkdir(exist_ok=True)
payload = {"asof": "2026-11-23"}
with sqlite3.connect(DB) as conn:
    conn.row_factory = sqlite3.Row
    for name in TABLES:
        columns = [r["name"] for r in conn.execute(f"pragma table_info({name})")]
        assert columns, name
        rows = [dict(r) for r in conn.execute(f"select * from {name}")]
        payload[name] = rows
        with (ROOT / "data" / f"{name}.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(rows)
(ROOT / "dashboard" / "data.json").write_text(
    json.dumps(payload, separators=(",", ":"), ensure_ascii=False), encoding="utf-8"
)
html = r"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>OpsConsult 360 | Management Intelligence</title>
<style>
:root{--ink:#1b2939;--muted:#657382;--accent:#137569;--line:#dce4e8;--bg:#f5f7f8}
*{box-sizing:border-box}body{font:14px/1.5 system-ui,-apple-system,sans-serif;color:var(--ink);background:var(--bg);margin:0}
header{background:#1a2e40;color:#fff;padding:24px 4vw}h1{margin:0;font-size:23px}h2{font-size:16px;margin:0 0 10px}small{color:var(--muted)}
header small{color:#b2c8cf}.nav{display:flex;gap:8px;flex-wrap:wrap;padding:12px 4vw;background:#fff;border-bottom:1px solid var(--line)}
main{margin:auto;max-width:1300px;padding:25px}button,select,input{font:inherit;padding:8px 10px;border:1px solid #b5c6cc;border-radius:6px;background:#fff;color:var(--ink)}
button{cursor:pointer}button:hover{border-color:var(--accent)}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #62beac;outline-offset:2px}
button[aria-pressed=true]{background:#e5f4ef;border-color:var(--accent);color:#07594f}.toolbar{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 18px}
.toolbar label{display:flex;align-items:center;gap:7px}.toolbar .right{margin-left:auto}
.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:16px}
.card,.panel{padding:16px;background:white;border:1px solid var(--line);border-radius:8px}
.card strong{display:block;font-size:23px;margin-top:5px}.panel{margin:0 0 16px}.muted{color:var(--muted)}
.tablewrap{overflow:auto}table{width:100%;border-collapse:collapse;min-width:630px}
th,td{border-bottom:1px solid #e7edef;padding:9px;text-align:left;white-space:nowrap}
th{color:var(--muted);background:#f7f9fa;font-size:12px}tr:hover td{background:#f5faf9}
.alert{color:#a23c33;font-weight:600}.badge{background:#e7f2ee;padding:2px 6px;border-radius:4px}
.detail{background:#f4fbf8;border-left:3px solid var(--accent);padding:16px;margin-top:15px}
.fields{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.fields dt{color:var(--muted);font-size:12px}.fields dd{margin:0;font-weight:600}
@media(max-width:850px){.cards{grid-template-columns:repeat(2,1fr)}}@media(max-width:500px){main{padding:15px}.cards{grid-template-columns:1fr}.fields{grid-template-columns:repeat(2,1fr)}}
</style></head><body>
<header><small>SIMULATED OPERATIONS · 23 NOV 2026</small><h1>OpsConsult 360</h1><div>Project Performance & Operations MIS</div></header>
<nav class="nav" aria-label="Report pages">
<button data-view="overview" aria-pressed="true">Executive overview</button>
<button data-view="projects" aria-pressed="false">Project delivery</button>
<button data-view="finance" aria-pressed="false">Financial analytics</button>
<button data-view="resources" aria-pressed="false">Resources & actions</button></nav>
<main><div class="toolbar"><label>Department <select id="dept"><option>All</option></select></label>
<label>Project search <input id="search" type="search" placeholder="Project ID or name"></label>
<div class="right"><button id="reset">Reset</button> <button class="primary" id="export">Export projects CSV</button></div></div>
<div id="content" aria-live="polite"></div>
<p class="muted">Synthetic data only. Costs and hours refer to sampled periods; full-project budgets are a different metric.</p></main>
<script>const DB=__DATA__;
const $=id=>document.getElementById(id),N=n=>Number(n||0),money=n=>'₹'+Math.round(n).toLocaleString('en-IN');
const escapeHTML=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const costs={};for(const r of DB.financials){const x=costs[r.project_id]??={plan:0,actual:0,revenue:0};x.plan+=N(r.planned_cost_inr);x.actual+=N(r.actual_cost_inr);x.revenue+=N(r.revenue_inr)}
let view='overview',selection=null;
for(const d of [...new Set(DB.projects.map(p=>p.department))].sort()){const e=document.createElement('option');e.textContent=d;$('dept').append(e)}
const filtered=()=>DB.projects.filter(p=>($('dept').value==='All'||p.department===$('dept').value)&&
(p.project_id.toLowerCase().includes($('search').value.toLowerCase())||p.project_name.toLowerCase().includes($('search').value.toLowerCase())));
const totals=ps=>ps.reduce((a,p)=>{const x=costs[p.project_id]||{plan:0,actual:0,revenue:0};a.plan+=x.plan;a.actual+=x.actual;a.revenue+=x.revenue;return a},{plan:0,actual:0,revenue:0});
const cards=rows=>'<div class="cards">'+rows.map(([l,v])=>'<div class="card"><small>'+escapeHTML(l)+'</small><strong>'+escapeHTML(v)+'</strong></div>').join('')+'</div>';
const table=(h,rs)=>'<div class="tablewrap"><table><thead><tr>'+h.map(x=>'<th>'+escapeHTML(x)+'</th>').join('')+'</tr></thead><tbody>'+
(rs.length?rs.map(row=>'<tr>'+row.map(x=>'<td>'+x+'</td>').join('')+'</tr>').join(''):'<tr><td colspan="'+h.length+'">No matching records</td></tr>')+'</tbody></table></div>';
const button=p=>'<button data-pid="'+escapeHTML(p.project_id)+'">Investigate</button>';
function investigate(id){selection=id;view='projects';render();document.getElementById('detail')?.scrollIntoView({block:'nearest'})}
function render(){
let ps=filtered(),f=totals(ps),done=ps.filter(p=>p.status==='Completed').length,late=ps.filter(p=>p.status==='Delayed').length,h='';
for(const b of document.querySelectorAll('[data-view]'))b.setAttribute('aria-pressed',String(b.dataset.view===view));
if(view==='overview'){
let exceptions=ps.map(p=>({p,v:(costs[p.project_id]?.actual||0)-(costs[p.project_id]?.plan||0)})).filter(x=>x.p.status==='Delayed'||x.v>0).sort((a,b)=>Number(b.p.status==='Delayed')-Number(a.p.status==='Delayed')||b.v-a.v);
h=cards([['Projects',ps.length],['Completed',done],['Delayed',late],['Recorded cost variance',money(f.actual-f.plan)]])
+'<section class="panel"><h2>Project status</h2>'+table(['Status','Project count'],['Completed','In Progress','Delayed','On Hold'].map(s=>[s,String(ps.filter(p=>p.status===s).length)]))+'</section>'
+'<section class="panel"><h2>Priority exceptions</h2><p class="muted">'+exceptions.length+' projects require review ('+exceptions.filter(x=>x.p.status==='Delayed').length+' delayed; '+exceptions.filter(x=>x.v>0).length+' above recorded cost plan)</p>'
+table(['Project','Department','Status','Cost variance','Action'],exceptions.slice(0,10).map(x=>[escapeHTML(x.p.project_name),escapeHTML(x.p.department),escapeHTML(x.p.status),money(x.v),button(x.p)]))+'</section>';
}
if(view==='projects'){
h=cards([['Projects',ps.length],['Completed',done],['Delayed',late],['Completion rate',ps.length?(done/ps.length*100).toFixed(1)+'%':'—']])
+'<section class="panel"><h2>Project portfolio register</h2>'+table(['ID','Project','Department','Status','Progress','Details'],ps.map(p=>[escapeHTML(p.project_id),escapeHTML(p.project_name),escapeHTML(p.department),escapeHTML(p.status),N(p.completion_pct)+'%',button(p)]))+'<div id="detail"></div></section>';
}
if(view==='finance')h=cards([['Recorded planned cost',money(f.plan)],['Actual cost',money(f.actual)],['Recorded revenue',money(f.revenue)],['Unfavorable variance',money(f.actual-f.plan)]])
+'<section class="panel"><h2>Project-level financial exceptions</h2>'+table(['Project','Department','Plan','Actual','Variance'],ps.map(p=>{const x=costs[p.project_id]||{plan:0,actual:0};return [escapeHTML(p.project_name),escapeHTML(p.department),money(x.plan),money(x.actual),'<span class="'+(x.actual>x.plan?'alert':'')+'">'+money(x.actual-x.plan)+'</span>']}))+'</section>';
if(view==='resources'){const ids=new Set(ps.map(p=>p.project_id)),ts=DB.timesheets.filter(t=>ids.has(t.project_id)),as=DB.actions.filter(a=>ids.has(a.project_id));
let hrs=ts.reduce((s,t)=>s+N(t.hours_logged),0),cap=ts.reduce((s,t)=>s+N(t.available_hours),0);
h=cards([['Sample utilization',cap?(hrs/cap*100).toFixed(1)+'%':'—'],['Hours logged',hrs.toLocaleString('en-IN')],['Open actions',as.filter(a=>a.status==='Open').length],['Overdue open actions',as.filter(a=>a.status==='Open'&&a.due_date<DB.asof).length]])
+'<section class="panel"><h2>Action follow-up register</h2>'+table(['Project','Owner','Action','Due','Priority','Status'],as.map(a=>[escapeHTML(a.project_id),escapeHTML(a.owner_id),escapeHTML(a.action),escapeHTML(a.due_date),escapeHTML(a.priority),escapeHTML(a.status)]))+'</section>'}
$('content').innerHTML=h;
if(view==='projects'&&selection){const p=ps.find(p=>p.project_id===selection);if(p){const x=costs[p.project_id]||{plan:0,actual:0};
$('detail').innerHTML='<div class="detail"><h2>Project investigation · '+escapeHTML(p.project_id)+'</h2><dl class="fields">'+
[['Owner',p.manager_id],['Target date',p.planned_end_date],['Progress',p.completion_pct+'%'],['Recorded plan',money(x.plan)],['Actual cost',money(x.actual)],['Cost variance',money(x.actual-x.plan)],['Tasks',DB.tasks.filter(t=>t.project_id===p.project_id).length],['Open actions',DB.actions.filter(a=>a.project_id===p.project_id&&a.status==='Open').length]].map(([k,v])=>'<div><dt>'+escapeHTML(k)+'</dt><dd>'+escapeHTML(v)+'</dd></div>').join('')+
'</dl><button id="close">Close</button></div>';$('close').onclick=()=>{selection=null;render()}}}
for(const b of document.querySelectorAll('[data-pid]'))b.addEventListener('click',()=>investigate(b.dataset.pid));
}
for(const b of document.querySelectorAll('[data-view]'))b.onclick=()=>{view=b.dataset.view;selection=null;render()};
$('dept').onchange=()=>{selection=null;render()};$('search').oninput=()=>{selection=null;render()};
$('reset').onclick=()=>{$('dept').value='All';$('search').value='';view='overview';selection=null;render()};
$('export').onclick=()=>{const cols=['project_id','project_name','department','status','completion_pct','planned_end_date'];const quote=v=>'"'+String(v??'').replaceAll('"','""')+'"';
const text=[cols.join(','),...filtered().map(p=>cols.map(k=>quote(p[k])).join(','))].join('\r\n');
const url=URL.createObjectURL(new Blob([text],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='opsconsult-projects.csv';document.body.appendChild(a);a.click();a.remove();URL.revokeObjectURL(url)};render();
</script></body></html>""";
html = html.replace("__DATA__", json.dumps(payload, separators=(",", ":"), ensure_ascii=False).replace("<", "\\u003c"))
# Keep the v2 enhancements during every automated source-data rebuild.
# Filter logic stays inside the original dashboard data model and all KPI computations.
html = html.replace("const filtered=()=>DB.projects.filter(p=>(",
    "let statusFilter='All';const filtered=()=>DB.projects.filter(p=>(statusFilter==='All'||p.status===statusFilter)&&(")
html = html.replace("</head>", '<link rel="stylesheet" href="v2.css"></head>')
html = html.replace("</body>", '<script src="v2.js"></script></body>')
(ROOT / "dashboard" / "index.html").write_text(html, encoding="utf-8")
print("Generated", ", ".join(TABLES), "and an offline dashboard.")
