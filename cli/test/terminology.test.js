/**
 * Unit tests for commands/terminology.js — doConvert must respect
 * `auto_convert: false` and the "無對應" placeholder skip.
 *
 * 2026-09-05: CLI's `terminology convert` built its replacement table from
 * every YAML entry, never checking `auto_convert`. The real converter
 * (src/pages/terminology/converter.astro:116) skips entries flagged
 * `auto_convert: false` because the China-side word is ALSO legitimate
 * Taiwanese usage in another sense (支持/保存/代表/照片…) — blind
 * replacement corrupts correct text, e.g. "我很支持你" → "我很支援你".
 * This test locks in the fix.
 *
 * It also covers converter.astro:145's companion skip: when the `taiwan`
 * display value is itself a "no correspondence" placeholder sentence
 * (e.g. 偷感.yaml → "無公認對應（做事怕被注意的彆扭感）"), there is nothing
 * sensible to replace the source word with.
 *
 * Fixtures here are hand-built (not read from data/terminology/*.yaml)
 * deliberately — those files are being edited concurrently by another
 * session, so a test tied to their live content would be flaky.
 *
 * Run with: cd cli && npx vitest run
 */

import { describe, it, expect, vi } from 'vitest';
import { doConvert } from '../src/commands/terminology.js';

/** Run `fn`, capture the single JSON string doConvert prints when
 *  opts.json is true, and return it parsed. */
function captureJson(fn) {
  const spy = vi.spyOn(console, 'log').mockImplementation(() => {});
  try {
    fn();
    const call = spy.mock.calls.find(([arg]) => {
      try {
        JSON.parse(arg);
        return true;
      } catch {
        return false;
      }
    });
    return call ? JSON.parse(call[0]) : null;
  } finally {
    spy.mockRestore();
  }
}

const terms = [
  { _china: '支持', _taiwan: '支援', auto_convert: false },
  { _china: '保存', _taiwan: '存檔 / 儲存', auto_convert: false },
  { _china: '軟件', _taiwan: '軟體' }, // auto_convert 未設 = 預設 true
  { _china: '偷感', _taiwan: '無公認對應（做事怕被注意的彆扭感）' },
];

describe('doConvert — auto_convert: false skip', () => {
  it('does not touch 支持 (同形異義, auto_convert:false)', () => {
    const out = captureJson(() =>
      doConvert('我很支持你', terms, { json: true }),
    );
    expect(out.output).toBe('我很支持你');
    expect(out.replacements).toHaveLength(0);
  });

  it('does not touch 保存 (auto_convert:false, "照片保存" sense)', () => {
    const out = captureJson(() =>
      doConvert('照片保存在雲端', terms, { json: true }),
    );
    expect(out.output).toBe('照片保存在雲端');
    expect(out.replacements).toHaveLength(0);
  });

  it('still converts entries without auto_convert:false', () => {
    const out = captureJson(() =>
      doConvert('軟件工程師很厲害', terms, { json: true }),
    );
    expect(out.replacements).toHaveLength(1);
    expect(out.replacements[0]).toMatchObject({ from: '軟件', to: '軟體' });
  });
});

describe('doConvert — "無對應" placeholder skip', () => {
  it('does not replace with a "no correspondence" explanation sentence', () => {
    const out = captureJson(() =>
      doConvert('這種偷感很重', terms, { json: true }),
    );
    expect(out.output).toBe('這種偷感很重');
    expect(out.replacements).toHaveLength(0);
  });
});
