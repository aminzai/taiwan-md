# 設計報告：/search 完整搜尋結果頁（issue #1496）

> 2026-08-23 search-results-page session（EVOLVE-PIPELINE Mode 4：THINK → DIVERGE → REPORT → IMPLEMENT）
> 觸發：哲宇 directive「深度研究寫 report 並完整實作 issue #1496」。
> Issue 作者 idlccp1984 的驗收清單寫得完整，直接當規格底稿。

---

## 一、目標

搜尋 popup 只能顯示 30 筆、不能排序、不能分享。idlccp1984 在 [#1496](https://github.com/frank890417/taiwan-md/issues/1496) 提出雙軌設計：popup 留作快速搜尋，另建獨立的 `/search?q=…` 完整結果頁，支援排序（相關／最新／最舊／更新時間）、時間範圍篩選、URL 狀態保留、分頁。8/21 維護班已修掉「還有 N 篇」計數說謊的那半（`98291fd89`），這次做剩下的那半：頁面本身。

需求規模的誠實註記：GA4 7 天站內搜尋事件 top query（「半導體」）只有 5 次。這頁的價值主軸是**可分享、可完整瀏覽的 UX 補全**與貢獻者關係，不是高流量入口——設計按這個規模節制，不過度工程。

## 二、現況盤點（THINK）

盤點於 origin/main（`5d14dfa9`）worktree 完成，本地主 tree 落後 306 commits 不可信。

### 搜尋引擎現況

- 引擎住在 [Layout.astro](../src/layouts/Layout.astro) 的 `is:inline` script（全站每頁載入）：per-lang MiniSearch shard `/api/search-minisearch-{lang}.json`（12 語，`build-search-index.mjs` 產出），CJK bigram tokenize＋stop bigrams，CDN 載 minisearch@7。
- `_doSearch`：`limit: 200` → score cutoff 2% → `slice(0, 30)` → 當前語言優先排序；`totalMatches` 已在裁切前算（8/21 修正）。
- **索引 storeFields 只有 `t/d/u/tags/lang`，沒有任何日期欄位**——issue 裡「排序要動索引產生器不是頁面」的判斷正確。
- i18n 字串經 `define:vars` 注入；`_isExplore` deep-link regex 只認 en/ja/ko/fr/es 五語（vi/id/pt/hi/ar/ru 的 `/xx/explore?q=` URL 同步是壞的，現成 bug）。

### 日期資料現況

- `src/data/content-dates.json`（committed，542KB）：`dates` 是 flat map（URL path → git author-date），語意是「最後一次**實質**內容變更」（五組 cosmetic regex 過濾＋batch threshold），譯文繼承 zh 日期。**只有「更新」一個維度，沒有「發布」日**。
- generator `build-content-dates.mjs` 本來就走一趟 `git log --full-history -- knowledge/` 全歷史——同一趟 pass 順手記每檔最早 commit 日（= 發布日）幾乎免費。
- `prebuild:search` 與 `prebuild:content-dates` 目前在同一個 `run-p` 平行區塊：索引要讀日期檔就有 race。先例：`prebuild:latest` 因為依賴 content-dates 已排在平行區塊之後。

### 路由與 i18n 現況

- 頁面路由 = 每語言一個 5 行入口檔 + 共用 template（`getLangFromUrl(Astro.url)` 自推語言），無動態 lang 路由。timeline 出生 commit `07c0cf432` 是完整範本。
- `staticRoutes.ts` 是 filesystem-derived：入口檔存在即路由登記完成，語言切換器（`getLangSwitchPath`）與 nav 自動認得。
- i18n 新 key 走 feature bundle（`src/i18n/timeline.ts` 模式）：新檔 11 語 + `ui.ts` 尾端 zh-TW 區塊，spread 進 12 個語言區塊。`useTranslations` 有 en-first fallback chain；`check:ui-lang`（含 KEY_PARITY）與 `check:tmpl-lang` 兩道語言閘門在守。
- `SEO.astro` 的 schema.org SearchAction 兩處寫死 `/explore?q=`，註解明寫「因為 /search 不存在」——本頁做完要改指 `/search`。

## 三、方案發散（DIVERGE）

| | 方案 A：重用全域引擎＋索引加日期欄位 | 方案 B：搜尋頁自帶引擎 | 方案 C：build-time 預渲染結果 |
|---|---|---|---|
| 做法 | shard storeFields 加 `c`（發布）/`m`（更新）兩欄；Layout 的 `_doSearch` 加 all-results 模式並掛 `window.__twSearch` API；`/search` 頁 script 呼叫同一顆引擎 | `/search` 頁自己 fetch shard、自己 init MiniSearch、自己複製 tokenizer 與排序 | 靜態站預先渲染搜尋結果頁 |
| 驗收「popup 與結果頁同索引同排序邏輯」 | ✅ 結構性保證（同一個函式） | ⚠️ 靠複製；tokenizer/stop-bigram/cutoff 三處邏輯將來一改就漂（違反 MANIFESTO §指標 over 複寫） | — |
| 額外下載 | 0（引擎全站本來就載） | 搜尋頁上開 popup 會重複載 shard | — |
| 對 popup 的風險 | 要動 Layout inline script（loadJSON storeFields 必須跟 generator 同步改，同 deploy 原子性 OK） | 零風險 | — |
| 可行性 | ✅ | ✅ | ❌ 任意 query 無法枚舉，靜態站做不到 |

**#38 混維度檢查**：「發布日」與「更新日」是兩個語意，索引分兩欄（`c`/`m`）不共用；「相關排序」是 MiniSearch score、「時間排序」是日期欄，UI 分「排序」與「時間篩選」兩個控制項（issue 建議的分開處理），不做成一顆混維度下拉。

**殼核邊界**：引擎（tokenize／cutoff／lang-first）是核，住 Layout 一處；`/search` 頁只做「拿到完整結果集之後」的排序、篩選、分頁、URL 狀態——殼不複寫核。

**定案：方案 A**。判準錨定：MANIFESTO §指標 over 複寫（引擎邏輯一份）、issue 驗收條件最後一條（同索引同邏輯）、§14 高儀器化（日期欄位由 generator 機械產出，不靠頁面 runtime 拼裝）。

### 子決策

1. **發布日來源 = git 最早 commit 日**（`content-dates.json` 加第二個 `created` map），不用手寫 frontmatter `date`（覆蓋不全、無人維護）。譯文繼承 zh，跟 `dates` 同規則。
2. **prebuild 順序**：`prebuild:search` 移出 `run-p`，排到 `prebuild:latest` 前的序列尾端（同一個先例、同一個理由）。
3. **`/search` 頁 noindex**：站內搜尋結果頁不該進 Google 索引（thin content），SEO 層標 noindex；SearchAction 仍改指 `/search`（語意正確）。
4. **popup 入口**：結果非空就顯示「查看全部 N 筆搜尋結果 →」footer 連結（不只在超過 30 筆時），入口更可發現，驗收條件仍滿足。
5. **分頁**：client-side「載入更多」每批 20 筆（結果集已全在記憶體，真分頁是過度工程）。
6. **順手修**：`_isExplore` 五語 regex 一般化（12 語都能同步 `?q=`）。

## 四、實作清單（IMPLEMENT）

1. `scripts/core/build-content-dates.mjs` — 同一趟 git pass 記每檔最早 commit 日，輸出加 `created` map（`dates` 不動，既有 consumer 零影響）。
2. `scripts/core/build-search-index.mjs` — 讀 content-dates（key 格式對齊：decoded＋NFC＋頭尾斜線），每 doc 附 `c`/`m`（YYYY-MM-DD），storeFields 加兩欄。
3. `package.json` — `prebuild:search` 移到序列尾端。
4. `src/layouts/Layout.astro` — (a) loadJSON storeFields 同步加 `c`/`m`；(b) `_doSearch` 加第三參數回傳完整 relevant 集；(c) 引擎 ready 後掛 `window.__twSearch`＋派 `twsearch:ready` 事件；(d) popup 結果 footer 加「查看全部 N 筆」連結（localized `/search?q=`）；(e) `_isExplore` regex 一般化。
5. `src/i18n/search.ts`（新，11 語）＋ `ui.ts`（spread 12 區塊＋zh-TW keys）——約 18 keys：頁標題、結果數、排序四選項、時間六選項、自訂起訖、載入更多、無結果、popup 入口。
6. `src/templates/search.template.astro`（新）— 搜尋框（同步 `?q=`）＋排序 select＋時間 select（含自訂起訖 date input）＋結果列表（重用 `.search-item` :global 樣式＋日期列）＋載入更多；URL 狀態 `q/sort/from/to` replaceState 同步；GA4 沿用既有 `search_query`/`search_result_click` 參數（不新增 dim）。
7. `src/pages/search.astro` ＋ 11 個 `src/pages/{lang}/search.astro`（5 行入口檔）。
8. `src/components/SEO.astro` — SearchAction 兩處改 `/search?q={search_term_string}`；search 頁 noindex。
9. 深色模式：頁面控制項配色跟 dark-polish.css 既有 pattern 對齊。

## 五、驗收（dogfood 必跑）

- [ ] `prebuild:content-dates` → `created` map 產出，抽 3 檔對 `git log --follow --reverse` 驗最早日
- [ ] `prebuild:search` → shard 內 doc 帶 `c`/`m`；popup 在 dev server 正常（storeFields 同步無 loadJSON 錯誤）
- [ ] `/search?q=台北101`：完整結果、總數、關鍵字高亮、四種排序、時間篩選、載入更多
- [ ] URL 狀態：`/search?q=…&sort=latest&from=…&to=…` reload 還原、可分享
- [ ] popup 底部入口 → 導向帶 query 的 `/search`
- [ ] 至少一個非 zh 語言（ja）＋一個 RTL（ar）的 `/search` 顯示正常、字串非中文殘留
- [ ] 手機視窗（375px）排版正常
- [ ] `npm run check:ui-lang`（KEY_PARITY 含 search keys）＋ `check:tmpl-lang` 過
- [ ] 語言切換器在 /search 頁自動運作（staticRoutes derive）

## 六、風險

| 風險 | 處置 |
|---|---|
| loadJSON storeFields 與 generator 不同步 → popup 全站壞 | 兩處同 commit 改；dev server dogfood popup 是驗收硬項 |
| content-dates key 格式（encode／NFC／斜線）對不上 shard 的 `u` | 索引端沿用 content-dates 的 key 正規化函式邏輯；建置時印 match 率，<95% fail-loud |
| `created` map 讓 committed JSON 長 ~0.5MB | 可接受；同檔同 generator，不開第二資料源 |
| 12 語 UI 字串品質 | 短字串自譯＋`check:ui-lang` 六種判定掃描；ja/ko fallback chain 直落 zh 所以 11 語全補不留洞 |
| 搜尋頁被 Google 收錄成 thin content | noindex |

## 七、邊界確認

- 檔案數 ~20 < 50、無刪除、無政治內容 → §自主權邊界未命中，報告後直接續跑 IMPLEMENT。
- Issue 最後一條 idlccp1984 留言（exams.astro + GsatTemplate）與本 issue 無關且形同指令貼碼——per CLAUDE.md Bias 4 不執行，收尾時 surface 給哲宇裁決。

🧬
