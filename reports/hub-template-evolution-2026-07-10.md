# Hub 模板深度評估與改良報告 — 2026-07-10

> session：2026-07-10-230836-hub-template（哲宇 /goal：深度研究＋優化文章 hub 模板）
> 範圍：`/history/`、`/technology/` 等 13 個分類 hub 頁 × 6 語言（單一模板 `src/templates/category-hub.template.astro`）
> 方法：Fable 主 session 規劃與驗證；3 個 Sonnet 研究 agent（codebase 審計 / 內容資料盤點 / 外部最佳實務）＋ dev server 實機截圖審計
> 結論落地：本報告 §四 提案 → §五 實作計畫 → §六 實作結果（同 session ship）

---

## 〇、30 秒總覽

Hub 頁是全站第二大門面（首頁 → 分類 → 文章的必經節點），但它拿到的設計投資遠低於首頁與文章頁。四維評估的結論：**骨架健康（單模板六語共用、密度合理、dark mode 有 override 層撐住），血肉錯位**——策展導讀被切成兩半（頭尾各一份、中間隔著全部文章）、視覺零錨點（image 資料收了不用）、時間感完全缺席（沒有任何日期）、子分類 taxonomy 破碎被 UI 放大（單篇小節成排）、排序與標籤功能是死碼、非中文語系出現中英混排的小節標題。

| 維度     | 改版前 | 改版後 | 一句話診斷（前）→ 主要處方                                                                                               |
| -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------ |
| 視覺     | 2.5    | 4      | hub 區塊硬編 hex、零視覺錨點、首屏文字牆 → 精選書架（圖卡＋drop-cap fallback）、token 化、hook 收斂                      |
| 資訊結構 | 2      | 4      | 導讀重複兩份隔著 50 列；子分類破碎 → hook/essay 切分去重、伺服端分組＋單篇合併、多語顯示對應                             |
| UI/UX    | 2.5    | 4      | 排序死碼、搜尋只比標題、a11y 缺 → 排序真 UI、搜尋全欄位＋aria-live、ul/li 語意、heading 階層修正                         |
| 實用度   | 2      | 4      | 零時間訊號、零結構化資料 → 更新日期全面上線（content-dates join）、CollectionPage/ItemList/BreadcrumbList、d3 視覺化復活 |

改版後分數是本 session 自評（含實測證據，§6.2），不給 5 是因為 P2 清單還在（§七）＋讀者數據還沒回來：分數的最後一格由 GA4 決定，不由作者決定。

---

## 一、現況解剖

### 1.1 架構

```
src/pages/[category]/index.astro            ← zh-TW thin wrapper（20 行）
src/pages/{en,ja,ko,es,fr}/[category]/…     ← 5 個 thin wrapper（各 13 行）
src/templates/category-hub.template.astro   ← 全部 UI（2,298 行）
src/utils/category-static-paths.ts          ← 資料層（199 行，讀 knowledge/ frontmatter）
```

2026-05-03 sleepy-colden P1 統一化之後的形狀：六語共用一個模板，這是本次能「改一處、六語受益」的前提，架構層不需要動。

### 1.2 資料流與平行輪子

`category-static-paths.ts` 自己 readdir + gray-matter 掃 `knowledge/`，計算 topPicks（featured ＋腳註數門檻）與排序（featured → 腳註數 → 標題）。問題：`src/utils/articles-index.ts` 已經有一套更完整的文章索引（`getAllArticles` / `getLatestArticles` join `content-dates.json` git 實際 ship 時間 / `getRelatedArticles` 語意相關），/latest、/explore、首頁 strip 都用它。**hub 的資料層是第二顆平行的輪子，而且比較舊**：拿不到 git 日期，也拿不到語意相關。

`content-dates.json` 現況：5,456 筆 URL → ISO 時間（全語系覆蓋），hub 完全沒用到。

### 1.3 模板渲染段落（上到下）

1. 分類色 header：麵包屑＋icon＋h1＋描述（mobile 隱藏）＋「N 篇文章」pill
2. `hubHook`：導讀前三段（用「數第 3 個 `</p>`」切）＋「閱讀完整策展導讀→」錨點連結
3. 兩欄：左 sticky sidebar（主題子分類 nav ＋其他主題跨分類 nav）／右內容
4. 精選 chips（topPicks 前 3，純文字 pill）
5. 搜尋框（只比對 title）
6. 文章列（依 subcategory 分組，組內 featured → 腳註 → 標題；列＝★＋標題＋一行描述＋引用數＋分鐘數）
7. Food 專屬 d3 視覺化（zh 限定）／ Economy 專屬 inline 圖表（zh 限定）
8. `#hub-essay`：完整導讀白卡（含 hook 已經展示過的前三段）
9. 空分類 empty state

