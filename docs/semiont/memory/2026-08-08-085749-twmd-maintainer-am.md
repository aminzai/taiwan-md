# 2026-08-08-085749-twmd-maintainer-am — 兩個 PR 修好免疫層的靜默失效，往下再挖出一道從沒活過的閘門

> session twmd-maintainer-daily — cron 08:30 am 例行維護
> Session span: 08:30:00 → 09:00:00 +0800（約 30 分鐘，3 commits）
> 資料來源：`git log %ai` / `gh issue list` / `gh pr list` / `gh api graphql`（discussions）/ `gh run list` / `verify-internal-links.sh` / `git -c core.quotepath` 實測 / `check-slug-consistency.py` 全量掃描 / 假 HOME 重現 CLI 獨立安裝

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，2026-08-08 08:32 跑）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 08:30 maintainer cron。BECOME review mode 完整跑 Step 0-9：wake-context 216,839 bytes / 1,268 行 / 11 段，用 Read 分頁讀到末行 `wake:END` sentinel，selftest 10 項全綠，零 head/tail 節選。Review subset self-test 全過後才進 Stage 1。

## Stage 1 SCAN — 連續第三天有真 backlog

| 項目             | 讀數                                                                     |
| ---------------- | ------------------------------------------------------------------------ |
| open PR          | **2**（#1298 / #1300，皆 stantheman0128，皆 MERGEABLE/CLEAN）            |
| open issue       | 8，其中 3 筆為昨日新進（#1297 / #1299 / #1301），全部有 label            |
| open discussion  | 11，全部至少一則維護者回覆，無 48hr 未回應者                             |
| 過去 24hr commit | 15 筆（10 筆 routine fire），48hr 累計 77 筆                             |
| build            | ✅ green（main deploy CI 最近三次 success，中間 cancelled 為併發取消）   |
| broken-link      | ✅ **0.22%** gated（門檻 7.0%）— 但 `dist/` 停在 8/05，這個數字有 3 天齡 |
| 免疫器官         | 🛡️ 60（yellow 自 2026-07-05）                                            |

PR triage 規模 2 < 5，未觸發 High-stake 強制升 Full。工作樹 clean。空場 vc 不適用（連三日有 fresh 場）。

## 兩個 PR：貢獻者報的是免疫層在靜默漏水

兩個 PR 都來自 stantheman0128，兩個動的都是閘門本身。**沒有照 PR 描述採信，兩條機制都自己驗過**（REFLEXES #31）。

`#1298` 修 `.husky/pre-commit` 的兩處。第一處是 `core.quotepath`：git 預設會把中文檔名輸出成 `"knowledge/About/\345\217\260..."`，開頭多一個雙引號、內容整串 octal-escape，於是 `grep '^knowledge/.*\.md$'` 一條都對不上。實測目前 zh-TW 有 **867 篇**中文檔名，而吃這個變數的除了 frontmatter auto-fix，還有 **article-health 那道 11-plugin pre-commit hard gate**（2026-05-04 Phase 10 上線）——主要的內容免疫閘門對中文檔名文章從來沒有生效過。第二處是 `staged_any` 的賦值排在第 246 行，而第一個消費者 language registry sync check 在第 147 行，拿到的永遠是空字串，2026-04-14 上線至今沒跑過。

合併前多做一件事：提前賦值後憑證掃描會第一次真的讀到中文檔名文章，所以拿它那五組 pattern 對全部 4,888 篇中文文章乾跑一次，**0 個誤報**，確認不會突然擋住大家的 commit。

`#1300` 是五支腳本的 Windows cp950 編碼修補。五支都在 worktree 裡實際執行過，不是只做 `ast.parse`——那條教訓是 7/24 mouhouse 遷移換來的。macOS 上輸出與行為零變化。

兩個都 squash merge（`2b625bfca` / `5e69cab42`），已用中文留言說明驗證方式，對應的 #1297 / #1299 隨 merge 自動 close，我補上 commit hash 與實測數字。

## 順著同一條線往下讀，發現一道從沒活過的閘門

修 `staged_md` 時順手把 `.husky/pre-commit` 讀完，撞到一件 PR 沒提的事。第 103 行 `staged_md` 的定義結尾排除了 `en|ja|ko|es|fr`，第 136 行卻拿 `staged_md` 去 grep `ja|ko|es|fr`——**條件恆為 false**。那是 2026-07-17 為了防止 98 檔 slug 漂移重演而設的閘門，上線至今從未執行過一次。全量掃描目前有 **12 筆真實漂移**（`computex-taipei` / `i-am-from` / `founder` 三組 × 四語）。

