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
 * 本工具查五件事：
 *
 *   1. SIMPLIFIED_LEAK — 任何語言區塊出現無歧義簡體字。Taiwan.md 全站不該有簡體。
 *   2. UNTRANSLATED_CJK — 非 CJK 語言的區塊裡整串都是中文（= 根本沒翻）。
 *   3. TABLE_DRIFT — 前端字串表的語言集合落後 LANGUAGES_REGISTRY（靜默 fallback 英文）。
 *   4. PRC_TERM — zh-TW 區塊用了中國用語（2026-08-12 新增，見下）。
 *   5. CJK_FRAGMENT — 非 CJK 語言區塊夾著漢字碎片（2026-08-12 新增，見下）。
 *
 * ── 為什麼 v1 的三件事不夠（2026-08-12 讀者連續回報第三天）────────────────
 *
 * v1 三查全部是**字形層**：它問「這些字長什麼樣子」。隔天讀者一次送來兩則，
 * 兩則都從字形層底下穿過去：
 *
 *   #1322  `/semiont/` 的「網路海量知識」——「海量」是中國用語，台灣說「大量」。
 *          它是正體字寫的，SIMPLIFIED_LEAK 當然放行。**字形對，詞彙錯。**
 *          諷刺的是 Taiwan.md 自己維護著 2,394 條的用語保存詞庫，
 *          `data/terminology/巨量.yaml` 白紙黑字寫著 china: 海量——
 *          我們有詞庫，卻從來沒有任何閘門拿它來檢查自己的介面。
 *
 *   #1320  `/companies/` 的公司名「巨大 Giant」——同一個 key 在 ko 區塊是
 *          「Giant 쥐다」（把「巨大」機器翻成韓文動詞「抓握」），在 ar/en/fr/es
 *          區塊是「Giant Manufacturing 巨大」（漢字漂在阿拉伯文與拉丁文介面裡）。
 *          UNTRANSLATED_CJK 有 8 字下限與 50% 佔比門檻，這種「短字串夾幾個漢字」
 *          全數低於門檻。**專有名詞被當成可翻譯的句子翻了。**
 *
 * 兩則是同一個形狀：字形對了，字義錯了。所以 v2 補的兩查都在**語意層**。
 *
 * ⚠️ 必要豁免（2026-08-11 實測：不寫進去假陽性率 82%，第一天就會被當噪音關掉）
 *
 *   a. ja 區塊整個跳過簡體檢查——日文新字體的 湾/数/点 與簡體同形，91 行全誤報
 *   b. QUOTED_EVIDENCE——about.ts 逐字引用騰訊 Hunyuan 拒答台灣主題的那 40 bytes，
 *      是 MANIFESTO 敘事的證據本身。改掉它等於刪證據
 *   c. TW_ACCEPTED_VARIANTS——台灣標準本來就採用的「簡體長相」字（游/台/表/污…），
 *      沿用 terminology-charcheck.js 已實戰校準的白名單
 *   d. PRC_TERM 只收**無語境歧義**的詞（沿用 terminology-prose-fix.py 已在 889 篇
 *      文章上實戰過的 A 類表）。像「質量」「程序」這種要讀上下文才判得準的，
 *      留給 terminology-prose-fix.py 的語境規則，不進這道閘門——
 *      閘門寧可漏，不可誤殺（2026-08-09 LESSONS：假陽性高的閘門會讓人改壞內容換綠燈）
 *   e. CJK_FRAGMENT 放行 CJK_OK_KEYS——少數 key 本來就該保留漢字原文
 *      （站名 Taiwan.md、逐字引用的證據、刻意並列原文的詞條）
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
const QUOTED_EVIDENCE = ['无法给到相关内容', '我无法'];

// 用 CJK 書寫系統的語言：這些語言出現漢字是正常的
const CJK_LANGS = new Set(['zh-TW', 'ja', 'ko']);
// 日文新字體與簡體同形，簡體檢查整個跳過
const SKIP_SIMPLIFIED = new Set(['ja']);

