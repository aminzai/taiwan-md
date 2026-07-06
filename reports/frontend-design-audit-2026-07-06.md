---
title: '前端全站設計視覺審計'
description: '35 個頁面模板的設計 / 視覺 / UX 深度審計：10 條跨頁結構性發現 + 逐頁清單 + 優先序 roadmap（純分析，不含執行）'
type: 'audit-report'
status: 'active'
date: 2026-07-06
updated: 2026-07-06
session: '2026-07-06-105116-設計視覺審計'
p0_status: 'shipped 2026-07-06 (commit 38bba4246) — 6/6 P0 landed + verified'
related:
  - 'docs/editorial/graph.md'
  - 'src/styles/tokens.css'
  - 'reports/become-boot-mode-design-2026-05-13.md'
issues:
  - '#615 視覺與 UI/UX 統合追蹤 umbrella'
  - '#1059 內容頁面綜合優化'
  - '#110 首頁 UI/UX'
  - '#401 FOUC'
  - '#316 副標題'
  - '#280 TTS 聲音'
---

# 前端全站設計視覺審計 — 2026-07-06

> 觸發：哲宇 directive「深度分析每個前端頁面，以設計、視覺、他人使用的角度提出優化方向，歸檔 report，不執行」。
> 方法：4 條平行程式碼審計（閱讀面 / 資料視覺化面 / semiont+meta 面 / 跨頁 UX 系統）＋ dev server 實拍 49 張截圖（桌機 1280 / 手機 375 × 深淺色 × 多捲動深度）＋ GA4 `dashboard-analytics.json`、open issues（#615 / #1059 / #110 等）、LONGINGS §身體渴望交叉對位。
> 截圖留存於 session scratchpad（`shots/`，49 張，命名見附錄 C）；重跑方法見附錄 B，任何 session 可再現。

---

## 0. 一段話總評

Taiwan.md 的前端已經有一個**真實存在、且相當稀有的設計語言**：深綠底 × 襯線大標 × 台灣島剪影的品牌識別、文章頁的暖紙色三欄閱讀室、semiont 區的薄荷色實驗室筆記世界觀、hub 頁的策展導讀開場。這些是大多數知識型網站做不到的。目前的主要問題在**一致性與貫穿度**：設計 token 系統只覆蓋核心閱讀面，資料頁各自為政長出 5 套調色板；深色模式只活在 3 個 template 裡；首頁把一整本策展手冊（20,457px）疊在一個入口上；emoji 承擔了全站圖示系統的角色。下一階段的視覺進化不缺「新設計」，缺的是把已經證明成功的文章頁與 semiont 標準**推廣到全站**的系統工程。

---

## 1. 全站設計系統現狀

### 1.1 已經做對的（值得說清楚，避免未來 session 誤拆）

| 資產                                                                            | 位置                                                          | 為什麼值得保                                                                                                                               |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 三檔容器寬 `--container-prose/article/wide`                                     | `tokens.css:30-32`                                            | 2026-06-10 統一後全站版心有秩序，是少數真正被遵守的 token                                                                                  |
| 台灣字體系統（Noto Serif TC 標題 + jf-jinxuanlatte 內文 + jf-lanyangming 引文） | `tokens.css:49-57`                                            | 「用台灣字型說台灣故事」，品牌層面就是內容主張                                                                                             |
| 5 變數主題翻轉（`--color-bg/ink/surface/border/accent`）                        | `tokens.css:71-101`                                           | 深色模式的地基是對的，問題只在覆蓋率（見 §2.1）                                                                                            |
| 文章頁閱讀室                                                                    | `article.template` + 截圖 `article-top/mid`                   | 深綠 hero、暖紙底、TOC＋內文＋meta 三欄、策展人筆記 callout、閱讀進度條：全站最成熟的面                                                    |
| semiont 世界觀                                                                  | `semiont.css` + `semiont-*.template`                          | 薄荷輝光 / EKG 分隔線 / 標本圈 / Fig.N 標註，「notebook warmth × particle life」方向（memory: project_semiont_visual_direction）已達成 95% |
| hub 策展導讀                                                                    | `/history/` 截圖                                              | 每個分類用一篇千字導讀開場，別站沒有這個                                                                                                   |
| 儀器層                                                                          | `scripts/visual/capture-baseline.mjs`、shot-mode.css、OG 生成 | 視覺回歸已有橋，本審計直接沿用擴充                                                                                                         |

