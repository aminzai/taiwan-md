/**
 * terminology-wording.test.mjs — /terminology/{id} 「算不算中國用語」四層說法契約
 *（跑：node --experimental-strip-types --test tests/terminology-wording.test.mjs）
 *
 * 守的是 OBSERVER-QUEUE #76（2026-10-10 哲宇拍板 C）：零佐證的條目不准再對讀者講
 * 「是，X 是中國大陸的常見說法」。E / F 與有佐證的條目維持原句，一個字不動。
 *
 * 跟 article-heading-id.test.mjs 同一個理由：測試載入正式站在用的那支函式
 * （src/utils/terminology-wording.ts），不自己重抄一份規則來驗。
 */
import assert from 'node:assert/strict';
import { test } from 'node:test';

import {
  TERM_PLACEHOLDERS,
  scrubTermField,
  hasTermEtymology,
  hasTermEvidence,
  termWordingBucket,
  termWording,
} from '../src/utils/terminology-wording.ts';

const empty = {
  origin: '',
  taiwanPath: '',
  chinaPath: '',
  forkPoint: '',
  forkCause: '',
  usageExample: '',
  usageNote: '',
};

const WIDE_CLAIM = '是中國大陸的常見說法';
const WIDE_LEAD = '是中國大陸的用法';

test('placeholder 填充字視同空值，其餘 trim', () => {
  for (const ph of TERM_PLACEHOLDERS) assert.equal(scrubTermField(ph), '');
  assert.equal(scrubTermField('  台灣用法 '), '');
  assert.equal(scrubTermField(' 真的有字 '), '真的有字');
  assert.equal(scrubTermField(undefined), '');
  assert.equal(scrubTermField(null), '');
});

test('佐證定義：詞源任一欄位，或 usage 範疇', () => {
  assert.equal(hasTermEtymology(empty), false);
  assert.equal(hasTermEvidence(empty), false);
  assert.equal(hasTermEvidence({ ...empty, origin: 'kernel 譯法分流' }), true);
  assert.equal(hasTermEvidence({ ...empty, forkCause: '1949' }), true);
  // usage 範疇算佐證，但不算詞源（showFork 仍吃詞源那把尺）
  const usageOnly = { ...empty, usageNote: '只有動詞用法是中國網路用語' };
  assert.equal(hasTermEtymology(usageOnly), false);
  assert.equal(hasTermEvidence(usageOnly), true);
  assert.equal(
    hasTermEvidence({ ...empty, usageExample: '這支影片很好看' }),
    true,
  );
  // placeholder 已被 scrub 成空字串，不會變成佐證
  assert.equal(
    hasTermEvidence({ ...empty, origin: scrubTermField('中國用法') }),
    false,
  );
});

test('分桶：E / F 不看佐證，其餘看佐證', () => {
  assert.equal(termWordingBucket('E', false), 'diverging');
  assert.equal(termWordingBucket('E', true), 'diverging');
  assert.equal(termWordingBucket('F', false), 'same-word');
  assert.equal(termWordingBucket('B', true), 'evidenced');
  assert.equal(termWordingBucket('B', false), 'unverified');
  assert.equal(termWordingBucket('', false), 'unverified');
  assert.equal(termWordingBucket('C', true), 'evidenced');
});

const base = {
  china: '視頻',
  taiwanPrimary: '影片',
  taiwanAlts: '',
  forkKey: 'B',
};

test('有佐證：維持 2026-06-22 以來的直述句，一字不動', () => {
  const w = termWording({ ...base, evidenced: true });
  assert.equal(w.bucket, 'evidenced');
  assert.equal(w.lead, '「視頻」是中國大陸的用法，在台灣通常說「影片」。');
  assert.equal(
    w.faqAnswer,
    '是，「視頻」是中國大陸的常見說法，台灣慣用「影片」。',
  );
  assert.equal(w.seoLead, '中國說「視頻」，台灣說「影片」。');
  assert.equal(w.heroSubtitle, '在台灣，「視頻」要說「影片」。');
});

test('零佐證：四句都降級，不再出現最寬那句', () => {
  const w = termWording({
    ...base,
    china: '視頻監視',
    taiwanPrimary: '影像監視',
    evidenced: false,
  });
  assert.equal(w.bucket, 'unverified');
  for (const s of [w.lead, w.faqAnswer, w.seoLead, w.heroSubtitle]) {
    assert.ok(!s.includes(WIDE_CLAIM), `不該出現「${WIDE_CLAIM}」：${s}`);
    assert.ok(!s.includes(WIDE_LEAD), `不該出現「${WIDE_LEAD}」：${s}`);
    assert.ok(!s.startsWith('是，'), `不該用「是，」開頭：${s}`);
  }
  // 只說「有人回報」＋「還沒查證」，而且兩個詞都還在句子裡讓讀者對得上
  assert.ok(w.lead.includes('有人回報') && w.lead.includes('還沒查證'));
  assert.ok(w.faqAnswer.startsWith('還不確定'));
  assert.ok(
    w.faqAnswer.includes('「視頻監視」') &&
      w.faqAnswer.includes('「影像監視」'),
  );
  assert.ok(w.seoLead.includes('待查證'));
  assert.ok(w.heroSubtitle.includes('還沒查證'));
});

test('E 正在分歧 / F 同詞不同語感：原句不動，佐證與否無關', () => {
  for (const evidenced of [true, false]) {
    const e = termWording({
      ...base,
      china: '估計',
      taiwanPrimary: '大概',
      forkKey: 'E',
      evidenced,
    });
    assert.equal(e.bucket, 'diverging');
    assert.equal(
      e.lead,
      '「估計」是兩岸正在分歧的詞，雙方大致都聽得懂；台灣這邊多半說「大概」。',
    );
    assert.equal(
      e.faqAnswer,
      '「估計」兩岸都在用、正在分歧，台灣這邊習慣說「大概」。',
    );
    const f = termWording({
      ...base,
      china: '消息',
      taiwanPrimary: '訊息',
      forkKey: 'F',
      evidenced,
    });
    assert.equal(f.bucket, 'same-word');
    assert.equal(
      f.lead,
      '「消息」兩岸都在用，但語感與常用度不太一樣；台灣這邊比較常說「訊息」。',
    );
    assert.equal(
      f.faqAnswer,
      '「消息」兩岸都用，但語感不同；台灣這邊比較常說「訊息」。',
    );
    assert.equal(f.heroSubtitle, '在台灣，「消息」要說「訊息」。');
  }
});

test('display.taiwan 的其他說法以「也說」接在 lead 後面（四桶都一樣）', () => {
  for (const [forkKey, evidenced] of [
    ['B', true],
    ['B', false],
    ['E', true],
    ['F', true],
  ]) {
    const w = termWording({ ...base, taiwanAlts: '影音', forkKey, evidenced });
    assert.ok(w.lead.includes('（也說影音）'), `${w.bucket}: ${w.lead}`);
    assert.ok(!w.faqAnswer.includes('也說'), 'FAQ 只講主要說法');
  }
});
