#!/usr/bin/env node
/**
 * check-template-language.mjs — 模板層的中文 fallback 閘門
 *
 * `check-ui-language.mjs` 守 `src/i18n/*.ts`：那裡的字串進了字串表，每個語言一格，
 * 缺了看得出來。但**沒進字串表的中文**它一個字也看不到——而 `.astro` 裡到處是
 * 這種寫法：
 *
 *     {lang === 'en' ? '💚 Support with a Donation' : '💚 金流支持'}
 *
 * 這行對英文讀者是英文，對**其他十一種語言全部是中文**。它不會報錯、不會變紅、
 * 頁面「有字」，`check-ui-language` 掃字串表當然全綠——因為這個字串從來沒進字串表。
 * 保護密度跟曝光量成反比的同一個洞，只是換一層樓。
 *
 * 2026-08-17 首掃實測：三元式 fallback **125 處**（20 個檔案），另有沒有任何語言
 * 條件的裸中文 1,122 處。渲染層對照：`/ar/contribute/` 456 個漢字、`/ar/dashboard/`
 * 632 個、`/ar/about/` 216 個。
 *
 * ── 三種判定 ─────────────────────────────────────────────────────────
 *
 *   1. EN_ONLY_TERNARY — `lang === 'en' ? 英文 : 中文`（含 `isEn ? …` 變體）
 *      十一種語言拿到中文。這是主要病灶。**擋 push。**
 *   2. PARTIAL_TERNARY — `lang === 'en' ? … : lang === 'ja' ? … : lang === 'ko' ? … : 中文`
 *      九種語言拿到中文。比 1 好一點，本質相同。**擋 push。**
 *   3. UNCONDITIONAL — 完全沒有語言條件的裸中文。**只印不擋**（--strict 才算）。
 *      這一類判準不夠硬：裡面既有真問題（文章頁的查證說明條、404 頁的
 *      「這篇文章尚未翻譯」——那句偏偏是給非中文讀者看的），也有刻意的中文專屬
 *      介面。硬擋會逼人為了綠燈把中文專屬頁面改壞。
 *
 * `lang === 'zh-TW' ? 中文 : 英文` **不報**——那是正確的寫法（中文只給中文頁），
 * 雖然非英文語言拿到英文是另一個議題（FALLBACK_CHAIN 設計，不在本閘門管轄）。
 *
 * 三元鏈**只報最後那一支**：`lang==='en'?A:lang==='ja'?B:lang==='ko'?C:'中文'` 裡
 * A/B/C 各有自己的語言守衛、寫法正確，只有最後的中文是 fallback。v1 用「往前看有沒有
 * lang ===」判，把 taiwan-shape 的日文韓文全報成問題，假陽性過半（見 §classifyLiteralPosition）。
 *
 * ── 豁免 ─────────────────────────────────────────────────────────────
 *
 *   a. ZH_ONLY_TEMPLATES — 整頁只有中文版的模板（/opendata /mcp /timeline
 *      /soundscape 這類）。它們的內容層本來就標明 zh-TW canonical + 其他語言
 *      fallback（見 `src/data/opendata-content.ts` 檔頭），是**內容層缺口**不是
 *      模板寫死，要修是整頁翻譯的工作，跟本閘門要防的「忘了接 i18n」不同類。
 *      清單見下方，每一條都要寫出它的內容層檔案在哪。
 *   b. 非使用者可見字串：console / import 路徑 / 註解 / class 名 / 資料 key。
 *   c. CJK_OK — 語言選單 endonym（中文／日本語／한국어）、站名、刻意雙語標示。
 *
 * 用法：
 *   node scripts/tools/check-template-language.mjs             # 報告（exit 1 = 有三元式 fallback）
 *   node scripts/tools/check-template-language.mjs --strict     # 裸中文那類也算 fail
 *   node scripts/tools/check-template-language.mjs --warn-only  # 只印不 fail
 *   node scripts/tools/check-template-language.mjs --json
 *   npm run check:tmpl-lang
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');
const SCAN_DIRS = [
  'src/templates',
  'src/components',
  'src/layouts',
  'src/pages',
];

const HAN = /[㐀-鿿豈-﫿]/;

/**
 * 整頁 zh-TW canonical 的模板（豁免 a）。key = 檔案 basename，value = 它的內容層
 * SSOT 與缺口現況，讓讀報告的人知道該去哪裡補、不是來這裡加豁免。
 */
