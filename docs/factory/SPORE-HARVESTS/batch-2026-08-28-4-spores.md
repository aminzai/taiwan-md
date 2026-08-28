---
spores: '#172, #173, #175, #176'
harvest_date: '2026-08-28 06:44'
harvest_window_day: 'mixed (D+10 for #172/#173, D+5 for #175/#176)'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am，四天空窗（8/24-8/27 mouhouse 排程器停擺）後首次恢復執行，budget-總預算十年 追蹤輪 + 用語保存副詞層 補上五天累積留言'
triggered_by: 'cron'
reply_count: '約 20 則留言可讀（Threads #172：7 則既有留言全數已回覆過，0 新增；Threads #175：約 14 則留言，多數在 4-5 天前已由某次 session 回覆過，本輪新回覆 2 則遺漏未答的；X #173：登入牆持續，僅 metrics 可讀；X #176：3 則可讀，皆為既有留言，0 新增）'
---

# 2026-08-28 harvest — budget-總預算十年 追蹤輪 + 用語保存副詞層 補漏輪

本輪是四天執行空窗（`twmd-embeddings-nightly` / `twmd-routine-sync` / `twmd-data-refresh-am` 三條 routine 同日皆確認本機 8/24-8/27 無任何觸發痕跡）後，`twmd-spore-harvest-am` 首次恢復執行。dashboard `harvestStatus` 顯示 #175/#176 自 8/23 發佈當天 harvest 一次後就沒有再被收割過，但實際上這兩則的留言區在 8/24 已經有一輪大量回覆（多數留言下方已掛 `taiwandotmd · 作者` 回覆），推測是空窗期間某次未經過 routine 記錄流程的 session 手動處理過，只是沒有寫進 batch log 也沒有更新 dashboard harvestCount。本輪的任務因此變成「確認先前已回覆的都還在、補上真正遺漏的」，而不是從零開始分桶。

## #172 Threads（budget-總預算十年，D+10）

- URL: https://www.threads.com/@taiwandotmd/post/DcKsP3Co9jm
- Metrics: views 4,989 / likes 309 / comments 15 / reposts 67 / shares 53
- 逐一核對：chipher、locadia641231、hyhct943、rosie_forosie 四則留言皆已有 `作者 2026-08-20` 回覆；zannaex「留己看」（書籤型，非互動內容）沿用歷輪判斷 skip。無新增讀者留言，0 條需處置。

## #173 X（budget-總預算十年，D+10）

- URL: https://x.com/taiwandotmd/status/2089561276938666168
- Metrics: views ~10,000（header「1萬」K-rounded）/ replies 5 / reposts 200 / likes 599 / bookmarks 90
- 本機未登入 X（`Log in or sign up for X` 牆），連 header metrics 之外的留言內容完全讀不到，僅能記錄 metrics。與 #176 同帳號同工具在不同貼文上的登入牆觸發不一致（#176 本輪可局部讀取），沿用 8/23 batch log 已記錄的判斷：這是正常波動不是工具故障。

## #175 Threads（用語保存副詞層，D+5）

- URL（canonical，dashboard 記錄）: https://www.threads.com/@taiwandotmd/post/DcWa9mnI4vJ（2/2 CTA 帖）
- 實際主帖: https://www.threads.com/@taiwandotmd/post/DcWa8qxo55C（1/2）
- Login-state probe：PASS（@taiwandotmd 個人檔案可見編輯個人檔案按鈕，帳號已登入）
- Metrics（主帖，harvest snapshot 時）: views 20,000（2 萬，直接開主帖頁時頭部顯示；透過 2/2 帖進入時「串文」header 顯示的 3,956 是尚未載入完整串文的暫態數字，以直接開主帖的 2 萬為準）/ likes 1,830 / comments 70 / reposts 240 / shares 175

### 留言逐字 + 分桶（依熱門排序，讀到登入牆前約 14 則）

