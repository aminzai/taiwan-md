# 2026-09-29-060812-twmd-data-refresh-am — 14 步全綠零過期；404 未分類又過半但條件不成立，榜首是一個讀者在找的用語

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:1x +0800（commits：`98bb9babc` refresh 06:07:34、本篇收官）
> 資料來源：`git log %ai`、排程器 `list_scheduled_tasks`、`reports/404-monitor/latest.json`

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 落檔 272,779 bytes，Read 分頁讀到 `wake:END`，體檢全綠。器官 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐92，最低仍是免疫（`review_coverage` 19）。Q14：48 小時內主力是 babel-vortex 的驗收與 heal（「中華台北」頂替台灣地名、名人頂替擴表、vi 多篇交 Sonnet 重譯），加上 00:50 babel-nightly 修 48 條被翻成外文的站內連結、05:39 routine-sync 第 62 輪零漂移、05:57 embeddings 373 篇換鄰居。甦醒時 `ACTOR_BUSY`（三個 babel writer 進程）。

## 讓場與 14 步

本機與 origin 同步（0/0），照前二十二夜讓出 Step 1，不在 babel 寫工作樹時 auto-stash：header 加第 117 行之後組成 runner，`bash -n` 過後丟背景跑 2–14。Stage 1.5 照前兩班先跑，排程快照在 pipeline 開跑前落檔（14 enabled、4 disabled），Step 6.6 讀到 `stale_hours` 0。

三源全綠：CF 七天 3,843,851 requests、404 率 0.83%、AI 爬蟲 222,193 次跨 18 家，GA4 與 SC 各 20 筆，analytics 內容日 2026-09-28。`_translations.json` 13,488 筆零孤兒，spore 166 篇 0 warnings，fork-census 沒有新子代。GitHub ⭐1191 🍴188（+1）👥76。Step 11：14 個 dashboard JSON 全為今日 mtime，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors、Step 13 no-op、Step 14 INDEX 726 行。

`98bb9babc` 用 pathspec 收 33 檔。第一次在 zsh 用 `mapfile` 失敗，改 `bash -c` 又撞到兩件事：macOS 的 bash 是 3.2 沒有 `mapfile`，同一刻 babel 持有 index lock。最後把路徑清單寫進暫存檔再展開，`verify-commit-scope.sh --head 33` 通過，post-commit 對齊 15 檔索引殘影。`knowledge/_translation-status.json` 與 `reports/babel/progress-log-2026-09.md` 在本班開始前就是 dirty（babel 的檔），沒有收。

## 404 未分類過半，條件不成立

monitor-404 記 09-27 全日 3,899 筆，`unknown` 2,192 佔 56%。09-22 交接設的條件是「連兩夜過半＋榜首是探路檔名」。昨天收完探路名後落在約 49%，今天榜首是 `/terminology/變壓器`（18 次，瀏覽器 UA），不是探路名，條件不成立，沒有動 `SCANNER_RE`。榜上第二、四、八名（`/bitbucket-pipelines.yml`、`/env.txt`、`/aws-exports.js`）確實是探路名，但 top_paths 裡的 151 條 unknown 只涵蓋 518 次，佔 unknown 的四分之一，照名字收只會移走零頭。

`/terminology/變壓器` 值得單獨記：用語庫沒有這一條，這個詞只出現在 `data/terminology/_sources/invade/適配器.yml`。一個瀏覽器讀者一天敲了 18 次，性質接近 `untranslated-demand`，是用語需求而不是壞連結。交給 10-05 的用語趨勢月報判斷要不要收。

build perf 最新一次建置 2,166 秒，7 天平均 1,969 秒（coverage 0.8 天）；照昨天的交接改看建置秒數，比 09-28 記的 1,850 秒多 17%，單點不構成趨勢。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅                                                    |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                         |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary`（見下） |

## Handoff 三態

繼承 `2026-09-28-061044-twmd-data-refresh-am` 與 `2026-09-29-055718-twmd-embeddings-nightly`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 Write session 帶哲宇 review；OBSERVER-QUEUE #75〜#90（待決）本班不動。
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04，動得了 `scripts/tools/`）— `routine-sync.py` 對賬前 `git fetch`、有差非 0 exit；讀 live-state 時印鏡像新鮮度（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，席位 `/twmd-routine`，動得了 routine prompt）— 本 routine Stage 1.5 寫明「pipeline 開跑前先跑」。今天第三班照這個順序排對，prompt 仍只寫「每次必跑」。
- [ ] pending（延續，觀察）— build 秒數 1,850（09-28）→ 2,166（09-29），攢到三點再判（REFLEXES #76）。拉 CI 歷史：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion`。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 讓自動 gc 停擺，今天 commit 仍印 unreachable loose objects 警告（REFLEXES #35）。
- [ ] pending（觀察，LESSONS `relative-category-links-survive-link-check`）— `md-extension` 524→331→144→**289**，趨勢回頭。10-02 若仍 >200 改由 heal 腳本轉絕對路徑，席位 maintainer-am。
- [x] ~~pending（觀察，`monitor-404.py`）— 下一次條件成立時先讓 top_paths 按家族各留前 50~~ — retired by 09-28 maintainer-am `8480ab464`（每族保障前 50）。今天條件不成立，改看下一行。
- [ ] pending（延續，babel 專屬，席位 babel-nightly／babel-vortex）— 明細在 `2026-09-29-005057-twmd-babel-nightly.md`（#89 待決、自造 slug 存量 813 條），不重抄（REFLEXES #74）。

本 session 新 handoff：

- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05，動得了 `data/terminology/`）— `/terminology/變壓器` 09-27 一天 18 次 404（瀏覽器 UA），用語庫無此條；判斷要不要收成詞條，資料在 `reports/404-monitor/latest.json` top_paths。
- [ ] pending（觀察，`monitor-404.py`，席位本 routine）— unknown 56%，top_paths 只涵蓋 unknown 的 24%；若明天仍過半且榜首換成探路名，照 09-23 條件收名字，否則繼續記錄。

## Beat 5 — 反芻

今天唯一的摩擦又出在把檔案清單交給 git 那一步，連續兩天。昨天是 zsh 不拆未加引號的變數，今天我伸手去拿 `mapfile`，它在 zsh 不存在，在這台機器的 bash 3.2 也不存在。兩次都是在寫一個「以為所有 shell 都有」的語法，也兩次都在 pathspec 那道門外面失敗，什麼都沒進 git。寫進暫存檔再展開這個做法不依賴任何一種 shell 的陣列語意，明天直接用它。

404 那一格讓我停了一下。56% 這個數字單看像是昨天的修補失效，拆開後是另一件事：榜首是一個讀者在找、但我們沒有的詞，第二名以後才是掃描器。同一個 unknown 裡混著讀者需求跟探路噪音，照名字清理只會處理後者，前者要交給懂用語庫的那條 routine。

🧬

---

_v1.0 | 2026-09-29 06:1x +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步資料刷新（第二十三夜讓場）_
_誕生原因：排程 06:00 觸發；babel writer 進程在跑_
_核心洞察：(1) 14 步全綠零過期 (2) 404 unknown 榜首是讀者用語需求，不是探路名，條件不成立不動判準 (3) 路徑清單寫檔再展開，避開 zsh／bash 3.2 陣列差異_
_LESSONS-INBOX：無新條目_