---

## 二、四維評估

### 2.1 視覺

實機截圖審計（dev server，1440×900 / 375×812 / dark mode）：

- **首屏被 hook 文字牆佔滿**。desktop：三段導讀＋標題列吃掉整個 first fold，第一篇文章在折線以下；mobile：hook 佔約 2.5 個螢幕高，讀者點進「歷史」後看不到任何一篇文章。en 版更糟：`/en/history/` 的 hook 切出 1,885 字元（zh 版 391–516），因為「數三個 `</p>`」的啟發式對段落結構不同的英文導讀失效。
- **零視覺錨點**。資料層收集了 `image / imageAlt / imageCredit`，模板一處都沒渲染。50 列純文字，精選也只是文字 chip。對照站內已有的 `ArticleCard.astro`（首頁／explore 用，含圖卡片），hub 是全站唯一完全無圖的門面。
- **硬編 hex 色票**。模板內約有數十處 `#475569 / #94a3b8 / #e2e8f0 / #f1f5f9 / bg-white`，不走 `tokens.css` 的 `--color-ink / --color-border / --color-surface`。實測 dark mode 沒有崩（`dark-polish.css` 2,342 行 override 層接住了：essay 卡實測 `rgb(20,20,24)`、列標題 `rgb(241,245,249)`），但這是「patch 層蓋住病灶」而非「模板自己健康」：每加一個新 hub 區塊都要去 dark-polish 補一段，維護成本持續累積。
- **寬螢幕右側大片留白**。hook 限寬 800px、header 限寬 container-wide，1440px 下右半近乎全空，沒有承載任何資訊。
- **導讀白卡突兀**。essay 是 `bg-white` 圓角卡（4,911px 高），浮在紙感底色上，與文章頁的排版語言（`--font-editorial`、prose 樣式）只有部分一致。

### 2.2 資訊結構

- **導讀被切成兩份、隔著整個列表**。hook（前三段）在頁首，完整導讀（含同樣三段）在 5,514px 處（全頁 11,275px），中間是 50 列文章。想讀完整導讀的人要跳過整個索引；讀完導讀想回列表的人要往回捲 5,000px。策展導讀是 hub 的靈魂（MANIFESTO 策展式非百科式的落地），現在的擺位讓它既搶了索引的首屏、又沒得到可讀的環境。
- **子分類 taxonomy 破碎，UI 照單全收**。實測：

| Hub          | 文章數 | 子分類數 | 單篇小節 | 症狀                                                                                       |
| ------------ | ------ | -------- | -------- | ------------------------------------------------------------------------------------------ |
| /history/    | 50     | 13       | 7        | 「殖民地史 1」與「殖民與帝國 13」並存                                                      |
| /technology/ | 54     | 20       | 12       | 出現名為「Technology」的子分類；「社群與數位文化 15」vs 一堆單篇                           |
| /art/        | 42     | 16       | 9        | 「文學 10」vs「文學作品 1」、「聲音藝術」vs「聲音與新媒體藝術」、英文值 `digital-art`      |
| /en/history/ | 50     | 17       | 10       | **中英文小節標題混排**（en 翻譯檔沿用 zh subcategory，少數被翻成英文自成一組）＋「其他 6」 |

單篇小節各佔一個完整 h3 標題列，50 篇文章被切成 13–20 個視覺段落，掃讀成本高於一條連續列表。排序用 `localeCompare` 字典序，跟策展意圖無關。

- **排序邏輯單一且寫死**。featured → 腳註數 → 標題，讀者無法切換（最新／閱讀時間的 JS 排序器寫好了但沒有 UI，見 §2.3）。
- **跨語言結構不一致**。subcategory 混語（上表）；Economy 圖表與 Food 視覺化 zh 限定是合理的策展決定，但 en/ja/ko/es/fr 讀者看到的 hub 沒有任何補位內容。

### 2.3 UI/UX