| Author          | 留言原文（節錄）                                                                                                                                                                                                                                                                                                            | Bucket                                                                                          | 處置                                                                                                                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| v.beibei        | 很少聽到別人說「蠻」，我自己會這樣講，原來我不怪是很台                                                                                                                                                                                                                                                                      | E（共鳴）                                                                                       | 已有 `作者` 回覆（4 天前），沿用                                                                                                                                                           |
| hsuanyi_liu     | 雖然兩字通用，但滿本身有多、非常的意思，蠻這個字本身很難導出上述意思⋯個人盡量避免用蠻                                                                                                                                                                                                                                       | F（語感偏好，非事實爭議）                                                                       | skip，optional，未回覆                                                                                                                                                                     |
| john02130316    | 反了吧，蠻才能表達八成，滿的十分反而卡住了                                                                                                                                                                                                                                                                                  | F（解讀分歧）                                                                                   | skip，optional，未回覆                                                                                                                                                                     |
| mon.\_.bee      | 我現在才知道「蠻」、「滿」相通但讀音不同                                                                                                                                                                                                                                                                                    | E（共鳴＋知識點）                                                                               | 已有 `作者` 回覆（4 天前），沿用                                                                                                                                                           |
| syuanantan      | 我覺得蠻是積非成是。用字義來看，滿才對                                                                                                                                                                                                                                                                                      | F（解讀分歧）                                                                                   | skip，optional，未回覆                                                                                                                                                                     |
| guanlaoban987   | 挺在文章中是會看到沒錯，但是「挺」的確是在抖音等「視頻」氾濫後才被年輕人口語上使用⋯積非成是的太多了⋯但至少是台灣自己的積非成是                                                                                                                                                                                              | B（entity/context 補充，短影音世代頻率變化的新角度）                                            | **本輪已回覆**（見下）                                                                                                                                                                     |
| yunc_bbb        | 想知道特別好、特別喜歡的用法怎麼改比較好？                                                                                                                                                                                                                                                                                  | B（直接提問，詞庫缺口）                                                                         | **本輪已回覆**（見下）；已核對詞庫（`data/terminology/`）確認「特別」尚未收錄，列入下一輪查證候選                                                                                          |
| cerul.noptill   | 我從小用的就是「蠻」、「滿」⋯二十年前到中国工作時知道他們是用「挺」來形容⋯中国影視 短影音也影響了台灣的用語文化，我們這幾一代人只是老 但還沒死吶                                                                                                                                                                            | E（共鳴＋個人經驗，跟文章立意一致）                                                             | skip，optional，未回覆（無新事實需處置）                                                                                                                                                   |
| ssu.cooklab     | 天啦好讚推推                                                                                                                                                                                                                                                                                                                | E（純共鳴，短）                                                                                 | skip，optional，未回覆                                                                                                                                                                     |
| 1yiyi_0707      | 我個人很常用蠻好聽，沒用過滿好⋯蠻好是超級好，挺好是還不錯這樣w                                                                                                                                                                                                                                                              | F（語感細分，個人用法）                                                                         | skip，optional，未回覆                                                                                                                                                                     |
| w.is_solis      | 我大概十幾年前還是國小生時，就習慣用「挺」⋯「蠻/滿」在生活上是更常見一點，但我認為沒到「頻率上遠遠差距」的地步。另外⋯你都做個語言相關網站了，就不要用AI生成的文案了吧⋯否則你做的到底是台灣人的用語，還是AI的用語啊。語感這麼細微的東西，如果連人類和機器人的使用方式你都區分不明白⋯那你哪來的說服力說你要區分兩岸的使用方式 | F（頻率解讀分歧）疊加 AI 書寫質疑（dimension 5，per SPORE-HARVEST-PIPELINE Step 2「人類判斷」） | **不自動回覆**，寫入本輪 handoff 供哲宇 review — 這則同時質疑內容是否為 AI 生成、以及 AI 是否有資格做語感分辨，屬於對 AI 本身信任的挑戰而非單純事實爭議，落在 REFLEXES #26 human-only 邊界 |
| pinky_kirara    | 我一直都用蠻好耶⋯滿好感覺就滿了變成完美了（個人感覺                                                                                                                                                                                                                                                                         | E（共鳴）                                                                                       | skip，optional，未回覆                                                                                                                                                                     |
| cindywu1981     | 原來「蠻好的」可代替「滿好的」，我之前還一直覺得是寫錯字                                                                                                                                                                                                                                                                    | E（共鳴＋知識點）                                                                               | skip，optional，未回覆                                                                                                                                                                     |
| bdoalongbong2\_ | 挺好，是雞共國用語！！😡😡                                                                                                                                                                                                                                                                                                  | F（與文章結論相反的斷言，未附新來源）                                                           | skip——文章本文已用教育部辭典＋清代小說書證處理過「挺」的合法性，非漏答的爭議                                                                                                               |
| sophie990329    | 但字典誰編的？誰有權利加入那個詞句？                                                                                                                                                                                                                                                                                        | F（方法論提問，非特定事實錯誤）                                                                 | skip，optional，未回覆——這條問的是詞庫編審機制本身，回覆需要引用 EDITORIAL/詞庫方法論說明，超出單則回覆範圍，留待下輪或觀察者決定要不要開一篇說明                                          |
| oliviachao1979  | 我以前在國語日報上作文課（40年前），老師（吳美川老師）是說「滿」，而不是「蠻」。兩者字義差很多，從不會用上「蠻」這個字                                                                                                                                                                                                      | E/F（個人歷史經驗，補充教育脈絡）                                                               | skip，optional，未回覆                                                                                                                                                                     |
| shine\_\_864    | 還沒有「挺」時我就很討厭「蠻」字⋯現在用「挺」字真的比較舒服所以這題我要投支語一票                                                                                                                                                                                                                                           | F（解讀分歧，個人立場）                                                                         | skip，optional，未回覆                                                                                                                                                                     |

