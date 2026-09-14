# 2026-09-15-003928-twmd-babel-nightly — 三重巡檢確認 dispatcher 健康在跑，沒有重複起跑；量出 ja 幾乎全滅的具體數字；安全網分支快轉

> session twmd-babel-nightly — cron 排程觸發（每天 00:30 Asia/Taipei）
> Session span: 00:38 → 00:42 +0800（~4 分鐘，0 knowledge commit，1 分支快轉）
> 資料來源：`ps` / `lsof` / report.jsonl / master.log / `git rev-list` / fleetctl

## 觸發與第一動作：BECOME write mode 完整跑過

`/twmd-become write` 完整讀 wake-context.latest.md 全 11 段（253KB）到 `wake:END` sentinel，selftest 9 項全綠。§Step 9 mode subset（Q1-4/Q8-11/Q14）全過才開口。

**缺席層**：groundtruth 讀到 observer mode=ABSENT（8 天，最後在場訊號 2026-09-07 audit-upgrade handle），缺席協議生效——到期預設必執行、🔒閾值類可代理、四紅線不動。本班沒有觸及任何四紅線或到期佇列項，缺席協議本身不改變今晚的判斷（不重啟 ja / 快轉安全網分支都不落在協議適用範圍內，是例行維護與代價判斷，不是需要代理的「到期預設」）。

**Stage 0 算力判定**：`babel-preflight.py` 回報 healthy（4/4 層可用：OpenRouter 7/7 key 通過、本機 ollama 1 模型可用、fleet 1 節點可達、codex 可用），唯一弱點是實績檢查標記的 ja 全組合 <15% 命中（詳見下節）。

## 三重巡檢：這次不是重啟，是確認別重啟

Stage 0 preflight 前先查是否有前晚存活的 dispatcher——`ps aux` 找到 PID 12398，`launchctl` label `com.taiwanmd.babel.nightly`，已經跑了 **23h45m**（昨晚 00:53 起跑，覆蓋十二語）。三重巡檢：

1. **存活**：`ps` 確認 PID 12398 在跑，`lsof` 確認開著 report.jsonl / master.log / freezes.jsonl 三個活躍檔案
2. **生產**：report.jsonl 969 行，最新一筆 00:36:03（查驗當下 00:38:44，落差 <3 分鐘）；最近 20 分鐘內完成 12 篇（跨 hi/ar/ja/en/id/es/fr/de/ko 多語言），非空轉
3. **第二訊號源**：`fleetctl workers --service llm` 回報 macm4max1/2/3 三台 mac-m4max ollama 節點，跟 dispatcher `--worker` 參數一致，無漂移

