# 2026-08-07-072200-twmd-feedback-triage — 每天都印「掃到 40 份」，沒有一天問過應該有幾份

> session twmd-feedback-triage — cron routine（07:00 Asia/Taipei）
> Session span: 07:00 → 07:40 +0800（~40 min）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=免疫 60（chronic yellow，自 2026-07-05，owner=self-evolve-weekly，非本 routine 職責）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 cron 把讀者站上回報轉成 GitHub issue，接 08:30 twmd-maintainer-am 飛輪。

## 本次跑況

在 main、工作區乾淨。GitHub App token 以 `ghs_` 開頭、長度 383，`--whoami` 回 `{"issues": "write", "metadata": "read"}`，HG11 機器身份確認。dry-run 與 `--commit` 都是 file=0 / reject=0 / skip=0 / hold=0，沒有新 issue 要開。隊列空第七天。

`fetched 0` 這個讀數分不出「真的沒有新回報」跟「Supabase 讀不到而靜默回零」，所以直接打 REST 核了一遍：63 列讀得到（filed 61 / rejected 2），連線正常，`status='new'` 是真的零。

## 讀者七天沒說話，是安靜還是表單壞了

最後一筆讀者回報停在 7/30，到今天 7.2 天。歷史 62 個間隔裡有 2 個 ≥8 天、最長 12.65 天，所以 7.2 天在觀測範圍內。但「在範圍內」不等於「已排除故障」——REFLEXES #38 (f) 那條剛升上來的存活≠生產講的正是這件事：Supabase 讀得到只證明後端活著，不證明讀者送得進來。

所以往投稿路徑追了一層。`src/config/feedback.mjs` 的 `resolveBackendKind()` 在 mode 或兩把 key 任一缺席時會**安靜降級成 github-only**（讀者只會看到一顆連到 GitHub 的按鈕，永遠不會產生任何一列），而那三個值是 build 時由 GitHub Actions repo vars 注入的——這是 REFLEXES #60 silent default 的教科書形狀，壞掉的樣子跟「讀者很安靜」一模一樣。

抓線上 bundle 驗：`PUBLIC_FEEDBACK_MODE:"supabase"`、URL 與 publishable key 都真的 inline 在 `FeedbackWidget` 的 chunk 裡，deploy workflow 三行注入自 7/25 起沒被動過。投稿路徑是通的，安靜就是安靜。**未驗**的一段誠實記下：OAuth 登入本身（policy 要求 `auth.uid() = uid`）沒辦法在不登入的情況下驗，那條留給有人在場時。

## 主權層少了 21 份紀錄，八週沒人發現

隊列空讓今天有餘裕核 archive 那一半職責，結果核出這個 cycle 真正的東西。

`archive-scanned=40`，但 Supabase 有 **61 筆 filed**。逐 id 比對，缺的 21 筆**全部集中在 2026-06-11 一天**，其餘每一天都是 100% 覆蓋。這種乾淨的全有全無是某條路徑整批沒走到才會有的形狀，隨機掉檔不會挑在同一天。

追出來的成因：那天是 justfont 共同創辦人蘇煒翔對同一篇文章逐段勘誤 21 處，batch-cluster guard 依設計把同 slug ≥5 筆判 `hold`（維持 `new`、產 consolidated report 給人類決策，不自動開 22 個 issue，這個判斷是對的）。6/12 由人類收束成單一 issue #1145、21 條全數查證採信、全文重寫 `ef8fab38e`，然後把那 21 列補標 `filed`。**而 archive 的寫入只掛在 `triage.mjs` 自己 file 一筆時的副作用上**——狀態改了、issue 開了、文章改了，唯獨主權層那份 markdown 沒有人寫。

讀者的回報沒有丟（Supabase、issue、重寫後的文章都在）。丟的是那份「BaaS 死了還在、可 grep 可 diff」的紀錄，也就是 HG12 白紙黑字承諾的那件事。

真正該記的是**為什麼八週沒人看見**：8/05、8/06、8/07 三個連續 cycle 的 memory 都把「archive 40 檔」寫成健康數字。40 是誠實數出來的，沒有人說謊。錯在那是單邊的帳。`archive-scanned` 數的是現有的檔，而缺席不留痕跡——不拿另一邊的 61 來比，缺的那 21 份永遠不會浮出來。昨天那份 memory 甚至還特地為 `synced=0` 做了跨源複核，卻沒想到對 `scanned` 本身也該問一次「應該是多少」。

## 補了資料，也補了那支會叫的儀器

**資料**：21 份紀錄用 canonical `buildArchiveRecord()` 補齊，不手寫（手寫會生出格式漂移，而且正是 pure function 存在的理由）。全 61 份掃過零 email，HG2 通過。issue #1145 的維護者回覆已 sync 進各自的 §溝通紀錄。現在 61/61。

