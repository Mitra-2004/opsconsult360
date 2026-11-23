const {chromium}=require('playwright');
const fs=require('fs');
const path=require('path');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:960},deviceScaleFactor:1,acceptDownloads:true});
 const src='file://'+path.resolve(__dirname,'../dashboard/index.html');
 const errors=[];
 page.on('pageerror',err=>errors.push(err.message));
 await page.goto(src,{waitUntil:'load'});
 const out=path.resolve(__dirname,'../docs/screenshots');fs.mkdirSync(out,{recursive:true});
 const shots=[['overview','01-executive-overview.png'],['projects','02-project-delivery.png'],
              ['finance','03-financial-analytics.png'],['resources','04-resources-actions.png']];
 for(const [view,filename] of shots){
   await page.locator('[data-view="'+view+'"]').click();
   if(!await page.locator('#content').isVisible())throw Error(view+' content unavailable');
   if((await page.locator('#v2-title').innerText()).length<4)throw Error(view+' page title missing');
   await page.screenshot({path:path.join(out,filename),fullPage:true});
 }
 await page.locator('[data-view="overview"]').click();
 if((await page.locator('.card strong').first().innerText())!=='60')throw Error('Expected 60 project KPI');
 if(!await page.locator('#v2-viz').isVisible())throw Error('V2 charts unavailable');
 await page.locator('[data-status="Delayed"]').click();
 if((await page.locator('.card strong').first().innerText())!=='15')throw Error('Delayed filter did not select 15 projects');
 await page.locator('#reset').click();
 if((await page.locator('.card strong').first().innerText())!=='60')throw Error('Reset should restore 60 projects');
 const before=await page.locator('#content').innerText();
 await page.locator('#dept').selectOption({label:'Engineering'});
 if((await page.locator('#content').innerText())===before)throw Error('Department selection did not affect KPIs');
 await page.locator('#reset').click();
 const [download]=await Promise.all([page.waitForEvent('download'),page.locator('#export').click()]);
 if(download.suggestedFilename()!=='opsconsult-projects.csv')throw Error('CSV export name mismatch');
 const csv=fs.readFileSync(await download.path(),'utf8');
 if(csv.trim().split(/\r?\n/).length!==61)throw Error('Full export should contain 60 records');
 await page.locator('[data-pid]').first().click();
 if(!await page.locator('#detail').isVisible())throw Error('Project investigation not visible');
 await page.locator('#close').click();
 if(await page.locator('.detail').count())throw Error('Project detail not closed');
 await page.setViewportSize({width:390,height:844});
 await page.locator('[data-view="overview"]').click();
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
 if(overflow>4)throw Error('Responsive page overflows viewport by '+overflow+'px');
 await page.screenshot({path:path.join(out,'05-mobile-overview.png'),fullPage:true});
 if(errors.length)throw Error('Uncaught browser errors: '+errors.join('; '));
 await browser.close();
 console.log('PASS: four pages, v2 charts, delayed quick-filter, department filter, reset, project investigation, CSV export, mobile viewport, no page errors');
})().catch(e=>{console.error(e);process.exit(1)});