#!/usr/bin/env node
/**
 * heading-id-audit.mjs — OBSERVER-QUEUE #44 標題錨點 id 產生器：新舊規則對照
 *
 * 為什麼這支腳本 import 真正的 render 函式，而不是自己重寫規則去量：
 * 2026-08-28「徹底處理那一輪」用 Python 重寫了一份新舊 slug 函式跑全站對照，
 * 得到「所有語言 0 個 id 會變」的乾淨錯答案——Python 的 `\w` 吃 Unicode 字母，
 * JS 的 `\w` 只吃 ASCII，兩邊 regex 長得一模一樣，量出的卻是完全不同的行為。
 * 見 docs/semiont/memory/2026-08-28-005518-footnote-cards.md「徹底處理那一輪」。
 *
 * 這支腳本從 src/utils/article-render.ts 直接 import `slugifyHeadingId`
 * （新規則的正式實作，也是 renderer.heading / TableOfContents.astro 唯一呼叫的
 * 那一支），舊規則則是 2026-09-05 修復前 renderer.heading 用過的正式行為，原封
 * 不動抄一份到這裡當基準（同一個語言 JS 對 JS，不是拿別的語言的 regex 語意去猜）。
 *
 * 用法（.ts 動態 import 需要 Node 型別剝離旗標）：
 *   node --experimental-strip-types scripts/tools/heading-id-audit.mjs
 *   或：NODE_OPTIONS=--experimental-strip-types node scripts/tools/heading-id-audit.mjs
 *
 * ── --toc 模式（OBSERVER-QUEUE #44 補強 2，2026-09-05 新增）──────────────
 *   node scripts/tools/heading-id-audit.mjs --toc
 * 掃 dist/**\/*.html：每個有 `<nav id="toc">` 的頁面，把 TOC 裡每個
 * `href="#x"` 拿去跟整頁所有 `id="x"` 比對，抓「TOC 連結指到一個頁面上根本不
 * 存在的 id」的頁面數（TableOfContents.astro 的 extractHeadings regex 舊 bug
 * 造成，見該檔案內註解）。跟上面度量標題「字面」的預設模式是兩件事：這裡量的
 * 是「錨點連結有沒有真的可以跳」，前提是 dist/ 已經跑過 `npx astro build`
 * （先跑 `bash scripts/core/sync.sh && npx astro build`）。
 *
 * 掃描範圍：knowledge/**\/*.md，依路徑分語言——
 *   knowledge/<Category>/*.md        → zh-TW（預設語言，無語言子目錄）
 *   knowledge/<lang>/<Category>/*.md → 該語言（lang 為 12 語 enabled code 之一）
 * 排除：knowledge/resources、knowledge/.obsidian、非 .md 檔（_slug-map.json 等）、
 *       _Home.md / _*.md 這類非文章 hub 檔仍計入（它們也是真的頁面，一樣有標題）。
 *
 * 度量口徑：
 *   - total：該語言全部標題（H1-H6，抓 marked heading token 會拿到的原文列，
 *     即 `#+ ` 之後、行尾之前的原始 markdown，跳過 fenced code block 內的 `#` 行）
 *   - degenerate：id 退化成空字串或純連字號（`/^-*$/`）——即「整個標題被規則
 *     剝到只剩空殼」，是 ko/ru/ar/hi 的主要症狀
 *   - duplicate：**同一個檔案內**兩個以上標題算出相同的非空 id 的「多出來的」
 *     個數（總數−該檔內相異 id 數，逐檔加總）。用檔案為單位而不是整語言，因為
 *     錨點衝突只在同一頁的 TOC / #fragment 導覽裡才會真的斷掉，跨檔同名 id 不影響
 *     任何人（不同頁面各自的 DOM）。
 */
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../../', import.meta.url));
const KNOWLEDGE_DIR = join(ROOT, 'knowledge');
const DIST_DIR = join(ROOT, 'dist');

// ── --toc 模式：走完全獨立的 dist 掃描路徑，跑完直接 exit，不落到下面
// 讀 knowledge/ + 動態 import article-render.ts 的語言對照邏輯 ──────────────
if (process.argv.includes('--toc')) {
  runTocAudit();
  process.exitCode = 0;
} else {
  await runLangAudit();
}

function walkFiles(dir, suffix) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) out.push(...walkFiles(full, suffix));
    else if (entry.endsWith(suffix)) out.push(full);
  }
  return out;
}

