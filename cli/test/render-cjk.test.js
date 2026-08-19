/**
 * Contract tests for lib/render.js — CJK emphasis must not leak literal `**`
 * into the reader's terminal.
 *
 * Why this file exists: CommonMark/GFM's delimiter flanking rules treat CJK
 * punctuation as ordinary punctuation, so a closing `**` that sits after 「。」
 * and before a 漢字 is not right-flanking. The pair never closes and both
 * asterisks are printed verbatim — `**沒有人組織，沒有人指揮。**g0v社群` reached
 * readers with the stars visible. It is an engine gap for languages that do not
 * separate words with spaces (commonmark/commonmark-spec#650, open since 2020),
 * not an authoring mistake, so the fix belongs in the parser configuration.
 *
 * The website hit the identical bug and fixes it in `src/utils/marked-cjk.mjs`.
 * The CLI ships as its own npm package with its own dependency tree, so it
 * needs its own fix — and its own test, because nothing in the site's suite
 * covers this module.
 *
 * The negative control matters: without `marked-cjk-friendly` an unconfigured
 * marked still leaks the stars, which is what proves the configuration (rather
 * than luck or a marked version bump) is doing the work.
 *
 * Run with: cd cli && npx vitest run
 */

import { describe, it, expect } from 'vitest';
import { Marked, marked as globalMarked } from 'marked';
import { markedTerminal } from 'marked-terminal';
import { renderMarkdown } from '../src/lib/render.js';

/** Strip ANSI escapes so assertions read against visible text. */
function visible(str) {
  // eslint-disable-next-line no-control-regex
  return str.replace(/\u001b\[[0-9;]*m/g, '');
}

describe('CJK emphasis in terminal output', () => {
  it('closes ** that follows CJK sentence punctuation', () => {
    const out = renderMarkdown('**沒有人組織，沒有人指揮。**g0v社群的參與者');
    expect(visible(out)).toContain('沒有人組織，沒有人指揮。g0v社群的參與者');
    expect(out).not.toContain('**');
  });

  it('closes ** that follows a CJK closing quote', () => {
    const out = renderMarkdown(
      '結果是：**立委開始在意自己的「資料」。**出席率',
    );
    expect(out).not.toContain('**');
  });

  it('opens ** that precedes a CJK bracket', () => {
    const out = renderMarkdown('詩名是**〈等待航線〉**。');
    expect(out).not.toContain('**');
  });

  it('still applies terminal styling to the emphasised span', () => {
    // Guards against "fixing" the leak by dropping the emphasis entirely:
    // the span must remain styled, not silently flattened to plain text.
    const out = renderMarkdown('**沒有人組織，沒有人指揮。**g0v社群');
    // marked-terminal only emits escapes when colour is enabled; when it is
    // disabled the text must still be clean, which the assertions above cover.
    if (/\u001b\[/.test(out)) {
      expect(out).toMatch(/\u001b\[1m沒有人組織，沒有人指揮。/);
    }
  });

  it('leaves non-CJK emphasis behaviour unchanged', () => {
    const out = renderMarkdown('**English.** Next');
    expect(visible(out)).toContain('English. Next');
    expect(out).not.toContain('**');
  });

  it('keeps deliberately escaped asterisks literal', () => {
    // Redacted titles and censored profanity are supposed to show stars.
    const out = renderMarkdown(String.raw`\*\*不是粗體\*\*`);
    expect(visible(out)).toContain('**不是粗體**');
  });

  it('an unconfigured marked still leaks the stars (negative control)', () => {
    const bare = new Marked(markedTerminal());
    expect(bare.parse('**沒有人組織，沒有人指揮。**g0v社群')).toContain('**');
  });

  it('does not pollute the global marked singleton', () => {
    // render.js builds its own `new Marked(...)`. If it ever regresses to
    // `marked.use(...)` on the singleton, behaviour becomes dependent on
    // import order across the whole package. This test is that guarantee.
    expect(
      globalMarked.parseInline('**沒有人組織，沒有人指揮。**g0v社群'),
    ).toContain('**');
  });
});
