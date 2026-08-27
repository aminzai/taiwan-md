---
spores: '#172, #173, #174, #175, #176'
harvest_date: '2026-08-23 07:20'
harvest_window_day: 'mixed (D+0 for #175/#176, D+5 for #172/#173/#174)'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am，budget-總預算十年 三平台第四輪 + 用語保存副詞層 首次 harvest'
triggered_by: 'cron'
reply_count: '9 則留言可讀（Threads #175：5 則讀者留言，本輪全數新回覆 4 則＋1 typo 修正重發；Threads #172：1 則未回覆的書籤型留言 skip；X #176：2 則讀者留言可讀但無法回覆；X #173：登入牆延續，僅 metrics 可讀；Facebook #174：0 讀者留言）'
---

# 2026-08-23 harvest — budget-總預算十年 第四輪 + 用語保存副詞層 首次收割

本輪涵蓋兩組孢子：8/18 發佈的「總預算十年」特別企劃（#172/#173/#174，D+5）第四次 harvest，以及 8/23 凌晨新發佈的「用語保存副詞層」（#175/#176，D+0）首次 harvest。

## #175 Threads（用語保存副詞層，D+0）

- URL: https://www.threads.com/@taiwandotmd/post/DcWa8qxo55C（主帖）+ https://www.threads.com/@taiwandotmd/post/DcWa9mnI4vJ（2/2 CTA 帖）
- Login-state probe：PASS（個人檔案／編輯個人檔案／追蹤中可見，帳號已登入）
- Metrics（harvest 後）: views 2,593 / likes 226 / comments 11 / reposts 35 / shares 18（主帖）；2/2 帖 likes 6 / reposts 1 / 尚無回覆

### 留言逐字 + 分桶

| Author          | 留言原文                                               | Bucket                                            | 處置                                                                             |
| --------------- | ------------------------------------------------------ | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| protective113   | 滿蠻混用呀，怎麼沒有？                                 | B（缺漏／疑問）                                   | **本輪已回覆**：確認「挺」條目 蠻／滿 兩個寫法皆已收錄，附連結（見下）           |
| bdoalongbong2\_ | 挺好，是雞共國用語！！😘😘                             | F（無新材料的斷言，觸及 §自主權邊界政治敏感相鄰） | skip，不回覆——條目本文已用「查證分歧誠信標註」段落正面處理過同一質疑，非漏掉未答 |
| v.beibei        | 很少聽到別人說「蠻」，我自己會這樣講，原來我不怪是很台 | E（共鳴）                                         | **本輪已回覆**（見下）                                                           |
| mon.\_.bee      | 我現在才知道「蠻」、「滿」相通但讀音不同               | E（共鳴＋知識點）                                 | **本輪已回覆**（見下，含一次 typo 修正）                                         |
| cludandsky      | 我一直以來都是用「滿」😎😎😎                           | E（共鳴）                                         | **本輪已回覆**（見下）                                                           |

**條目查證**：先讀 `taiwan.md/terminology/挺/` 頁面確認內容——「台灣完整說法：蠻 / 滿」已同時列出兩個字，且頁面本身有「⚠️ 查證分歧誠信標註」段落正面回應「支語警察」式質疑（引用 Threads 用語策展者 @thiankiu.to 的反方立場）。protective113 的疑問答案已在條目裡，回覆時附連結即可；bdoalongbong2\_ 的斷言條目也已處理過，不需要新增修文或防衛性回覆。

### Bucket E/B 回覆執行（本輪四則，Chrome MCP execCommand insertText via 各留言 permalink 頁）

| Author        | 回覆內容                                                                                                         |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| protective113 | 有喔，滿跟蠻兩個都收了，這條寫的是「挺」的完整台灣說法是蠻／滿都算，你可以看 taiwan.md/terminology/%E6%8C%BA/ 🧬 |
| v.beibei      | 對，蠻／滿是台灣一直都在用的講法，你這樣講超台的 🧬                                                              |
| mon.\_.bee    | 對，這個小細節蠻多人不知道，字典都有收只是大家不會去查 🧬                                                        |
| cludandsky    | 對，滿也是台灣本來就在用的說法，你這樣講很到位 🧬                                                                |

**Pitfall 3 命中一次（我端 unicode 誤算）**：mon.\_.bee 第一次送出的回覆把「蠻」誤寫成形似字「蓸」（U+84F8 非 U+883B），post-ship verify 用 codePointAt 逐字元核對才發現（肉眼看小字級時兩者難以分辨）。處置：先試「編輯」功能修正文字，但 Lexical 編輯器的 `document.execCommand('selectAll'/'delete')` 對已渲染內容無效（多次呼叫只會在原文字後方疊加而非取代），改用整則刪除＋用 `String.fromCodePoint(0x883b)` 明確指定正確碼位重新回覆一次，二次 post-ship verify 逐字元 codePointAt 核對通過。其餘三則回覆首次送出即逐字核對正確。

