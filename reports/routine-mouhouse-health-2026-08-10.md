# Routine 飛輪遷居 mouhouse 後的完整健檢（D+17）

> session `2026-08-10-144521-mouhouse-audit` — 哲宇 directive「連去 mouhouse，看整個轉移 taiwan.md routine 後整個運作狀態如何，有沒有要修復的東西，深度研究後歸檔 report 到 Obsidian」。
> 方法：Full mode BECOME → 指揮部側 git／儀器對賬 → SSH 進 mouhouse 分層健檢（系統／repo／排程／憑證）→ origin/main 逐日 fire 率統計 → 讀遷移後全部異常 memory。
> 姊妹檔：本報告同步歸檔哲宇 Obsidian vault `Projects/Taiwan.md/`。

## 總評

**遷移成功，飛輪健康。** mouhouse-macmini 自 7/24 開機起連續運轉 16 天 21 小時未斷，遷移後 16 天裡每天該跑的 daily routine 全勤（唯一一次缺勤是 8/6 spore-harvest，屬 Chrome MCP 擴充功能故障期，當時已被 LESSONS vc 累積接住）。週日反思鏈四工位、週一 supporters、月度 terminology-trends 全部照排程 fire。排程層三層對賬連續十七輪一致，repo 乾淨零未推零 untracked，憑證全齊。

真正的問題有兩個，都卡在**登入態層**，都是 human-only：Gmail MCP 連三週缺席（贊助資料缺口 4 週）、Threads/X 帳號登出連 2 天（3 則讀者回覆草稿卡住）。另外本次健檢在 mouhouse 的 agent worktree 裡挖出一篇被額度斷頭事故困住 16 天的**完整孤兒文章**（台灣公投制度，53KB），已撿回留證。

## 一、時間線回顧

| 日期       | 事件                                                                                                                                                                               |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7/24       | 遷移日：機器面全部完成（工具鏈 user-space、repo clone、build 煙霧測試 66s exit 0、憑證搬遷、19 條 task prompt 落位）                                                               |
| 7/25       | cutover 完成；同日哲宇三個 directive：babel 營運機暫停（避撞指揮部算力軍團）、rewrite 兩台皆停（額度控制，當晚營運機撞過一次 5 小時上限）、指揮部 18 條排程刪除只留 flywheel-watch |
| 7/25 19:06 | rewrite-daily 最後一次 fire——本次健檢發現它的產出（台灣公投制度.md）從未 commit，困在 agent worktree（見 §五）                                                                     |
| 7/26       | founder-lens 停用（哲宇：效果不好）；指揮部撿回 24 個孤兒（16 落地 6 隔離）——漏了 agent worktree 裡這篇                                                                            |
| 7/26–8/10  | 穩定運轉期：daily 全勤、三次週日反思鏈完整、8/5 terminology-trends 月度首跑                                                                                                        |
| 8/5–8/8    | spore-harvest Chrome MCP 擴充功能故障四天（8/6 完全沒跑），8/9 連線恢復但退到登入層阻塞                                                                                            |
| 8/10       | 哲宇關 flywheel-watch（「幫助不大」）——本報告同日把 SSOT 對齊並補了替代視角（見 §六）                                                                                              |

## 二、機器層（全綠）

- **uptime 16d21h**（7/24 起未重開）、load ~1.0、記憶體 free 93%、磁碟餘 778Gi
- 電源設定齊：`sleep 0`／`autorestart 1`／`womp 1`，斷電自復活三件套在位
- Claude Desktop app 常駐（8/8 20:39 起本輪，重啟過一次無影響）、Chrome 常駐、ollama serve 常駐（bge-m3／embeddinggemma／gemma4 三模型在位）
- 憑證層：`gh auth` 有效（frank890417，repo+workflow）、GA4 service account／OpenRouter／Resend／feedback env／codex／gemini 全在
- repo：working tree 乾淨、0 未推、對 origin 只落後即時產線 1 筆

觀察項（不動手）：一條 8/9 08:15 起的 claude CLI 進程殘留 31hr+（0% CPU、533MB，app 未回收 session；機器記憶體無壓力，不擋新 routine）。兩個歷史 stash（7/25 孤兒 WIP 快照、golive 前狀態）保留為證據鏈。

## 三、排程層與 fire 率（全綠）

**逐日 routine memory 檔統計（origin/main ground truth）**：7/26 起每天穩定 7 檔（mouhouse 6 daily + 指揮部 flywheel-watch），週日 11-12、週一 8。16 天 × 平日 7 條的應跑格子裡，唯一缺格是 8/6 spore-harvest（Chrome MCP 故障期）。

- live 排程器 13 enabled / 5 disabled，與 ROUTINE.md SSOT 一致（8/10 routine-sync 第十七輪 18 條 in-sync 零漂移）
- 每條 routine 的 memory 開頭都有完整 BECOME ACK（wake-context 讀到 sentinel 的 bytes 數為證）——遷移沒有讓 STRICT BECOME GATE 鬆掉
- 品質內核活著的證據：flywheel-watch 四次自校假象、maintainer 連兩天挖出檢查器對中文檔名靜默全跳的家族病、supporters 第三次阻塞時主動把教訓從「散落 handoff」聚合成正式 LESSONS entry、feedback-triage 被前日自己的約束擋住「為了好看再焊一道閘門」

**遷移報告的驗收定義已達成**：24h 內 6+ daily 時段命中 ✓、7 天內週日反思鏈四工位 + supporters 各 fire ✓（founder-lens 後被哲宇停用，不計）。

## 四、問題清單

### P0 — human-only，等哲宇（兩個都是登入態層）

