import test from 'node:test';
import assert from 'node:assert/strict';
import { renderUiIcons } from '../src/icons/render-ui-icons.mjs';
import { icons, emojiIcons, iconSvg } from '../src/icons/taiwan-icons.mjs';
test('icon aliases resolve and unknown names fail', () => {
  for (const name of Object.values(emojiIcons)) assert.ok(icons[name]);
  assert.throws(() => iconSvg('missing'));
  assert.match(iconSvg('book', '<script>'), /&lt;script&gt;/);
});
test('UI replacement preserves content, attributes, scripts, flags and signature', () => {
  const preserved =
    '<div class="prose"><p>📚 原文</p></div><blockquote>🌱 引用</blockquote><script>let x="📚";</script>';
  const html =
    '<html><head><title>📚 題名</title></head><body><h2 title="📚">📚 書架</h2>' +
    preserved +
    '🇹🇼 🧬<p data-preserve-emoji>🌱</p></body></html>';
  const out = renderUiIcons(html);
  assert.ok(out.includes(preserved));
  assert.ok(out.includes('<title>📚 題名</title>'));
  assert.ok(out.includes('title="📚"'));
  assert.ok(out.includes('🇹🇼 🧬'));
  assert.match(out, /<use href="\/icons\/taiwan.svg#book"/);
  assert.equal(renderUiIcons(out), out);
});
test('icon-only controls preserve accessible labels', () => {
  assert.match(renderUiIcons('<button>🔍</button>'), /aria-label="🔍"/);
  assert.match(
    renderUiIcons('<button aria-label="搜尋">🔍</button>'),
    /aria-hidden="true"/,
  );
});
