---
session_id: '2026-08-08-071725-twmd-feedback-triage'
session_span: '2026-08-08 07:00 → 07:35 +0800'
trigger: 'cron routine twmd-feedback-triage（每天 07:00 Asia/Taipei）'
observer: 'none（cron，無人值守）'
beat_coverage: 'Beat 1 診斷 / Beat 3 執行 / Beat 4 收官 / Beat 5 反芻'
---

# 2026-08-08-071725-twmd-feedback-triage — 隊列空第八天，手動核 61 份紀錄核出「抓不到」與「沒有」共用同一個回傳值

> session twmd-feedback-triage — cron routine，無觀察者在場
> Session span: 07:00:00 → 07:35:00 +0800（約 35 分鐘，1 commit）
> 資料來源：`git log %ai` + Supabase REST 直查 + GitHub API 逐 issue 核對

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 60（自 2026-07-05 黃燈）/ Q13=PASS / Q14=PASS

## 觸發

每天 07:00 的讀者回報轉 issue 例輪。Supabase `status='new'` 是空的——**連續第八天**。隊列空的日子，這條 routine 真正的工作落在它的另一半職責：主權層那 61 份 git 紀錄的健康。

## 三邊帳對得起來，但那只是第一層

`triage.mjs` 印 `file=0 reject=0 skip=0 hold=0`、`archive-reconcile=61/61 ✅`。這是昨天（8/07）剛補上的 HG12b 第一次在乾淨狀態下報數，不是它誕生那天的 40/61 破口。

自報的數字不當結論用（REFLEXES #69）。直接打 Supabase REST 拿三個 status 的 count：`new=0` / `filed=61` / `rejected=2`。加上磁碟上 `find` 出來的 61 個檔，三邊互相對得起來——隊列真的是空的，不是 fetch 條件寫錯把新回報濾掉了。

## 手動核留言，核出一個「壞掉跟正常長得一樣」的回傳值

`archive-comments-synced=0` 這個數字沒有另一邊的帳。所以逐份紀錄抽出 `issue_number`、打 GitHub API 拿每個 issue 的實際留言數，跟檔案裡 `<!-- comment: -->` marker 的數量比。30 個 issue 裡 29 個對得上，一個對不上。

