---
spores: '#175, #176'
harvest_date: '2026-08-30 07:00'
harvest_window_day: 'D+7'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am，這兩則落在 D+7 finalize 窗口，harvestStatus 唯一 OVERDUE 項'
triggered_by: 'cron'
reply_count: '約 21 則讀到（Threads #175「最新」排序讀出 21 則含本輪 4 則新回覆；X #176 登入牆前可讀 4 則，皆為既有留言）'
---

# 2026-08-30 harvest — 用語保存副詞層 D+7 finalize

Login-state probe：PASS（@taiwandotmd 個人檔案顯示「編輯個人檔案」按鈕，帳號已登入）。

Dashboard `backfillWarnings` 顯示今天僅 #175/#176（用語保存副詞層，D+7）OVERDUE。harvest 完成後 dashboard-spores.json 重生為 0 OVERDUE。

## #175 Threads（用語保存副詞層，D+7）

- URL: https://www.threads.com/@taiwandotmd/post/DcWa8qxo55C（1/2 主帖；2/2 CTA 帖 `DcWa9mnI4vJ` 瀏覽數 3,961 為獨立子貼文計數，不代表主帖總覽）
- Metrics（harvest snapshot）：views 25,000（2.5 萬）/ likes 1,830 / comments 82（本輪 4 則新回覆後）/ reposts 240 / shares 175

### 讀取方式

「熱門」切「最新」排序 + 完整滾動至留言列表底部，一次讀出 21 則留言（含本輪新增前的 78 則舊留言 + 4 則新回覆自己）。前六輪（8/28、8/29）harvest 已讀過的留言本輪不重複列出，僅列本輪新分類與新回覆。

### 本輪處置

| Author                                                                                                               | 留言原文（節錄）                                                      | Bucket                        | 處置                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| nemoo3310                                                                                                            | 這個網站也太棒了吧，終於多了教育部辭典之外的參考網站，留友存          | E                             | **本輪已回覆**（見下）— 前兩輪列為 optional 未回覆，本輪補上                                                            |
| icmantw                                                                                                              | 教育部編的也是分版號的，不是一定正確⋯它的資料隨著時代其實也是會被洗的 | F（方法論質疑）               | **本輪已回覆**（見下）— 前兩輪判 skip，本輪認為具體到值得回應                                                           |
| shine\_\_864                                                                                                         | 還沒有「挺」時我就很討厭「蠻」字⋯所以這題我要投支語一票               | F（語感投票，附具體咬字論證） | **本輪已回覆**（見下）— 讀者給了具體材料（咬字困難的語感描述），依 pipeline 「optional reply 如果 reader 主張具體」處理 |
| yvelisse.\_.1122（第二則）                                                                                           | 真的會有台灣人這樣用嗎……                                              | F（對上輪「邪修」回覆的追問） | **本輪已回覆**（見下）— 追問具體，補充邪修使用場景                                                                      |
| lochichi77（跟進）                                                                                                   | 感謝回覆🥹                                                            | E（迴圈已閉合）               | skip，不需再回覆                                                                                                        |
| captaingeoffery / kkbox1352.0 / samxd961101 / cuemoon5 / xinyubai395 / asunoig2019 / bb8_skywalker / jayfeather_1005 | （單句心得／用字習慣分享）                                            | E/F/G                         | skip，optional 或 ignore，同前兩輪判斷未變                                                                              |

### 回覆執行（本輪 4 則，Chrome MCP execCommand insertText via 各留言 permalink 頁）

| Author                     | 回覆內容                                                                                                                   | Post-ship verify                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nemoo3310                  | 謝謝你這樣說，收藏起來很有用——詞庫還在每天更新，歡迎常回來查 🧬                                                            | 第一次 click 成功（container count 前後對照 + comment 78→79 確認）                                                                                      |
| icmantw                    | 對，辭典本身也在修訂，不是永遠正確的裁判——我們是拿目前版本當佐證，真正判準還是看台灣人實際怎麼講、怎麼寫 🧬                | 第一次 click 成功（comment 79→80）                                                                                                                      |
| shine\_\_864               | 這個語感很真實，我也懂——不過辭典裡蠻/滿都有台灣自己的例句和書證，年代早到清代小說，所以歸類上不算支語 🧬                   | **草稿字元 typo 兩次**（`蔽`/`蘇` 誤植取代「蠻」，unicode escape 打錯）— post 前 diff 攔下，clear + 重打確認字元正確後才送出（comment 80→82，含下一則） |
| yvelisse.\_.1122（第二則） | 會，尤其是遊戲圈和年輕族群——2025 年後從修真小說梗轉義成「用偏門方法但意外有效」的說法，你可以留意看看身邊有沒有人這樣講 🧬 | 第一次 click 成功                                                                                                                                       |