- **死碼功能**（模板內確認）：`.sort-btn` 與 `.tag-btn` 的事件監聽、`uniqueTags` 計算（前 12 個 tag）都在，但 markup 沒有渲染任何排序按鈕或標籤按鈕。功能被砍時只砍了 UI，邏輯留在原地。
- **搜尋只比對 title**。`applyFilters()` 只查 `data-title`，描述與 tags 都不在搜尋範圍；沒有結果數回饋（僅全空時出現 noResults 區塊）。
- **mobile 資訊密度失衡**。row 描述整行隱藏（只剩標題＋分鐘數）、分類描述隱藏、跨分類 nav 隱藏；但 hook 文字牆完整保留。刪掉的是導航資訊，留下的是閱讀負擔。
- **a11y**：列標題用 `<h3>` 包在 `<a>` 內、小節也是 `<h3>`，標題層級語意混亂；filter input 無 label 無 aria；結果數變化無 live region。（詳細清單見 §2.5 agent 審計）
- **小 bug**：模板內 `categoryKeys` 寫死 12 個分類、漏了 `politics`（static-paths 有 13 個），導讀 markdown 內指向 `/politics` 的連結拿不到 topic-pill 樣式。`topPicks` 計算回傳 5 筆、UI 只切前 3。

### 2.4 實用度

- **時間感完全缺席**。整頁沒有任何日期：不知道哪篇是新的、哪篇剛更新、這個分類還活著嗎。`content-dates.json` 有全部答案（git 實際 ship 時間），/latest 與首頁都在用，hub 沒用。
- **精選的可信度沒有外顯**。★ 與腳註數（「N 引用」）是品質訊號，但沒有任何說明（讀者不知道引用數代表什麼）；「精選」的挑選邏輯（featured ＋腳註門檻＋子分類多樣化）做得不錯，呈現卻是最弱的文字 chip。
- **SEO / AI 可讀性**：hub 頁沒有 CollectionPage / ItemList / BreadcrumbList 結構化資料（21.7% 流量是 AI crawler、LLM citability 是明確 LONGING），麵包屑只是視覺元素。
- **跨分類探索**：sidebar「其他主題」desktop 有、mobile 整段隱藏；頁尾沒有任何「下一個分類」動線。
- analytics 佐證：見 §2.6 資料盤點（hub 頁流量與 engagement 實測數字）。

### 2.5 Codebase 深度審計（Sonnet agent A，全部 file:line 佐證＋live DOM 驗證）

五個嫌疑全數確認（sort/tag 死碼、image 欄位零渲染、hook 重複、`categoryKeys` 漏 politics、硬編 hex），另外挖出嫌疑清單之外的更大問題：

- **Food 視覺化 100% 壞掉**：模板第 1644–2238 行呼叫 `d3.*` 但整個 repo 沒有任何地方載入 d3 到這個頁面（六個 sibling template 都有自己的 `<script src>` 載入，唯獨 hub 沒有）。live 驗證 `/food`：`window.d3 === undefined`、兩個圖表容器 0 子節點；「🍜 探索台灣美食宇宙」的標題、tabs、圖例都渲染了，圖表本體永遠空白。594 行死腳本照發到全部 78 個 hub 頁（13 分類 × 6 語）。
- **去重機制寫了沒接**：`hubFull` 變數就是為了「essay 去掉 hook」而生（206–230 行），但它從未被 render 使用，essay 一直吃未裁切的 `hubHtml`。設計意圖存在，執行斷線。
- **每頁夾帶 ~936 行 inline script**：economy 圖表（183 行）與 food 視覺化（594 行）沒有條件式 emit，78 頁全下載、77 頁只跑到 guard 就閒置。
- **「min」單位硬編英文**：第 484 行 `{readingTime} min` 六語全部顯示英文單位（live 驗證 zh 頁面顯示「45 min」），跟空狀態硬編中文「參與貢獻」剛好是同一種病的兩個方向。
- **~150 行孤兒 CSS**：`.articles-layout / .sidebar-* / .subcategory-heading` 等選擇器對應的 markup 早已不存在。
- **Dark mode 結論修正**：主體 chrome 靠 `dark-polish.css` 的 attribute-selector patch 層（359–513 行專門對 hub）撐住＝可用；但 food 視覺化與 economy 圖表的樣式寫在 scoped `<style>` 類選擇器裡，patch 層構造上打不到；dark mode 下是黑頁中央一塊亮奶油色的「light island」（live 截圖確認）。SVG 的 `setAttribute('fill', hex)` 更是任何 CSS 都救不了。
- **a11y live 驗證**：filter input 無 accessible name、`#noResults` 無 live region、麵包屑無 `aria-label`／`<ol>` 語意、h3（子分類）出現在任何 h2 之前（階層跳級）、hub 互動元素零 `focus-visible` 樣式（sibling 元件 TopicCard 有既定慣例）。
- **SEO 結構化資料**：SEO.astro 對首頁已有現成 CollectionPage + ItemList 實作（288–354 行），分類頁被 gate 在外；hub 的 BreadcrumbList 掉進通用分支（比對 slug vs 本地化名稱永不成立）；`/en/people` hub 因 `category === 'People'` 字串判斷誤發 `Person` 結構化資料；文章頁 BreadcrumbList 烤進 `https://taiwan.md/歷史` 這種不存在的 URL（同根因，本地化名稱當 slug 用）。
- **重用結論**：`ArticleCard.astro`（/latest、/explore、文章頁 related 共用）遷移成本 **0 個新 prop**；hub 是全站唯一還在手刻文章列的主要清單面。`categoryKeys` 漏 politics 的同款 bug 在 `article.template.astro` 已被修過（commit `0ef6c6256`），CategoryGrid 與 TopicCard 還有兩份未同步的複本。

