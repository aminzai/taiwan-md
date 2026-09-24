# 2026-09-25-060610-twmd-data-refresh-am — 第二十夜讓場 14 步全綠零 stale；/sitemap.xml 那條 301 三天來從沒生效過

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:1x +0800（3 commits：`c900cafda` refresh 06:05:43、`78b480aa8` 註解更正、本篇收官）
> 資料來源：`git log %ai`、排程器 `lastRunAt`、線上 `curl -sI`

## 觸發

排程 06:00 觸發。任務三段：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門可能抓到的過期檔。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 落檔 257,433 bytes，Read 分頁讀到 `wake:END`，體檢全綠。器官 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐90，最低仍是免疫 59（`review_coverage` 19，黃燈自 07-05）。Q14：48 小時內幾乎全是統一調度器的十二語批次；00:30 那班修了三道「一篇卡死所有模型」的閘門、替三篇新文補 slug；05:30 routine-sync 第 59 輪零漂移；embeddings 05:00 那班確認殼層修補後第一夜用對的殼啟動。觀察者 09-19 最後在場。

## 讓場、快照落檔與 14 步

`ACTOR_BUSY`：dispatcher 98122 連跑四天五小時，帶四個翻譯進程在寫工作樹。`git fetch` 後本機比 origin 多一個 commit（embeddings 的 memory，`b7ccd44af`），沒有東西可拉，於是照前十九夜切掉 Step 1，用 header 加第 117 行之後組成 runner，`bash -n` 過後丟背景跑 2–14。趁 Step 2 在抓資料，先呼叫 `list_scheduled_tasks` 並跑 `routine-live-normalize.py`，讓 Step 6.6 讀到今天的快照：面板 18 條 13 operational、1 degraded、4 disabled，`stale_hours=0`。昨天交接說這個順序只有當班記得才會對，今天這班是從昨天的 memory 讀到才照做的。

三源全綠。CF 七天 3,998,585 requests、404 率 1.0%、AI 爬蟲 227,529 次跨 18 家，GA4 與 SC 各 20 筆。`_translations.json` 13,049 筆零孤兒，spore 166 篇 0 warnings，免疫 59，fork-census 零新子代。llms.txt zh 1122／en 1108／ja 1073／ko 1113／es 1111／fr 1112，GitHub ⭐1190 🍴187 👥75。CI build 1,801 秒、ms/page 136（前夜 148）。Step 11：14 個 dashboard JSON 全為今日 mtime，analytics 內容日 2026-09-24，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors、Step 13 no-op、Step 14 INDEX 722 行。整條跑了約四分鐘，`c900cafda` 用 pathspec 收 37 檔，收官後 14 檔又呈 `MM`，逐檔驗工作樹等於 HEAD 後清掉。

## /sitemap.xml 的 301 沒有作用

monitor-404 記 09-23 全日 3,885 筆，`unknown` 2,259 佔 58%，回到過半。前 300 條只涵蓋其中 693 筆，看得到的是長尾：韓文 slug 掛在中文路徑下、德文譯文路徑尾巴接中文詞之類，各十來筆，沒有探路檔名當榜首，所以不動判準。榜上仍有 `/sitemap.xml` 一天 10 筆，但 09-22 已經為它補過 301。

線上一查，`curl -sI https://taiwan.md/sitemap.xml` 回 404，`/sitemap-index.xml` 回 200。追下去：站體部署在 GitHub Pages，不讀 `_redirects`；會生效的只有 astro.config 用 `config/redirects-generated.json` 生成的 meta-refresh 頁，而 `generate-redirects.mjs` 刻意略過帶副檔名的 source，因為 `.xml` 路徑放不了 HTML 頁。09-22 那條規則只活在沒人讀的檔案裡。同一條產線的兩份說明也對不上：產生器檔頭寫「CF Pages 讀 `_redirects`」，astro.config 註解寫部署是 GitHub Pages、不支援 `_redirects`；手寫規則檔的檔頭還說「直接加一行即可」。本班只做了一件小事，`78b480aa8` 把那條規則旁的註解改成實情，免得下一班讀到它就以為已處理。真正的修法（build 產出裡放一份 `sitemap.xml`）動到建置流程，留給交接。LESSONS 開新條 `fix-lands-in-a-layer-the-platform-never-reads`（REFLEXES #84 的新維度）。

