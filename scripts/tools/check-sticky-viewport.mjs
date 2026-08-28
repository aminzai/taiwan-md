#!/usr/bin/env node
/**
 * check-sticky-viewport.mjs — 黏在畫面上的東西不准吃掉手機的視野
 *
 * 誕生 2026-08-28（twmd-maintainer-am）：兩位讀者在四天內各自回報同一件事 —
 * /terminology/ 的篩選列是 sticky，裡面有 6 個分歧類型加 46 個子分類共 53 顆按鈕，
 * 在手機上疊起來蓋掉 65% 的畫面，而且沒有任何收合控制（issue #1612 / #1614）。
 * 修掉那一頁很容易，但站上任何一條 sticky 或 fixed 的列都能安靜地長成同樣的東西 —
 * 加一個分類、多一種語言、換一支字體，高度就往上跑，沒有人會發現。
 *
 * 這支腳本量的是「頁面剛載入時，單一個 sticky/fixed 元素擋住手機視野的百分之幾」。
 * 量真的渲染出來的交集，不是原始碼裡的 class —— 原始碼看不出 53 顆按鈕會排成幾列。
 *
 * 用法：
 *   node scripts/tools/check-sticky-viewport.mjs --base http://localhost:4399
 *   node scripts/tools/check-sticky-viewport.mjs --base ... --report   # 只印不擋，校準門檻用
 *
 * 需要一個已經 build 好並且服務中的 dist/。CI 在 deploy 前跑。
 */

import { chromium } from 'playwright';

/** 手機基準視野。iPhone 13/14 的 CSS 尺寸，站上手機流量的主力。 */
const VIEWPORT = { width: 375, height: 812 };

/**
 * 門檻 35%。2026-08-28 用站上 10 個代表性頁面實測校準（見本檔 §校準紀錄）：
 * 健康頁面的 sticky chrome 全部落在 8-13%，出事的 /terminology/ 是 65%。
 * 兩群之間空了五十個百分點，門檻放在 35% 對現況零假陽性，
 * 也還留得下「一列按鈕加一列搜尋」這種合理的兩層 sticky。
 */
const MAX_PERCENT = 35;

/** 校準過的取樣頁面：每種版型各一，全部是 build 後真的存在的路徑。 */
const DEFAULT_PATHS = [
  '/terminology/',
  '/terminology/converter',
  '/',
  '/latest',
  '/explore',
  '/dashboard',
  '/map',
  '/about',
  '/search',
  '/culture/archipelago-thinking',
];

function parseArgs(argv) {
  const args = { base: 'http://localhost:4399', report: false, paths: null };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--base') args.base = argv[++i];
    else if (argv[i] === '--report') args.report = true;
    else if (argv[i] === '--paths') args.paths = argv[++i].split(',');
  }
  return args;
}

/**
 * 在頁面裡量每個 sticky/fixed 元素**實際擋住畫面的那一段**。
 *
 * 量的是它跟視野的交集高度，不是它自己的高度 —— 這兩件事在第一版校準時
 * 就分岔了：/map 的 `.sidebar-panel` 高 487px（60%），但它整個收在畫面
 * 下緣之外（rectTop 剛好等於視野高度），是抽屜不是路障，讀者一眼都看不到它。
 * 拿「它多高」當「它擋住多少」的替身，就是在閘門的位置量錯東西。
 *
 * 只看剛載入的狀態 —— 讀者是先撞到它才知道要找收合鈕的，
 * 所以要問的是「什麼都還沒做的時候它佔掉多少視野」。
 */
async function measure(page) {
  return page.evaluate(() => {
    const out = [];
    const vh = window.innerHeight;
    for (const el of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'sticky' && cs.position !== 'fixed') continue;
      if (cs.display === 'none' || cs.visibility === 'hidden') continue;
      if (parseFloat(cs.opacity) === 0) continue;
      const rect = el.getBoundingClientRect();
      if (rect.height < 1 || rect.width < 1) continue;
      // 只算橫跨畫面的那種列。浮動小按鈕（回饋鈕、字級鈕）不是這條規則要防的病，
      // 它們窄，不會擋住閱讀動線。
      if (rect.width < window.innerWidth * 0.6) continue;
      // 交集：真正壓在視野裡的那幾個 pixel。畫面外的抽屜得 0。
      const blocked = Math.max(
        0,
        Math.min(rect.bottom, vh) - Math.max(rect.top, 0),
      );
      if (blocked < 1) continue;
      out.push({
        selector:
          el.tagName.toLowerCase() +
          (el.id ? `#${el.id}` : '') +
          (el.className && typeof el.className === 'string'
            ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.')
            : ''),
        position: cs.position,
        height: Math.round(rect.height),
        blocked: Math.round(blocked),
        percent: Math.round((blocked / vh) * 100),
      });
    }
    return out;
  });
}

