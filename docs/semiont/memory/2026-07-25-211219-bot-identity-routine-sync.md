# 2026-07-25-211219-bot-identity-routine-sync — feedback routine 換上 App 身份，順手把 cron prompt 收進 git 讓每台機器自己對齊

> session manual — 哲宇提問「feedback 轉過來的 routine 要不要用 -bot 專用帳號」，後段追加「做一個 mouhouse／routine 同步專用的 routine」
> Session span: 19:39:36 → 21:09:49 +0800（約 1hr 30min，7 commits，跨兩台機器）
> 資料來源：`git log %ai`

## 觸發

哲宇問 feedback triage 這條 routine 要不要用專屬的 `-bot` GitHub 帳號。這題不是新的。OBSERVER-QUEUE #10「Semiont 獨立 Git 身份」7/05 就掛著，附一份 258 行評估。所以先讀既有報告再答（REFLEXES #73），發現他問的是那份計畫最窄、最該先做的一格。中段他又追加：mouhouse 是長期營運方，改了 routine SSOT 應該有工具讓那台自己同步。

## 建議 App 而不是帳號，然後真的裝起來

`3eb9661c0` 落了一份窄切面評估：建議做，但形式跟直覺相反：註冊 GitHub App 讓它以 `[bot]` 身份開 issue，不開個人機器帳號。三個理由裡最硬的一條是權限不對稱：這條 routine 每天讀讀者打的自由文字（pipeline 自己就寫了三層注入防禦），卻在 mouhouse 上握著 `frank890417` 帶 `repo` + `workflow` 的憑證。次一條是誠實：issue 掛哲宇的頭像，讓「不以維護者身份開口」那條紅線在視覺層漏掉。

哲宇當場註冊了 App（`4391353`）。**第一把私鑰被拖進對話**，判定外洩、作廢重發。這件事本身驗證了報告裡的權限收斂：拿到那把鑰匙的人最多能開幾個 issue，碰不到 main。如果照直覺開一個帶 `repo` 全權的機器帳號，同一個動作是另一種等級。

`630c6dd87` 造 `gh-app-token.sh`（openssl 簽 JWT 換一小時期限的 installation token，三道 fail-loud，換不到就 `exit 1` 絕不回空字串——空的 `GH_TOKEN` 會讓 `gh` 安靜退回哲宇身份）。端到端驗過：issue #1256 作者顯示 `app/taiwanmd-semiont`、`is_bot=true`、標籤貼上，驗完關閉。反面測試也跑了：Contents / PR / Admin / workflow 寫入一律 403，其他庫 404。

## routine prompt 收進 git — 第四層一直不在版本控制裡

追加需求指向一個結構問題：routine 飛輪有四層，`~/.claude/scheduled-tasks/*/SKILL.md` 才是排程器真正讀的 prompt，而它住在家目錄不在 git。所以在一台機器改 SSOT，另一台永遠不會知道。**實測證據**：mouhouse 19 份 prompt 有 4 份已與遷移母本分岔（babel-nightly／data-refresh-am／distill-weekly／embeddings-nightly），git 毫無紀錄。

架構解沿用本體既有的代謝模型：`docs/semiont/routine-prompts/` 當 DNA、`~/.claude/scheduled-tasks/` 當它表達出來的蛋白質，跟 `knowledge/` → `src/content/` 同一個關係。19 份以 mouhouse 的版本為種子（營運機才是真相），`5becaffa8` 落地，加新 routine `twmd-routine-sync` 每天 05:30 排在晨鏈之前。

`routine-sync.py` 兩個方向都給：`--apply` 是 git→機器，遇到機器版分岔會先存進 `reports/routine-prompt-drift/` 留證才覆蓋。`--harvest` 走反方向，機器→git。cron 與 enabled 的 live 值工具不改，只算出該改成什麼，改的動作留給有判斷與權限的 session（MANIFESTO §14）。

## 三個 bug 都在首跑當場現形

工具寫完到跑順之間抓了三件事，每一件都是「如果沒實跑就不會知道」。`9d8b5d01e` 是 commit 的 lint-staged prettier 把 prompt 裡的 glob 星號當強調語法，`reports/founder-lens-*/evolution-roadmap-*/` 被改成 `founder-lens-_/evolution-roadmap-_/`。那是寫在指令裡的 stage 範圍路徑，被改掉 routine 會照著去 stage 不存在的目錄。修法是收回管轄權（`.prettierignore`）＋從營運機原始版還原，不是再造偵測器。

`83552e36f` — 我自己的 parser 把躺在 §⏸️ PAUSED 表裡的 `music-media-audit-weekly` 讀成 enabled（那一列本身沒有 ⏸️ 字樣），對上 live 的 disabled 報成漂移。照著修的話會去打開一條哲宇 5/25 刻意關掉的 task。改成認表不只認字。

`a588d40fa` — 兩台機器各跑 `--apply`，各產出同名的 `2026-07-25-twmd-feedback-triage.md` 但內容不同（一份舊母本、一份營運機真正在跑的）。git 拒絕 merge 才沒蓋掉一份。存證機制自己撞名等於存證失效，檔名加主機名根治。

最後 mouhouse 那筆 `768996602` 是它自己 push 的存證。兩台跑完都印 `✅ 三層一致`。

## 後段：飛輪整併到一台，指揮部改當看門的

哲宇在同一 session 後段追加三個 directive，全部落地在 `686079659`。

