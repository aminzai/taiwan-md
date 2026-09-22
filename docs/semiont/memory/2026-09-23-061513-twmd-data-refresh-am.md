# 2026-09-23-061513-twmd-data-refresh-am — 第十八夜讓場 14 步全綠零 stale；404 探路檔名收進掃描器，routine 面板遲一天的成因找到並當場修掉

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:15:13 → 06:22:00 +0800（2 commits `ad9167e9c` + 本篇收官）
> 資料來源：`git log %ai`

## 觸發

排程 06:00 觸發。任務三段：跑 14 步 ground truth 刷新、scheduler live-state 落檔、Step 11 freshness gate 的 catch ≠ fix 處置。

## 甦醒

`/twmd-become micro` 走完 Step 0-9。`wake-context.py` 落檔 265,727 bytes，用 Read 分頁讀到末行 `wake:END` sentinel，11 項體檢全綠。即時器官分數 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐89，最低是免疫 59（`review_coverage` 19，黃燈自 07-05）；快照自身標 stale 23h，是 refresh 之前的正常狀態。Q14：過去 48 小時幾乎整片是統一調度器的十二語 babel 批次，穿插 babel-nightly 當夜把正文網址改由工具持有、殘留佔位符補閘門、量出 87% 譯文出自白名單外的 8.1B 模型；另有 routine-sync 第 57 輪把 babel-nightly 的機器殼補上白名單落差警語。觀察者 09-19 最後在場（handle golden-bell-v2），mode=present。

## Step 1 讓場（第十八夜）

`check-parallel-actor.sh` 回 `ACTOR_BUSY`，babel dispatcher 98122 帶五個 worker 正在寫工作樹（37 個檔案 dirty）。先 `git fetch` 量到本機領先 1、落後 0，那一個領先是 babel 剛落的批次；Step 1 的 stash 會把 dispatcher 手上的檔案抽走，而 pull 又拉不到東西。照前十七夜的做法切 header 與 Step 2 以後組 runner，`bash -n` 過語法，並確認第 115 行之後零引用 `DIRTY` / `PULL_OK` / `STASH_LABEL` 三個只屬於 Step 1 的變數。

## 14 步結果

三源全綠：CF 七天 4,640,366 requests、404 率 1.03%（前夜 1.07%）、AI crawler 213,667 次跨 18 家（前夜 206,756）；GA4 與 SC 各 20 筆 top。`_translations.json` 12,801 筆零孤兒（前夜 12,697，babel 一夜補了 104 條）。spore records 166 篇 unchanged、dashboard-spores 0 warnings；immune v2 維持 **59**，`external_rulers` 3.6 → 3.5；fork-census 0 新 sighting；llms.txt zh 1122／en 1106／ja 1056（前夜 1045）／ko 1104／es 1107／fr 1108；GitHub ⭐1187 🍴187 👥75 📄1122；newsroom 222 篇上板 17 warnings；build perf ms/page **158**（前六夜 125→138→136→139→143→158，最新 build 2099 秒）；reports/INDEX.md 722 行。

Step 11：14 個 `dashboard-*.json` 全部今日 mtime，analytics 內容對齊 UTC 今日，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors／0 warnings，Step 13 no-op，Step 14 重生。

Stage 1.5：`list_scheduled_tasks` 18 條（14 enabled + 4 disabled），`routine-live-normalize.py` 落 `routine-live-state.json`，過濾 0 條私人 routine。

## 404 的探路檔名：交接立的條件成立，當夜收掉

09-22 的交接寫了一個條件：若 unknown 連兩夜過半、且榜首換成探路檔名，就把這族收進掃描器判準。今晚兩個條件同時成立，unknown 2,252 佔 57%，榜首是 `/config.yml`。下面整族是框架預設路徑與設定檔名：`/configs/application.ini`、`/debug/vars`、`/actuator/env/spring.cloud.config.token`、`/v1/graphql`、`/telescope/requests`、`/docker-compose.yaml`、`/id_rsa`、`/payment_gateways/stripe.yaml`，沒有一條是站上路由。

判準只收今天有證據的名字，沒有放寬成通配。動手前先驗尺：對 `public/api/articles.json` 的 27,850 條真實路由字串零誤判，也不從其他家族搶件（兩條命中的本來就已經是 scanner）。同一份快照上 23 條路徑、300 筆命中從 unknown 移進 scanner，unknown 佔比 52.8% → 46.2%，首次落到半數以下。

