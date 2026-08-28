# 2026-08-29-070817-twmd-feedback-triage — 零筆新回報，這輪的產出全在留言 sync 那一半

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:12:00 +0800（約 12 分鐘，2 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 59（黃燈「漂移 — 多維度退化中」，自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

每天 07:00 的 routine：把讀者站上的回報轉成 GitHub issue，接 08:30 maintainer 的收割。這輪 Supabase 只有一筆 `status='new'`，而那一筆是 `b78ee4f5`。

## 只有一筆，而它是那封信

`b78ee4f5` 是 8/13 那封第三人指控信，這是第十二次原樣出現。內容指名一位在台灣的越南籍女子，附上一個月跟監得到的居住與工作地點、入境日期與班表推論，並要求對回報者身份保密。今天它掛在 `media-and-press-freedom-in-taiwan` 底下（跟昨天同一個位置）。

沒有靠 id 認它。直接打 Supabase REST 把 `status='new'` 的全文拉出來讀完再判——8/17 記過「辨識力綁在單一案例的座標上會越用越淺」，8/21 撞過同一筆換條目換副面孔，昨天的結論是「順序比辨識力耐用」。今天照順序走了一次，讀完內容判斷不需要依賴任何座標。

照 HG13 用 `--exclude b78ee4f5-...` 攔下，`status` 維持 `new`，未回覆回報者（對外開口屬人類 gate）。[OBSERVER-QUEUE](../OBSERVER-QUEUE.md) #28 那格只推日期與輪數到第十二次，照那格自己寫的規則不追加新段落。

## 產出全在另一半

`file=0 reject=0 skip=0 hold=0 exclude=1`。轉錄那半今天是零，但 `--commit` 照跑，於是保管那半照常做事：`archive-comments-synced=6`，六則昨天 maintainer 寫給讀者的回覆收進了主權層紀錄。

六則回覆搬動的東西不小。副詞條目原本把「詞類」跟「句子成分」對照起來，改成正確對照並加了 `auto_convert: false`。轉換器把社群範例裡的「粉絲」改成「冬粉」那則，順著追上游又抓到全站 17 條規則會把詞條的括號說明整段塞進使用者的文字裡，例如「網紅」被換成「網紅（已通用，早期說「部落客」「網路名人」）」。用語頁的篩選列在手機上佔 65% 視野，修到 8%，並補了一道用 375×812 真實渲染的 CI 閘門。最後一則是對某條斷代主張的誠實回覆：那條目唯一的來源是一則 Threads 留言串，讀者舉的卻是早七十年的台灣一手文本，於是加了誠信標註但沒直接改判定——理由是「在沒查證的情況下照著讀者的說法改結論，跟當初照著一則留言串下結論，是同一個毛病的兩面」。

這些話寫在 GitHub 上，隨時可能被刪或隨帳號消失。今天它們進了 `docs/feedback/archive/2026-08/` 的六份紀錄（`db3e4c97c`），Supabase 或 GitHub 哪天不在了都還留著。

## 兩道對賬

`archive-reconcile=82/82` ✅。`comment-reconcile=81/82`，差的那份是 [#1252](https://github.com/frank890417/taiwan-md/issues/1252)：7/29 那則答錯的留言在上游被刪，git 這邊留住了。照 HG12c 的方向表，archive 多於線上屬於主權層正常運作，不報警。

這輪剛好是 HG13 存在理由的乾淨示範。零筆可開的情況下若照舊走法整條 `--commit` 不跑，今天這六則回覆就會留在 GitHub 上不進 git，兩道對賬也一起消失——`zero-input-cycle-drops-the-reconciliation` 那條教訓講的正是這個形狀。

## 收官 checklist

| 檢查項                       | 狀態                                   |
| ---------------------------- | -------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                     |
| Timestamp 精確               | ✅（`git log %ai`）                    |
| Handoff 三態已審視           | ✅                                     |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot 齡 0h，黃燈照實記在下方） |
| 自我檢查工具 PASS            | ✅（prose-health）                     |

本輪 groundtruth 黃燈原樣繼承：免疫 v3=59 漂移（自 2026-07-05）、UNKNOWNS `EXP-2026-07-25-alias` 驗證日 8/24 已過期未判定、四條 routine 沉默死亡告警（本條 routine 自己也在名單上，指的是 8/24–8/27 那四天空窗，8/28 起已恢復）。

## Handoff 三態

繼承上一 session（`2026-08-29-064907-twmd-spore-harvest-am`）：五縣市圖片補正、`.husky/pre-push` `VAR="$(...)"` 掃描、#1453 人物卡連結、#1365 KENJI 門檻、OBSERVER-QUEUE #39-#43、免疫分數 59 漂移、w.is_solis 質疑、sophie990329 字典編審提問候選、terminology 查證候選（含 #1609）、空窗期人工回覆確認、harvest 排序盲區、#176（X）未登入、`/map` `.sidebar-panel` 高度問題。全部原樣繼承，本 session 未碰。

- [x] ~~指控信 `b78ee4f5` 第十一次攔下~~ retired by 本 session（第十二次已攔，計數推進 OBSERVER-QUEUE #28）

本 session 新 handoff：

- [ ] pending — 指控信 `b78ee4f5` 第十二次攔下，`status` 仍 `new`，明天會第十三次出現。下一輪照 HG13 拉全文讀完再 `--exclude`，不靠 id 認人。OBSERVER-QUEUE #28 的 (a) 偵測器與「要不要回這位回報者」兩件仍 🔒 等哲宇

## Beat 5 — 反芻

零輸入的 cycle 最容易被讀成沒事發生，而今天真正搬動東西的是沒人在看的那一半。轉錄那條線的產出是 `file=0`，保管那條線收了六則回覆進 git——如果收官只印「今天沒開 issue」，這份工作就整個不見了。

值得記的是這條 routine 的兩個職責原本綁在同一個開關上。8/15 之前「不開這個 issue」的唯一走法是整條不跑，於是攔一筆的代價是保管那半跟著停手。今天是那道閥第一次在**轉錄側完全沒有產出**的情況下生效：`file=0 exclude=1`，而 82/82 與 81/82 兩道對賬照樣落地。一道閘門的價值不在它擋下什麼，在它讓旁邊那條線不必跟著停。

🧬

---

_v1.0 | 2026-08-29 07:12 +0800_
_session twmd-feedback-triage — cron routine，零筆新回報 + 六則維護者回覆進主權層_
_誕生原因：每日 07:00 讀者回報轉錄 routine_
_核心洞察：轉錄零產出的 cycle 裡，保管那半仍在搬東西；HG13 的價值在讓攔一筆不必連累旁邊那條線_
