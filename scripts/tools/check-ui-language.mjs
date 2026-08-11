#!/usr/bin/env node
/**
 * check-ui-language.mjs — UI 字串層的語言正確性閘門
 *
 * 文章層（knowledge/）早就有 cjk-leak-check.py 守著「這篇譯文是不是還留著中文」。
 * src/i18n/*.ts 這層一支都沒有——而 UI 字串出現在每一頁的頂端與底部，曝光量
 * 遠高於任何單篇文章。保護密度跟曝光量成反比，於是同一種病靠讀者回報了三次：
 *
 *   2026-08-06  俄文讀者看了半年的烏克蘭文介面
 *   2026-08-10  讀者 @Pigcasso6 回報 taiwan-shape / bench / 回饋模組多語未譯（#1311/#1312/#1314）
 *   2026-08-11  ar 區塊整段是簡體中文且用中國詞彙（#1318）
 *
 * 本工具查三件事：
 *
 *   1. SIMPLIFIED_LEAK — 任何語言區塊出現無歧義簡體字。Taiwan.md 全站不該有簡體。
 *   2. UNTRANSLATED_CJK — 非 CJK 語言的區塊裡整串都是中文（= 根本沒翻）。
 *   3. TABLE_DRIFT — 前端字串表的語言集合落後 LANGUAGES_REGISTRY（靜默 fallback 英文）。
 *
 * ⚠️ 三類必要豁免（2026-08-11 實測：不寫進去假陽性率 82%，第一天就會被當噪音關掉）
 *
 *   a. ja 區塊整個跳過簡體檢查——日文新字體的 湾/数/点 與簡體同形，91 行全誤報
 *   b. QUOTED_EVIDENCE——about.ts 逐字引用騰訊 Hunyuan 拒答台灣主題的那 40 bytes，
 *      是 MANIFESTO 敘事的證據本身。改掉它等於刪證據
 *   c. TW_ACCEPTED_VARIANTS——台灣標準本來就採用的「簡體長相」字（游/台/表/污…），
 *      沿用 terminology-charcheck.js 已實戰校準的白名單
 *
 * 用法：
 *   node scripts/tools/check-ui-language.mjs           # 報告（exit 1 = 有真陽性）
 *   node scripts/tools/check-ui-language.mjs --json
 *   npm run check:ui-lang
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import * as OpenCC from 'opencc-js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');
const I18N_DIR = path.join(ROOT, 'src/i18n');

const s2t = OpenCC.Converter({ from: 'cn', to: 't' });
const t2s = OpenCC.Converter({ from: 't', to: 'cn' });

// 台灣標準採用的 dual-status 字（跟 terminology-charcheck.js 同一份，勿各自維護）
const TW_ACCEPTED_VARIANTS = new Set(
  Array.from('群里吃台峰托雇床霉游秘采布污表制复范志于后系着克涂松咨采夹'),
);

// 正體本字，OpenCC candidate 判定的已知誤判（2026-08-11 全庫實測反推）
const TRADITIONAL_FALSE_POSITIVES = new Set(Array.from('栗粽岳郁凶'));

// 逐字引用 PRC 模型拒答訊息——是證據不是外洩
const QUOTED_EVIDENCE = ['无法给到相关内容'];

// 用 CJK 書寫系統的語言：這些語言出現漢字是正常的
const CJK_LANGS = new Set(['zh-TW', 'ja', 'ko']);
// 日文新字體與簡體同形，簡體檢查整個跳過
const SKIP_SIMPLIFIED = new Set(['ja']);

const CJK_RE = /[㐀-鿿豈-﫿]/;
const LANG_HEADER = /^\s{0,4}['"]?([a-zA-Z-]{2,7})['"]?\s*:\s*\{\s*$/;

function leakedSimplified(str) {
  const out = [];
  for (const c of str) {
    if (!CJK_RE.test(c)) continue;
    if (TW_ACCEPTED_VARIANTS.has(c) || TRADITIONAL_FALSE_POSITIVES.has(c))
      continue;
    if (s2t(c) !== c && t2s(c) === c) out.push(c);
  }
  return out;
}

function isQuotedEvidence(line) {
  return QUOTED_EVIDENCE.some((q) => line.includes(q));
}

/** 一整串值幾乎都是漢字 = 這個非 CJK 語言根本沒翻到 */
function looksUntranslated(value) {
  const chars = Array.from(value).filter((c) => /\S/.test(c));
  if (chars.length < 8) return false; // 太短：可能是專有名詞
  const cjk = chars.filter((c) => CJK_RE.test(c)).length;
  return cjk / chars.length > 0.5;
}

