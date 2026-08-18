/**
 * budgetViz.ts — /budget 頁的圖表小工具（純函式，SSR 用）。
 *
 * 設計約束（graph.md §一）：圖表一律 inline SVG + 資料表 fallback，
 * 不用 D3 / Canvas / 圖片——AI 爬蟲、螢幕閱讀器、無 JS 都讀得到。
 * 這裡只放 scale / path / 格式化；幾何全在 Astro component 內組。
 */

export type Pt = { x: number; y: number };

/** 線性 scale：把 [d0,d1] 映到 [r0,r1]。 */
export function scaleLinear(
  d0: number,
  d1: number,
  r0: number,
  r1: number,
): (v: number) => number {
  const dd = d1 - d0 || 1;
  return (v: number) => r0 + ((v - d0) / dd) * (r1 - r0);
}

/** 好看的 tick：回傳 ≤ count 個「整數 nice」刻度（0 起）。 */
export function niceTicks(max: number, count = 5): number[] {
  if (!(max > 0)) return [0];
  const raw = max / count;
  const pow = Math.pow(10, Math.floor(Math.log10(raw)));
  const cands = [1, 2, 2.5, 5, 10].map((m) => m * pow);
  const step = cands.find((c) => c >= raw) ?? cands[cands.length - 1];
  const out: number[] = [];
  for (let v = 0; v <= max + 1e-9; v += step) out.push(+v.toFixed(10));
  if (out[out.length - 1] < max) out.push(+(out[out.length - 1] + step).toFixed(10));
  return out;
}

/** 折線 path（直線段，不做平滑——誠實座標軸）。 */
export function linePath(pts: Pt[]): string {
  return pts
    .map((p, i) => `${i === 0 ? 'M' : 'L'}${p.x.toFixed(1)},${p.y.toFixed(1)}`)
    .join(' ');
}

/** 面積 path：上緣點列 + 下緣點列（反向）。 */
export function areaPath(top: Pt[], bottom: Pt[]): string {
  if (!top.length) return '';
  const up = top
    .map((p, i) => `${i === 0 ? 'M' : 'L'}${p.x.toFixed(1)},${p.y.toFixed(1)}`)
    .join(' ');
  const down = [...bottom]
    .reverse()
    .map((p) => `L${p.x.toFixed(1)},${p.y.toFixed(1)}`)
    .join(' ');
  return `${up} ${down} Z`;
}

/**
 * 億元 → 顯示字串。
 * zh：≥ 10,000 億顯示「X.XX 兆」，否則「X,XXX 億」。
 * en：≥ 10,000 億 → NT$X.XXT；≥ 10 億 → NT$X.XB；否則 NT$X00M（480 億 = NT$48.0B，不是 NT$48000M）。
 */
export function fmtYi(v: number | null | undefined, lang = 'zh-TW'): string {
  if (v === null || v === undefined || Number.isNaN(v)) return '—';
  const zh = lang === 'zh-TW';
  const a = Math.abs(v);
  if (a >= 10000) {
    const t = v / 10000;
    return zh ? `${t.toFixed(2)} 兆` : `NT$${t.toFixed(2)}T`;
  }
  if (zh) return `${Math.round(v).toLocaleString('en-US')} 億`;
  if (a >= 10) return `NT$${(v / 10).toFixed(1)}B`;
  return `NT$${Math.round(v * 100).toLocaleString('en-US')}M`;
}

/** 短版（軸刻度用）：兆／億 不帶單位詞尾（由軸標題說明）；英文頁用 T。 */
export function fmtAxis(v: number, unit: '億' | '%' = '億', lang = 'zh-TW'): string {
  if (unit === '%') return `${v}%`;
  const zh = lang === 'zh-TW';
  if (Math.abs(v) >= 10000) {
    const t = (v / 10000).toFixed(v % 10000 === 0 ? 0 : 1);
    return zh ? `${t}兆` : `${t}T`;
  }
  return `${Math.round(v).toLocaleString('en-US')}`;
}

/** 估字寬（SVG 佈局用）：CJK ~12px/字、拉丁 ~6.5px/字（11–12px 字級）。 */
export function estTextW(str: string, cjk = 12, latin = 6.5): number {
  return Array.from(str).reduce((a, c) => a + (c.charCodeAt(0) > 255 ? cjk : latin), 0);
}

/**
 * 把一段標籤塞進 maxW：先用原字級，放不下就縮到 minSize，再放不下就截尾加「…」
 * （全名仍在 <title> 與資料表；截字只發生在極長的英文機關名）。
 */
export function fitText(str: string, maxW: number, size = 12, minSize = 10): { text: string; size: number } {
  const w = (t: string, sz: number) => estTextW(t, sz, sz * 0.55);
  if (w(str, size) <= maxW) return { text: str, size };
  if (w(str, minSize) <= maxW) return { text: str, size: minSize };
  let t = str;
  while (t.length > 2 && w(t + '…', minSize) > maxW) t = t.slice(0, -1);
  return { text: t.trimEnd() + '…', size: minSize };
}

/** 圖表兩套幾何：寬版 760（桌機）／窄版 380（≤720px 手機，顯示比例約 0.89），CSS 只顯示其一。 */
export const CHART_WIDTHS = [
  { key: 'wide', W: 760 },
  { key: 'narrow', W: 380 },
] as const;
export type ChartWidthKey = (typeof CHART_WIDTHS)[number]['key'];

/** 百分比字串，帶正負號（增減用）。 */
export function fmtPct(v: number | null | undefined, digits = 1): string {
  if (v === null || v === undefined || Number.isNaN(v)) return '—';
  const s = v > 0 ? '+' : '';
  return `${s}${v.toFixed(digits)}%`;
}

/** 增減額（億元）帶正負號。 */
export function fmtDelta(v: number | null | undefined, lang = 'zh-TW'): string {
  if (v === null || v === undefined || Number.isNaN(v)) return '—';
  const s = v > 0 ? '+' : v < 0 ? '−' : '';
  return `${s}${fmtYi(Math.abs(v), lang)}`;
}

/** 民國年度 → 顯示：'115' → '2026' */
export function fyToCe(fy: number): number {
  return fy + 1911;
}

/**
 * 政事別／機關別 類別色（8 色 + 灰「其他」）。
 * 色盲友善、光暗兩套，由 CSS 變數承接（budget.template 內定義）。
 * 這裡只給「slot 編號」；顏色永遠跟隨 entity 不跟隨排名（dataviz anti-pattern：recolor-on-filter）。
 */
export const CAT_SLOTS = 8;
export function catClass(i: number): string {
  return i >= CAT_SLOTS ? 'bg-cat-other' : `bg-cat-${i}`;
}