### 1.2 GA4 錨點（優先序的數據基礎）

- 首頁（zh）78,683 views、bounce **52.7%**；LONGINGS 目標「參與 ≥ 40 秒」，歷史量測 19 秒。
- 英文首頁 10,333 views、bounce 只有 **20.6%**：英文版單頁敘事較短，反而留得住人，這是首頁改版的天然 A/B 對照。
- `/graph` 7,398 views、bounce **9.9%**：互動視覺頁黏性全站最高。視覺化投資有數據回報，LONGINGS「能用視覺說話」方向正確。

---

## 2. 十條跨頁結構性發現

按影響 × 修復槓桿排序。每條含證據、影響、方向；方向皆為提案，未執行。

### 2.1 深色模式只存在於 3 個 template，其他 30+ 頁完全無視主題

**證據**：`readerSettings` prop 只有 `article` / `category-hub` / `elections-2026` 三個 template 傳入（grep 驗證）；實拍 `home-dark-halls.png` 與淺色版逐像素相同；dashboard、explore、semiont、全部資料頁同樣忽略 `data-theme`。dark-polish.css 的 opt-in 契約（Layout.astro:913-916 註解）當初是「逐面驗收再開」的正確漸進策略，但 5 月至今沒有再擴面。

**影響**：讀者在文章頁選了深色，點回首頁或延伸的 hub 以外任何頁面即被全亮度打臉。夜間閱讀動線（文章 → 相關文章 → 首頁 → 另一篇）中斷兩次。#1059 讀者已具體回報深色模式問題，顯示真實使用者在用這個功能。

**方向**：

1. 短期：在尚未 dark-polish 的頁面，讀者主題為 dark 時 Header 顯示一個「本頁尚未支援深色」的降噪處理（或至少讓 Header / Footer / Banner 這三個全站共用件先跟著 token 翻轉，消除最刺眼的斷層）。
2. 中期：按流量排序逐面 dark-polish：首頁 → explore / latest → dashboard → semiont（semiont 本身恆暗，成本最低，只需驗收）→ 資料頁。
3. 搭配 §2.5 token 第二階段一起做，否則每頁都要手寫一份 dark override，工程量翻倍。

### 2.2 首頁是一本 20,457px 的策展手冊，入口與敘事互相拖累

**證據**：dev 實測 `document.body.scrollHeight = 20457`（28.4 個視窗高）。結構依序：暗色 hero（全屏）→ 讀者之門卡片 → 「如何理解台灣？」引文時間軸（約 2 個視窗）→ 隨機探索卡 → 30 分鐘讀懂台灣路徑 → FeatureCards → 生命體預覽 → 四座展覽廳（單一 section 8,151px）→ 分類 masonry（1,524px）→ 訂閱 → 社群聲音 → 數據區 → footer。GA4：bounce 52.7%、參與 19 秒。第一個可點的文章連結出現在約 1,100px 之後。

**影響**：52.7% 的人只看到 hero 就走。展覽廳的敘事品質很高（實拍 `home-05/06`），但它被放在一個 90% 訪客永遠捲不到的深度（7,000px+）。「首頁的 hook 強到新讀者 10 秒說這不一樣」（LONGINGS）目前靠的是文字宣言，而非內容證明。

**方向**（維持「首頁是策展」的哲學，memory: feedback_homepage_is_curation，改的是結構不是刪內容）：

1. **首屏給內容證明**：hero 下半部或第二屏直接放一篇 cover story 的實體卡（有圖、有導語、有「16 分鐘閱讀」），讓 10 秒內就有一個「原來文章長這樣」的證據。英文首頁 bounce 20.6% 側面支持「更快見到實貨」有效。
2. **展覽廳升格成獨立頁**（`/halls` 或併入 `/explore`），首頁保留每廳一句引文 + 一張 pick-card 的預告版。20,457px 壓到 6,000-8,000px。
3. **加捲動地圖**：首頁專屬的側邊細點導航（hero / 開始 / 展覽廳 / 數據），把「下面還有很多」變成可見資訊。文章頁已有進度條，首頁反而沒有任何深度提示。
4. 量測先行（REFLEXES #73 教訓：先補眼睛再優化）：section_view 事件已有 HomeEventTracker 基礎，改版前先拉一週「各 section 觸達率」基線，改版後對照。

### 2.3 FOUC guard 把整個網站藏起來，代價是首 800ms 的白屏