/**
 * 掃 dist/**\/*.html：每個有 `<nav id="toc">` 的頁面，把 TOC 裡的每個
 * `href="#x"` 拿去跟整頁所有 `id="x"` 比對。用「整頁所有 id」而不是只比對
 * h2/h3 的 id，是因為 TOC 連結指到的目標本來就是頁面上某個元素的 id 屬性，
 * 只要那個 id 存在於頁面 DOM 裡連結就能跳，不需要額外假設它一定長在標題上。
 */
function runTocAudit() {
  if (!existsSync(DIST_DIR)) {
    console.error(
      '❌ dist/ 不存在。先跑：bash scripts/core/sync.sh && npx astro build',
    );
    process.exitCode = 1;
    return;
  }
  const htmlFiles = walkFiles(DIST_DIR, '.html');

  let pagesWithToc = 0;
  let pagesBroken = 0;
  let totalHrefs = 0;
  let totalBrokenHrefs = 0;
  const samples = [];

  for (const file of htmlFiles) {
    const html = readFileSync(file, 'utf8');
    const tocMatch = html.match(/<nav\b[^>]*\bid="toc"[^>]*>([\s\S]*?)<\/nav>/);
    if (!tocMatch) continue;
    pagesWithToc++;

    const hrefs = [...tocMatch[1].matchAll(/href="#([^"]*)"/g)].map(
      (m) => m[1],
    );
    if (hrefs.length === 0) continue;

    const ids = new Set([...html.matchAll(/\bid="([^"]*)"/g)].map((m) => m[1]));

    const brokenHrefs = hrefs.filter((h) => !ids.has(h));
    totalHrefs += hrefs.length;
    totalBrokenHrefs += brokenHrefs.length;
    if (brokenHrefs.length > 0) {
      pagesBroken++;
      if (samples.length < 5) {
        samples.push({ page: relative(DIST_DIR, file), brokenHrefs });
      }
    }
  }

  console.log(`有 TOC 的頁面數：${pagesWithToc}`);
  console.log(
    `至少一條連結壞的頁面數：${pagesBroken}（${
      pagesWithToc ? ((pagesBroken / pagesWithToc) * 100).toFixed(1) : '0.0'
    }%）`,
  );
  console.log(`壞連結總數：${totalBrokenHrefs} / ${totalHrefs}`);
  if (samples.length > 0) {
    console.log(`\n樣本（最多 5 個）：`);
    for (const s of samples) {
      console.log(`  ${s.page}`);
      console.log(`    壞 href: ${s.brokenHrefs.join(', ')}`);
    }
  }
}

