/* OpsConsult 360 v2 progressive enhancement: all summaries use the existing synthetic DB. */
(function(){
  'use strict';
  const root=document.querySelector('main'), content=document.getElementById('content');
  if(!root||!content||typeof DB==='undefined'||typeof render!=='function') return;
  const pages={
    overview:['Executive overview','Portfolio health, delivery visibility and exceptions requiring review'],
    projects:['Project delivery','Investigate delivery progress, project ownership and outstanding actions'],
    finance:['Financial analytics','Recorded-period planned versus actual expenditure and revenue'],
    resources:['Resources & actions','Sampled utilization and action-owner accountability']
  };
  const intro=document.createElement('div');
  intro.className='v2-intro';intro.innerHTML='<div><span class="v2-kicker">Management intelligence · portfolio / 2026</span><h2 id="v2-title">Executive overview</h2><p id="v2-subtitle">Portfolio health, delivery visibility and exceptions requiring review</p></div><div class="v2-snapshot">● Synthetic dataset &nbsp;·&nbsp; 23 NOV 2026</div>';
  root.insertBefore(intro,root.firstChild);
  const quick=document.createElement('div');quick.id='v2-quick';quick.className='v2-quick';quick.setAttribute('aria-label','Project status quick filters');
  const toolbar=document.querySelector('.toolbar');toolbar.insertAdjacentElement('afterend',quick);
  const statusChoices=[['All','All projects'],['Delayed','Delayed'],['In Progress','In progress'],['Completed','Completed']];
  const calcScope=()=>DB.projects.filter(p=>(document.getElementById('dept').value==='All'||document.getElementById('dept').value===p.department)&&
      (p.project_id.toLowerCase().includes(document.getElementById('search').value.toLowerCase())||
       p.project_name.toLowerCase().includes(document.getElementById('search').value.toLowerCase())));
  const scopedCount=(base,s)=>s==='All'?base.length:base.filter(p=>p.status===s).length;
  const statusMarkup=s=>'<span class="v2-status '+(s==='Delayed'?'delayed':s==='In Progress'?'in-progress':'')+'">'+escapeHTML(s)+'</span>';
  const pctMarkup=n=>{const p=Math.max(0,Math.min(100,Number(n)||0));return '<div class="v2-progress" aria-label="Completion '+p+' percent"><span><i style="width:'+p+'%"></i></span><small>'+p+'%</small></div>'};
  const totalFor=ps=>ps.reduce((sum,p)=>{const c=costs[p.project_id]||{plan:0,actual:0};sum.plan+=c.plan;sum.actual+=c.actual;return sum;},{plan:0,actual:0});
  function drawStatusChart(ps){
    const total=ps.length, completed=ps.filter(p=>p.status==='Completed').length,delayed=ps.filter(p=>p.status==='Delayed').length,progress=total-completed-delayed;
    const a=total?completed/total*100:0,b=total?(completed+delayed)/total*100:0;
    const donut=total?'conic-gradient(#0b9180 0 '+a+'%,#e2a66a '+a+'% '+b+'%,#789cce '+b+'% 100%)':'#e8edf2';
    const row=(c,l,v)=>'<div class="v2-legrow"><span><i class="v2-dot" style="background:'+c+'"></i>'+l+'</span><b>'+v+'</b></div>';
    return '<section class="panel"><div class="v2-viz-head"><h2>Delivery composition</h2><small>Current filter</small></div><div class="v2-ring-wrap">'+
      '<div class="v2-ring" role="img" aria-label="'+completed+' completed, '+delayed+' delayed, '+progress+' in progress" style="background:'+donut+'">'+
      '<div class="v2-ring-inner"><strong>'+total+'</strong><small>Projects</small></div></div><div class="v2-legend">'+
      row('#0b9180','Completed',completed)+row('#e2a66a','Delayed',delayed)+row('#789cce','In progress',progress)+'</div></div></section>';
  }
  function drawDepartmentChart(ps){
    const depts=[...new Set(ps.map(p=>p.department))].sort();
    const rows=depts.map(d=>{const p=ps.filter(x=>x.department===d),s=totalFor(p);return {d,delta:s.actual-s.plan,count:p.length}}).sort((a,b)=>Math.abs(b.delta)-Math.abs(a.delta));
    const max=Math.max(1,...rows.map(r=>Math.abs(r.delta)));
    const bars=rows.length?rows.map(r=>'<div class="v2-barrow" title="'+escapeHTML(r.d)+' · '+r.count+' projects"><span>'+escapeHTML(r.d)+'</span><div class="v2-track"><i class="'+(r.delta<0?'negative':'')+'" style="width:'+Math.max(2,Math.abs(r.delta)/max*100)+'%"></i></div><b>'+money(r.delta)+'</b></div>').join(''):
    '<p class="muted">No departments for this filter.</p>';
    return '<section class="panel"><div class="v2-viz-head"><h2>Department cost variance</h2><small>Actual − plan · sampled period</small></div><div class="v2-bars">'+bars+'</div></section>';
  }
  function enhanceRows(){
    // Replace only text-only portfolio status and percentage cells; never alter the original table's data values.
    if(view==='projects'){
      for(const row of content.querySelectorAll('tbody tr')){
        const cells=row.querySelectorAll('td');
        if(cells.length===6){
          const s=cells[3].textContent.trim(),n=cells[4].textContent.trim();
          if(['Completed','Delayed','In Progress'].includes(s))cells[3].innerHTML=statusMarkup(s);
          if(/^\d+(\.\d+)?%$/.test(n))cells[4].innerHTML=pctMarkup(n.slice(0,-1));
        }
      }
    }
    if(view==='overview'){
      for(const row of content.querySelectorAll('tbody tr')){
        const cells=row.querySelectorAll('td');
        if(cells.length===5&&['Completed','Delayed','In Progress'].includes(cells[2].textContent.trim()))cells[2].innerHTML=statusMarkup(cells[2].textContent.trim());
      }
    }
  }
  function addInsights(ps){
    if(view!=='overview')return;
    const delayed=ps.filter(p=>p.status==='Delayed').length;
    const above=ps.filter(p=>{const c=costs[p.project_id]||{actual:0,plan:0};return c.actual>c.plan}).length;
    const open=DB.actions.filter(a=>ps.some(p=>p.project_id===a.project_id)&&a.status==='Open').length;
    const insight=document.createElement('div');insight.className='v2-insight';
    insight.innerHTML='<span class="v2-insight-icon" aria-hidden="true">↗</span><div><strong>Management attention</strong>'+
      '<span>'+delayed+' delayed project'+(delayed===1?'':'s')+', '+above+' above recorded cost plan and '+open+' open follow-up'+(open===1?'':'s')+' in the current selection. Review owners and deadlines before making an intervention decision.</span></div>';
    content.querySelector('.cards')?.insertAdjacentElement('afterend',insight);
  }
  function injectVisuals(ps){
    if(view!=='overview')return;
    const viz=document.createElement('div');viz.className='v2-viz';viz.id='v2-viz';
    viz.innerHTML=drawStatusChart(ps)+drawDepartmentChart(ps);
    const insight=content.querySelector('.v2-insight');
    if(insight)insight.insertAdjacentElement('afterend',viz);
    else content.querySelector('.cards')?.insertAdjacentElement('afterend',viz);
  }
  function updateQuick(){
    const scope=calcScope();
    quick.innerHTML='<span class="v2-caption">Quick view</span>'+statusChoices.map(([v,label])=>
      '<button type="button" class="v2-chip" data-status="'+v+'" aria-pressed="'+String(statusFilter===v)+'">'+
      label+' <em>'+scopedCount(scope,v)+'</em></button>').join('');
    for(const b of quick.querySelectorAll('[data-status]'))b.addEventListener('click',()=>{
      statusFilter=b.dataset.status;selection=null;render();
    });
  }
  const baseRender=render;
  render=function(){
    baseRender();
    const page=pages[view]||pages.overview;
    document.getElementById('v2-title').textContent=page[0];
    document.getElementById('v2-subtitle').textContent=page[1];
    updateQuick();
    const ps=filtered();
    addInsights(ps);injectVisuals(ps);enhanceRows();
  };
  // Reset should also restore the quick-status filter.
  const reset=document.getElementById('reset'),baseReset=reset.onclick;
  reset.onclick=function(){statusFilter='All';baseReset.call(this)};
  render();
})();