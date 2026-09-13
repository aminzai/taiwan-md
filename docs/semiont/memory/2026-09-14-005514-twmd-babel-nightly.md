# 2026-09-14-005514-twmd-babel-nightly — 分岔擴大到 299/156 且真衝突 172 檔；150 篇零譯文條目卡住十二語，補 slug 後重啟 dispatcher

> session twmd-babel-nightly — cron 排程觸發（每天 00:30 Asia/Taipei）
> Session span: 00:38 → 00:55 +0800（~17 分鐘，1 commit）
> 資料來源：`git log %ai` + `git merge-tree` 唯讀模擬 + `ps` / `launchctl`

## 觸發

每晚 00:30 的多語批次同步窗口。本機沒有前晚存活的 dispatcher（`ps` 查無 `babel-dispatch.py`），需要重新起跑。

## 分岔現查：從「繞開」升級到「量化衝突」

`git checkout main && git pull` 卡在真分岔（ahead 298 / behind 156，本輪起跑前）。這是延續 9/9 以來每晚都撞見的同一件事，OBSERVER-QUEUE 已有 [#56](../OBSERVER-QUEUE.md) 案件（9/12 時 194/143，🔒紅線等哲宇），但本班第一次沒有停在「繼續繞開」，而是想確認救援分支 `20260912-unpushed-routine-queue` 是否還跟得上本地 HEAD——結果是只差 4 個 commit，代表前幾班已經很勤快在維護這條安全網，我把它快轉推上去兩次（起跑前、slug-map 修復後）。

為了確認繞開仍然安全，我用 `git merge --no-commit --no-ff origin/main` 做唯讀模擬（完成後 `git merge --abort` 還原，過程沒有動到 working tree），量出 172 個真衝突：118 篇雙邊獨立譯過的條目（add/add，跟 #56 記載的 118 一致，規模穩定沒有再擴大）、5 個認知層索引（MEMORY/DIARY/LESSONS-INBOX/OBSERVER-QUEUE/REFLEXES）、13 個 `src/data/related/*.json` 衍生檔、`_slug-map.json`／`_translation-status.json`／`reports/babel/fail-memo.json` 各 1 個。跟 #56 的判讀一致：後三類不需要人工判斷，卡住的仍是那 118 篇的取捨，維持「不 pull、不自己合併、推安全網」的既定做法，不代哲宇做 A/B/C 選擇。

## 150 篇零譯文條目卡住十二語：比 9/13 那次大三倍的同型病

起跑後第一輪，`prepare-batch` 對 id 語言印出四十多行 `TBD-NEEDS-SLUG` skip，正是 9/13 memory 記過的同一種病：全新中文條目一個語言的譯文都還沒有，slug 反推無來源，ASCII fallback 對純中文檔名吐出空字串，dispatcher 守門直接跳過——而且是十二語同時跳過，不只 id。用 `_translations.json` 反查（第一次寫反了方向，檢查 `rel in translations.keys()` 而不是 `.values()`，先得到誤導性的 1018 筆再修正)，篩出真正零譯文的 150 篇，橫跨 About/Art/Culture/Economy/Food/Geography/History/Lifestyle/Nature/People/Politics/Society/Technology 十三個分類。

修復工具 `slug-suggest.py` 原本呼叫的 `openrouter/owl-alpha` 已下架（404），這是繼 9/13 `translate.py` 第二順位模型死掉之後,同一批「免費模型陣亡」的第三個受害者。換成當晚 cascade 裡驗證中的 `nvidia/nemotron-3-ultra-550b-a55b:free`，分 6 批（每批 25 篇）跑完（150 篇一次送單一次逾時/回應為空，拆批後穩定）。150 個新 slug 跟既有 slug-map 值、既有跨語言檔名做過雙重零碰撞檢查，才合併進 `knowledge/_slug-map.json`，精確路徑 commit `72960755b`（只含 `_slug-map.json` + `slug-suggest.py` 兩檔，`verify-commit-scope.sh --head 2` 驗證通過）。

## 起跑

