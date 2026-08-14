/**
 * markdown-cjk.test.mjs — CJK 強調渲染契約（跑：node --test tests/markdown-cjk.test.mjs）
 *
 * 守的是讀者回報的那個病：`**完整句。**下一句` 整組 `**` 印在頁面上
 * （/technology/開源社群與g0v/，2026-08-14）。病根在 CommonMark／GFM 的
 * delimiter flanking 規則，不在文章本身，所以這裡驗的是**引擎設定**，
 * 不是某幾篇文章的字串。
 *
 * ⚠️ 為什麼 import src/utils/marked-cjk.mjs 而不是自己 new 一個 marked：
 * 第一版測試自己組了一個 Astro remark processor 來驗，測試綠燈但頁面照壞——
 * 因為文章根本不走 Astro 的 markdown pipeline，是 article-render.ts 用 marked 渲染。
 * 測試必須載入正式站在用的那個 marked 實例，否則綠燈只是自我安慰。
 */
import assert from 'node:assert/strict';
import { test } from 'node:test';

import { Marked } from 'marked';
import { marked } from '../src/utils/marked-cjk.mjs';

test('CJK 句末標點後的收尾 ** 會收成 <strong>', () => {
  assert.equal(
    marked.parseInline('**沒有人組織，沒有人指揮。**g0v社群'),
    '<strong>沒有人組織，沒有人指揮。</strong>g0v社群',
  );
  assert.equal(
    marked.parseInline('結果是：**立委開始在意自己的「資料」。**出席率'),
    '結果是：<strong>立委開始在意自己的「資料」。</strong>出席率',
  );
});

test('CJK 括號緊貼的起始 ** 也會收成 <strong>', () => {
  assert.equal(
    marked.parseInline('詩名是**〈等待航線〉**。'),
    '詩名是<strong>〈等待航線〉</strong>。',
  );
});

test('未套設定的 marked 仍會漏出字面 **（證明修正來自設定，不是巧合）', () => {
  const bare = new Marked();
  assert.equal(
    bare.parseInline('**沒有人組織，沒有人指揮。**g0v社群'),
    '**沒有人組織，沒有人指揮。**g0v社群',
  );
});

test('GFM 刪除線在 CJK 邊界仍成立', () => {
  assert.equal(
    marked.parseInline('這是~~舊句。~~下一句'),
    '這是<del>舊句。</del>下一句',
  );
});

test('刻意轉義的星號維持字面（如審查過的書名／粗話）', () => {
  const html = marked.parseInline(String.raw`\*\*不是粗體\*\*`);
  assert.equal(html, '**不是粗體**');
  assert.doesNotMatch(html, /<strong>/);
});

test('非 CJK 輸入行為不變', () => {
  assert.equal(
    marked.parseInline('**English.** Next'),
    '<strong>English.</strong> Next',
  );
});
