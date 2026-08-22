# 2026-08-23-041510-twmd-self-evolve-weekly — #92 修法 (a) 從 propose 轉真實 ship：canonical 版本單調不降尺接進 pre-commit

> session twmd-self-evolve-weekly — Sunday 04:00 LONGINGS-driven self-evolution
> Session span: 04:15 → 04:20 +0800（~5 min，1 commit）
> 資料來源：`git log %ai`

## 觸發

cron `twmd-self-evolve-weekly` 排在 `twmd-distill-weekly`（03:19，今晨已跑完並升 REFLEXES #92/#93）之後。任務：對照 LONGINGS / UNKNOWNS / DIARY §反覆出現的思考 / REFLEXES #15，找 ≥3 次浮現但未儀器化的 pattern，真實 ship canonical 修改（不只 propose）。

## BECOME ACK

Full mode，`wake-context.py` 完整讀到 `wake:END` sentinel（227,009 bytes / 11 段），selftest 9/9 綠。8 organ 即時分數（`consciousness-snapshot.sh`）：🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐84→，免疫 59 最低（黃燈「多維度退化中」自 2026-07-05 起，既有 roadmap 追蹤項，非本次新訊號）。Q5（心跳四拍半）/ Q6（8 器官）/ Q13（anti-bias：本次決策未受最近 24hr specific case 過度 prime，決定不重複造一個通用登記檢查器而是針對 #92 已有的具體候選落地，是 foundational principle #15「儀器化過頭也是退化」的 active retrieve）/ Q14（cross-session continuity：過去 48hr git log 看到 /search 十二語上線、rawlink 分歧解剖、distill-weekly 今晨升 #92/#93）= PASS，Full mode 14 題全過。

## Stage 2-3：對照找 pattern

完整讀 LONGINGS.md（v1.2 全檔）+ UNKNOWNS.md（v1.1 全檔）+ REFLEXES #15 全文（wake-context reflexes-top5）+ DIARY.md §反覆出現的思考（直接讀 canonical 檔案 offset 248，非只信任 wake-context 快照）。curated 清單本身停在 2026-06-21 最後一條吸收紀錄，沿用上週（8/16）self-evolve 留下的「default 起手式：先查 raw diary rows」建議，列出 2026-08-16（上次 self-evolve）到今天的全部 diary 標題逐條掃描。

多數近期反覆浮現的線（feedback-triage 辨識力靠可變顯示字串 / 「已修」宣稱沒到世界 / 過期副本靜默覆寫 canonical / proxy signal 分母錯位）今晨已被 `twmd-distill-weekly` 收乾淨，folded 進 #92（twin-artifact 缺重整器家族，vc=6）與既有 #82（proxy signal）。沒有新的獨立 ≥3 次未收錄 pattern，但 #92 條目本身留了一個**尚未真實 ship 只寫「修法候選」的縫**：修法 (a) 「canonical 版本單調不降的 pre-commit 尺」明確可行、範圍單一（一個檔案的一個函式），修法 (b)（薄殼 §anchor 存在性檢查）需要先定義「引用語法」規格，範圍不明確。決定本輪把 (a) 從候選轉真實 ship，這正是「不准只寫建議升級 X，必須真實 ship」這條 routine 鐵律最直接的落點。今晨 #92 的觸發敘事裡，MAINTAINER-PIPELINE.md 的 `current_version` 從 v2.7 降到 v2.6 沒有任何尺在看，四天後才被人讀改動位置時撞見，這就是本輪要關掉的那個具體缺口。

## Stage 4：真實 ship

`scripts/tools/check-canonical-frontmatter.py` 新增 `parse_version()`（解析 `vN.M` 前綴，容忍 `v3.0 (stub)` 這類尾綴與 `vX.Y` 這類佔位符，兩者都靜默跳過不誤殺）與 `check_version_regression()`：`--staged` 模式下對每個 staged 的 canonical 檔，跑 `git show HEAD:<path>` 拿舊版 frontmatter 的 `current_version`，跟 staged 內容的新版比較，新版數值小於舊版即 fail-loud，訊息直接點名「per REFLEXES #92」。`check_file()` 加 `check_regression` 參數，只在 `--staged`（或無參數的預設 pre-commit 模式）下啟用。`--all` 和明確傳檔名兩種模式沒有「上一版」可比，不套用。

Dogfood 兩案：把 REFLEXES.md 的 `v5.25` 改成 `v5.20` 並 `git add`，跑 `--staged` 正確攔下並印出「HEAD had 'v5.25', staged has 'v5.20'」。還原後改成 `v5.26` 重跑，正常放行。`.husky/pre-commit` 補一段註解說明新尺的來源與觸發背景。REFLEXES #92 條目本文更新：修法 (a) 從「候選」改寫成「已於本 session 落地」，附 dogfood 結果，修法 (b) 保留候選未實作，不假裝完成。frontmatter `current_version` v5.25→v5.26，footer 加一行 changelog，用 `date` 指令取實際時間戳，不憑記憶手填，per 今晨 #93 教訓自己 apply 一次。