對不上的那個是 [issue #1252](https://github.com/frank890417/taiwan-md/issues/1252)，archive 有 4 則、線上只有 3 則。讀完全文才知道是什麼事：7/25 早上回錯（說讀者把張寶成寫錯成張又升），7/25 下午更正（兩個署名是同一個人，錯的是我），7/29 有一輪又把更正**前**的舊版問題重貼了一次，7/31 道歉並重述正確狀態。之後 7/29 那則錯的在 GitHub 被刪掉，git 這邊四則全留著。**主權層做的正是這件事**，所以這個方向不該報警。

查的過程本身帶出了更要緊的東西。翻 `fetchIssueComments()` 的實作，所有失敗一律 `return []`：`gh` 不在 PATH、token 過期、API 變形、rate limit，全部變成「這個 issue 沒有新留言」，於是 `synced` 不加，收官印 `archive-comments-synced=0`。把 `gh` 移出 PATH 實跑一次完整 `--commit` 驗證，那一行輸出跟健康的那一次**逐字相同**。故障被編碼成了一個合法的健康讀數。

跟昨天補的 HG12b 是同一種病低一層。HG12b 對的是「該有幾份紀錄」。紀錄**裡面**的 §溝通紀錄自己那條線，一直沒有帳在比。

## 修法：先讓「不知道」有自己的符號，再拿線上的帳來比

根因分層改在取數端：`fetchIssueComments()` 抓不到回 `null`、真的沒留言才回 `[]`，`null` 時不寫檔（不確定就不動 git 紀錄）。接著 `reconcileComments()` 與 `countArchivedComments()` 兩支純函式進 `archive.mjs`，收官多印一行 `comment-reconcile=N/M`，三個方向分開報：archive 比線上少是漏收（破口，要叫）、archive 比線上多是上游刪了留言而 git 留住（正常，記錄不報警）、抓不到是 unknown（不准讀成對得起來）。

反向驗證這道閘門真的會變紅（REFLEXES #52）：`gh` 移出 PATH 重跑，輸出從 `comment-reconcile=60/61 · 上游已刪留言 1 份紀錄,git 留著: #1252 ✅` 變成 `comment-reconcile=0/61 · ⚠️ 抓不到留言 61 份紀錄（未對賬,不等於對得起來）`。單元測試 46 個全過，其中 6 個是本輪新增，含 #1252 那個形狀跟 `gh` 掛掉那個形狀。

HG12c 同波寫進三層：pipeline canonical v1.4、repo 薄殼 skill、機器上的 cron mirror。三層一起改是因為今晨 `twmd-routine-sync` 才剛抓到 8/6-8/7 兩波聲稱同步了 cron mirror、實際 git 那份沒收——changelog 說同步了不等於三層真的收了。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅（`git log %ai` + `date`）                          |
| Handoff 三態已審視           | ✅                                                    |
| HG2 issue body 無 email      | ✅（本輪 0 筆 file，61 份既有紀錄零 email）           |
| HG11 機器身份                | ✅ `ghs_` App token，`issues:write` + `metadata:read` |
| HG12 archive 落 git          | ✅（本輪無新增紀錄，既有 61 份在 git）                |
| HG12b `archive-reconcile`    | ✅ 61/61                                              |
| HG12c `comment-reconcile`    | ✅ 60/61（1 份為上游刪留言，git 留著）                |
| 單元測試                     | ✅ 46/46                                              |

## Handoff 三態

繼承（非本 session 新產生，接住不動）：

- [ ] pending（給哲宇）— #1184 justfont 後台網域白名單、免疫黃燈連 28+ 天且三選一待拍板
- [ ] pending（給哲宇）— cron 環境無 Gmail MCP（supporters-weekly checkpoint 停在 2026-07-12）
- [ ] pending（給哲宇）— 黃崇仁 #165/#166 Bucket D「是否洗白」框架質疑待拍板
- [ ] pending（給哲宇）— Discussion #104 對外合作建議，已回覆告知需哲宇拍板，尚待回應
- [ ] pending（給哲宇，最高優先，連續第 4 天）— Chrome MCP 擴充功能完全連不上，spore-harvest 連四天中止
- [ ] pending（繼承不動）— 本機 `dist/` 只在有人手動 build 時才更新
- [ ] pending（給下次碰 EMBEDDING-PIPELINE.md 的 session，vc=2）— Stage 3 commit template co-author 行寫死跟實際 cron 模型不符
- [ ] pending（繼承，8/5-8/7 累積未 ship）— 3 則 Bucket E reply draft 待 Chrome MCP 恢復後補發

本 session 新 handoff：

- [x] ~~HG12c 留言層對賬缺儀器~~ — 本輪當場儀器化並三層同步，retired by 2026-08-08-071725
- [ ] pending（給任何碰 `article-health` 輸出契約的 session）— 8/07 的 `check-disabled-by-default-reports-green` 跟本輪的 `error-and-emptiness-share-one-return` 是同一個形狀的兩端（一個在檢查器輸出、一個在取數輸入）。兩條合起來可能夠一條獨立反射：「不知道」必須有自己的符號，不能借用「沒事」那個。留給 self-evolve-weekly 判斷要獨立升還是折進 REFLEXES #38。
- [ ] pending（給下次 twmd-feedback-triage）— 隊列空第八天。空的日子把餘裕用在主權層對賬這個模式，兩天各補一道閘門（8/07 HG12b、8/08 HG12c），下一輪該問的是這條線上還有哪一層沒有帳在比，而不是預設再找一道閘門補。

## Beat 5 — 反芻

今天這道閘門是我自己拿 GitHub API 一個一個 issue 核出來的，儀器沒有叫。查完才想起來，8/06 那一輪也做過同樣的手動跨源核，memory row 上還留著一句「拿 GitHub API 跨源核過」。

兩個獨立的 cycle、兩次同樣的手工，中間沒有任何東西記得這件事該被儀器化。手動核過一次會留在 memory，留不進管線裡。REFLEXES #15 那句「memory 是自律，canonical gate 才是閘門」，這次是在我自己身上又驗證了一遍，而我能發現它的唯一原因是剛好回頭看了昨天的自己在做什麼。

比較不安的是另一件事。這條 routine 每個 cycle 都印 `archive-comments-synced=0`，那個 0 在健康時跟壞掉時逐字相同。如果 `gh` 是在某個安靜的早晨壞掉的，我不會在任何一天發現，因為每一天的輸出都長得跟前一天一樣正常。8 週前 HG12b 那個破口就是這樣活下來的。今天補的是同一種洞的另一層，我沒有把握這條線上已經沒有第三層。

教訓已 append [LESSONS-INBOX](../LESSONS-INBOX.md) `error-and-emptiness-share-one-return`（vc=2）。

🧬

---

_v1.0 | 2026-08-08 07:35 +0800_
_session twmd-feedback-triage — cron 例輪，隊列空第八天，主權層留言層對賬儀器化_
_誕生原因：隊列空的日子手動拿 GitHub API 核 61 份 archive 紀錄的留言完整性，核出取數層「抓不到」與「沒有」共用同一個回傳值_
_核心洞察：(1) 故障被編碼成合法的健康讀數，比量錯層更難察覺——把 `gh` 移出 PATH 跑一次，輸出跟健康時逐字相同 (2) 上游刪留言而 git 留住，是主權層正常運作，跟漏收是相反方向的事，同一道閘門必須分開報 (3) 手動核過的東西留在 memory 不會留在管線裡，這次是隔一天回頭看昨天的自己才發現已經核過兩遍_
_LESSONS-INBOX 候選：`error-and-emptiness-share-one-return`（已 append，vc=2）_
