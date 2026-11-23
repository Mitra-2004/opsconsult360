const {chromium}=require('playwright');
const fs=require('fs');
const path=require('path');
(async()=>{
  const browser=await chromium.launch({headless:true});
  const page=await browser.newPage({viewport:{width:1440,height:960},deviceScaleFactor:1});
  const src='file://'+path.resolve(__dirname,'../dashboard/index.html');
  await page.goto(src,{waitUntil:'load'});
  const out=path.resolve(__dirname,'../docs/screenshots');
  fs.mkdirSync(out,{recursive:true});
  const shots=[
    ['overview','01-executive-overview.png'],
    ['projects','02-project-delivery.png'],
    ['finance','03-financial-analytics.png'],
    ['resources','04-resources-actions.png']
  ];
  for(const [view,filename] of shots){
    await page.locator('[data-view="'+view+'"]').click();
    await page.screenshot({path:path.join(out,filename),fullPage:true});
    if(!await page.locator('#content').isVisible())throw Error(view+' content unavailable');
  }
  await page.locator('[data-view="overview"]').click();
  const before=await page.locator('#content').innerText();
  await page.locator('#dept').selectOption({label:'Engineering'});
  const after=await page.locator('#content').innerText();
  if(after===before)throw Error('Department filter did not change output');
  await page.locator('#reset').click();
  if((await page.locator('#content').innerText())!==before)throw Error('Reset did not restore overview');
  await browser.close();
  console.log('PASS browser screenshots, view navigation, department filter and reset');
})().catch(e=>{console.error(e);process.exit(1)});