三項全過 → **判定：不重啟、不起第二個 dispatcher**。同時執行兩個 dispatcher 會在同一個 working tree 上搶 git commit 序、搶同一批 fleet worker 額度，是明確的反模式（[REFLEXES #40](../REFLEXES.md) shared file per-key serial dispatch）。

## 量出 ja 幾乎全滅：1/81 成功，非猜測

`babel-preflight.py` 弱適配清單早就標記 ja 所有 worker×model 組合 <15% 命中（lagunas 0%／macm4max1-3 0%／nemo 11%），本班用 report.jsonl 對這條產線的實際輸出做逐筆統計：**今晚 81 次 ja 嘗試，1 成功、80 失敗（1.2%）**。`lagunas` 被 dispatcher 自身的健康帳凍結機制觸發 **8 次**「🥶 FREEZE worker=lagunas for 30min」，累積凍結時數約 4 小時。失敗訊息主要兩類：`[NO_NATIVE_SCRIPT] 0 個 ja 原生文字字元` 與 `no output written by translate.py (exit=1)`——不是網路或額度問題，是這批 worker 池裡沒有一個真的會產出合法日文。

**沒有動手重啟去修這件事**：per [BABEL-VORTEX-LOOP §重啟有成本](../../pipelines/BABEL-VORTEX-LOOP.md#重啟有成本修完不要立刻重啟)，單一發現不值得一次重啟（會砍掉當下 3-4 篇進行中的翻譯，且 dispatcher 自身的 freeze 機制已經在自動限制 lagunas 消耗，屬於部分自癒）。已用 `spawn_task` 開一張獨立卡片，留給下一個有空間的 session 判斷要不要把 ja 從這批 worker 池整個拔掉、換一個真正支援日文的 backend（cascade 文檔提過的 Hy3 或本地 qwen3.6，這批 12 語 dispatcher 目前都沒接）。

## 安全網分支快轉（非解決分岔本身）

上一班（`2026-09-14-085914-twmd-maintainer-am`）留的 handoff：救援分支 `20260912-unpushed-routine-queue` 落後本機 HEAD 已到 115 commits，請下一班快轉推一次。驗證 `git merge-base --is-ancestor` 確認是純 fast-forward（origin 端無獨立 commit）後 `git push origin HEAD:20260912-unpushed-routine-queue`，`6d42c122e..ee635df0b`。**這不是解決分岔決策**——OBSERVER-QUEUE #56 的 A/B/C 選擇仍完全保留給哲宇，本次只是維護安全網本身的新鮮度，跟前幾班同一動作同一分寸。

分岔現讀：`git rev-list --left-right --count origin/main...HEAD` = **181 behind / 418 ahead**（上一班收工時 343 ahead，一夜之間 dispatcher 自己又推進 75 個 commit；behind 181 不變，代表 origin 端這段時間沒有新的獨立 commit 進來）。

## 各語進度 delta（status.py @ ee635df0b，本班查驗當下）

| lang | fresh | stale | missing | coverage |
| ---- | ----: | ----: | ------: | -------: |
| en   |   906 |    79 |     120 |    87.9% |
| ja   |   764 |    94 |     232 |    76.5% |
| ko   |   916 |    75 |     113 |    88.4% |
| es   |   894 |    79 |     130 |    86.8% |
| fr   |   899 |    81 |     122 |    87.4% |
| vi   |   814 |    81 |     150 |    79.8% |
| id   |   703 |    48 |     361 |    67.0% |
| pt   |   886 |    65 |     156 |    84.8% |
| hi   |   740 |    38 |     334 |    69.4% |
| ar   |   804 |    43 |     260 |    75.6% |
| ru   |   849 |    41 |     221 |    79.4% |
| de   |   617 |     6 |     497 |    55.6% |

本班沒有跑批次翻譯（未重複起跑 dispatcher），這張表是「dispatcher 已存活 23h45m 後」的現況快照，不是本班貢獻的 delta——真正的 delta 在 dispatcher 自己持續產生的每輪 commit 裡（過去 24hr 十餘條 `🧬 [semiont] babel: {lang} 批次 N 篇` commit）。de 覆蓋率仍最低（55.6%，497 篇 missing），是明語系裡進度最慢的一支。

## 收官 checklist

| 檢查項                       | 狀態                                                              |
| ---------------------------- | ----------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                |
| Timestamp 精確               | ✅（`session-id.sh` + `git log %cI`）                             |
| Handoff 三態已審視           | ✅（安全網分支快轉完成；其餘 blocked 項延續，無新資訊改變其狀態） |
| 三重巡檢                     | ✅ 存活 + 生產（20 分鐘內 12 篇）+ 第二訊號源（fleetctl）三項全過 |
| ja 量化                      | ✅ 81 次嘗試 1.2% 成功，8 次 freeze，spawn_task 已開卡片          |
| 不重複起跑                   | ✅ 確認判斷依據記錄在案，不是省略 Stage 0 的藉口                  |

## Handoff 三態

- ⏳ blocked（沿用 #56，🔒紅線不適用 default-action）：main 本機 418 個未推送 commit 與 origin 181 個真分岔，118 篇雙邊獨立譯文的取捨仍等哲宇選 A/B/C。安全網 `20260912-unpushed-routine-queue` 已推到 `ee635df0b`（本機 HEAD）。
- [x] ~~救援分支落後 115 commit~~：已快轉推上去，`6d42c122e..ee635df0b`。
- [ ] pending（新增）：本輪 12 語 worker 池對 ja 幾乎全滅（81 次 1.2% 成功，8 次 lagunas freeze），已 spawn_task 開卡片，等哲宇或下一個有空間的 session 決定要不要換 ja 專屬 backend（cascade 文檔的 Hy3／本地 qwen3.6 未接進這批 dispatcher）。
- ⏳ blocked（延續）：issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程；`twmd-spore-pick-daily` / `twmd-spore-publish-daily` 停用三個月未拍板。

## Beat 5 — 反芻

今晚第一次真正需要判斷的不是「要不要修」，是「要不要重啟去修」——preflight 早就把 ja 的弱適配列出來了，report.jsonl 只是把它變成一個可以引用的數字（1.2%）。但知道問題存在跟決定動手是兩件事，尤其動手的唯一路徑（重啟）本身就有明確記載過的代價。這班選擇不重啟，賭的是「11/12 語言健康運作 + 自帶 freeze 自癒」比「立刻修好 ja 但砍掉當下進行中的工作」更划算——這個判斷本身該被記下來，因為它跟義務鐵律「推向 100%」表面上有張力：不重啟不是守預算式的 defer，是讀過重啟成本記錄後的具體換算。如果下次還遇到同樣的猶豫，這篇該是可以直接拿來對照的先例。

🧬

---

_v1.0 | 2026-09-15 00:42 +0800_
_session twmd-babel-nightly — 每日多語批次同步 cron_
_誕生原因：例行 00:30 routine fire，發現 dispatcher 已存活 23h45m，本班角色從「起跑」變成「巡檢＋不干擾＋量化紀錄」_
_核心洞察：(1) 三重巡檢的價值不只是確認活著，是給「不重複起跑」這個決定一個可驗證的依據 (2) 「重啟有成本」不是抽象原則，這次真的攔下了一次單點修復的衝動 (3) 安全網分支維護是可以每班都做、風險趨近於零的例行動作，跟真正的分岔決策要分開對待_
_LESSONS-INBOX 候選：babel worker 池的語言×backend 適配應該在 dispatcher 啟動前就用 preflight 結果自動排除 <15% 組合，而不是讓它跑到自己觸發 8 次 freeze 才被動發現_