const args = parseArgs(process.argv);
const paths = args.paths || DEFAULT_PATHS;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: VIEWPORT });

const violations = [];
const unmeasured = [];
const rows = [];

for (const path of paths) {
  const url = args.base.replace(/\/$/, '') + path;
  let res;
  try {
    res = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch (err) {
    console.error(
      `  ⚠️  ${path} — 打不開（${err.message.split('\n')[0]}），跳過`,
    );
    continue;
  }
  if (!res || res.status() >= 400) {
    console.error(`  ⚠️  ${path} — HTTP ${res ? res.status() : '?'}，跳過`);
    continue;
  }
  // 等版面真的安定再量。networkidle 對這個站不夠 —— /terminology/ 有 2,400 張
  // 卡片，DOM 掛好之後版面還在算，太早量會拿到一份空的清單。而空清單如果
  // 被當成「這頁沒問題」印出去，就是閘門在說謊（第一版校準時真的間歇發生過，
  // 同一頁兩次跑一次 13% 一次 0 個元素）。
  try {
    await page.waitForFunction(
      () => {
        const h = document.getElementById('header-container');
        return h && h.getBoundingClientRect().height > 0;
      },
      { timeout: 15000 },
    );
  } catch {
    /* 沒有 header 的頁面走下面的 measured=false 分支報 ⚠️，不靜默 */
  }
  const found = await measure(page);
  const worst = found.sort((a, b) => b.percent - a.percent)[0];
  // 站上每一頁都有那條全寬的 header。量到 0 個元素代表這支腳本沒看見這一頁，
  // 不代表這一頁沒問題 —— 這兩件事必須用不同的符號講。
  const measured = found.length > 0;
  rows.push({ path, worst, all: found, measured });
  if (!measured) unmeasured.push(path);
  if (worst && worst.percent > MAX_PERCENT) {
    violations.push({ path, ...worst });
  }
}

await browser.close();

console.log(
  `\n════════ sticky 元素佔手機視野比例（${VIEWPORT.width}×${VIEWPORT.height}）════════`,
);
for (const r of rows) {
  if (!r.measured) {
    console.log(
      `  ⚠️  ${r.path.padEnd(33)} 量不到（連 header 都沒看到，這頁沒被檢查）`,
    );
    continue;
  }
  const mark = r.worst.percent > MAX_PERCENT ? '❌' : '✅';
  console.log(
    `  ${mark} ${r.path.padEnd(34)} ${String(r.worst.percent).padStart(3)}%  ` +
      `擋 ${r.worst.blocked}px  ${r.worst.selector}`,
  );
}
console.log('─'.repeat(72));

if (unmeasured.length > 0) {
  console.log(
    `\n  ⚠️  ${unmeasured.length} 個頁面量不到：${unmeasured.join(', ')}\n` +
      `  這不是「通過」，是這支腳本沒看見那幾頁。先查是不是 build 壞了或路徑改了。\n`,
  );
}

if (violations.length === 0 && unmeasured.length === 0) {
  console.log(
    `  PASSED — 最高 ${Math.max(0, ...rows.map((r) => r.worst?.percent || 0))}% < ${MAX_PERCENT}% 門檻\n`,
  );
  process.exit(0);
}

if (violations.length === 0) {
  process.exit(args.report ? 0 : 1);
}

console.log(
  `\n  ${violations.length} 個頁面的 sticky 元素在手機上吃掉超過 ${MAX_PERCENT}% 的畫面：\n`,
);
for (const v of violations) {
  console.log(
    `    ${v.path}  →  ${v.selector} 擋住 ${v.percent}%（${v.blocked}px）`,
  );
}
console.log(`
  這是讀者會直接撞到的問題：捲不掉、蓋住內容、而且多半沒有收合的地方。
  修法是給它一個預設收起的收合控制（/terminology/ 的 #filter-bar 是範例），
  不是把門檻調高。
`);

process.exit(args.report ? 0 : 1);
