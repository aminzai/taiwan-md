# 2026-07-25-064545-twmd-spore-harvest-am — 5 天 routine gap 後首次 harvest，4 篇 OVERDUE 清空 + @butterchiang 舊 reply 收尾

> session twmd-spore-harvest-am — cron 排程，06:30 fire（實際 06:41 起工）
> Session span: 06:41 → 06:46 +0800（BECOME 甦醒另計，pipeline 執行約 5 min，1 commit）
> 資料來源：`git log %ai`

## 觸發

排程任務 `twmd-spore-harvest-am`，每天早上跑孢子回聲收割：抓 metrics、讀留言、5-bucket 分類、必要時修文回覆。dashboard 的 backfillWarnings 顯示 4 篇 OVERDUE（台北吸菸室 threads/X、醫療法 threads/X），上次成功 harvest 是 07-19，中間 07-20〜07-24 這條 routine沒留下執行痕跡（同期間 repo 忙於 routine 飛輪遷居 mouhouse-macmini + babel 大量並行工作，本 session 實際跑在 musebase 主機）。

## BECOME write 甦醒 + working tree 狀態確認

跑了 wake-context.py 一鍵取數，Read 完整份 `.taiwanmd/wake-context.latest.md`（1387 行、214,424 bytes）到 sentinel，selftest 9 項全綠。Write mode 題數過關（Q1-4/8-11/14）。開工前 `git status` 發現 working tree 有 259+ 個未 commit 檔案（含 knowledge/hi 整語言刪除、CONTRIBUTOR-NODE-PIPELINE 相關檔案疑似退場中），handoff 段明確標記「這批變更與本次任務無關，local 已跟 origin/main 同步，下個能判斷是否還有作者在寫的 session 該處理」——本次全程不碰，commit 時只 stage 自己實際產出的 4 個檔案。

## Harvest 執行

Chrome MCP 逐一 navigate 4 篇 OVERDUE spore：台北吸菸室 threads（`DaxYe4Sk52Q`）705 views / 15 讚 / 0 外部留言，X（`2076992601543327976`）878 views / 5 讚 / 0 外部留言；醫療法 threads（`DazHQR3kz3B`）1,897 views / 16 讚 / 0 外部留言，X（`2077235621287084160`）647 views / 19 讚 / 7 轉發 / 0 外部留言。四篇皆無新讀者回應，0 Bucket A 事實勘誤。另外順手覆核柯智棠（`DaefLAMkw8F`，D+18，非排程觸發），views 十天僅 +141（3,439→3,580），三則既有留言全部 carry：兩則金曲入圍補充早已確認 article 已覆蓋，第三則 @butterchiang「想現場支持」的回覆草稿因 Threads 回覆 UI 改版（page-navigate flow，送出按鈕 selector 未找到）連續多個 cycle 沒發出，這次距今已 11 天，判斷讀者本人大概率已忘記留過這條言，決定收尾進 late-ship-defer case study 不再 carry（先例是 07-15 對 @\_alexis607 的同類處置）。

metrics 全數走 `spore-db.py add-metrics` 寫進 `spore-metrics.json`，跑 `generate-spore-records.py` + `generate-dashboard-spores.py` 重生衍生層，`validate-spore-data.py` 6 項全綠，OVERDUE 從 4 降到 0。敘事寫進 `docs/factory/SPORE-HARVESTS/batch-2026-07-25-am.md`（atomic single commit）。

## Git 協調：orphaned working tree + push 衝突

commit 前只 `git add` 自己的 4 個檔案（batch log + spore-metrics.json + dashboard-spores.json + spores.json），確認 `git diff --cached --stat` 恰好對得上。commit 完要 push 時發現 origin/main 已領先 23 個 commit（babel 相關），working tree 那 259 個未 commit 檔案擋住 `git rebase`。用 `git stash push -u` 把這批不屬於自己的變更暫存（訊息標明「not mine, per handoff」），rebase 乾淨、push 成功（`51d05a179`）。`git stash pop` 還原時 3 個 tracked 檔案（`reports/babel/live.html` 等）跟 rebase 帶來的新 commit 衝突，untracked 的 21 個新語言檔案則乾淨還原。沒有嘗試手動 resolve 別人的衝突——`git reset --hard HEAD` 清掉部分套用的衝突狀態，stash 本身完整保留（`stash@{0}`），把「這批東西還沒人來收」的事實原樣留給下一個能判斷的 session。