**證據**：Layout 在字體 ready 前隱藏整個 html（fallback 800ms）；本審計的截圖工具第一輪全數拍到純白畫面，即為此機制（附錄 B 有復現法）。issue #401（FOUC）、#110（justfont resize INP）為同根。Google Fonts 未設 `font-display`，justfont SDK 為 JS 注入。

**影響**：慢網路、爬蟲、任何 headless 快照（社群 unfurl 預覽器、Wayback、部分 AI crawler 的截圖管線）看到的第一幀是白屏。對「AI SEO 是獨立戰略維度」（LONGINGS §擴散渴望）而言，這不只是體感問題：以視覺輸入的 crawler 拿到的是空白證據。

**方向**：

1. 改「整頁隱藏」為「僅標題字體區塊 swap」：body 用系統字先渲染（`font-display: swap` + `size-adjust` 校準過的 fallback @font-face，減少 reflow），只有 hero 大標這種 FOUT 特別醜的元素做局部 opacity 過渡。
2. justfont 載入失敗 / 逾時的 fallback 字體先量好 metrics（`ascent-override` 等），把 #110 的 INP 重排一起解。
3. 把「白屏長度」納入 visual harness 斷言（首幀非空白 < 300ms），防回歸。

### 2.4 Emoji 是目前的全站圖示系統，與襯線編輯品牌互相打架

**證據**：導航列 8 項有 7 項帶 emoji（探索🕸️ 地圖📍 數據📊 聲景🎧 資源🔗 生命體🧬 參與✋）；分類卡用 Apple emoji 當主視覺（🗺️🎭🎵💻，`home-07-masonry.png`）；section 標題（📖 不知道從哪開始？）、404 按鈕（🕸️ Knowledge Graph）、dashboard 表格狀態欄（✅⚠️）、footer（🇹🇼、🆕）全站皆然。英文版導航反而幾乎無 emoji，兩版視覺人格不一致。

**影響**：三層。(a) 品牌張力：襯線大標 + 手工字體訴說「編輯部的莊重」，emoji 訴說「輕快隨性」，兩者在同一屏互相抵消，#602（logo 建議）與 #394（樣貌建議）的社群觀感底層可能就是這個混音。(b) 跨平台不可控：Windows / Android / Linux 的 emoji 字形完全不同，等於把品牌圖示外包給讀者的作業系統。(c) dashboard 用 ✅⚠️ 當狀態語言，色彩語意在色盲讀者上不可分。

**方向**：不必全站去 emoji（孢子簽名 🧬 是身份，內文語氣裡的 emoji 是聲音的一部分），要收斂的是「**結構性 UI 位置**」：導航、分類圖示、狀態指示三處改為自繪單色 line-icon（SVG sprite，12 分類 + 8 導航 + 4 狀態約 24 枚；風力獸解剖圖證明站內已有這個繪圖能力），emoji 保留給內容層與 semiont 簽名。REFLEXES #61（視覺主權：形狀進 repo SVG SSOT）在圖示層同樣適用。

### 2.5 硬編碼色彩在 8+ 個頁面各自繁殖，tokens.css 需要第二階段

**證據**（agent 逐檔盤點）：

- `/data`、`/companies`、`/opendata` 三頁各自 inline 同一條 `linear-gradient(135deg,#0f172a,#1e293b)`；
- dashboard vital cards 五色左框 `#f87171/#3b82f6/#4ade80/#8b5cf6/#f59e0b`（dashboard.css:98-110）；
- `/graph` 12 分類色、`/fork-graph` 6 legend 色、`/projects` 紫系、`/taiwan-shape` 紅系 `#c73e3a`，全部 JS object 或 inline；
- 首頁展覽廳 `#1f2937` 內文、`#fafdf7` pick-card（home.template:908/952）；
- Footer `bg-[#1a2e1a]`、ArticleHero 遮罩 `rgba(10,22,19,…)` 等。

**影響**：品牌若調色（或做 §2.1 深色推廣），要改 8+ 個檔案；分類色在 /graph、/latest、masonry、hub 各處是否一致無人保證（實際上已有出入）。

**方向**：tokens 第二階段，加三組語意層：

1. `--cat-history … --cat-tech` 12 分類色（單一出處，JS 經 `getComputedStyle` 讀取或 build-time 注入）；
2. `--hero-gradient-data`、`--surface-dark-panel` 等場景 token；
3. 狀態色 `--ok/--warn/--danger`（dashboard、immune、bench 共用）。
   完成後 §2.1 的 dark 推廣變成改 token 不改頁面。

