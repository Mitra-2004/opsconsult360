const assert=require('node:assert/strict');
const origin='https://opsconsult360.vercel.app';
async function get(path){
 const r=await fetch(origin+path,{signal:AbortSignal.timeout(25000),redirect:'follow'});
 assert.equal(r.status,200,path+' HTTP '+r.status);
 const text=await r.text();
 assert.ok(text.length>1000,path+' body too small');
 return text;
}
(async()=>{
 const [html,css,js]=await Promise.all([get('/'),get('/v2.css'),get('/v2.js')]);
 assert.match(html,/OpsConsult 360/);
 assert.match(html,/href="v2\.css"/);
 assert.match(html,/src="v2\.js"/);
 assert.match(html,/let statusFilter='All'/);
 assert.match(css,/\.v2-viz/);
 assert.match(js,/drawStatusChart/);
 assert.match(js,/statusFilter=b\.dataset\.status/);
 console.log('PASS public HTTP: HTML, CSS and JS all respond 200; v2 enhancements referenced and available');
})().catch(e=>{console.error(e);process.exit(1)});
