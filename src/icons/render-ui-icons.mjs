import { parse } from 'parse5';
import { emojiIcons, iconSvg } from './taiwan-icons.mjs';
const symbols = Object.keys(emojiIcons).sort((a, b) => b.length - a.length);
const expression = new RegExp(
  symbols.map((s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|'),
  'gu',
);
const protectedTags = new Set([
  'head',
  'script',
  'style',
  'pre',
  'code',
  'textarea',
  'svg',
  'blockquote',
]);
/** Transform only rendered interface text. Source offsets preserve HTML, attributes,
 * quoted prose, and scripts byte-for-byte. No client observer or runtime dependency. */
export function renderUiIcons(html) {
  expression.lastIndex = 0;
  if (!expression.test(html)) return html;
  const root = parse(html, { sourceCodeLocationInfo: true });
  const edits = [];
  function walk(node, protectedContent = false) {
    const attrs = Object.fromEntries(
      (node.attrs ?? []).map((a) => [a.name, a.value]),
    );
    const blocked =
      protectedContent ||
      protectedTags.has(node.tagName) ||
      'data-preserve-emoji' in attrs ||
      /(?:^|\s)(?:prose|article-content|diary-content)(?:\s|$)/.test(
        attrs.class ?? '',
      );
    if (node.nodeName === '#text' && !blocked && node.sourceCodeLocation) {
      const { startOffset, endOffset } = node.sourceCodeLocation;
      const raw = html.slice(startOffset, endOffset);
      expression.lastIndex = 0;
      const replaced = raw.replace(expression, (emoji) => {
        // Standalone symbols retain their accessible name; paired labels remain quiet.
        const parent = node.parentNode;
        const hasLabel = parent?.attrs?.some((a) => a.name === 'aria-label');
        const paired = (parent?.childNodes ?? []).some(
          (n) =>
            n.nodeName === '#text' && n.value.replace(expression, '').trim(),
        );
        return iconSvg(emojiIcons[emoji], hasLabel || paired ? '' : emoji);
      });
      if (raw !== replaced) edits.push({ startOffset, endOffset, replaced });
    }
    for (const child of node.childNodes ?? []) walk(child, blocked);
  }
  walk(root);
  for (const e of edits.sort((a, b) => b.startOffset - a.startOffset))
    html = html.slice(0, e.startOffset) + e.replaced + html.slice(e.endOffset);
  return html;
}
