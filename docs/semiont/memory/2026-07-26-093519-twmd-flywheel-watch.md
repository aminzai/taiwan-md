# 2026-07-26-093519-twmd-flywheel-watch — 飛輪綠燈，但看門的那把尺自己漏抓了一條真的跑完的 routine

> session twmd-flywheel-watch — cron routine（每天 09:30，跑在指揮部 commander-macbook）
> Session span: 09:33:00 → 10:0x:00 +0800（約 30 分鐘，2 commits）
> 資料來源：`git log %ai` / `origin/main` / `flywheel-watch.py`

✅ BECOME ack: mode=micro / Q14=PASS

## 觸發

飛輪 7/24 整批遷到 mouhouse 之後，指揮部這台唯一的工作是從外面看它還活著沒有。今天是這條 routine 第一個排程 cycle。

## 飛輪狀態：綠燈

過去 24 小時 `origin/main` 累積 258 筆 commit，其中 11 筆帶 `[routine]` 標記。週日該跑的整條鏈都留下痕跡——news-lens-weekly 01:12、weekly-report-sun 02:18、distill-weekly 03:15、self-evolve-weekly 04:18，接著 embeddings-nightly 05:27、routine-sync 05:38、data-refresh-am 06:14、feedback-triage 07:10、maintainer-daily 08:40。中間夾著整夜不停的巴別塔批次（ar/ru/hi/pt/id/vi 各語 fleet 派發）。**飛輪在轉，而且轉得比平常密。**

## 儀器報了三條靜默，兩條是假的

`flywheel-watch.py` 給的 WARN 是 distill-weekly、flywheel-watch、spore-harvest-am 三條。逐條對 ground truth 查完，只有一條是真的：

**distill-weekly 是假警報。** 它 03:15 確實跑完（MEMORY 索引列 `031527-twmd-distill-weekly`，W30 §未消化 27→2），但產出 commit `e1bebcc85` 寫成 `[semiont] distill:`，窗口內沒有任何一筆 subject 帶得出 `twmd-distill-weekly` 這個字串，於是儀器看不見它。這跟前一晚 weekly-report 誤報 maintainer-daily「靜默死亡」是同一種病——索引列已經把它寫成「名字的替身」，八小時後同一種病換一個宿主再犯一次。

**flywheel-watch 是自己。** 這條今天首次排程觸發，跑的當下還沒留下自己的 commit，所以必然報自己靜默。今天這筆收官 commit 帶 `[routine] twmd-flywheel-watch` 標記之後，明天的 cycle 就看得見昨天的自己。

**spore-harvest-am 是真的沒動。** 06:30 的槽位今天沒留下任何痕跡。它的病史不算乾淨：7/13-7/15 天天跑、7/16 跳一天、7/17 只留「Chrome MCP 沒 pair，0 抓」、7/20-7/24 連續 5 天空白、7/25 06:44 回來一次清掉 4 篇 OVERDUE。`routine-live-state.json` 顯示它 enabled、`lastRun` 停在 7/25 06:34（dump 齡 7.5 小時，早於今天的 06:30 槽位，所以對今天無話可說）。今天算靜默第 1 天，依飛輪判準要看趨勢不看單點，先進觀察不進警報。可疑的方向有兩個：這條依賴 Chrome MCP 配對，而遷居後的營運機是一台 headless mac mini；同組的 spore-pick-daily 與 spore-publish-daily 已經是刻意 disabled 狀態，整條孢子產線目前只剩 harvest 一環還開著。

## 給看門的那把尺加第二把

假警報放著不管會變成信號通膨——每天報一條假的，真的那條就沒人信了。所以當場修了儀器本身：

`flywheel-watch.py` 原本只認 `[routine] <slug>` 這一把尺。現在多一把獨立的：MEMORY.md 索引列的 session-id handle（`| 日期 | HHMMSS-handle |` 帶得出精確到秒的時間戳，可以直接跟窗口比對），兩把都不中才算靜默。修完重跑，distill-weekly 從靜默名單消失，spore-harvest-am 留著，符合手查的結論。

驗證過程自己撞到第二個洞。第一次在 worktree 裡重跑，flywheel-watch 那條憑空消失了——因為 `.taiwanmd/node-name.local` 是 gitignored，worktree 裡沒有，`belongs_to_this_node()` 就把所有帶 `🖥️` 標記的列整批跳過，而本檔自己正是其中一列。檢查範圍靜靜縮小，輸出看起來還是一份正常報告。補了一道 fail-loud 印到 stderr，順手把兩件事寫回 ROUTINE.md 註 ²⁰。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅ 取自 `git log %ai`                         |
| Handoff 三態已審視           | ✅                                            |
| 未碰營運機排程               | ✅ 只讀 `origin/main`，未 pull、未改 mouhouse |
| 未夾帶平行產線檔案           | ✅ 獨立 worktree，只 stage 本 routine 產出    |

## Handoff 三態

繼承 2026-07-26-071056-twmd-feedback-triage：

- [x] ~~「雙機器 cron 調度待釐清」~~ retired by 上一棒（routine-sync 三層對賬零漂移已結案）

本 session 新 handoff：

- [ ] **spore-harvest-am 靜默第 1 天**（2026-07-26 06:30 槽位）。明天 09:30 先看它 7/27 的槽位有沒有痕跡；連 3 天靜默且非空場 → 進 OBSERVER-QUEUE，附兩個預設選項：(A) 確認 headless 營運機是否還能配對 Chrome MCP，不能就把這條改成 pick/publish 那樣明確 ⏸️，(B) 拆出不依賴瀏覽器的 metrics-only 半條先撐著
- [x] ~~儀器只認一把尺~~ 本 cycle 修掉（第二把尺 + fail-loud + ROUTINE 註 ²⁰）

## Beat 5 — 反芻

這條 routine 存在的理由是「儀器只看見存在，看不見缺席」，今天它證明了自己的價值——也在同一次呼吸裡示範了看門人自己會怎麼看錯。它抓到的三條裡兩條是假的，命中率三分之一；如果沒有逐條對 ground truth 查，我今天交出去的會是一份「三條 routine 疑似死亡」的驚嚇報告，而真相是飛輪跑了一個相當漂亮的週日。

假陽性的代價在這種每天跑的哨兵身上特別高：它不會吵到讓人立刻修，只會慢慢把「WARN」這個字磨到沒有重量。所以修尺比寫報告重要。教訓本身不新（外部尺、名字的替身、代理訊號），新的是它在八小時內換了三個宿主——weekly-report 誤報 maintainer、flywheel-watch 誤報 distill、我自己在 worktree 裡誤讀 flywheel-watch。同一個形狀，三個不同的檢查器，各自寫在各自的檔案裡。

🧬

---

_v1.0 | 2026-07-26 10:0x +0800_
_session twmd-flywheel-watch — 首個排程 cycle：飛輪綠燈 + 儀器兩處校準_
_誕生原因：飛輪遷居 mouhouse 後，指揮部保留這條從外部看它是否還活著的哨兵，今天第一次照表觸發_
_核心洞察：儀器報的三條靜默有兩條是假的，命中率三分之一——每天跑的哨兵，假陽性會把警報的重量磨掉；同一種「名字的替身」在八小時內換了三個宿主_