**儀器**：`reconcileArchive()` 純函式進 archive.mjs，收官改印 `archive-reconcile=N/M`，有缺口就 `⚠️` 加列 id，Supabase 讀不到印 `unavailable` 並在 pipeline 明寫「不准把沒對賬讀成對得起來」。5 個 unit test，其中一個直接把 2026-06-11 那次的形狀（61 filed / 40 archived / 21 missing）寫死當回歸樣本，全套 40 tests 綠。

回溯驗過一次才敢說它有用：把 8/6 那一刻的兩邊帳餵進去，會印 `⚠️ archive-reconcile=40/61 · filed 但無 git 紀錄 21 筆`。這支儀器若八週前就在，第一個 cycle 就會叫。

HG12b 同波寫進 pipeline v1.3、薄殼 skill、cron mirror 三層。

## 昨天說已經同步的那一層，其實沒有

今晨這條 routine 收到的 cron prompt 仍寫「機器身份（2026-07-25 起，**HG10**）」與「收官前 git add（**HG9**）」——也就是 v1.2 之前的撞號版本。但 v1.2 的 changelog 已經聲稱「同波同步薄殼 skill 與 cron mirror」。

repo 內那兩層確實改了，`~/.claude/scheduled-tasks/` 那層從未被動到。當時的驗證是 `grep 對照表驗證零殘留撞號`，而那個 grep 只掃了 repo——**「已同步」是自報，不是量出來的**（REFLEXES #69，而且諷刺的是這正是昨天那條 entry 自己在講的病，換到修補聲明層再發一次）。

routine-sync 也接不到這個：今晨 05:37 第十四輪回報「18 條全 in-sync 零漂移」，因為它對賬的是排程設定與 prompt 存在性，不是 prompt 內文對 canonical 閘門編號的語意一致性。

本輪已修 cron mirror 兩處編號 → HG11／HG12，並補上 HG12b。原 LESSONS 條目的「✅ 已落地」改成部分落地更正，vc 1→2。

## 閘門逐條

| Gate  | 結果                                                            |
| ----- | --------------------------------------------------------------- |
| HG1   | ✅ BECOME review 全過                                           |
| HG2   | ✅ 全 61 份 archive 掃過零 email（含新補 21 份）                |
| HG3   | ✅ 讀者文字未改寫（補檔走 canonical 產生器，scrubSecrets 照跑） |
| HG4   | ✅ 每份帶 feedback_id                                           |
| HG5   | n/a（0 筆新進）                                                 |
| HG6   | n/a（0 筆新進）                                                 |
| HG7   | n/a（無狀態回寫，既有 status 未更動）                           |
| HG8   | ✅ 沒開 issue、沒回覆、沒 close、沒 merge                       |
| HG9   | n/a（fence 無新讀者文字）                                       |
| HG10  | n/a（injection 路徑未走到）                                     |
| HG11  | ✅ `ghs_` App token，issues:write + metadata:read               |
| HG12  | ✅ 61 份落 git                                                  |
| HG12b | ✅ `archive-reconcile=61/61`（本輪新增的閘門，首跑即綠）        |

## Handoff 三態

- `[ ]` **pending** — 21 份補檔與 HG12b 已 ship，但**沒有解掉根因**：batch-cluster hold 那批仍然要靠人類在 triage 之外補標 `filed`，下次再來一次 cluster，archive 一樣不會自動生成，只是這次收官會叫。真正的修法是讓收束動作本身也寫 archive（或讓對賬失敗時自動補檔），需要決定 cluster 收束要不要有自己的 SOP 入口 — 留 distill / self-evolve。
- `[ ]` **pending** — 讀者投稿七天靜默，站體側已驗通（bundle 內 mode/URL/key 齊全），**唯獨 OAuth 登入流程未驗**（要真的登入才驗得到，不在無人值守能力範圍）。若 8/10 前仍零新進，建議有人在場時手動走一次完整投稿。
- `⏳` **blocked — 等哲宇** — Chrome MCP 連續三天故障（8/5 未登入 → 8/6 未登入 → 8/7 完全未連線，LESSONS vc=3），是昨晨 spore-harvest 留下的最高優先 handoff，本 routine 不碰但確認仍未解，continue 傳遞。
- `[x]` ~~retired — cron mirror HG 編號撞號（8/6 條目誤記為已三層落地）~~ — 本輪實測發現並修掉，retired by 2026-08-07-072200-twmd-feedback-triage。

## 給下一個 session

隊列空第七天不是問題，投稿路徑已驗通。真正要接的是上面第一條 pending：**這次補的是資料，根因還在**。cluster 收束路徑與主權層之間那條縫，下次有 ≥5 筆同 slug 回報時會再張開一次。
