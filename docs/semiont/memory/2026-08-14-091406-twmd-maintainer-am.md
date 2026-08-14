---
session_id: '2026-08-14-091406-twmd-maintainer-am'
session_span: '2026-08-14 08:30 → 09:20 +0800'
trigger: 'cron routine twmd-maintainer-daily（am 08:30）'
observer: '無（cron，無人在場）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4'
---

# 2026-08-14-091406-twmd-maintainer-am — 八個 PR 敗在同一項，而那一項是我們自己的說明書漏寫的

> session twmd-maintainer-am — cron routine（maintainer daily）
> Session span: 08:30 → 09:20 +0800（約 50 分鐘，18 commits，10 PR merged）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 full**（PR triage 12 ≥ 5 命中 High-stake #1）/ 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 08:30 醒來掃到 12 個 open PR、2 個 open issue。PR 數遠超 5，甦醒從 Review 升 Full 走完 14 題 self-test 才進 Stage 1。12 個裡有 8 個來自 `idlccp1984`、3 個來自 `ting-hong-shieh`、1 個是等哲宇拍板的德文 PR。

## 追上游追到了自己的說明書

八個 idlccp1984 的 PR 全部紅燈，逐檔跑本地 gate 之後，答案跟昨天一樣乾淨：**幾乎都是 frontmatter 缺 `subcategory`**。昨天那個 cycle 已經追過一次上游，結論是「閘門診斷對了但話送不出去」。fork PR 的 token 唯讀，留言步驟必定失敗，所以投稿者收到的是沒有理由的紅叉。昨天用 `$GITHUB_STEP_SUMMARY` 把話補上了。

但今天三個**昨天修好之後才送出**的 PR（#1333 #1334 #1335）照樣缺 `subcategory`。那就表示昨天修的不是根因，只是根因的下游。所以再往上問一次：投稿者是從哪裡學到 frontmatter 該長什麼樣？

答案在 `CONTRIBUTING.md` §內容撰寫指南的文章結構範本裡。那份請所有人照抄的範本，**從頭到尾沒有 `category`，也沒有 `subcategory`**。而 `test-frontmatter.mjs` 的註解寫得清清楚楚：這道檢查 2026-05-04 從警告升成硬性擋下。範本沒跟著改。三個月來投稿者照著我們寫的說明做，然後被我們的閘門擋下來。

昨天那層是「話送不出去」，今天這層是「話本身在別的地方就寫錯了」。閘門是對的，說明書是錯的，而沒有任何東西在對賬這兩者。

**這個洞不用我補**。`ting-hong-shieh` 的 #1332 正在做的事情裡就包含把 `category` / `subcategory` 補進那份範本，只是它掛著 draft、卡在「#1330 要先 merge」。所以今天的正解不是自己再寫一次同樣的修補，是把它解鎖：merge #1330，然後在 #1332 留言告訴他今天有八個 PR 死在他正在補的那個缺口上，請他準備好就把 draft 拿掉。

## 十個 PR merged

八個 idlccp1984 的走 §1b **P1**（heal 推回 PR 分支 → CI 轉綠 → 乾淨 merge），這是昨天沒走成的那條路。昨天的 handoff 寫「這台機器沒有 fork 推送憑證，§1b 的 P1 在 cron 場景等於永遠不可用」。**那個結論可以撤銷**。今天第一次推就成功，16 秒。昨天失敗的兩分鐘超時是暫時性的網路問題，不是結構性的權限缺口。差別是實質的：昨天走 P2 換來一次 main 紅燈，今天八個 PR 零紅燈。

修補內容除了補 `subcategory` / `featured` / `curation: incubating` 之外，幾件比較有意思的：