const CJK_RE = /[㐀-鿿豈-﫿]/;
const LANG_HEADER = /^\s{0,4}['"]?([a-zA-Z-]{2,7})['"]?\s*:\s*\{\s*$/;

/**
 * 中國用語 → 台灣用語。**只收無語境歧義的**（豁免 d）。
 *
 * 前 25 條逐字沿用 scripts/tools/terminology-prose-fix.py 的 A_REPLACEMENTS
 * ——那份表已經在 889 篇文章上跑過，是實戰校準過的安全集合。兩邊要一起改，
 * 不要各自維護（同一個判準散成兩份 = REFLEXES #83 兩把尺）。
 *
 * 末尾是本閘門自己加的，每條都要能在 data/terminology/ 找到對應詞條。
 */
const PRC_TERMS = [
  ['視頻', '影片'],
  ['軟件', '軟體'],
  ['硬件', '硬體'],
  ['博主', '部落客'],
  ['點贊', '按讚'],
  ['互聯網', '網際網路'],
  ['內存', '記憶體'],
  ['人工智能', '人工智慧'],
  ['操作系統', '作業系統'],
  ['信息', '資訊'],
  ['服務器', '伺服器'],
  ['屏幕', '螢幕'],
  ['打印', '列印'],
  ['盒飯', '便當'],
  ['出租車', '計程車'],
  ['移動設備', '行動裝置'],
  ['移動支付', '行動支付'],
  ['移動端', '行動端'],
  ['用戶', '使用者'],
  ['賬號', '帳號'],
  ['賬戶', '帳戶'],
  ['大數據', '大資料'],
  ['雲計算', '雲端運算'],
  ['下載量', '下載次數'],
  // ⚠️ 刻意不收「代碼 → 程式碼」。A 類表收它是因為那張表跑在文章散文上，
  //    那裡「代碼」幾乎都指 source code。但 UI 字串裡「代碼」常常是識別碼
  //    的正常台灣用法（行政區代碼、郵遞區號、股票代碼），2026-08-12 首跑
  //    5 筆命中有 2 筆是 taiwanShape 的行政區代碼表 = 假陽性 40%。
  //    語境詞留給 terminology-prose-fix.py 的語境規則，不進這道閘門。
  // ↓ 本閘門新增。data/terminology/巨量.yaml — china: 海量 / taiwan: 巨量。
  //   讀者 CJ C 在 #1322 建議「大量」，一般語境比「巨量」自然
  //   （「巨量」在台灣幾乎只黏在「巨量資料」上），採讀者的說法。
  ['海量', '大量'],
];

/**
 * 允許夾漢字的 key（豁免 e）。比對用 includes。
 * 加東西進來前先問：這個漢字對該語言的讀者有意義嗎？沒有就是該修不是該豁免。
 */
const CJK_OK_KEYS = [
  'hunyuan',
  'refusal',
  // 語言選單的 endonym：日文那格本來就該寫「日本語」，跟德文那格寫 Deutsch
  // 同一個道理。這是慣例不是漏譯（2026-08-12 首跑 18 筆全是這個）。
  '.japanese',
  '.chinese',
  '.korean',
  '.traditional',
  '.lang.ja',
  '.lang.zh',
  '.lang.ko',
];

/**
 * 每個語言「自己的書寫系統」。UNREADABLE_FOR_LOCALE 用它判斷
 * 「這個字串有沒有留給這語言的讀者任何讀得到的東西」。
 * 拉丁字母系語言共用 LATIN_RE。
 */
const LATIN_RE = /[A-Za-z]/;
const OWN_SCRIPT = {
  ar: /[؀-ۿ]/,
  ru: /[Ѐ-ӿ]/,
  hi: /[ऀ-ॿ]/,
};
const ownScriptRe = (lang) => OWN_SCRIPT[lang] || LATIN_RE;

function prcTerms(str) {
  return PRC_TERMS.filter(([bad]) => str.includes(bad));
}

/** 抽出 `'key': 'value'` 這行的 key 與 value（單雙引號都收） */
function parseEntry(line) {
  const m = line.match(
    /^\s*['"]?([\w.$-]+)['"]?\s*:\s*(['"])((?:\\.|(?!\2).)*)\2/,
  );
  return m ? { key: m[1], value: m[3] } : null;
}

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

    const entry = parseEntry(line);

    // 4. zh-TW 用了中國用語（字形對、詞彙錯 — #1322）
    if (lang === 'zh-TW' && entry) {
      const hits = prcTerms(entry.value);
      for (const [bad, good] of hits) {
        findings.push({
          kind: 'PRC_TERM',
          file: rel,
          lang,
          line: i + 1,
          chars: `${bad} → ${good}`,
          text: line.trim().slice(0, 100),
        });
      }
    }

    // 5. 這個字串沒留給該語言的讀者任何讀得到的東西（#1320 的真正形狀）
    //
    //    第一版寫成「非 CJK 語言區塊出現漢字就報」，實測 319 筆、假陽性 ~95%：
    //    en 的 'Taiwan Semiconductor 台積電'、各語言選單的 '🇯🇵 日本語' 都是
    //    刻意的雙語標示與 endonym 慣例，報它們只會讓人把好東西刪掉換綠燈
    //    （2026-08-09 LESSONS gate-triggers-content-degradation-incentive）。
    //
    //    真正壞掉的判準不是「有沒有漢字」，是「**扣掉漢字之後還剩什麼**」：
    //    ar 的 'الاسم' 有阿拉伯文、en 的 'TSMC 台積電' 有拉丁字母，讀者都接得住；
    //    ar 的 '國泰金控' 兩者皆無 —— 阿拉伯讀者看到的就是一串完全讀不到的字。
    //    改成這個判準後假陽性歸零（見 §校準紀錄）。
    if (!CJK_LANGS.has(lang) && entry) {
      const exempt = CJK_OK_KEYS.some((k) => entry.key.includes(k));
      const hasCJK = CJK_RE.test(entry.value);
      const readable = ownScriptRe(lang).test(entry.value);
      if (hasCJK && !readable && !exempt) {
        findings.push({
          kind: 'UNREADABLE_FOR_LOCALE',
          file: rel,
          lang,
          line: i + 1,
          chars: `無 ${lang} 可讀字元`,
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