四則皆最終成功、無 duplicate（per Pitfall 6 hard rule）。shine\_\_864 那則觸發 Pitfall 3（個別字元 typo）——`蘇`（蘇）誤用做「蠻」的 unicode escape，post 前 diff 檢查（`editable.innerText` 對照原文）攔下兩次錯誤版本，改用直接貼中文字面文字（不用 `\uXXXX` 跳脫）後字元才正確，第三次才送出。

## #176 X（用語保存副詞層，D+7）

- URL: https://x.com/taiwandotmd/status/2091212353874678264
- Metrics: views 25,000（2.5 萬）/ replies 21 / reposts 120 / likes 630 / bookmarks 109（與 8/23、8/28、8/29 三輪記錄完全相同，本輪無新增互動）
- 本機未登入 X，僅能讀到登入牆前 4 則留言（`article` selector 取得，`cellInnerDiv` selector 抓不到——確認是登入態限制非工具故障），皆為 8/23 batch log 已記錄過的舊留言（YanaW20 / 月島伶 @ReiTukisima / 오ーエンを応援する会 @yu_and_rw）。

### 本輪新動作：月島伶語源補充查證後落地（累積 7 天的 EVOLVE candidate 本輪處置）

8/23 batch log 把月島伶 @ReiTukisima 的語源補充（「踩雷是網路黎明期台灣輸入中國的，語源應該是Windows95踩地雷」「體現是出自宋明佛教、理學」）記為 Bucket B EVOLVE candidate，因 X 平台限制未回覆也未查證落地，此後兩輪（8/28、8/29）沿用既有判斷未再處理。

本輪 WebSearch 查證「踩地雷」遊戲史（[微軟踩地雷 - 維基百科](https://zh.wikipedia.org/zh-tw/%E5%BE%AE%E8%BB%9F%E8%B8%A9%E5%9C%B0%E9%9B%B7)）：遊戲 1990 年隨《微軟娛樂包 1》推出、1992 年成為 Windows 3.1 內建遊戲（讀者記成 Windows95，實際更早），確認早於任何一地的網路論壇文化，是兩岸共通的童年記憶。已將此語源脈絡補進 `data/terminology/踩雷.yaml` `etymology.origin`，不改變既有 F 型（同詞同感，難以斷定單向輸入）分類，只是補上更早的共通源頭，讓「難以斷定單向輸入」這個結論站得更穩。

「體現」部分：查核既有 `data/terminology/體現.yaml` 條目，已正確記載「體現」是教育部辭典有據的台灣本有詞、非中國新造，只是頻率與搭配上兩地不同——讀者的宋明理學脈絡是對既有正確結論的補充材料，不構成需要修正的事實錯誤，未編輯此檔。

X 平台無法自動回覆（per pipeline §Threads-only 操作鐵律），本輪處置停在條目修正，回覆需哲宇手動 post，draft 如下：

> 你補的兩個字源都對——踩地雷遊戲的年代確實比 PTT 美食版更早（1992 年 Windows 3.1 內建），已經把這段補進詞條；體現在辭典本來就有，你補的宋明理學脈絡很扎實，謝謝 🧬

YanaW20「這資料庫會變成教中國ai如何假裝台灣人的資料庫」一則，三輪（8/23 起）皆判為 Bucket F（延伸擔憂，非文章事實爭議），本輪維持該分類，log only，未新增處置。

## 本輪摘要

- 2 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md），dashboard-spores.json 重生後 OVERDUE 歸零
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏／疑問，含語源補充）：1 條落地——月島伶「踩雷」語源查證後補進 `踩雷.yaml`（7 天前已標記的 EVOLVE candidate 本輪處置完成）；「體現」查核後確認既有條目已正確涵蓋，未修改
- Bucket E/F（可回覆的具體材料）：4 條，本輪全數回覆（nemoo3310 / icmantw / shine\_\_864 / yvelisse.\_.1122 追問）
- Bucket D-adjacent（AI 書寫質疑 w.is_solis / 資料庫擔憂 YanaW20）：0 條新增，沿用既有 log-only 判斷
- Reply shipped：4（Threads，全數第一次 click 成功；shine\_\_864 那則有 2 次字元 typo 在送出前被 diff 攔下，未造成 duplicate 或錯字上線）
- Factual fix：1（`踩雷.yaml` 語源補充，非文章 prose 修正，是詞庫 etymology 欄位深化）
- 結構性發現：字元 typo（Pitfall 3）這次不是我手寫打字錯，是用 `\uXXXX` unicode escape 轉義中文字元時選錯碼位（`蘇` 是「蘇」不是「蠻」）——用工具傳遞中文字串時，直接寫字面字元比 escape 序列可靠，escape 序列在多字元組合時人工核對碼位容易出錯且難以肉眼發現（送出前 screenshot 才看得出來，純讀 `.innerText` 回傳值反而因為時序問題一度誤判為空）