中途自己踩了一次尺的問題。查「站上有沒有發出這種連結」時寫了 `grep -rl ... | head -5 && echo "emitted"`，`head` 沒有命中也回 0，於是 shell 替我印出了「有」。改成數數才看見真相是 0。

**同一個日期的 404 總數不是一個穩定的數**：09-21 在 06:0x 查到 3,935，25 分鐘後再查是 4,533，之後連兩次都穩定在 4,533。歷史日期一旦寫進 `state.json` 就不再變（09-20 前後都是 3,123），所以每天的數字等於「那天是哪一刻被查的」，跨日比較帶著一個查詢時點的誤差。因為這件事，commit 訊息裡的佔比改成同一份快照的 52.8% → 46.2%，沒有拿 06:0x 的 57% 去跟後來的 46% 相減——那會把改善說大一倍。

## routine 面板遲一天：成因在步驟順序

`dashboard-status.json` 的 routine 區今晚標了 2 條 degraded（本 routine 自己與 embeddings），比前夜多一條。前幾個 cycle 都把它記成「量測時機問題」放過去，今晚進去看順序：`generate-dashboard-status.mjs` 讀 `docs/semiont/routine-live-state.json`，而那個檔案只有 session 層的 Stage 1.5 能寫（bash 進不了 MCP store），Stage 1.5 卻排在 bash pipeline 的 Step 6.6 之後。於是面板每天都是拿昨天的 live-state 蓋今天的章，剛跑完的 routine 看起來像 24 小時沒動，被判 degraded。

Stage 1.5 跑完後手動重生一次，`stale_hours` 24 → 0.1，embeddings 那條假警報消失。剩下的一條是本 routine 自己，成因不同也無法在自己的 run 裡解決：`last_fire` 的尺是 memory 檔（REFLEXES #82 的「fire 之後有沒有落檔」），而今天的 memory 檔正是這一步在寫。本篇 commit 後再重生一次就會轉綠。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅                                            |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                 |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary` |

## Handoff 三態

繼承 `2026-09-23-054243-twmd-routine-sync`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註，已擴散 12 語）仍 OPEN，等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板（ROUTINE.md 註 ¹³），本輪 live-state 對賬一致，未擅自打開。
- [ ] pending（延續，席位已釘 09-27 `twmd-self-evolve-weekly`，第 5 輪往下傳）— `routine-sync.py` 對賬前 `git fetch`，routine 層與 `origin/main` 有差時印一行並 exit 非 0（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`、REFLEXES #67 子規則）。本班不做的理由不變：commit 範圍鎖本 routine 檔案，改 `scripts/tools/routine-sync.py` 越界。
- [ ] pending（延續，同席位 09-27）— `routine-sync.py` 的 `load_live()` 讀不到或讀到舊鏡像都不吭聲，應印鏡像 mtime 並在超過 24 小時標 ⚠️（REFLEXES #82／#85）。本輪 live-state 由本班當場重寫，鏡像是新的。
- [x] ~~pending — 單檔收官改 `git commit -- <path>`，避免 `git add` 到 `commit` 之間被 babel 的 commit 掃走存證檔~~ — 本班採用並驗證有效：38 個檔案全程用 pathspec commit，期間 babel 另有 commit 落地且有一份 embeddings memory 檔正掛在 index 上（`MM`），pathspec 形式讓它沒有被捲進來，`verify-commit-scope.sh --head 38` 過。建議寫進 routine prompt 第 6 步當固定做法。

繼承 `2026-09-22-060315-twmd-data-refresh-am`：

- [x] ~~pending（觀察，`monitor-404.py`）— 若 unknown 仍 >50% 且榜首換成探路名，把 `.zip`／`.bak`／`.tfvars`／`.config.js` 收進 scanner 判準~~ — retired by 本班 `ad9167e9c`，條件成立當夜做掉，實際收的名字比交接列的更貼近今天的證據。
- [ ] pending（延續，本輪再加一個數據點）— build perf ms/page 125→138→136→139→143→**158**，七夜內從 112 漲到 158，最新 build 2099 秒。可執行動作不變：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion` 拉 CI 歷史找 ms/page 起跳那天（REFLEXES #41 CI capacity 是會跟內容量長大失效的設定）。這條已連四輪往下傳，建議下一個 Review 或 Full mode session 認領。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 存在讓自動 gc 停擺；平行 writer 期間不動（REFLEXES #35）。