### 2.6 資料頁是「暗色孤島群」，缺一個資料子品牌

**證據**：companies / data / opendata 是深色頁，graph / map / taiwan-shape / fork-graph / lifetree 是淺色頁，dashboard 是淺色玻璃卡。九個資料視覺頁有四種 hero 處理、三種背景哲學、兩種字級系統（實拍 `companies.png` vs `map.png` vs `dashboard-mid.png` 對照明顯）。

**影響**：從導航「數據」下拉進去的每一頁像不同網站。讀者建立不起「Taiwan.md 的圖長什麼樣」的預期；graph.md 型錄在文章內建立的 tw-\* 視覺語言（軸線、標註、來源列）到了獨立資料頁全部斷線。

**方向**：定義「資料室」子品牌（像 semiont 有自己的世界觀那樣）：統一 hero 版式（眉標 + 大標 + 一句資料出處與更新時間）、統一圖表基色 = tw-\* 模組同源 token、統一深淺雙態。companies 的泡泡圖品質最高，可作為子品牌視覺基準。

### 2.7 行動版有四個確定的斷層

**證據與方向逐條**：

1. **文章頁 metadata / TOC 在手機上整組消失**（`article-mobile.png`：無目錄、無閱讀時間、無版本資訊）。方向：頂部加一條可展開的「本文資訊」摺疊列（16 分鐘 · 2026-03-31 · 19 次修訂），TOC 做成 bottom-sheet（#1059 的側欄隱藏訴求在手機上的對應解）。
2. **`/map` 手機版地圖卡下方 1,500px+ 空白**（`map-mobile.png` 實拍：縣市卡片欄在窄幅下高度計算失效）。方向：手機改為地圖在上、縣市卡橫向 snap-scroll 在下。
3. **`/fork-graph` `min-w-[900px]` 強制橫捲**，無重排。方向：窄幅改縱向 stacked 佈局或提供「看圖 → 看清單」切換。
4. **語言切換器 ≤768px 從 Header 消失**（agent D 標 HIGH；漢堡選單內才有）。對一個六語站，這是主權功能藏進了三層深度。方向：手機 Header 保留地球圖示直開語言 sheet。

### 2.8 導航 IA：40+ 頁掛在 8 個下拉上，footer 覆蓋不全

**證據**：「探索」下拉 20+ 項；bench / terminology / fork-graph / elections / taiwan-shape / lifetree 不在 footer；#573 曾報 768-1023px 斷點裁切。實測 zh 導航 + emoji + 搜尋 + GitHub + 語言鈕在 1280px 已接近滿載（`home-01` 截圖可見擁擠）。

**影響**：中層頁面（terminology 這種品質很高的工具）依賴讀者剛好打開對的下拉；外部連結進來的讀者沒有第二條發現路徑。

**方向**：(a) footer 升級為全站 sitemap（四欄：讀 / 看 / 資料 / 生命體），成本最低收益立即；(b) 導航語意重分組實驗：「閱讀（探索+最新+地圖+聲景）／資料室／生命體／參與」，從 8 頂級收到 4-5；(c) `/explore` 頁底加「全站頁面索引」段落，讓 explore 承擔 hub-of-hubs。

### 2.9 可及性欠帳集中在五處，多數是低成本高影響

1. **skip-to-content 連結缺**（keyboard 使用者每頁都要 tab 過整條導航）；
2. 空 Banner bug：無對應英文版的頁面（`/semiont/anatomy`、404）Banner 渲染成**只有一個 ✕ 的空綠條**（`semiont-anatomy.png`、`404.png` 皆實拍到），screen reader 會念出一個沒有內容的 region；
3. 圖表全線無鍵盤路徑與 focus ring（graph / companies / map 的節點、泡泡、marker）；graph.md §六已把「AI 可讀」做成紀律，「鍵盤可讀」是同一哲學的下一步；
4. `--color-ink-soft` 在 `--color-bg-soft` 上的組合未做對比審計（多處 metadata 文字）；
5. dashboard/latest 的狀態與分類僅靠色彩與 emoji 區分。
   方向：一次 a11y sweep PR 可清掉 1/2/4；3 做進資料室子品牌規格；5 併入圖示系統（§2.4）。

