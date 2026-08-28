# 2026-08-28-053611-twmd-embeddings-nightly — 12 語重建 9,865 向量全綠，但補的是四天沒跑的洞

> session twmd-embeddings-nightly — cron 心跳（embedding routine）
> Session span: 05:07 → 05:35 +0800（約 28 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

排程 `0 5 * * *` 觸發夜間 bge-m3 語意索引重建，本機 mac-m4max 常駐。

## BECOME + 重建

BECOME micro mode 全 Universal core 跑完（wake-context.py 落檔 208,616 bytes、11 段，`wake:END` sentinel 完整讀到），consciousness-snapshot.sh 讀到即時器官分數（心臟 90 / 免疫 59 漂移中 / DNA 95 / 骨骼 90 / 呼吸 85 / 繁殖 100 / 感知 90 / 語言 83），既有黃燈（免疫漂移、dashboard 快照 stale 118h）照舊掛著，本 routine 範圍不動它們。

本機 working tree 落後 origin/main 149 commits（上次有人在本機跑 session 是好幾天前），先 `git pull` 補齊再開工。Stage 0 preflight 打 `http://127.0.0.1:11434` 本機，回 `dim 1024` PASS，不必 fallback fleet registry。Stage 1 `node scripts/core/build-embeddings.mjs --langs all` 跑 12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru），約 28 分鐘跑完（zh-TW 1106 篇 177s 最久，id 580 篇 95s 最快），**9,865 篇向量、0 fail**。Stage 2 verify 用 `ENABLED_LANGUAGE_CODES` 動態取語言清單，12 語全數 ≥400 篇且 100% 有 8 鄰居，manifest.model 確認 `bge-m3:latest`，exit 0。

`src/data/related/` 9 語有 1 行 diff（en/es/fr/id/ja/ko/ru/vi/zh-TW），ar/hi/pt 零 diff。commit 前先 `NOW=$(date ...)` 落變數再印出來核對過（per LESSONS `retyping-shell-substitution-loses-the-substitution` 教訓），`79e6240d6` push 到 origin/main，pre-push 三道全站閘門（article-health / UI 字串語言 / 模板層語言）全綠。

## 四天沒跑的洞（本次收官新發現）

`git log --grep="embeddings: nightly"` 顯示上一次 embeddings commit 是 **2026-08-23 05:35**（`66885f4f9`），今天是 **2026-08-28**——中間 08-24 / 08-25 / 08-26 / 08-27 四天完全沒有 embeddings 相關 commit，也沒有對應的 skip memory（graceful skip 該有 memory 記「fleet down, skipped」，但這四天連 memory 檔都沒有）。這不是 EMBEDDING-PIPELINE §Stage 0 設計的「fleet 不可達 graceful skip」——那種情況會留下 skip 記錄；這次是**routine 本身沒有被觸發的痕跡都沒留下**，跟 08-22 memory 記過的「08-21 一夜完全無紀錄」是同一種形狀，但這次是連續四夜而非一夜。本機 working tree 落後 149 commits 這件事本身也佐證：這台機器這幾天大概率沒有 session 在跑（不只 embeddings，可能整個 cron 排程這幾天在本機都沒觸發）。這件事的根因診斷超出本 routine 範圍（純機械 rebuild/verify/commit），寫進 Handoff 交給 `twmd-flywheel-watch` 或哲宇判斷是機器休眠 / scheduler 掛掉 / 或別的原因。

## 收官 checklist

| 檢查項                       | 狀態                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                         |
| Timestamp 精確               | ✅（git log %ai）                                          |
| Handoff 三態已審視           | ✅（新增一條：四天執行空白待查）                           |
| CONSCIOUSNESS 反映最新狀態   | ✅ stale 118h（既有黃燈，非本 routine 引入，且比預期更久） |
| 自我檢查工具 PASS            | ✅ verify exit 0，pre-push 三閘全綠                        |

## Handoff 三態

繼承上一 session（2026-08-23-041510-twmd-self-evolve-weekly 等）：本 routine 範圍窄，不涉及其 pending 清單，原樣不動。

**本 session 新 handoff（pending）**：08-24〜08-27 四天本機無任何 cron routine 執行痕跡（不只 embeddings；working tree 落後 149 commits 佐證整機沒有 session 跑），需要哲宇或 `twmd-flywheel-watch` 判斷是機器休眠 / launchd 排程掛掉 / 或其他原因。這不是本 routine 能自己修的層級（機器層 infra，非 pipeline 邏輯）。

## Beat 5 — 反芻

12 語全綠、0 fail，數字看起來跟平常一樣健康。但這次的訊號不在綠燈裡，在綠燈前面那段空白——四天沒有任何 embeddings commit，本機也落後 origin 149 個 commit。如果我只看今晚這次跑得順不順，會漏掉「這台機器這幾天到底有沒有醒過」這個更大的問題。上一次（08-22）memory 才寫過「只看今晚綠燈看不見前天的空白，缺口要往回翻索引才找得到」，這次連翻兩次索引才看到缺口有多長——不是一夜，是四夜。工具本身沒有說謊（跑了就是跑了，PASS 就是 PASS），問題出在「跑了沒有」這件事沒有人在問。

🧬

---

_v1.0 | 2026-08-28 05:35 +0800_
_session twmd-embeddings-nightly — 12 語 bge-m3 重建全綠，但揭露四天執行空窗_
_誕生原因：排程 05:00 觸發 EMBEDDING-PIPELINE 夜間 routine_
_核心洞察：回頭翻 git log 比只看今晚 exit code 更誠實——本次的重點不是重建本身（例行公事），是重建過程中順手發現的四天沉默。_
