// usage (from repo root): node scripts/docread.js outdir key=url ...   -> saves text, prints plan-related sentences
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const out=process.argv[2];const b=await chromium.launch();
for(const kv of process.argv.slice(3)){const i=kv.indexOf('=');const k=kv.slice(0,i),u=kv.slice(i+1);const p=await b.newPage();
 try{const r=await p.goto(u,{waitUntil:'domcontentloaded',timeout:45000});await p.waitForTimeout(+(process.env.WAIT||4000));const t=await p.innerText('body');fs.writeFileSync(`${out}/${k}.txt`,u+'\n'+t);
 const sents=t.replace(/\s+/g,' ').split(/(?<=[.!?])\s+/).filter(s=>/\b(plan|plans|tier|available on|available to|Free|Starter|Pro|Business|Enterprise|Premium|Growth|Essential|Plus|Team|subscription)\b/.test(s)&&/(webhook|API|api|integration|available|require)/i.test(s)).slice(0,14);
 console.log(`=== ${k} ${r&&r.status()} ${t.length}ch\n`+sents.map(s=>'- '+s.slice(0,260)).join('\n'));}catch(e){console.log(`=== ${k} ERR ${e.message.slice(0,80)}`)}await p.close()}
await b.close()})();
