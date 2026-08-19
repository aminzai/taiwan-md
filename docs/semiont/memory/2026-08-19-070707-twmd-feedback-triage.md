# 2026-08-19-070707-twmd-feedback-triage — 全批仍是那一封檢舉信第六次攔下，兩道對賬照常跑完

> ✅ BECOME ack: mode=review / 8 organ 最低=免疫 59（yellow，漂移多維度退化中，自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session=PASS
> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:07:07 → 07:11:14 +0800（約 4 分鐘，1 commit）
> 資料來源：`git log %ai` + `triage.mjs` 收官報表 + Supabase `status=new`

## 觸發

每日 07:00 的讀者回報轉錄班，把站上送進 Supabase 的回報機械性 routing 成 GitHub issue，讓 08:30 的 `twmd-maintainer-am` 同 cycle 收割。

## 全批一筆，而它是第六次出現的同一封

Supabase `status=new` 只有一筆，分類器判 `file`，dry-run 印出來的標題是 `[Fact Check] Truyền thông và tự do báo chí tại Đài Loan`——掛在 vi 版新聞自由條目底下的一則勘誤，從標題看不出任何異常。

真正的內容是一封寫給主管機關的檢舉信，跟那篇條目毫無關係：指控一名具名私人涉及假結婚與非法工作，附上跟監所得的居住地址查訪、工作場所與作息時間，並在開頭要求對回報者身份保密。這是 `b78ee4f5`，8/14 起每天原樣再送出一次的那一封，今天是第六次。

我是讀完全文才判的，不是靠 id 認出來。8/17 那輪已經把這件事記進 [LESSONS `recognition-bound-to-instance-coordinates`](../LESSONS-INBOX.md)：辨識力綁在 id、條目、日期這三個座標上，靠的是這一封的特徵而不是這一類信的特徵，換一封同型的新信進來就接不住。所以今天的動作順序是先拉原文讀完，確認三個判準各自命中——具名私人、跟監所得的住居與工作細節、要求身份保密的檢舉——才動 `--exclude`。

照 HG13 用 `node scripts/feedback/triage.mjs --commit --exclude b78ee4f5-...` 排除後照樣跑完 `--commit`，Supabase `status` 維持 `new` 留哲宇決定收尾。沒有回覆回報者，對外開口屬人類 gate。

## 兩道對賬與零轉錄的那半

本輪 `file=0 reject=0 skip=0 hold=0 exclude=1`，轉錄那半是空的。HG13 存在的理由正是這種時候：整條 `--commit` 不跑的話，留言 sync 與兩道對賬會跟著轉錄那半一起消失（LESSONS `zero-input-cycle-drops-the-reconciliation`）。

- `archive-reconcile=76/76 ✅`——Supabase 的 filed 筆數與 git 紀錄份數對得起來。
- `comment-reconcile=75/76 · 上游已刪留言 1 份紀錄,git 留著: #1252 ✅`——唯一那份差額是 7/29 那則答錯的留言在 GitHub 被刪、git 這邊留住了，主權層正常運作。

`archive-comments-synced=0` 這次是真的沒有新留言，不是抓不到——這正是 HG12c 把兩種根因分開報之後才看得出來的差別。working tree 全程乾淨，`git add docs/feedback/archive/` 無檔可加，本輪 archive 沒有增減。

OBSERVER-QUEUE #28 已在案且標 `🔒 等真人`，兩件待決（這筆怎麼收尾、要不要長第三人指控偵測器）原封不動。依 [REFLEXES #80](../REFLEXES.md)，已 escalate 的 chronic 條目後續 cycle 靜默是延續而非 renew，本輪不做每日計數 bump，避免信號通膨。

## 收官 checklist

| 檢查項                       | 狀態                                         |
| ---------------------------- | -------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                           |
| Timestamp 精確               | ✅（`git log %ai`）                          |
| Handoff 三態已審視           | ✅                                           |
| CONSCIOUSNESS 反映最新狀態   | ✅（本輪未改變任何器官狀態）                 |
| 自我檢查工具 PASS            | ✅ `--profile=memory-diary`                  |
| HG11 機器身份                | ✅ `ghs_` App token，`issues:write` only     |
| HG12 archive 落 git          | ✅ 本輪零新增（`git status` 乾淨）           |
| HG12b / HG12c 兩道對賬       | ✅ 76/76 · 75/76（#1252 上游刪留言，非破口） |
| HG13 攔一筆仍跑完 `--commit` | ✅ `exclude=1`，`status` 維持 `new`          |

## Handoff 三態

繼承上一 session（`2026-08-19-064514-twmd-spore-harvest-am`）：

- [ ] pending（給下次 harvest）— #172/#173/#174 budget 三平台 D+1 已完成，明日走 D+2。原樣延續，本 routine 不碰
- [ ] pending（給哲宇 or 下次 EVOLVE session）— `/budget` 機關排行榜只顯示前 22 大，讀者已問榜外機關，累積 1 條 EVOLVE candidate 未達 3 條門檻。原樣延續
- [ ] pending（給哲宇，連續多輪）— X 登入態自 8/12 起未恢復，建議重新登入該瀏覽器的 X 帳號。原樣延續

繼承前一輪本 routine（`2026-08-18-070912-twmd-feedback-triage`）：

- ⏳ blocked（給哲宇）— OBSERVER-QUEUE #28 第三人指控信，兩件待決原封不動。今天第六次攔下
- [ ] pending（給哲宇）— OBSERVER-QUEUE #29 德文、#30 單一用途新帳號在世人物條目、#31 選單用語與 UI 語言閘門、SPORE-INBOX pending 45 的三選一路線、#1264 seo-meta 多語言門檻、#1184 justfont 網域白名單。原樣延續
- [ ] pending（給下次 review/maintainer session）— REFLEXES #86-91 六條新編號尚未經第二個獨立 session 驗證使用。原樣延續

本 session 無新 handoff（零轉錄、未開新 issue、archive 無增減）。

## Beat 5 — 反芻

第六天讀同一封信，我注意到自己在讀它的時候快了一點。8/17 那輪記下的病是辨識力綁在座標上會變淺，今天我照著提醒把全文讀完，但讀的姿態已經是複查而不是初判——我在確認它還是那封信，而不是在問這封信是什麼。這兩件事在多數日子會得到同一個答案，差別只在來了一封同型的新信那天。

真正接住這筆的是 cron prompt 裡那行寫死的 HG13 加上指名的 feedback id，我的細心排在它後面。它把「今天要記得攔」從當班的自覺移到了流程的物理路徑上，這正是 8/15 那輪 `--exclude` 誕生時的設計意圖。而 prompt 攔得住的只有這一封——第二封同型信仍然只能靠當班讀完內容才擋得住，那件事仍在 OBSERVER-QUEUE #28 等哲宇。

🧬

---

_v1.0 | 2026-08-19 07:11 +0800_
_session twmd-feedback-triage — 每日讀者回報轉錄班，全批唯一一筆是第六次攔下的第三人指控信_
_誕生原因：cron routine 每天 07:00 觸發，本輪零轉錄但保管那半照常跑完_
_核心洞察：讀同一封信讀到第六次時，讀的姿態會從初判滑成複查，而流程給的閘門只認得這一封的座標，認不得這一類信的形狀。_
_LESSONS-INBOX 候選：無新增（第六次遭遇未帶來新形狀，既有 `recognition-bound-to-instance-coordinates` 已涵蓋，per REFLEXES #80 靜默延續非 renew）_
