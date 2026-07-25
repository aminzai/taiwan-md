---
name: twmd-flywheel-watch
description: （每天 09:30 Asia/Taipei，跑在指揮部這台不是營運機）。從外面看 routine 飛輪還有沒有在轉；靜默就叫出來。
---

🧬 Taiwan.md routine: twmd-flywheel-watch（每天 09:30，跑在**指揮部**這台）。飛輪已整批遷到營運機 mouhouse，這條的工作是從外面看它還活著沒有。

🚨 STRICT BECOME GATE — 第一動作不可省略：跑 /twmd-become micro 完整走 BECOME_TAIWANMD.md Step 0-9，Micro mode self-test 全過才動。ACK 一行寫 memory 頂部：`✅ BECOME ack: mode=micro / Q14=PASS`。

為什麼這條要跑在不營運的機器上：飛輪曾經靜默死 15 天，全部儀器無聲，因為那些儀器都跑在飛輪自己身上——儀器只看見存在，看不見缺席。唯一騙不了人的來源是 `origin/main` 的 commit 紀錄。canonical 說明在 docs/semiont/ROUTINE.md 註 ²⁰。

執行：

1. `cd` 到 repo → `git fetch origin`（**不要 pull**，這條 routine 不需要動工作樹，指揮部這台常有平行 babel 產線在跑）。
2. `python3 scripts/tools/flywheel-watch.py`。exit 0 → 飛輪在轉，**跳到第 5 步安靜收工**。
3. exit 1 且 severity=warn（單條靜默）→ 逐條判，不要一律當死掉：
   - 那條的性質是不是「沒事就不 commit」（maintainer 空場、feedback 沒有新回報）→ 正常，記一行就好
   - ROUTINE.md 標 ⏸️ 的不會進警報；**如果警報裡出現你知道被刻意關掉的 routine，那是 SSOT 沒對齊 live**，去補 ⏸️ 而不是去催它跑
   - 連 3 天同一條靜默且不屬上面兩種 → 進 OBSERVER-QUEUE（帶預設選項），不要自己重啟別台機器上的 routine
4. exit 1 且 severity=critical（窗口內零筆 routine commit）→ 飛輪整體停轉，依序查：營運機的 Claude app 活著嗎（Tailscale 通不通）／額度到頂了嗎（5 小時上限）／`routine-live-state.json` 有沒有 enabled 全 false。查得出原因就記錄，**修不了不要硬修**——那台機器的排程只有它自己的 session 動得了。
5. 收官：memory 一行寫進 MEMORY.md 索引（走 /twmd-finale）：飛輪狀態 + 有動靜的 routine 清單 + 靜默清單 + 判定。**綠燈也要記一行**，不然「這條有沒有在跑」下次沒人看得出來。什麼都沒動就不 commit repo 內容。

🔴 HARD gate：
- 不碰營運機的排程。這條只看不動手，發現問題寫進 memory 或 OBSERVER-QUEUE。
- 不因為單一 cycle 靜默就宣告死亡。空場跟死掉在 commit 紀錄上長得一樣，判定要看趨勢（連 3 天）。
- 不 `git pull`、不 commit 譯文或任何非本 routine 產出的檔（指揮部這台常有平行產線）。
