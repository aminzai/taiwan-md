/**
 * Build-time search index generator.
 *
 * Reads all markdown articles from knowledge/, tokenizes title/description/tags
 * with CJK bigrams + Latin words, builds serialized MiniSearch indexes.
 *
 * Output（2026-06-13 RAG Phase 0 — 六語系 per-lang shard）:
 *   public/api/search-minisearch-{lang}.json   ×6（每語言一份，client 按
 *     <html lang> 抓自己的 shard — 修復 ja/ko/es/fr 讀者搜尋零母語結果的洞，
 *     詳 reports/research/2026-06/rag-design-research-2026-06-13.md Phase 0）
 *   public/api/search-minisearch.json          legacy combined zh+en
 *     （back-compat：已部署/快取頁面的舊 client 仍指這個 URL，不能斷）
 *
 * 語言清單從 src/config/languages.mjs SSOT 讀（REFLEXES #20 architecture-as-data，
 * 新語言出生時本檔零改動）。
 */

import { readdir, readFile, writeFile, mkdir } from 'node:fs/promises';
import { resolve, join, basename } from 'node:path';
import matter from 'gray-matter';
import MiniSearch from 'minisearch';
import {
  ENABLED_LANGUAGE_CODES,
  DEFAULT_LANGUAGE,
} from '../../src/config/languages.mjs';

// ── Publish/update date lookup (src/data/content-dates.json, built by
// build-content-dates.mjs in the SAME prebuild sequence just before this
// script — package.json's prebuild chain was reordered 2026-08-23 to
// guarantee this file exists by the time we run). Fail-loud on missing: a
// silent skip would ship a search index with no dates and nobody would
// notice until a reader saw blank date chips on /search.
const CONTENT_DATES_PATH = resolve(
  process.cwd(),
  'src/data/content-dates.json',
);
let contentDatesRaw;
try {
  contentDatesRaw = JSON.parse(await readFile(CONTENT_DATES_PATH, 'utf-8'));
} catch (err) {
  console.error(
    `[search-index] FATAL: cannot read ${CONTENT_DATES_PATH} (run prebuild:content-dates first): ${err.message}`,
  );
  process.exit(1);
}
const DATES = contentDatesRaw.dates || {};
const CREATED = contentDatesRaw.created || {};

// Key alignment with build-content-dates.mjs's `knowledgePathToUrl()`: that
// generator's key is `${prefix}/${catSlug}/${slug}/` — NFC-normalized slug,
// trailing slash. This script's `doc.u` is `/${catSlug}/${name}` (default
// lang) or `/${lang}/${catSlug}/${name}` (other langs) — same shape minus the
// trailing slash, `name` un-normalized (raw fs basename). No decodeURIComponent
// needed: `u` is built here from plain JS strings, never percent-encoded.
function dateKeyForUrl(u) {
  return `${u.normalize('NFC')}/`;
}

const CATEGORY_MAP = {
  history: 'History',
  geography: 'Geography',
  culture: 'Culture',
  food: 'Food',
  art: 'Art',
  music: 'Music',
  technology: 'Technology',
  nature: 'Nature',
  people: 'People',
  politics: 'Politics',
  society: 'Society',
  economy: 'Economy',
  lifestyle: 'Lifestyle',
  // 2026-08-18 哲宇 directive「搜尋索引納入 about」：About 類（緣起故事／
  // Taiwan.md 寫 Taiwan.md／文章如何誕生／創作者長文…）之前整個資料夾不進
  // 索引，站內搜「珊瑚礁」「晶種」找不到自己是怎麼來的。URL 走 /about/<slug>，
  // client 只拿 u 當 href，不依 category 分流，加這一列零副作用。
  about: 'About',
};

// ── CJK bigram tokenizer ──

const isCJK = (cp) =>
  (cp >= 0x4e00 && cp <= 0x9fff) ||
  (cp >= 0x3400 && cp <= 0x4dbf) ||
  (cp >= 0xf900 && cp <= 0xfaff) ||
  (cp >= 0x3100 && cp <= 0x312f) ||
  // 2026-06-13 Phase 0：ja 假名 + ko 諺文也走 bigram（原本只有漢字，
  // ja/ko shard 的母語 query 打不中 — ko shard 421KB vs 他語 1.2MB+ 暴露的洞）
  (cp >= 0x3040 && cp <= 0x30ff) || // Hiragana + Katakana
  (cp >= 0x31f0 && cp <= 0x31ff) || // Katakana phonetic extensions
  (cp >= 0xac00 && cp <= 0xd7a3); // Hangul syllables