### Bucket B 回覆執行（本輪兩則，Chrome MCP execCommand insertText via 各留言 permalink 頁）

| Author        | 回覆內容                                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| guanlaoban987 | 你補的這個角度有意思——「挺」字典裡本來就有，但頻率被短影音世代的口語習慣推高，這跟純粹的兩岸用語滲透不是同一件事，會記一筆 🧬               |
| yunc_bbb      | 特別好、特別喜歡目前詞庫還沒收，可以說「真的很好」「超喜歡」，或延續這篇的脈絡講「挺好的」「挺喜歡」。會把「特別」這個副詞排進下一輪查證 🧬 |

Post-ship verify（per Pitfall 6 hard rule，`[data-pressable-container]` count diff）：guanlaoban987 該則 comment 計數 70→71 一次成功；yunc_bbb 該則 comment 計數 3→4 一次成功。兩則皆 after > before，無 retry。

## #176 X（用語保存副詞層，D+5）

- URL: https://x.com/taiwandotmd/status/2091212353874678264
- Metrics: views 2.4 萬 / replies 21 / reposts 120 / likes 631 / bookmarks 110
- 本則登入牆未完全擋住（與 #173 不同），可讀到 3 則（皆已在 8/23 batch log 記錄過，本輪無新增）：

| Author                          | 留言原文（節錄）                                                                                                         | Bucket                           | 處置                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | --------------------------------------------------------------------------------------- |
| YanaW20                         | 這資料庫會變成教中國ai如何假裝台灣人的資料庫⋯未來將會少了支語做判斷協助⋯                                                 | F（延伸擔憂，非文章事實爭議）    | log only，X 平台限制無法回覆                                                            |
| 月島伶 @ReiTukisima             | 挺、肯定、行吧都是１９４５前就在用的⋯踩雷是網路黎明期台灣輸入中國的，語源應該是Windows95踩地雷⋯體現是出自宋明佛教、理學⋯ | B（entity/context 語源細節補充） | 沿用 8/23 batch log 已記錄的判斷：累積進 EVOLVE candidate（詞條補語源），X 不支援 reply |
| 오ーエンを応援する会 @yu_and_rw | 我都寫「滿」⋯打字時都會自動跳出蠻才知道原來應該是蠻，但我寫字還是寫滿，哈哈哈哈哈（死不改）                              | E（共鳴）                        | log only，X 平台限制無法回覆                                                            |

## 本輪摘要

- 4 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏／疑問）：3 條（guanlaoban987、yunc_bbb 本輪已回覆；月島伶語源補充延續累積，X 平台限制無法回覆）
- Bucket D-adjacent（AI 書寫質疑，人類判斷邊界）：1 條（w.is_solis，寫入 handoff 不自動回覆）
- Bucket E（正面互動）：約 8 條，其中 2 條（v.beibei、mon.\_.bee）確認先前已有作者回覆，其餘 6 條為純共鳴或個人經驗、無新事實內容，本輪判斷 optional 不逐一回覆
- Bucket F：約 6 條（語感偏好或解讀分歧，無新材料，optional 不回覆）
- Reply shipped：2（Threads，guanlaoban987 + yunc_bbb，皆一次成功無 retry）
- Factual fix：0
- 殘留訊號：四天執行空窗期間 #175/#176 的留言區已有一輪未經 routine 記錄的回覆動作（多則留言在 8/24 已有 `作者` 回覆但 dashboard harvestCount 仍顯示只 harvest 過一次），代表空窗期間曾有人工介入但未走完整 pipeline 留痕；w.is_solis 的 AI 書寫信任質疑需要哲宇決定要不要回應以及怎麼回應，本輪只記錄不處置。
