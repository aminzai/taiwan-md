/**
 * article-embeds.ts — 把 renderer 吐出的 tw-article placeholder 解析成可以餵給
 * <ArticleCard density="embed"> 的資料（2026-08-19）
 *
 * 分工：
 * - article-render.ts 的 renderTwModule('tw-article') 是純字串層，只吐
 *   `<div class="tw-article"><div class="tw-article-slot" data-tw-cat data-tw-slug
 *   [data-tw-note]><a href>…</a></div>…</div>`，裡面那條 <a> 是沒有 Astro 後處理
 *   的消費端（RSS／llms.txt）看到的 fallback。
 * - 這裡在 Astro 層把 HTML 切成「純 HTML 片段」與「卡片資料」交錯的陣列，
 *   ArticleProse.astro 逐段 set:html／逐卡 <ArticleCard>。卡片 markup 因此只有
 *   ArticleCard.astro 一份，renderer 不手刻第二份。
 *
 * 語言：作者寫的是 zh 路徑；十二語頁面靠 getArticleByZhPath 用譯文 frontmatter 的
 * translatedFrom 反查該語譯文；查無就退回 zh 文章＋zh 連結（不 404、不留空殼）。
 */
import {
  getArticleByZhPath,
  getArticleShipDate,
  type ArticleSummary,
} from './articles-index';

export interface EmbedCard {
  article: ArticleSummary;
  /** 實際命中的語言（可能退回 zh-TW），呼叫端據此組 href 前綴 */
  lang: string;
  /** 作者在區塊裡用 `| …` 覆蓋的一句摘要（已 HTML-unescape） */
  note?: string;
  /** git 上站時間 ISO 字串；沒有就空字串 */
  shipDate: string;
}
export interface EmbedHtml {
  kind: 'html';
  html: string;
}
/** 同一個 ```tw-article 區塊裡的一或多張卡，同一個 .tw-article 容器內堆疊 */
export interface EmbedCards {
  kind: 'cards';
  cards: EmbedCard[];
}
export type ProsePart = EmbedHtml | EmbedCards;

// 整個 .tw-article 容器（含一或多個 slot）；slot 內是 renderer 的 fallback <a>。
// 結構是 renderer 固定吐的，所以用「一到多個完整 slot」精準比對，不用 lazy `.*?`
// 去猜巢狀 </div> 是誰的。
const CONTAINER_RE =
  /<div class="tw-article">((?:<div class="tw-article-slot"[^>]*><a [^>]*>[\s\S]*?<\/a><\/div>)+)<\/div>/g;
const SLOT_RE =
  /<div class="tw-article-slot" data-tw-cat="([^"]*)" data-tw-slug="([^"]*)"(?: data-tw-note="([^"]*)")?><a [^>]*>[\s\S]*?<\/a><\/div>/g;

const _unesc = (s: string) =>
  s
    .replace(/&quot;/g, '"')
    .replace(/&gt;/g, '>')
    .replace(/&lt;/g, '<')
    .replace(/&amp;/g, '&');

/**
 * 摘要截短：卡片住在段落之間，摘要要比 /latest 短一截。以 CJK 字元計、在
 * 句讀（。！？；，、）處優先斷，超過上限才硬切加省略號。作者用 `| …` 覆蓋時
 * 不截（那句是他刻意寫的）。
 */
export function trimSummary(text: string, max = 64): string {
  const t = (text || '').trim();
  if ([...t].length <= max) return t;
  const head = [...t].slice(0, max).join('');
  const cut = Math.max(
    head.lastIndexOf('。'),
    head.lastIndexOf('！'),
    head.lastIndexOf('？'),
    head.lastIndexOf('；'),
    head.lastIndexOf('，'),
    head.lastIndexOf('、'),
    head.lastIndexOf('. '),
    head.lastIndexOf(', '),
  );
  // 斷點太靠前（少於一半）就不用它，硬切
  const body = cut >= max / 2 ? head.slice(0, cut) : head;
  return body.replace(/[，、,\s]+$/, '') + '…';
}

/**
 * 把渲染後的文章 HTML 切成 ProsePart[]。沒有任何 tw-article 時回傳單一 html
 * 片段（零成本路徑：絕大多數文章）。查無的 slot 原樣留下（fallback <a> 仍在）。
 */
export async function resolveArticleEmbeds(
  html: string,
  lang: string,
): Promise<ProsePart[]> {
  if (!html.includes('class="tw-article"')) return [{ kind: 'html', html }];

  const parts: ProsePart[] = [];
  let last = 0;
  CONTAINER_RE.lastIndex = 0;
  let m: RegExpExecArray | null;
  while ((m = CONTAINER_RE.exec(html)) !== null) {
    const before = html.slice(last, m.index);
    if (before) parts.push({ kind: 'html', html: before });
    last = m.index + m[0].length;

    const inner = m[1];
    const cards: EmbedCard[] = [];
    const unresolved: string[] = [];
    SLOT_RE.lastIndex = 0;
    let sm: RegExpExecArray | null;
    while ((sm = SLOT_RE.exec(inner)) !== null) {
      const cat = _unesc(sm[1]);
      const slug = _unesc(sm[2]);
      const note = sm[3] ? _unesc(sm[3]) : undefined;
      const hit = await getArticleByZhPath(lang, cat, slug);
      if (!hit) {
        unresolved.push(sm[0]);
        continue;
      }
      // 上站日優先取該語譯文自己的；譯文太新還沒進 content-dates 時退回 zh 原文的
      // ——讀者要的是「這篇什麼時候出來的」，翻譯日是次要的。
      let shipDate = await getArticleShipDate(
        hit.lang,
        hit.article.category,
        hit.article.slug,
      );
      if (!shipDate && hit.lang !== 'zh-TW') {
        shipDate = await getArticleShipDate('zh-TW', cat, slug);
      }
      cards.push({
        article: hit.article,
        lang: hit.lang,
        note,
        shipDate,
      });
    }
    // 有卡片就以卡片取代整個容器；查無的 slot 保留 fallback 連結，不靜默消失
    if (cards.length === 0) {
      parts.push({ kind: 'html', html: m[0] });
      continue;
    }
    if (unresolved.length) {
      parts.push({
        kind: 'html',
        html: `<div class="tw-article">${unresolved.join('')}</div>`,
      });
    }
    parts.push({ kind: 'cards', cards });
  }
  const tail = html.slice(last);
  if (tail) parts.push({ kind: 'html', html: tail });
  return parts;
}