// 2026-08-23（issue #1496 dogfood 抓到）：原 LATIN_RE 只認 ASCII [a-z0-9]，
// 阿拉伯文／西里爾／天城文的母語詞整個掉出索引（ar/ru/hi 站內搜尋自出生
// 即 0 命中），vi/fr/es 帶變音符的詞被切碎。改用 Unicode 字母/數字類別，
// CJK 字元仍走下方 bigram 路徑（由 isCJK 排除，不會變成整串長 token）。
// 連字號夾在詞中時保留（covid-19 維持一個 token，與舊行為一致）。
const WORD_RE = /[\p{L}\p{N}][\p{L}\p{N}-]*[\p{L}\p{N}]|[\p{L}\p{N}]/gu;

function bigramTokenize(text) {
  if (!text) return '';
  const normalized = text.toLowerCase().normalize('NFKC');
  const tokens = [];

  // 非 CJK 詞（2+ chars）— 拉丁與所有 Unicode 文字系統（ar/ru/hi/vi…）。
  // CJK 字元先換成空白再取詞（CJK 走下方 bigram 路徑；直接跳過含 CJK 的
  // token 會把「台北101」裡的 101 一起丟掉）
  const nonCjkText = [...normalized]
    .map((ch) => (isCJK(ch.codePointAt(0)) ? ' ' : ch))
    .join('');
  for (const m of nonCjkText.matchAll(WORD_RE)) {
    if (m[0].length >= 2) tokens.push(m[0]);
  }

  // CJK bigrams（ja 漢字/假名混排與 ko 諺文走 NFKC 後的 Latin/CJK 雙路；
  // 假名與諺文不在 isCJK 範圍時由 MiniSearch prefix match 接住 Latin 化查詢，
  // 母語標題的 CJK 漢字 bigram 仍為主要召回路徑）
  const chars = [...normalized];
  for (let i = 0; i < chars.length - 1; i++) {
    const cp1 = chars[i].codePointAt(0);
    const cp2 = chars[i + 1].codePointAt(0);
    if (isCJK(cp1) && isCJK(cp2)) {
      tokens.push(chars[i] + chars[i + 1]);
    }
  }

  return tokens.join(' ');
}

// ── Scan one language's articles ──

async function scanLang(lang, startId) {
  const docs = [];
  let id = startId;
  const isDefault = lang === DEFAULT_LANGUAGE.code;

  for (const [slug, folder] of Object.entries(CATEGORY_MAP)) {
    const dirPath = isDefault
      ? resolve(process.cwd(), 'knowledge', folder)
      : resolve(process.cwd(), 'knowledge', lang, folder);
    try {
      const files = (await readdir(dirPath)).filter(
        (f) => f.endsWith('.md') && !f.startsWith('_'),
      );
      for (const file of files) {
        try {
          const { data } = matter(await readFile(join(dirPath, file), 'utf-8'));
          const name = basename(file, '.md');
          const title = data.title || name;
          const description = data.description || '';
          const tags = Array.isArray(data.tags)
            ? data.tags
            : data.tags
              ? [data.tags]
              : [];
          docs.push({
            id: id++,
            t: title,
            d: description,
            u: isDefault ? `/${slug}/${name}` : `/${lang}/${slug}/${name}`,
            tags,
            lang,
            title_bigram: bigramTokenize(title),
            desc_bigram: bigramTokenize(description),
            tags_bigram: bigramTokenize(tags.join(' ')),
          });
        } catch {
          console.warn(`[search] skipped ${lang}/${file}: YAML parse error`);
        }
      }
    } catch (err) {
      if (err.code !== 'ENOENT')
        console.warn(`[search] error reading ${dirPath}:`, err.message);
    }
  }

  return docs;
}

// ── Build one serialized MiniSearch index from docs ──

function buildIndex(docs) {
  const miniSearch = new MiniSearch({
    idField: 'id',
    fields: ['title_bigram', 'desc_bigram', 'tags_bigram'],
    storeFields: ['t', 'd', 'u', 'tags', 'lang', 'c', 'm'],
    tokenize: (text) => text.split(/\s+/).filter(Boolean),
    searchOptions: {
      boost: { title_bigram: 6, tags_bigram: 4, desc_bigram: 2 },
      prefix: true,
    },
  });
  miniSearch.addAll(docs);
  return JSON.stringify(miniSearch);
}