同一個檔案裡還有第二個形狀相同的東西：第 160 行專門抓「寫死語言清單」的 detector 只掃有副檔名的檔案，而 `.husky/pre-commit` 沒有副檔名，所以它從沒掃過那個自己就寫死了兩處語言清單的檔案（註冊表有 11 個語言，hook 寫 5 個）。這一項實測目前無損害：ar/hi/id/pt/ru/vi 共 3,933 檔的 `translatedFrom` 缺失數是 0，babel dispatcher 寫得正確，所以是地雷不是傷口。

**沒有當場修，理由是耦合**：修 wiring 只要三行，但閘門一活，那 12 筆既有漂移就會開始擋住任何碰到它們的 commit。而清償 12 筆要 `git mv` + 補 301 + 改 `_translations.json`，動到線上 URL，命中 §自主權邊界。兩者綁在一起，整包留給觀察者（選項見 §Handoff）。

過程中差點被自己騙一次：我先把 `check-slug-consistency.py` 複製到 repo 外跑，拿到 `✅ 0 檔全部與 en 對齊`，把它當成全站通過寫進判斷。是後來兩把尺對不上才回頭查，發現那支腳本**掃到零個檔案時印的綠勾跟全數通過逐字相同**。這條已 append 進 LESSONS 既有 pattern（第三個 instance）。

## CLI 的兩個 Windows / 獨立安裝問題

issue #1301（ian0953329333）報兩件事，都確認並修掉，commit `b49b40cf6`。第一件單純：`sync --force` 直接呼叫 shell 的 `rm -rf`，Windows 沒這個指令，改用 Node 的 `rmSync` 就好，回報者自己也猜到了原因。

第二件比較有意思：`read` / `cite` 在獨立安裝下找不到任何文章。跟回報者猜的 sparse checkout 無關，是路徑差一層。`sync` 把整個 repo clone 進 `~/.taiwanmd/knowledge/`，文章因此落在再下一層，而 `sync.js` 自己算摘要時用的是那個較深的路徑，讀取端 `getKnowledgePath()` 回傳的卻是 clone 根目錄。同一個套件裡兩個檔案對「知識庫在哪」的答案不一致。`hasLocalData()` 又只檢查「根目錄底下有沒有任何子目錄」，`.git` 也算數，所以同步回報成功而讀取是空的。

驗證用假 `HOME` 重現回報者的目錄結構，修復前 `getArticleFiles()` 回 0 篇、修復後正常。in-repo 路徑仍是 886 篇不變，扁平舊版面 fallback 另外測過。issue 保留 open，等回報者在真的 Windows 上確認 `--force`（我沒有 Windows 環境，那一半是照 `rm` 這條路徑推的，已在回覆裡講明）。

## 收官 checklist

| 檢查項                       | 狀態                           |
| ---------------------------- | ------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                             |
| Timestamp 精確               | ✅（`git log %ai`）            |
| Handoff 三態已審視           | ✅                             |
| open issue 都有 label        | ✅（#1301 本次補 `bug`）       |
| open PR ≤ 5d 都有 review     | ✅（兩個都已 merge + 留言）    |
| broken-link < 門檻           | ✅ 0.22% < 7%（附 3 天齡但書） |
| build green                  | ✅                             |
| 連續空場 ≥ 3 cycle           | ✅ 不適用（連三日有 fresh 場） |
| 自我檢查工具 PASS            | ✅ pre-commit / pre-push 全綠  |

## Handoff 三態

繼承（非本 session 新產生，接住不動）：

- [ ] pending（給哲宇）— #1184 justfont 後台網域白名單、免疫黃燈連 28+ 天且三選一待拍板
- [ ] pending（給哲宇）— cron 環境無 Gmail MCP（supporters-weekly checkpoint 停在 2026-07-12）
- [ ] pending（給哲宇）— 黃崇仁 #165/#166 Bucket D「是否洗白」框架質疑待拍板
- [ ] pending（給哲宇）— Discussion #104 對外合作建議，已回覆告知需哲宇拍板，尚待回應
- [ ] pending（給哲宇，最高優先，連續第 5 天）— Chrome MCP 擴充功能完全連不上，spore-harvest 連四天中止
- [ ] pending（繼承不動）— 本機 `dist/` 只在有人手動 build 時才更新（本 cycle 的 broken-link 讀數因此帶 3 天齡）
- [ ] pending（給下次碰 EMBEDDING-PIPELINE.md 的 session，vc=2）— Stage 3 commit template co-author 行寫死跟實際 cron 模型不符
- [ ] pending（繼承，8/5-8/7 累積未 ship）— 3 則 Bucket E reply draft 待 Chrome MCP 恢復後補發
- [ ] pending（給 self-evolve-weekly）— 8/07 `check-disabled-by-default-reports-green` 與 8/08 `error-and-emptiness-share-one-return` 是否合併升獨立反射。**本 cycle 補上第三個 instance，且是輸出端**，建議直接判不必再等

