import test from 'node:test';
import assert from 'node:assert/strict';
import {
  keyCoverage,
  coverage,
} from '../scripts/core/lib/dashboard-coverage.mjs';
test('coverage measures expected keys, not a threshold or comments', () => {
  const source = `export const ui={'zh-TW': {'a':'甲','b':'乙'}, en: {'a':\n'one', 'unrelated':'x'}, de:{'a':''}};`;
  assert.equal(keyCoverage(source, 'en').pct, 50);
  assert.equal(keyCoverage(source, 'de').pct, 0);
  assert.equal(coverage(13, 13).pct, 100);
  assert.equal(keyCoverage(source, 'en').qualityVerified, false);
});
