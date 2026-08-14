/**
 * marked-cjk.mjs — 全站唯一的 marked 設定點（CJK 強調修正）
 *
 * 為什麼存在（2026-08-14）：
 * CommonMark／GFM 的 delimiter flanking 規則把 CJK 標點當成一般標點，於是
 * `**完整句。**下一句` 的收尾 `**` 前是「。」後是漢字，不算 right-flanking，
 * 整組 `**` 就原封不動印給讀者看（讀者回報：/technology/開源社群與g0v/）。
 * 這不是某一篇文章的錯字，是引擎規則對無空格語言的已知缺口
 * （commonmark/commonmark-spec#650，2020 年開到現在）。
 *
 * `marked-cjk-friendly` 是 CommonMark CJK-friendly 修正案的 marked 官方移植，
 * 同一份規格另有 remark／markdown-it／Comrak／goldmark／Markdig 移植，
 * 且保證非 CJK 輸入與原本 CommonMark 逐字元同輸出——所以英文／既有內容不受影響。
 *
 * ⚠️ 為什麼是「所有 marked 呼叫點都 import 這裡」而不是各自 `import { marked }`：
 * 兩個理由，第二個是 2026-08-14 code review 補的。
 *
 * 1. 設定跟著 import 一起到，不會有「某個 render 路徑忘記套」的漂移。
 *    新增任何 marked 呼叫點時，import 這裡，不要直接 import 'marked'。
 *
 * 2. 這裡刻意用 `new Marked()` 建**獨立實例**，不對 marked 單例做 `marked.use()`。
 *    因為 `marked.use()` 改的是模組單例，一旦這麼做，行為就變成「誰先被 import
 *    誰決定」的隱性耦合：任何日後 `import { marked } from 'marked'` 的程式都會
 *    無聲繼承（或反過來覆蓋）這裡的設定。本 repo 已經有一個會撞的例子——
 *    `cli/src/lib/render.js` 對單例跑 `marked.use(markedTerminal())`；它現在是
 *    另一個 npm 套件（taiwanmd，自帶 marked ^15）所以不同進程，但沒有理由
 *    留著這種等著爆的耦合。獨立實例讓兩邊互不影響，而且「本檔是唯一設定點」
 *    這句話從慣例升級成機制。
 *    對應測試：tests/markdown-cjk.test.mjs 直接斷言全域單例沒有被污染。
 *
 * 刻意用 .mjs 而非 .ts：tests/markdown-cjk.test.mjs 要能用 `node --test` 直接
 * 載入「正式站在用的那個 marked 實例」來驗行為，不經過 TS 轉譯或 Astro build。
 */
import { Marked } from 'marked';
import markedCjkFriendly from 'marked-cjk-friendly';

/**
 * 全站共用的 marked 實例。`.parse` / `.parseInline` / `.Renderer` 都在實例上，
 * 呼叫端用法與原本的 `marked` 完全相同。
 */
const marked = new Marked(markedCjkFriendly());

export { marked };
export default marked;