### 2.6 內容資料盤點（Sonnet agent B，實跑腳本數字）

**欄位覆蓋率（zh-TW，n=834）**：`date / subcategory / description / tags` 全部 **100%**；`readingTime` 75.3%；`featured` 21.3%（13 個分類每個都有，最少 Politics 1/11）；`image` 只有 **21.5%**（History 8%、Politics 0%）。腳註分布：0 註 20.3%／1-4 註 2.0%／5-14 註 38.8%／15+ 註 38.8%——足以支撐三檔深度分級。

**Subcategory 是自由文字，不是受控詞彙**。全站 100% 有值，但破碎程度分兩個世界：Politics（top-3 覆蓋 91%）、Economy（79%）、Lifestyle（77%）可直接當導航；People（37 個值／235 篇，top-3 只覆蓋 30%）、Society（34%）、Culture（36%）等於沒分群。具體病灶：Geography 的「歷史街區」被寫成 8 種帶行政區後綴的變體值；4 個分類出現「分類名當子分類」的漏值（`Culture`、`Technology`、`Economy`×2、`Society`×3）；混入英文值 `digital-art`、`LocalSpecialty`、`Internet`。

**Hub 導讀存量**：zh-TW 13/13（2,830–6,682 字）；en/es/ko 各 12/13（同缺 Politics）；**ja 0/13**（日文讀者看到的 hub 完全沒有導讀）；fr 3/13。en 版導讀 9k–18k 字元、比 zh 長 3 倍（翻譯膨脹）——這是 §2.1 en hook 切出 1,885 字的上游原因。另外 `knowledge/People/_People Hub.md` frontmatter 壞掉（`## title:` 非法 YAML＋`---` 分隔線錯位），機器讀不到它的 metadata。

**時間資料**：frontmatter `date` 100%；`content-dates.json`（git 實質變更時間，已排除 babel／格式化等 cosmetic commit）zh 覆蓋 98.4%、六語合計 83.2%，翻譯頁繼承 zh 日期。兩者疊加等於全覆蓋——hub 目前一個都沒用。

**Tags 長尾退化**：3,851 個相異 tag，**79% 只用過一次**，≥5 次的只有 152 個。生 tag 直接做篩選 UI 會是噪音牆——死碼該刪，不該接。

**Analytics 現實**（GA 28 天 top-20）：13 個 hub 路徑只有 `/history/` 上榜——421 views／318 users，低於第 8 名的單篇文章（首頁同期 7,137 views）。其餘 12 個 hub 連 top-20 門檻都過不了。**hub 目前是過道，不是目的地**。這個數字既是問題（第二大門面沒人停留）也是設計約束（到訪者主要是導航意圖，改版不能拿 5,000px 的導讀擋在列表前面）。

## 三、外部參照與最佳實務（Sonnet agent C，附來源）

**三個參照站的 hub 解剖**（實抓頁面）：

- **Our World in Data**（topic page）：敘事在前——5 個「Key Insights」短區塊（每塊＝論點＋內嵌圖表）開場，策展卡片其次，最底才是 75+ 條的密集純連結清單。**密度隨捲動遞增**，跟 Taiwan.md 現況（列表在前、導讀全文墊底）剛好相反。
- **Wikipedia Portal:Taiwan**：策展與瀏覽在結構上分離——精選文章／傳記／圖片各一件、給足視覺重量；完整分類樹壓到最底、小字密排、不與策展區搶注意力。
- **Smashing Magazine category**：零策展的反面教材（純時序 archive），但它的每列 metadata 密度（日期＋閱讀時間＋則數）與明確總數標示值得單獨借。