// ── 預設模式：12 語新舊 slug 規則對照（原本這支腳本唯一做的事，2026-09-05
// 補強 2 加 --toc 模式時包成函式，邏輯本身一行沒動）──────────────────────
async function runLangAudit() {
  // 12 個目前 enabled 的語言（src/config/languages.ts LANGUAGES，排除 de：
  // enabled:false，尚未出生）。zh-TW 沒有語言子目錄，用 Category 資料夾偵測。
  const LANG_DIRS = new Set([
    'en',
    'ja',
    'ko',
    'es',
    'fr',
    'vi',
    'id',
    'pt',
    'hi',
    'ar',
    'ru',
  ]);
  const EXCLUDE_TOP = new Set(['resources', '.obsidian']);

  // ── 舊規則（2026-09-05 修復前 renderer.heading 的正式行為，原樣抄一份當基準）──
  function oldSlugify(text) {
    return text
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^\w一-鿿-]/g, '')
      .slice(0, 60);
  }

  // ── 新規則：直接 import 正式實作，不重寫 ─────────────────────────────────
  const { slugifyHeadingId: newSlugify } =
    await import('../../src/utils/article-render.ts');

  /** 從一份 markdown 抽出所有標題原文列（略過 frontmatter 與 fenced code block）。 */
  function extractHeadingTexts(md) {
    const lines = md.split('\n');
    const headings = [];
    let inFence = false;
    let i = 0;
    // frontmatter：檔案開頭 --- ... --- 整段跳過
    if (lines[0] === '---') {
      i = 1;
      while (i < lines.length && lines[i] !== '---') i++;
      i++; // 跳過結尾的 ---
    }
    for (; i < lines.length; i++) {
      const line = lines[i];
      const fenceMatch = /^\s*(```+|~~~+)/.exec(line);
      if (fenceMatch) {
        inFence = !inFence;
        continue;
      }
      if (inFence) continue;
      const h = /^(#{1,6})\s+(.+?)\s*$/.exec(line);
      if (h) headings.push(h[2]);
    }
    return headings;
  }

  function walkMdFiles(dir) {
    const out = [];
    for (const entry of readdirSync(dir)) {
      const full = join(dir, entry);
      const st = statSync(full);
      if (st.isDirectory()) {
        out.push(...walkMdFiles(full));
      } else if (entry.endsWith('.md')) {
        out.push(full);
      }
    }
    return out;
  }

  function langForFile(relPath) {
    const seg = relPath.split('/')[0];
    return LANG_DIRS.has(seg) ? seg : 'zh-TW';
  }

  /** 每語言累積量：total / degenerate(old,new) / duplicate(old,new) */
  function makeBucket() {
    return {
      total: 0,
      degenerateOld: 0,
      degenerateNew: 0,
      duplicateOld: 0,
      duplicateNew: 0,
    };
  }

  const isDegenerate = (id) => /^-*$/.test(id);

  const buckets = new Map();
  const bucketFor = (lang) => {
    if (!buckets.has(lang)) buckets.set(lang, makeBucket());
    return buckets.get(lang);
  };

  const topLevel = readdirSync(KNOWLEDGE_DIR).filter((e) => {
    if (EXCLUDE_TOP.has(e)) return false;
    const full = join(KNOWLEDGE_DIR, e);
    return statSync(full).isDirectory();
  });

  for (const top of topLevel) {
    const files = walkMdFiles(join(KNOWLEDGE_DIR, top));
    for (const file of files) {
      const rel = relative(KNOWLEDGE_DIR, file);
      const lang = langForFile(rel);
      const md = readFileSync(file, 'utf8');
      const headingTexts = extractHeadingTexts(md);
      if (headingTexts.length === 0) continue;

      const bucket = bucketFor(lang);
      const oldIds = headingTexts.map(oldSlugify);
      const newIds = headingTexts.map(newSlugify);

      bucket.total += headingTexts.length;
      for (const id of oldIds) if (isDegenerate(id)) bucket.degenerateOld++;
      for (const id of newIds) if (isDegenerate(id)) bucket.degenerateNew++;

      // per-file 重複計數：總數 - 相異數 = 多出來的碰撞次數。
      // 注意：空字串 / 純連字號本身也可能互撞（都算「重複」），
      // 這裡不排除 degenerate id——它們一樣是「兩個標題共用一個 id」的真實症狀。
      const countDupes = (ids) => {
        const seen = new Map();
        for (const id of ids) seen.set(id, (seen.get(id) || 0) + 1);
        let dup = 0;
        for (const count of seen.values()) if (count > 1) dup += count - 1;
        return dup;
      };
      bucket.duplicateOld += countDupes(oldIds);
      bucket.duplicateNew += countDupes(newIds);
    }
  }

  // ── 輸出：12 語新舊對照表 ────────────────────────────────────────────────
  const LANG_ORDER = [
    'zh-TW',
    'en',
    'ja',
    'ko',
    'es',
    'fr',
    'vi',
    'id',
    'pt',
    'hi',
    'ar',
    'ru',
  ];

  const rows = LANG_ORDER.map((lang) => {
    const b = buckets.get(lang) || makeBucket();
    return { lang, ...b };
  });

  const pad = (s, n) => String(s).padStart(n);
  const padEnd = (s, n) => String(s).padEnd(n);

  console.log(
    padEnd('lang', 6),
    pad('total', 7),
    '|',
    pad('deg(old)', 9),
    pad('deg(new)', 9),
    '|',
    pad('dup(old)', 9),
    pad('dup(new)', 9),
  );
  console.log('-'.repeat(70));
  for (const r of rows) {
    console.log(
      padEnd(r.lang, 6),
      pad(r.total, 7),
      '|',
      pad(r.degenerateOld, 9),
      pad(r.degenerateNew, 9),
      '|',
      pad(r.duplicateOld, 9),
      pad(r.duplicateNew, 9),
    );
  }

  const grand = rows.reduce(
    (acc, r) => ({
      total: acc.total + r.total,
      degenerateOld: acc.degenerateOld + r.degenerateOld,
      degenerateNew: acc.degenerateNew + r.degenerateNew,
      duplicateOld: acc.duplicateOld + r.duplicateOld,
      duplicateNew: acc.duplicateNew + r.duplicateNew,
    }),
    {
      total: 0,
      degenerateOld: 0,
      degenerateNew: 0,
      duplicateOld: 0,
      duplicateNew: 0,
    },
  );
  console.log('-'.repeat(70));
  console.log(
    padEnd('TOTAL', 6),
    pad(grand.total, 7),
    '|',
    pad(grand.degenerateOld, 9),
    pad(grand.degenerateNew, 9),
    '|',
    pad(grand.duplicateOld, 9),
    pad(grand.duplicateNew, 9),
  );
}