function readRegistryCodes() {
  const src = fs.readFileSync(
    path.join(ROOT, 'src/config/languages.ts'),
    'utf8',
  );
  return [...src.matchAll(/^\s*code:\s*'([a-zA-Z-]+)'/gm)].map((m) => m[1]);
}

function scanFile(file) {
  const rel = path.relative(ROOT, file);
  const lines = fs.readFileSync(file, 'utf8').split('\n');
  const findings = [];
  let lang = null;
  lines.forEach((line, i) => {
    const h = LANG_HEADER.exec(line);
    if (h) {
      lang = h[1];
      return;
    }
    if (!lang) return;
    if (isQuotedEvidence(line)) return;

    if (!SKIP_SIMPLIFIED.has(lang)) {
      const chars = leakedSimplified(line);
      if (chars.length) {
        findings.push({
          kind: 'SIMPLIFIED_LEAK',
          file: rel,
          lang,
          line: i + 1,
          chars: [...new Set(chars)].join(''),
          text: line.trim().slice(0, 100),
        });
      }
    }

    if (!CJK_LANGS.has(lang)) {
      const m =
        line.match(/:\s*'([^']{8,})'/) || line.match(/:\s*"([^"]{8,})"/);
      if (m && looksUntranslated(m[1])) {
        findings.push({
          kind: 'UNTRANSLATED_CJK',
          file: rel,
          lang,
          line: i + 1,
          text: line.trim().slice(0, 100),
        });
      }
    }
  });
  return findings;
}

function checkTableDrift() {
  const registry = readRegistryCodes();
  const out = [];
  const widget = path.join(ROOT, 'src/scripts/feedback/i18n.ts');
  if (fs.existsSync(widget)) {
    const src = fs.readFileSync(widget, 'utf8');
    const tbl = src.match(
      /const TABLE: Record<string, FeedbackStrings> = \{([\s\S]*?)\n\};/,
    );
    if (tbl) {
      const have = new Set(
        [...tbl[1].matchAll(/^\s*'?([a-zA-Z-]{2,7})'?\s*[,:]/gm)].map(
          (m) => m[1],
        ),
      );
      const missing = registry.filter((c) => !have.has(c));
      if (missing.length)
        out.push({
          kind: 'TABLE_DRIFT',
          file: 'src/scripts/feedback/i18n.ts',
          detail: `feedback widget TABLE 缺 ${missing.join(', ')}（會靜默 fallback 英文）`,
        });
    }
  }
  return out;
}

const asJson = process.argv.includes('--json');
const files = fs
  .readdirSync(I18N_DIR)
  .filter((f) => f.endsWith('.ts') && f !== 'utils.ts')
  .map((f) => path.join(I18N_DIR, f));

let findings = files.flatMap(scanFile).concat(checkTableDrift());

if (asJson) {
  console.log(JSON.stringify({ findings }, null, 2));
} else {
  console.log('# UI 字串語言閘門\n');
  if (!findings.length) {
    console.log('✅ 無簡體外洩、無整串未譯、字串表與語言註冊表同步');
  } else {
    const byKind = {};
    for (const f of findings) (byKind[f.kind] ||= []).push(f);
    for (const [kind, list] of Object.entries(byKind)) {
      console.log(`\n## ${kind}（${list.length}）\n`);
      for (const f of list.slice(0, 40)) {
        if (f.kind === 'TABLE_DRIFT') console.log(`  ${f.file} — ${f.detail}`);
        else
          console.log(
            `  ${f.file} [${f.lang}] L${f.line}` +
              (f.chars ? ` 「${f.chars}」` : '') +
              `\n     ${f.text}`,
          );
      }
      if (list.length > 40) console.log(`  … 另 ${list.length - 40} 筆`);
    }
    console.log(`\n總計 ${findings.length} 筆`);
  }
}

process.exit(findings.length ? 1 : 0);