本 session 新 handoff：

- [ ] pending（1-file，`scripts/tools/refresh-data.sh` 或本 routine prompt）— **Step 6.6 `generate-dashboard-status.mjs` 排在 Stage 1.5 之前，面板永遠拿昨天的 live-state**。今晚手動重生後 `stale_hours` 24 → 0.1、一條假 degraded 消失，但下一輪會原樣復發。兩個修法：把 Step 6.6 從 `refresh-data.sh` 移出、改由 session 在 Stage 1.5 之後呼叫；或在 routine prompt 的 Stage 1.5 末尾固定補一行 `node scripts/core/generate-dashboard-status.mjs`。後者 1-file 且不動 bash pipeline，建議先走。對應 REFLEXES #43（新 generator 要有自動 refresh path，這條是「有 path 但排錯位置」的變體）。
- [ ] pending（觀察，`monitor-404.py`）— **unknown 降到 46.2% 後，榜上剩兩種形狀**。一種仍是探路檔名但今晚才出現（`/helm/values.yaml`、`/chart/values.yaml`、`/ses.json`、`/app/etc/local.xml`，本輪已一併收進判準）；另一種是 `/terminology/{中文詞}` 與 `/{lang}/{category}/{English Title}`，要先判是外部 bot 拼的還是我們曾經發出過的連結，不宜直接歸類。
- [ ] pending（需判斷，非本班可決）— **重複語言前綴的 404：`/arar/`、`/koko/`、`/idid/`、`/ptpt/`、`/frfr/`、`/hihi/`、`/eses/` 共 81 條路徑、243 筆命中，UA 全部是瀏覽器，後面接的都是真實 slug**（`/arar/people/li-ang`、`/koko/society/hahatai`）。已驗不是我們發的：`dist` 14,457 份 HTML 零命中，`_redirects` 201 條無此形狀，原始碼無字面。所以是外部（很可能是翻譯代理或某個把 `{lang}{lang}` 當 locale 拼的客戶端）。值得決定的是要不要補一條 `^/(ar|ko|id|pt|fr|hi|es|ja|en|vi|ru|de)\1/` → `/$1/` 的 301：這些是帶著真實 slug 的真人瀏覽器，接回來就是接回讀者，但它同時會把一個外部錯誤變成我們永久維護的相容層。重現指令：`python3 -c` 讀 `reports/404-monitor/latest.json` 過濾該 regex。

## Beat 5 — 反芻

今晚兩件事都是把「已經被看見但沒被動手」的東西收掉，而它們被放過的理由不一樣。404 探路檔名那族是前一班寫了條件式交接，條件寫得夠具體（連兩夜過半、榜首換成探路名），今晚一對就成立，於是沒有重新發現的成本，直接做。routine 面板那條相反：它連續幾個 cycle 被寫成「量測時機問題」，那句話本身是對的，但它同時是一個讓人不必往下看的解釋——命名一個現象會讓它顯得已經被處理過。今晚只多問一句「時機問題的時機是誰決定的」，就看到是步驟順序，而且順序錯得很規律：唯一能寫那個檔案的步驟，排在唯一會讀它的步驟後面。

兩件事放在一起看，差別在交接寫的是條件還是結論。寫條件的那條帶著「什麼時候該動手」，下一班只要對一次；寫結論的那條帶著「這件事已經理解了」，下一班讀完就過去了。前十七夜的面板每天都遲一天，而每天都有一個人看著它、寫下一句合理的解釋。

自己踩的那個 `head` 也是同一個形狀。我要的是「站上有沒有發出這種連結」，工具回的是「這個指令有沒有跑完」，而兩者長得一模一樣，因為我讓 shell 替我下了結論。尺先驗再用這條，今晚在 404 判準上記得（先跑 27,850 條真實路由的正控制），在旁邊那個隨手的查證上就忘了——想起要驗的是那把正在造的尺，順手拿來看一眼的那把不算。

🧬

---

_v1.0 | 2026-09-23 06:22 +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步 ground truth 刷新（第十八夜讓場）_
_誕生原因：排程 06:00 觸發，babel dispatcher 仍在寫工作樹_
_核心洞察：命名一個現象會讓它看起來已經被處理過，於是面板遲一天遲了十七夜；同一個日期的 404 總數取決於哪一刻查它，跨日比較帶查詢時點誤差。_
