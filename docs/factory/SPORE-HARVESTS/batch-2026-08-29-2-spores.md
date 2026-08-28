---
spores: '#175, #176'
harvest_date: '2026-08-29 07:10'
harvest_window_day: 'D+6'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am，僅這兩則落在 D+1-D+7 收割窗口內'
triggered_by: 'cron'
reply_count: '約 30 則可讀（Threads #175 排序切換「最新」後補讀出 13 則先前「熱門」排序漏掉的低互動留言；X #176 局部可讀 3 則，皆為既有留言）'
---

# 2026-08-29 harvest — 用語保存副詞層 排序盲區補漏輪

Login-state probe：PASS（@taiwandotmd 個人檔案顯示「編輯個人檔案」按鈕，帳號已登入）。

Dashboard `harvestStatus` 顯示今天只有 #175/#176（用語保存副詞層，D+6）落在 D+1-D+7 窗口內，其餘孢子均已超出或尚未到窗口。

## #175 Threads（用語保存副詞層，D+6）

- 實際主帖：https://www.threads.com/@taiwandotmd/post/DcWa8qxo55C（canonical 記錄的 2/2 CTA 帖 `DcWa9mnI4vJ` 進入時「串文」header 顯示的瀏覽數是暫態未載入完整值，沿用前輪判斷以直接開主帖為準）
- Metrics（harvest snapshot）：views 25,000（2.5 萬）/ likes 1,830 / comments 76（回覆本輪後）/ reposts 240 / shares 175

### 本輪發現：「熱門」排序系統性漏掉低互動留言

昨天（8/28）的 harvest 用「熱門」排序讀了約 14 則留言就到登入牆前緣，未曾切換排序。今天把排序切成「最新」重新掃過一輪，發現至少 13 則先前完全沒被讀到、沒有讚數或只有 1 讚的留言——「熱門」排序對這些留言的能見度趨近於零，代表過去每一輪 harvest 都可能系統性漏掉這類尾端留言（跟 REFLEXES #82 proxy signal antipattern 同型：用「熱門」這個排序代理「留言全貌」，量到的是排序演算法選中的子集，不是全部留言）。

補讀到的留言（依「最新」排序，皆為 5 天前留言，此前未出現在任何 batch log）：

| Author           | 留言原文（節錄）                                                                       | Bucket                                    | 處置                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------- |
| captaingeoffery  | 我用「滿」已經30多年了，我滿喜歡這個用法🫶推薦給2010年後出生的台灣人                   | E                                         | skip，optional，未回覆                                                                   |
| kkbox1352.0      | 我一直是用蠻好的，沒用挺好的                                                           | F                                         | skip，optional，未回覆                                                                   |
| icmantw          | 教育部編的也是分版號的，不是一定正確⋯它的資料隨著時代其實也是會被洗的                  | F（方法論質疑，跟昨輪 sophie990329 同型） | skip，優先級同昨輪判斷                                                                   |
| cuemoon5         | 我個人用「蠻」比較多，但「挺」一直以來也都會使用到，只是沒有蠻用得頻繁                 | F                                         | skip，optional，未回覆                                                                   |
| yvelisse.\_.1122 | 邪修是仙俠小說的詞吧                                                                   | B（詞源確認）                             | **本輪已回覆**（見下）— 詞庫 `邪修.yaml` 已完整記載此脈絡，讀者觀察與現有詞條一致        |
| liasnic          | 想說一個，乾貨。不要再整天乾貨滿滿，是有多乾？（1 讚）                                 | B（新詞建議）                             | **本輪已回覆**（見下）— 查證詞庫 `乾貨.yaml` 已收錄（2026-03-30 新增），讀者不知道已存在 |
| asunoig2019      | 因為我打字時會不知道要選滿還是蠻，所以我就選挺                                         | E                                         | skip，optional，未回覆                                                                   |
| bb8_skywalker    | 挺台灣～                                                                               | E                                         | skip，optional，未回覆                                                                   |
| lochichi77       | @taiwandotmd 我跟兒子提個意見時，他竟然回我：「行！」⋯希望這個「行」也能被收錄（1 讚） | B（新詞建議）                             | **本輪已回覆**（見下）— 查證詞庫 `行吧.yaml` 已完整記載「行」單獨作為應答詞的觀察        |
| samxd961101      | 滿                                                                                     | F                                         | skip，optional，未回覆                                                                   |
| xinyubai395      | 就又老又土為什麼要配合你                                                               | G（敵意/離題）                            | ignore，不回覆                                                                           |
| nemoo3310        | 這個網站也太棒了吧，終於多了教育部辭典之外的參考網站，留友存                           | E                                         | skip，optional，未回覆                                                                   |
| jayfeather_1005  | 從小就是用滿！                                                                         | E                                         | skip，optional，未回覆                                                                   |

