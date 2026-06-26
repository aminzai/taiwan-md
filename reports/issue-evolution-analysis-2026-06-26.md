# Issue 進化分析報告 — 2026-06-26

> twmd-become Full mode session（哲宇 directive：「處理線上可以進化的 issue 先完整分析 report 然後跟我討論 一個一個進化＋實作＋驗證＋紀錄」）
> 前置已完成：PR #1178 烏坵 + #1174 滿月習俗 heal+merge（見 git log `bce742694` / `8f7ec7d5a`）。

9 個 open issue，依「可進化性 ×（價值 / 工時 / 自主權邊界）」分四層。每條附 ground-truth 程式碼定位（Explore agent 實查）。

---

## Tier 1 — 快速進化（高價值、低工時、可自主做完＋驗證）

### #1172a — 更新日誌每筆加「前往文章」按鈕（idlccp1984）

- **價值**：高。讀者在 changelog 看到感興趣的修訂，目前無動線直達文章，要手動搜。導流痛點。
- **程式定位**：`src/templates/changelog.template.astro:355-502`（client filter）+ `src/components/commits/CommitLog.astro`（render commit item）+ `src/lib/commits.ts`（parse）。
- **技術判斷**：每筆 changelog = 一個 commit。挑戰在 commit → 文章 URL 的對應（一個 commit 可能動多檔 / 非文章檔）。可行解：從 commit 動到的 `knowledge/<Cat>/<slug>.md` 推 article route，單檔 commit 直接給按鈕、多檔給「查看 N 篇」。
- **工時**：S–M。**自主權**：純前端，可自主。

### #1140 — 用語分歧誤判清理（哲宇本人 + 白煮蛋回報）

- **價值**：高（**改善 immune organ 精準度 — 目前 immune=50 是最低分器官**）。糾心／揪心、吸引眼球這類「台灣人本來就在用」的詞被當中國用語誤判 = false positive 侵蝕信任。
- **程式定位**：`data/terminology/*.yaml`（term cards SSOT）→ `data/terminology/.china-terms.detection.tsv`（偵測表）+ `.china-terms.false-positives.tsv`（例外表）；checker 在 `scripts/tools/lib/article_health/checks/terminology.py`。
- **技術判斷**：把確認是台灣慣用的詞，從 detection 降級或加進 false-positives。需逐詞查證（這詞台灣媒體史上用多久）。
- **工時**：S。**自主權**：⚠️ terminology = DNA/editorial 層，**白名單哪些詞要哲宇拍板**（避免把真中國用語也放行）。

### #1059-small — 內容頁三個小修（idlccp1984 umbrella 拆出）

- **(c) 暗黑模式 TOC active state**：`src/components/TableOfContents.astro:73-76` active 樣式存在（teal 左框），暗黑模式對比不足 → 調 `src/styles/dark-polish.css`。S。
- **(d) 回到頂部按鈕**：目前**沒有**（只有 reading progress bar）。加一顆 floating back-to-top。S。
- **(f) 關鍵詞雲擋住分享鈕**：`src/components/ArticleSidebar.astro:274-385` 窄寬度無 reflow → 加 media query。S。
- **自主權**：純前端 UI，可自主。**但有圖片參考（IMG_0015-0018）我看不到**，需哲宇確認視覺意圖或我截圖 dogfood 驗證。

---

## Tier 2 — 中度進化（需哲宇策展決策才動）

### #1175 — 鹽酥雞／鹹酥雞 合併（idlccp1984）★ handoff 已掛哲宇

- 兩篇同一食物（[台灣鹹酥雞](https://taiwan.md/food/台灣鹹酥雞/) + [台灣鹽酥雞](https://taiwan.md/food/台灣鹽酥雞/)）。
- **決策點**：(A) 留一篇 canonical + 另一篇 301 redirect / (B) 兩篇都留、強化交叉引用 / (C) 真正合併成一篇。需哲宇選方向（策展判斷 + SEO 影響）。
- **工時**：M（含 redirect 設定 + 多語同步）。

### #1016 — 夜生活與KTV文化 拆兩篇（idlccp1984）

- 建議把現有〈夜生活與KTV文化〉拆成「夜生活」+「KTV」。
- **決策點**：拆分是否真的更好？KTV 是夜生活子集，拆開可能各自單薄。需哲宇判斷（策展）。
- **工時**：M（拆 = 近乎重寫兩篇）。

### #1172b — 「最新文章」定義分流（新建 vs 近期修改）

- `content-dates.json` 已分別存 git last-modified；目前 `/latest` 只用 `date`（發佈日）排序，未分流。
- **決策點**：要不要在 /latest 旁開「近期更新」區？還是 changelog 已涵蓋？需哲宇決定資訊架構。
- **工時**：M。

---

## Tier 3 — 大型進化（完整文章 / 大功能）

### #574 — 聲景投稿（nistoreyo）★ 高價值貢獻者

- **投稿者是聲景研究碩士**，無 GitHub 背景，主動提供持續內容協作。這是難得的領域專家小丑魚。
- 已附一份起手稿（聲景／soundscape 概念文）。需走完整 REWRITE-PIPELINE 變成正式文章 + 後續邀他持續供料。
- **工時**：L（完整深度文）。**價值**：高（專家 + 獨特題材 + 長期關係）。

### #1171 — /latest + /changelog 分段載入（idlccp1984）

- 現況：`/latest` 一次載全部 ~240 篇；`/changelog` 抓多達 9999 commit。確有 perf 隱憂。
- 解：pagination 或 infinite scroll（每次 10–20 筆）。
- **工時**：M–L。**前置**：先量目前實際載入大小，確認不是 premature optimization。

### #1059-big — sidebar 隱藏切換 + 章節朗讀

- 側邊欄 hide/expand toggle（+ 狀態保持）：M。
- 章節級朗讀按鈕（每個 h2 前加朗讀）：M-L，且關聯 #280 語音品質。

---

## Tier 4 — 已知限制 / meta

### #280 — 朗讀 AI 聲音令人不適（alstontsai0816，2026-03-29）

- 現況：`src/components/TextToSpeech.astro` 用瀏覽器 `SpeechSynthesis`（rate 0.95），全文一鍵朗讀。
- AI 語音不適是瀏覽器 TTS 先天限制；人工錄音不可規模化（240 篇 × 6 語）。
- **可做**：提供語音選單 / 調更自然的預設 voice / 語速控制。**難全解**。關聯 #1059 章節朗讀。

### #615 — 視覺與 UI/UX 統合追蹤 umbrella（哲宇）

- Meta 容器 issue，非直接可實作。建議當常駐 tracker，把 #1059 / #1172 / #1171 掛進去；或關掉改用 label。

---

## 建議起手順序

1. **#1140 用語誤判**（改善最低分 immune organ + 哲宇本人 idea，但要你拍板白名單）
2. **#1172a 前往文章按鈕**（純前端、高導流價值、可自主驗證）
3. **#1059-small 三個 UI 小修**（dogfood 截圖驗證）
4. → 再進 Tier 2 策展決策（#1175 / #1016）
5. → Tier 3 大工程（#574 聲景文最有戰略價值）

---

_作者：Taiwan.md 🧬 | 2026-06-26 twmd-become Full mode_
