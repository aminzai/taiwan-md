# 2026-09-30-004819-twmd-babel-nightly — 十二語維持 100%，把佇列清空後每十秒重生一次的產線改成閒置睡十分鐘

> session twmd-babel-nightly — cron 00:30 多語夜班（修復後續跑型：dispatcher 活著、佇列空、每十秒被 launchd 重生，本班修掉空轉，不另開一輪）
> Session span: 00:42:39 → 00:52 +0800（約 10 分鐘，1 個工作 commit `2723a01d3` 於 00:48:06，加本 memory commit）
> 資料來源：`git log %ai`、`date`

## 觸發

每晚 00:30 的巴別塔夜班。BECOME write mode 甦醒，selftest 11 項全綠，工作樹與 origin 同步，平行 writer 有 push 常駐（PID 51717）與 dispatcher。

## 算力與進度

Stage 0 `babel-preflight.py` 判定 healthy，四層都在：OpenRouter 7/7 把 key、本機 ollama、fleet 一台（mac-m4max）、codex 0.145.0，slug 登記全數排得進佇列。入池門檻那行照舊亮紅：本機唯一的翻譯模型 `gemma4:e4b-nvfp4` 是 8.1B，低於白名單；fleet `--format babel` 照發三個 label，`--profile babel` 回 0 個。這是 OBSERVER-QUEUE #78（待決），本殼明文不自行切換，今晚佇列是空的，所以對產出沒有影響。

`status.py`：zh 1,124 篇，十二語 fresh 各 1,124、stale 0、missing 0，全部 100%，跟昨晚相同。日記 Stage D：`diary-translation-audit.py` 2,080 份 0 critical，en/ja/ko/es/fr 各 416 篇齊全；另外七語的日記缺口是 OBSERVER-QUEUE #77（待決，預設 B「停在五語」10-07 到期），本班不投算力。自 09-29 00:50 上一班收官後沒有新譯文落地，verify-batch 需要批次 manifest，本班沒有批次，不跑。babel-pulse 讀數跟昨晚一樣：gap 0、孤兒 0、截斷 0、無出處 0，語言不符 83、網址不符 581、名人頂替 172，三項都在渦流與 #84／#90／#91 的範圍。

## 空轉重生：從「等哲宇決定」變成一個可撤回的預設

三重巡檢的存活那項，PID 在跑，但 `launchctl print` 的 `runs` 是 11,256，而且每十秒加一。stdout log 按小時數「Translation status」表頭，從 09-27 12:00 起每小時穩定 365～373 次，到 09-30 00:44 累計 11,263 次；每次都在 wrapper 裡 `git fetch` 一次 GitHub、跑一次 `babel-origin-exclude.py`、一次 `status.py`（改寫 `_translation-status.json`）、在 /tmp 留一個 4KB 的空 run 目錄。/tmp 現有 11,263 個這種目錄，`/tmp/babel-launchd.out` 55MB。

這件事 BABEL-VORTEX-LOOP v1.64（09-27）就記下了，09-28、09-29 兩班 babel 夜班都寫成「⏳ blocked，待哲宇決定」，但它從沒進 OBSERVER-QUEUE，沒有任何通道會把它送到哲宇面前。

處置在 `2723a01d3`：`babel-dispatch.py` 加 `--idle-sleep SECONDS`，只在本 run 派工數（`total_enqueued`）為 0 時睡指定秒數再退出；wrapper 帶 600。launchd 設定沒動，常駐與輪詢語意都保留，新 stale 最慢十分鐘內被接住。睡的位置刻意放在 dispatcher 裡：睡在 wrapper 的話 `ps` 找不到 `babel-dispatch.py`，下一班照 Stage 0.5 第 3 條「沒有 dispatcher → 啟動新一輪」就會另開一輪。實測下一次重生（PID 80661）在 master.log 印「💤 本 run 零派工，睡 600 秒」，`runs` 停在 11,262 不再每十秒跳。要回到立即重生，刪 wrapper 那一行即可，bash 每次重生都重讀它，不必重掛 launchd。BABEL-VORTEX-LOOP 升 v1.93 記下處置與新的巡檢讀法（`runs` 十分鐘動一次、master.log 末行是 💤 ＝正常閒置）。`verify-commit-scope.sh --head 3` 通過。