const ZH_ONLY_TEMPLATES = {
  'opendata.template.astro':
    'src/data/opendata-content.ts（型別 6 語、實際 zh-TW/en/ja/ko，其餘 fallback zh）',
  'mcp.template.astro': 'src/data/mcp-content.ts（同上機制）',
  'timeline.template.astro': 'src/data/timeline-*.ts / knowledge 時間軸資料層',
  'soundscape.template.astro': 'src/data/soundscape-*.ts（錄音條目本身是中文）',
  'elections-2026.template.astro': '選舉資料層（zh-TW only 專題頁）',
  'budget.template.astro': 'src/i18n/budget.ts（zh-TW/en 雙語專題頁）',
  // 只在中文頁被 render 的視覺化元件（呼叫端就寫著條件）
  'FoodViz.astro':
    "呼叫端 `{category === 'food' && lang === 'zh-TW' && <FoodViz />}`（見該檔檔頭）",
  'EconCharts.astro':
    "呼叫端 `{category === 'economy' && lang === 'zh-TW' && <EconCharts />}`（見該檔檔頭）",
};

/**
 * 整個目錄只有中文版的路由（豁免 a 的目錄版）。判準是 `src/pages/<lang>/` 底下
 * 沒有對應檔案——例如 `src/pages/ar/` 沒有 semiont / fork-graph，那些頁只掛在
 * 中文根路徑上，本來就是中文專屬表面（認知層對外的公開視窗）。
 * 相對地 `src/pages/ar/terminology/index.astro` 存在，所以詞庫頁**不**豁免。
 */
const ZH_ONLY_DIRS = [
  [
    'src/pages/semiont/',
    '認知層公開頁，只掛中文根路徑（src/pages/ar/ 無 semiont）',
  ],
  ['src/pages/fork-graph.astro', '子代譜系圖，只掛中文根路徑'],
  ['src/pages/lifetree/', '生命樹視覺化，只掛中文根路徑'],
  ['src/pages/raw/', '純文字鏡像，內容即中文原文'],
];

/** 語言選單 endonym 與站名等刻意保留的漢字 */
const CJK_OK_LITERALS = new Set([
  '中文',
  '繁體中文',
  '日本語',
  '한국어',
  '台灣',
  '臺灣',
  'Taiwan.md 台灣知識庫',
]);

/** 這些前綴的行不是使用者可見字串 */
const NON_UI_LINE = /^\s*(?:\/\/|\/\*|\*|import\s|export\s+type|console\.)/;

/**
 * 把註解與 <style> 內容挖空（保留換行，行號不動）。
 *
 * 沒做這步的話 UNCONDITIONAL 那類幾乎不可用：首跑 2,056 筆裡一大半是**跨行註解的
 * 續行**（`article.template.astro` 那種長註解一段十幾行），單行 regex 只認得第一行。
 * 而那類底下埋著真正嚴重的一批——文章頁把「進化中 · 社群貢獻」「圖片」「原始來源」
 * 寫死成中文，十二種語言的每一篇文章頁都看得到。噪音蓋住訊號，比沒有這個檢查更糟。
 */
