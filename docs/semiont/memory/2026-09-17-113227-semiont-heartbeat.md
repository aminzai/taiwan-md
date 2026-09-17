# 2026-09-17-113227-semiont-heartbeat — 本機 main 分岔 7 天（+318／-74）的合併，8 篇打撈完稿，追刷 tracker

> session semiont-heartbeat — 排程心跳（`~/.claude/scheduled-tasks/semiont-heartbeat`，daily full BECOME + HEARTBEAT）
> Session span: 約 11:00 → 13:00 +0800（依 commit timestamp 推算，本檔為事後補記）
> 資料來源：`git log`、`git merge-tree`、wake-context selftest、`docs/semiont/memory/2026-09-1[5-7]*.md`

✅ BECOME ack：mode=full（排程心跳強制升 Full）/ wake-context selftest 開場即亮 ⚠️ 落後 origin 74 commit + ⚠️ handoff 空

## 觸發

排程心跳照 §Boot 流程跑 `wake-context.py`，selftest 開場就是全紅：本機 main 落後 origin/main 74 個 commit、領先 318 個（實測後更正為落後 74／領先 318，selftest 印的方向沒錯，數字跟本輪實測一致）。這台機器（此 working directory）過去幾天的維護班全部改走掛 `origin/main` 的獨立 worktree 操作（見 09-15〜09-17 三份 maintainer memory 的「本機 main 不 pull 不 push」慣例），本機 main 本身則被冷落——babel dispatcher 在這裡跑，但沒有任何東西在這裡跑 `git push`。

## 診斷：分岔不是新聞，是本機 main 這個特定 working directory 第一次被指派去處理它

`git merge-base` 顯示兩側從 09-10 一個共同祖先開始各自前進：本機側 318 個 commit（09-10〜09-15，幾乎全是 babel 批次）、origin 側 74 個（09-11〜09-17，maintainer routine 直接寫 origin worktree 產生）。這正是三份 maintainer memory 反覆記的「main 本機未推 commit 與 origin N 個真分岔」，數字從 09-15 的 181/09-16 的 193/09-17 早上的 203 一路長大——那些數字量的是 origin 這一側能看到的落後量，跟我在這裡量到的「318 領先」是同一個分岔的兩個面。

## 修復：merge（非 rebase），7 個 add/add 衝突全解

`git merge-tree` 先驗過零衝突信心過高——實際 `git merge origin/main` 跑出 7 個 add/add：兩側各自把同一批中文原文獨立翻成同語言（ar/校園順口溜韻文對照、hi/桃園埤塘、hi/帕拉告、id/工班換工、id/IG 在台灣、id/開源精神、ru/黃土水），都是 `sourceCommitSha` 相同、純粹重工。裁決規則：留 `translatedAt` 較新的一版（6 篇取 origin、1 篇取本機），全部有 schema 更完整（`sourceContentHash`/`sourceBodyHash`）佐證判斷方向。Merge commit `0b2883cfd`，push 成功。

選 merge 不選 rebase：rebase 318 個 commit 逐一重放，任一步撞衝突都要人工介入；merge 只在最終樹狀態撞一次，且不重寫既有 commit hash（babel 追蹤檔可能引用舊 hash）。

## 打撈：merge 之外還有 8 篇孤兒完稿 + 5 個 tracker 檔案

本機 disk 上還有 8 篇 09-15 babel dispatcher 停擺瞬間的完稿（校園順口溜/ar、台灣蘭花/ar+hi、拉阿魯哇族/hi、帝雉/hi、蔡同榮/id、電網韌性/id、中華民國美學/ko）——寫在磁碟上但 `git add` 都沒做過。逐篇核對 `translatedFrom` 來源檔仍存在、frontmatter 完整含 `sourceCommitSha`/`translatedAt`，判定完稿而非半成品，commit `b44548b9d`。

