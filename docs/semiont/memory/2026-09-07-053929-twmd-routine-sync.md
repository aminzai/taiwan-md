# 2026-09-07-053929-twmd-routine-sync — 第 41 輪對賬：18/18 prompt 一致，babel-nightly 的 proxy signal 這次讀對了

> session twmd-routine-sync — cron 排程觸發（每天 05:30 Asia/Taipei）
> 資料來源：`git log %ai` + `mcp__scheduled-tasks__list_scheduled_tasks`

## 觸發

每天 05:30 的例行三層對賬：讓這台機器的 routine prompt／排程設定跟 git 的 SSOT 對齊，卡在 embeddings-nightly 之後、晨鏈之前。

## 三層對賬

`git checkout main && git pull` 前工作樹有 8 個語言的 `src/data/related/*.json` 修改，來源不明未查——pull 之後沒消失，但幾分鐘後重跑 `git status` 已乾淨：這是同時段 fire 的 `twmd-embeddings-nightly`（05:37）自己完成並 commit 了（`58d147f08`），不是本 routine 的漂移，順路等它收尾即可，沒有搶著碰它的檔案。

`routine-sync.py` 印 18/18 prompt in-sync（比上輪多 5 份轉正——上輪 `--apply` 補的薄殼化這次穩定住了，沒有再退回舊版）。唯一印出的一項是 `twmd-babel-nightly` 🔌 `enabled SSOT=True live=False`，跟上輪（2026-09-06 12:59）記錄過的同一顆假警報同源：工具讀的 `docs/semiont/routine-live-state.json` 是 `twmd-data-refresh-am` 每天早上拋的快照，rider 把 babel-nightly 開回 enabled 是 09-06 中午的事，快照要等下一次 data-refresh-am 才會刷新，中間這段時間永遠會誤報。這次沒有重新驗證就相信上輪的判斷，直接用 `mcp__scheduled-tasks__list_scheduled_tasks` 現查：`enabled: true`、`lastRunAt: 2026-09-06T16:33:51Z`（=今天台北時間 00:33，正常 fire）。SSOT 與 live 實際一致，不需要動排程，也不是本 routine 職責去改那份快照檔。

## 順便驗證上輪留的 handoff

上一輪（09-06 12:59）在 handoff 裡寫「babel-nightly 應該會每天開始跑，下週體檢要確認它真的有 fire 且產出，不能只看 enabled=true 這個 proxy signal」。今天早上有現成的證據可以直接核對：git log 顯示 00:33 fire → 02:04-02:15 一串 commit（`80950cdcb` 補 slug、`a2ee8b44a` 7 語 + 3 patch 落地、`ef16d9a78` memory）。**不只 enabled=true，是真的有 fire 且真的有產出**——這條 handoff 提前在本輪就有答案，不用等到週報。（今早那輪 babel-nightly 自己的 memory 也記了「preflight 判健康、實測活著的只剩兩層」，速度變慢但確實在動，是另一條 routine 的事，這裡只確認「有沒有跑」這個問題本身已經有答案。）

Commit 身份延續上輪切換的 `Taiwan.md Semiont`，這次是它的第二個活驗證，author 欄位正常。

## 收官 checklist

| 檢查項                       | 狀態                                                                      |
| ---------------------------- | ------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                        |
| Timestamp 精確               | ✅（`git log %ai`）                                                       |
| Handoff 三態已審視           | ✅，上輪 babel-nightly fire-且-產出 的待驗證項本輪確認為真                |
| 三層對賬複驗                 | ✅ 18/18 prompt in-sync；唯一的 enabled 差異經 MCP 直查證實非真實漂移     |
| git add 範圍                 | 僅本檔 + MEMORY.md 索引行，未碰 `src/data/related/*`（embeddings 自己收） |

## Handoff 三態

繼承 `2026-09-06-125926-twmd-routine-sync`：

- [x] ~~babel-nightly 是否真的每天在 fire 且有產出~~ — 本輪確認：是，00:33 準時 fire，02:04-02:15 有真實 commit 產出
- [ ] pending（原樣延續，不屬本 routine 範疇）— 台鐵鳴日號卡片圖 / EVOLVE 投稿角度 / 句構型別實作 / SC 高倍數成長基準值 / BIM 英文 metadata / `lastHumanReview` 週度重數 / 🟠 unregistered 橘燈觀察
- [ ] pending（哲宇端，原樣延續）— #48 身份 Phase 1（紅線）／兩把 API key 放進營運機憑證目錄／09-26 前重新登入營運機
- [ ] pending（給下一輪 twmd-routine-sync 或任何在這台跑 routine 的 session，原樣延續）— 這台的 routine commit author 應維持 `Taiwan.md Semiont`；本輪再次確認正常，若下次 author 欄位跑掉要當異常處理

本 session 新 handoff：

- [ ] pending（給 `routine-live-state.json` 的維護者 `twmd-data-refresh-am`，非急件）— 這是同一顆 enabled-proxy-signal 假警報連續第二次被人工重新驗證才排除；如果未來要減少這種「每次都要現查」的重複工作，可以考慮讓快照多存一個 `fetched_at`-vs-`rider_applied_at` 的比較欄位，但這是儀器化升級，不在本輪 Micro mode 範圍內，僅記錄構想

## Beat 5 — 反芻

這輪最值得留下的不是修了什麼（什麼都不用修），是「同一個假警報第二次出現時，沒有偷懶引用上輪的結論，而是重新查了一次 live 狀態」——上輪的 memory 已經把根因寫得很清楚，這輪原本可以直接照抄「這是已知的 proxy signal，忽略」，但那樣就沒有真的排除「這次會不會不一樣」的可能性（例如 rider 是不是又被誰改回去了）。順手核對了上輪留的 handoff，答案剛好就在今天的 git log 裡，不用等一週。

🧬

---

_v1.0 | 2026-09-07 05:39 +0800_
_session twmd-routine-sync — 每日三層對賬 cron_
_誕生原因：例行 05:30 routine-sync fire_
_核心洞察：proxy signal 的假警報不會因為「上次也遇過」就自動變得可信任，每次都要現查一次 ground truth；上一輪寫的驗證型 handoff 這輪剛好有現成證據可以直接兌現，不必等到指定的驗證窗口（週報）。_
