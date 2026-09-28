# 2026-09-29-071521-twmd-feedback-triage — 零回報第八輪，兩道對賬全綠，而想量「讀者多久來一次」時發現主權層那批檔案量不出這件事

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:15:30 +0800（約 15 分鐘，1 commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 v3 59（consciousness-snapshot，最大缺口 review_coverage=19）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 把讀者站上回報轉成 GitHub issue，接 08:30 maintainer-am 的收割。本輪佇列是空的，第八次。

## 轉錄 0 筆，保管層兩道對賬全綠

`triage.mjs` dry-run 與 `--commit` 都回 `fetched 0`，`file=0 reject=0 skip=0 hold=0`。HG11 機器身份先驗過：token 是 `ghs_` 開頭，`--whoami` 印 `{"issues": "write", "metadata": "read"}`、`repositories: frank890417/taiwan-md`（真實安裝範圍，不是把缺欄位印成「覆蓋全部庫」的舊版）。

零輸入仍照 HG13 跑完 `--commit`，兩道對賬因此都有讀數：`archive-reconcile=87/87`、`comment-reconcile=86/87`。後者那一筆差額是 issue #1252——7/29 那則答錯的留言在 GitHub 被刪掉，git 這邊留著。方向是 archive 多於線上，屬主權層正常運作，不報警。`archive-comments-synced=0` 這次可以放心讀成「沒有新留言」，因為 comment-reconcile 給的是 86/87 而不是 `null`：抓得到線上帳，就排除了 gh 或 token 壞掉那條根因。這正是 HG12c 存在的理由。

本輪沒有任何 archive 檔變動（零新回報、零新留言），所以 HG12 的 `git add docs/feedback/archive/` 沒東西可加。

## 想回答「9 天沒人回報算不算異常」，結果換錯了母體

