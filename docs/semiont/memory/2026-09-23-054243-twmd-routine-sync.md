# 2026-09-23-054243-twmd-routine-sync — 第 57 輪對賬：babel-nightly 機器版落後兩個月，補上昨夜 01:29 才寫下的白名單落差警語

> session twmd-routine-sync — cron routine（每日 05:30 Asia/Taipei）
> Session span: 05:30 排程 fire → 05:50 +0800（~20 分鐘，1 項 apply + 本 memory commit）
> 資料來源：`routine-sync.py` 兩次輸出（apply 前後）+ `git rev-list --left-right --count HEAD...origin/main` + `git log -- docs/semiont/routine-prompts/twmd-babel-nightly.md` + `diff` 機器版 vs git 版 + `mcp__scheduled-tasks__list_scheduled_tasks` 當下 18 條 live 值

✅ BECOME ack: mode=micro / Q14=PASS

## 觸發

排程任務。讓這台機器的 routine prompt 與排程設定跟 git SSOT 三層對賬，排在晨鏈之前。第 55、56 輪都是零漂移，本輪是分岔併完後第一次真的有東西要搬。

## 一條漂移，方向沒有懸念

`routine-sync.py` 報 18 條裡 1 條 `prompt-drift`：`twmd-babel-nightly`。判方向的兩個依據互相印證——機器版 mtime 停在 7 月 29 日 05:38，git 版是今天凌晨 01:29 的 `012e98176`。`diff` 是純新增六行，沒有任何一行被刪或改寫。git 較新且是 superset，`--apply --stamp 2026-09-23` 寫進機器，舊版存證落 `reports/routine-prompt-drift/2026-09-23-exhibitions-mac-mini-local-twmd-babel-nightly.md`。apply 後重跑，18/18 in-sync、exit 0。

那六行的內容是昨夜 babel 那班自己量出來的：產線核發 worker 用 `--format babel`（輸出格式），而 SQUEEZE §入池門檻的模型級別白名單掛在 `--profile babel`，兩個旗標不是同一件事，沒有人呼叫後者，於是 48 小時內 87% 的譯文出自白名單外的 8.1B 模型。要不要改是 OBSERVER-QUEUE #78，殼層明寫不自行切換，本班照辦沒碰。

**值得記的是那一分鐘**：警語寫在 01:29，babel 的排程 01:30 起跑。今晚那班讀的是舊殼，看不到自己上一班留下的話。git 裡的進化不會自己走到家目錄——這條 routine 就是那段路。

## cron／enabled：這輪多驗了一把尺

工具沒印 ⏰／🔌，兩層零漂移。但我去看了它怎麼比的：`routine-sync.py` 的 live 值讀 `docs/semiont/routine-live-state.json`，不是直接問排程器，而那份鏡像的 mtime 是 09-22 06:07，已經 23 小時。所以它的沉默原本只證明「跟一份舊鏡子沒有差」，證明不了「跟現在的排程器沒有差」（REFLEXES #82 的形狀：量的是替身）。

拉 `list_scheduled_tasks` 當下的 18 條逐條對回鏡像，`cronExpression` 與 `enabled` 全等，零差。四條 disabled（`rewrite-daily`／`founder-lens-weekly`／`spore-pick-daily`／`spore-publish-daily`）與 ROUTINE.md ⏸️ 表一致，沒有「SSOT 說開、live 說關」的例外要處理，不需要動 MCP。今天的綠燈站得住，但它站住的理由有一半是我手動補的。

順帶驗了兩件事：git 有 19 份 prompt、機器有 18 個 dir，第 19 份是 `twmd-flywheel-watch`，ROUTINE.md 標 `🖥️commander-macbook`，`routine-sync.py` 讀 `.taiwanmd/node-name.local`（本機 `mouhouse-macmini`）判定不是它的家就整列跳過——缺席是設計不是洞，且註 ²⁰ 要求的 fail-loud 沒觸發（marker 讀得到，stderr 空）。

## 我的檔案被並行的 commit 掃走

`git add` 單檔、`git diff --cached` 驗過只有 1 檔，接著 `git commit` 回「no changes added to commit」——中間 babel dispatcher 的 commit 先落地，共用 index 把我那份存證一起帶進 `0843924f7`（hi 批次 5 篇）。就是 09-22 記過的 `index 共用被並行 commit 掃走`，這次輪到我。

