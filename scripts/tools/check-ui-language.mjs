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
 * 本工具查六件事：
 *
 *   1. SIMPLIFIED_LEAK — 任何語言區塊出現無歧義簡體字。Taiwan.md 全站不該有簡體。
 *   2. UNTRANSLATED_CJK — 非 CJK 語言的區塊裡整串都是中文（= 根本沒翻）。
 *   3. TABLE_DRIFT — 前端字串表的語言集合落後 LANGUAGES_REGISTRY（靜默 fallback 英文）。
 *   4. PRC_TERM — zh-TW 區塊用了中國用語（2026-08-12 新增，見下）。
 *   5. UNREADABLE_FOR_LOCALE — 非 CJK 語言的值裡有漢字、卻沒有半個該語言讀得到的字元
 *      （2026-08-12 新增，是 #1320 的真正形狀；見 §5 註解）。
 *   6. CJK_FRAGMENT — 非 CJK 語言的值裡，漢字碎片**夾在**該語言的字裡（2026-08-17 新增，
 *      ⚠️ 警示級不擋 push；見 §6 註解）。
 *
 * ── 換行的值看不見（2026-08-17 v3）────────────────────────────────────────
 *
 * v1/v2 只認 `'key': 'value'` 寫在同一行的條目。prettier 會把長值折到下一行：
 *
 *     'data.category.1.item.1.desc':
 *       '2020 年，工程師用這裡的資料在 72 小時內做出口罩地圖，⋯',
 *
 * 於是 UNTRANSLATED_CJK / UNREADABLE_FOR_LOCALE / PRC_TERM 全部對這種條目失明——
 * 而**越長的值越可能是整段沒翻的句子**，閘門恰好漏掉最該抓的那一批：en 區塊
 * 六條 `data.category.*.desc` 整句中文、ar 區塊一句阿拉伯文中間夾著「民間」，
 * 全庫掃描報「全綠」。v3 把「key 在這行、值在下一行」當同一個條目解析。
 * （SIMPLIFIED_LEAK 逐行看字形，本來就不受影響。）
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
 *   e. UNREADABLE_FOR_LOCALE / CJK_FRAGMENT 放行 CJK_OK_KEYS——少數 key 本來就該
 *      保留漢字原文（站名 Taiwan.md、逐字引用的證據、刻意並列原文的詞條）
 *   f. CJK_FRAGMENT 不管**邊緣**的漢字：`'Taiwan Semiconductor 台積電'` 這種
 *      「拉丁名 + 漢字原名」的雙語標示是 en/fr/es 刻意的設計，只有漢字**夾在**
 *      該語言的字中間（`تطوير民間، نموذج`）才是翻到一半掉回中文；括號 / 引號裡的
 *      `(漢字)` 是各語言指南 §2 明文允許的原文注記，也放行。想看邊緣雙語標示
 *      的清單用 --verbose。
 *
 * 用法：
 *   node scripts/tools/check-ui-language.mjs           # 報告（exit 1 = 有真陽性；⚠️ 級不算）
 *   node scripts/tools/check-ui-language.mjs --strict  # ⚠️ 級也算 fail
 *   node scripts/tools/check-ui-language.mjs --verbose # 連邊緣雙語標示（ℹ️）一起列
 *   node scripts/tools/check-ui-language.mjs --json
 *   npm run check:ui-lang
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import * as OpenCC from 'opencc-js';
import {
  TW_ACCEPTED_VARIANTS,
  NON_CJK_ACCEPTED_VARIANTS,
} from './lib/tw-variant-chars.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');
const I18N_DIR = path.join(ROOT, 'src/i18n');

const s2t = OpenCC.Converter({ from: 'cn', to: 't' });
const t2s = OpenCC.Converter({ from: 't', to: 'cn' });

