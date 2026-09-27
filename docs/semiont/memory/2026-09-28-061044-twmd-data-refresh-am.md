# 2026-09-28-061044-twmd-data-refresh-am — 14 步全綠零過期；狀態板寬限修補第一次生效；404 探路檔名第二次照條件收進掃描器

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:1x +0800（commits：`d6f566651` refresh 06:08:22、`dd00bd111` 404 判準 06:08:33、本篇收官）
> 資料來源：`git log %ai`、排程器 `list_scheduled_tasks`、線上 `curl -sI`

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 落檔 304,790 bytes，Read 分頁讀到 `wake:END`，體檢全綠。器官 🫀90 🛡️57 🧬95 🦴90 🫁85 🧫100 👁️90 🌐92，最低仍是免疫（刷新後 59，`review_coverage` 19）。Q14：48 小時內幾乎全是 babel-vortex 的驗收與 heal（數字事件表六個、二二八／九二一／八二三等譯錯修掉數十篇），加上 05:39 routine-sync 第 61 輪零漂移、05:59 embeddings 687 篇鄰居換了。甦醒時 `ACTOR_BUSY`，跑 pipeline 時只剩 `babel-push-every.py --watch` 一個常駐進程，commit 時 pre-commit 又偵測到兩個新 writer。

## 讓場與 14 步

本機與 origin 同步（0/0），照前二十一夜讓出 Step 1：header 加第 117 行之後組成 runner，`bash -n` 過後丟背景跑 2–14。Stage 1.5 先跑，排程快照在 pipeline 開跑前落檔（14 enabled、4 disabled）。

三源全綠：CF 七天 3,944,980 requests、404 率 0.85%、AI 爬蟲 219,694 次跨 18 家，GA4 與 SC 各 20 筆，analytics 內容日 2026-09-27。`_translations.json` 13,488 筆零孤兒，spore 166 篇 0 warnings，fork-census 沒有新子代。GitHub ⭐1191 🍴187 👥76。Step 11：14 個 dashboard JSON 全為今日 mtime，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors、Step 13 no-op、Step 14 INDEX 726 行。

Step 6.6 印出 `operational:14, disabled:4`，沒有 degraded 也沒有 down。昨天加的三小時寬限第一次在本 routine 自己身上生效：當天格記 idle，不再把正在跑的自己記成錯過。

build perf 的 ms/page 從 146 掉到 104，但這不是變快：建置秒數 1,941 → 1,850 只少 5%，分母頁數從約 13,300 跳到 17,785（十三語頁數封頂後計進來），coverage 只有 0.2 天。這串數字換了分母，前後不能直接比。

`d6f566651` 用 pathspec 收 32 檔。第一次下 commit 失敗：zsh 不對未加引號的變數做字詞分割，32 條路徑變成一個帶換行的參數。改用陣列展開後才進去，`verify-commit-scope.sh --head 32` 通過，post-commit 自動對齊 14 檔索引殘影。`knowledge/_translation-status.json` 在本班開始前就是 dirty（babel 的狀態檔，不是 refresh 產物），沒有收。

## 404 探路檔名第二次照條件收進掃描器

monitor-404 記 09-26 全日 2,918 筆，`unknown` 1,470 佔 50.4%；09-25 是 53%，榜首 `/rclone.conf`。09-22 交接設的條件（連兩夜過半＋榜首是探路檔名）成立，09-23 那班第一次照它做掉，今天是第二次。