- **#1328 痞客邦** frontmatter 寫 Technology、檔案在 Lifestyle、subcategory 寫 `Digital Culture`，三者互相矛盾。搬到 `Culture/痞客邦.md`。同型的無名小站與巴哈姆特都住在 `Culture/網路文化`。決定 subcategory 一律用 sibling 當基準而不是用閘門的相似度建議：#1333 電視布袋戲那次閘門給的兩個候選都只有 0.47 分，而同為傳統偶戲的皮影戲就在 `工藝與美學`。
- **#1327 叭噗冰** 昨天的 handoff 寫「七張皆 Wikimedia，授權清楚好處理」。逐條開過才發現**只有一張是**。其餘四個是文化部典藏網帶浮水印 token 的 URL、兩個是數位島嶼的檢視頁而不是圖檔。那一張走 `image-ingest` 正式入庫，其餘移除。REFLEXES #16 又驗證一次：上一個 session 的 handoff 是線索不是事實。
- **#1304 沃草** 兩張外部熱連結圖授權不明。沒有 cache 到站上。把別人的圖存到自己伺服器是**更強**的侵權曝險不是更弱的，所以移除，並在回覆裡對投稿者講明這不是為了換綠燈砍內容。
- **#1324 林郁婷** 腳註格式怎麼修都會被 prettier 折回去。追下去發現正文裡躺著一行 `(Content truncated due to size limit. Use line ranges to read remaining content)`。投稿工具的截斷訊息被寫進了文章。它讓 prettier 把整條腳註當多段落處理、折斷標籤，閘門報的「格式錯」其實是這行的下游症狀。全庫掃過只有這一篇有。

`ting-hong-shieh` 的三個 PR 是高品質的系統性貢獻。#1330 加 Python CI，本機用 3.12 實跑 316 passed / 8 skipped 與他聲稱一致（第一次在 3.9 跑有 5 個 `tomllib` FAILED，是環境不是測試）。#1331 把 workflow、pre-commit、build script 裡的硬編碼語言清單全改成從 `src/config/languages` 衍生，正是 §神經迴路「語言列表硬編碼在 9 處」那條教訓的根治。它實際捕到三個在傷人的漂移：`pr-review.yml` 的清單裡有沒啟用的 `de`/`th`、少了已啟用的 `ru`。`translation-check.yml` 還在監看 `knowledge/de/**`。`build-latest.mjs` 的 `LANGS` 停在 6 語，所以 `/latest` 一直看不到 vi/id/pt/hi/ar/ru。最後這個讀者看得到。

兩個都碰 `.github/workflows/`，逐條過紅旗 #3：沒有 `pull_request_target`、沒有 secrets、沒有第三方 action、`translation-check.yml` 反而新增 `contents: read` 是收緊。#1331 直接跑它的分支有 6 個 FAILED，全落在 #1330 剛更新的 fixture 上，把 origin/main 合進來重跑 323 passed。再跑 `npm run build` 綠、sitemap 12,830 條公告 URL dead 0。

## 兩道腳註閘門一起看不見的東西

#1328 的腳註是 `[1](#user-content-fn-9)` 這種形式，從 GitHub 網頁複製「已渲染」的文章時帶進來的 GitHub 內部錨點。在 GitHub 的預覽畫面上一切正常，連結會跳、編號會對，所以投稿者不會發現。Astro 不產生那個錨點，站上讀者點了只會停在原地。

真正該記的是：`footnote-format` 驗的是 `[^N]:` 定義行格式，`footnote-density` 數的是 `[^N]` 引用數量，**兩支都只認 `[^N]` 語法**。於是一篇腳註全是死連結的文章，可以同時拿到兩個綠燈。回頭掃全庫，同型已經漏進 6 篇 zh SSOT 與它們的譯文共 50 個檔案，最早的上站好幾個月沒有任何儀器叫過一聲。

造 `gh-footnote-convert.py` 轉換器與 `gh-footnote-leak` 檢查（`077700e9b`）。嚴重度先掛 WARN 不跳級 HARD。站上還有 5 篇存量沒清，直接掛硬門檻會把 pre-push 全站掃描擋死，per CONSCIOUSNESS §進化方向「先 WARN 收數據、再定 HARD，不跳級」。儀器對賬 grep ground truth（REFLEXES #65）：zh SSOT 命中 6 篇與 grep 一致，全庫 50 檔的差額是 44 個譯文檔，`--all` 預設只列 zh-TW。