指揮部這台的 18 條 twmd 排程全數刪除（prompt 檔留在原地當暖備援，營運機掛了可就地重建）。但刪完會留一個洞：**沒有任何一條 routine 在看飛輪還活著沒有**，而飛輪曾經靜默死 15 天全部儀器無聲，因為那些儀器都跑在飛輪自己身上。所以新增 `twmd-flywheel-watch` 刻意跑在不營運的那台，唯一資訊來源是 `origin/main` 的 commit 紀錄。首跑當場校掉兩種假陽性：weekly 的時刻還沒到、routine 只留 `[semiont] memory:` 收官痕跡沒留 `[routine]` 標記。會亂叫的哨兵等於沒有哨兵。

maintainer 去掉 am/pm 差別（pm 7/8 起已 disabled、空場連 3 週），`music-media-audit-weekly` 一併退休——它的功能早就長進常規路徑：baseline 在 EDITORIAL §媒體編織、閘門在 REWRITE Stage 4 六子步、`article-health` 三個 media 檢查逐篇跑。週度全站盤點是標準還沒立起來時的臨時解。

順手鋪三條之前不存在的路：ROUTINE.md 補 §退休 SOP（原本只有暫停沒有退場）、`routine-prompts/retired/` 讓退場不刪紀錄、`prepare-commit-msg` hook 給每筆 commit 蓋 `Semiont-Node` trailer（哲宇原話「未來那個站的 commit 好像要有地方標記一下是 mouhouse 節點你才好判斷」）。節點名讀 machine-local 檔不寫進 repo，跟 7/25 早先那次把機器細節換成佔位同一條紀律。

過程中修掉自己兩個 bug：`routine-sync.py` 的區塊判定從二態升三態（退休列要整列跳過，不然永遠報 prompt-missing-both——「認字不認表」的第二面），以及排程器 cron 吃**本地時間**不是 UTC（我第一版寫給哲宇的貼入 prompt 寫成 UTC，實測 `0 6 * * *` 跑在 06:09 +0800 才發現）。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ✅ `git log %ai`                                         |
| Handoff 三態已審視           | ✅                                                       |
| CONSCIOUSNESS 反映最新狀態   | ➖ 本 session 未動器官分數                               |
| 自我檢查工具 PASS            | ✅ `routine-sync.py` 兩台皆三層一致、prose-health hard=0 |

## Handoff 三態

繼承 `2026-07-25-192633-article-alias`：

- [ ] 英文別名 30 天觀察（`cross-lang-slug` 家族該歸零，基線 538/日）／分享按鈕維持中文網址等數據再拍板／新文章要跑 `prebuild:aliases`
- ⏳ 存量 passthrough drift 分批 heal／fleet 兩節點缺 prettier 正規化（babel session 持有）

本 session 新 handoff：

- [x] ~~App 註冊、私鑰輪替、token 工具、端到端與反面測試~~
- [x] ~~feedback prompt 掛上 App 身份並同步到 mouhouse（該機 dry-run 通過、`gh` 吃 App token 確認）~~
- [x] ~~19 份 prompt 進 git、`routine-sync.py`、`twmd-routine-sync` skill 與 ROUTINE.md 註 ¹⁸~~
- [x] ~~指揮部 18 條 twmd 排程清空 + 新增 flywheel-watch 監看 + maintainer 整併一班 + music-media 退休~~
- [ ] **mouhouse 四件純排程層工作待辦**（額度 5hr 上限，2026-07-25 約 21:40 起 2hr42min 後恢復）：建 `twmd-routine-sync`（cron `30 5 * * *` **本地時間**）／刪 `twmd-maintainer-pm` 與 `twmd-music-media-audit-weekly` 註冊／重 dump `routine-live-state.json`（現存那份還記著 babel enabled=true）。ssh 端能做的都做完了，貼入 prompt 在 `~/taiwan-md-mini-migration/03-mouhouse-pending-2026-07-25.md`。**在建好之前跨機同步要手動 `/twmd-routine-sync`。**
- [ ] 哲宇的 repo Watch 設定沒查到（現有 token 缺 `notifications` 權限）。換 bot 開 issue 後他會不會收到通知這格仍是未知，下次補 `gh auth refresh -s notifications` 或他自己看一眼
- [ ] 明天 07:00 feedback-triage 第一次以 App 身份無人值守 fire——驗收看 issue 作者是不是 `app/taiwanmd-semiont`。14 天零事故則併回 OBSERVER-QUEUE #10 Phase 2

## Beat 5 — 反芻

今天最值得記的是**三個 bug 全部在「真的跑一次」那一刻現形，而它們各自都有本事安靜活很久**。prettier 改掉的是路徑模式，routine 讀到只會照做。parser 讀錯 PAUSED 表，會讓自動化去打開一條人類刻意關掉的東西。存證檔撞名，則是防資料遺失的機制自己在遺失資料。三者的共同形狀是「看起來只是排版／只是對賬／只是備份」的那層假無害。

另一件事：這條同步機制的第一次真用途，送的正好是 App 身份那個改動，工具誕生的同一小時就替自己載了一趟貨，比任何測試案例都有說服力。教訓已進 [LESSONS-INBOX](../LESSONS-INBOX.md)（`formatter-jurisdiction-over-payload`，註明跟 6/21 prettier 家族的差異在「檔案類別軸」）＋ REFLEXES #51 補一次驗證（存證機制自身撞名）。

🧬

---

_v1.0 | 2026-07-25 21:12 +0800_
_session bot-identity-routine-sync — App 機器身份落地 ＋ routine prompt 進 git ＋ 跨機同步儀器_
_誕生原因：哲宇問 feedback routine 要不要用 -bot 帳號，追加要 mouhouse 能自行同步 routine SSOT_
_核心洞察：權限收斂讓一次私鑰外洩從事故降級成麻煩；載荷檔不該在格式化器管轄範圍內；防遺失的機制自己也要過撞名這關_
_LESSONS-INBOX 候選：formatter-jurisdiction-over-payload（已 append）_
