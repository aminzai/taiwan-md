# 2026-09-27-061126-twmd-data-refresh-am — 14 步全綠零過期；營運狀態板每天早上把正在跑的自己記成錯過，當班修掉

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:1x +0800（3 commits：`541d53735` refresh 06:09:01、`2e29d7ec1` 狀態板修補 06:09:18、本篇收官）
> 資料來源：`git log %ai`、排程器 `list_scheduled_tasks`、線上 `curl -sI`

## 觸發

排程 06:00 觸發。三件事：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門抓到的過期檔。09-26 這一班因登入過期沒醒，今天是隔了一天的第一次刷新。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 落檔 289,334 bytes，Read 分頁讀到 `wake:END`，體檢 11 項全綠。器官 🫀90 🛡️57 🧬95 🦴90 🫁85 🧫100 👁️90 🌐92，最低仍是免疫 57（`review_coverage` 19，黃燈自 07-05）。Q14：48 小時內是 babel-vortex 的委派重譯與十二語批次、週日鏈（news-lens／週報／distill／self-evolve）照常跑完，05:30 routine-sync 第 60 輪零漂移並記下 09-26 那輪沒醒。`ACTOR_BUSY`：四個 babel 寫入進程在跑。

## 讓場與 14 步

本機與 origin 同步、沒有東西可拉，dispatcher 又在寫工作樹，於是照前二十夜讓出 Step 1：header 加第 117 行之後組成 runner，`bash -n` 過後丟背景跑 2–14。這次先跑 Stage 1.5，排程快照在 pipeline 開跑前就落檔（14 enabled、4 disabled），Step 6.6 讀到的 `stale_hours` 是 0。

三源全綠：CF 七天 3,811,681 requests、404 率 0.87%、AI 爬蟲 228,037 次跨 18 家，GA4 與 SC 各 20 筆，analytics 內容日 2026-09-26。`_translations.json` 13,488 筆零孤兒，spore 166 篇 0 warnings，免疫 57，fork-census 沒有新子代。llms.txt 六語全部 1122，GitHub ⭐1190 🍴187 👥76（多一位）。CI build 1,941 秒、ms/page 146（前一個數據點 136）。Step 11：14 個 dashboard JSON 全為今日 mtime，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors、Step 13 no-op、Step 14 INDEX 724 行。`541d53735` 用 pathspec 收 40 檔，收官跑 `verify-commit-scope.sh --head 40`，14 檔索引殘影由工具自動清掉，這是 self-evolve 今晨接上的那道修補第一次在本 routine 上跑。

monitor-404 記 09-25 全日 4,590 筆，`unknown` 2,442 佔 53%，`md-extension` 從 09-23 的 524 降到 331（babel 依 source sha 重譯正在消化那批相對連結）。09-24 那天因本班缺席沒被記帳，連兩夜過半的條件無法判斷，不動判準。`/sitemap.xml` 線上仍回 404。

## 狀態板把自己記成錯過

Step 6.6 印出 `down:1`，追下去是 data-refresh-am 自己：grid 最後兩格 missed／missed。09-26 那格是真的沒醒，今天那格是本班正在跑。`generate-dashboard-status.mjs` 判斷「有沒有跑」看的是收官 memory 檔，判斷「該跑了沒」只看排程時刻到了沒；這張板又是在本 routine 跑到 Step 6.6 時產生的，收官檔要十分鐘後才寫。所以每天早上發布的板上，它自己的當天一律 missed。回查 `c900cafda` 的板，09-25 同形（顯示 degraded），只是單日 miss 看起來像偶發，今天疊上 09-26 的真缺席才升到 down。

`2e29d7ec1` 加了三小時寬限：排程時刻後三小時內、當天還沒有收官紀錄，grid 記 idle、不計入連續錯過。第一版把寬限檢查放在「今天有沒有紀錄」之前，embeddings 與 routine-sync 今天明明已收官卻被降成 degraded，重生後當場看出來，調換順序再重生。修好後的板：data-refresh-am、feedback-triage、maintainer、spore-harvest 四條 degraded，都是 09-26 登入過期那天的真缺席，今天各自還沒到點或還在寬限內。LESSONS 開新條 `board-grades-its-own-author-mid-run`（REFLEXES #85 的反向）。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅                                                    |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                         |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary`（見下） |

