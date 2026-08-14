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
 * `marked.use()` 改的是 marked 單例，誰先跑到誰決定行為。改成一律從本檔取用
 * `marked`，設定就跟著 import 一起到，不會有「某個 render 路徑忘記套」的漂移。
 * 新增任何 marked 呼叫點時，import 這裡，不要直接 import 'marked'。
 *
 * 刻意用 .mjs 而非 .ts：tests/markdown-cjk.test.mjs 要能用 `node --test` 直接
 * 載入「正式站在用的那個 marked 實例」來驗行為，不經過 TS 轉譯或 Astro build。
 */
import { marked } from 'marked';
import markedCjkFriendly from 'marked-cjk-friendly';

marked.use(markedCjkFriendly());

export { marked };
export default marked;