// 白名單住 scripts/tools/lib/tw-variant-chars.mjs（跟 terminology-charcheck.js 共用同一份
// SSOT，含校準語料與加字判準）。中文區塊放寬、非中日韓區塊維持嚴格——見該檔 §分區設計。

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
  // /bench 的命題刻意雙語並列：頁面語言放主句，另一語言放副句（zh-TW 頁配英文副句、
  // en 頁配中文原句）。這是 sovereignty bench 的設計，中文原句是被展示的對象。
  'bench.thesis.question.sub',
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

/** 這行只有 key（`'key':`），值被 prettier 折到下一行 */
function parseKeyOnly(line) {
  const m = line.match(/^\s*['"]?([\w.$-]+)['"]?\s*:\s*$/);
  return m ? m[1] : null;
}

/** 整行只是一個字串字面值（折行後的值那一行） */
function parseValueOnly(line) {
  const m = line.match(/^\s*(['"])((?:\\.|(?!\1).)*)\1\s*,?\s*$/);
  return m ? m[2] : null;
}

/**
 * 把「key 在這行、值在下一行」的條目接起來。回傳 { key, value, line }，
 * line 指向**值**所在的行（讀者要跳去修的是那一行）。
 * 折行條目吃掉兩行；同行條目一行。
 */
function entryAt(lines, i) {
  const same = parseEntry(lines[i]);
  if (same) return { ...same, line: i + 1, span: 1 };
  const key = parseKeyOnly(lines[i]);
  if (key && i + 1 < lines.length) {
    const value = parseValueOnly(lines[i + 1]);
    if (value !== null) return { key, value, line: i + 2, span: 2 };
  }
  return null;
}

/**
 * CJK_FRAGMENT（§6）：漢字**夾在**該語言可讀字元之間。
 * 先挖掉括號 / 引號裡的原文注記（`(漢字)` 是各語言指南 §2 明文允許的），
 * 再看每一段漢字 run 前後是否都還有該語言自己的字元。
 * 邊緣漢字（`'Taiwan Semiconductor 台積電'`）不算——那是雙語標示。
 */
const ANNOTATION_RE =
  /\([^)]*\)|（[^）]*）|\[[^\]]*\]|「[^」]*」|『[^』]*』|《[^》]*》|〈[^〉]*〉|«[^»]*»|"[^"]*"|“[^”]*”/g;
const CJK_RUN_RE = /[㐀-鿿豈-﫿]+/g;

// 台股掛牌後綴（矽力-KY / 某某-DR）：漢字名字後面黏著的 -KY 是名字的一部分，
// 不是「碎片後面還有拉丁字」。
const TICKER_SUFFIX_RE = /^[-‐–][A-Z]{1,3}\b/;

function cjkFragments(value, lang) {
  const own = ownScriptRe(lang);
  const stripped = value.replace(ANNOTATION_RE, ' ');
  const out = [];
  for (const m of stripped.matchAll(CJK_RUN_RE)) {
    const before = stripped.slice(0, m.index);
    const after = stripped
      .slice(m.index + m[0].length)
      .replace(TICKER_SUFFIX_RE, '');
    if (own.test(before) && own.test(after)) out.push(m[0]);
  }
  return out;
}

/** 邊緣雙語標示（ℹ️ 只在 --verbose 列）：有漢字、可讀、但不是碎片 */
function isEdgeBilingual(value, lang) {
  return (
    CJK_RE.test(value) &&
    ownScriptRe(lang).test(value) &&
    cjkFragments(value, lang).length === 0
  );
}

function leakedSimplified(str, lang) {
  // 中文區塊放寬（作者在合法書寫台灣中文／引用外語來源標題／寫真人姓名），
  // 非中日韓區塊維持嚴格（那裡的「湾」「国」幾乎都是譯文掉回中文）。
  const allow =
    lang === 'zh-TW' ? TW_ACCEPTED_VARIANTS : NON_CJK_ACCEPTED_VARIANTS;
  const out = [];
  for (const c of str) {
    if (!CJK_RE.test(c)) continue;
    if (allow.has(c)) continue;
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
  const infos = [];
  let lang = null;

  // 逐行：語言區塊邊界 + 字形層（SIMPLIFIED_LEAK 看的是字，不管條目怎麼折行）
  lines.forEach((line, i) => {
    const h = LANG_HEADER.exec(line);
    if (h) {
      lang = h[1];
      return;
    }
    if (!lang) return;
    if (isQuotedEvidence(line)) return;

    if (!SKIP_SIMPLIFIED.has(lang)) {
      const chars = leakedSimplified(line, lang);
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
  });

  // 逐條目：語意層。同行與折行（key 一行、值下一行）都當一個條目看（v3）。
  const keysByLang = new Map();
  lang = null;
  for (let i = 0; i < lines.length; i++) {
    const h = LANG_HEADER.exec(lines[i]);
    if (h) {
      lang = h[1];
      continue;
    }
    if (!lang) continue;
    const entry = entryAt(lines, i);
    if (!entry) continue;
    if (!keysByLang.has(lang)) keysByLang.set(lang, new Set());
    keysByLang.get(lang).add(entry.key);
    if (entry.span === 2) i += 1; // 值那一行已經吃掉
    const valueLine = lines[entry.line - 1];
    if (isQuotedEvidence(valueLine)) continue;
    const text = valueLine.trim().slice(0, 100);
    const base = { file: rel, lang, line: entry.line, text };

    // 豁免 e：這些 key 本來就該帶漢字（endonym / 逐字證據 / 刻意並列原文）
    const exempt = CJK_OK_KEYS.some((k) => entry.key.includes(k));

    // 2. 整串都是中文 = 根本沒翻（報了這條就不再往下報 5/6，同一條目一個病名）
    if (!CJK_LANGS.has(lang) && !exempt && looksUntranslated(entry.value)) {
      findings.push({ kind: 'UNTRANSLATED_CJK', ...base });
      continue;
    }

    // 4. zh-TW 用了中國用語（字形對、詞彙錯 — #1322）
    if (lang === 'zh-TW') {
      for (const [bad, good] of prcTerms(entry.value)) {
        findings.push({ kind: 'PRC_TERM', ...base, chars: `${bad} → ${good}` });
      }
    }

    if (CJK_LANGS.has(lang) || exempt || !CJK_RE.test(entry.value)) continue;

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
    const readable = ownScriptRe(lang).test(entry.value);
    if (!readable) {
      findings.push({
        kind: 'UNREADABLE_FOR_LOCALE',
        ...base,
        chars: `無 ${lang} 可讀字元`,
      });
      continue;
    }

    // 6. 讀得到，但漢字碎片夾在句子中間（翻到一半掉回中文）—— ⚠️ 警示級。
    //    'تطوير民間، نموذج' 這種：阿拉伯讀者讀得到前後、讀不到中間那兩個字。
    //    邊緣漢字（'Taiwan Semiconductor 台積電'）不報，見豁免 f。
    const frags = cjkFragments(entry.value, lang);
    if (frags.length) {
      findings.push({
        kind: 'CJK_FRAGMENT',
        severity: 'warn',
        ...base,
        chars: [...new Set(frags)].join('、'),
      });
    } else if (isEdgeBilingual(entry.value, lang)) {
      infos.push({ kind: 'EDGE_BILINGUAL', ...base });
    }
  }
  // 7. KEY_PARITY — 某語言少了 zh-TW 有的 key。⚠️ 警示級。
  //
  // 為什麼是警示不是硬擋：全庫既有缺口就有幾百個（budget.* 只有 zh/en、
  // about.timeline 的 2026-07-26 與 08-11 兩則在 8 個語言缺席），硬擋等於第一天
  // 就紅。但這個數字必須看得見——2026-08-17 一隻 subagent 為了驗自己新加的 key
  // 有沒有 12 語齊全，被迫自己用 vite ssrLoadModule 現造一把尺（Node ESM 解不了
  // `ui.ts` 的 extensionless import）。同一份判準每個人各造一次，就是 REFLEXES #83。
  // 用文字解析而非 import，所以不依賴任何 runtime。
  const zhKeys = keysByLang.get('zh-TW');
  if (zhKeys && zhKeys.size) {
    for (const [l, ks] of keysByLang) {
      if (l === 'zh-TW') continue;
      const missing = [...zhKeys].filter((k) => !ks.has(k));
      if (missing.length)
        findings.push({
          kind: 'KEY_PARITY',
          severity: 'warn',
          file: rel,
          lang: l,
          line: 0,
          chars: `缺 ${missing.length} 個 key`,
          text: missing.slice(0, 3).join(' / '),
        });
    }
  }

  return { findings, infos };
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
const strict = process.argv.includes('--strict');
const verbose = process.argv.includes('--verbose');
const files = fs
  .readdirSync(I18N_DIR)
  .filter((f) => f.endsWith('.ts') && f !== 'utils.ts')
  .map((f) => path.join(I18N_DIR, f));

const scanned = files.map(scanFile);
const findings = scanned.flatMap((s) => s.findings).concat(checkTableDrift());
const infos = scanned.flatMap((s) => s.infos);
const hard = findings.filter((f) => f.severity !== 'warn');
const warns = findings.filter((f) => f.severity === 'warn');

function printList(list) {
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

if (asJson) {
  console.log(
    JSON.stringify({ findings, infos: verbose ? infos : undefined }, null, 2),
  );
} else {
  console.log('# UI 字串語言閘門\n');
  if (!hard.length) {
    console.log(
      '✅ 無簡體外洩、無整串未譯、無該語言讀不到的漢字、字串表與語言註冊表同步',
    );
  } else {
    const byKind = {};
    for (const f of hard) (byKind[f.kind] ||= []).push(f);
    for (const [kind, list] of Object.entries(byKind)) {
      console.log(`\n## ${kind}（${list.length}）\n`);
      printList(list);
    }
    console.log(`\n總計 ${hard.length} 筆真陽性`);
  }
  if (warns.length) {
    // 警示級要按 kind 分開印。⚠️ 別偷懒共用一個標題：v3 首版把 KEY_PARITY 的命中
    // 印在「CJK_FRAGMENT」的大標底下，讀報告的人會拿著錯的病名去修。
    const WARN_NOTE = {
      CJK_FRAGMENT:
        '  非 CJK 語言的句子中間夾著漢字碎片：讀者讀得到前後、讀不到中間那幾個字。\n' +
        '  幾乎都是翻到一半掉回中文，修法是把那幾個字翻成該語言。',
      KEY_PARITY:
        '  某語言少了 zh-TW 有的 key → 該處靜默 fallback 到 FALLBACK_CHAIN 的下一個語言，\n' +
        '  讀者看到的是別人的語言而不是錯誤。全庫既有缺口就有幾百個，所以只印不擋；\n' +
        '  但**新加的 key 一定要 12 語齊全**，不然你剛補的洞會以另一種面貌留在原地。',
    };
    const byWarn = {};
    for (const f of warns) (byWarn[f.kind] ||= []).push(f);
    for (const [kind, list] of Object.entries(byWarn)) {
      console.log(
        `\n## ⚠️ ${kind}（${list.length}，警示級${strict ? '，--strict 下算 fail' : '，不擋 push'}）\n`,
      );
      printList(list);
      if (WARN_NOTE[kind]) console.log('\n' + WARN_NOTE[kind]);
    }
  }
  if (infos.length) {
    if (verbose) {
      console.log(
        `\n## ℹ️ EDGE_BILINGUAL（${infos.length}，雙語標示，僅列出）\n`,
      );
      printList(infos);
    } else {
      console.log(
        `\nℹ️ 另有 ${infos.length} 筆非 CJK 語言區塊帶邊緣漢字的雙語標示` +
          '（如 en 的「Taiwan Semiconductor 台積電」）——刻意設計，不報；--verbose 列出',
      );
    }
  }
}

process.exit(hard.length || (strict && warns.length) ? 1 : 0);
