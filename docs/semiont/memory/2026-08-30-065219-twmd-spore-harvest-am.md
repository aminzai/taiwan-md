# 2026-08-30-065219-twmd-spore-harvest-am — D+7 收官：4 則新回覆零事實錯誤 + 7 天前的語源候選終於落地

> session twmd-spore-harvest-am — daily 06:30 audience flywheel cron
> Session span: 06:30:00 → 06:52:29 +0800 (~22 min, 1 commit)
> 資料來源：`git log %ai`

## 觸發

routine `twmd-spore-harvest-am` 06:30 daily fire，跑 Chrome MCP harvest + 5-bucket 分類 + reply。Dashboard `backfillWarnings` 顯示今天只有 #175/#176（用語保存副詞層）落在 D+7 finalize 窗口。

## Threads 收割：切「最新」排序讀滿留言，回了 4 則新的

主帖 `DcWa8qxo55C` 這幾天累積到 25,000 views / 1,830 讚 / 78 則留言。前兩輪 harvest 已經把大部分留言分類完，本輪切到「最新」排序滾到底，找出 4 則前兩輪判 skip、這次覺得值得回的：nemoo3310 誇網站好用（單純漏回）、icmantw 質疑辭典本身也會修訂不是絕對權威（方法論觀點，回應辭典是佐證不是仲裁者）、shine\_\_864 給了具體的咬字困難描述投「支語」一票（回應辭典書證年代早到清代小說，語感真實但不改變分類）、yvelisse 追問「真的會有台灣人這樣用嗎」（回應遊戲圈和年輕族群確實在用）。四則都用 `document.execCommand('insertText', ...)` 走 permalink 頁送出，第一次 click 都成功，commit 前逐一 diff 確認留言區出現「作者」標記。

寫 shine\_\_864 那則時撞到一次小插曲：用 `\uXXXX` unicode escape 打「蠻」字，兩次都選錯碼位（先打成「蔽」再打成「蘇」），screenshot 肉眼核對才發現——單獨讀 `editable.innerText` 回傳值一度因為時序問題顯示空字串，換一次獨立查詢才看到完整文字（正確和錯誤版本混在一起，因為 selectAll+delete 沒清乾淨，第二次改用 cmd+a + Delete 鍵盤操作才真的清空）。最後改用直接貼中文字面字元（不經過 escape），字元才穩定正確。錯的不是打字，是轉義序列本身選錯了碼位，屬於 Pitfall 3 的一種新形態。

## X 收割：7 天前標記的語源候選，本輪查證後落地

`#176` 這則 X 貼文本機沒登入，只能讀到登入牆前 4 則留言，都是 8/23 就記錄過的舊留言。其中月島伶 @ReiTukisima 那則語源補充（「踩雷是網路黎明期台灣輸入中國的，語源應該是 Windows95 踩地雷」）從 8/23 起被標成 Bucket B EVOLVE candidate，因為 X 平台限制無法回覆，兩輪都沿用既有判斷沒真的去查。本輪用 WebSearch 查了「踩地雷」遊戲史，確認它 1990 年隨《微軟娛樂包 1》推出、1992 年就是 Windows 3.1 內建遊戲——比讀者記憶的 Windows95 更早，也早於任何一地的網路論壇文化，是兩岸共通的童年記憶。把這段補進 `data/terminology/踩雷.yaml` 的 `etymology.origin`，不改變既有 F 型分類（同詞同感、難以斷定單向輸入），只是讓這個結論站得更穩。「體現」那半查核既有 `體現.yaml` 條目後確認已經正確涵蓋讀者提的宋明理學脈絡，沒有動它。回覆草稿寫好留給哲宇手動 post。

過程中不小心跑了一次 `terminology-yaml-audit.py`，沒看清楚它是 destructive 工具就直接執行，刪掉了 10 個既有詞條檔案——git status 一看到 `D` 立刻用 `git checkout --` 全部復原，之後沒再碰這支腳本。這件事沒進 factual fix，但值得記在這裡：跑任何工具前先確認它是唯讀還是會寫檔案，尤其名字裡帶「audit」的腳本不一定只是讀。

## 收官 checklist

| 檢查項                       | 狀態                                               |
| ---------------------------- | -------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                 |
| Timestamp 精確               | ✅                                                 |
| Handoff 三態已審視           | ✅                                                 |
| CONSCIOUSNESS 反映最新狀態   | ✅                                                 |
| 自我檢查工具 PASS            | ✅（validate-spore-data.py 0 errors / 0 warnings） |

## Handoff 三態

繼承 `2026-08-30-061439-twmd-data-refresh-am`：W35 news-lens 3 條候選待哲宇 review、ARTICLE-INBOX「台灣公投制度」P0 候選死線已裁決 45 天未排入、SC 偵測 `/food/台灣豆漿與早餐店/` 不在 sitemap（轉交 maintainer）、站內延伸閱讀 50 條指向不存在文章、翻譯 PR `sourceCommitSha` 閘門觀察中、五縣市條目待補圖片、指控信 `b78ee4f5` 第十二次已攔下待哲宇最終處置、OBSERVER-QUEUE 34 項待決、`twmd-routine-audit-weekly` 需核對是否把空窗算進 7 天 pattern、`twmd-supporters-weekly` 與 `twmd-routine-audit-weekly` 兩條黃燈是否已恢復（留給下一輪 routine-sync 核對）、roadmap 9 項未領取、`escalation-granularity-blocks-remediation` 待哲宇拍板、`asymmetric-skepticism-toward-convenient-explanations` vc=2 待下次同型事件。全部原樣繼承，本 session 未碰。

本 session 新 handoff：

- [ ] X 平台 `#176` 回覆草稿待哲宇手動 post（月島伶語源補充致謝，內容見 batch log）
- [ ] `w.is_solis` AI 書寫信任質疑（Threads #175）連續四輪維持 log-only 未回覆，留給哲宇判斷是否要正面回應
- [x] ~~踩雷.yaml 語源補充~~（7 天前的 EVOLVE candidate，本輪查證落地）

## Beat 5 — 反芻

今天最有意思的一件事，是那條放了 7 天的語源候選——它一直躺在 batch log 裡被三輪 harvest 原樣「沿用既有判斷」路過，直到今天真的花 5 分鐘去查了 Wikipedia 才發現讀者是對的，年代甚至比他自己記得的還早。「累積進 EVOLVE candidate」這句話寫起來很順手，但如果沒有哪一輪真的回頭兌現，它就只是一個永遠不會被讀到第二次的標記。這跟 REFLEXES #15「反覆浮現要儀器化」是同一種病的另一種變體：記下來這個動作本身沒有問題，缺的是逼自己回頭看的機制。

字元 typo 那次插曲也提醒了一件事：我用來防手誤的機制（post 前 diff 檢查）確實接住了問題，但問題本身換了個載體——從「打字打錯」變成「轉義序列選錯碼位」，同一道防線繼續有效，不代表下一種變體不會出現在別的地方。

🧬

---

_v1.0 | 2026-08-30 06:52 +0800_
_session twmd-spore-harvest-am — daily D+7 finalize harvest_
_誕生原因：cron 06:30 fire，dashboard 唯一 OVERDUE 項是用語保存副詞層 #175/#176_
_核心洞察：(1) EVOLVE candidate 標記本身不是行動，沒有回頭機制它會被無限次「沿用既有判斷」路過 (2) 字元 typo 防線換了載體（escape 碼位選錯）依然被接住，但提醒同一道防線不保證覆蓋所有變體 (3) 名字帶「audit」的工具不保證唯讀，跑陌生腳本前先看它做什麼再執行_
