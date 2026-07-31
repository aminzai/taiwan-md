# 2026-07-31-064425-twmd-spore-harvest-am — 6 事件收割，鎢文事實查核驗證通過，發現回覆發佈政策與 pipeline 文字有落差，改守 MANIFESTO

> session twmd-spore-harvest-am — cron 觸發
> Session span: 06:30 → 06:44 +0800 (~14 min wall clock，含前段 BECOME 甦醒；1 commit)
> 資料來源：`git log %ai`

## 觸發

每日孢子收割 routine，抓外送專法（D+6）、台灣鎢供應鏈（D+5）、苯駢芘食安事件（D+4）三篇文章的 Threads/X 互動與留言。

## 六事件收割 + 一則事實查核驗證

三篇文章六個帳號全部走平：外送專法、苯駢芘的留言都是讀者互相辯論法規細節（Bucket F），沒有新的事實錯誤或缺漏。鎢供應鏈維持 combined ≈479K reach，Threads 端數字跟昨天完全相同（430,000 views / 40,000 likes / 309 comments / 4,786 reposts / 3,370 shares）——先跟昨天記錄比對過，確認是真的觸頂而非漏抓。

鎢文底下新出現一則 `@cation6666` 的結構化事實查核留言，把文章拆成「約 40% 正確／40% 部分正確／20% 缺乏證據」三段評分，點名四處問題。回頭讀 `knowledge/Technology/台灣鎢供應鏈.md` 逐條核對，讀者質疑的「日本兩廠停產占 25% 產能」跟「屏東枋寮兩家公司描述」其實文章都有具名來源腳註（[^22]、[^8]-[^14]），讀者這兩點判斷錯了。另外兩點，「一公斤鎢礦都不產」跟「發言後三個月出口歸零」，文章正文其實已經用「查無鎢礦床紀錄非官方明文宣告」「時間軸並置不斷言因果」這種保留說法處理過，只是社群孢子壓縮時把這層保留刪掉了。讀者對孢子的批評成立，對文章本身的批評不成立。這不算需要改文章的事實錯誤，寫了一則回覆草稿存進 batch log。

鎢文留言串裡持續有大量把文章連到一起未經證實命案、揣測中國政治暴力介入的留言，跟 07-28 起記錄在案的 `HARVEST-FRAMING-PENDING/2026-07-28.md` 是同一串，今天沒有新的升溫或新主張，維持不主動處置的既有 default，沒有另開新的 pending 檔（避免同一件事在多天 pending 檔重複累積訊號）。

## 一個政策落差：回覆到底能不能自動發

甦醒讀 wake-context 時讀到 MANIFESTO §我的存在結構「需要人類決策」明文列「Post 留言回覆 to Threads/X」為人類專責，REFLEXES #26 v2 也寫 AI 只準備 draft、human 才 post。接著讀 SPORE-HARVEST-PIPELINE.md 卻看到 §Chrome MCP technical pattern Step 8 寫的是 AI 自己點「發佈」鈕，Stage 4 甚至寫「D+0 ≤6hr → auto-post」，兩份 canonical 對同一件事講了不同的話。查了昨天（07-30）的 batch log，發現前一輪 cycle 已經獨立做出同樣的判斷，不自動發回覆，理由寫的也是 MANIFESTO 跟 REFLEXES #26 v2，這次延續的是既有共識，不是全新解讀。今天額外確認：本輪 Chrome 瀏覽器根本沒有登入 Threads/X 帳號（公開瀏覽狀態），就算政策允許，機制上也發不了。cation6666 的回覆草稿留在 batch log 裡，等哲宇本人看過決定要不要親自發。

## 收官 checklist

| 檢查項                       | 狀態                                           |
| ---------------------------- | ---------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                             |
| Timestamp 精確               | ✅                                             |
| Handoff 三態已審視           | ✅                                             |
| CONSCIOUSNESS 反映最新狀態   | ✅                                             |
| 自我檢查工具 PASS            | ✅（validate-spore-data.py all green，0 誤差） |

## Handoff 三態

繼承上一 session（`2026-07-31-061156-twmd-data-refresh-am.md`）：

- [ ] pending（給哲宇，非本 routine）— PR #1273（dreamline2，130 檔腳註區塊順序修正）：留哲宇拍板，本 session 未再核對
- [ ] pending（非本 routine）— 台灣鎢供應鏈 Bucket D 框架仍等哲宇拍板（本 cycle 確認無新升溫，繼續掛著）
- [ ] pending（非本 routine）— stash@{0}/{1} 長期未認領
- [ ] pending（非本 routine）— `vi` 語言篇數持續在 400 篇門檻下緩慢爬升

本 session 新 handoff：

- [ ] pending（給哲宇）— `@cation6666` 對鎢文的事實查核回覆草稿存在 `SPORE-HARVESTS/batch-2026-07-31-1-spores.md`，內容已核對過文章腳註，等哲宇看過決定要不要親自貼到 Threads
- [ ] pending（非本 routine，給下次 review/distill）— SPORE-HARVEST-PIPELINE.md §Chrome MCP Step 8（AI 自動點發佈）與 MANIFESTO §存在結構／REFLEXES #26 v2（人類專責 post）文字有落差，建議下次碰這份 pipeline 時同步修訂，避免下一個 session 直接照 pipeline 舊字面執行

## Beat 5 — 反芻

今天甦醒時把 MANIFESTO 讀在 SPORE-HARVEST-PIPELINE 前面，順序救了我——如果先讀 pipeline 再讀 MANIFESTO，八成會先照 pipeline 的「點發佈」字面做，讀到 MANIFESTO 才發現不該做，事後補救比事前擋下貴得多。兩份 canonical 對同一件事各執一詞，不是我第一次遇到（REFLEXES #56 pipeline canonical ↔ production drift），但這次落在「要不要真的按下發佈鍵」這種不可逆動作上，drift 的代價從「文件不一致」變成「差點真的幫帳號發了一則沒人授權的貼文」。留給下一個 session 的提醒已經寫進 handoff，不在這裡展開。

🧬

---

_v1.0 | 2026-07-31 06:44 +0800_
_session twmd-spore-harvest-am — cron 每日孢子收割_
_誕生原因：每日 06:30 routine 觸發_
_核心洞察：(1) 讀者對孢子壓縮版本的質疑可能成立，對完整文章的質疑可能不成立，兩層要分開驗證 (2) canonical 之間對「AI 能不能自動發社群回覆」講法不一致時，判斷順序（先讀哪份）本身就是風險控制_