function blankComments(text) {
  // ⚠️ 別用跨行 regex 幹這件事。`article.template.astro` L93 有一行**註解**寫著
  // 「wired into <style define:vars> below」，`/<style[\s\S]*?<\/style>/` 從那個
  // 字串一路吃到 L1717 的真 </style>，把整份 body 挖空（實測含漢字行 80 → 9，
  // 於是文章頁那批寫死中文憑空消失、我還一度以為它們本來就是註解）。
  // 逐行狀態機才知道「標籤」與「講到標籤的字」的差別。
  const out = [];
  let inHtml = false;
  let inBlock = false;
  let inStyle = false;
  for (const raw of text.split('\n')) {
    let line = raw;
    if (inHtml) {
      const e = line.indexOf('-->');
      if (e === -1) {
        out.push('');
        continue;
      }
      line = line.slice(e + 3);
      inHtml = false;
    }
    if (inBlock) {
      const e = line.indexOf('*/');
      if (e === -1) {
        out.push('');
        continue;
      }
      line = line.slice(e + 2);
      inBlock = false;
    }
    if (inStyle) {
      const e = line.toLowerCase().indexOf('</style');
      if (e === -1) {
        out.push('');
        continue;
      }
      line = line.slice(line.toLowerCase().indexOf('>', e) + 1);
      inStyle = false;
    }
    // 同行閉合的註解先拿掉
    line = line.replace(/<!--.*?-->/g, ' ').replace(/\/\*.*?\*\//g, ' ');
    // 開啟未閉合的
    if (line.includes('<!--')) {
      line = line.slice(0, line.indexOf('<!--'));
      inHtml = true;
    }
    if (line.includes('/*')) {
      line = line.slice(0, line.indexOf('/*'));
      inBlock = true;
    }
    // <style> 只認「行首的標籤」，不認註解裡提到的標籤名
    const styleOpen = line.match(/^\s*<style\b/i);
    if (styleOpen) {
      line = '';
      inStyle = true;
    }
    out.push(line);
  }
  return out.join('\n');
}

function isCjkOk(s) {
  const t = s.trim();
  if (CJK_OK_LITERALS.has(t)) return true;
  // 純 endonym 清單（中文、English、日本語⋯）
  if (
    /^[\s、,·|]*(?:中文|繁體中文|English|Español|日本語|한국어|Français)(?:[\s、,·|]+(?:中文|繁體中文|English|Español|日本語|한국어|Français))*[\s、,·|]*$/.test(
      t,
    )
  )
    return true;
  return false;
}

/**
 * 找出「被 `&&` 守衛的中文專屬區塊」的行域。
 *
 * `{lang === 'zh-TW' && (<div>整段中文策展文</div>)}` 是正確寫法——那段只會渲染在
 * 中文頁。但它不是三元式，位置判定看不到守衛，整段會被誤報成 UNCONDITIONAL
 * （首頁策展文 90 行、FoodViz 190 行都是這樣進來的）。這裡用括號配對算出守衛的
 * 作用範圍，把那些行整段排除。
 *
 * 反向也成立：`lang !== 'zh-TW' && …` 或 `isEn && …` 守衛的區塊裡如果有中文，
 * 那才是真的壞掉——但那種寫法目前不存在，先不特別報。
 */
function zhGuardedRanges(lines, aliases) {
  const zhAliases = [...aliases]
    .filter(([, c]) => c.op === '===' && c.lang === 'zh-TW')
    .map(([n]) => n);
  const guard = new RegExp(
    `(?:lang\\s*===\\s*'zh-TW'${zhAliases.length ? '|\\b(?:' + zhAliases.join('|') + ')\\b' : ''})\\s*&&`,
  );
  const ranges = [];
  for (let i = 0; i < lines.length; i++) {
    if (!guard.test(lines[i])) continue;
    // 從這一行往下做括號配對，找出這個 JSX 表達式結束在哪
    let depth = 0;
    let started = false;
    let end = i;
    for (let j = i; j < Math.min(lines.length, i + 400); j++) {
      for (const ch of lines[j]) {
        if (ch === '{' || ch === '(') {
          depth++;
          started = true;
        } else if (ch === '}' || ch === ')') depth--;
      }
      end = j;
      if (started && depth <= 0) break;
    }
    ranges.push([i + 1, end + 1]);
  }
  return ranges;
}

/** 找出檔案裡 `const isEn = lang === 'en'` 這類別名 */
function langAliases(text) {
  const out = new Map();
  for (const m of text.matchAll(
    /const\s+(\w+)\s*=\s*lang\s*(===|!==)\s*'([a-zA-Z-]+)'/g,
  )) {
    out.set(m[1], { op: m[2], lang: m[3] });
  }
  return out;
}

/** 把字串字面值換成佔位符，讓 ?: 計數不被字串裡的標點干擾 */
function blankStrings(s) {
  return s
    .replace(/'(?:\\.|[^'\\])*'/g, "'∎'")
    .replace(/"(?:\\.|[^"\\])*"/g, '"∎"')
    .replace(/`(?:\\.|[^`\\])*`/g, '`∎`');
}

/**
 * 判斷一個含漢字的字面值是不是三元鏈的 **default 分支**（最後那個 `:` 後面）。
 *
 * 這是本閘門唯一有判斷力的地方，所以講清楚為什麼要這樣判：
 *
 *   lang === 'en' ? 'A' : lang === 'ja' ? 'B' : lang === 'ko' ? 'C' : '中文'
 *
 * A/B/C 各自有自己的語言守衛，寫法正確——**只有最後那個「中文」是 fallback**，
 * 九種語言全部落在它身上。v1 的做法是「往前 12 行看有沒有 lang ===」，結果把
 * taiwan-shape 的日文韓文字串全報成問題（那些是對的），假陽性一半以上。
 *
 * 判準：從表達式開頭掃到這個字面值，如果看到的 `:` 數量 ≥ `?` 數量，它就站在
 * default 位置。`lang === 'zh-TW' ? '中文' : 'English'` 的中文在第一支（? 1 : 0），
 * 不報——那是正確寫法。
 *
 * 回傳 { isDefault, coveredLangs }；coveredLangs 是有自己分支的語言，用來寫
 * 「哪些語言會讀到這段中文」。
 */
function classifyLiteralPosition(exprText, aliases) {
  const blanked = blankStrings(exprText);
  const q = (blanked.match(/\?(?!\.)/g) || []).length;
  const c = (blanked.match(/:/g) || []).length;
  const covered = [];
  for (const m of exprText.matchAll(/lang\s*===\s*'([a-zA-Z-]+)'/g))
    covered.push(m[1]);
  for (const [name, cmp] of aliases) {
    if (cmp.op === '===' && new RegExp(`\\b${name}\\b`).test(exprText))
      covered.push(cmp.lang);
  }
  return {
    isDefault: q > 0 && c >= q,
    hasLangCond: covered.length > 0,
    coveredLangs: [...new Set(covered)],
  };
}

/**
 * 把 window 切到「這個表達式的開頭」：最後一個 JSX `{` / `=>` / `return` / 變數賦值。
 *
 * ⚠️ 別用 `lastIndexOf('= ')` 當錨點——它會命中 `lang === 'en'` 裡的第三個等號，
 * 把整個語言條件切掉，於是所有 `{lang === 'en' ? 英 : 中}` 全被誤判成
 * UNCONDITIONAL（v2 首跑 contribute 45 處真陽性就是這樣消失的）。賦值錨點要用
 * regex 明確要求 const/let/var。
 */
const ASSIGN_RE = /\b(?:const|let|var)\s+[\w{}[\],\s]+=\s*/g;

function exprSlice(win) {
  let cut = Math.max(
    win.lastIndexOf('{'),
    win.lastIndexOf('=>'),
    win.lastIndexOf('return '),
  );
  for (const m of win.matchAll(ASSIGN_RE)) {
    const end = m.index + m[0].length;
    if (end > cut) cut = end;
  }
  return cut > 0 ? win.slice(cut) : win;
}

/**
 * 掃一個檔案。策略是「逐個含漢字的字串字面值，往前看它所在的條件式」——
 * 不做完整 JS 解析（.astro 混 JSX，解析成本遠高於本閘門的價值），改用
 * 「同一個表達式往前 12 行的窗」近似 governing condition。實測對現存 8 個
 * 檔案的三元式全部判對；判不準時報 UNKNOWN 讓人看，不靜默放過。
 */
function scanFile(rel) {
  const abs = path.join(ROOT, rel);
  const text = blankComments(fs.readFileSync(abs, 'utf8'));
  const base = path.basename(rel);
  const dirExempt = ZH_ONLY_DIRS.find(([p]) => rel.startsWith(p));
  const exemptReason = ZH_ONLY_TEMPLATES[base] || (dirExempt && dirExempt[1]);
  const aliases = langAliases(text);
  const lines = text.split('\n');
  const findings = [];
  const zhRanges = zhGuardedRanges(lines, aliases);
  const inZhBlock = (n) => zhRanges.some(([a, b]) => n >= a && n <= b);

  lines.forEach((line, i) => {
    if (!HAN.test(line)) return;
    if (NON_UI_LINE.test(line)) return;
    if (inZhBlock(i + 1)) return; // `lang === 'zh-TW' &&` 守衛的區塊，正確寫法
    // 取出這一行所有含漢字的字串字面值 + JSX 文字節點
    const literals = [];
    for (const m of line.matchAll(
      /'((?:\\.|[^'\\])*)'|"((?:\\.|[^"\\])*)"|`((?:\\.|[^`\\])*)`/g,
    )) {
      const v = m[1] ?? m[2] ?? m[3] ?? '';
      if (HAN.test(v)) literals.push(v);
    }
    // JSX 文字節點：>中文< 或整行只有中文（縮排的 JSX 文字）
    const jsxText = line
      .replace(/<[^>]*>/g, '')
      .replace(/\{[^}]*\}/g, '')
      .trim();
    if (!literals.length && HAN.test(jsxText) && jsxText.length > 1) {
      literals.push(jsxText);
    }
    if (!literals.length) return;

    for (const lit of literals) {
      if (isCjkOk(lit)) continue;
      // 路徑 / URL / 純程式碼片段不是給讀者看的字
      if (/^[/.]|:\/\//.test(lit.trim())) continue;
      if (/=>|\bRegExp\b|\.test\(|querySelector|\$\{_esc/.test(lit)) continue;
      // 表達式範圍：往前 12 行、再切到表達式開頭，然後看這個字面值站在哪一支
      const winFull = lines.slice(Math.max(0, i - 12), i + 1).join('\n');
      const litAt = winFull.lastIndexOf(lit);
      const upto = litAt > 0 ? winFull.slice(0, litAt) : winFull;
      const expr = exprSlice(upto);
      const pos = classifyLiteralPosition(expr, aliases);
      let kind;
      if (!pos.hasLangCond) kind = 'UNCONDITIONAL';
      else if (!pos.isDefault)
        continue; // 有自己的語言守衛，寫法正確
      else if (pos.coveredLangs.includes('zh-TW'))
        continue; // 中文那支才是它
      else
        kind =
          pos.coveredLangs.length > 1 ? 'PARTIAL_TERNARY' : 'EN_ONLY_TERNARY';
      findings.push({
        kind,
        file: rel,
        line: i + 1,
        text: lit.slice(0, 90),
        exempt: exemptReason || null,
        reachedBy: pos.hasLangCond
          ? `除 ${pos.coveredLangs.join('/')} 外的語言`
          : '全部 12 語',
      });
    }
  });
  return findings;
}

function walk(dir) {
  const out = [];
  const abs = path.join(ROOT, dir);
  if (!fs.existsSync(abs)) return out;
  for (const e of fs.readdirSync(abs, { withFileTypes: true })) {
    const rel = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walk(rel));
    else if (e.name.endsWith('.astro')) out.push(rel);
  }
  return out;
}

