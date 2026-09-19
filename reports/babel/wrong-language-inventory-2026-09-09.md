---
title: '譯文語言錯置盤點 2026-09-09'
description: '九個語言目錄裡有 65 篇文章不是它宣稱的那個語言，六道閘全部放行 — 量測、判準、三個處置選項'
type: 'measurement-report'
status: 'active'
last_updated: 2026-09-09
---

# 譯文語言錯置盤點（2026-09-09）

## 怎麼發現的

Haiku 委派層第一批五篇，其中一篇（`Technology/Threads在台灣.md` → `knowledge/de/`）交回來的是**英文**。而委派層的六道閘全部給它綠燈：

| 閘門                                     | 結果                                              |
| ---------------------------------------- | ------------------------------------------------- |
| `enrich-batch-targets --check`           | ✅ 腳註 55/55、H2 30/30、圖說連結 0/0、網址 71/71 |
| `verify-translation.py`                  | ✅ 17 pass / 1 warn，exit 0                       |
| `cjk-leak-check.py`                      | ✅ 0 處中文洩漏                                   |
| `cjk-adjacency-check.py`                 | ✅ 0 處漢字黏著                                   |
| `article-health.py --profile=pre-commit` | ✅ hard=0                                         |

閘門沒有壞。它們量的都是**形式**——數字對不對、有沒有中文殘留、網址一不一致、frontmatter 欄位齊不齊。一篇英文文章滿足這些條件的程度，跟德文文章一模一樣。發現它靠的是我抽看了正文第一行，不是任何一道閘。