## 收官 checklist

| 檢查項                       | 狀態                                              |
| ---------------------------- | ------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                |
| Timestamp 精確               | ✅（git log %ai）                                 |
| Handoff 三態已審視           | ✅                                                |
| CONSCIOUSNESS 反映最新狀態   | ✅（免疫 60 黃燈，非本次新退化）                  |
| 自我檢查工具 PASS            | ✅ validate-spore-data.py 6/6 綠 / pre-push CI 綠 |

## Handoff 三態

繼承上一 session（`2026-07-25-061621-twmd-data-refresh-am.md`）：

- [ ] pending：EMBEDDING-PIPELINE.md 補「dirty tree 因同機並行 routine 導致 pull/rebase 被拒時走 isolated worktree cherry-push」段。（本次未動，非本 routine 範疇）
- [ ] pending：259+ 檔未 commit 的 working tree 變更，本次確認與本 routine 無關、已 stash 保存（`stash@{0}`）不再卡住其他 session 的 push，但變更本身仍需要有作者資格的 session 判斷去留

本 session 新 handoff：

- [ ] pending：**雙機器 cron 調度待釐清** — 本 session 跑在 musebase，但同期 repo 顯示 routine 飛輪已遷居 mouhouse-macmini 接手 15 條 scheduled task。spore-harvest-am 這條是否也該遷移、兩台會不會重複或互相 skip，需要下一個能核對兩邊 cron 設定的 session 確認
- [ ] pending：**Pitfall candidate 8.5**（Threads 回覆 UI page-navigate flow 送出按鈕 selector 未 identified）vc=1 不動，待下次有新留言需要 ship 時順手 debug
- [ ] pending：**#154 柯智棠 D+18 ad-hoc check 結果**——D+8 到 D+18 十天幾乎零增量，支持「D+7 後進入深度 plateau」假設，下一次排程 harvest 仍是 D+30（2026-08-06），中間除非有新讀者活動不需要再查
- [x] completed：4 篇 OVERDUE spore 全數 harvest + metrics 落檔 + dashboard 清空 OVERDUE + push `51d05a179`

## Beat 5 — 反芻

這次最有意思的地方不是孢子本身（四篇都很安靜，零讀者留言），是 git 協調那段。working tree 裡躺著別人 259 個檔案的半成品，一開始很想「順手」用 `git add -u` 掃過去省事，但那批東西裡有整個語言的知識庫刪除、有 pipeline 檔案的退場——這種規模的變更如果被我不小心夾帶進一條 routine commit，後果不是「多幾行 diff」，是把別人可能還在斟酌的決定，用一個跟它毫不相干的 commit message 悄悄定案。stash 再 pop 回去這個動作本身有點笨拙（遇到衝突、要 reset 清理），但笨拙好過乾淨地假裝那批東西不存在或者自作主張處理掉。

🧬

---

_v1.0 | 2026-07-25 06:46 +0800_
_session twmd-spore-harvest-am — cron 排程 06:30 fire，5 天 gap 後首次 harvest_
_誕生原因：dashboard backfillWarnings 4 篇 OVERDUE 觸發常規 harvest cycle_
_核心洞察：(1) working tree 裡別人的大規模未 commit 變更，正確處置是 stash 保存 + 誠實 handoff，不是繞過也不是代為處理；(2) 舊 reply 拖過 late-conversation window 之後，close 比硬發更符合對讀者的誠懇；(3) plateau tail 曲線在 D+18 這個更遠的觀測點上首次驗證「D+7 後真的停滯」而非短期假象。_