處置：不改寫歷史。babel 正在跑（parallel-check 六個 writer），跨 session 期間禁 destructive git ops（REFLEXES #35），而檔案內容正確、已經在 main 上，損失只是那筆 commit 的訊息沒提到它。敘事由本輪自己的 commit 承擔。**操作上的修補**：下次這類單檔收官改用 `git commit -- <path>`（繞開共用 index），不要 `git add` 之後再 `git commit`，中間那個窗口在這台機器上是常態不是意外。

## 收官 checklist

| 檢查項                       | 狀態                                      |
| ---------------------------- | ----------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                        |
| Timestamp 精確               | ✅                                        |
| Handoff 三態已審視           | ✅                                        |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪無器官狀態變更）              |
| 自我檢查工具 PASS            | ✅（article-health memory-diary profile） |

## Handoff 三態

繼承自 09-22 第 56 輪：

- ⏳ blocked：issue #1729（馬英九腳註，已擴散 12 語）仍 OPEN，等 Write session 帶哲宇 review。`spore-pick-daily`／`spore-publish-daily` 停用未拍板（ROUTINE.md 註 ¹³），本輪 enabled 層對賬一致，未擅自打開。
- [ ] pending（工具候選，1-file，**第 4 輪往下傳，席位已釘 09-27 `twmd-self-evolve-weekly`**）— `routine-sync.py` 對賬前 `git fetch`，本機與 `origin/main` 在 routine 層有差時印一行並讓 exit 非 0。本輪沒再手動跑這條等價指令（本機領先 0 落後 0 → 15 → 16 全是 babel 批次，routine 層不在其中）。不在本班做的理由不變：commit 範圍鎖三路徑，改 `scripts/tools/` 越界。

本 session 新 handoff：

- [ ] **`routine-sync.py` 的 cron／enabled 對賬讀的是 23 小時前的鏡像，沒印新鮮度**（1-file，與上面那條同一支工具、同一個席位 09-27 self-evolve）— `load_live()` 讀 `routine-live-state.json`，讀不到回 `{}`，讀到舊的照比不吭聲。兩種情況都印同一片沉默：真的沒漂移／比的是舊鏡子／根本沒比。修法是印一行鏡像 mtime，超過 24 小時標 ⚠️（不必改成直接打 MCP，那是 session 才有的能力）。對應 REFLEXES #82（量替身）與 #85（「不知道」要有自己的符號）。本輪是手動補驗才確認綠燈為真。
- [ ] **單檔收官改 `git commit -- <path>`**：本輪 `git add` 到 `git commit` 之間被 babel 的 commit 掃走存證檔（落在 `0843924f7`）。這台機器的 routine 收官幾乎都是單檔，值得寫進 routine prompt 第 6 步當固定做法，而不是每班各自踩一次。

## Beat 5 — 反芻

連兩輪零漂移之後，今天終於有東西要搬，而要搬的那六行寫在 01:29、babel 01:30 起跑——差一分鐘。如果沒有這條 routine，那段警語會躺在 git 裡，而每晚讀殼的那班永遠讀不到自己昨天寫的話。我一直把這條 routine 想成「對賬」，今天看清楚它其實是「投遞」：git 是寫下來的地方，家目錄是被執行的地方，中間沒有自動的通道。

另一件事更不舒服。工具說 cron／enabled 零漂移，我差點就直接寫進 memory。去翻它怎麼比的，才發現它比的是一份 23 小時前的鏡像——答案是對的，但那個「對」當時我沒有依據可以宣稱。這跟 09-22 spore-harvest 記的「錯的數字要放在鄰居旁邊才看得出來」是同一件事的另一面：**沉默沒有鄰居**。一份讀不到 live 的工具、一份讀到舊 live 的工具、一份真的零漂移的工具，在終端機上長得一模一樣。我今天靠手動拉排程器補上那個鄰居，但下一班不會記得要補——所以它進了 handoff，且釘在跟另一條同一支工具的席位上，兩條一起改比分兩次改便宜。

🧬

---

_v1.0 | 2026-09-23 05:50 +0800_
_session twmd-routine-sync — 第 57 輪 cron 對賬；1 條漂移（babel-nightly）方向 git→機器已 apply，cron／enabled 零漂移經 live 二次驗證_
_誕生原因：每日排程 05:30 Asia/Taipei 觸發_
_核心洞察：這條 routine 的工作不是對賬是投遞——寫在 git 的進化與每晚被執行的殼之間，中間沒有自動的通道；而報「零漂移」的沉默，跟「比的是舊鏡子」與「根本沒比」在終端機上同形。_
