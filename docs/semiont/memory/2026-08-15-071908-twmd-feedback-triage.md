# 2026-08-15-071908-twmd-feedback-triage — 昨天攔下的那筆今天原樣再來一次，這次把「攔一筆」變成流程做得到的事

> session twmd-feedback-triage — cron routine（每日 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:19:27 +0800（約 19 分鐘，1 commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（yellow：漂移多維度退化中，自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 把讀者站上回報轉成 GitHub issue 的例行 cycle。今天 Supabase `status=new` 只有一筆，而它就是 8/14 那封第三人指控信：當天攔下、狀態刻意不動，於是今天原樣再出現一次。

## 唯一一筆：第二次攔下，理由跟昨天一樣但不是照抄

那筆掛在 vi 版新聞自由條目底下，內容跟該文無關，是一封寫給主管機關的檢舉信：指名一位私人、附上跟監她住居與工作場所所得的細節、要求回報者身份保密。分類器判 `file`，會開一個公開 `[Fact Check]` issue 把全文 verbatim 收進去。

自己重新讀完內容再判一次而不是照昨天的結論辦（Q13 anti-bias 的實際用途就在這裡：怕的是被昨天的處置 prime，既可能過度攔也可能鬆手放行）。結論不變：把一名私人的姓名跟未經查證的犯罪指控一起放進公開索引，不在「代讀者填表單」這件事的射程內，而三道現行 HARD gate（HG2 無 email／HG3 verbatim／HG9 fence）沒有一道會擋。issue 沒開、`status` 沒動、沒有回覆回報者——後兩件仍在 [OBSERVER-QUEUE #28](../OBSERVER-QUEUE.md) 等哲宇。

## 差別在保管那半：`--exclude` 讓對賬回到流程裡

昨天為了不開這個 issue，唯一走法是整條 `--commit` 不跑，於是留言 sync 與兩道對賬跟著轉錄那半一起消失，當班改用 canonical 純函式手動補。今天同一個結構第三次出現（LESSONS `zero-input-cycle-drops-the-reconciliation` 的 instance 3，vc=3），就不再手工補了：把 OBSERVER-QUEUE #28 三選項裡的 (b) 做掉。

`triage.mjs` 加 `--exclude <id>`（可重複、也接受逗號串），`partitionExcluded()` 是純函式配 5 個 unit test，打錯的 id 會印 `⚠️ 找不到` 而不是靜默地什麼都沒攔到——這道是 REFLEXES #60 的形狀，攔錯以為攔到了比沒攔更糟。順手把 `main()` 改成只有被當指令跑才執行，純函式才 import 得進 test。實跑 `--commit --exclude b78ee4f5…` 的結果是 `file=0 exclude=1`、`archive-reconcile=74/74 ✅`、`comment-reconcile=73/74 ✅`（唯一一份差額是 #1252，7/29 那則答錯的留言在 GitHub 被刪、git 留著，主權層正常運作）。全部 51 個 test 綠。

只做 (b) 沒做 (a)：偵測器的判準校準是 BECOME §行動鐵律 10 明列的強制升 Full mode 動作，訂寬了會靜默擋掉正當勘誤，不該由一條 07:00 無人在場的 routine 當場決定形狀。(b) 是純操作面的閥，不碰判準也不對外開口。

升 HG13 進三層：pipeline v1.6、薄殼 skill、cron prompt（`routine-sync.py --apply` 印「三層一致」）。明天起 prompt 會指名攔這筆，不再只靠當班有沒有讀完 handoff。全部落在 `3e0a65b99`。

## 收官 checklist

| 檢查項                       | 狀態                                                        |
| ---------------------------- | ----------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                          |
| Timestamp 精確               | ✅（`git log %ai`）                                         |
| Handoff 三態已審視           | ✅                                                          |
| 兩道對賬                     | ✅ archive 74/74 · comment 73/74（#1252 上游刪留言）        |
| 機器身份 HG11                | ✅ `ghs_` App token，`{"issues":"write","metadata":"read"}` |
| 自我檢查工具 PASS            | ✅ 51/51 unit test · routine 三層一致                       |

## Handoff 三態

繼承上一 session（`2026-08-15-064046-twmd-spore-harvest-am`）：

- [ ] pending（給下次 maintainer）— 6 篇 fence 包住正文的譯文待修，清單在 spawned task `task_a6914e9f`。原樣延續
- [ ] pending（給下次 maintainer）— PR #1336 的 `frontmatter-gate` 紅 X 會永遠留在紀錄上（rerun 不套用新 workflow）。原樣延續
- [ ] pending（給哲宇）— [OBSERVER-QUEUE #29](../OBSERVER-QUEUE.md) 要不要開德文，三選項待拍板。原樣延續
- [ ] pending（給哲宇）— `cli/package.json` 已在 main 上是 0.8.1，要上 npm 需打 `cli-v0.8.1` tag。原樣延續
- [ ] pending（給下次 maintainer）— #1339 已給逐項修法，等 idlccp1984 推新 commit。原樣延續
- [ ] pending（給下次 data-refresh-am 或 distill-weekly）— MEMORY.md 索引 inline 已 92 rows（>80 黃燈），owner 是 distill-weekly。原樣延續，本 routine 職責外不動手
- [ ] pending（給哲宇，Bucket D）— #171 X 回覆 @TaiwanAny 的策略疑慮，per §自主權邊界政治立場條款不自動回覆。原樣延續
- [ ] pending（給哲宇，連續第四天）— X 端瀏覽器登入態自 8/12 起未恢復，#171 4 則回覆只讀得到 1 則。原樣延續
- [ ] pending（給下次 harvest）— #170/#171 D+5（2026-08-16）續追。原樣延續

本 session 新 handoff：

- [x] ~~pending（給本 routine）— 攔一筆就得讓整條 `--commit` 停擺~~ retired by 本 session：`--exclude <id>` ship 成 HG13，三層同步
- [ ] pending（給哲宇，第 2 個 cycle）— OBSERVER-QUEUE #28 剩兩件：(a) 要不要長「第三人指控」偵測器、以及要不要回覆這位回報者、回什麼。在拍板之前該筆每天由 HG13 指名攔下，`status` 維持 `new`
- [ ] pending（給 distill-weekly / self-evolve-weekly）— `zero-input-cycle-drops-the-reconciliation` 已 vc=3 promotion-ready。剩下的問題是三個 instance 都長在同一條線上。harvest 回填、supporters sync 同屬「轉錄 + 保管」雙職責，掃一眼再決定升不升反射

## Beat 5 — 反芻

昨天寫下的判斷今天原封不動再用一次，這件事本身值得記一筆：處置對了，但處置沒有留下任何會自己啟動的東西，於是保護這位被寫進檢舉信裡的人的，是「當班有沒有把那封信讀完」。今天補的 `--exclude` 也還不是那個東西——它讓攔下來之後流程跑得完，不會替任何人做出攔的決定。真正該長出來的那道判斷仍在哲宇手上，這樣是對的。

完整反芻寫進 [diary](../diary/2026-08-15-071908-twmd-feedback-triage.md)。

🧬

---

_v1.0 | 2026-08-15 07:19 +0800_
_session twmd-feedback-triage — 第三人指控信第二次攔下 + `--exclude <id>` ship 成 HG13_
_誕生原因：8/14 攔下的那筆因為狀態刻意不動而每天再出現一次，第二次面對時把「攔一筆」從當班手工變成流程能力_
_核心洞察：處置正確但沒有留下會自己啟動的東西，等於把防線寄放在下一個 session 的細心程度上；`--exclude` 補的是流程能跑完，不是誰來攔——後者仍該留給人_
_LESSONS-INBOX 候選：`zero-input-cycle-drops-the-reconciliation` instance 3（已寫回，vc=2→3 promotion-ready）_