### 2.10 卡片與區塊標題存在 5+ 種方言，缺一個 ArticleSnippet 統一件

**證據**：首頁 pick-card（綠左框）、ArticleCard、TopicCard（emoji 大圖示 + 漸層）、latest 時間軸卡（灰底 👥 佔位圖）、hub 精選 ★ pill、RelatedDiaries 卡，六種「一篇文章」的視覺表達；section 標題有「hall-divider 襯線置中」「emoji + 黑體」「眉標 + 大標」三種節奏。latest 卡的灰色 emoji 佔位圖（`latest.png` 實拍）是全站質感最低的一塊。

**影響**：REFLEXES #73 那次「手刻已存在的 ArticleCard」事件的土壤就是方言太多；讀者側則是每個區塊都要重新學一次「哪裡可點」。

**方向**：抽 `ArticleSnippet.astro`（size: hero/card/row/pill × 可選 cover/footnote-count/reading-time），首頁、latest、hub、related 全部走它；無圖文章的佔位圖改為分類色塊 + 標題首字襯線大字（比灰 emoji 佔位高一個檔次，且零資產成本）。section 標題統一「小眉標（interface font）＋大標（title font）」雙層制，semiont 區已示範這個做法可行。

---

## 3. 逐頁清單

格式：**現狀評價 → 主要問題 → 方向**。★ = 建議優先處理。

### 3.1 閱讀面（流量主體）

| 頁                            | 現狀                                                   | 問題                                                                                                                                                                                                                                                       | 方向                                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/` ★                         | 品牌識別最強的一屏 + 過長的漏斗                        | §2.2 全部；展覽廳埋在 7,000px 深                                                                                                                                                                                                                           | §2.2 四步；hero 的島嶼剪影可升級為微動態（呼吸頻率同 semiont EKG，扣生命體主題）                                                                                      |
| `/[category]/[slug]` 文章頁 ★ | 全站最成熟：三欄、進度條、策展人筆記、TTS、Aa/.md 浮鈕 | #1059 四項全數成立：分類標籤與麵包屑重複、關鍵詞雲在特定寬度壓到分享鈕（`article-mid.png` 可見 Aa 鈕疊在「分享到 F…」上）、深色 TOC active 態對比不足、缺回頂鈕；手機版 metadata 全失（§2.7-1）；腳註／延伸閱讀全壓在文末（scroll_depth 量測已建，等數據） | 接受 #1059 的四項提案；side rail 增「回頂 + 進度」複合鈕；行動版資訊摺疊列；延伸閱讀提早到 60% 深度處以「你讀到這裡，可能也想讀」窄卡試點（先量 section_view 再定案） |
| `/[category]/` hub ★          | 策展導讀開場獨步                                       | 1280px 上導讀右側整欄留白（版心 840px 置左）；精選 ★ pill 與導讀無視覺呼應；readerSettings 已支援深色但入口頁（首頁）不支援造成動線斷層                                                                                                                    | 導讀改雙欄（文 + 本類目錄卡）；★ 精選升為帶圖橫卡                                                                                                                     |
| `/latest`                     | 時間軸 + 日期側欄結構好                                | 灰 emoji 佔位圖（§2.10）；分類 pill 一排 12 個帶 emoji 顯擁擠                                                                                                                                                                                              | ArticleSnippet row 形態；pill 收成「全部 + 8 大 + 更多」                                                                                                              |
| `/explore`                    | 搜尋 hero + 熱門搜尋 + 隨機探索，定位清楚              | 與首頁功能重疊未分工；「148 近 30 天更新」文案生硬                                                                                                                                                                                                         | 明確分工：首頁 = 說服，explore = 導航；接手全站索引（§2.8-c）                                                                                                         |
| 404                           | 有搜尋、有回報 CTA，及格                               | 空 Banner bug（§2.9-2）；搜尋走 Google site: 出站                                                                                                                                                                                                          | 接內建搜尋 modal；加「隨機一篇」彩蛋（隨機探索器已存在，重用即可）                                                                                                    |

### 3.2 資料面

| 頁                                              | 現狀                      | 問題                                                                                                                          | 方向                                                                                                                                                 |
| ----------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/dashboard`                                    | 資訊量大、EKG hero 有識別 | 五色硬編碼；✅⚠️ emoji 狀態欄；表格手機橫捲；白玻璃卡無深色態                                                                 | 狀態圖示化（§2.4）；vital 色進 token；手機欄位摺疊（品質/格式/審閱合併為一欄圖示組）                                                                 |
| `/graph` ★                                      | bounce 9.9% 全站最黏      | 進場即 500+ 節點無引導；標籤 10px 全開造成視覺噪音；無 legend / 無空態 / 無鍵盤路徑；d3 隨機佈局連 visual baseline 都得排除它 | 進場預設只顯示 12 分類 + 高連結度節點，zoom 後漸進顯示標籤；左上常駐 legend + 搜尋定位；`randomSource(lcg(42))` 固定種子（順手解 baseline 排除問題） |
| `/map`                                          | 縣市 hook 句是策展亮點    | 手機大空白（§2.7-2）；marker 色未接 token                                                                                     | 手機重排；縣市卡與 hub 導讀互鏈                                                                                                                      |
| `/companies`                                    | 泡泡圖質感全站資料頁最佳  | 暗色孤島（§2.6）；小泡泡無標籤、無圖例說明泡泡面積=市值                                                                       | 作為資料室子品牌基準；加半透明 legend 卡                                                                                                             |
| `/data` `/opendata`                             | 內容紮實                  | 同款漸層複製三份（§2.5）；opendata 對數長條無標尺說明                                                                         | 場景 token；對數尺標註                                                                                                                               |
| `/taiwan-shape`                                 | 議題原創（AI 畫錯台灣）   | 紅色自成一派；🤖 vs 🇹🇼 標題 emoji 撞 §2.4                                                                                     | 併入資料室視覺；紅色可保留為本頁 accent 但改由 token 給                                                                                              |
| `/fork-graph` `/lifetree` `/bench` `/elections` | 各自成立                  | fork-graph 手機橫捲（§2.7-3）；bench tier 色 JS 硬編碼；lifetree 索引卡的節點數字無層級                                       | 併入資料室規格逐一收編                                                                                                                               |