Post-ship verify（per Pitfall 6 hard rule，`[data-pressable-container]` count diff）：四則回覆皆 after > before 一次成功；mon.\_.bee 額外歷經 1 次刪除 + 1 次重發，非 Pitfall 6 定義的「同一動作重試」而是「發現內容錯誤後主動修正」，不計入 retry 次數。

## #176 X（用語保存副詞層，D+0）

- URL: https://x.com/taiwandotmd/status/2091212353874678264
- Metrics: views 2,536 / replies 3 / reposts 18 / likes 106 / bookmarks 16
- 本則 X 貼文的回覆內容**未完全被登入牆擋住**（與 #173 budget 貼文不同），可讀到 2 則（第 3 則仍需登入）：

| Author              | 留言原文（節錄）                                                                                                                                                            | Bucket                             | 處置                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------- |
| 月島伶 @ReiTukisima | 「挺、肯定、行吧都是１９４５前就在用的，不是嚴格定義支語⋯甚好→挺好→（很好）→滿好→蠻好⋯踩雷是網路黎明期台灣輸入中國的，語源應該是Windows95踩地雷⋯體現是出自宋明佛教、理學⋯」 | B（entity/context 補充，語源細節） | 累積進 EVOLVE candidate（詞條補語源）；**X 不支援 reply via Chrome MCP，無法回覆** |
| Jadis @jadisy       | 「我一直在想，有沒有這樣的網頁，支語字典，支語辭典，爹味爺味辭典。然後餵給AI，叫他自動屏蔽這些來源。」                                                                      | F（功能建議，實際上該功能已存在）  | log only；**X 不支援 reply via Chrome MCP，無法回覆**                              |

**留言內容記錄但不處置**：per pipeline §Threads-only 操作鐵律，X reply 必須人工手動 post，本輪僅讀取歸檔。月島伶提供的語源細節（踩雷源自 Windows95 踩地雷、體現出自宋明佛教理學等）具備領域知識含量，值得未來詞庫補語源欄位時參考，但不在本輪自動處置範圍。

## #172 Threads（budget-總預算十年，D+5）

- URL: https://www.threads.com/@taiwandotmd/post/DcKsP3Co9jm
- Metrics: views 4,839 / likes 304 / comments 15 / reposts 67 / shares 53
- 用「未回覆」篩選確認：僅 zannaex「留己看」（書籤型，非互動內容）仍未回覆，沿用歷輪判斷 skip；alden.0202、chipher、locadia641231 三則既有回覆均在，無新增讀者留言。

## #173 X（budget-總預算十年，D+5）

- URL: https://x.com/taiwandotmd/status/2089561276938666168
- Metrics: views ~10,000（header「1萬」K-rounded）/ replies 5 / reposts 201 / likes 599 / bookmarks 90
- X 登入牆連續命中（延續第 7 天）：本則 5 條 reply 內容仍完全被登入牆擋住，僅 header metrics 可讀。

## #174 Facebook（budget-總預算十年，D+5）

- URL: https://www.facebook.com/61576525376323/posts/pfbid02iQux9KoUcNtxZHLVdFQ9R2oFXTH8X3EQmauC8XJ3CoUacveZVPKFXoqphTxwbzYwl
- Metrics: likes 1 / comments 1 / shares 1（與前幾輪完全持平）
- 唯一一則留言仍是作者本人置頂補連結，非讀者留言，0 條讀者互動需分桶。

## 本輪摘要

- 5 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏／疑問）：2 條（protective113 已回覆確認條目已收錄；月島伶語源補充累積進 EVOLVE candidate，X 平台限制無法回覆）
- Bucket D（立場質疑）：0 條（bdoalongbong2\_「雞共國用語」斷言判為 F 非 D，因條目本身已在正文正面處理過同一質疑，非未答的立場爭議）
- Bucket E（正面互動）：4 條新回覆（v.beibei / mon.\_.bee / cludandsky / protective113 合併回覆），皆為 #175 首次 harvest
- Bucket F/G：2 條（zannaex 書籤型延續 skip；Jadis 功能建議 log only，X 平台限制無法回覆）
- Reply shipped：4（Threads，1 次額外刪除+修正非 retry）
- Factual fix：0
- 殘留訊號：X 登入牆連續第 7 天（#173），與此同時 #176 該則 X 貼文的回覆內容卻能局部讀到——同帳號同工具在不同貼文上登入牆的觸發不一致，供未來 harvest 遇到「這則能讀那則不能讀」時先當作正常波動，不必假設工具故障；月島伶語源補充已記錄供詞庫未來補語源欄位參考。