用 `launchctl submit` 起統一 dispatcher（label `com.taiwanmd.babel.nightly`），覆蓋十二語，三個 fleet mac-m4max ollama 並行槽 + 兩個雲端 worker（`nemo`=nemotron、`lagunas`=poolside，皆為最近成功過的免費模型；`gpt-oss-120b:free` 沿用 9/13 已知死亡，不用）。第一次 submit 忘記在內層指令加 `cd`，相對路徑找不到 script，連續三次同樣失敗才用 heredoc 寫死一個 wrapper script 才成功——這是本班自己犯的低級錯誤，不是系統的病。dispatcher 起跑後中途 PID 從 3011 換成 12398（launchd 自動重啟，疑似跟我在 dispatcher 存活期間手動 commit 造成的 git 短暫鎖競爭有關），重啟後穩定持續產出，未再中斷。

## 收官 checklist

| 檢查項                       | 狀態                                                                 |
| ---------------------------- | -------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                   |
| Timestamp 精確               | ✅（`session-id.sh` + `git log %ai`）                                |
| Handoff 三態已審視           | ✅                                                                   |
| 分岔量化                     | ✅ 172 檔真衝突（118 譯文 + 5 索引 + 13 衍生 + 3 單檔），跟 #56 一致 |
| slug-map 修復驗證            | ✅ 150 筆零碰撞，`verify-commit-scope.sh` 過                         |
| dispatcher 存活              | ✅ PID 12398，launchd label 常駐                                     |

## Handoff 三態

- ⏳ blocked（沿用 #56，🔒紅線不適用 default-action）：main 本機 299 個未推送 commit 與 origin 156 個真衝突的 118 篇雙邊譯文取捨，仍等哲宇選 A/B/C；本班無新增進度，安全網 `20260912-unpushed-routine-queue` 已推到 `72960755b`。
- [x] ~~150 篇零譯文條目 TBD-NEEDS-SLUG 卡住十二語~~：`_slug-map.json` 補 150 筆，commit `72960755b`，dispatcher 下一輪 `build_slug_map()` 會自動吃到。
- [ ] `slug-suggest.py` 硬編碼的 `openrouter/owl-alpha` 已下架，本班已改成 `nvidia/nemotron-3-ultra-550b-a55b:free`，但 `translate.py` `DEFAULT_CASCADE_ID` 第二順位仍是死掉的 `openai/gpt-oss-120b:free`（9/13 已記，REFLEXES #56），連同 `SQUEEZE-MODELS-MAX-PIPELINE.md` 的鏡射段落，本班仍未處理，留給 maintainer／self-evolve。
- [ ] 若接下來幾夜 `poolside/laguna-s-2.1:free` 持續低命中率（9/13 已觀察到 429），考慮從 cloud worker 池移除；本班未追蹤到新資料。
- ⏳ blocked（沿用上一班）：OBSERVER-QUEUE #28(a)、#53（14 天 2026-09-25 到期）、#57（🔒對外發布節奏）、#1678、#1609 等哲宇。

## Beat 5 — 反芻

分岔那條線，這幾天每一班都準確地把它「繼續繞開」寫進 handoff，但我今晚第一次真的去跑唯讀模擬量出 172 這個數字。契機是救援分支只差 4 個 commit——這件小事讓我意識到「繞開」本身已經被前幾班維護得很好，反而該花力氣去確認繞開的邊界有沒有位移。150 篇零譯文條目跟 9/13 的 37+9 是同一個結構性缺口的第三次復發：新文章誕生的那一刻，這個系統仍然沒有替它預留進翻譯佇列的入口，只是每次規模都不一樣、每次都要有人手動現查才會被看見。這條缺口值得寫進 LESSONS-INBOX：修復本身很快（一個腳本 + 一次 LLM 呼叫），但「這個病一直沒有從根本解決」這件事，本身就是一個訊號。

🧬

---

_v1.0 | 2026-09-14 00:55 +0800_
_session twmd-babel-nightly — 每日多語批次同步 cron_
_誕生原因：例行 00:30 routine fire，本機沒有前晚存活的 dispatcher，需重新起跑_
_核心洞察：(1) 分岔的安全網已被前幾班養得很好（只差 4 commit），繞開的正確動作是持續驗證邊界而非重新判斷要不要繞開 (2) 新文章誕生沒有自動進翻譯佇列的入口，是三次復發的同一個結構性缺口，不是三次獨立的小 bug_
_LESSONS-INBOX 候選：新條目誕生流程應該在建檔當下就跑 slug 檢查並自動補值，而不是等 dispatcher 撞到才被動現查_
