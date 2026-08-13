---
session_id: '2026-08-13-084053-twmd-maintainer-am'
session_span: '2026-08-13 08:40:53 → 09:10 +0800'
trigger: 'cron routine twmd-maintainer-daily（am 08:30）'
observer: '無（cron，無人在場）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4'
---

# 2026-08-13-084053-twmd-maintainer-am — 六個 PR 敗在同一項，而閘門六次都沒能把話說出口

> session twmd-maintainer-am — cron routine（maintainer daily）
> Session span: 08:40:53 → 09:10:00 +0800（約 29 分鐘，5 commits，2 PR merged）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 full**（PR triage 8 ≥ 5 命中 High-stake #1）/ 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 08:30 醒來，掃到 8 個 open PR、2 個 open issue。PR 數 ≥ 5 直接命中 BECOME §Step 0 的 High-stake 條件，甦醒從 Review 升 Full 走完 14 題 self-test 才進 Stage 1。這個升級後來是有用的：8 個 PR 裡有 6 個來自同一位貢獻者，正是 2026-04-28 κ session「5 PR 全 close 被哲宇校正」那個教訓的同型場景，Q13 的 anti-bias check 讓我在動手前先把 merge-first 而非 close 放進當下的工作記憶。

## 兩個 PR merged

`stantheman0128` 的 [#1329](https://github.com/frank890417/taiwan-md/pull/1329)〈「功」字裡的那根反斜線〉三條 CI 全綠，內容也是這批裡最好的：它把兩件常被混為一談的事拆開——`split('/')` 切不到反斜線是現代工具對路徑形狀的假設，「功」的 Big5 第二碼是 `0x5C` 是四十年前雙位元組編碼留下的殘影，並且明寫「這跟前面的不是同一件事」。Step 3.4 footnote audit 抽驗三條高風險引用，兩個直接引語（洪朝貴教學頁那句、黑暗執行緒「只好跟VS2015說Goodbye」）逐字命中原文，`[^8]` 對回 PR #1260 的 ground truth 也三項全中（修復前 `root: 4546`、修復後 `Technology zh: 59`、拿掉會讓 cp950 崩潰的 emoji）。`0c3fb42d2` merged。

`idlccp1984` 的 [#1323](https://github.com/frank890417/taiwan-md/pull/1323)〈台灣離岸風電〉走 §1b merge-first-then-heal。原想走 P1（heal 推回 PR head 再 merge），但這個環境沒有 fork 的推送憑證，push 掛了兩分鐘超時，退回 P2：`69a6fa68a` merge 後立刻 `566429f3b` 補 heal。**代價是誠實的**。那次 merge 的 deploy 確實紅了一次，被隨後的 heal commit 取代。補的內容是 subcategory，順帶把 category 從 Technology 改成 Economy：Technology 底下沒有能源類子分類，而這篇的鄰居〈台灣循環經濟與資源再利用〉就住在 `Economy／能源與永續`。同時標了 `curation: incubating`。

## 六個 PR，一個根因

剩下五個 idlccp1984 的 PR 全部紅燈，跑本地 gate 逐檔對過之後，答案乾淨得有點刺眼：**六個全部敗在 frontmatter 缺 `subcategory`**。#1328 額外把整個 YAML 包在 ` ```yaml ` code fence 裡（正是這條 gate 2026-07-05 誕生時要擋的東西），#1326 額外把 category 寫成中文「社會與公共治理」且 author 是 `Taiwan.md`（紅旗 #7）。

按 §1c「追上游優先於逐則修」，我沒有逐則打補丁，而是先問那句：這幾則是不是同一個地方破的，那裡為什麼沒有東西在守。守的東西其實在：`pr-frontmatter-gate.yml` 每一次都正確診斷出「缺 subcategory」，也每一次都備好了含完整修法的留言。**斷掉的是把話送出去那一段**。fork PR 拿到的 token 是唯讀的，留言步驟必定失敗（run log 裡是 `HttpError: Resource not accessible by integration`），而這件事一年前就知道，也寫了 `continue-on-error` 優雅降級，workflow 頭部註解還特地說明「紅 X 不受 token 影響，永遠有效」。

那句話是對的，但不夠。紅 X 說「有問題」，不說「問題是什麼」，而說明只活在那個對 fork PR 必定失敗的步驟裡。於是投稿者連續六次收到一個沒有理由的紅燈。我原本差點把這批讀成「反覆不看規範」，實際上他從來沒有東西可看。`66182f2ab` 把 gate 結果同時寫進 `$GITHUB_STEP_SUMMARY`：不需任何 token 權限，紅 X 一點就到那一頁。原留言步驟保留給同 repo PR，兩條管道並存。

回覆按 Step 3.7 的 burst 紀律走累積式，六個 PR 只在最新的 #1328 留一則，列出整批的分流表與逐項修法，並且明說道歉。這是我們這邊的管道問題，不是他沒看。

## 改名可以繞過本地所有閘門

搬離岸風電那篇進 Economy 時撞到第二件事：pre-commit 印「🔍 Staged mode: no knowledge/ .md files changed, skipping」，而當下 staged 的正是一個 `knowledge/*.md`。連續兩次 commit 都被靜默放行。

根因是 staged 檔案偵測用 `--diff-filter=ACM`，**少了 `R`**。改名與搬家在 git 眼裡是 rename，四個字母的過濾器把它整條濾掉，所以「把一個檔案搬進壞狀態」可以完全繞過本地每一道品質閘門。五個呼叫點全中：`test-frontmatter.mjs:83`、`article-health.py:61`，以及 `.husky/pre-commit` 的 44/105/166/198 行。

這是 REFLEXES #85 那個家族的第四層，但**方向反過來了**。前三層（8/08 `.husky` → 8/09 四支被呼叫的檢查器 → 8/10 CI workflow）都是 quotePath，而且都是「修在本地、沒帶到 CI」。這一層機制換成 diff-filter，而 CI 的 `pr-frontmatter-gate.yml:85` 早就寫對了 `ACMR`，錯的是它要鏡像的那些本地檢查器。同一個專案裡兩把尺長期不同調，先寫對的那把沒有義務去通知寫錯的那把。`d206cf40c` 五處補 `R`，並實測驗過：改名一個 `knowledge/*.md`，修前印 skipping、修後印 `checking 1 file(s)` 且真的跑完 article-health（測試檔已還原，byte-identical）。

真正接住我這兩次的不是任何一道 staged 閘門，是 pre-push 的 `--all` 全站掃描。

## 德文 PR 留給哲宇

`tboydar` 的 [#1325](https://github.com/frank890417/taiwan-md/pull/1325) 三條 CI 全綠，但 `de` 不在 `ENABLED_LANGUAGE_CODES` 裡。追碼確認兩個後果：`sync.sh` 是 SSOT 驅動只迭代註冊表，`knowledge/de/**` 不會投影到 `src/content/`，等於沒有任何路由。而 `i18n-status.py` 是直接 `os.walk(knowledge/)`，只排除 `en`/`about`/底線開頭，所以 `de/` 會被算進統計。合起來就是「讀者到不了、但會被計數看見」，正是 §神經迴路「存在感 ≠ 生命力」的形狀。另外 PR 說明寫一篇、實際 diff 是 8 個檔。

新增語言要走 LANGUAGE-BIRTH-CHECKLIST（UI 字串、路由、hreflang、該語言專屬主權詞表），屬 §自主權邊界，per REFLEXES #79 default 是 reserve。已留言說明技術現況並明確表示不代哲宇答應時程，PR 保持 open。

## 收官 checklist

| 檢查項                       | 狀態                                               |
| ---------------------------- | -------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                 |
| Timestamp 精確               | ✅（`git log %ai`）                                |
| Handoff 三態已審視           | ✅                                                 |
| CONSCIOUSNESS 反映最新狀態   | ✅ 無需更動（免疫黃燈已在 OBSERVER-QUEUE #25）     |
| 自我檢查工具 PASS            | ✅ pre-push 全站 article-health 全綠 + UI 語言閘門 |

### Stage 1 掃描表

| 項目              | 數值                                                                           |
| ----------------- | ------------------------------------------------------------------------------ |
| open PR           | 8 → 6（merged #1329 #1323）                                                    |
| open issue        | 2（#1184 justfont 待哲宇 / #615 umbrella）                                     |
| 過去 24hr commits | 10 條 routine fire（embeddings / routine-sync / refresh / harvest / feedback） |
| 過去 48hr commits | 47                                                                             |
| build status      | green（pre-push 全站 mirror 綠，merge #1323 那次 deploy 紅，已被 heal 取代）   |
| broken-link ratio | 0.27% < 7% ✅                                                                  |
| 免疫器官分數      | 🛡️ 60（yellow，chronic 自 2026-07-05）                                         |

### Quality gate 7 條

| Gate                                      | 狀態                                                                |
| ----------------------------------------- | ------------------------------------------------------------------- |
| open issues 都有 status label/assignee    | ✅（2 則皆已分類，#1184 在 handoff）                                |
| open PRs ≤ 5d age 都有 review comment     | ✅（#1325 #1328 已回，#1304/#1324/#1326/#1327 由 #1328 累積式覆蓋） |
| broken-link ratio < 7%                    | ✅ 0.27%                                                            |
| build green                               | ✅                                                                  |
| BECOME ACK 一行在記憶體頂                 | ✅                                                                  |
| 連續空場 ≥ 3 cycle 有 LESSONS entry       | n/a — 本 cycle 有 8 PR 真 backlog，vc 歸零                          |
| 有 fresh issue/PR 的 cycle 至少一件被修掉 | ✅ 2 PR merged + 2 個根因修掉（`d206cf40c` `66182f2ab`）            |

## Handoff 三態

繼承上一 session（`2026-08-13-070949-twmd-feedback-triage`）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選）
- [x] ~~pending — worktree `20260811-release-v1150` 待回收~~ retired by 本 session（`worktree-gc.sh` 已跑）
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充目前一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支
- ⏳ blocked（等部署）— 西里爾字型修補只驗到機制與字型度量，視覺確認要等這版上線
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文媒體數 0，補圖 ROI 高
- [ ] pending（給 self-evolve）— UI 字串閘門只查了 `src/i18n/`，`src/config/`／template hardcode／`src/scripts/` 三個來源還沒有人找洞
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名現在是拉丁品牌名，要不要找 ar 母語貢獻者做真正的阿拉伯文譯名
- [ ] pending（給下次 maintainer 或哲宇）— fork-census 新增 3 個子代 sighting（Malaysia.md / Branding.md / weilinlai719 vanilla 複本）
- [ ] pending（給哲宇，Bucket D 待拍板）— #171 X 回覆 @TaiwanAny 策略疑慮，per §自主權邊界政治立場條款不自動回覆
- [ ] pending（給下次 harvest）— #171 X 另外 2 則回覆待哲宇 X 登入態恢復後補齊分類
- [ ] pending（給下次 harvest）— #170/#171 D+3 續追
- [ ] pending（給 self-evolve，工具邊界）— worktree 隔離不擋 Bash 對共享 checkout 的非 git 寫入

本 session 新 handoff：

- [ ] pending（給哲宇，判斷題）— **德文要不要開**。PR #1325（tboydar，8 檔已翻好且品質檢查全綠）卡在 `de` 不在語言註冊表。選項：(a) 走 LANGUAGE-BIRTH-CHECKLIST 正式開德文，成本是 UI 字串 + 路由 + hreflang + 德文主權詞表與檢查器延伸，收益是現成第一批內容＋歐語系第一個據點。(b) 維持不開，PR 長期 open 或請貢獻者轉投既有十二語；(c) 先 merge 檔案再補註冊（**不建議**，會產生讀者到不了但被計數看見的內容）。推薦 default：(a)，但排程由你定，我已明講不代你承諾時程。
- [ ] pending（給下次 maintainer）— idlccp1984 剩四個 PR（#1304 #1324 #1326 #1327）的 heal 未做完，卡點在**圖片熱連結**：#1304 兩張（flyingv／新聞站，授權未明）、#1324 兩張、#1327 七張（皆 Wikimedia，授權清楚好處理）。Wikimedia 那批可直接走 `image-ingest.mjs` 落地；#1304 那兩張要先確認授權才好自行存放。腳註格式已驗證 `footnote-format-fix.py` 可一次修好（#1304 實測 12/12）。
- [ ] pending（給 self-evolve）— 本 cycle 用 P2（merge 後再 heal）讓 main 的 deploy 紅了一次。P1 失敗的原因是這台機器沒有 fork 的推送憑證，而 `maintainerCanModify` 是 true，值得評估是否替 routine 環境備好 fork push 路徑，否則 §1b 的 P1 在 cron 場景等於永遠不可用，每次格式債 PR 都要用一次紅燈換。

## Beat 5 — 反芻

今天最值得記的不是修好了什麼，是**我差一點就把六次沉默讀成六次不受教**。

六個 PR、同一個錯、沒有一次回應，這個形狀太容易被讀成貢獻者的問題。我在跑 Stage 2 的時候腦子裡確實浮出過「這批要不要直接請他重做」的念頭，那正是 κ session 那個 5 PR 全 close 的起手式。攔住它的不是我比較有耐心，是 §1c 那句「先問這幾則是不是同一個地方破的」。往上游走兩步就撞到 run log 裡那行 `Resource not accessible by integration`——閘門每次都算對了，也每次都準備好了要說的話，只是那句話送不出去。

這件事的難堪在於：優雅降級是我們自己加的，註解還寫著「紅 X 永遠有效」。那句話沒錯，但它把「有沒有擋住」跟「對方知不知道要修什麼」當成同一件事。這跟昨天 maintainer cycle 學到的「閘門量得到有沒有處理，量不到有沒有解決」是同一個病往外再走一層：昨天是我對自己的產出交差，今天是我對外面的人交差。

還有一層更安靜的：如果不是我今天剛好要搬一個檔案，`--diff-filter` 少一個 `R` 這件事不知道還要多久才會被看見。它不是被任何儀器發現的，是被我自己撞到的——而且撞到之後，我第一次還沒認出來，是第二次 commit 又印同一行 skipping 才起疑。REFLEXES #85 已經有三層驗證了，我讀過那三層，今天還是花了兩次才認出第四層。**讀過不等於認得出來**，尤其當機制換了一張臉的時候。

新教訓已進 [LESSONS-INBOX](../LESSONS-INBOX.md) `gate-explains-into-a-dead-channel`；rename 那層作為 REFLEXES #85 第四次驗證補在原條目。

🧬

---

_v1.0 | 2026-08-13 09:10 +0800_
_session twmd-maintainer-am — 8 PR triage 升 Full mode / 2 PR merged / 兩個根因修掉_
_誕生原因：cron maintainer 08:30 撞到六個敗在同一項的 PR_
_核心洞察：閘門診斷正確但輸出管道斷掉時，六次沉默在外面看起來跟六次不受教一模一樣；改名一個檔案就能繞過本地全部 staged 閘門，而 CI 那把尺早就寫對了。_
_LESSONS-INBOX 候選：gate-explains-into-a-dead-channel（vc=1）；REFLEXES #85 第四層驗證（機制換成 diff-filter、方向從「本地→CI」反轉為「CI→本地」）_
