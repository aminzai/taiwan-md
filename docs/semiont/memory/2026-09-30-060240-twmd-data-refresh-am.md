# 2026-09-30-060240-twmd-data-refresh-am — 14 步全綠，但建置效能那份是八月的舊資料，翻歷史發現第五次，當班接進新鮮度閘門

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:02 → 06:1x +0800（commits：`c4b571794` refresh 06:09:09、`5d431f771` fix 06:09:44、本篇收官）
> 資料來源：`git log %ai`、排程器 `list_scheduled_tasks`、`public/api/dashboard-build-perf.json` 的 git 歷史

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 落檔 246,880 bytes，分頁讀到 `wake:END`，體檢全綠。器官 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐92，最低仍是免疫（`review_coverage` 19）。Q14：48 小時內 babel-vortex 第五十二輪收官（十二語缺口 475 對歸零），00:48 babel-nightly 讓空佇列的 dispatcher 改睡十分鐘，05:39 routine-sync 第 63 輪零漂移並撞見 09-29 維護班因用量上限沒醒成，05:55 embeddings 索引零 diff。甦醒時 `ACTOR_BUSY`（`babel-push-every --watch` 與 `babel-dispatch` 兩個進程）。

## 讓場與 14 步

本機與 origin 同步（0/0），照前二十三夜讓出 Step 1，不在 babel 寫工作樹時 auto-stash：header 加第 117 行之後組成 runner，`bash -n` 過後丟背景跑 2–14。Stage 1.5 先跑，排程快照在 pipeline 開跑前落檔（14 enabled、4 disabled）。

三源全綠：CF 七天 3,804,778 requests、404 率 0.84%、AI 爬蟲 219,359 次跨 18 家，GA4 與 SC 各 20 筆，analytics 內容日 2026-09-29。`_translations.json` 13,488 筆零孤兒，spore 166 篇 0 warnings，fork-census 無新子代。GitHub ⭐1191 🍴188 👥76。狀態板記一筆 degraded：09-29 維護班 fire 後零 git 痕跡，就是 routine-sync 已記的用量上限那次，今天 08:30 會再排。Step 11 報 14 個 JSON 全為今日 mtime、0 stale。Step 12 spore SSOT 0 errors、Step 13 no-op、Step 14 INDEX 726 行。

`c4b571794` 用路徑清單檔收 31 檔。清單列 32 檔，`verify-commit-scope` 報 31≠32：少的 `src/data/map-markers.json` 被 prettier 格式化回跟 HEAD 一字不差，本來就沒東西可收，索引裡留著格式化前的 blob，`git reset -- 那一檔` 對齊後 scope OK。babel 的五個檔沒碰。

## 建置效能是舊的，而閘門看不見

Step 10 印「latest build 250s／7d avg nulls／coverage 60.9d」，昨天是 2,166 秒。打開檔案，最新一筆 run 是 2026-08-01，status 寫 `ok`，mtime 是今天，所以 Step 11 放行。當下重跑產生器就拿到正常資料（最新 1,764 秒、7 天平均 1,939 秒），代表 06:06 那一次 GitHub API 對帶 `status=completed` 的查詢回了一頁舊 run。

回頭逐 commit 讀這份檔案的歷史，同樣的症狀已經 commit 過四次：08-21（最新停在 08-03）、09-02（08-03）、09-18 與 09-19（09-08）。四次都是 `ok`、都過了 Step 11，也沒有任何一班提到。這跟 dashboard-immune 五月那次 11 天靜默同一類，只是這次 mtime 是新的、內容是舊的。

`5d431f771` 把修補落在兩處：`extract-build-perf.mjs` 看最新成功 run 的年齡，超過兩天就換不帶 status 的查詢重抓，還是舊的就寫 `stale-source`、附原因、exit 1（`prebuild:buildperf` 有 `|| true`，不會擋建置），Step 11 讀這份檔的 `status`，非 `ok` 算 stale。強制把門檻設到極小做了一次正控制，確認會寫出 `stale-source`，正常門檻重跑回到 `ok`。DATA-REFRESH-PIPELINE 升 v2.3 記下這條。順手修掉平均值為空時印「nulls」的字樣。

## 404 條件仍不成立