const asJson = process.argv.includes('--json');
const warnOnly = process.argv.includes('--warn-only');
const strict = process.argv.includes('--strict');
const files = SCAN_DIRS.flatMap(walk);
const all = files.flatMap(scanFile);
const live = all.filter((f) => !f.exempt);
const exempted = all.filter((f) => f.exempt);

// 三元式兩類判得準（每一筆都能指出「這一支是 default、那些語言落在它身上」），
// 當 fail 條件。UNCONDITIONAL 是「沒有任何語言條件的裸中文」——它同時包含真問題
// （文章頁的查證狀態說明條、404 頁的「這篇文章尚未翻譯」）與需要逐表面判斷的
// 中文專屬介面，判準不夠硬，只印不 fail（--strict 才算）。寧可漏不可誤殺：
// 假陽性高的閘門會被當噪音關掉，那比沒有閘門更糟（2026-08-09 LESSONS）。
const HARD_KINDS = new Set(['EN_ONLY_TERNARY', 'PARTIAL_TERNARY']);
const hard = live.filter((f) => HARD_KINDS.has(f.kind));
const info = live.filter((f) => !HARD_KINDS.has(f.kind) && HAN.test(f.text));

function groupPrint(list, limit = 8) {
  const byFile = {};
  for (const f of list) (byFile[f.file] ||= []).push(f);
  for (const [file, hits] of Object.entries(byFile).sort(
    (a, b) => b[1].length - a[1].length,
  )) {
    console.log(`  ${file}（${hits.length}）`);
    for (const h of hits.slice(0, limit))
      console.log(`    L${h.line} ${h.reachedBy} 讀到：${h.text}`);
    if (hits.length > limit) console.log(`    … 另 ${hits.length - limit} 處`);
  }
}