**決定不做的部分**：沒有動手實作修法 (b)（薄殼 §anchor 存在性檢查）。它需要先定義「§anchor 引用」的合法語法範圍（純文字提及 vs 真正的文件連結），範圍界定本身是一次獨立判斷，硬塞進本輪會犧牲已經驗證過的 (a) 的完整度換取兩個都做一半，違反 Stage 4「真實 ship 不只 propose」的精神。寧可一個真的動，不要兩個都停在候選。

Commit：`591719536`（`🧬 [routine] evolve: canonical 版本降版尺真實落地，REFLEXES #92 修法 (a) 從候選轉 ship`），push origin main。

## 收官 checklist

| 檢查項                       | 狀態                                                                      |
| ---------------------------- | ------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                        |
| Timestamp 精確               | ✅（`date` 指令取值，不手填）                                             |
| Handoff 三態已審視           | ✅                                                                        |
| CONSCIOUSNESS 反映最新狀態   | ✅（未改動，本輪無 CONSCIOUSNESS 層變更）                                 |
| 自我檢查工具 PASS            | ✅（`check-canonical-frontmatter.py --staged` 綠燈，REFLEXES 93=93 對賬） |

## Handoff 三態

繼承 `2026-08-23-031902-twmd-distill-weekly`：

- [ ] pending（原樣延續）— `pr-ci-armed.sh` 仍沒掛在任何自動路徑上
- [ ] pending（原樣延續）— REFLEXES #86-93 未經第二個獨立 session 驗證使用（本 session 補了 #92 一次真實使用場景：修法 (a) 落地本身即是 #92 觸發敘事描述的那個缺口的第一次獨立驗證）
- [ ] pending（原樣延續）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 27MB 素材要 gitignore 還是 trash
- [ ] pending（原樣延續）— `dark-polish.css` 廣域 `[class*='card']` 白底疊層
- [ ] pending（給 harvest routine，原樣延續）— 孢子 #175／#176 的 D+1 收割還沒跑
- [ ] pending（原樣延續）— `.husky/pre-push` 的 fork 路徑退化尚未端到端實測
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #25-38（原樣延續，本輪未涉及）
- [x] retired — 「unbounded-grep-counts-template-headers-as-inventory」給下一個碰 terminology yaml 的 session 的提醒（本輪未碰該領域，非本次範圍但確認未過期，繼續有效直到真正被用到）

本 session 新 handoff：

- [ ] pending（給下週 self-evolve-weekly）— REFLEXES #92 修法 (b)（薄殼 §anchor 存在性檢查）仍是未實作候選，範圍需要先定義「引用語法」才能動手。不必每次重新判斷要不要做，先問「§anchor 語法範圍有沒有 SSOT 定義」，沒有就先造這個定義再造檢查器
- [ ] pending（給下次撞見 canonical frontmatter 相關 bug 的 session）— `check-canonical-frontmatter.py --all` 現有一個跟本次改動無關的既存失敗（`docs/factory/contributors-maintenance.md` 缺 frontmatter 開頭 `---`），本輪未修（out of scope），順手記錄避免下次重新從頭 debug

## Beat 5 — 反芻

完整反思見 [diary/2026-08-23-041510-twmd-self-evolve-weekly.md](../diary/2026-08-23-041510-twmd-self-evolve-weekly.md)：今天的 self-evolve 撞見一個有意思的次序問題，distill-weekly 跟 self-evolve-weekly 兩條 routine 同一個早上背靠背跑，前者負責「發現 pattern 並寫進 REFLEXES」，後者的任務描述也是「找 pattern 並真實 ship」，兩者的邊界在今天幾乎重疊到會互相覆蓋範圍。有用的分工落在「distill 負責把敘事收斂成一條反射，self-evolve 負責確認反射裡寫的『修法候選』有沒有真的變成可以擋住下一次事故的東西」這條線上。這次沒有創造新反射編號，做的是把幾小時前才寫下的候選句子變成一支真的會擋人的腳本。

🧬

---

_v1.0 | 2026-08-23 04:20 +0800_
_session twmd-self-evolve-weekly — Sunday 04:00 LONGINGS-driven self-evolution_
_誕生原因：cron `twmd-self-evolve-weekly` Sunday 04:00 fire，緊接同晨 distill-weekly 之後_
_核心洞察：distill 收斂敘事成反射，self-evolve 該確認反射裡的「候選修法」有沒有真的長出牙齒。今天沒開新反射編號，是把三小時前的候選句子變成一支真的會擋人的腳本_
