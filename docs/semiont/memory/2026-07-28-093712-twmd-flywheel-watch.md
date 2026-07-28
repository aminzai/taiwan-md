# 2026-07-28-093712-twmd-flywheel-watch

✅ BECOME ack: mode=micro / Q14=PASS

routine `twmd-flywheel-watch` @ 09:37，跑在指揮部（commander-macbook）。工作只有一件：從飛輪外面看它還活著沒有。

---

## 判定：飛輪在轉，一盞黃燈

`python3 scripts/tools/flywheel-watch.py` exit=1 / severity=warn。但 `silent` 是空的——**沒有任何一條 routine 靜默**，warn 完全來自另一個維度：感知層自己的快照過期。

24 小時窗口（origin/main）：commit 110 筆，其中 `[routine]` 標記 11 筆。營運機 mouhouse 上今天該跑的日更全部留下痕跡，逐條對過 commit 訊息不只信工具分類：

| 時間  | routine                | 產出                                            |
| ----- | ---------------------- | ----------------------------------------------- |
| 05:32 | twmd-embeddings-nightly | bge-m3 12 語 7642 向量                          |
| 05:37 | twmd-routine-sync       | 17 條全 in-sync                                 |
| 06:14 | twmd-data-refresh-am    | 14 步刷新，文章 867                             |
| 06:42 | twmd-spore-harvest-am   | 6 events，465K reach spike + 1 escalation       |
| 07:09 | twmd-feedback-triage    | 隊列連續第三天空（非斷線）                      |
| 08:40 | twmd-maintainer-daily   | 動保.md merge-first + heal，修好一個壞掉的維基連結 |

另有 vortex-babel 產線整夜在指揮部這台連續跑（十語 unified dispatcher + 每小時脈搏快照），不屬 routine 飛輪但佔掉 110 筆裡的大半。

---

## 黃燈：live dump 55.4 小時沒更新，而且是第三天講同一件事

`docs/semiont/routine-live-state.json` 的 `fetched_at` 停在 2026-07-26T02:09，齡 55.4 小時，過了 48 小時門檻。

往回查這個檔的 commit 歷史，真正由 owner 更新的最後一次是 **2026-07-24 23:14 的 `twmd-data-refresh-pm`**。07-26 那兩筆（00:20 routine-sync 建排程、02:11 weekly-report Stage 2.5 前置）都是別條 routine 路過順手刷的，不是 rider 自己跑。

這一步的設計位置是關鍵：它是 **data-refresh skill 的 session 層 rider**，不在 `refresh-data.sh` 裡——因為它要呼叫 MCP `list_scheduled_tasks`，而 bash 摸不到 MCP server 的 store（DATA-REFRESH-PIPELINE.md:172 寫得很清楚）。所以它只能活在 session 的自覺裡，而自覺會漏。

今天 06:14 的 data-refresh-am 回報「14 步全綠，零 stale」，它的 memory 檔裡 grep 不到 rider / live-state / normalize 任何一個字。**owner 報全綠，而那一步根本沒發生**——這是「fire ≠ 完成」家族（REFLEXES #82 proxy signal / #60 silent default）在 rider 層的樣子。

昨天 09:33 的 flywheel-watch 已經寫過「每日 live dump 的 rider 沒自己跑」，當時齡還在門檻內。今天它跨過去了。同一個發現連三天 → 進 OBSERVER-QUEUE。

### 為什麼我不從這台補跑

補跑很容易，但會補錯。這台是指揮部，`list_scheduled_tasks` 列的是**指揮部自己的**排程；飛輪已整批遷到 mouhouse。現有 dump 的 17 條裡沒有 `twmd-flywheel-watch`（它跑在這台），正好證明那份 dump 反映的是 mouhouse。從這裡 dump 會把營運機的 live 狀態覆蓋成錯的機器，`fetched_at` 歸零、三層對賬全綠——換來一盞假綠燈，比停在 55 小時的黃燈更糟。

這正是這條 routine 存在的理由的反面：儀器只看見存在。要讓它看見缺席，就不能讓它自己去填那個缺席。

---

## 順手核到、但不歸我修的三件

1. **`routine-sync-check.py` 的 5 筆 `LIVE_ENABLED_DRIFT` 全是假陽性**。`twmd-flywheel-watch` 是「live 沒有」因為它跑在指揮部（SSOT 已標 🖥️commander-macbook）；`founder-lens-weekly` / `data-refresh-pm` / `maintainer-pm` / `music-media-audit-weekly` 四條 ROUTINE.md 排程表都已標 ⏸️（founder-lens 見註 ²³，2026-07-26 哲宇 directive）。**SSOT 沒有漂，是檢查器讀不到 ⏸️ 標記**。跟昨天「三條靜默警報兩條是假的」同一族，屬 routine-audit-weekly 的地盤。
2. **flywheel-watch 自己的 warn 文案混維度**：`silent` 空的時候仍然印「部分靜默。單條靜默常見原因⋯⋯」，而本次 warn 的唯一來源是 live dump 過期。讀的人會去找一條根本不存在的死 routine。訊息該跟著觸發原因走（REFLEXES #38）。
3. **`scripts/tools/routine-status.sh` 無輸出（rc=1）**，wake-context groundtruth 段四查掉了一查。BECOME 的過去 24hr 跑況這一欄目前是空的，今天靠 git log 直接補。

三件都寫在這裡不動手——這條 routine 只看不動手。

---

## Handoff 三態

- [ ] **OBSERVER-QUEUE #22**：live dump rider 靜默，預設選項 (a) 給 data-refresh skill 加 rider hard gate，default-action 2026-08-11
- [ ] **明天再看一次 live dump 齡**：若 08-11 前有任何 session 順手刷新，齡會歸零但病沒好——判準看 commit 是不是 data-refresh 自己打的，不看數字
- [x] ~~昨日「rider 沒自己跑」carry~~ retired by 本 session（已升 OBSERVER-QUEUE，handoff 不重複背）

---

_session 2026-07-28-093712-twmd-flywheel-watch — cron @ 09:30 指揮部。不碰營運機排程、不 pull、只 commit 本 routine 產出（工作樹有 169 檔 babel 平行產線，故開 worktree 隔離）。_