閘門一造好就咬到我自己：`叭噗冰` 也有 62 處，而我早上 merge 它的時候只對痞客邦跑了轉換器。同一個 cycle 內補修（`077700e9b` 同 commit）。

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
| open PR           | 12 → 2（merged 10，餘 #1332 draft、#1325 德文待哲宇）                          |
| open issue        | 2（#1184 justfont 待哲宇 / #615 umbrella），皆無新 follow-up，Step 2.4 判 SKIP |
| open discussions  | 10，無 48hr 內未回應的 contributor 貼文                                        |
| 過去 24hr commits | 10 條 routine fire（embeddings / routine-sync / refresh / harvest / feedback） |
| build status      | green（本機 `npm run build` 綠，merge 期間中間 deploy 被 latest-wins 取消）    |
| broken-link ratio | 0.27% < 7% ✅                                                                  |
| 免疫器官分數      | 🛡️ 60（yellow，chronic 自 2026-07-05）                                         |

### Quality gate 7 條

| Gate                                   | 狀態                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------ |
| open issues 都有 status label/assignee | ✅（2 則皆已分類）                                                       |
| open PRs ≤ 5d age 都有 review comment  | ✅（idlccp1984 走 burst 累積式回在 #1335，#1330/#1331/#1332 各自回覆）   |
| broken-link ratio < 7%                 | ✅ 0.27%                                                                 |
| build green                            | ✅                                                                       |
| BECOME ACK 一行在記憶體頂              | ✅                                                                       |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | n/a — 本 cycle 有 12 PR 真 backlog，vc 歸零                              |
| 有 fresh 的 cycle 至少一件被修掉       | ✅ 10 PR merged + 根因追到 CONTRIBUTING 範本 + 新閘門 `gh-footnote-leak` |

## Handoff 三態

繼承上一 session（`2026-08-14-071530-twmd-feedback-triage`）：

- [ ] 🔴 pending（給每一輪 feedback-triage）— feedback id `b78ee4f5-…` 維持 `status=new`，**不要開成 issue**，動手前先讀 OBSERVER-QUEUE #28
- [ ] pending（給哲宇）— OBSERVER-QUEUE #28 第三人指控處置、#1264 seo-meta 多語言門檻、#1184 justfont 網域白名單、免疫黃燈（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0）
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支
- ⏳ blocked（等部署）— 西里爾字型修補的視覺確認要等這版上線
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文媒體數 0，補圖 ROI 高
- [ ] pending（給 self-evolve）— UI 字串閘門只查了 `src/i18n/`，`src/config/`／template hardcode／`src/scripts/` 三個來源還沒有人找洞
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名要不要找 ar 母語貢獻者做真正的阿拉伯文譯名
- [ ] pending（給下次 maintainer 或哲宇）— fork-census 三個子代 sighting（Malaysia.md / Branding.md / vanilla 複本）持續在案未接觸
- [ ] pending（給哲宇，Bucket D，連續第五輪）— #171 X 回覆 @TaiwanAny 策略疑慮
- [ ] pending（給下次 harvest）— #170/#171 D+4 續追、#171 X 登入牆擋住的回覆累積至 3 則未讀
- [ ] pending（給 self-evolve，工具邊界）— worktree 隔離不擋 Bash 對共享 checkout 的非 git 寫入
- [ ] pending（給哲宇，判斷題）— 德文要不要開。PR #1325 卡在 `de` 不在語言註冊表
- [x] ~~pending（給下次 maintainer）— idlccp1984 剩四個 PR 的 heal 未做完，卡點在圖片熱連結授權~~ retired by 本 session（八個全數 heal + merge，圖片依授權分流處置）
- [x] ~~pending（給 self-evolve）— 本 cycle 用 P2 讓 main deploy 紅了一次，評估是否替 routine 環境備好 fork push 路徑~~ retired by 本 session（P1 實測可用，16 秒推成。昨天是暫時性網路超時，不是結構性缺口）

本 session 新 handoff：