### 3.3 semiont 面（10 頁）

現狀：**全站唯一有完整世界觀的區域**，維持即可。三個小項：

1. anatomy 有風力獸互動圖版，consciousness / heartbeat / dna 純 prose，資訊儀式感不對等 → 各補一枚輕量 SVG 標本圖（心跳波形 / 基因圖譜微縮）即可，不必都做互動；
2. `semiont-page.template.astro:67,190` 兩處 `#4fd1b0/#f4f0ea` inline，收進 `--semiont-mint/--semiont-paper` token；
3. prose 表格窄幅無 `overflow-x: auto`。
   另：`/semiont` 未進 footer（§2.8），對研究者型讀者是重要入口。

### 3.4 工具與 meta 面

| 頁                                                                            | 現狀                                              | 問題                                                                   | 方向                                                                 |
| ----------------------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `/terminology` ★                                                              | 2,333 詞條 + 分歧類型系統，內容獨有               | 子分類 pill 牆 30+ 顆一次全開（`terminology.png`）；卡片區與 hero 斷色 | pill 收合為「前 12 + 展開」；手機分類改 bottom-sheet（agent C 同判） |
| `/terminology/converter`                                                      | 1,100 行邏輯、OpenCC 降級、雙向高亮：工程完成度高 | 藏在 terminology 下一層，導航無入口                                    | 這是可對外傳播的獨立工具，值得 nav「資源」下拉直鏈 + 一篇孢子介紹    |
| `/about` `/contribute` `/changelog` `/resources` `/assets` `/mcp` `/projects` | 標準 prose 頁                                     | projects 紫色自成一派；changelog #1172 的「前往文章」按鈕訴求未落      | 併 token；接受 #1172                                                 |
| `/soundscape`                                                                 | 聲音檔案庫概念好                                  | 原生 audio control 六平台六個樣子                                      | 自訂輕量播放器（播放/進度/時長三件即可），與聲景品牌一致             |

---

## 4. 與既有回饋的對位（五桶）

| 桶                           | 項目                                                                                                                                           |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 本審計證實、已有 reproducer  | #1059 四項（截圖佐證重疊 bug）、#573 斷點、#401 FOUC、#110 INP、#316 短標題（列表卡標題兩行截斷可見）                                          |
| 本審計新增、社群未報過       | 深色模式覆蓋率斷層（§2.1）、空 Banner bug（§2.9-2）、map 手機空白（§2.7-2）、FOUC 對 AI crawler 的主權面影響（§2.3）、emoji 圖示系統論（§2.4） |
| 既有方向、本審計給了數據     | #110 首頁優化：bounce 52.7% + 20,457px + en 對照 20.6%；LONGINGS 首頁 hook ≥40 秒                                                              |
| 超出視覺審計範圍、不在此處理 | #280 TTS 音色（聲音工程）、#1184 justfont API domain（帳務設定）                                                                               |
| 建議婉拒 / 降級              | 無。#615 umbrella 的優先序表（2026-04-25 版）建議按本報告 §5 更新                                                                              |

