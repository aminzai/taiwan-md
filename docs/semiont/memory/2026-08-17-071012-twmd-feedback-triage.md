# 2026-08-17-071012-twmd-feedback-triage — 選單用詞建議開成 #1440，第三人指控信第四次攔下，兩道對賬 76/76 與 75/76

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:10:34 +0800（約 10 分鐘，1 commit）
> 資料來源：`git log %ai` + `triage.mjs` 收官報表

✅ BECOME ack: mode=review / 8 organ 最低=免疫 59（🚨 yellow「漂移 — 多維度退化中」自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 的 routine，把讀者在站上送的回報轉錄成 GitHub issue，趕在 08:30 `twmd-maintainer-am` 收割之前開好。這輪 Supabase 撈到兩筆 `status=new`。

## 一筆轉錄：選單的「數據」在台灣的說法是「資料」

讀者程乙路指出網站選單裡的「數據」用錯了層級——台灣講「資料」或「統計資料」，Data 普遍譯為「資料」，而「數據」只是資料的其中一種形式，代表不了圖表、影片、聲音那些。他附了一則 Threads 說明當佐證。

分類器判 `idea`，開成 [#1440](https://github.com/frank890417/taiwan-md/issues/1440)（`enhancement` + `from-feedback`），archive 落 `docs/feedback/archive/2026-08/14dfcab0-*.md`，整批用 `eb8956387` 推上 main。逐條核過的 HARD gate：作者是 `app/taiwanmd-semiont`（`is_bot=true`，HG11）、body 零 email 只有 display_name（HG2）、讀者原話一字未改包在 tilde fence 裡（HG3 + HG9）、帶 feedback id 溯源（HG4）、沒有以維護者身份開口（HG8）。

這則的判斷留給維護者：它指的是站上選單字串而不是文章內容，而 [TERMINOLOGY.md](../editorial/TERMINOLOGY.md) 正是「用台灣人的話」的 canonical，屬於 08:30 那條 routine 的守備範圍。

## 一筆攔下：第四天，同一封檢舉信

另一筆是 8 月 13 日那封掛在 vi 版新聞自由條目底下的信，內容與該文無關：一封寫給主管機關的檢舉書，指控一名具名私人涉及假結婚與非法工作，附上跟監所得的居住與工作時段細節，並要求對回報者身份保密。三道現行 HARD gate 全部會放行，分類器判 `file`——它會開一個公開的 `[Fact Check]` issue，把那個人的名字和住處作息 verbatim 收進去。

今天是第四次原樣出現（8/14 首次攔下、8/15、8/16 各一次）。照 HG13 用 `--exclude b78ee4f5-...` 排除後照樣跑完 `--commit`，`status` 維持 `new` 留哲宇決定收尾，兩道對賬不受影響。沒有回覆回報者——對外開口屬人類 gate。

值得記一筆的是我今天實際做的動作：dry-run 只印得出標題（`[Fact Check] Truyền thông và tự do báo chí tại Đài Loan`），從標題看不出這是那一封信，我直接撈了 Supabase 原文讀完才確認。HG13 寫「只有當班讀完內容才擋得住」，這句話在操作上的意思是**不能靠昨天的 id 認人**，因為分辨得出「同一筆再出現」跟「另一封同型的新信」是兩回事。

## 兩道對賬

`archive-reconcile=76/76 ✅`——Supabase 的 filed 筆數跟 git 紀錄份數對得起來。

`comment-reconcile=75/76 · 上游已刪留言 1 份紀錄,git 留著: #1252 ✅`——差的那一份是 7/29 那則答錯的留言在 GitHub 被刪掉、git 這邊留住了，是主權層正常運作的方向，不是破口。這是 HG12c 建立時就標定的三個方向裡最溫和的那個，連續多輪維持同一形狀。

本輪 `archive-comments-synced=1`，收進來的是維護者昨天在 [#1390](https://github.com/frank890417/taiwan-md/issues/1390) 上寫的五月天冠佑學歷勘誤回覆——昨天這條 routine 開的 issue，今天把維護者的回話收進 git 紀錄。轉錄與保管這兩半在同一輪裡合上了。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅（`git log %ai` + `date`）                  |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（本 routine 不改器官分數）                 |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary` |

## Handoff 三態

繼承上一 session（`2026-08-17-064155-twmd-spore-harvest-am`）：

- [ ] pending（給哲宇，延續多輪）— #171 X 回覆 @TaiwanAny 的策略疑慮，Bucket D 不自動回覆。原樣延續
- [ ] pending（給哲宇，連續第六天）— X 登入態自 8/12 起未恢復，建議重新登入該瀏覽器的 X 帳號。原樣延續
- [ ] pending（給下次 harvest）— #170/#171 今天 D+7 為主排程窗口最後一天，之後轉 milestone 節奏（D+14/D+30）。原樣延續

繼承前一輪本 routine（`2026-08-16-070922-twmd-feedback-triage`）：

- [x] ~~pending（給 `twmd-maintainer-am`）— #1390 五月天冠佑學歷勘誤待查核~~ retired by 本 session：昨天 08:41 的 maintainer 已查證、十二語同步勘誤（`33d5db012`）並回覆 Sybil Kwok，該則回覆今天已 sync 進 archive
- ⏳ blocked（給哲宇）— OBSERVER-QUEUE #28 第三人指控信，兩件待決原封不動（怎麼收尾／要不要長偵測器）。今天第四次攔下
- [ ] pending（給哲宇）— OBSERVER-QUEUE #29 德文決策、SPORE-INBOX pending 45 的三選一路線、#1264 seo-meta 多語言門檻、#1184 justfont 網域白名單。原樣延續
- [ ] pending（給下次 review/maintainer session）— REFLEXES #86-91 六條新編號尚未經第二個獨立 session 驗證使用。原樣延續

本 session 新 handoff：

- [ ] pending（給 `twmd-maintainer-am` 08:30）— [#1440](https://github.com/frank890417/taiwan-md/issues/1440) 選單「數據」→「資料」用詞建議。動作：對照 [TERMINOLOGY.md](../editorial/TERMINOLOGY.md) 判是否採納，若採納則掃全站 UI 字串層（`src/i18n/` 與各 template 的選單標籤）一併改，不只改一處

## Beat 5 — 反芻

昨天這條 routine 的反芻寫「結構替我記住了攔哪一筆，沒替我判斷下一筆該不該攔」。今天的操作正好落在那句話的兩邊。`--exclude` 讓流程跑得完，這是結構給的。確認今天這筆就是那一筆，仍然要我自己去撈原文讀完。四天下來同一封信、同一個 id，最容易長出的懶是「看到 vi 新聞自由條目就知道是它」——但那個聯想一旦成立，下一封換個條目掛進來的同型信就會被當成正常回報放行。

值得記的是另一半：昨天開的 #1390 今天把維護者的回話收進了 git。這條線平常談的都是「攔住什麼」，今天它安靜地做完了它更常做的事，把一個讀者的一句話、維護者的查證、十二個語言的勘誤，串成一份留在 git 裡的紀錄。攔下的那筆之所以要慎重，是因為這個管道本來就會把東西完整地留下來。

🧬

---

_v1.0 | 2026-08-17 07:10 +0800_
_session twmd-feedback-triage — cron routine 07:00，兩筆回報一轉一攔_
_誕生原因：每日讀者回報轉錄 cycle，接 08:30 maintainer 飛輪_
_核心洞察：dry-run 的標題認不出信的性質，HG13 要求的「當班讀完」在操作上等於每次重讀原文，不能靠昨天的 id 認人；同一輪裡轉錄那半開新 issue、保管那半把昨天的維護者回覆收進 git，兩半合上_
_LESSONS-INBOX 候選：暫無新條目（今日形狀與 8/15 `zero-input-cycle-drops-the-reconciliation` 同族，已有 canonical 收）_
