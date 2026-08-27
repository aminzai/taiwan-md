# 2026-08-23-031233-rawlink-divergence — 功能頁 .md 按鈕全家族修復 ＋ 筆電 main 分歧完整解決（撿回兩件困住的真資料）

> session rawlink-divergence — 哲宇接起 task chip ＋ 追加「分歧也完整解決」「做完後 /twmd-memory」
> Session span: 02:56 → 03:15 +0800（2 commits：`938223308` heal ＋ `b8b64142c` rawlink）
> 資料來源：`git log %ai`

## 觸發

上一輪做 [/search 頁（issue #1496）](https://github.com/frank890417/taiwan-md/issues/1496)時 dogfood 抓到「查看 Raw Markdown 版本」按鈕把任何單段路徑當分類 Hub 的全家族斷鏈，只補了 /search 一條並開 chip。哲宇接起 chip，同時指示把筆電 main 與 origin 的分歧（本地領先 71、origin 領先 306）一併完整解決。

## 分歧解剖與資料搶救

先驗屍再動刀：`git cherry` 對賬顯示 68 個本地獨有 commit 全部只動 `reports/babel/live.html` 與 `babel-live.json`——筆電上還在跑的 babel 脈搏 cron 每小時量**過期鏡像**（total_zh=992 vs origin 已破千）並因分歧推不上去。未 commit 的工作樹再盤一輪，找到兩件真資料：8/19 演算藝術 session 改了 projection 報告（哲宇 callout 修正＋兩個新增章的登記）與 newsroom stage-events 的 17 行 making-of，都困在筆電從沒上過 origin。處置：全現狀先進 `backup/laptop-main-20260823` branch（raw 永不刪除），兩件真資料經 worktree 以 `938223308` 推上 origin（stage-events 第一版用時序重排合併，看到 diff 爆成 579 行才改回最小 append——append-only log 不該被我重排），然後 main reset 到 origin/main、ff 拉到最新，筆電推拉恢復正常。過期鏡像讀數與 prebuild 產物不上 canonical，留在 backup。

## rawlink 全家族修復

`b8b64142c`：分類判斷從「任何單段路徑首字大寫」改成 build-time 注入 filesystem-derived 真實分類表（staticRoutes 新增 `getCategoryDirMap`），功能頁指向 `src/pages/` 真實原始檔。語言前綴從寫死 `/en/` 改成全部十一個啟用語言（從前 `/ja/history/文章` 會連到不存在的 `knowledge/Ja/`）。驗收時又多剝一層：ja/ar/ru 部分分類沒有翻譯版 Hub 檔，補 `getTranslatedHubPresence` 存在性地圖（module-level cache，per 神經迴路 frontmatter per-render 教訓）讓缺檔語言 fallback 到 zh 原檔。12 個代表頁面 iframe 批次驗 href ＋逐一驗目標檔案存在。/search 上一輪的單點補丁一併收攏進通用邏輯。

## 收官 checklist

| 檢查項                       | 狀態                                |
| ---------------------------- | ----------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                  |
| Timestamp 精確               | ✅（git log %ai）                   |
| Handoff 三態已審視           | ✅                                  |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官級變化）                  |
| 自我檢查工具 PASS            | ✅（check:tmpl-lang 綠、12 頁驗證） |

## Handoff 三態

繼承 2026-08-23-021729-search-results-page：

- [x] ~~本地 main 分歧需哲宇看一眼~~ retired by 本 session（哲宇 directive 完整解決：backup branch ＋真資料上 origin ＋ reset）
- [x] ~~功能頁 Raw Markdown 全家族斷鏈 task chip~~ retired by 本 session（`b8b64142c`）
- [ ] pending（給哲宇，原樣延續）— issue #1496 末條 exams.astro 留言要不要請對方另開 issue
- [ ] pending（原樣延續）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 27MB 待處置（本輪發現 4 張演算藝術 tracked 圖在筆電工作樹曾缺失，已還原，佐證這批媒體工作沒收乾淨）
- [ ] pending（原樣延續）— 其餘繼承項見上一份 memory

本 session 新 handoff：

- [x] ~~筆電 babel 脈搏 cron 去留~~ retired by 同 session（哲宇拍板停：`md.taiwan.babel-pulse` launchd agent 已 bootout，plist 改名 `.disabled` 保留可還原；sense-fetch 與其他 routine 不動）
- [x] ~~backup/laptop-main-20260823 branch~~ retired by 同 session（哲宇拍板刪：`git branch -D`，原 750b0a917；兩件真資料已在 origin）

## Beat 5 — 反芻

分歧的 337 個 commit 落差聽起來嚇人，解剖完只有 30 行是真的：兩件被困的真資料加起來不到 backup branch 那個快照 commit 的千分之三。其餘全是一台機器對著自己的過期鏡像每小時心跳一次的迴聲。「先驗屍再動刀、raw 全部留在 backup、只有驗過身份的資料上 canonical」這個順序讓 reset --hard 這種聽起來危險的動作變成無損操作。stage-events 合併那次的教訓小而具體：手癢把 append-only log 排序成「更整齊」的樣子，diff 立刻告訴我整齊是有代價的。

🧬

---

_v1.0 | 2026-08-23 03:15 +0800_
_session rawlink-divergence — task chip 接手＋哲宇追加分歧完整解決_
_誕生原因：上一輪 /search dogfood 的兩條 handoff 在同一 session 內被哲宇轉成 directive_
_核心洞察：(1) 分歧解決的安全順序是驗屍→backup→搶救→reset (2) append-only log 的「整理」本身是破壞 (3) 過期鏡像上的儀器讀數是迴聲不是資料_