monitor-404 記 09-28 全日 3,558 筆，unknown 2,219 佔 62%，連三夜過半，但榜首是 `/lifestyle/台灣海關報關制度與ezway`（12 次），不是探路檔名，照 09-29 交接不動 `SCANNER_RE`。這一格裡有一部分其實不該是 unknown：`台灣海關報關制度與EZWAY.md`、`NVIDIA在台灣.md`、`Music/五月天.md` 都存在，讀者打的是小寫或錯分類的網址，分類器沒解析成 slug-variant／renamed。交給維護班。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅                                                    |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生，build-perf 當班重抓）    |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary`（見下） |

## Handoff 三態

繼承 `2026-09-29-060812-twmd-data-refresh-am` 與 `2026-09-30-055548-twmd-embeddings-nightly`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 Write session 帶哲宇 review；OBSERVER-QUEUE #75〜#90（待決）本班不動。
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04，動得了 `scripts/tools/`）— `routine-sync.py` 對賬前 `git fetch`、有差非 0 exit；讀 live-state 時印鏡像新鮮度（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，席位 `/twmd-routine`，動得了 routine prompt）— 本 routine Stage 1.5 寫明「pipeline 開跑前先跑」。第四班照這個順序排對，prompt 仍只寫「每次必跑」。
- [x] ~~pending（觀察）— build 秒數攢到三點再判~~ — retired by 本班：09-28 1,850 → 09-29 2,166 → 09-30 1,764，沒有方向，而且 09-19 以前有幾天的點本身是舊資料，改看修好後的 7 天平均。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 讓自動 gc 停擺，今天 commit 仍印 unreachable loose objects 警告（REFLEXES #35）。
- [ ] pending（觀察，LESSONS `relative-category-links-survive-link-check`）— `md-extension` 10-02 若仍 >200 改由 heal 腳本轉絕對路徑，席位 maintainer-am。
- [ ] pending（延續，席位 `twmd-terminology-trends-monthly` 10-05）— `/terminology/變壓器` 用語需求，今天仍在 unknown 榜上（9 次）。
- [ ] pending（延續，babel 專屬，席位 babel-nightly／babel-vortex）— 明細在 `2026-09-30-004819-twmd-babel-nightly.md`（OBSERVER-QUEUE #89 待決、自造 slug 存量 813 條），不重抄（REFLEXES #74）。

本 session 新 handoff：

- [x] ~~build-perf 舊資料以 ok 過關~~ — `5d431f771` 已修並接進 Step 11。
- [ ] pending（席位 maintainer-am，動得了 `scripts/tools/monitor-404.py`）— unknown 裡有能解析的：`/lifestyle/台灣海關報關制度與ezway`（實檔 EZWAY 大寫）、`/technology/nvidia在台灣`（實檔 NVIDIA）、`/people/五月天`（實檔在 Music）。分類器對大小寫與跨分類同名不做比對，資料在 `reports/404-monitor/latest.json` top_paths。另有 `/es/technology/taiwan-bicycle-industry/null` 11 次，是某處把 null 接進網址。
- [ ] pending（觀察，席位本 routine）— 明天看 Step 10 是否印出「換查詢重抓」那行，有的話記下日期，量 GitHub 回舊頁的頻率。

## Beat 5 — 反芻

今天的新鮮度閘門回報全綠，卻有一份檔案的內容比檔案日期舊兩個月。閘門量的是「檔案有沒有被碰過」，而產生器每次都會把檔案寫一次，所以這把尺對產生器本身的輸入是瞎的。analytics 那一份早在九月就補過內容日期檢查，當時修的是同一種病，只是沒有人把那個修法推到其他檔案。

讓我注意到的是一個不對勁的數字（250 秒對上昨天的 2,166 秒），不是任何警告。前四次數字可能沒那麼刺眼，或者當班沒停下來看。現在產生器自己會說它拿到的是舊的，下一次不必再靠有人剛好覺得哪裡怪。

🧬

---

_v1.0 | 2026-09-30 06:1x +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步資料刷新（第二十四夜讓場）_
_誕生原因：排程 06:00 觸發；babel writer 進程在跑_
_核心洞察：(1) 14 步全綠零過期 (2) build-perf 內容舊而 mtime 新，歷史第五次，當班修進產生器與 Step 11 (3) 404 unknown 有一部分是大小寫與跨分類的可解析網址_
_LESSONS-INBOX：無新條目（修補已落 canonical，DATA-REFRESH v2.3）_
