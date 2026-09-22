/**
 * viz-source-line.test.mjs — tw-* 模組「來源」列的解析契約
 * （跑：node --test tests/viz-source-line.test.mjs）
 *
 * 守的是 2026-09-23 量到的那個缺口：renderer 的 VIZ_STRINGS 早就有十三語的
 * srcPrefix（寫得出 `Nguồn:`／`Quelle:`／`Источник:`），但解析端的 regex 停在
 * 2026-07-16 手列的五語，於是 07 月之後出生的七語有 1,124 列來源被當成資料列
 * 吃進圖表、來源 caption 消失（vi 250／pt 218／hi 177／id 171／ar 168／ru 163／de 112）。
 *
 * 這支測試驗的是**推導關係**不是某一組字串：解析用的標籤集合必須涵蓋
 * VIZ_STRINGS 裡每一個語言的 srcPrefix。新語言出生時 VIZ_STRINGS 是型別強制
 * 要填的，填了就自動被這裡涵蓋——除非有人又手列了第二份清單，那時這支會紅。
 */
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { readFileSync } from 'node:fs';

const SRC = readFileSync(
  new URL('../src/utils/article-render.ts', import.meta.url),
  'utf-8',
);

function buildRe() {
  const prefixes = [...SRC.matchAll(/srcPrefix:\s*'([^']+)'/g)].map(
    (m) => m[1],
  );
  const extraBlock = SRC.slice(
    SRC.indexOf('_SRC_EXTRA_LABELS'),
    SRC.indexOf('function _buildSrcLineRe'),
  );
  const extra = [...extraBlock.matchAll(/'([^']+)'/g)].map((m) => m[1]);
  const labels = new Set(extra);
  for (const p of prefixes)
    labels.add(
      p
        .replace(/[:：]\s*$/, '')
        .trim()
        .toLowerCase(),
    );
  const alt = [...labels]
    .filter(Boolean)
    .sort((a, b) => b.length - a.length)
    .map((l) => l.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))
    .join('|');
  return { re: new RegExp(`^(?:${alt})\\s*[:：]\\s*(.+)$`, 'i'), prefixes };
}

test('每個語言的 srcPrefix 都解析得回來（寫入端與讀取端不分岔）', () => {
  const { re, prefixes } = buildRe();
  assert.ok(
    prefixes.length >= 13,
    `VIZ_STRINGS 應有 13 語 srcPrefix，實際 ${prefixes.length}`,
  );
  for (const p of prefixes) {
    const line = `${p}Taiwan.md Contributors API`;
    const m = line.match(re);
    assert.ok(m, `解析不到自己寫出來的前綴：${JSON.stringify(p)}`);
    assert.equal(m[1], 'Taiwan.md Contributors API');
  }
});

test('語料裡出現過的複數形也收得到', () => {
  const { re } = buildRe();
  for (const line of [
    'Fontes: a, b',
    'Источники: ЦВК',
    'Quellen: Taipower',
    'Nguồn dữ liệu: X',
  ]) {
    assert.ok(line.match(re), `複數形沒收到：${line}`);
  }
});

test('一般資料列不被誤判成來源列', () => {
  const { re } = buildRe();
  for (const line of [
    '台北 | 120',
    'system Engineering and Infrastructure | 4,582',
    '*content Writing | 1,418',
  ]) {
    assert.equal(line.match(re), null, `資料列被誤判：${line}`);
  }
});