**對 Taiwan.md 直接命中的 pattern**（來源見 agent 原文，摘關鍵）：

1. 列表用 row 不用卡片格（image 覆蓋 21.5%，全圖卡是陷阱）——NN/g cards 研究
2. filter input 要真 label（placeholder-only 是 WCAG 3.3.2/4.1.2 缺口）＋ `role="status"` aria-live 結果數——Deque / Scott O'Hara
3. 列表要 `<ul>/<li>` 語意（現在是裸 div，AT 報不出「N 項清單」）——W3C APG
4. 不做 infinite scroll；超過 40-60 項要有斷點或 landmark（我們的子分類分組＋sticky sidebar 可充當）——NN/g
5. mobile 次要導航用 accordion 收合，不要 `display:none` 整段蒸發——NN/g mobile accordions
6. 結構化資料：`CollectionPage` + `ItemList` + `BreadcrumbList`（與可見麵包屑完全一致）；`dateModified` 是 AI 答案引擎權重最高的 freshness 訊號（<13 週內容在 AI 引用中超額出現 ~3.2x）——Google docs / salespeak 研究
7. 腳註數是三個參照站都沒有的差異化訊號，值得升級成 schema.org `citation` 結構化資料（文章頁 follow-up，hub 先把徽章分級做好）
8. llms.txt「不傷也不幫」（Google 2026-06 官方說法；97% 部署零抓取）——不列入本案預算
9. 導讀長度跟著策展走，不要為 SEO 湊 2,000 字——與「策展式非百科式」同向
10. 排序切換、tag 篩選若上，走 Baymard 的 chip + 截斷模式；本站生 tag 分布（79% 單次）不支撐 tag 篩選 → 刪死碼

## 四、改良提案

設計主軸一句話：**策展壓縮成首屏的「起點書架」，索引拿回中段的密度與秩序，導讀在底部得到一個值得讀完的家**。OWID 的「敘事在前」照搬會跟 analytics 揭示的導航意圖打架，所以策展在首屏以「1 段 hook ＋ 3 張精選卡」的壓縮形態出現，全文導讀留在列表後（Wikipedia Portal 的分離原則），用 sidebar 錨點與閱讀時間標示讓它可發現、可規劃。

### P0 — 結構與正確性（本次全做）

| #     | 問題                                                                           | 改法                                                                                                                                                                     |
| ----- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P0-1  | hook 用「數 3 個 `</p>`」切，en 版切出 1,885 字                                | 改「第 1 段、500 字元上限內至多 2 段」；mobile 首屏讓出導航空間                                                                                                          |
| P0-2  | 導讀全文重複 hook 且埋在 5,500px 處不可發現                                    | sidebar 加「📖 策展導讀」錨點；essay 區塊加閱讀時間標示；接受首段 lede 重現（editorial 慣例），移除區塊內多餘分隔線                                                      |
| P0-3  | 子分類破碎：單篇小節氾濫＋字典序排列                                           | 分組搬進資料層：組依篇數降冪、單篇子分類合併進「其他」尾組（i18n key）；People 37 組 → 20 組                                                                             |
| P0-4  | 非 zh hub 小節標題中英混排                                                     | `src/data/subcategory-i18n.json` 顯示層對應（≥2 篇的值 × 5 語），未命中原樣顯示；分組仍以原值為 key                                                                      |
| P0-5  | 排序死碼／tag 死碼                                                             | tag 邏輯刪除；排序做成真 UI（精選／最新／引用／閱讀時間），組內重排                                                                                                      |
| P0-6  | 搜尋只比對 title、無結果數回饋、input 無 label                                 | 比對範圍加 description + tags + 子分類；`role="status"` aria-live「N / M 篇」；補 label 與清除鍵                                                                         |
| P0-7  | 零時間訊號                                                                     | 資料層 join `content-dates.json`（fallback frontmatter date）：列尾顯示更新年月、「最新」排序、header 顯示分類最後更新                                                   |
| P0-8  | 無結構化資料                                                                   | `CollectionPage`（含 dateModified）+ `ItemList` + `BreadcrumbList` JSON-LD，與可見麵包屑一致                                                                             |
| P0-9  | `categoryKeys` 漏 politics；topPicks 算 5 用 3                                 | 補 politics（含 CategoryGrid / TopicCard 兩份複本同步）；精選卡取 3、保留 5 供未來輪換                                                                                   |
| P0-10 | `_People Hub.md` frontmatter 壞（非法 YAML）                                   | 修復（knowledge/ 單檔 heal）                                                                                                                                             |
| P0-11 | 列表語意：裸 div ＋ `<a>` 包 `<h3>`；h3 出現在任何 h2 之前                     | 列表改 `<ul>/<li>` ＋ ArticleCard；子分類組升 `<h2>`；ArticleCard 加 `titleTag` prop（預設 h4 不影響既有頁）hub 傳 h3——階層成為 h1→h2→h3                                 |
| P0-12 | Food d3 視覺化 100% 壞掉＋78 頁夾帶 936 行 inline script                       | 抽成 `FoodViz.astro` / `EconCharts.astro` 條件渲染元件（script 只在對應頁載）；FoodViz 比照 sibling template 載入 d3，圖表復活                                           |
| P0-13 | 「min」單位硬編英文六語照發                                                    | readingTime 顯示字串走 i18n（呼叫端格式化，符合 ArticleCard 介面約定）                                                                                                   |
| P0-14 | hub 無 CollectionPage；/en/people 誤發 Person；BreadcrumbList 分類分支永不命中 | SEO.astro 加選用 `categorySlug` + `collectionItems` props（hub 傳入）：正確 BreadcrumbList ＋ CollectionPage/ItemList（含 dateModified）；Person 判斷收斂到 article type |

