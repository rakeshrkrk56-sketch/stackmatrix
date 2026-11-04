const {chromium}=require('playwright');const exp=require(process.argv[2]);
(async()=>{const b=await chromium.launch();const pg=await b.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));let bad=0;
const num=async id=>Number((await pg.textContent('#'+id)).replace(/[$,]/g,''));
for(const [p,[m,y1m,y1a,t3a]] of Object.entries(exp)){await pg.goto(`http://127.0.0.1:8765/stack/${p}/`);await pg.waitForTimeout(150);
 await pg.fill('#calc-seats','10').catch(()=>{});await pg.dispatchEvent('#calc-seats','input');
 const M=await num('calc-total'),Y=await num('calc-year1');await pg.check('#calc-annual');const YA=await num('calc-year1'),TA=await num('calc-tco3');
 const ok=Math.abs(M-m)<.01&&Math.abs(Y-y1m)<.01&&Math.abs(YA-y1a)<.01&&Math.abs(TA-t3a)<.01; if(!ok){bad++;console.log('MISMATCH',p,{M,Y,YA,TA},{m,y1m,y1a,t3a})}}
console.log('pages',Object.keys(exp).length,'mismatches',bad,'js errors',errs.length,errs.slice(0,3));await b.close()})();