昨輪（8/28）已回覆的 guanlaoban987、yunc_bbb 兩則沿用不重複處理；w.is_solis 的 AI 書寫信任質疑（Bucket D-adjacent）沿用昨輪判斷，繼續留給哲宇 review，本輪未動。

### Bucket B 回覆執行（本輪三則，Chrome MCP execCommand insertText via 各留言 permalink 頁）

| Author           | 回覆內容                                                                                                                              | Post-ship verify                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| lochichi77       | 「行」辭典本來就有收（同意、可以的意思），詞庫「行吧」那條已經記了——真正在變的是它當應答語氣詞的使用頻率，不是這個字本身。謝謝補充 🧬 | 第一次 click 即成功（container 2→3，comment 73→74）                                                                   |
| liasnic          | 「乾貨」詞庫已經收了，中國網路用語指有料的分享，台灣通常說「實用內容」「有料的內容」。謝謝提醒 🧬                                     | 第一次 click 未觸發（container 2→2，comment 74→74，genuine fail），**retry 1 次**成功（container 2→3，comment 74→75） |
| yvelisse.\_.1122 | 對，邪修本來就是修真小說的設定用語，2025 年被挖用轉義成「離譜但高效」的生活方法，詞庫裡有寫完整脈絡。謝謝 🧬                          | 第一次 click 未觸發（container 2→2，comment 75→75，genuine fail），**retry 1 次**成功（container 2→3，comment 75→76） |

三則皆最終成功、無 duplicate（per Pitfall 6 hard rule：max 1 retry，兩次 retry 都在單次失敗後立即用同一顆送出鈕重點一次，未觸發第二次重試）。

## #176 X（用語保存副詞層，D+6）

- URL: https://x.com/taiwandotmd/status/2091212353874678264
- Metrics: views 2.4 萬 / replies 21 / reposts 120 / likes 630 / bookmarks 110（與 8/23、8/28 兩輪記錄完全相同，本輪無新增互動）
- 本機未登入 X，僅能讀到登入牆前 3 則留言，皆為 8/23 batch log 已記錄過的舊留言（YanaW20 / 月島伶 @ReiTukisima / 오ーエンを応援する会 @yu_and_rw），本輪無新增，沿用既有判斷。

## 本輪摘要

- 2 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏／疑問）：3 條，本輪全數回覆（lochichi77「行」/ liasnic「乾貨」/ yvelisse.\_.1122「邪修」）——三則讀者建議查證後發現詞庫其實都**已經收錄**，回覆重點是讓讀者知道已存在的紀錄，而非承諾新增
- Bucket D-adjacent（AI 書寫質疑）：0 條新增（w.is_solis 沿用昨輪 handoff，未處置）
- Bucket E（正面互動）：7 條（captaingeoffery / asunoig2019 / bb8_skywalker / samxd961101（偏 F 但語氣近共鳴）/ nemoo3310 / jayfeather_1005 等），皆無新事實內容，optional 不逐一回覆
- Bucket F：4 條（kkbox1352.0 / icmantw / cuemoon5 / samxd961101），無新材料，optional 不回覆
- Bucket G：1 條（xinyubai395，敵意離題，ignore）
- Reply shipped：3（Threads，lochichi77 / liasnic / yvelisse.\_.1122，後兩則各 1 次 retry，皆在 hard rule 範圍內無 duplicate）
- Factual fix：0
- 結構性發現：「熱門」排序讀留言會系統性漏掉低互動尾端留言（本輪切「最新」排序才補讀出 13 則），過去每一輪 harvest 可能都有同樣的盲區——這是排序代理「完整留言」的 proxy signal 問題，建議未來 harvest 固定用「最新」排序或兩種排序都掃一次，而非只用「熱門」讀到登入牆前緣就停