照 09-23 的做法只收當夜 top 300 裡有證據的名字：`/rclone.conf`（21 筆）、`/api/console/api_server`（9）、`/settings/_payload.json`（6）、`/_profiler/latest`（3）、`/elmah.axd`（3）。動手前先驗尺：對 `articles.json` 裡 59,922 條路由字串與 `dist/` 49,526 條路徑零誤判。`dd00bd111` 改 `SCANNER_RE`，重跑後 unknown 1,428（約 49%），榜首換成 `/vi/society/the-reporter-investigative-journalism/:XGi` 這種站內長尾。移走的只有 42 筆：top 300 只涵蓋 unknown 的一小部分，長尾裡的探路名看不到，這一格仍會在過半邊緣來回。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅                                                    |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                         |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary`（見下） |

## Handoff 三態

繼承 `2026-09-27-061126-twmd-data-refresh-am` 與 `2026-09-28-055906-twmd-embeddings-nightly`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 為 manual-by-decision，本輪 live-state 與排程器一致。
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04，動得了 `scripts/tools/`）— `routine-sync.py` 對賬前 `git fetch`、有差非 0 exit；讀 live-state 時印鏡像新鮮度（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，席位 `/twmd-routine`，動得了 routine prompt）— 本 routine Stage 1.5 寫明「pipeline 開跑前先跑」。今天照前兩班的順序排對，prompt 仍只寫「每次必跑」。
- [ ] pending（延續，改寫）— build perf ms/page 序列 125→…→146→**104**，但今天換了分母（頁數 ~13,300→17,785），前後不可直接比。拉 CI 歷史時改看建置秒數：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion`（REFLEXES #41、#38）。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 讓自動 gc 停擺，今天 commit 仍印 unreachable loose objects 警告（REFLEXES #35）。
- [x] ~~pending（Full／Review session，LESSONS `fix-lands-in-a-layer-the-platform-never-reads`）— `/sitemap.xml` 部署後要回 200~~ — retired：今晨 `curl -sI https://taiwan.md/sitemap.xml` 回 200（routine-audit 09-27 已先看到）。
- [ ] pending（觀察，LESSONS `relative-category-links-survive-link-check`）— `md-extension` 524→331→144，babel 重譯在消化；10-02 若仍 >200 改由 heal 腳本轉絕對路徑（照目前趨勢不會觸發）。
- [x] ~~pending（觀察，`monitor-404.py`）— 條件（連兩夜過半＋探路檔名榜首）明天再判~~ — retired by 本班 `dd00bd111`，條件成立當班做掉。
- [x] ~~pending（本 routine）— 讀 Step 6.6 確認當天格是 idle~~ — retired：operational 14、無 degraded，寬限生效。babel-nightly 等長跑 routine 今天沒被記錯過，暫不按 routine 調寬限。

本 session 新 handoff：

- [ ] pending（觀察，`monitor-404.py`）— 移走探路名後 unknown 約 49%，仍在門檻邊緣。top 300 只看得到 unknown 的一部分，下一次同條件成立時先考慮讓 `top_paths` 按家族各留前 50，再決定收哪些名字（REFLEXES #38 零維度變體）。

## Beat 5 — 反芻

今天兩件事都是照前例做的：讓場的 runner 是第二十二夜同一個組法，探路名是 09-23 同一個條件的第二次成立。唯一出錯的是最機械的那一步，把檔案清單交給 git commit。前幾班都在 bash 語境裡寫同一行，今天這一行在 zsh 裡被當成一個參數，失敗訊息列出的卻是整串路徑，看起來像是檔案不存在，其實只是分隔方式不同。好在 pathspec 失敗時什麼都不會 commit，範圍檢查也把「HEAD 不是我的」當場叫出來，沒有讓錯的 commit 混進去。

build perf 那串數字值得記一筆：ms/page 掉三成看起來像一個好消息，分子幾乎沒動，是分母長大了。前面九個數據點累積的「在變慢嗎」這個問題，從今天起要換一把尺才問得下去。

🧬

---

_v1.0 | 2026-09-28 06:1x +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步資料刷新（第二十二夜讓場）_
_誕生原因：排程 06:00 觸發；babel 常駐推送進程在跑_
_核心洞察：(1) 狀態板寬限修補第一次生效 (2) 404 探路名照條件第二次收進判準，top 300 的視野限制仍在 (3) ms/page 換了分母，舊序列不可直接比_
_LESSONS-INBOX：無新條目_