1. **supporters-weekly Gmail MCP 缺席 vc=3**（7/27、8/3、8/10 連三週）：scheduled-task 執行環境找不到任何 Gmail 工具（7/13 首跑成功過，是後來 drift——`cron-execution-env-tool-availability-drift`）。贊助資料缺口累積 4 週（checkpoint 停 7/12）。已在 LESSONS P0，三選一：(a) 補掛 Gmail connector 到該執行環境 (b) routine 遷到有 Gmail 的環境 (c) 換讀信管道。checkpoint 設計冪等，跑通一次即補齊全部空窗。
2. **Threads/X 帳號登出**（8/9 起連 2 天）：mouhouse 的 Chrome 需人工重新登入一次。8/5-8/6 累積的 3 則 Bucket E reply draft（@haoyingmiao／@daphne.globalsun／@huwenxian54）卡在登入層後待補發。harvest 本身在登出態仍可讀公開數據（8/10 D+6 已完成）。

### 本次修復（自主權內，同 commit ship）

3. **`routine-status.sh` v2**：修掉「當天尚無 memory 檔時空 glob 撞 `set -euo pipefail`，整支腳本 rc=1 一行不印」的殼層 bug（fail-loud 被通道截成 fail-silent，今晨 wake-context groundtruth 的 ⚠️ 就是它）；並補 **origin/main 雙視角**——飛輪遷走後這把尺只讀本機 checkout，指揮部產線期間不 pull 就把「本機 stale」誤讀成「飛輪停擺」（本 session 甦醒時親身被誤導一次）。v2 起本機 ∪ origin/main 取聯集、標注 origin ref 齡。
4. **ROUTINE.md SSOT 對齊 flywheel-watch 停用**（哲宇 8/10 directive「幫助不大」）：排程表標 ⏸️、PAUSED 5→6 條、新增註 ²⁵ 記錄停用理由與缺席監看的兩層承接（routine-status.sh v2 被動視角 + weekly-report 週級 liveness 對賬），避免 v2.9「死 routine 列 active 15 天」同型病。
5. **孤兒文章救援**：`台灣公投制度.md`（53KB，7/25 rewrite-daily 最後一跑的產物，額度斷頭未收官，困在 mouhouse agent worktree 16 天）撿回留證至 `reports/orphan-rescue/`；mouhouse 側殘留 worktree 已清。**不自動上站**：researchReport 指標斷（報告不存在）、寫作 session 驗證痕跡不可考，article-health 體檢 hard=2 warn=16（後台洩漏 7 處＝polish 輪沒跑完的典型樣貌）。處置待決：補研究報告重驗後上站，或作為素材重跑 rewrite。

### 觀察項（不動手，列給未來）

- 殭屍 CLI session 與歷史 stash（§二）
- BECOME §Step 9 表 Review 欄勾 12 題但過題數寫 11 的計數 drift（8/10 maintainer 已留痕給 self-evolve）
- babel-nightly 維持暫停正確：恢復條件「軍團批次收工」未到（指揮部產線本日仍整點落地）
- 免疫黃燈第 36 天（OBSERVER-QUEUE #25）、UNKNOWNS EXP-2026-07-17-G 過期未判定（404 收斂驗證，due 8/7）——皆非 mouhouse 事務，另有 owner

## 五、孤兒文章事故的結構教訓

7/25 深夜的額度斷頭讓 rewrite session 死在收官前，產出困在 `.claude/worktrees/agent-*`。7/26 的孤兒大撿回（24 個）漏了它，因為那次掃的是主工作樹的 untracked，**agent worktree 是另一個沒人巡的角落**。16 天裡 repo 乾淨、對賬全綠、儀器無聲——又一個「儀器只看見存在、看不見缺席」（REFLEXES #82／#69）的活案例：一篇不存在於任何索引的文章，沒有任何一把尺會替它叫。

candidate 方向（不在本次 scope，留給 self-evolve 判）：worktree-gc 或 weekly-report 體檢加一步「掃兩台機器的 `.claude/worktrees/*` 有無 untracked 產出」。

## 六、flywheel-watch 停用後的監看拓撲

哲宇今日停用 flywheel-watch 的理由（日更綠燈資訊量低）成立：監看儀器的價值在異常時刻，每天一條「飛輪在轉」是注意力稅。停用後的缺席監看由兩層被動視角承接：

1. **routine-status.sh v2（本次 ship）**：任何 session 在指揮部甦醒，BECOME groundtruth 自帶 origin/main 過去 24hr routine 痕跡——飛輪整體停轉時，甦醒第一眼就是空清單加「檢查營運機」提示。零排程成本，覆蓋所有互動 session。
2. **weekly-report `routine-liveness-check.py`**（週日）：fire-vs-commit 對賬，最長延遲 7 天。

殘餘風險誠實列出：兩層都是被動的。若指揮部連續多天沒有任何 session 甦醒、又不是週日，飛輪靜默的最長無人知窗口是 7 天（舊：1 天）。若這個窗口不可接受，方向是 alert-only 模式（綠燈靜默、WARN/CRITICAL 才 PushNotification），不是恢復日更。

## 七、給下一個 session

- P0 兩項（Gmail connector／Threads 登入）只能等哲宇在 mouhouse 上做一次人工動作，做完後 supporters 與 reply 補發都會自動歸位。
- 孤兒文章在 `reports/orphan-rescue/2026-08-10-台灣公投制度-rewrite-orphan.md`，上站前必須：補研究報告或重驗全文事實原子、清 7 處後台洩漏、補 `lastHumanReview`。
- routine-status.sh v2 若在 mouhouse 端也要新視角（它本機 checkout 永遠新鮮，不需要，但無害），routine-sync 會自然同步 prompt 層，工具層走 git。

🧬
