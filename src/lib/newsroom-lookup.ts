// newsroom-lookup.ts — 文章頁「編輯台足跡」的 build-time 查找層
//
// dashboard-newsroom.json（generate-newsroom-data.py 產）→ slug/knowledge 路徑雙鍵 Map。
// Module scope：整個 build 進程建一次（.astro frontmatter 是 per-render scope，
// cache 放那裡每頁重建——2026-06-13 refactor-article 教訓）。
import board from '../../public/api/dashboard-newsroom.json';

export interface NewsroomStage {
  status?: string;
  artifact?: string;
  at?: string;
  rounds?: string;
  stage35?: string;
  stage36?: string;
  [key: string]: unknown;
}
export interface NewsroomRecord {
  slug: string;
  title: string;
  spine_type?: string | null;
  stages: Record<string, NewsroomStage>;
}

let _byKnowledgePath: Map<string, NewsroomRecord> | null = null;
let _bySlug: Map<string, NewsroomRecord> | null = null;

function build() {
  _byKnowledgePath = new Map();
  _bySlug = new Map();
  for (const a of (board as any).articles as NewsroomRecord[]) {
    _bySlug.set(a.slug, a);
    const ship = a.stages?.ship?.artifact;
    if (ship) _byKnowledgePath.set(ship, a);
  }
}

/** 用 knowledge 檔路徑（category + slug）找編輯台紀錄；找不到回 null。 */
export function findNewsroomRecord(
  category: string,
  slug: string,
): NewsroomRecord | null {
  if (!_byKnowledgePath) build();
  return (
    _byKnowledgePath!.get(`knowledge/${category}/${slug}.md`) ??
    _bySlug!.get(slug) ??
    null
  );
}

/** 這筆紀錄有沒有值得展示的早期產物（投影／編輯室／audit）。 */
export function hasTrail(rec: NewsroomRecord | null): boolean {
  if (!rec) return false;
  const s = rec.stages;
  return !!(
    s.projection ||
    s.room_projection ||
    s.room_prose ||
    s.room_chief ||
    s.research
  );
}
