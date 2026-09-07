import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  escapeHtml,
  localAnalyticsPath,
  decodePathLabel,
} from '../src/scripts/dashboard/safe-html.mjs';

test('external analytics text cannot inject HTML or external/script links', () => {
  assert.equal(
    escapeHtml('<img src=x onerror="alert(1)">'),
    '&lt;img src=x onerror=&quot;alert(1)&quot;&gt;',
  );
  for (const path of [
    'javascript:alert(1)',
    '//evil.test',
    '/\\evil.test',
    '/\n/evil.test',
  ])
    assert.equal(localAnalyticsPath(path), '/');
  assert.equal(localAnalyticsPath('/food/夜市文化/'), '/food/夜市文化/');
  assert.equal(decodePathLabel('/%E0%A4%A'), '%E0%A4%A');
  assert.equal(decodePathLabel('/%E5%8F%B0%E7%81%A3/'), '台灣');
});