`fetched 0` 那行附帶印出「最近一筆回報：2026-09-19（距今 9.0 天）」。要判斷這個數字，得拿歷史間隔來對。九月中同一條 routine 已經為這件事校正過兩次（9/11 查最近 60 筆得 10 天、9/15 查全庫 87 筆得 12.65 天），並在 [REFLEXES #24](../REFLEXES.md) 形式 4 留下處方：問「歷史上最 X」要全庫，**重驗要換取數形狀**。

於是換了形狀：改掃 `docs/feedback/archive/*/*.md` 的 87 份主權層紀錄，本地、確定性、不依賴外部服務，看起來是更好的尺。它算出歷史最長間隔 **15.94 天**（07-04 → 07-20），比 12.65 更大，讀起來像又找到一個前一次漏掉的極值——**跟處方生效的樣子完全一樣**。

改查全庫所有 status 才看清：全庫 **90 筆 = 87 filed + 3 rejected**，其中一筆 rejected 落在 2026-07-11，把七月那個窗切成 7.04 + 8.90 天。真實上限就是 **12.65 天**，9/15 那個數字一直是對的。差別在 archive 只收 `filed`（Stage 4 的 reject 分支不寫檔，canonical 刻意如此，不讓 spam 文字進 git），所以它量得出勘誤之間的間隔，量不出讀者到達之間的間隔——spam 也是一次到達，只是沒在 git 留痕。偏差方向固定偏大，長相是「讀者比實際更安靜」，而且沒有任何閘門會響，因為兩把尺都沒壞。

差一步就把 15.94 當成新的歷史上限寫進這份 memory，蓋掉 REFLEXES #24 那行正確的數字。目前 9.05 天排歷史第 4 名／89 個已收口間隔，在變異範圍內，不是訊號。刻意不設閾值（屬 threshold 調整，per BECOME §行動鐵律 10 要 Full mode 加人類 gate）。

修法兩處都落在 `91256334e`：`docs/feedback/README.md` 補一段「這層對 filed 完整，對『到達』不完整」，寫在下一個要拿它算節奏的人會讀到的位置，LESSONS 則記一條 `requery-with-a-new-shape-can-swap-the-population-not-just-the-window`。pre-commit 的 narrative scope 對這個 commit 亮了黃燈（cognitive 加 other 兩個 domain），這次刻意留著：教訓跟它的落地註記是同一個發現的兩半。

## 收官 checklist

| 檢查項                       | 狀態                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                            |
| Timestamp 精確               | ✅（`git log %ai`）                                           |
| Handoff 三態已審視           | ✅                                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅ 本輪未改讀數（免疫 59 chronic 由 self-evolve-weekly 持有） |
| 自我檢查工具 PASS            | ✅ prose-health（memory-diary profile）                       |
| HG12b / HG12c 兩道對賬       | ✅ 87/87 與 86/87（#1252 上游刪留言，git 留著）               |

## Handoff 三態

繼承 `2026-09-29-064213-twmd-spore-harvest-am`（非本班職權，原樣傳遞，不重抄明細，REFLEXES #74）：

- ⏳ blocked（延續）— issue `#1729`（馬英九腳註）等 Write session 帶哲宇 review，`OBSERVER-QUEUE #75`〜`#90` 待決。
- [ ] pending（延續）— routine-sync 對賬前 `git fetch`（席位 `twmd-self-evolve-weekly` 10-04）、data-refresh Stage 1.5 寫明順序（席位 `/twmd-routine`）、build 秒數三點再判、`.git/gc.log`、`md-extension` 10-02 觀察、babel 自造 slug 存量、`/terminology/變壓器`（10-05 用語月報）、404 unknown 觀察。明細見該檔。
- [ ] pending（延續，席位 spore-harvest／spore-pick，零判斷）— `list_connected_browsers` 回 `[]` 的查法、`/activity/replies` 逐則對 `time[datetime]`、`#29` 重抓門檻聚合到 1.5 萬、`#29` 兩則位置不明的留言需帶 permalink 巢狀展開能力的 session、`#175`／`#176` 公告型孢子不排 D+30 milestone。
- [ ] pending（延續，席位 `/twmd-routine`，動得了 scheduled-task 殼）— `twmd-spore-harvest-am` 殼的 `/Users/cheyuwu/` 路徑與 `git add -u`，連三班照現況繞開（LESSONS `routine-prompt-prescribes-add-u-on-shared-index`，vc=3 已達升級門檻）。
- [ ] pending（延續，低優先，等哲宇在場）— Threads 私訊夾是否納入受眾飛輪，屬對外溝通，建議週報桶 3 登記 OBSERVER-QUEUE。

繼承 `2026-09-28-071520-twmd-feedback-triage`（本班職權）：

- [x] ~~pending — `#1609` 續量~~ retired by 本班：9/27 那則回覆已進 archive，該項已搬進 `OBSERVER-QUEUE #85`（待決，缺一次真人登入），續量基準改追佇列項。本輪 `comment-reconcile` 86/87 覆蓋了這條線的健康。
- [ ] pending（延續，席位 `twmd-distill-weekly` 10-04，只需裁決不需權限）— LESSONS `reconciliation-blind-to-what-reached-neither-side`（vc=1 structural）：判它是 REFLEXES #82／#88 的子規則還是新號。
- [ ] pending（延續，席位需能改排程或架構者，即 Full mode 加哲宇）— 上條那個窗口要不要收窄或加第三個證人（webhook／事件流）。每日一掃等於 24 小時窗，漏一輪 48 小時。
- [ ] pending（延續，席位 Full／Review session）— `#1678` 第 25 天照舊續量。

本 session 新 handoff：

- [ ] pending（席位 `twmd-distill-weekly` 10-04，只需裁決不需權限）— LESSONS `requery-with-a-new-shape-can-swap-the-population-not-just-the-window`（vc=1）：判它是 REFLEXES #24 形式 4 的新維度（處方帶副作用）還是只是 FEEDBACK-TRIAGE 的操作規則。已落的只有 README 範圍註記，判準本身沒動。
- [ ] pending（席位 `twmd-feedback-triage` 本班，零判斷，動得了 `scripts/feedback/`）— 到達節奏若要常問，在 `formatIntakeAge()` 旁補一支全庫間隔分佈（它本來就握著全 status 讀取權），免得下一班又從 archive 推。本輪只寫了註記沒造工具，因為八輪零回報還不確定這個問題值不值得一支常設儀器。
- [ ] pending（席位 Full／Review session 或 `/twmd-routine`，動得了 `.husky/pre-push`，接 9/28 `c9fcf850f` 的「build 秒數三點再判」那條）— 本班 push 給那條剛校準過的閘門一個實測資料點：`TYPICAL` 取的是近五次成功的**中位**（今天 2,018 秒，全距 1,869〜2,079），`THRESH = 中位 − 120`，所以任何比中位慢的那一次一定會白等滿 120 秒。本班遇到的 run 已跑 2,052 秒進入「近完成」分支，等到 2,172 秒仍未完，照設計放行。用中位當門檻等於結構上讓大約一半的等待註定落空。改用近五次的**最大值**或 p90 算 `THRESH` 就能把這類白等收掉，代價是更少次數會去等。數字小、方向明確，屬閾值調整（per BECOME §行動鐵律 10 要 Full mode），本班只記不改。

## Beat 5 — 反芻

今天量到的是一個處方自己帶的副作用。REFLEXES #24 形式 4 說重驗要換取數形狀，那條規則是對的，九月中連兩次校正都靠它。但「換形狀」跟「換母體」在操作上是同一個動作——我改用 archive 而不是 REST 查詢，同時換掉了取數方式跟被取的那群人，而只有前者是我打算換的。更麻煩的是失敗的長相：新數字變大，看起來正是「窗外還有更大的極值」該有的樣子，也就是處方生效時該有的樣子。如果我停在那裡，不只會寫錯一個數字，還會以為自己剛剛示範了一次紀律。

停下來的理由其實很薄——只是覺得 15.94 跟 12.65 差得有點多，而 12.65 那個數字前後校正過三次才落定。那點不對勁比任何閘門都早一步。這也說明為什麼 REFLEXES #99「尺先驗再用」要跟 #24 一起讀：換尺之後那個讀數，在確認新尺量的是同一群東西之前，不算數。

零輸入第八輪本身還不是訊號（9.05 天排第 4／89）。但值得記一筆：這條線量得到讀取端，寫入端仍只有推論，而今天的發現說明連「讀取端」那一側也有分層——同一個問題問 Supabase 跟問 git，得到的是兩種不同的完整性。

🧬

---

_v1.0 | 2026-09-29 07:15 +0800_
_session twmd-feedback-triage — 每日 07:00 讀者回報轉錄；第八輪零回報，兩道對賬全綠_
_誕生原因：cron routine 每日固定收官_
_核心洞察：換取數形狀重驗極值時，換掉的可能是母體而不是窗大小——archive 只收 filed，量得出勘誤之間的間隔，量不出讀者到達之間的間隔，而偏差方向固定偏大、長相跟「終於找到漏掉的極值」一模一樣。_
_LESSONS-INBOX 候選：`requery-with-a-new-shape-can-swap-the-population-not-just-the-window`（已 append，vc=1）_
