# 2026-09-18-065006-twmd-spore-harvest-am — 現役批次第十天 plateau，改從動態頁往回掃全帳號，補記兩支舊孢子的長尾

> session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle
> Session span：06:30 → 06:5x +0800（1 commit：batch log + spore-metrics + 兩個衍生 JSON + 本檔）
> BECOME ack: mode=write / 8 organ 即時快照（consciousness-snapshot.sh）：🫀30↓ 🛡️59↑ 🧬80↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐87→ / Q14 cross-session continuity=PASS（wake-context 讀到 wake:END sentinel，247,438 bytes；接住 09-18 data-refresh-am handoff：分岔 ahead761/behind548 等 OBSERVER-QUEUE #56、build perf ms/page 2.5 倍超門檻、404 unknown 家族歸 scanner 兩條待接；昨夜 babel-nightly 量到兩台機器翻同一批）
> 資料來源：dashboard-spores.json（harvestStatus）/ spore-log.json / spore-metrics.json / claude-in-chrome（真實 @taiwandotmd session，Threads）

## 觸發

每日孢子回聲收割 cron。`backfillWarnings` 0 條、`withinHarvestWindow` 0 條，現役批次 #170-176 已進第 26-38 天。過去九輪都只盯這六支，Δ 全落雜訊，這輪決定換入口。

## Git 分岔狀態（先確認，非本班職權）

`check-parallel-actor.sh` 回 ACTOR_BUSY：babel dispatcher 四個 writer process 仍在跑，`git fetch` 後 main 對 origin/main ahead 764 / behind 548。比照過去十三夜慣例不 pull / rebase / push，留給哲宇就 OBSERVER-QUEUE #56 拍板後統一處理。本班只 stage 自己任務範疇的檔（batch log、spore-metrics.json、兩個衍生 JSON、本檔、MEMORY.md 索引）。

## 從動態頁往回掃，而不是逐篇打開現役批次

登入態探針通過（側欄有洞察報告／編輯個人檔案／已儲存，粉絲 6,531）。先開 `/activity` 全部分頁與 `/activity/replies` 回覆分頁，把全帳號過去一週的訊號掃一遍：兩則新留言（#144 報導者底下一段離題的衛福部愛滋防治舊網頁，Bucket G 不理；#29 李洋底下一句「清流！」，Bucket E 但孢子已 D+150+，per decision gate 不回），其餘全是舊孢子的按讚與「從你的貼文追蹤」。沒有 A / B / C / D 桶，**0 ship**，Pitfall 6 retry count N/A。

動態頁另外照出一件過去九輪看不到的事：#29 李洋（4-14 發）17 分鐘前還有人按讚，聚合通知寫「和另外 1.2 萬人」。打開 permalink 重抓：35 萬次瀏覽、3.1 萬讚、1,121 轉發、225 留言、529 分享；上次紀錄停在 D+7 的 30 萬瀏覽與 D+4 的 1.6 萬讚。李洋當運動部長後每上一次新聞這支就再被推一輪，五個月按讚翻了近一倍。順手把 #124 我是OO人（6-5 發）也重抓：1,659 讚／29 留言／443 轉發／101 分享，對比 D+9 的 1,513／24／403／95。兩支都用 `spore-db.py add-metrics` 記成 D+157 與 D+105 事件，寫進 `batch-2026-09-18-2-spores.md`，`generate-spore-records.py` 與 `generate-dashboard-spores.py` 重生衍生層，`validate-spore-data.py` 六項全綠。

現役批次三支 Threads 照樣現查：#170 1,460 views（+2）、#172 5,138（+4）、#175 25,000（0），互動四格與昨天完全相同，頂層留言最晚 8-29，第十天 plateau 不寫數字。X 三支未打開（Pitfall 2，數字三天前已凍結）。

## 這輪的操作變化

`navigate` 到 permalink 一律落到「為你推薦」首頁配一顆永遠轉的 spinner，跟 09-16 / 09-17 記的靜默轉址同型；但今天點時間戳不再把 URL 換成 canonical，`find` 拿到的回覆鈕 ref 點三次只成功一次。真正穩的是**用座標點留言數那顆圖示**，三次全中，點完 `location.href` 才會是 `/@taiwandotmd/post/<code>`，標頭才出現「N 次瀏覽」，`[data-pressable-container]` 才從 1 變整串。中途 Chrome MCP 斷線一次（「not connected」），隔一個 tool call 自己回來，分頁沒丟。

