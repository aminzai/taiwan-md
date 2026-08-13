# 2026-08-14-071530-twmd-feedback-triage — 一則不能開成 issue 的回報：三道閘門全綠，而它們沒有一道在問會傷到誰

> session twmd-feedback-triage — cron routine（每日 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:20:00 +0800（約 20 分，1 commit）
> 資料來源：`date "+%Y-%m-%d %H:%M:%S %z"`、`triage.mjs` dry-run 與對賬輸出

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 60（`consciousness-snapshot.sh`，yellow 自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

Cron 每日 07:00 的讀者回報轉錄班。抓到一筆 `status=new`，掛在 vi 版 `/vi/society/media-and-press-freedom-in-taiwan` 底下。

## 那一筆回報

它跟那篇文章沒有關係。內容是一封寫給主管機關的檢舉信：回報者自稱調查人員，指控一名**具名私人**涉及假結婚與非法工作，附上跟監所得的居住與工作細節，要求調查，並請求對自己的身份保密。

`triage.mjs` dry-run 判 `file`，準備開一個公開的 `[Fact Check]` issue，把全文 verbatim 收進去，provenance 區署上回報者的 `display_name`。

這個 issue 沒有開出去。開下去有四件不可逆的事。一名不是公眾人物的私人，姓名會跟未經查證的犯罪指控一起被搜尋引擎與 AI 爬蟲永久收走。跟監所得的個人資料會公開。要求保密的回報者反而被署名推到台前。而收件人根本不是我們，這是給移民署或警察機關的檢舉，誤投到知識庫的回報表單。命中 MANIFESTO §自主權邊界的「敏感素材決定 — AI 準備 blueprint，人類 final call」，per REFLEXES #79 預設 reserve。

處置：`--commit` 沒跑（`triage.mjs` 沒有排除單筆的參數），Supabase 維持 `status=new` 且無任何 out-of-band 寫入，沒有回覆回報者。完整記述與三條修補路線寫進 [reports/feedback-third-party-allegation-hold-2026-08-14.md](../../reports/feedback-third-party-allegation-hold-2026-08-14.md)，正式出口是 OBSERVER-QUEUE #28（標 `🔒 等真人`）。報告刻意不寫被指控者的任何識別資訊，那些留在 Supabase 原始紀錄裡 — 抄進 git 等於用另一個形式完成了要攔下的那件事。

值得記下的是三道 HARD gate 在這則上**全部會通過**：HG2 無 email、HG3 verbatim 一字未改、HG9 隱形字元剝除加 fence 都乾淨。`detectSpam` 擋的是廣告的形狀（太短、賭場詞、四個以上連結、洗版字元），這則一項不中。`detectInjection` 也不響，因為它確實沒夾帶指令。**閘門量的是回報者的文字有沒有被正確搬運，沒有一道在問這段文字搬到公開處會傷到誰。** 教訓進 LESSONS-INBOX `transcription-gates-guard-fidelity-not-consequence`。

## 兩道對賬照樣要跑

昨天那輪剛留下 `zero-input-cycle-drops-the-reconciliation`：轉錄職責與保管職責是兩個獨立變數，輸入為零時不能讓核帳跟著消失。今天是同一結構的鏡像 — 輸入不為零，但不能轉錄，而兩者都綁在同一個 `--commit` 開關上。

改用 canonical 純函式（`mergeComments` / `reconcileArchive` / `reconcileComments` / `countArchivedComments`）在 scratchpad 跑一份只做保管那半的腳本，逐字沿用 `triage.mjs` 的 `syncArchiveComments` 邏輯，不碰 status、不開 issue：

```
archive-scanned=74 archive-comments-synced=0
archive-reconcile=74/74 ✅
comment-reconcile=73/74 · 上游已刪留言 1 份紀錄,git 留著: #1252 ✅
```

`#1252` 是 7/29 那則在 GitHub 被刪、git 留住的留言，主權層正常運作。`archive-comments-synced=0` 這次是真的沒有新留言（73 份對得上線上則數，`gh` 抓得到），不是抓不到 — 那正是 HG12c 存在的理由。這一輪把昨天那條教訓的 vc 推到 2，修補方向也跟著擴大：從「零輸入也要跑 `--commit`」變成「讓保管那半有自己的入口」（`--exclude <id>`，或把 sync 與對賬拆成獨立子指令，讓它不依賴轉錄那半跑不跑得動）。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                                                                                                                                                         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                                                                                                                                                           |
| Timestamp 精確               | ✅                                                                                                                                                                                                                                           |
| Handoff 三態已審視           | ✅                                                                                                                                                                                                                                           |
| HG11 機器身份                | ✅ `ghs_` App token，`{"issues":"write","metadata":"read"}`                                                                                                                                                                                  |
| HG12 git archive             | ✅ `git add docs/feedback/archive/`（本輪無新增檔）                                                                                                                                                                                          |
| HG12b archive-reconcile      | ✅ 74/74                                                                                                                                                                                                                                     |
| HG12c comment-reconcile      | ✅ 73/74（1 份為上游刪留言，非破口）                                                                                                                                                                                                         |
| `check-parallel-actor.sh`    | ✅ CLEAN（入口跑）                                                                                                                                                                                                                           |
| 自我檢查工具                 | ⚠️ `article-health --profile=memory-diary` hard=0，score 12 > budget 8（來源全是 memory 固有結構：handoff 清單佔比、零腳註零 URL）。同日 data-refresh-am 13、spore-harvest 8，屬 OBSERVER-QUEUE #24 待重校的那個家族，不為了壓分數刪 handoff |
| `memory-index-lint.py`       | ✅ 最新 index row ≤ 150 字                                                                                                                                                                                                                   |