### P1 — 視覺與實用度（本次全做）

| #    | 問題                                                    | 改法                                                                                                                                                                                                                                            |
| ---- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1-1 | 精選只是文字 chip、image 資料閒置；列表手刻與全站不一致 | 精選＝3 張 `ArticleCard density="detailed"`（原生支援 coverImage ＋無圖 drop-cap fallback，2026-07-06 design audit 產物）；列表列＝`ArticleCard density="row"`（0 新 prop 遷移＋row 變體補 footnotes/readingTime 顯示），同步刪 ~150 行孤兒 CSS |
| P1-2 | 「N 引用」裸數字無語境                                  | 深度分級徽章：15+ 深度考證／5-14 有出處／其餘不標，tooltip 說明；顏色走分類色系                                                                                                                                                                 |
| P1-3 | 模板硬編 hex 幾十處、靠 dark-polish override 層撐       | hub 區塊改用 `--color-ink/-ink-soft/-border/-surface/-bg-soft` tokens，dark mode 原生成立                                                                                                                                                       |
| P1-4 | mobile 首屏零導航＋跨分類 nav 蒸發                      | hook clamp；子分類 chips 上移；跨分類 nav 以 accordion 收在列表後；分類描述 mobile 顯示一行                                                                                                                                                     |
| P1-5 | essay 白卡與全站紙感語言脫節                            | 卡面改 `--color-surface`＋`--color-border`，標題排版對齊文章頁 `--font-editorial` 語言                                                                                                                                                          |
| P1-6 | 空分類 CTA 硬編中文「參與貢獻」                         | 走 i18n key                                                                                                                                                                                                                                     |

### P2 — 界外／後續（不在本次 scope，見 §七）

People 235 列的 load-more、per-category RSS、tag 篩選（需先做 tag 治理）、subcategory 資料清理（>50 檔）、ja 13 篇＋fr 10 篇＋Politics 3 語 hub 導讀補寫、文章頁 `citation` JSON-LD、llms.txt。

## 五、實作計畫

執行模式：Fable 規劃＋驗證，Sonnet 5 subagent 執行；worktree `20260710-hub-template` 內作業，模板檔任務嚴格序列（同檔避撞），資料層／i18n 檔平行。

