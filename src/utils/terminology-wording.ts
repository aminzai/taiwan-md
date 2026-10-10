/**
 * terminology-wording.ts — /terminology/{id} 頁面的「這個詞算不算中國用語」說法。
 *
 * 從 src/pages/terminology/[id].astro 抽出來，讓它能被 node 直接測
 * （tests/terminology-wording.test.mjs），不用整站 build 才看得到字。
 *
 * 四層說法（2026-10-10 哲宇拍板 OBSERVER-QUEUE #76 選項 C）：
 *   diverging   fork_type E：兩岸正在分歧，雙方都聽得懂
 *   same-word   fork_type F：同一個詞，語感與常用度不同
 *   evidenced   其餘分類、而且條目有佐證（詞源任一欄位，或 usage 範疇）
 *               → 保留原本的直述句「是中國大陸的用法／常見說法」
 *   unverified  其餘分類、零佐證（import 預設的那一千七百條）
 *               → 只說這條記錄了有人回報的差異，來源還沒查證
 *
 * 為什麼要降級：2026-06-22 import 的 1,716 條預設 B、93% 零佐證，站上卻對每
 * 一條都講最寬那句「是，X 是中國大陸的常見說法」。09-15 讀者從站外踩到「消息」
 * （issue #1733，教育部辭典本就有的台灣詞目）、09-30 再踩到「內核」（issue #1786）。
 * 這裡命中的是 render 層，不動 data/terminology/*.yaml；逐條複查是另一張工單。
 */

/** 1997/ThunderKO import 留下的填充字，視同空值（跟 [id].astro 原本的清單一致）。 */
export const TERM_PLACEHOLDERS: ReadonlySet<string> = new Set([
  '台灣用法',
  '台灣用語',
  '中國用法',
  '中國用語',
  '用法',
  '無',
]);

/** 填充字 → 空字串；其餘 trim。 */
export const scrubTermField = (s: string | undefined | null): string => {
  const v = (s || '').trim();
  return TERM_PLACEHOLDERS.has(v) ? '' : v;
};

export interface TermEvidenceFields {
  origin: string;
  taiwanPath: string;
  chinaPath: string;
  forkPoint: string;
  forkCause: string;
  usageExample: string;
  usageNote: string;
}

/** 詞源任一欄位有字（placeholder 已清掉）。沿用 [id].astro 的 hasRealEtymology。 */
export const hasTermEtymology = (f: TermEvidenceFields): boolean =>
  Boolean(
    f.origin || f.forkPoint || f.forkCause || f.taiwanPath || f.chinaPath,
  );

/**
 * 佐證定義（OBSERVER-QUEUE #76 原文：「`etymology` 空且無 `usage` 範疇」= 零佐證）。
 * 傳進來的欄位必須先過 scrubTermField。
 */
export const hasTermEvidence = (f: TermEvidenceFields): boolean =>
  hasTermEtymology(f) || Boolean(f.usageExample || f.usageNote);

export type TermWordingBucket =
  | 'diverging'
  | 'same-word'
  | 'evidenced'
  | 'unverified';

export function termWordingBucket(
  forkKey: string,
  evidenced: boolean,
): TermWordingBucket {
  if (forkKey === 'E') return 'diverging';
  if (forkKey === 'F') return 'same-word';
  return evidenced ? 'evidenced' : 'unverified';
}

export interface TermWordingInput {
  china: string; // cleaned primary china term
  taiwanPrimary: string; // first alternative of display.taiwan
  taiwanAlts: string; // remaining alternatives joined by 「、」, may be ''
  forkKey: string; // normalized A–F or ''
  evidenced: boolean; // hasTermEvidence(...)
}

export interface TermWording {
  bucket: TermWordingBucket;
  /** 正文第一句（粗體 lead）。 */
  lead: string;
  /** FAQ「算中國用語嗎？」的答案（不含 usage.note 尾巴，由頁面自己接）。 */
  faqAnswer: string;
  /** meta description 的第一句。 */
  seoLead: string;
  /** Hero 副標（display.taiwan 沒有多個說法時用）。 */
  heroSubtitle: string;
}

export function termWording(i: TermWordingInput): TermWording {
  const bucket = termWordingBucket(i.forkKey, i.evidenced);
  const alt = i.taiwanAlts ? `（也說${i.taiwanAlts}）` : '';
  const c = i.china;
  const t = i.taiwanPrimary;

  switch (bucket) {
    case 'diverging':
      return {
        bucket,
        lead: `「${c}」是兩岸正在分歧的詞，雙方大致都聽得懂；台灣這邊多半說「${t}」${alt}。`,
        faqAnswer: `「${c}」兩岸都在用、正在分歧，台灣這邊習慣說「${t}」。`,
        seoLead: `中國說「${c}」，台灣說「${t}」。`,
        heroSubtitle: `在台灣，「${c}」要說「${t}」。`,
      };
    case 'same-word':
      return {
        bucket,
        lead: `「${c}」兩岸都在用，但語感與常用度不太一樣；台灣這邊比較常說「${t}」${alt}。`,
        faqAnswer: `「${c}」兩岸都用，但語感不同；台灣這邊比較常說「${t}」。`,
        seoLead: `中國說「${c}」，台灣說「${t}」。`,
        heroSubtitle: `在台灣，「${c}」要說「${t}」。`,
      };
    case 'evidenced':
      return {
        bucket,
        lead: `「${c}」是中國大陸的用法，在台灣通常說「${t}」${alt}。`,
        faqAnswer: `是，「${c}」是中國大陸的常見說法，台灣慣用「${t}」。`,
        seoLead: `中國說「${c}」，台灣說「${t}」。`,
        heroSubtitle: `在台灣，「${c}」要說「${t}」。`,
      };
    case 'unverified':
    default:
      return {
        bucket,
        lead: `有人回報「${c}」在中國比較常見、台灣說「${t}」${alt}；這一條還沒查證來源，先照實記著。`,
        faqAnswer: `還不確定。這條目前只記錄了有人回報的差異（中國說「${c}」、台灣說「${t}」），來源還沒查證。`,
        seoLead: `有人回報中國說「${c}」、台灣說「${t}」，來源待查證。`,
        heroSubtitle: `有人回報的差異，來源還沒查證。`,
      };
  }
}