// ── Main ──

const apiDir = resolve(process.cwd(), 'public', 'api');
await mkdir(apiDir, { recursive: true });

const docsByLang = new Map();
let nextId = 0;
for (const lang of ENABLED_LANGUAGE_CODES) {
  const docs = await scanLang(lang, nextId);
  nextId += docs.length;
  docsByLang.set(lang, docs);
}

// Attach `c` (created/published) and `m` (modified) YYYY-MM-DD date fields
// from content-dates.json, and tally per-lang match rate to catch a
// key-format misalignment the moment it happens rather than as a silent
// blank-date regression on /search.
let totalDocs = 0;
let totalMatched = 0;
const matchLines = [];
let zhSampleMisses = [];
for (const [lang, docs] of docsByLang) {
  let matched = 0;
  for (const doc of docs) {
    const key = dateKeyForUrl(doc.u);
    const created = CREATED[key];
    const modified = DATES[key];
    if (created) doc.c = created.slice(0, 10);
    if (modified) doc.m = modified.slice(0, 10);
    if (created || modified) {
      matched++;
    } else if (lang === DEFAULT_LANGUAGE.code && zhSampleMisses.length < 5) {
      zhSampleMisses.push(key);
    }
  }
  totalDocs += docs.length;
  totalMatched += matched;
  const pct = docs.length ? ((matched / docs.length) * 100).toFixed(1) : '0.0';
  matchLines.push(`${lang}=${matched}/${docs.length} (${pct}%)`);
}
const totalPct = totalDocs
  ? ((totalMatched / totalDocs) * 100).toFixed(1)
  : '0.0';
console.log(
  `[search-index] date match: ${totalMatched}/${totalDocs} docs (${totalPct}%) — ${matchLines.join(', ')}`,
);

const zhDocs = docsByLang.get(DEFAULT_LANGUAGE.code) || [];
const zhMatched = zhDocs.filter((d) => d.c || d.m).length;
const zhPct = zhDocs.length ? (zhMatched / zhDocs.length) * 100 : 0;
if (zhPct < 95) {
  console.error(
    `[search-index] FATAL: ${DEFAULT_LANGUAGE.code} date match rate ${zhPct.toFixed(1)}% < 95% — key format misaligned with content-dates.json. Sample unmatched keys:\n` +
      zhSampleMisses.map((k) => `  ${k}`).join('\n'),
  );
  process.exit(1);
}

// Per-lang shards ×6
for (const [lang, docs] of docsByLang) {
  const serialized = buildIndex(docs);
  await writeFile(
    join(apiDir, `search-minisearch-${lang}.json`),
    serialized,
    'utf-8',
  );
  console.log(
    `[search] shard ${lang}: ${docs.length} docs, ${(serialized.length / 1024).toFixed(0)} KB → search-minisearch-${lang}.json`,
  );
}

// Legacy combined zh+en（back-compat：舊 client / 快取 HTML 仍 fetch 這個 URL）
const legacyDocs = [
  ...(docsByLang.get(DEFAULT_LANGUAGE.code) || []),
  ...(docsByLang.get('en') || []),
];
const legacySerialized = buildIndex(legacyDocs);
await writeFile(
  join(apiDir, 'search-minisearch.json'),
  legacySerialized,
  'utf-8',
);
console.log(
  `[search] legacy combined zh+en: ${legacyDocs.length} docs, ${(legacySerialized.length / 1024).toFixed(0)} KB → search-minisearch.json`,
);

// Plain-array fallback for Layout.astro's indexOf path (used only when
// MiniSearch fails to load). 2026-06-13 EVO-A2: this REPLACES the duplicate
// runtime route src/pages/api/search-index.json.ts, which re-scanned knowledge/
// with its OWN category map that had drifted (missing politics, zh+en only).
// Derived from legacyDocs = the same single scan → zh+en, all categories, no
// drift. Strip the bigram fields; keep the {t,d,u,tags,lang} shape the old
// route emitted so Layout's fallback is unchanged.
const fallbackDocs = legacyDocs.map((d) => ({
  t: d.t,
  d: d.d,
  u: d.u,
  tags: d.tags,
  lang: d.lang,
}));
await writeFile(
  join(apiDir, 'search-index.json'),
  JSON.stringify(fallbackDocs),
  'utf-8',
);
console.log(
  `[search] fallback plain index: ${fallbackDocs.length} docs (zh+en) → search-index.json`,
);
