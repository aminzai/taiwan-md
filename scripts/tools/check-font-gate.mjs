#!/usr/bin/env node
/**
 * check-font-gate.mjs — 字型可見性閘門的行為驗證（#1666）
 *
 * Layout.astro 把整份 <html> 設成 `visibility: hidden`，等 `.fonts-loaded`
 * 才揭開。這支腳本問的是唯一重要的那個問題：**當字型來源拿不到時，讀者
 * 還看得到內容嗎？**
 *
 * 它不看程式碼長什麼樣，它把字型主機整個擋掉，然後量瀏覽器實際算出來的
 * `visibility`。這是 #1666 的 ground truth——2026-09-04 之前，答案是「看不到，
 * 而且永遠看不到」，因為那道閘門一個逾時出口都沒有。
 *
 * 用法：
 *   node scripts/tools/check-font-gate.mjs                      # 預設打 http://localhost:4321
 *   node scripts/tools/check-font-gate.mjs --url=https://taiwan.md
 *   node scripts/tools/check-font-gate.mjs --url=... --paths=/,/about/
 *
 * 需要 `npx playwright install chromium` 跑過一次。
 * exit 0 = 每條路徑在字型被擋的情況下都揭開了；exit 1 = 有路徑卡在隱形。
 */

import { chromium } from 'playwright';

const args = process.argv.slice(2);
const getArg = (name, fallback) => {
  const hit = args.find((a) => a.startsWith(`--${name}=`));
  return hit ? hit.slice(name.length + 3) : fallback;
};

const BASE = (getArg('url', 'http://localhost:4321') || '').replace(/\/$/, '');
const PATHS = getArg('paths', '/').split(',').filter(Boolean);
// 揭開的預算：站上 fallback 是 800ms，給 3 倍寬容度吸收慢機器與 CI 抖動。
const BUDGET_MS = Number(getArg('budget', '2500'));

// ⚠️ 這裡要「掛住」不是「擋掉」，兩者是完全不同的失敗模式。
// route.abort() 會讓請求**快速失敗**，字型進入 error 狀態、載入結束，
// 於是 `document.fonts.ready` 照樣 resolve、頁面照樣揭開——用 abort 測
// 會測出一片綠，然後什麼都沒證明。真正會咬人的是**慢或永不回應**：
// 字型停在 loading，`fonts.ready` 就一直是 pending。所以這裡讓 CSS 正常
// 通過（@font-face 要被解析出來），把字型檔本身掛住不回應。
const HANG_HOSTS = ['**://fonts.gstatic.com/**', '**://*.justfont.com/**'];

const browser = await chromium.launch();
const results = [];

for (const path of PATHS) {
  const context = await browser.newContext();
  const page = await context.newPage();
  for (const pattern of HANG_HOSTS) {
    // 不 fulfill、不 abort：請求就這樣懸在那裡，字型永遠停在 loading。
    await page.route(pattern, () => {});
  }

  const url = `${BASE}${path}`;
  let visibility = '(never loaded)';
  let bodyOpacity = '(never loaded)';
  let text = '';
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(BUDGET_MS);
    visibility = await page.evaluate(
      () => getComputedStyle(document.documentElement).visibility,
    );
    bodyOpacity = await page.evaluate(
      () => getComputedStyle(document.body).opacity,
    );
    text = (await page.evaluate(() => document.body.innerText || '')).trim();
  } catch (err) {
    results.push({ path, ok: false, why: `載入失敗：${err.message}` });
    await context.close();
    continue;
  }

  // 「看得到」= html 沒被藏起來 + body 沒被 opacity 蓋掉 + 真的有字。
  const ok =
    visibility === 'visible' && Number(bodyOpacity) > 0 && text.length > 0;
  results.push({
    path,
    ok,
    visibility,
    bodyOpacity,
    chars: text.length,
    why: ok
      ? ''
      : `字型被擋 ${BUDGET_MS}ms 後仍不可讀（visibility=${visibility} bodyOpacity=${bodyOpacity} 可見字數=${text.length}）`,
  });
  await context.close();
}

await browser.close();

console.log(`════════ 🧬 字型閘門行為檢查 — ${BASE} ════════`);
console.log(
  `（字型檔請求掛住不回應，等 ${BUDGET_MS}ms 後量實際 computed style）\n`,
);
let failed = 0;
for (const r of results) {
  if (r.ok) {
    console.log(
      `  ✅ ${r.path}  visibility=${r.visibility} bodyOpacity=${r.bodyOpacity} 可見字數=${r.chars}`,
    );
  } else {
    failed++;
    console.log(`  ❌ ${r.path}  ${r.why}`);
  }
}
console.log('');
if (failed) {
  console.log(
    `❌ ${failed}/${results.length} 條路徑在字型拿不到時是空白頁。\n` +
      `   Layout.astro 的 \`html { visibility: hidden }\` 必須自己有出口：\n` +
      `   逾時 setTimeout、promise 的 catch、以及 noscript 解除。缺任何一條，\n` +
      `   字型慢一點讀者就看不到東西（#1666）。`,
  );
  process.exit(1);
}
console.log(
  `✅ ${results.length}/${results.length} 條路徑在字型拿不到時仍可讀`,
);