順手撞到一個值得記的 prettier 病：兩篇蘭花譯文的圖說用 `_整行斜體_` 包住含底線的 Wikimedia 檔名 URL，prettier 每次 `--write` 都把 URL 內部的 `_NN` 咬成 `*NN`（連結因此 404），而且是 idempotent 的壞——單改字元下一次 `--write` 又咬回去。真正的修法是把連結整個移出斜體範圍（linter 自己給的建議），不是改字元。

`_translation-status.json`（用 `status.py` 對現在 HEAD 重算，不是沿用舊快照）、`dashboard-analytics.json`（撿回今早 08:17 已生成但未 commit 的新資料）、`reports/babel/{cascade-exhausted,fail-memo,fail-reasons}.json`（dispatcher 停擺前最後真實跑況）一併 commit（`299018e18`）。

## 沒動的東西，理由寫明

- `reports/research/2026-08/比國家還大的演算藝術-media-staging/`（14MB screenshots，Aug 18-28 遺留）：站上從無任何 `-media-staging` 資料夾被 commit 過的先例，判斷是文章寫作時的暫存素材。不擅自決定去留，留給哲宇。
- OBSERVER-QUEUE #67「babel 可不可以覆蓋投稿者翻好的譯文」的政策決定（open-PR 過濾 / 人寫譯文不覆蓋）：本輪只是把兩棵分岔的樹接回同一棵，不是在執行 #67 的修法。7 個實際衝突遠低於維護班累計提及的「118 篇」，差距沒查清，寫進 [LESSONS-INBOX](../LESSONS-INBOX.md) `unpushed-divergence-silently-redirects-volunteer-effort` 的驗證欄，未開新 entry（DNA-first 查重）。

## Handoff 三態

繼承 `2026-09-17-085150-twmd-maintainer-am`：

- [x] ~~⏳ blocked — 本機 main 未推送 commit 與 origin 真分岔~~ **本輪解除**：merge + push 完成，本機現在落後 0／領先 0（與 origin 同步）。
- [ ] pending（延續，給哲宇）— OBSERVER-QUEUE #67「babel 覆蓋投稿者譯文」政策決定，仍等哲宇拍板選項 B。
- [ ] pending（延續，給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留。

本 session 新 handoff：

- [ ] pending — 「118 篇」與本次實測「7 個 git-level 衝突」的落差沒有查清根因，下一輪若有餘裕可對照更早（09-11〜09-14）的 maintainer 記錄還原完整清單。
- [ ] pending — 8 篇打撈完稿與今日重刷的 tracker 檔案是否已被下游 prebuild/dashboard 消化，尚未驗證（本輪未跑完整 build）。

## Beat 5 — 反芻

分岔的兩個面互相看不見對方：origin 側連續三天的 maintainer session 記著「本機領先 N」卻從沒進來這個 working directory 處理過；這個 working directory 則從沒被排進任何一次心跳、直到今天排程心跳照表操課才第一次真正踩進來。**多核心協調寫的是「怎麼避免同時碰撞」，沒寫「怎麼保證每一棵樹都會被排到」**——這台機器上的本機 main 分岔了 7 天，不是因為沒人知道，是因為每個知道的人都用繞過它的方式把工作做完（掛 origin worktree），而繞過的方式剛好也是正確的短期解，於是分岔本身從沒被排進任何一個人的待辦。

🧬

---

_v1.0 | 2026-09-17_
_session semiont-heartbeat — 本機 main 7 天分岔 merge（+318/-74）／8 篇孤兒完稿打撈／tracker 重刷／2 篇 prettier idempotent 修復_
_誕生原因：排程心跳跑 wake-context，selftest 開場即亮本機落後 origin 74 commit 的紅燈_
_核心洞察：分岔期間「繞過它把工作做完」跟「解決分岔」是兩件事，前者做了 7 天不代表後者有進度——沒有一個排程規則保證每一棵樹遲早會被踩進去處理_
_LESSONS-INBOX 候選：無新 entry。DNA-first 查重命中 `unpushed-divergence-silently-redirects-volunteer-effort`，補驗證欄（vc 1→2）_
