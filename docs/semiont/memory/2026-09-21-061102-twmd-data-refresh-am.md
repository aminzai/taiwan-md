# 2026-09-21-061102-twmd-data-refresh-am — 第十六夜讓場 14 步全綠零 stale；探憑證的 404 路徑歸進掃描器家族；剩下的 unknown 長尾浮出一個自家斷鏈家族

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:10:03 → 06:21:00 +0800（約 11 分鐘，1 commit `0794810dd`，另兩個 babel commit 隨本班一起推上 origin）
> 資料來源：`git log %ai`

## 觸發

排程 06:00 觸發。任務三段：跑 14 步 ground truth 刷新、scheduler live-state 落檔、Step 11 freshness gate 的 catch ≠ fix 處置。

## 甦醒

`/twmd-become micro` 走完 Step 0-9，`wake-context.py` 11 項體檢全綠，落檔 266,936 bytes 用 Read 分頁讀到 `wake:END`。即時器官分數 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐89，最低是免疫 59（review_coverage=19，黃燈自 07-05）。Q14：過去 48 小時是統一調度器的十二語 babel 批次（每十篇一 commit）穿插排程心跳的事實巡邏第十二到第二十三篇（李登輝康乃爾演講題目與引語是填的、海廢快篩掛錯機構、黑熊篇零錯）、W38 週體檢、蒸餾三條新反射、self-evolve 給交接量年齡、supporters 第六輪零候選但升 OBSERVER-QUEUE #75。觀察者 09-19 在場（handle golden-bell-v2），mode=present。

## Step 1 讓場（第十六夜）

`check-parallel-actor.sh` 回 `ACTOR_BUSY`：babel dispatcher 主進程 98122 已跑五小時十三分，四個 worker 在翻 es／hi／ru／de。照前十五夜的做法從 `refresh-data.sh` 切 header 加 Step 2 以後組 runner，`bash -n` 過語法，後段零引用 `DIRTY / PULL_OK / STASH_LABEL`。先 `git fetch` 量到 HEAD 領先 origin 兩個 babel commit、落後零，所以跳過的 pull 本來也拉不到東西，讓場成本仍然是零。

## 14 步結果

三源全綠：CF 七天 4,402,550 requests、404 率 1.28%、AI crawler 200,747 次跨 18 家（前夜 181,210）；GA4 與 SC 各 20 筆 top。`_translations.json` 12,665 筆零孤兒、零變動。spore records 166 篇 unchanged、dashboard-spores 0 warnings；immune v2 維持 **59**，`external_rulers` 3.6（前夜 2.6，巡邏查核檔又多了三篇）；fork-census 0 新 sighting；dashboard-status 18 routines（13 operational／1 degraded／4 disabled，0 down，degraded 那條照例是本 routine 自己，量測時機問題）；llms.txt zh 1122／en 1106／ja 1038（前夜 1033）；GitHub ⭐1185（+3）🍴186 👥75 📄1122；newsroom 222 篇上板 17 warnings；build perf ms/page 139（前四夜 112→125→138→136，又回到 138 附近，最新 build 1848 秒）；reports/INDEX.md 722 行。

Step 11：14 個 `dashboard-*.json` 全部今日 mtime，analytics 內容 2026-09-20 對齊 UTC 今日，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors／0 warnings，Step 13 no-op，Step 14 重生。

Stage 1.5：`list_scheduled_tasks` 18 條（14 enabled + 4 disabled），`routine-live-normalize.py` 落 `routine-live-state.json`，過濾 0 條私人 routine。

## 404 的 unknown 家族：拆掉一半，另一半浮出自家的病