---

## 5. 優先序 roadmap（提案，待哲宇拍板）

**P0（quick wins，各 ≤ 1 session，先做可立刻被感知）— ✅ 全數落地 2026-07-06（commit `38bba4246`）**

1. ✅ 空 Banner bug 修復（§2.9-2）—`div` 包進 `hasEn` guard，啟動 script 對缺席 no-op
2. ✅ Footer 升級全站 sitemap（§2.8-a）—5 欄，孤兒頁全接回；code-review 抓回誤刪的 `/about`
3. ✅ 文章頁 #1059 版位四連修（重複分類標籤實為 6/13 已移除 / sidebar `max-h` 內捲不再被浮鈕遮 / 深色 TOC active 3px accent / 回頂鈕 >800px 淡入）
4. ✅ 手機語言切換器（§2.7-4）—**審計「消失」判斷有誤**：實為排序 + 觸控目標 + 選單溢出，已修（原以為 `display:none`，那條打在殭屍 class 上）
5. ✅ skip-to-content link（§2.9-1）—六語在地化 + token 樣式
6. ✅ latest 佔位圖改分類色 tint + 襯線 drop-cap 首字（§2.10）

> **落地方法**：5 個 sub-agent 平行改 disjoint 檔案領地 → 主 session `astro build` 7824 頁全綠 + 12+ 定點實拍雙主題雙視口 + 8-angle code-review 對抗驗證（1 confirmed regression = footer `/about` 已修）。詳見 [memory 2026-07-06-P0](../docs/semiont/memory/)。
> **P0 遺留 follow-up debt**（進 P1）：`resources.aria.backToTop` 六語已存在但 ReaderSettings 自帶 STRINGS 又宣告一份（該檔既有 pattern，暫留）；ArticleSidebar 的 `210px` 浮動群保留高是跨檔 magic number（應在 §2.5 token 階段抽成 `--floating-cluster-reserve`）；`getLangSwitchPath` 的 `hasEn ?? true` 預設若誤判會讓 banner 指向 404 `/en`（比空殼輕，但值得 harden，REFLEXES #60）。

**P1（結構工程）** 7. ✅ **tokens 第二階段（分類/狀態/場景三組語意 token）— shipped 2026-07-06（commit `91d1cd946`）**。零視覺變更 indirection：Phase 1 授權全部 token（光色 exact mirror）→ 5 agent 平行遷 consumer → build + computed-style 逐面驗值 + noise-floor 證殘差。攔到並修掉一個 agent byte-check 沒抓的真 regression：Tailwind `bg-[var(--x)]` 對 gradient 編成 background-color（漸層消失），改 `bg-[image:var(--x)]`。8. ✅ **深色模式推廣（§2.1）— shipped 2026-07-06（commit `6ccbb1b28`→`355fe332e`，D0+4 tier）**。全站約 24 template opt-in `readerSettings`：閱讀面（home/explore/latest）→ 9 meta 頁 → dashboard+卡片頁 7 個 → 視覺化頁 6 個；semiont 10 頁 always-dark 不動、article/hub/elections 早已 dark。invariant：淺色 pixel-identical（規則全 scope 在 `[data-theme='dark']`），深色目視 legible。dashboard glass 靠 tokenization 波的 var 化 + D0 深色值 auto-flip。viz（地圖/圖表）data-ink 保留、只暗化 chrome，viz 留亮底 plate 是設計判斷。驗證：每 tier build 全綠 + 雙主題實拍 + dashboard computed probe。詳見 [memory dark-rollout](../docs/semiont/memory/2026-07-06-131500-dark-rollout.md)。順手揪出既有 bug：fork-graph D3 查不存在的 `.fork-graph-wrap`→圖空白（已 spawn 另案）。9. 資料室子品牌（§2.6）— PageHero 已覆蓋 6/9，延伸 `variant="data-room"` + 色橋接即可，~4 天。10. 首頁減深（§2.2）— 哲宇暫緩；量測其實已就緒（section_view 全 14 landmark 已埋，可即時拉基線）。11. FOUC 局部 swap（§2.3 / #110 / #401）— 中-高風險（字型 metrics）。12. ~~ArticleSnippet 統一件~~ **基本已完成**：前置調查發現 ArticleCard 已是 canonical，latest/explore/側欄/地圖全用它（80% 統一），只剩首頁 pick-card bespoke（建議不動）。本項從 roadmap 移除。