if (asJson) {
  console.log(JSON.stringify({ findings: live, exempted }, null, 2));
} else {
  console.log('# 模板層中文 fallback 閘門\n');
  if (!hard.length) {
    console.log('✅ 沒有語言三元式把中文當 fallback 丟給非中文讀者');
  } else {
    const byKind = {};
    for (const f of hard) (byKind[f.kind] ||= []).push(f);
    for (const [kind, list] of Object.entries(byKind)) {
      console.log(`\n## ${kind}（${list.length}）\n`);
      groupPrint(list);
    }
    console.log(`\n總計 ${hard.length} 處三元式 fallback`);
  }
  if (info.length) {
    console.log(
      `\nℹ️ 另有 ${info.length} 處**沒有任何語言條件**的裸中文（只印不 fail，--strict 才算）。` +
        '\n   這一類要逐表面判斷：文章頁的查證說明條與 404 頁的「尚未翻譯」提示是真問題，' +
        '\n   中文專屬介面則是刻意的。前 10 個檔案：\n',
    );
    groupPrint(info.slice(0, 0)); // 只列檔案彙總，細節用 --json
    const byFile = {};
    for (const f of info) (byFile[f.file] ||= []).push(f);
    for (const [file, hits] of Object.entries(byFile)
      .sort((a, b) => b[1].length - a[1].length)
      .slice(0, 10))
      console.log(`  ${String(hits.length).padStart(4)}  ${file}`);
  }
  if (exempted.length) {
    const byFile = {};
    for (const f of exempted) (byFile[f.file] ||= []).push(f);
    console.log(
      `\nℹ️ 另有 ${exempted.length} 處在中文專屬表面（豁免 a）——這些是內容層的語言缺口，` +
        '要修是整頁翻譯不是接 i18n：\n',
    );
    for (const [file, hits] of Object.entries(byFile)
      .sort((a, b) => b[1].length - a[1].length)
      .slice(0, 8))
      console.log(`  ${file}（${hits.length}）→ ${hits[0].exempt}`);
  }
}

process.exit(!warnOnly && (hard.length || (strict && info.length)) ? 1 : 0);