monitor-404 記 2026-09-19 總 404 **5,993**，前一日 2,891，翻了一倍。`unknown` 3,983 筆佔三分之二，代表路徑 `/.docker/secrets.json`，往下看是 `/.gitlab-ci.yml`、`/s3.secret`、`/aws/config/s3.json`、`/credentials.yml`、`/.netrc`、`/.gitconfig`、`/client_secret.json`、`/localhost.key`——跟前三天的 `/inc/data/database.sdb`、`/login`、`/credentials` 是同一批探憑證的流量。這條 handoff 已經被三班原樣往下傳，今天第四次撞到就順手做掉（1-file）：`monitor-404.py` 的 `SCANNER_RE` 補根目錄 dotfile（明確排除 `.well-known/`，它有自己的家族且判定順序在掃描器之後）、`secret`／`credential`、`.key`／`.pem`／`.sdb`、`/aws/`、`/login` 與幾個常見設定檔名。重跑後 scanner 805→1,122，unknown 3,983→3,671。

只移走 312 筆，因為 `latest.json` 只存 top 300 路徑，這 300 條裡的 unknown 加起來 1,157，其餘 2,500 筆是三筆五筆的長尾，看不到。但 top 300 裡剩下的 unknown 有兩個形狀值得記：一是 `/ptpt/…`、`/arar/…`、`/idid/…`、`/hihi/…`、`/enen/…`、`/eses/…` 雙語言前綴，每條六七筆，grep 過 `articles.json`、`lang-switch-map.json` 與 `dist/` 都零命中，是外面的 bot 自己拼壞的，不是我們發的連結。二是 `/{lang}/history/History/台灣鐵道史` 這種「小寫分類再接大寫分類再接中文 slug」，十二個語言各七到九筆，這個是我們自己的：西螺大橋那篇 zh 母稿的延伸閱讀寫成 `../History/台灣鐵道史` 相對路徑，瀏覽器從 `/en/history/xiluo-bridge/` 往上解析就變成 `/en/history/History/台灣鐵道史`。全庫量了一下：12 篇 zh 母稿有這種相對連結（造山者、誠品、AAMA、玉山氣象站、西螺大橋、蔡英文、林啟維、木曜4超玩、蔡健雅等），巴別塔忠實地把它放大成 12 語 129 份譯文、405 條連結，zh 本身也是 404。`verify-internal-links.sh` 沒抓到它，因為它查的是絕對路徑。修法在母稿那 12 篇（改成 `/history/slug` 絕對路徑），譯文等 source sha 變了由 babel 自己追；129 檔超過 §自主權邊界，且母稿修完譯文會自動 stale，本班只登記不動手。

## Commit 與推送

只 stage 本 routine 的 36 個檔案（排除 dispatcher 在寫的 `reports/babel/*.json` 與 27 篇多語 `knowledge/*.md`；`knowledge/_translation-status.json` 是 prebuild 重生的，跟前夜一樣當本 routine 產出），`verify-commit-scope.sh --staged 36`／`--head 36` 都過，commit `0794810dd`。pre-push 看到一個跑了 1,212 秒的 in-flight deploy，超過 900 秒窗口依 latest-wins 放行，`57ea9472d..0794810dd` 上 origin，連同 dispatcher 那兩個 babel commit 一起推。`gh run list` 對賬：前夜 handoff 提到的 04:26 OIDC 逾時之後六個 deploy 是 success／cancelled 交替，沒有第二次 failure，那條 GitHub Pages 側連續故障的觀察結案。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅                                            |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                 |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary` |

## Handoff 三態

繼承 `2026-09-21-053759-twmd-routine-sync`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板（ROUTINE.md 註 ¹³）。
- ⏳ blocked（延續）— issue #1733（用語庫「消息」判定）等維護者判斷。
- [ ] pending（延續，1-file 工具候選，第 3 輪原樣往下傳）— `routine-sync.py` 對賬前 `git fetch`，routine 層與 `origin/main` 有差時印一行並 exit 非 0（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`，REFLEXES #67 子規則）。

繼承 `2026-09-20-061851-twmd-data-refresh-am`：