本 session 新 handoff：

- [ ] **pending（給哲宇，需拍板）— slug 一致性閘門接錯線且有 12 筆既有漂移**。閘門自 2026-07-17 從未執行（`staged_md` 排除了它要 grep 的語言）。三個選項：
  - **Option A**：先清償 12 筆（`git mv` + `config/redirects-manual.txt` 補 301 + `_translations.json`）再修 wiring。成本最高，但結束後閘門真的守得住。動到線上 URL。
  - **Option B**：修 wiring + 把 12 筆放進腳本既有的 `ALLOWLIST`（附日期註記）。成本約 30 分鐘，**新漂移立刻被擋**，舊債留紀錄慢慢還。腳本註解寫「新檔案不得加入」，所以要哲宇同意把這 12 筆定性為既有債而非新檔。
  - **Option C**：維持現狀，只留 LESSONS 紀錄。成本 0，但閘門繼續是裝飾。
  - **推薦 default：B**。它讓「防再犯」這個原始目的立刻生效，而 URL 變更那一段可以獨立排程，不必綁在一起。
- [ ] pending（給任何碰 `.husky/pre-commit` 的 session）— hook 兩處寫死 5 語言（第 58 / 103 行）而註冊表有 11 個。hardcoded-lang detector 因 hook 沒副檔名而掃不到它。目前 0 損害（3,933 檔 `translatedFrom` 缺失為 0），屬地雷不屬傷口。
- [ ] pending（低優先）— `knowledge/en/` 有 4 篇缺 `translatedFrom`，皆為 2026-04-14 閘門上線前的舊檔。其中僅 `handmade-taiwanese-cuisine.md` 可機械對回 `Food/台灣手路菜.md`，另 3 篇無明顯 zh 對應，**不猜**（猜錯等於捏造譜系）。
- [x] ~~#1297 / #1299 待處理~~ — 隨 #1298 / #1300 merge 解決，已補 commit hash 回覆，retired by 本 session
- [ ] pending（等回報者）— issue #1301 保留 open，等 ian0953329333 在 Windows 確認 `sync --force` 是否真的通了

## Beat 5 — 反芻

今天兩個 PR 的價值不在那十行 diff，在它們證明了一件事：**這個生命體最主要的內容免疫閘門，對 867 篇中文檔名文章從來沒有生效過**，而站上每天照常印綠燈。發現它的是一個在 Windows 上裝不起來的外部貢獻者，我自己的儀器一支都沒叫。他因為環境跟我不同，才看得見我看不見的東西。這正是 REFLEXES #69「每層自評都需要外部尺」最字面的形狀。

更值得記的是我自己在同一個 cycle 裡踩了一次一模一樣的坑。我把 `check-slug-consistency.py` 複製到 repo 外跑，拿到綠勾就當它是全站通過。那個綠勾的真正意思是「我一個檔案都沒掃到」。差別只在於我剛好因為別的線索回頭查了。一支檢查器騙過的第一個人，是拿它來檢查的那個人。今天三個獨立的東西（footnote-url 預設關閉、seo-meta 語言排除、這支腳本的空掃描）指向同一句話：**「不知道」必須有自己的符號，不能借用「沒事」那個**。這件事已經累到第三個 instance，我在 handoff 裡建議 self-evolve 不要再等第四次。

還有一個我當下想直接動手、後來停住的地方。那道死掉的 slug 閘門，修 wiring 只要三行，手很癢。但修完它會立刻變成陷阱——12 筆既有漂移會開始擋人，而清償那 12 筆要動線上 URL。把一個乾淨的三行修補跟一個需要拍板的 URL 決策綁成一包送出去，那並不算「能做就做完」。所以我把它拆成三個選項附成本留給哲宇，而不是自己選一個。

🧬

---

_v1.0 | 2026-08-08 09:00 +0800_
_session twmd-maintainer-am — 2 PR merge（皆修免疫層靜默失效）+ 3 issue 回覆 + CLI 兩個 Windows/獨立安裝修補_
_誕生原因：每日 08:30 maintainer cron，連續第三天有真 backlog_
_核心洞察：(1) article-health pre-commit hard gate 對 867 篇中文檔名文章從未生效，發現者是環境不同的外部貢獻者 (2) slug 一致性閘門的 guard 條件過濾掉了它自己要找的東西，上線至今零執行 (3) 檢查器空掃描印出的綠勾跟全數通過逐字相同，我自己當場被騙了一次_
_LESSONS-INBOX 候選：新開 `gate-guard-contradicts-its-own-filter`（vc=2）；`check-disabled-by-default-reports-green` append 第三個 instance 並建議直接升反射_
