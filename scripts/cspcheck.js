// Load every page in Chromium and report anything the Content-Security-Policy blocks, plus JS errors.
// Usage (server running on 8765): node scripts/cspcheck.js page1.html page2/index.html ...
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext();
  await ctx.route(/^https?:\/\/(?!localhost)/, r => r.fulfill({ status: 204, body: '' })); // no outside requests
  let bad = 0;
  for (const f of process.argv.slice(2)) {
    const p = await ctx.newPage(); const errs = [];
    p.on('console', m => { if (/Content Security Policy|Refused to/.test(m.text())) errs.push('CSP: ' + m.text().slice(0, 160)); });
    p.on('pageerror', e => errs.push('JS: ' + e.message.slice(0, 160)));
    const url = 'http://localhost:8765/' + f.replace(/index\.html$/, '');
    await p.goto(url, { waitUntil: 'load' }).catch(e => errs.push('load: ' + e.message.slice(0, 100)));
    await p.waitForTimeout(150);
    if (errs.length) { bad++; console.log(f, errs); }
    await p.close();
  }
  console.log(`csp browser check: ${process.argv.length - 2} pages, ${bad} with problems`);
  await b.close(); process.exit(bad ? 1 : 0);
})();