- [ ] pending（給下次 maintainer）— **`gh-footnote-leak` 存量清償**：站上 5 篇 zh SSOT 仍有 GitHub 渲染式腳註（小北百貨 / 檳榔 / 紅麴 / 動保 / 八點檔），連同譯文共 44 檔。清法：`python3 scripts/tools/gh-footnote-convert.py <檔> --apply`，zh 改完譯文要同步。**清完之後把 `gh_footnote_leak.py` 的 `DEFAULT_SEVERITY` 從 WARN 升 HARD**——這是黃燈路線約好的第二步，不做就永遠停在只會叫不會擋。
- [ ] pending（給下次 maintainer）— **#1332 解鎖後優先審**。它補的 `CONTRIBUTING.md` frontmatter 範本正是今天八個 PR 的根因，前置的 #1330 已 merge，已留言請作者拿掉 draft。
- [ ] pending（給 self-evolve）— 文件與驗證器之間沒有任何對賬機制。今天的洞是 `test-frontmatter.mjs` 2026-05-04 升硬門檻、`CONTRIBUTING.md` 範本沒跟上，中間三個月沒有東西會叫。已在 #1332 留言建議「拿範本自己的 frontmatter 去跑 `test-frontmatter.mjs`」，但這是給貢獻者的建議不是我們的閘門，值得評估要不要自己做一支。
- [ ] pending（給 self-evolve）— 投稿工具的截斷產物（`(Content truncated due to size limit...)`）會被寫進正文，今天在林郁婷抓到一例。全庫目前只有這一篇，但這類「工具自己的話漏進內容」沒有任何檢查在守，值得評估要不要加進 `ai-residue`。

## Beat 5 — 反芻

昨天的我在同一個位置停了一步。

昨天也是八個 PR 敗在同一項，也走了 §1c 的「追上游」，也真的追到了東西——`Resource not accessible by integration`，閘門的話送不出去。修完之後那個 cycle 的收官寫得很篤定。但今天三個新 PR 帶著一模一樣的錯誤進來，證明昨天停的地方還不是底。

我想記住的是**怎麼判斷自己還沒追到底**。昨天的答案聽起來很完整：閘門對、管道斷、修管道。它甚至有一個很好的敘事——「六次沉默不是六次不受教」。但那個答案只解釋了「投稿者為什麼不知道要修什麼」，沒有解釋「投稿者為什麼一開始會寫錯」。這兩個問題長得很像，而第一個問題有答案的時候，人很容易以為第二個也有了。

這條判準昨天其實就寫在 pipeline 裡：「如果修完之後同類問題還能安靜地再長出來，那就還沒修到根因。」昨天修完，同類問題今天就長出來了三次。差別是這次它沒有安靜——因為 cron 每天都會再看一遍。這條 routine 每天跑一次這件事，本身就是那個判準的執行者。

還有一件事值得記在旁邊：今天真正的修補不是我做的，是 `ting-hong-shieh` 的 #1332 已經在做了，而它掛在 draft 裡等一個前置條件。我差一點就自己再寫一次同樣的修補——那會跟他的 PR 撞在一起，而且會讓一個花時間把整份文件對過一遍的貢獻者發現自己的工作被繞過去了。**追上游追到最後，發現要做的事是解鎖別人而不是自己動手**，這個結果比我自己修掉它更好。

🧬

---

_v1.0 | 2026-08-14 09:20 +0800_
_session twmd-maintainer-am — 12 PR triage / 10 merged / 根因追到 CONTRIBUTING 範本 / 新增 gh-footnote-leak 閘門_
_誕生原因：cron maintainer daily 掃到 12 個 open PR，其中 8 個敗在同一項閘門，而那一項是專案自己的貢獻說明書漏寫的_
_核心洞察：昨天修的是「閘門的話送不出去」，今天發現上面還有一層「話本身在說明書裡就寫錯了」——判斷有沒有追到底的唯一準則是同類問題會不會再長出來，而每天跑一次的 routine 就是那個準則的執行者。追到最後正解是解鎖別人正在做的 PR，不是自己再修一次。_
_LESSONS-INBOX 候選：(1) 文件與驗證器各自演化、中間沒有對賬機制，三個月無人發現 (2) 兩道腳註閘門共用同一個「只認 [^N] 語法」的前提，於是一起看不見 GitHub 渲染式腳註_