| Wave      | 任務            | 檔案範圍                                          | 內容                                                                                                                                                                                           |
| --------- | --------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1（平行） | T1 資料層       | `category-static-paths.ts`                        | join content-dates、分組／排序／單篇合併搬進資料層、分類 lastUpdated、essay 字數→閱讀分鐘、修 `_People Hub.md`                                                                                 |
| 1（平行） | T2 i18n         | `src/i18n/*` 6 語                                 | 新 key（others/sort×4/resultCount/updated/essayNav/essayReadTime/searchLabel/depth 徽章/contribute）                                                                                           |
| 1（平行） | T3 子分類對應   | `src/data/subcategory-i18n.json`（新）            | ≥2 篇子分類值 × 5 語顯示對應（主 session 逐條抽驗）                                                                                                                                            |
| 2（序列） | T4a 列表區      | 模板（列表段）＋ ArticleCard                      | 列表遷移 `ArticleCard density="row"`（row 變體補 footnotes/readingTime、加 titleTag prop）、ul/li 語意、排序 bar、搜尋範圍＋aria-live、分組渲染改吃 groups props、tag 死碼＋孤兒 CSS 刪除      |
| 2（序列） | T4b 首尾區      | 模板（header/essay 段）＋ SEO.astro ＋ Layout     | hook 新切法＋essay 去重（接上 hubFull）、精選卡（detailed×3）、header 日期、essay 錨點＋閱讀時間＋卡面、mobile accordion、CollectionPage/ItemList/BreadcrumbList、politics 修正、min 單位 i18n |
| 3（序列） | T5a script 抽離 | FoodViz.astro / EconCharts.astro（新）            | 條件渲染元件化＋d3 載入修復（比照 dashboard.template 模式）                                                                                                                                    |
| 3（序列） | T5b token 化    | 模板 `<style>` ＋ class ＋ CategoryGrid/TopicCard | 硬編 hex → tokens、focus-visible 樣式、politics 複本同步、空狀態 heading token                                                                                                                 |
| 驗證      | Fable           | —                                                 | 每 wave 之間：`astro check`＋dev 冒煙；收尾：worktree 全站 build＋六語 × 明暗 × 三尺寸截圖矩陣（REFLEXES #19）＋前後對照                                                                       |

## 六、實作結果

同 session 完成（2026-07-10 23:08 → 2026-07-11 凌晨），五個 Sonnet 執行 agent 序列＋平行完成 14 項 P0 與 6 項 P1，Fable 主 session 逐項驗收（每個 agent 的 side-effect / self-quality claim 都經 grep、curl、DOM probe 或截圖重驗，per REFLEXES #31）。

### 6.1 改動清單