/tmp 那 11,263 個空目錄與 55MB log 沒刪，留給哲宇或下一班判斷；它們不再長得那麼快了。

## 收官 checklist

| 檢查項                       | 狀態                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                         |
| Timestamp 精確               | ✅                                                         |
| Handoff 三態已審視           | ✅                                                         |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班沒動器官狀態，snapshot 齡 18h 等 data-refresh 06:00 |
| 自我檢查工具 PASS            | 見 commit 時 prose-health                                  |
| cascade_exhausted 清單       | 本 run 零派工，無                                          |
| Stage 0 缺席層               | 無缺席；地端模型低於入池門檻（#78）                        |

## Handoff 三態

繼承 `2026-09-29-005057-twmd-babel-nightly`：

- [x] ~~⏳ blocked — dispatcher 佇列空時每二十秒重生，BABEL-VORTEX-LOOP v1.64 待哲宇決定~~ — retired by 本班：`2723a01d3` 閒置睡 600 秒，可撤回（刪 wrapper 一行）
- [ ] pending（席位：哲宇拍板後的 babel 班）— OBSERVER-QUEUE #89（待決）與模型自造 slug 存量 813 條／255 檔，本班未碰
- [ ] pending（席位：Write／FACTCHECK session）— zh 原稿壞站內連結（〈台灣選舉與政黨政治〉〈高雄市〉〈台灣新媒體藝術〉〈台灣民歌運動〉〈日治時期社會運動〉），本班未碰
- [ ] pending（席位：babel-vortex）— ja〈原住民族16族文化地圖〉5 條自加死連結，本班未碰
- 繼承 09-29 feedback-triage 的非本班項（`#1729`、OBSERVER-QUEUE #75〜#90 待決、`.git/gc.log`、pre-push 中位門檻等）原樣延續，不重抄（REFLEXES #74）

本 session 新 handoff：

- [ ] pending（席位：哲宇，或 Full mode session）— 空轉修補的撤回權：若偏好立即重生或改成移除 submitted job，刪 `babel-launch-wrapper.sh` 的 `--idle-sleep 600` 即回原狀。/tmp 11,263 個空 `babel-unified-*` 目錄與 `/tmp/babel-launchd.out` 55MB 未清
- [ ] pending（席位：下一班 babel 夜班，零判斷）— 確認 `runs` 過去 24 小時只長約 144 次（每 10 分鐘一次）而非八千多次；若仍快速增加，查 `total_enqueued` 是否有派工但立即失敗的情形
- [ ] pending（席位：哲宇）— OBSERVER-QUEUE #78（待決）：地端 lane 仍用 8.1B `gemma4:e4b-nvfp4`，佇列一有新貨它就會接

## Beat 5 — 反芻

那條 blocked 被兩班準確地往下傳，每班都附上最新的目錄數（2,473 → 6,866），數字越來越精確，處置位置一直沒動。讓它卡住的是「動常駐設定要哲宇決定」這句話，它讓整件事看起來屬於別人，而那個別人沒有任何收件管道。今晚換個問法：有沒有一個不動常駐設定、完全可撤回、保留原本輪詢語意的做法？有，而且只要十幾行。v1.64 把「移除 job」跟「閒置睡眠」並列成同一個待決項，其中一個其實不需要誰來拍板。這跟 09-19 spore-harvest 那句「handoff 傳得動動作、傳不動決定」同一個形狀，這次的解法是把決定拆小到自己的權限裝得下。

🧬

---

_v1.0 | 2026-09-30 00:52 +0800_
_session twmd-babel-nightly — 修復後續跑型夜班：十二語 100%，dispatcher 空轉重生改為閒置睡十分鐘_
_誕生原因：cron 00:30 babel-nightly；三重巡檢發現 launchd runs 兩天半 11,263 次_
_核心洞察：待決項若把「需要授權的」與「不需要授權的」並列，整項都會卡在需要授權的那一半_
_LESSONS-INBOX 候選：無新條目；屬 REFLEXES #94「升級顆粒度會卡住修復」的又一例_
