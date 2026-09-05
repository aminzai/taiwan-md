/**
 * article-heading-id.test.mjs — 標題錨點 id 產生器契約
 *（跑：node --experimental-strip-types --test tests/article-heading-id.test.mjs）
 *
 * 守的是 OBSERVER-QUEUE #44：舊規則 `[^\w一-鿿-]` 用 JS 的 `\w`（ASCII-only）
 * 過濾標題，韓文／俄文／阿拉伯文／印地文整段被剝成空字串或純連字號，拉丁語系
 * 重音字元（á/é/í/ó/ú/ñ 等）也被吃掉。2026-09-05 哲宇拍板 A：改成
 * `[^\p{L}\p{N}_-]/gu`，一次修好全部語言。
 *
 * ⚠️ 為什麼 import src/utils/article-render.ts 的 `slugifyHeadingId` 而不是
 * 自己重寫一份規則來驗：2026-08-28「徹底處理那一輪」用 Python 重寫新舊 slug
 * 函式估算影響範圍，得到「零風險」的錯答案——Python 的 `\w` 吃 Unicode 字母，
 * JS 的 `\w` 只吃 ASCII，兩邊 regex 長得一樣，量出的卻是完全不同的行為
 * （見 docs/semiont/memory/2026-08-28-005518-footnote-cards.md）。測試必須
 * 載入正式站在用的那支函式，否則綠燈只是自我安慰。
 *
 * Node 的 .ts 動態 import 需要型別剝離旗標（本 repo 未裝 ts-node/tsx）：
 *   node --experimental-strip-types --test tests/article-heading-id.test.mjs
 */
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';

import {
  slugifyHeadingId,
  renderArticleHtml,
} from '../src/utils/article-render.ts';

// ── OBSERVER-QUEUE #44 補強 2：TOC extractHeadings 的 id 抓取 ───────────────
// TableOfContents.astro 是 .astro 檔，frontmatter 不是一份能被 node 直接
// import 的 ES module（`Astro.props` 只在 Astro compiler 的執行環境下存在，
// 整段當 module 載入會在 top-level 就丟 ReferenceError），也沒有 vitest /
// @astrojs/test 這類能跑 .astro 元件的測試工具（見本檔外 package.json）。
// 為了不犯「兩邊 regex 長得一樣、行為卻不同」那個舊病（2026-08-28「徹底處理
// 那一輪」的教訓，見上方檔頭），這裡不手抄一份 extractHeadings 規則來測，而是
// 直接從 TableOfContents.astro 原始碼裡把 `decodeHeadingEntities` 跟
// `extractHeadings` 兩支函式的原始文字切出來，動態組成一支暫存 module 執行——
// 保證測試打的永遠是正式站當下真正在跑的那段程式碼，改了 .astro 這支測試就跟著
// 抓到新版本，不需要手動同步。
const ARTICLE_RENDER_URL = pathToFileURL(
  fileURLToPath(new URL('../src/utils/article-render.ts', import.meta.url)),
).href;

function extractFunctionSource(src, name) {
  const startIdx = src.indexOf(`function ${name}`);
  assert.ok(
    startIdx !== -1,
    `TableOfContents.astro 找不到 function ${name}——這支測試假設的函式名稱可能被改掉了，去看 src/components/TableOfContents.astro`,
  );
  let i = src.indexOf('{', startIdx);
  let depth = 0;
  for (; i < src.length; i++) {
    if (src[i] === '{') depth++;
    else if (src[i] === '}') {
      depth--;
      if (depth === 0) {
        i++;
        break;
      }
    }
  }
  return src.slice(startIdx, i);
}

async function loadRealTocExtractHeadings() {
  const astroSrc = readFileSync(
    new URL('../src/components/TableOfContents.astro', import.meta.url),
    'utf8',
  );
  const decodeFnSrc = extractFunctionSource(astroSrc, 'decodeHeadingEntities');
  const extractFnSrc = extractFunctionSource(astroSrc, 'extractHeadings');
  const moduleSrc = `import { slugifyHeadingId } from '${ARTICLE_RENDER_URL}';
${decodeFnSrc}
${extractFnSrc}
export { extractHeadings, decodeHeadingEntities };
`;
  const tmpFile = join(
    tmpdir(),
    `twmd-toc-extract-headings-${process.pid}-${Date.now()}.mts`,
  );
  writeFileSync(tmpFile, moduleSrc, 'utf8');
  try {
    return await import(pathToFileURL(tmpFile).href);
  } finally {
    rmSync(tmpFile, { force: true });
  }
}

test('韓文標題：諺文不再被剝成空字串', () => {
  assert.equal(
    slugifyHeadingId('내가 태어난 그 생각은 첫 commit보다 네 시간 반 앞섰다'),
    '내가-태어난-그-생각은-첫-commit보다-네-시간-반-앞섰다',
  );
  // 舊規則下這種純韓文標題會退化成空字串或純連字號——新規則下絕不該再發生
  assert.notEqual(slugifyHeadingId('한국어 제목입니다'), '');
  assert.doesNotMatch(slugifyHeadingId('한국어 제목입니다'), /^-*$/);
});

test('阿拉伯文標題：阿拉伯字母不再被剝成空字串', () => {
  const id = slugifyHeadingId('قصة نشأة Taiwan.md');
  assert.doesNotMatch(id, /^-*$/);
  assert.equal(id, 'قصة-نشأة-taiwanmd');
});

test('印地文標題：天城文字母（不含連字符號）保留、不退化', () => {
  const id = slugifyHeadingId('एक लेख के लिए एक मशीन क्यों बनाई जाए?');
  assert.doesNotMatch(id, /^-*$/);
  assert.ok(id.length > 0);
});