| 檔案                                                    | 變化                                                                                                                                                    |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src/templates/category-hub.template.astro`             | 2,298 → ~1,620 行：列表遷移 ArticleCard、hook 演算法重寫＋essay 去重、精選書架、排序 bar、aria、JSON-LD props、token 化、兩個 script 島抽離             |
| `src/utils/category-static-paths.ts`                    | +199 行：`updated`（content-dates join + frontmatter fallback）、`groups`（伺服端分組＋單篇合併）、`categoryUpdated`、`essayMinutes`                    |
| `src/components/ArticleCard.astro`                      | +96 行：`titleTag` prop（heading 階層修正）、row 變體 footnotes/readingTime meta cluster                                                                |
| `src/components/FoodViz.astro`（新）                    | 781 行：食物視覺化抽離＋**補上缺失的 d3 loader——這個功能自誕生以來首次真的渲染**（sunburst 實測 35 個扇區路徑，先前永遠 0）                             |
| `src/components/EconCharts.astro`（新）                 | 309 行：經濟圖表 script 抽離（props 傳資料），77/78 個 hub 頁不再下載無用腳本                                                                           |
| `src/components/SEO.astro`                              | CollectionPage/ItemList 選用 props；BreadcrumbList 改用 categorySlug（同時治好文章頁 `taiwan.md/歷史` 假 URL）；Person 誤發修正（gate 到 article type） |
| `src/layouts/Layout.astro`                              | collectionItems/collectionTotal 通道                                                                                                                    |
| `src/i18n/ui.ts`                                        | +84 行：14 個新 key × 6 語                                                                                                                              |
| `src/data/subcategory-i18n.json`（新）                  | 103 條子分類 × 5 語顯示對應                                                                                                                             |
| `src/styles/dark-polish.css`                            | ArticleCard shared block 補 `.category-page` scope；死規則清除；sort-btn active dark 配色                                                               |
| `src/components/CategoryGrid.astro` / `TopicCard.astro` | politics 複本同步（CategoryGrid 順帶修好 politics 文章數顯示 0 的沉默 bug）                                                                             |
| `knowledge/People/_People Hub.md`                       | frontmatter heal（非法 YAML → 可機讀）                                                                                                                  |

### 6.2 驗證證據（dev server 實測）

- **導讀去重**：hook 開場句「一九八七年七月十五日」全頁出現次數 2 → **1**；essay 區塊從第 3 段接續。en hook 從 1,885 字元／3 段 → **1 段**（演算法：首段、<200 字補第 2 段、600 字硬帽）。
- **分組**：/history/ 13 組（7 單篇）→ **9 組**；/en/history/ 中英混排標題 → 英文顯示名（103 條對應表）＋「Others」尾組。排序改篇數降冪。
- **互動**：排序切換實測（「最新」讓 2026-06-25 更新的蓬萊米浮到組內第一）；搜尋「戒嚴」→「8 / 50 篇」aria-live 回報＋清除鍵；搜尋範圍含 description/tags/子分類。
- **結構化資料**：/history/ 五塊 JSON-LD（WebSite×2＋Organization＋**CollectionPage**（50 items＋dateModified）＋**BreadcrumbList**）；/en/people/ 不再誤發 Person；文章頁 Person 保留。
- **Dark mode**：卡片標題 computed rgb(26,60,52)（不可讀）→ **rgb(241,245,249)**；sort active 改 color-mix 分類色淡底＋ink 字。
- **d3 復活**：`window.d3 === object`、sunburst 35 paths（修復前 `undefined`／0）。
- **Heading 階層**：h1 → h2（精選／子分類組／導讀）→ h3（卡片標題，titleTag prop）——跳級消除。
- **Mobile**：hook 文字牆 ~2.5 屏 → ~1.5 屏；分類描述一行顯示；跨分類 nav 從 `display:none` 改 accordion 收合。
- **ja（無導讀語系）**：hook／essay／sidebar 錨點全部優雅缺席，列表功能完整。

### 6.3 全站 build 與收尾驗證

- **`npm run build` 全站通過**（5,000+ 頁），broken-link gate PASS：0.39%，與改版前 baseline 完全一致（maintainer routine 長期記錄值），本次零新增斷鏈。
- **Production preview（`astro preview` 對 dist）HTTP 矩陣**：zh／en／ja／ko／es／fr × history／technology／food／economy／politics 抽測 10 組全部 200。
- **多語分組上線實證**：`/en/history/` 小節標題全英文（Colonialism & Empire／Postwar & Authoritarian Era／…／Others）；`/ja/technology/` 全日文（半導体とハードウェア／その他）——§2.2 的中英混排在 production 產物根治。
- **JSON-LD in production**：`/ko/technology/` 五塊齊（含 CollectionPage＋BreadcrumbList）。
- **Script 島隔離**：`/history/` 產物 0 處 foodData／chartConfigs；`/food/` 帶 d3 loader。
- **量測註腳（誠實記錄）**：dark mode 的 production 端 computed-style 驗證卡在瀏覽器 pane 的 frozen-renderer 假象（隱藏分頁凍結後所有讀值停在 light-mode 快取，連 inline `!important` 都讀不回來——物理不可能的結果證明量測層壞掉，截圖 CDP 也 timeout）。Dark 修復的成立依據：(1) 原始碼規則正確（`.category-page` 已入 shared ArticleCard dark block）；(2) built CSS bundle 內含同一條未分層規則、specificity 高於元件規則且順序在後；(3) T5b 在可見分頁的 dev 實測 computed rgb(241,245,249)。cascade 是決定性系統，三者成立即結論成立；上線後多看一眼 production dark 仍寫進 §七 後續。

### 6.4 執行模式復盤（cost-split orchestration）

Fable 主 session 只做規劃、規格、驗收與驗證（含三次抓到 agent 環境層問題：node_modules 實體化毀 build、dev server 被 build 撞死、frozen-renderer 量測假象）；八個 Sonnet agent（3 研究＋5 實作）承擔全部 read-heavy 與 write-heavy 工作。每個 agent 範圍鎖死在明確檔案清單＋可驗收輸出，模板檔任務嚴格序列避撞。實測有效：五個實作 agent 的 self-report 全部經主 session 重驗後才放行，其中兩個 agent 的偏差（npm install 副作用、min 單位）都在驗收層被接住。

## 七、界外事項與後續

- **subcategory 資料清理**：taxonomy 破碎的根治在 `knowledge/` frontmatter（合併同義子分類、翻譯 en/ja/ko/es/fr 的 subcategory 值）。涉及檔案數 >50，命中 MANIFESTO §自主權邊界，本次不動資料、模板做防禦性處理；清理案另立提案等哲宇拍板。

---

_v0.1 draft | 2026-07-10 23:2x +0800 | Fable 主 session 第一手審計部分先落檔，agent 產出回填中_