另一個家族 `md-extension` 524 筆，路徑長這樣：`/ko/culture/Culture/台灣文化創意園區發展.md`。全庫量到 15 份譯文還留著 39 條 `](../Culture/X.md)` 相對連結，是 09-21 母稿修好後、譯文還沒被 babel 依 source sha 重譯到的殘餘（09-21 當時 129 份）。dispatcher 正在寫這些語言，本班不碰，記進既有 LESSONS `relative-category-links-survive-link-check` 當第二個 instance。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅                                                    |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                         |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary`（見下） |

## Handoff 三態

繼承 `2026-09-24-060314-twmd-data-refresh-am`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）仍等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 為 manual-by-decision，本輪 live-state 與排程器一致。
- [ ] pending（延續，席位 09-27 `twmd-self-evolve-weekly`）— `routine-sync.py` 對賬前 `git fetch`，有差非 0 exit（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，同席位）— `routine-sync.py` 讀 live-state 時印鏡像新鮮度（REFLEXES #82／#85）。
- [ ] pending（延續，加一個數據點）— build perf ms/page 125→138→136→139→143→158→148→**136**。趨勢檔覆蓋仍只 2 天，拉 CI 歷史找起跳點的動作不變：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion`（REFLEXES #41）。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 讓自動 gc 停擺（REFLEXES #35）。
- [ ] pending（routine prompt，REFLEXES #43 變體）— Stage 1.5 應寫成「pipeline 丟背景後立刻跑」。今天是讀了昨天 memory 才排對，prompt 仍只寫「每次必跑」沒寫順序。
- [ ] pending（觀察，`monitor-404.py`）— unknown 58%，第一夜回到過半，但榜首是長尾不是探路檔名；條件（連兩夜過半＋探路檔名榜首）未成立，不動判準。
- [ ] pending（需判斷，延續）— 重複語言前綴 404 要不要補 301，要從 `state.json` 或 CF 全量撈，不能用截斷的 `top_paths`。本輪未量。
- [ ] pending（LESSONS `formatter-vs-generator-quote-churn-fakes-scope-alarm`，vc=4）— pathspec 收官後清索引殘影，連三班仍靠當班手動；寫進 refresh 與 embeddings 兩條 routine 的收官步驟或做成小工具。

本 session 新 handoff：

- [ ] pending（LESSONS `fix-lands-in-a-layer-the-platform-never-reads`）— `/sitemap.xml` 真正接住：在 build 產出放一份 `sitemap.xml`（複製 `sitemap-index.xml`，或讓 sitemap 整合多吐一個檔名），部署後 `curl -sI https://taiwan.md/sitemap.xml` 要回 200。順手把 `generate-redirects.mjs` 與 `config/redirects-manual.txt` 檔頭的平台說明改成跟 astro.config 一致。動建置流程，建議 Full／Review session 認領。
- [ ] pending（LESSONS `relative-category-links-survive-link-check`）— 15 份譯文 39 條 `](../Category/X.md)` 殘留，等 babel 依 source sha 重譯；若一週後仍在，改由 heal 腳本直接轉絕對路徑。

## Beat 5 — 反芻

09-22 那班做了正確的診斷、寫了正確的規則、重生後也看到規則出現在輸出裡，每一步都有證據，只是證據全都住在我們自己這一側。檢查修補有沒有成功，最短的路是從讀者那一側問一次；那一行 curl 成本不到一秒，三天來沒人跑，因為產生器吐出那一行的時候，感覺已經很像完成了。

今天的 runner 順序是照昨天的 memory 排的，所以面板綠了。明天這一班如果沒讀到這段，面板會退回昨天的樣子。兩件事的形狀相同：做對的那一刻留在紀錄裡，讓它繼續對的那一道步驟還沒寫進會被執行的地方。

🧬

---

_v1.0 | 2026-09-25 06:1x +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步資料刷新（第二十夜讓場）_
_誕生原因：排程 06:00 觸發，babel dispatcher 仍在寫工作樹_
_核心洞察：修補的驗收要從讀者那一側量；產物裡出現那一行，只證明產生器照做了，證明不了平台讀它。_
_LESSONS-INBOX：新 `fix-lands-in-a-layer-the-platform-never-reads`；`relative-category-links-survive-link-check` +1（vc=2）；`formatter-vs-generator-quote-churn-fakes-scope-alarm` +1（vc=4）_