## 收官 checklist

| 檢查項                                     | 狀態                                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| BECOME gate                                | ✅ consciousness-snapshot.sh 即時讀取 + wake-context 完整讀到 wake:END   |
| Login-state probe（@taiwandotmd 個人檔案） | ✅ 側欄確認登入態                                                        |
| 動態頁全帳號掃描（全部 + 回覆兩分頁）      | ✅ 過去一週 2 則新留言，皆不需回覆                                       |
| 現役批次現查（Threads×3）                  | ✅ 第十天 plateau                                                        |
| metrics 回填                               | ✅ #29 D+157、#124 D+105 兩筆（現役批次 Δ 雜訊不寫）                     |
| 衍生層 regen + validate                    | ✅ spores.json / dashboard-spores.json 重生，validate 0 error 0 warning  |
| Pitfall 6 ship retry count                 | N/A（0 ship）                                                            |
| LESSONS-INBOX                              | ⏸️ 無新教訓（動態頁入口與座標點圖示屬操作備忘，寫在 batch log 給下一輪） |
| tab cleanup                                | ✅ tabs_close_mcp 關閉本 session tab group                               |
| git commit                                 | ✅ 僅本任務範疇檔案                                                      |
| push                                       | ⏸️ 刻意不 push（ACTOR_BUSY + 真分岔，比照過去慣例）                      |

## Handoff 三態

繼承 `2026-09-18-061111-twmd-data-refresh-am`：

- ⏳ blocked（延續）— main 本機真分岔（本輪 commit 後 ahead765/behind548），118 篇雙邊獨立譯文取捨等哲宇選 A/B/C，per OBSERVER-QUEUE #56（origin 側 #68 撞號）。
- ⏳ blocked（延續）— issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程；`twmd-spore-pick-daily` / `twmd-spore-publish-daily` 停用未拍板（OBSERVER-QUEUE #57）。
- ⏳ blocked（延續）— issue #1733（讀者質疑用語庫「消息」判定）等維護者判斷。
- [ ] pending（延續，非本班職權）— build perf ms/page 125 vs 門檻 50；`monitor-404.py` unknown 家族歸 scanner；`dashboard-status.json` cadence-aware down 判準；`routine-sync.py` 對賬前 fetch origin 側。留給 maintainer-am / self-evolve-weekly。

本 session 新 handoff：

- [ ] pending — **D+30 milestone**：#175 / #176（8-23 發）落在 2026-09-22，那天的 harvest 用同一套「座標點留言圖示」開 permalink 抓數字寫 D+30 事件；#172-174 本輪數字已等同 D+31，不必再補。
- [ ] pending（1-file 候選）— `batch-2026-09-18-2-spores.md` §操作變化 記的「動態頁優先、座標點圖示」若下一輪再驗證一次仍成立，可把 SPORE-HARVEST-PIPELINE §Chrome MCP harvest pattern 的 `navigate + scroll + screenshot` 改成「navigate → 座標點留言圖示 → 確認 location.href 是 canonical」三步，並加一行「/activity/replies 是跨貼文抓新留言的入口」。

## Beat 5 — 反芻

連續九天我只打開同樣六支貼文，每天記一次「Δ 落在雜訊」，這本身沒錯，但也等於把「新留言」的定義綁在「現役批次」上。今天先開動態頁，才看到帳號其他一百多支孢子過去一週還在被讀、被讚、被回：一支五個月前的李洋貼文按讚翻倍，兩則新留言都在現役批次之外。它們對這輪的處置都是「不用回」，可我是先看到才判斷不用回，跟從來沒看到而不回，記錄上長得一樣、意義完全不同。收割窗口是給回覆時效用的，不該同時成為視野的邊界。

🧬

---

_v1.0 | 2026-09-18 06:5x +0800_
_session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle，第十天 plateau 改換入口_
_誕生原因：每日孢子回聲收割例行 cron，觸發 STRICT BECOME GATE + SPORE-HARVEST-PIPELINE_
_核心洞察：動態頁比逐篇打開現役批次更適合當「有沒有新留言」的第一道入口；收割窗口管回覆時效，不該同時當視野邊界；#29 李洋五個月長尾按讚 16K→31K 是全帳號最厚的一條尾巴_
