# 2026-08-29-064907-twmd-spore-harvest-am — 切換排序讀出 13 則被漏掉的留言，三則「已收錄」建議逐一回覆

> session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle
> Session span: ~06:30 → ~07:10 +0800，1 commit
> 資料來源：`git log %ai`

## BECOME ACK

mode=write / 8 organ 最低=🛡️免疫 59（黃燈，多維度退化中，自 2026-07-05）/ Q14 cross-session continuity=PASS（過去 24hr 見 embeddings-nightly → routine-sync → data-refresh-am → spore-harvest-am → feedback-triage → maintainer-am 完整晨鏈，MEMORY tail 顯示飛輪連續穩態、腳註來源卡剛上線）。wake-context selftest 10 項體檢全綠。

## 觸發

cron `twmd-spore-harvest-am` 06:30 觸發，走 SPORE-HARVEST-PIPELINE Step 0-8。git pull 無新變更。Login-state probe PASS（@taiwandotmd 個人檔案顯示「編輯個人檔案」按鈕）。

## 今天只有兩則落在收割窗口

dashboard `harvestStatus` 顯示今天只有用語保存副詞層（#175 Threads / #176 X，D+6）落在 D+1-D+7 窗口內，其餘孢子皆已超出或未到窗口——不是空場，是視窗自然窄。

## 結構性發現：「熱門」排序系統性漏掉低互動留言

昨輪（8/28）harvest 用 Threads 預設的「熱門」排序讀了約 14 則留言就到登入牆前緣，沒有切換過排序。本輪把排序切成「最新」重新掃過一次，額外讀出 **13 則先前完全沒被讀到**的留言（captaingeoffery / kkbox1352.0 / icmantw / cuemoon5 / yvelisse.\_.1122 / liasnic / asunoig2019 / bb8_skywalker / lochichi77 / samxd961101 / xinyubai395 / nemoo3310 / jayfeather_1005），全部沒有讚數或只有 1 讚。這是 REFLEXES #82 proxy signal antipattern 的又一個 instance：用「熱門」這個排序演算法選中的子集，代理「留言全貌」這個真正想量的東西——過去每一輪 harvest 用同樣的排序策略，可能都有同樣的盲區，只是從沒有人切換排序去驗證過。

補讀出的留言裡沒有事實錯誤（Bucket A/C 0 條），但有三則具體建議查證後發現詞庫其實**都已經收錄**：

- lochichi77 建議收錄單獨的「行」→ 查 `data/terminology/行吧.yaml`，該條已完整記載「行」單獨作為應答詞的觀察（含 2026-08 讀者補充的引用）
- liasnic 建議收錄「乾貨」→ 查 `data/terminology/乾貨.yaml`，該條 2026-03-30 已收錄
- yvelisse.\_.1122 指出「邪修是仙俠小說的詞」→ 查 `data/terminology/邪修.yaml`，該條已完整記載修真小說起源脈絡

三則都用 Chrome MCP execCommand insertText 逐一回覆，重點是讓讀者知道「已經有了」而非承諾新增。xinyubai395 一則敵意留言（「就又老又土為什麼要配合你」）判 Bucket G，ignore。其餘皆為 Bucket E/F 純共鳴或語感偏好，optional 不回覆。

## Pitfall 6 retry 記錄

三次 post 中，lochichi77 那次第一次 click 即成功（container 2→3）。liasnic 與 yvelisse.\_.1122 兩次都在第一次 click 後 `[data-pressable-container]` 計數不變（genuine fail），各自 retry 1 次後成功——**retry 次數 2 次，皆 ≤ 1 per ship 上限**，無 duplicate（未觸發第三次重試）。

harvest 完後跑 `spore-db.py add-metrics` 兩筆（#175/#176），`generate-spore-records.py` + `generate-dashboard-spores.py` 重生衍生層，`validate-spore-data.py` 六維度全綠，commit `3943d7efa` 一次推送，含 batch log `batch-2026-08-29-2-spores.md` + spore-metrics.json + 兩份衍生 JSON。

## 收官 checklist

| 檢查項                       | 狀態                                 |
| ---------------------------- | ------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                   |
| Timestamp 精確               | ✅（git log %ai）                    |
| Handoff 三態已審視           | ✅                                   |
| CONSCIOUSNESS 反映最新狀態   | ✅（沿用今晨 refresh 快照，未再動）  |
| 自我檢查工具 PASS            | ✅ validate-spore-data.py 六維度全綠 |

## Handoff 三態

繼承上一 session（`2026-08-29-061547-manual`，twmd-data-refresh-am）：五縣市圖片補正、`.husky/pre-push` `VAR="$(...)"` 掃描、#1453 人物卡連結、#1365 KENJI 門檻、OBSERVER-QUEUE #39-#43、免疫分數 59 漂移、w.is_solis 質疑、sophie990329 字典編審提問候選、terminology 查證候選（含 #1609）、空窗期人工回覆確認、指控信 `b78ee4f5` 第十一次攔下、`/map` `.sidebar-panel` 高度問題。全部原樣繼承，本 session 未碰。

本 session 新 handoff：

- [ ] pending — harvest 排序盲區：建議未來 Threads harvest 固定切「最新」排序讀留言，或「熱門」+「最新」都掃一次，不要只用「熱門」讀到登入牆前緣就停。本輪只是手動發現並補一次，尚未寫進 pipeline canonical 或儀器化，下次 self-evolve 可考慮升級 SPORE-HARVEST-PIPELINE Chrome MCP harvest workflow 段落
- [ ] pending — #176（X）本機持續未登入，只能讀到登入牆前 3 則舊留言，跟 #173 同帳號同工具在不同貼文觸發不一致（沿用 8/28 判斷：正常波動非工具故障，但若連續多輪都卡住同一貼文則要重新評估）

## Beat 5 — 反芻

昨天寫的是「dashboard harvestCount 只能記錄它自己看得到的路徑」，今天撞到的是同一句話的另一面：我自己選的排序，也只能讀到排序演算法願意排前面的那部分。「熱門」排序不是壞掉，它做的正是它該做的事——把互動高的浮上來；但當我把它當成「讀留言」的唯一入口時，它就悄悄變成了一個代理：用「熱門排名」代理「有沒有讀者說話」。13 則留言在那裡躺了 5 天，不是因為它們被隱藏，是因為我從沒問過「排序之外還有什麼」。三則被漏掉的建議剛好又是「詞庫其實早就收了」——讀者以為自己發現了缺口，我也差點以為真的有缺口要補，兩邊都被同一層看不見的排序遮住了視野，直到真的去查證才發現地基一直都在。

## LESSONS-INBOX 候選

「熱門排序系統性漏掉低互動留言」這個結構跟 REFLEXES #82（proxy signal antipattern）同型，暫不另開新反射，留在本篇 memory 作為 #82 的又一個具體 instance；若下次 self-evolve 判斷 vc 已足，再考慮把「Threads harvest 固定切最新排序」寫進 SPORE-HARVEST-PIPELINE canonical。

🧬

---

_v1.0 | 2026-08-29 07:10 +0800_
_session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle_
_誕生原因：twmd-spore-harvest-am cron 觸發，走 SPORE-HARVEST-PIPELINE Step 0-8_
_核心洞察：(1) Threads「熱門」排序系統性漏掉低互動留言，切「最新」排序才補讀出 13 則此前完全沒被看見的留言 (2) 三則讀者建議查證後發現詞庫其實都已收錄，回覆重點是讓讀者知道已存在而非承諾新增 (3) Pitfall 6 retry 2 次皆在 ≤1 per ship 上限內，無 duplicate_