file=0 reject=0 skip=0 hold=0 · 開的 issue：無。

## Handoff 三態

繼承上一 session（`2026-08-14-064141-twmd-spore-harvest-am`）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選）
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [x] ~~pending（給 self-evolve）— 讀者對既有 issue 的後續補充一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支~~ 仍 pending，本輪無新事證（維持繼承）
- ⏳ blocked（等部署）— 西里爾字型修補只驗到機制與字型度量，視覺確認要等這版上線
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文媒體數 0，補圖 ROI 高
- [ ] pending（給 self-evolve）— UI 字串閘門只查了 `src/i18n/`，`src/config/`／template hardcode／`src/scripts/` 三個來源還沒有人找洞
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名現在是拉丁品牌名，要不要找 ar 母語貢獻者做真正的阿拉伯文譯名
- [ ] pending（給下次 maintainer 或哲宇）— fork-census 新增 3 個子代 sighting（Malaysia.md / Branding.md / weilinlai719 vanilla 複本），持續在案未接觸
- [ ] pending（給哲宇，Bucket D 待拍板，連續第四輪）— #171 X 回覆 @TaiwanAny 策略疑慮，per §自主權邊界政治立場條款不自動回覆
- [ ] pending（給下次 harvest）— #170/#171 D+4 續追、#171 X 登入牆擋住的回覆累積至 3 則未讀
- [ ] pending（給 self-evolve，工具邊界）— worktree 隔離不擋 Bash 對共享 checkout 的非 git 寫入
- [ ] pending（給哲宇，判斷題）— 德文要不要開。PR #1325（tboydar，8 檔已翻好且品質檢查全綠）卡在 `de` 不在語言註冊表
- [ ] pending（給下次 maintainer）— idlccp1984 剩四個 PR（#1304 #1324 #1326 #1327）的 heal 未做完，卡點在圖片熱連結授權
- [ ] pending（給 self-evolve）— 本 cycle 用 P2（merge 後再 heal）讓 main 的 deploy 紅了一次，值得評估是否替 routine 環境備好 fork push 路徑

本 session 新 handoff：

- [ ] 🔴 pending（給明天以後每一輪 feedback-triage）— feedback id `b78ee4f5-e1af-4876-93d6-852694246e58` 維持 `status=new`，**不要開成 issue**。哲宇拍板前每輪都會再看到它一次，動手前先讀 [報告](../../reports/feedback-third-party-allegation-hold-2026-08-14.md) 與 OBSERVER-QUEUE #28
- [ ] pending（給哲宇）— OBSERVER-QUEUE #28 兩件事：這筆怎麼收尾（要不要回一句「請向移民署或警察機關提出」），以及分類器要不要長出第三人指控這道閘門（推薦 (b) 先上、(a) 排進有觀察者在場的 session）
- [ ] pending（給 self-evolve）— 保管那半沒有自己的入口：只要轉錄那半因為任何理由停手，留言 sync 與兩道對賬就一起消失。本輪靠 scratchpad 腳本手動補，不是流程給的

## Beat 5 — 反芻

這條線的第一性原理寫得很漂亮：把讀者自己的原話 verbatim 機械性轉錄成 issue，等同代讀者填表單。那個類比在回報內容關於文章時完全成立。今天遇到的是它破掉的地方 — 代填表單的前提是填表人有權處分表單內容，而今天被寫進表單的那個人，從頭到尾沒有出現在這場對話裡。

我造的閘門都站在回報者那一側：有沒有洩漏他的 email、有沒有改動他的字、有沒有替他判對錯。三道全綠。**沒有任何一道站在被寫進去的人那一側**，因為過去八十幾筆回報裡，從來沒有第三個人。

跟 8/11 那輪對照著看蠻清楚的：那次六條閘門全綠而讀者的問題一個都沒解決，是好事沒發生。今天三道閘門全綠，而壞事差點發生。同一種形狀，後果的方向相反。閘門只會回答你問它的問題，而我一直問的是「搬得對不對」。

🧬

---

_v1.0 | 2026-08-14 07:15 +0800_
_session twmd-feedback-triage — cron 07:00 讀者回報轉錄班_
_誕生原因：唯一一筆新回報是不能開成公開 issue 的內容（具名第三人指控），整條轉錄流程沒有對應的攔截位置_
_核心洞察：(1) 忠實度閘門全綠不代表後果安全，這條線上沒有任何一道閘門站在被寫進文字裡的第三人那一側 (2) 轉錄職責與保管職責綁在同一個 `--commit` 開關上，轉錄停手保管就跟著停 — 昨天是零輸入，今天是不可轉錄的輸入 (3) 攔下來之後不要用手改 status，那是 HG12b 誕生時就記過的繞道_
_LESSONS-INBOX 候選：`transcription-gates-guard-fidelity-not-consequence`（新，vc=1，severity high）／`zero-input-cycle-drops-the-reconciliation`（vc=1→2，修補方向擴大）_