- [ ] pending（延續，本輪補一個數據點）— build perf ms/page 112→125→138→136→**139**，在 138 附近打平；`dashboard-build-perf.json` trend 視窗仍只有 1.2 天。可執行動作不變：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion` 拉 CI 歷史找 ms/page 起跳那天（REFLEXES #41 CI capacity）。
- [x] ~~pending（1-file 候選）— `monitor-404.py` 的 `unknown` 家族連三天 55-62%，探路型路徑加進 scanner 判準（REFLEXES #38）~~ — retired by 本班 `0794810dd`，第四天撞到才做掉（REFLEXES #15 第 13 次驗證的形狀）。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 存在讓自動 gc 停擺，本輪 fetch／commit／push 各印一次「too many unreachable loose objects」；平行 writer 期間不動（REFLEXES #35）。
- [x] ~~pending（觀察）— 04:26 self-evolve 的 deploy 是 GitHub OIDC ID token 逾時，若下一班看到第二次同因 failure 才是 Pages 側故障~~ — retired：之後六個 deploy 無 failure，一次性事件。

本 session 新 handoff：

- [ ] pending（maintainer-am 或任何 Micro session，12 檔 zh 母稿）— 12 篇 zh 母稿延伸閱讀寫 `../Category/中文slug` 相對路徑，站上解析成 `/{cat}/{Cat}/中文` 404，巴別塔放大成 12 語 129 份譯文 405 條（09-19 單日 CF 上每語七到九筆）。清單：`grep -rlE '\]\(\.\./[A-Z][a-z]+/' knowledge/*/ | grep -vE '^knowledge/(en|ja|ko|es|fr|de|ru|ar|pt|hi|id|vi)/'`。改母稿為 `/history/…` 絕對路徑後譯文由 babel 依 source sha 自動追；順手讓 `verify-internal-links.sh` 認相對路徑（LESSONS 候選 `relative-category-links-survive-link-check`）。
- [ ] pending（觀察，不需動作）— `monitor-404.py` 的 `latest.json` 只存 top 300 路徑，unknown 3,671 筆裡 2,500 筆在 300 名以外看不到；若 unknown 連兩夜仍 >50%，考慮讓 `top_paths` 按家族各留前 50（REFLEXES #38 零維度變體：看不到的長尾跟「沒事」長得一樣）。

## Beat 5 — 反芻

那條「探路路徑加進 scanner 判準」的交接，昨天 self-evolve 剛量出交接的年齡，今天它就以自己為例：三班讀到、三班原樣傳下去，第四班做掉，花了不到十分鐘。做掉的理由跟前三班不做的理由一樣充分——都是 Micro mode、都是 1-file——差別只在今天 unknown 翻了一倍，數字大到讓我去看它裡面是什麼。看了才發現那個 `unknown` 是兩種東西疊在一起：外面的人在探我們的憑證，跟我們自己把相對路徑翻成十二種語言。前者歸類就好，後者是母稿的病被巴別塔放大，跟四天前那條「未審初稿的幻覺放大到十二語」是同一個形狀，只是這次放大的是一個 `../`。修 regex 花了三分鐘，量出 129 檔用了五分鐘，把它登記進交接又是一條要靠下一次被絆到才會落地的東西。

🧬

---

_v1.0 | 2026-09-21 06:21 +0800_
_session twmd-data-refresh-am — 第十六夜讓場 14 步全綠零 stale；探憑證 404 歸進 scanner；unknown 長尾浮出 12 篇母稿相對路徑被巴別塔放大成 129 檔_
_誕生原因：cron 06:00 每日資料刷新_
_核心洞察：(1) 交接落地的觸發是數字變大讓人去看，不是讀到交接本身 (2) 一個 unknown 家族裡疊著「外人探憑證」與「自家相對路徑」兩種根因，前者歸類、後者是母稿的病 (3) 巴別塔放大的不只是幻覺，一個 `../` 也放大成 405 條斷鏈_
_LESSONS-INBOX 候選：`relative-category-links-survive-link-check`（相對路徑延伸閱讀躲過 verify-internal-links，經巴別塔放大 12 語）_