這是 [REFLEXES #69](../../docs/semiont/REFLEXES.md)「形式閘門 ≠ 意義閘門」最基本的一格：連「譯文是不是那個語言」都沒有人在量。

## 量測方法

`scripts/tools/lang-sync/target-language-check.py`（本次新造）。

判準分兩類：**非拉丁書寫系統**（ru/ar/hi/ja/ko）用字符集判定，書寫系統本身就是最強訊號；**拉丁字母語言**（en/de/es/fr/pt/id/vi）用功能詞佔比——冠詞、介系詞、連接詞在任何散文裡都必然大量出現，而且跨語言幾乎不重疊。用功能詞而不是內容詞，是因為內容詞會被專有名詞（台灣地名、人名、品牌）稀釋。

刻意不引入 `langdetect` / `fasttext`：多一個相依就是產線多一個會壞的地方，而這裡要判的只有十二個已知語言的二選一。

判 fail 的條件是「偵測語言 ≠ 目標語言，且領先 1.5 倍以上」。設 1.5 倍而不是「只要領先就 fail」，是因為 es/pt、id/vi 幾組功能詞有零星重疊，短文上會出現接近分數，那種情況該給人看不該直接擋。正文少於 80 個詞不判（清單體、極短文）。

**校準**（用真實產出，不憑想像設閾值 — REFLEXES #66）：已知錯的那篇 de 0.0005 vs en 0.123（差 246 倍）；已知對的四篇德文譯文全過，零誤擋。

**誤判抽驗**：對三篇隨機命中人工讀正文第一行，`ko/Geography/penghu-county.md` 是英文、`ja/History/taiwan-white-terror.md` 是英文、`es/People/teresa-teng.md` 是**法文**。3/3 真陽性。

## 結果

掃描 9,161 檔，**65 篇 fail / 0 warn**。

| 目標語言 | 篇數 | 實際語言                   |
| -------- | ---: | -------------------------- |
| ja       |   22 | en                         |
| ko       |   17 | en                         |
| es       |   13 | en 12、fr 1                |
| fr       |    9 | en                         |
| de       |    1 | en（今天這篇，已移除重做） |
| hi       |    1 | en                         |
| id       |    1 | en                         |
| ru       |    1 | pt                         |

老四語（ja/ko/es/fr）佔 61/65 = 94%，是歷史批次留下的債，不是這次委派造成的。61 篇實際是英文——早期批次的 backend 拿到「翻譯成 X 語」的指令後直接輸出英文，而當時沒有任何一道閘在看語言。

**ja（22 篇）**

| 檔案                                                         | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ------------------------------------------------------------ | ------------ | ------------ | ------------ |
| `ja/Art/post-martial-law-taiwanese-literature.md`            | en           | 0.0          | 0.2796       |
| `ja/Art/taiwan-new-media-art.md`                             | en           | 0.0          | 0.2322       |
| `ja/Art/tehching-hsieh-performance-artist.md`                | en           | 0.0          | 0.2285       |
| `ja/Food/taiwan-specialty-home-cooking.md`                   | en           | 0.0          | 0.2564       |
| `ja/History/psychological-warfare.md`                        | en           | 0.0          | 0.2034       |
| `ja/History/taiwan-democratization-history.md`               | en           | 0.0          | 0.2469       |
| `ja/History/taiwan-democratization.md`                       | en           | 0.0254       | 0.2325       |
| `ja/History/taiwan-white-terror.md`                          | en           | 0.0232       | 0.2493       |
| `ja/Lifestyle/mascot-culture-in-taiwan.md`                   | en           | 0.0          | 0.1847       |
| `ja/Lifestyle/national-highway-system.md`                    | en           | 0.0          | 0.2509       |
| `ja/People/cheng-li-wun.md`                                  | en           | 0.0          | 0.2528       |
| `ja/People/chia-yung-chieh.md`                               | en           | 0.0          | 0.2242       |
| `ja/People/hebe-tien-singer.md`                              | en           | 0.0          | 0.2177       |
| `ja/People/huang-shan-liao.md`                               | en           | 0.0          | 0.2157       |
| `ja/Society/2026-cheng-xi-meeting-kmt-ccp-decade-reunion.md` | en           | 0.0          | 0.2479       |
| `ja/Society/chinese-taipei.md`                               | en           | 0.0001       | 0.2573       |
| `ja/Society/complex-life-festival.md`                        | en           | 0.0          | 0.1986       |
| `ja/Society/i-am-from.md`                                    | en           | 0.0          | 0.2195       |
| `ja/Society/united-front-tour-groups.md`                     | en           | 0.0          | 0.231        |
| `ja/Society/za-share.md`                                     | en           | 0.0          | 0.2316       |
| `ja/Technology/into-the-cellar-taiwan-game-podcast.md`       | en           | 0.0          | 0.2349       |
| `ja/Technology/national-cultural-memory-bank.md`             | en           | 0.0          | 0.2355       |

**ko（17 篇）**

| 檔案                                                    | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ------------------------------------------------------- | ------------ | ------------ | ------------ |
| `ko/Culture/taiwan-religion-and-temple-culture.md`      | en           | 0.0          | 0.2432       |
| `ko/Food/taiwan-banquet-culture.md`                     | en           | 0.0          | 0.2483       |
| `ko/Food/taiwan-specialty-home-cooking.md`              | en           | 0.0          | 0.247        |
| `ko/Geography/nantou-county.md`                         | en           | 0.0          | 0.2235       |
| `ko/Geography/penghu-county.md`                         | en           | 0.0          | 0.2318       |
| `ko/History/psychological-warfare.md`                   | en           | 0.0          | 0.2109       |
| `ko/History/taiwan-white-terror.md`                     | en           | 0.0417       | 0.2454       |
| `ko/Lifestyle/taiwan-mahjong-and-celebrity-shortage.md` | en           | 0.0          | 0.2264       |
| `ko/Lifestyle/taoyuan-airport.md`                       | en           | 0.0          | 0.2682       |
| `ko/People/huai-te-indie-singer.md`                     | en           | 0.0          | 0.2037       |
| `ko/People/huang-shan-liao.md`                          | en           | 0.0          | 0.206        |
| `ko/Society/complex-life-festival.md`                   | en           | 0.0          | 0.212        |
| `ko/Society/taiwan-generations.md`                      | en           | 0.0          | 0.2439       |
| `ko/Society/za-share.md`                                | en           | 0.0          | 0.2402       |
| `ko/Technology/into-the-cellar-taiwan-game-podcast.md`  | en           | 0.0          | 0.2289       |
| `ko/Technology/submarine-cables-taiwan-lifeline.md`     | en           | 0.0          | 0.1986       |
| `ko/Technology/taiwan-bim-construction-tech.md`         | en           | 0.0127       | 0.2053       |

**es（13 篇）**

| 檔案                                                  | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ----------------------------------------------------- | ------------ | ------------ | ------------ |
| `es/Economy/aama-taipei-cradle-program.md`            | en           | 0.0071       | 0.2017       |
| `es/Food/taiwan-banquet-culture.md`                   | en           | 0.0012       | 0.2328       |
| `es/History/psychological-warfare.md`                 | en           | 0.0          | 0.2108       |
| `es/People/chen-shui-bian-controversial-president.md` | en           | 0.0          | 0.2282       |
| `es/People/han-kuo-yu.md`                             | en           | 0.0027       | 0.2526       |
| `es/People/huang-shan-liao.md`                        | en           | 0.0009       | 0.2104       |
| `es/People/rainie-yang.md`                            | en           | 0.0          | 0.2555       |
| `es/People/teresa-teng.md`                            | fr           | 0.13         | 0.2797       |
| `es/Society/chinese-taipei.md`                        | en           | 0.0003       | 0.2554       |
| `es/Society/complex-life-festival.md`                 | en           | 0.0003       | 0.2231       |
| `es/Society/united-front-tour-groups.md`              | en           | 0.0011       | 0.2254       |
| `es/Society/za-share.md`                              | en           | 0.0024       | 0.2409       |
| `es/Technology/facebook-in-taiwan.md`                 | en           | 0.0026       | 0.2226       |

**fr（9 篇）**

| 檔案                                      | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ----------------------------------------- | ------------ | ------------ | ------------ |
| `fr/History/psychological-warfare.md`     | en           | 0.0          | 0.2055       |
| `fr/History/taiwan-emigration-history.md` | en           | 0.0          | 0.2369       |
| `fr/People/cheng-li-wun.md`               | en           | 0.0002       | 0.2502       |
| `fr/People/huang-shan-liao.md`            | en           | 0.0004       | 0.2112       |
| `fr/People/ji-lin-lian.md`                | en           | 0.0006       | 0.2492       |
| `fr/Society/falun-gong-in-taiwan.md`      | en           | 0.0          | 0.254        |
| `fr/Society/united-front-tour-groups.md`  | en           | 0.0011       | 0.2233       |
| `fr/Society/za-share.md`                  | en           | 0.001        | 0.24         |
| `fr/Technology/facebook-in-taiwan.md`     | en           | 0.0036       | 0.2285       |

**de（1 篇）**

| 檔案                                 | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ------------------------------------ | ------------ | ------------ | ------------ |
| `de/Technology/threads-in-taiwan.md` | en           | 0.0005       | 0.123        |

**hi（1 篇）**

| 檔案                                 | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ------------------------------------ | ------------ | ------------ | ------------ |
| `hi/Lifestyle/hot-spring-culture.md` | ko           | 0.007        | 0.6588       |

**id（1 篇）**

| 檔案                | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ------------------- | ------------ | ------------ | ------------ |
| `id/Art/fab-dao.md` | hi           | 0.0          | 0.7326       |

**ru（1 篇）**

| 檔案                                       | 實際看起來是 | 目標語言分數 | 偵測語言分數 |
| ------------------------------------------ | ------------ | ------------ | ------------ |
| `ru/Economy/foxconn-precision-industry.md` | pt           | 0.0003       | 0.0213       |

## 已經做的

`babel-dispatch.py` 的 `verify_one()` 第一關接上這道閘（commit 見本日 git log），擋住增量。放在第一是因為它最便宜也最根本：如果檔案不是目標語言，後面三道檢查回答的是另一份文件的問題。擋下時原因記成 `wrong-language[en]`，`report.jsonl` 查得到敗在哪。已跑 end-to-end smoke（真德文放行、ko 目錄裡的英文擋下且原因歸類正確），不只 `py_compile`。

委派層的 agent prompt 也加了這道閘作為交件前必跑的第一項。

## 待決：65 篇存量怎麼處理

屬 §自主權邊界（>50 檔重構），需要哲宇拍板。

**選項 A — 全部重譯**：65 篇丟回產線重翻。乾淨，但 ja/ko/es/fr 目前都有免費算力軌在跑，插隊 65 篇會排擠當前佇列；而且這 65 篇現在站上「有內容」，重譯期間如果先刪掉會變成 missing，比英文更糟。

**選項 B — 標記後分批重譯（推薦）**：先把 65 篇的 `sourceCommitSha` 清掉，讓 `status.py` 把它們歸成 stale，自然排進既有佇列由產線逐步汰換，站上內容不中斷。缺點是這批在被汰換前，讀者仍會讀到英文。

**選項 C — 只擋增量，存量不動**：讓它們留著，等自然重譯。成本最低，但那 61 篇英文會一直在站上，而且沒有任何機制保證它們會被排到。

**推薦 B**：這批不是「內容錯」是「語言錯」，內容本身是完整的譯文（只是語言不對），降級成 stale 由產線接手最不打斷讀者，也不需要另開一條批次。真正的急迫性在 `ko` 那 17 篇——韓文讀者現在點進去讀到的是英文，而韓文是老四語裡覆蓋率最高的（78.1%），讀者密度也最高。