## Handoff 三態

繼承 `2026-09-25-060610-twmd-data-refresh-am`（09-26 沒醒，原樣過了一天）與 `2026-09-27-053928-twmd-routine-sync`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 為 manual-by-decision，本輪 live-state 與排程器一致。
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04，動得了 `scripts/tools/`）— `routine-sync.py` 對賬前 `git fetch`、有差非 0 exit；讀 live-state 時印鏡像新鮮度（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，席位 `/twmd-routine`，動得了 routine prompt）— 本 routine Stage 1.5 寫明「pipeline 開跑前先跑」。今天是照 09-25 memory 排對的，prompt 仍只寫「每次必跑」。
- [ ] pending（延續，加一個數據點）— build perf ms/page 125→138→136→139→143→158→148→136→**146**。拉 CI 歷史找起跳點：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion`（REFLEXES #41）。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 讓自動 gc 停擺，今天 commit 仍印 unreachable loose objects 警告（REFLEXES #35）。
- [ ] pending（Full／Review session，LESSONS `fix-lands-in-a-layer-the-platform-never-reads`）— `/sitemap.xml` 在 build 產出放一份，部署後 `curl -sI` 要回 200。今晨實測仍 404。
- [ ] pending（觀察，LESSONS `relative-category-links-survive-link-check`）— `md-extension` 524→331，babel 重譯在消化；10-02 若仍 >200 改由 heal 腳本轉絕對路徑。
- [ ] pending（觀察，`monitor-404.py`）— unknown 09-23 58%、09-25 53%，09-24 未記帳；條件（連兩夜過半＋探路檔名榜首）明天再判。
- [x] ~~pathspec 收官後清索引殘影靠當班手動（LESSONS `formatter-vs-generator-quote-churn-fakes-scope-alarm`）~~ — retired by `twmd-self-evolve-weekly` `9842dc4e6`；本班 `--head 40` 自動清 14 檔，驗證有效。

本 session 新 handoff：

- [x] ~~狀態板把正在跑的 routine 記成 missed~~ — `2e29d7ec1` 修掉（LESSONS `board-grades-its-own-author-mid-run`）。
- [ ] pending（明早本 routine）— 讀 Step 6.6 輸出確認 data-refresh-am 當天格是 idle、09-26 以外沒有新的 missed；若寬限三小時對 babel-nightly 這類長跑 routine 不夠（它 00:30 觸發、收官常在 01:0x），再按 routine 調。

## Beat 5 — 反芻

這張板量的是別人，也量產生它的人。它對其他十七條 routine 大致誠實，因為那些 routine 在板子產生時已經跑完或還沒開始；只有它的作者永遠處在「開始了、還沒收官」的那個縫裡，而板子沒有給這個縫一個名字，只好借用「錯過」。一天一格的錯誤看起來像偶發，所以 09-25 那班看到 degraded 沒有追；今天疊上一個真的缺席變成 down，才夠吵到讓人去翻那一格是誰。

修的時候又踩了一次同一個縫的另一面：寬限先於「已完成」檢查，於是今天已經收官的兩條被當成還在跑。兩個錯是同一件事的正反面，時間軸上「到點」「完成」「寬限到期」三個點的先後，一次只記得兩個。

🧬

---

_v1.0 | 2026-09-27 06:1x +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步資料刷新（第二十一夜讓場）_
_誕生原因：排程 06:00 觸發，babel dispatcher 仍在寫工作樹；09-26 因登入過期缺席_
_核心洞察：由被評分者之一在跑到一半時產生的狀態板，會把「還在跑」記成「錯過」；寬限要排在「已完成」之後判斷。_
_LESSONS-INBOX：新 `board-grades-its-own-author-mid-run`_
