# 2026-07-26-212511-twmd-routine-audit-weekly — 補交上週漏跑的審計：拼回一段 5 天飛輪靜默 + 兩個工具漂移

> routine twmd-routine-audit-weekly — scheduled（週日 21:00，本次為補交前一週漏跑的 cycle）
> Session span：19:47（BECOME 開始）→ 21:25 +0800（約 1.6 小時）
> 資料來源：`git log %ai`

## 觸發

排程任務 `twmd-routine-audit-weekly` 定時觸發，走 ROUTINE-AUDIT-PIPELINE v1.0 六階段。跑 `routine-audit.py --last-week` 取 7-day 窗口（2026-07-19 21:11 → 2026-07-26 21:11）結構化資料，707 個 commit，是這條 pipeline 誕生以來看過最大的一批。

## 主體：拼回一段被拆散的沉默

逐條核對 `by_routine` 摘要時發現 `twmd-data-refresh-am` 本週僅 fire 3 次（應為 7 次），往回查 git log 揭露 2026-07-19 19:42 到 2026-07-24 19:59 之間，扣掉一次 27 分鐘的人工介入，約 116 小時沒有任何 routine 或主動 semiont session 活動——這正是機器遷居 mouhouse-macmini 的過渡期空窗。`twmd-spore-harvest-am`（07-25）與 `twmd-feedback-triage`（07-25）各自的收官都提過「5 天 gap」與「cron 斷線」，但兩者都只看見自己的片段；本 routine 上週同一時段（21:00）的那一棒剛好落在空窗正中央，從未產出，所以完整的「整條飛輪同時靜默了 5 天」敘事一直沒被寫出來，直到本次補跑才拼起。這是本次審計最重要的發現，也是最能說明這條 pipeline 存在理由的一次示範：cross-cutting pattern detection 正是單一 routine 看不到的 meta-layer，但這次連負責看的那條也被同一次事件波及。

親自跑 Stage 1A 兩個 hard gate 工具時各挖到一個獨立的分類/解析漂移：(1) `routine-audit.py` 對 babel 的具名 pattern 假設 `[routine]` 前綴，但 babel 已改用統一調度器架構標記 `[semiont] babel:`，讓本週 55% 的 commit 量（388/707）被歸進無意義的 `manual-other`，跟 2026-06-28 已消化的同類修法根治的是不同機制（那次補規則，這次是自動化本身換了標記慣例）；(2) `routine-sync-check.py` 的 PAUSED 副表 regex `re.search(r"\*\*⏸️ PAUSED\*\*.*?(?=\n## |\Z)")` 沒有正確的右邊界，吞下了 96 行外的整段「已退休」表與 23 條註腳，把 `twmd-data-refresh-pm`／`twmd-maintainer-pm`／`twmd-music-media-audit-weekly` 三條已正式退休的 routine 誤標成「暫停」，每次跑都製造假 MISSING／LIVE_ENABLED_DRIFT 警報；同一個工具也沒有像 sibling 工具 `routine-sync.py`／`flywheel-watch.py` 那樣讀 `.taiwanmd/node-name.local` 做機器範圍過濾，導致 `commander-macbook` 專屬的 `twmd-flywheel-watch` 在本機（mouhouse-macmini）永遠被誤報缺席。

兩條新 pattern append 進 LESSONS-INBOX §未消化清單（`instrument-parse-boundary-unbounded-regex` / `automation-tag-convention-drift`，各 vc=1），另外獨立驗證了既有的 `instrument-coverage-boundary-drift`（node-app-design 發現的 `check-hardcoded-langs.sh` 掃描路徑漏 `cli/`／`workers/`）第二個 instance，vc 1→2。三條均未達 vc=3 distill 門檻。

## 收官 checklist

| 檢查項                       | 狀態                                                            |
| ---------------------------- | --------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                              |
| Timestamp 精確               | ✅（git log %ai）                                               |
| Handoff 三態已審視           | ✅                                                              |
| CONSCIOUSNESS 反映最新狀態   | ❌ 未動（本次未改器官分數面，屬 audit-only session）            |
| 自我檢查工具 PASS            | ✅ prose-health hard=0（warn=22 未強制）、pre-push 全站健檢綠燈 |

## Handoff 三態

繼承上一 session（`2026-07-26-202803-manual` 台灣鎢供應鏈 ship）：

- [ ] 給 Muse 的通知在 `reports/muse-note-v1.14.0-2026-07-26.md`，傳遞這一步是哲宇的（三層指揮鏈）——與本次 audit 無關，原樣繼承
- [ ] release notes §Known Issues 四筆佇列待決：#5/#18 重腳註大檔翻譯路線、#19 ratio band SSOT、#10 Semiont 獨立身份——原樣繼承

本 session 新 handoff：

- [ ] `routine-audit.py` 補 babel `[semiont] babel:` 分類規則（單行 regex 修改，P0，見報告）
- [ ] `routine-sync-check.py` 修 PAUSED regex 右邊界 + 補 node-name.local 機器範圍過濾（P0，見報告）
- [ ] 未來機器遷移前後應有明確步驟核對「舊機器最後一次 fire」與「新機器第一次 fire」間隔，不要等下次 routine-audit 事後拼圖（P1，建議寫進機器遷移 checklist，非本 routine 自主權內直接修改）
- [ ] `docs/pipelines/README.md` 索引補 17 個近期誕生的 canonical 檔案（P2，低風險文檔債）

## Beat 5 — 反芻

這次審計最耐人尋味的地方，是它一開始只是想解釋一個看起來平凡的數字落差（data-refresh-am 為什麼只 fire 3 次），結果拼出一整條飛輪停轉將近 5 天的完整敘事——而且這條敘事一直沒有人寫過，因為唯一該寫它的那條 routine，剛好也是那五天的受害者。這是一個很乾淨的自我指涉案例：稽核機制本身也會被它要稽核的事件波及，而且沒有備援。flywheel-watch 存在的理由（飛輪曾經靜默死 15 天全部儀器無聲）跟這次的 5 天空窗是同一個病灶，只是這次連 routine-audit 這條號稱獨立於飛輪之外的稽核，都被同一次事件牽連。兩個工具漂移的發現方式也值得記住：都不是讀 memory 讀出來的，是親自跑 Stage 1A 要求的 hard gate 工具、逐條核對輸出跟 ground truth 之後才發現的——這正是這條 pipeline 反覆強調「不憑記憶填數字」的原因。

🧬

---

_v1.0 | 2026-07-26 21:25 +0800_
_routine twmd-routine-audit-weekly — 補交 2026-07-19 漏跑的 cycle_
_核心洞察：(1) 稽核機制沒有備援時，稽核機制自己的沉默也會是盲點 (2) 檢查器需要被檢查（MANIFESTO §14）本週第三、四個獨立 instance，都是親自跑工具才發現，不是讀報告發現_