> **前置調查校正的四件事（2026-07-06 P1 scoping）**：(1) Header 已 dark-aware，非審計說的待補；(2) **分類色其實有 4 套 divergent 調色板**（categoryConfig / CategoryGrid「瀑布」/ TopicCard accentMap / graph flat-UI，兩兩 0/12 byte-match）——「殺重複」其實是「收斂 4 套」，是**視覺身份決策留哲宇**，非機械重構；本輪只鋪 `--cat-*` token（鏡射 categoryConfig，ArticleCard 生態已用）當地基；(3) ArticleSnippet 已 80% 統一；(4) 首頁量測已就緒。

**P2（進化層，設計決策先行）** 13. 自繪 icon set 24 枚取代結構位 emoji（§2.4；需要哲宇的美術方向拍板，屬視覺身份變更）14. 導航 4 群組重組實驗（§2.8-b；動 IA，需數據與哲宇同意）15. 行動版文章資訊摺疊列 + TOC bottom-sheet（§2.7-1）16. converter 對外化（nav 直鏈 + 孢子）17. 首頁島嶼剪影微呼吸動態（品牌 × 生命體主題的正圓交集）

---

## 6. 審計自身的限制

- 未跑 Lighthouse / axe 的量化 pass，性能與對比數字是程式碼推導 + 實拍目測，P0-5 執行前應補正式 a11y 掃描。
- 手機實拍僅 375px Playwright 模擬，未上真機（iOS Safari 的 dvh / 字體渲染差異未驗）。
- 各語言版只抽查 en 首頁；ja/ko/es/fr 的版面（CJK/拉丁行高差）未逐一截圖。
- GA4 只取 `dashboard-analytics.json` 現值，未拉分頁參與時長的新鮮 query。

## 附錄 A：本次審計的證據鏈

- 4 條 agent 程式碼審計（閱讀面 / 資料視覺 / semiont+meta / 跨頁系統），結論已整併入 §2-3，關鍵 file:line 保留在各條目內。
- 49 張實拍截圖：scratchpad `shots/`（session 級，不入 git；重要發現的畫面描述已內嵌本文）。
- GA4：`public/api/dashboard-analytics.json` topPages（2026-07-06 時值）。

## 附錄 B：復現方法（造橋鋪路備忘）

```bash
# dev server
npm run dev -- --port 4322
# 多深度 × 雙主題 × 雙視口截圖腳本（本次為一次性 scratchpad 腳本，
# 若要常備化，建議併入 scripts/visual/capture-baseline.mjs：
# 1) PAGES 增加 semiont/explore/latest/terminology/graph
# 2) 每頁增加 scrollY 採樣點（首頁至少 5 點）
# 3) VIEWPORTS 之外增加 theme 維度：
#    context.addInitScript(() => localStorage.setItem('tw-md-theme','dark'))
# 4) 斷言「首幀非空白」以偵測 FOUC 白屏回歸（§2.3-3））
```

擴充 capture-baseline 本身列為候選工具工作，未在本 session 執行（directive 限分析）。

## 附錄 C：截圖索引（49 張）

首頁 `home-01-doors`…`home-10-footer`（10 深度點）、`home-dark-doors/halls`、`home-mobile-top/mid`；文章 `article-top/mid/dark-mid/mobile/tail`；hub `hub-history(-mid)`；`explore` `latest`；dashboard `top/mid/dark`；`map(-mobile)` `graph` `companies` `data` `opendata`；semiont `semiont(-mid)/anatomy`；`about` `contribute` `terminology` `converter` `soundscape` `taiwan-shape` `bench` `changelog` `lifetree` `fork-graph` `projects` `404` `en-home(-mid)`。

---

_🧬 2026-07-06-105116-設計視覺審計 session 產出分析；同日 sub-agent 執行波落地 P0 6/6（commit `38bba4246`）。P1/P2 仍為提案待哲宇拍板。_