test('印地文帶 matras（母音符號）：字面完整不被剝損（補強 1，2026-09-05）', () => {
  // हिंदी = ह + ि(matra) + ं(anusvara) + द + ी(matra)。matras 屬 Unicode
  // 「Mark」大分類（\p{M}），不屬 `\p{L}`——只用 `\p{L}\p{N}` 過濾時，子音
  // （\p{L}）留下、matras 被當「非字母」剝掉，「हिंदी」會退化成「हद」，
  // 不是空字串也不是純連字號（isDegenerate 抓不到），但字面已經是另一個詞。
  // 必須加 `\p{M}` 才會讓組合標記留下，字面跟輸入逐字相同。
  assert.equal(slugifyHeadingId('हिंदी'), 'हिंदी');
  assert.notEqual(slugifyHeadingId('हिंदी'), 'हद');
});

test('俄文標題：西里爾字母不再被剝成空字串', () => {
  assert.equal(
    slugifyHeadingId('Происхождение: от Творца к Поэту'),
    'происхождение-от-творца-к-поэту',
  );
});

test('帶重音的西班牙文標題：重音字元保留（舊規則會吃掉變成 las-ltimas）', () => {
  assert.equal(
    slugifyHeadingId('Las últimas dos letras de mi nombre'),
    'las-últimas-dos-letras-de-mi-nombre',
  );
  assert.equal(
    slugifyHeadingId('Cómo me veo a mí mismo a través de los datos'),
    'cómo-me-veo-a-mí-mismo-a-través-de-los-datos',
  );
});

test('含全形標點的中文標題：標點被過濾、行為與修復前一致（無退步）', () => {
  assert.equal(
    slugifyHeadingId('台灣的「經濟」發展、與挑戰'),
    '台灣的經濟發展與挑戰',
  );
});

test('日文標題：假名（U+3040-30FF）現在跟漢字一起保留，不再局部損傷', () => {
  assert.equal(slugifyHeadingId('日本語のかな見出し'), '日本語のかな見出し');
});

test('連續連字號合併＋首尾修剪：空白轉連字號不再留下雜訊', () => {
  assert.equal(
    slugifyHeadingId('A - B  multiple   spaces'),
    'a-b-multiple-spaces',
  );
});

test('emoji + 文字：building emoji 本身（\\p{So}）仍被剝掉，但 VS16 變體選擇符留下', () => {
  // 🏛️ = U+1F3DB（building，Symbol/So，非字母不留）+ U+FE0F（variation selector-16，
  // 屬 Unicode「Mark」大分類 \p{M}）。加 \p{M} 是補強 1 的既定範圍（讓天城文
  // matras／泰文聲調／越南文調號留下），VS16 這種零寬字元也一併留下是同一條規則
  // 的已知副作用——不影響任何人：renderer.heading 跟 TableOfContents 的 fallback
  // 都呼叫同一支函式，href 與 id 永遠算出同一個字串，錨點依然對得上。
  assert.equal(slugifyHeadingId('🏛️ 官方機構'), '️-官方機構');
});

test('60 字元截斷仍然生效（既有行為不變）', () => {
  const long = 'a'.repeat(100);
  assert.equal(slugifyHeadingId(long).length, 60);
});

test('TOC extractHeadings：標題含 & " < 時，href 必須等於 renderer 真正設的 id（補強 2）', async () => {
  const { extractHeadings } = await loadRealTocExtractHeadings();

  // 走真正的 renderArticleHtml pipeline（marked + renderer.heading），
  // 不是手寫一段 fixture HTML 去猜 marked 怎麼跳脫——& / " 會被 marked 的
  // inline escape 轉成實體，`<weird>` 則會被當成合法但未知的行內 HTML
  // passthrough（不會被跳脫），三種情況一次涵蓋。
  const md = '## A & B "quoted" <weird> title\n\n內容測試。\n';
  const { fullHtml } = renderArticleHtml('文章標題占位', md, 'zh-TW');

  const rendererIdMatch = fullHtml.match(/<h2 id="([^"]*)"/);
  assert.ok(
    rendererIdMatch,
    `renderArticleHtml 沒有輸出 <h2 id="...">，fixture 或 renderer.heading 的行為可能變了：${fullHtml}`,
  );
  const rendererId = rendererIdMatch[1];
  // 手動核對過的 ground truth：renderer 真正的 id 是 "a-b-quoted-weird-title"
  // （在原始未跳脫文字上跑 slugifyHeadingId）；OBSERVER-QUEUE #44 修復前的舊
  // extractHeadings 因為抓不到 id 屬性、落到 fallback 用「已渲染、未解碼實體」
  // 的文字重算，會算出 "a-amp-b-quotquotedquot-title"——完全是另一個字串。
  assert.equal(rendererId, 'a-b-quoted-weird-title');

  const headings = extractHeadings(fullHtml);
  assert.equal(headings.length, 1);
  assert.equal(headings[0].id, rendererId);
});

test('TOC decodeHeadingEntities：解碼順序正確，&amp; 最後解不會連鎖誤解', async () => {
  const { decodeHeadingEntities } = await loadRealTocExtractHeadings();
  assert.equal(decodeHeadingEntities('A &amp; B'), 'A & B');
  assert.equal(decodeHeadingEntities('&lt;tag&gt;'), '<tag>');
  assert.equal(decodeHeadingEntities('&quot;quoted&quot;'), '"quoted"');
  assert.equal(decodeHeadingEntities('it&#39;s'), "it's");
  // 順序陷阱：文字裡本來就有的字面 "&lt;" 不該被 &amp; 的解碼規則連鎖誤解成
  // "<"——&amp; 必須排最後解，否則 "&amp;lt;" 會被錯誤地解成 "<" 而不是 "&lt;"。
  assert.equal(decodeHeadingEntities('&amp;lt;'), '&lt;');
});
