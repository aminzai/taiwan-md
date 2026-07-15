---
article: knowledge/People/尊.md
audit_date: 2026-07-15
mode: FACTCHECK Full Phase 1-6
verdict: CONDITIONAL_FAIL
claimed_web_opens: 25
actual_network_actions: 40+
article_modified: false
---

# 尊：最終正文完整事實查核（final factcheck agent）

## 執行摘要

本次只查核 `knowledge/People/尊.md`，沒有修改正文。依 `docs/pipelines/FACTCHECK-PIPELINE.md` 判定為 A 級 People 條目，跑 Phase 1-6、9/9 正式腳註四維稽核、72 個 atom、所有正文直接引語逐字比對、數字算術與跨段時序檢查。實際執行 23 次 `curl` 開頁、4 次 `yt-dlp` 官方影片 metadata、4 次 YouTube oEmbed，以及多次中文搜尋與頁內開啟；保守只宣稱 25 次來源開啟。

**總 verdict：CONDITIONAL FAIL／尚不可視為完全 ship-safe。** 主要原因不是文章主脊失真，而是 1 個正式腳註死亡、數個精確時間／年齡 claim 沒有被現有腳註承載，以及一個直接引語無法在其實際 footnote 的 HTML 逐字命中。

| 分類         | 數量 | 結論                                                                                            |
| ------------ | ---: | ----------------------------------------------------------------------------------------------- |
| ✅ PASS      |   60 | 2018 起步與訪問、2023 業配回應、2024 司法數字、三支官方影片 metadata、蘿倫 Q&A 核心內容大致成立 |
| ⚠️ SOFT-FIX  |    6 | 「十四年」口徑、貓、限動 24 小時、2021 女友報導等需降級／補引                                   |
| ❌ HARD-FIX  |    5 | 本名腳註缺口、曝光隔天、26／27 歲、[^5] 直接引語逐字承載不足                                    |
| 🔴 DEAD-LINK |    1 | `[^2]` 達人秀 URL `/48444` 為 404；正確同題文章為 `/49685`                                      |

> 分類數量以「獨立問題 atom」計，不把同一個「十四年」在全文五次重複算五件，也不把 `[^2]` 所承載的兩個相鄰句子重複算兩個 DEAD。

## Phase 1：Scope & budget

- Tier：A（真人 People、超過 3,000 字、含司法犯罪與多句直接引語）。
- 輸入：`knowledge/People/尊.md`、`reports/research/2026-07/尊.md`、`reports/research/2026-07/尊-facts-agent.md`、FACTCHECK pipeline。
- 目標：正文 100% 高風險 atom；至少 50 行，實際 72 行。
- 正式腳註：9；四維 audit：9/9。
- 開頁預算：25+；實際網路動作 40+，其中可逐筆重現的來源開啟／metadata 至少 31。
- 輸出：本檔；依任務約束不修改 article。

## 搜尋軌跡／開頁紀錄（逐條）

以下保留 query → 發現 → URL；中文頁均以中文原文核查，沒有用英文摘要替代中文逐字。

1. WebSearch「site:news.housefun.com.tw 尊 最剛開始做的 包袱」→ 命中 2018 聯合報／好房網人物訪問 → https://news.housefun.com.tw/news/article/196239205065.html
2. WebFetch 好房網 canonical → HTTP 202 但可正常讀取完整正文；命中 19 歲、120 萬、國二、最年輕、先機、包袱、漫畫家 → https://news.housefun.com.tw/news/article/196239205065.html
3. WebFetch 好房網 AMP → HTTP 202；內容與 canonical 同源交叉 → https://news.housefun.com.tw/news/article/amp/196239205065.html
4. WebSearch「site:ttshow.tw 尊 黑歷史 拍片菜鳥」→ 搜尋實際命中 `/49685`，不是正文腳註的 `/48444` → https://www.ttshow.tw/article/49685
5. WebFetch 正文 `[^2]` → HTTP 404 → https://www.ttshow.tw/article/48444
6. WebFetch 正確達人秀文章 → HTTP 200；命中 2012、早期遊戲實況、回看舊片、模仿／自嘲 → https://www.ttshow.tw/article/49685
7. WebSearch「尊 口袋奇兵 草率接下 下架我的影片」→ 命中 Newtalk 2023 同日保存 → https://newtalk.tw/news/view/2023-11-03/895065
8. WebFetch Newtalk → HTTP 200；頁內逐字命中「草率接下」「應該在那個時候就讓廣告商下架我的影片」 → https://newtalk.tw/news/view/2023-11-03/895065
9. WebFetch 中央社 2024-05-09 → HTTP 200；命中 119、1,000 萬餘、83／36、5 年＋1 年 8 月 → https://www.cna.com.tw/news/asoc/202405090066.aspx
10. WebFetch 公視司法交叉 → HTTP 200；最高法院 5 月 8 日駁回上訴、刑期結構一致 → https://news.pts.org.tw/article/694360
11. WebFetch 中央社 2024-12-18 → HTTP 200；交叉確認入監後刑度敘述 → https://www.cna.com.tw/news/asoc/202412180146.aspx
12. WebSearch「尊 小玉 不切割 我真的很累了」→ 命中 TVBS 同日報導 → https://news.tvbs.com.tw/entertainment/1611575
13. WebFetch TVBS → HTTP 200；命中「一時發生太多事情，我真的很累了」與哥哥自行承擔；報導日期 2021-10-18 → https://news.tvbs.com.tw/entertainment/1611575
14. WebFetch 民視同日保存 → curl HTTP 403；搜尋工具既有索引可交叉但不可當本輪可讀頁 → https://www.ftvnews.com.tw/news/detail/2021A18W0248
15. WebSearch 精確字串「沒有要和小玉切割，他依然是我哥哥不會變」→ TVBS HTML 未完整命中；鏡週刊逐字命中 → https://www.mirrormedia.mg/story/20211018edi042
16. WebFetch 鏡週刊 2021-10-18 → 可讀；逐字承載「他依然是我哥哥不會變」與完整疲憊句 → https://www.mirrormedia.mg/story/20211018edi042
17. WebSearch「尊 蘿倫 三天 四年半」→ 命中 Newtalk 正確 ID `/762807` → https://newtalk.tw/news/view/2022-05-30/762807
18. WebFetch Newtalk 蘿倫文 → HTTP 200；命中小玉牽線、三天、無正式告白、四年半 → https://newtalk.tw/news/view/2022-05-30/762807
19. WebFetch 鏡週刊 2021 女友／同居交叉 → HTTP 200；可補正文「2021 已稱女友」之來源 → https://www.mirrormedia.mg/story/amp/20211019edi023
20. WebFetch YouTube oEmbed 蘿倫 Q&A → HTTP 200；標題、作者頻道正確 → https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=BDxeiny76y4&format=json
21. yt-dlp 蘿倫 Q&A → `20220528 / 18:15 / public / playable_in_embed=True` → https://www.youtube.com/watch?v=BDxeiny76y4
22. WebFetch YouTube oEmbed 新家 → HTTP 200；作者「人生肥宅x尊」 → https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=twgMJSxS-H8&format=json
23. yt-dlp 新家 → `20251213 / 16:10 / public / playable_in_embed=True` → https://www.youtube.com/watch?v=twgMJSxS-H8
24. WebFetch YouTube oEmbed 副頻道百萬 Q&A → HTTP 200；作者為副頻道 → https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=m5Za_ARPRx0&format=json
25. yt-dlp 副頻道百萬 Q&A → `20241228 / 13:14 / public / playable_in_embed=True` → https://www.youtube.com/watch?v=m5Za_ARPRx0
26. WebFetch YouTube oEmbed 黑歷史回顧 → HTTP 200 → https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=OUZB30lyGcc&format=json
27. yt-dlp 黑歷史回顧 → `20180505 / 7:08 / public / playable_in_embed=True` → https://www.youtube.com/watch?v=OUZB30lyGcc
28. WebFetch 主頻道 → HTTP 200；handle `@loserzun` 活著 → https://www.youtube.com/@loserzun
29. WebFetch 副頻道 → HTTP 200；handle `@nerdzun` 活著 → https://www.youtube.com/@nerdzun
30. WebFetch 蘿倫頻道 → HTTP 200；handle `@laurenveur` 活著 → https://www.youtube.com/@laurenveur
31. WebFetch 卡優 2018-01-12 → HTTP 200；99.7 萬只作早期里程碑交叉，不進正文 → https://www.cardu.com.tw/news/detail.php?34691=
32. WebFetch 4Gamers 2017 年底盤點 → HTTP 200；當時尊仍列 70–100 萬潛力頻道 → https://www.4gamers.com.tw/news/detail/33848/2017-taiwan-youtube-million-subscribers-award
33. WebFetch 民視龍船／雙百萬 → HTTP 200；研究背景交叉，正文未使用龍船細節 → https://sport.ftvnews.com.tw/news/detail/2025112W0208
34. WebFetch 民視勝利組 → curl HTTP 403；不拿來承載本篇現存 claim → https://www.ftvnews.com.tw/news/detail/2024314W0181
35. WebSearch「尊 本名 朱玉恩」→ 搜到公司登記聚合與低階人物頁，但現有九個腳註沒有任何一個承載本名 → https://info.technews.tw/company/90570184-%E4%BA%BA%E7%94%9F%E8%82%A5%E5%AE%85%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8

## Phase 2：Atomic decomposition（72 atoms）

狀態欄是「正文現狀相對於現有 footnote」；PASS 不代表來源是完美一手，只代表四關及 claim 對應足夠。

|   # |                   Line | 類型       | Atom                                         | Fn        | 判定    | 核查摘要                                                                                           |
| --: | ---------------------: | ---------- | -------------------------------------------- | --------- | ------- | -------------------------------------------------------------------------------------------------- |
|   1 |                  19/27 | 人名       | 尊本名朱玉恩                                 | [^1] 鄰近 | ❌ HARD | [^1] 沒寫本名；外部公司資料可補，但現有 citation gap                                               |
|   2 |                  19/27 | 時間       | 國二開始拍片                                 | [^1]      | ✅ PASS | 好房網 L116／達人秀正確頁均支持                                                                    |
|   3 |                  19/27 | 動作       | 最初上傳遊戲實況                             | [^1]      | ✅ PASS | 源文「最初是以遊戲實況主出道」                                                                     |
|   4 |                  19/21 | 時間       | 2018 年                                      | [^1]      | ✅ PASS | 來源日期 2018-08-24                                                                                |
|   5 |               19/21/27 | 數字       | 19 歲                                        | [^1]      | ✅ PASS | 源文逐字「年僅19歲」                                                                               |
|   6 |                  19/27 | 數字       | 120 萬訂閱                                   | [^1]      | ✅ PASS | 源文逐字                                                                                           |
|   7 |                  19/27 | 數字／機構 | 當時台灣最年輕百萬 YouTuber                  | [^1]      | ✅ PASS | 媒體明確如此稱呼；應保留來源化語氣                                                                 |
|   8 |               19/42/91 | 時間／數字 | 2024 年底副頻道越過百萬                      | [^8]      | ✅ PASS | 官方片 2024-12-28，標題含百萬訂閱                                                                  |
|   9 | 3/19/23/29/109/129/131 | 數字／時間 | 十四年／跨度十四年                           | [^2]/[^7] | ⚠️ SOFT | 約 2012 至 2025-12 是 13 年 elapsed；若用 inclusive calendar years 才是 14，需明示或改「逾十三年」 |
|  10 |                  19/67 | 物件       | Deepfake 換臉色情影片                        | [^4]      | ✅ PASS | 中央社明確支持                                                                                     |
|  11 |                  19/57 | 物件       | 《口袋奇兵》業配                             | [^3]      | ✅ PASS | Newtalk 明確支持                                                                                   |
|  12 |                     21 | 引語       | 「最剛開始做的」                             | [^1]      | ✅ PASS | 源文長句中逐字命中                                                                                 |
|  13 |                     21 | 引語       | 「訂閱低什麼都敢拍，訂閱高會有一定的包袱。」 | [^1]      | ✅ PASS | 源文逐字前半句；正文在句號前截短，未改詞                                                           |
|  14 |              23/42/125 | 數字       | 兩個／雙頻道皆百萬                           | [^8]+[^1] | ✅ PASS | 主頻道 [^1]、副頻道 [^8] 合併成立                                                                  |
|  15 |                 23/107 | 地點／物件 | 新家進入公開影片                             | [^7]      | ✅ PASS | 官方標題與 metadata 支持「新家」最小 claim                                                         |
|  16 |                     23 | 人名／物件 | 女友與貓                                     | 無直接 fn | ⚠️ SOFT | 女友有 [^9]；「貓」不由現有 footnote 承載                                                          |
|  17 |                     27 | 動作       | 從遊戲轉實驗、開箱、都市傳說                 | [^1]      | ✅ PASS | 源文支持                                                                                           |
|  18 |                     27 | 人名／機構 | 受日本 YouTuber 影響                         | [^1]      | ✅ PASS | 源文逐字支持                                                                                       |
|  19 |                     27 | 時間       | 2018 年 8 月已有 120 萬                      | [^1]      | ✅ PASS | 日期與內文支持                                                                                     |
|  20 |                     29 | 動作       | 公開翻出早期影片                             | [^2]      | 🔴 DEAD | claim 可由正確 `/49685` 支持，但現有 URL `/48444` 404                                              |
|  21 |                  29/35 | 動作       | 拿模仿與生澀當笑料／回看自己                 | [^2]      | 🔴 DEAD | 同上，同一 dead footnote 問題不重複計件                                                            |
|  22 |                  33/49 | 機構       | 沒簽經紀公司                                 | [^1]      | ✅ PASS | 源文支持                                                                                           |
|  23 |                     33 | 動作       | 當時沒有做業配                               | [^1]      | ✅ PASS | 源文「也沒做業配」                                                                                 |
|  24 |                  33/49 | 機構／動作 | 收入主要靠 YouTube 點閱                      | [^1]      | ✅ PASS | 源文「收入來源全靠YT點閱」                                                                         |
|  25 |                     33 | 數字       | 頻道百萬不代表身價百萬                       | [^1]      | ✅ PASS | 源文「身價沒有百萬」                                                                               |
|  26 |                     33 | 人名／機構 | 小玉公開收入引國稅局注意                     | [^1]      | ✅ PASS | 源文支持                                                                                           |
|  27 |                 37/119 | 動作／物件 | 想當漫畫家、喜歡畫畫                         | [^1]      | ✅ PASS | 逐字意義相符                                                                                       |
|  28 |                     40 | 時間／數字 | 約 2012 年開始                               | [^2]      | 🔴 DEAD | 正確達人秀頁寫 2012；現有腳註死鏈                                                                  |
|  29 |                     42 | 數字       | 2 個頻道皆破百萬                             | [^1]+[^8] | ✅ PASS | 跨源成立                                                                                           |
|  30 |                     45 | 引語       | 承認「早」帶來平台紅利                       | [^1]      | ✅ PASS | 源文「比較早抓到先機」；「平台紅利」是策展概括，不是直接引語                                       |
|  31 |                     49 | 引語       | 「很無聊、很爛的東西」                       | [^1]      | ✅ PASS | 源文逐字片段                                                                                       |
|  32 |                  53/55 | 引語／稱號 | 媒體稱「清流」                               | [^3] 鄰近 | ✅ PASS | Newtalk 原文「YT唯一清流」；正文有來源化語氣                                                       |
|  33 |                     57 | 時間       | 2023 年 11 月                                | [^3]      | ✅ PASS | 來源 2023-11-03                                                                                    |
|  34 |                     57 | 人名       | YouTuber 賴鴻麟提出指控                      | [^3]      | ✅ PASS | 源文支持                                                                                           |
|  35 |                     57 | 動作       | 多名創作者用同一廣告影片配音                 | [^3]      | ✅ PASS | 源文支持                                                                                           |
|  36 |                     57 | 動作       | 內容與實際遊戲不符                           | [^3]      | ✅ PASS | 正文正確歸屬為賴鴻麟「指出」，不是作者獨立鑑定                                                     |
|  37 |                     57 | 數字／物件 | 廠商提供五段影片                             | [^3]      | ✅ PASS | 源文逐字                                                                                           |
|  38 |                     57 | 引語／動作 | 「草率接下」                                 | [^3]      | ✅ PASS | Ctrl-F exact hit                                                                                   |
|  39 |                     57 | 動作       | 要求撤下廣告                                 | [^3]      | ✅ PASS | 源文支持                                                                                           |
|  40 |                     57 | 動作       | 往後更嚴格審視業配                           | [^3]      | ✅ PASS | 源文逐字意義                                                                                       |
|  41 |                     59 | 引語       | 「應該在那個時候就讓廣告商下架我的影片。」   | [^3]      | ✅ PASS | Ctrl-F exact hit，正文僅補句號                                                                     |
|  42 |                     59 | 數字／動作 | 廠商加錢仍拒絕                               | [^3]      | ✅ PASS | 源文支持                                                                                           |
|  43 |                     67 | 時間       | 事件於 2021 年發生                           | [^5]      | ✅ PASS | TVBS 日期 2021-10-18                                                                               |
|  44 |                     67 | 人名       | 尊哥哥朱玉宸即小玉                           | [^4]/[^5] | ✅ PASS | 兩源交叉支持                                                                                       |
|  45 |                  67/69 | 數字       | 119 名被害人                                 | [^4]      | ✅ PASS | CNA exact                                                                                          |
|  46 |                     67 | 數字       | 犯罪所得逾新台幣 1,000 萬                    | [^4]      | ✅ PASS | CNA「1000萬餘元」                                                                                  |
|  47 |                     67 | 時間／機構 | 2024 最高法院維持二審                        | [^4]      | ✅ PASS | 2024-05-08 駁回上訴，5/9 報導                                                                      |
|  48 |                     67 | 數字       | 不得易科部分 5 年                            | [^4]      | ✅ PASS | CNA exact                                                                                          |
|  49 |                     67 | 數字       | 另 1 年 8 月得易科罰金                       | [^4]      | ✅ PASS | CNA exact                                                                                          |
|  50 |                     69 | 人名／動作 | 小玉與助理合成公眾人物臉部                   | [^4]      | ✅ PASS | CNA 支持                                                                                           |
|  51 |                     69 | 動作       | 上傳供付費觀看                               | [^4]      | ✅ PASS | CNA 支持                                                                                           |
|  52 |                     69 | 數字       | 83 人提告、36 人未提告                       | [^4]      | ✅ PASS | 83+36=119，源文 exact                                                                              |
|  53 |                     71 | 時間       | 「案件曝光隔天」尊發限動                     | [^5]      | ❌ HARD | TVBS 說 10/18 當日案件曝光、尊同日發文；不是隔天                                                   |
|  54 |                     71 | 動作       | 小玉從未向家人提過在做什麼                   | [^5]      | ✅ PASS | TVBS／鏡週刊均保存相同意義                                                                         |
|  55 |                     71 | 動作       | 向被害者道歉                                 | [^5]      | ✅ PASS | TVBS 支持                                                                                          |
|  56 |                     71 | 引語       | 「沒有要和小玉切割，他依然是我哥哥不會變」   | [^5]      | ❌ HARD | TVBS HTML 只有前半意義的轉述，整句 Ctrl-F 不命中；鏡週刊 `/20211018edi042` 可補 exact              |
|  57 |                     71 | 引語       | 「一時發生太多事情，我真的很累了。」         | [^5]      | ✅ PASS | TVBS exact wording hit；標點差異不改字                                                             |
|  58 |                     75 | 時間／機構 | IG 限動二十四小時後消失                      | 無專門 fn | ⚠️ SOFT | 一般平台規則合理，但本段未附官方規則；且可被加到精選，宜寫「通常 24 小時後消失」                   |
|  59 |                  91/99 | 時間／機構 | 2022 蘿倫頻道 Q&A                            | [^6]      | ✅ PASS | 官方 metadata 2022-05-28、標題與頻道正確                                                           |
|  60 |                     95 | 時間       | 2024-12-28 上傳副頻道問答                    | [^8]      | ✅ PASS | yt-dlp exact                                                                                       |
|  61 |                     95 | 引語／物件 | 標題有「百萬訂閱」與監獄問小玉               | [^8]      | ✅ PASS | 官方 title exact meaning；正文「探監」是合理概括                                                   |
|  62 |                     95 | 數字       | 副頻道百萬時尊 26 歲                         | [^8]      | ❌ HARD | 官方 metadata 不含出生日期／年齡；現有九腳註無 DOB 來源                                            |
|  63 |                 99/101 | 人名／動作 | 蘿倫與尊透過小玉認識                         | [^9]      | ✅ PASS | Newtalk 支持；原文誤稱「尊的弟弟小玉」，正文未複製錯誤親屬稱謂                                     |
|  64 |                    101 | 數字／動作 | 相處三天決定交往                             | [^9]      | ✅ PASS | source exact meaning                                                                               |
|  65 |                    101 | 動作       | 沒有正式告白                                 | [^9]      | ✅ PASS | source exact meaning                                                                               |
|  66 |                    101 | 數字／時間 | 2022 時交往四年半                            | [^9]      | ✅ PASS | source exact                                                                                       |
|  67 |                    101 | 時間／人名 | 2021 報導已稱蘿倫為女友                      | [^9] 鄰近 | ⚠️ SOFT | 事實可由鏡週刊 2021 支持，但正文未附該 URL；[^9] 只概述先前已公開                                  |
|  68 |                    107 | 時間／機構 | 2025 年 12 月主頻道上架新家片                | [^7]      | ✅ PASS | metadata exact 2025-12-13                                                                          |
|  69 |                107/109 | 引語／物件 | 片名只寫「新家」                             | [^7]      | ✅ PASS | official title supports minimal claim                                                              |
|  70 |                    109 | 物件       | 不推斷所有權、房價、首購                     | [^7]      | ✅ PASS | 是證據護欄，正確                                                                                   |
|  71 |                109/127 | 數字       | 新家時／目前尊 27 歲                         | [^7]      | ❌ HARD | [^7] 只有影片日期，不含 DOB；現有 citation chain 不足                                              |
|  72 |                    119 | 引語／動作 | 想畫漫畫；成功因抓得早                       | [^1]      | ✅ PASS | 兩項均在 source 原文                                                                               |

## Phase 3：Footnote source authority 四維 audit

記號依 pipeline：`URL_resolves / source_real / desc_accurate / claim_matches`。

| Fn   | URL                                                         | 四維                   | Source authority 與結論                                                                                                                                                                       |
| ---- | ----------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [^1] | https://news.housefun.com.tw/news/article/196239205065.html | Y / Y / Y / Y          | 可讀完整聯合報署名人物訪問；正文日期、年齡、120 萬、國二、題材、先機、包袱、漫畫夢均命中。唯「朱玉恩」不在此頁，故本名 atom 不能假借 [^1] 過關。                                              |
| [^2] | https://www.ttshow.tw/article/48444                         | **N / N / N / N**      | curl 404，Web open 不可讀。正確同題頁為 https://www.ttshow.tw/article/49685 ，可承載回看舊片與 2012 起步。正式腳註仍是 DEAD。                                                                 |
| [^3] | https://newtalk.tw/news/view/2023-11-03/895065              | Y / Y / Y / Y          | Newtalk 真頁、日期與描述準確；五段影片、草率接下、撤廣告、加錢拒絕、加強審視及完整下架引語均支持。                                                                                            |
| [^4] | https://www.cna.com.tw/news/asoc/202405090066.aspx          | Y / Y / Y / Y          | 中央社司法報導，權威度高；119、1000 萬餘、83／36、5 年＋1 年 8 月均 exact。另由公視交叉。                                                                                                     |
| [^5] | https://news.tvbs.com.tw/entertainment/1611575              | Y / Y / Y / **部分 N** | 真頁、描述大致準確，支持致歉、不切割之意、哥哥自行承擔與疲憊句；但正文完整引語「沒有要和小玉切割，他依然是我哥哥不會變」無法在 TVBS HTML Ctrl-F exact，且「曝光隔天」與 TVBS 同日時間線衝突。 |
| [^6] | https://www.youtube.com/watch?v=BDxeiny76y4                 | Y / Y / Y / Y\*        | 官方蘿倫頻道一手影片，2022-05-28、18:15、public、可嵌。無可下載字幕，逐項交往內容需以 [^9] 交叉，不可聲稱本輪完成整片人工逐字稿。                                                             |
| [^7] | https://www.youtube.com/watch?v=twgMJSxS-H8                 | Y / Y / Y / **部分 N** | 官方主頻道影片，2025-12-13、16:10、public、可嵌；支持新家最小事實，不支持 27 歲或十四年算法。                                                                                                 |
| [^8] | https://www.youtube.com/watch?v=m5Za_ARPRx0                 | Y / Y / Y / **部分 N** | 官方副頻道影片，2024-12-28、13:14、public、可嵌；標題含百萬訂閱與監獄問小玉，支持副頻道百萬里程碑；不支持 26 歲。                                                                             |
| [^9] | https://newtalk.tw/news/view/2022-05-30/762807              | Y / Y / Y / Y\*        | 真頁，支持小玉牽線、三天、無告白、四年半。源文把小玉誤寫為「尊的弟弟」，正文沒有採這個錯誤。正文「2021 報導已稱女友」仍宜補鏡週刊 2021 URL。                                                  |

四維 gate 結論：8 個 URL 活著，1 個 DEAD；`[^5]`、`[^7]`、`[^8]` 有局部 over-citing／scope creep。不能用「整個 footnote 大致正確」掩蓋個別 atom mismatch。

## Phase 4：直接引語 verbatim audit

|   # | 正文引號文字                                 | Source Ctrl-F                                              | 結論                                                      |
| --: | -------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
|  Q1 | 「最剛開始做的」                             | [^1] 原句「我會成功是因為我是最剛開始做的」exact substring | ✅ PASS                                                   |
|  Q2 | 「訂閱低什麼都敢拍，訂閱高會有一定的包袱。」 | [^1] exact，來源後面另有「不敢拍很無聊、很爛的東西」       | ✅ PASS；合法截短                                         |
|  Q3 | 「百萬」                                     | [^1] 多處 exact；此處兼具概念性 scare quote                | ✅ PASS                                                   |
|  Q4 | 「早」                                       | [^1] 原文「比較早抓到先機」                                | ✅ PASS；單字 exact，後面的「平台紅利」是作者概括         |
|  Q5 | 「很無聊、很爛的東西」                       | [^1] exact substring                                       | ✅ PASS                                                   |
|  Q6 | 「清流」                                     | [^3] 原文「YT唯一清流」                                    | ✅ PASS；應維持媒體稱號歸屬                               |
|  Q7 | 「草率接下」                                 | [^3] exact                                                 | ✅ PASS                                                   |
|  Q8 | 「應該在那個時候就讓廣告商下架我的影片。」   | [^3] exact words                                           | ✅ PASS                                                   |
|  Q9 | 「沒有要和小玉切割，他依然是我哥哥不會變」   | [^5] TVBS HTML 不 exact；鏡週刊 2021-10-18 exact           | ❌ HARD-FIX：補 exact source 或拆成 TVBS 可承載的間接敘述 |
| Q10 | 「一時發生太多事情，我真的很累了。」         | [^5] exact words；來源標點為驚嘆號／置於長句               | ✅ PASS                                                   |
| Q11 | 「切割」「不切割」                           | 作者對框架的概念性 scare quotes，非宣稱逐字原話            | ✅ N/A（非 direct attribution）                           |
| Q12 | 「百萬訂閱」                                 | [^8] official title exact                                  | ✅ PASS                                                   |
| Q13 | 「新家」                                     | [^7] official title exact                                  | ✅ PASS                                                   |
| Q14 | 「流量退潮後改拍家庭」                       | 明確以「這不是……的證明」否定的假說，不是尊原話             | ✅ N/A                                                    |
| Q15 | 「成年紀錄」                                 | 文章自訂分析框架，不是人物原話                             | ✅ N/A                                                    |

Verbatim gate：可歸屬人物的 10 組核心引語中 9 組 pass，1 組 footnote-specific fail。沒有發現 third-person flip；沒有把「他」改成人名塞入引號。

## Phase 5：算術、時序、跨 claim consistency

### 算術

- `83 + 36 = 119`：✅ 與 [^4] 一致。
- 刑期不能簡單相加成「6 年 8 月」：正文正確分寫不得易科 5 年、另 1 年 8 月得易科，✅。
- `2018 → 2024 = 6 年`，若 2018-08 為 19 歲，2024-12 可能為 25 或 26；沒有 DOB 就不能唯一推出 26。❌ 年齡 claim source gap。
- `2018 → 2025 = 7 年`，同理只能推出約 26／27，不能唯一推出 27。❌ 年齡 claim source gap。
- `約 2012 → 2025-12 = 約 13 年 elapsed`；若把 2012、2013……2025 各曆年都算一格，才有 14 個曆年。正文寫「兩個畫面之間的十四年」容易被理解為 elapsed duration，⚠️ 建議「逾十三年」或明說「跨越十四個曆年」。
- 主、副頻道各一個，共 2 個：✅ [^1]+[^8]。

### 時序

| 時序 claim                                           | 結果                                          |
| ---------------------------------------------------- | --------------------------------------------- |
| 國二／約 2012 起步 → 2018 黑歷史回顧                 | ✅ 正確頁與官方 metadata 相容                 |
| 2018-05 黑歷史片 → 2018-08 人物訪問                  | ✅                                            |
| 2021 案件曝光 → 尊發限動                             | ❌ 正文寫「隔天」，TVBS 記載同日 2021-10-18   |
| 2021 已公開女友 → 2022 Q&A 補交往細節                | ✅ 外部鏡週刊交叉成立，但正文 citation 不完整 |
| 2023-11 業配回應 → 2024-12 副頻道百萬 → 2025-12 新家 | ✅ metadata 順序正確                          |
| 2024 最高法院定讞刑度                                | ✅ 5/8 駁回、5/9 報導；正文只寫年份，安全     |

### 跨 claim／稱謂

- 尊／朱玉恩／人生肥宅x尊：稱謂使用一致；但本名 citation 不在現有 footnote 中。
- 小玉／朱玉宸／哥哥：[^4]+[^5] 一致。
- 主頻道「人生肥宅x尊」與副頻道「人生魯宅x尊-第2頻道」：官方 metadata 一致。
- 蘿倫 Q&A：official channel 與 Newtalk 二手整理相互對上；Newtalk 自己把小玉誤稱「尊的弟弟」，不能反向污染正文。
- 「清流」在全文被清楚處理成外界標籤，不是作者對品格的 fact verdict，✅。
- 「新家」被限制為片名與住處畫面，不推導所有權、房價、第一棟房，✅ 是優良 negative-boundary。

## Phase 6：Triage（HARD／DEAD／UNVERIFIED 明細）

### 🔴 DEAD-LINK（1）

1. `[^2]` `https://www.ttshow.tw/article/48444`：HTTP 404。正確同題文章是 `https://www.ttshow.tw/article/49685`。受影響 atom：L29 回看早期影片、L40 約 2012、圖片來源的歷史語境。這是可直接換 URL 的明確 dead-link，不是內容不可查。

### ❌ HARD-FIX（5）

1. L19/L27「尊本名朱玉恩」：高度具體人名 atom，現有 `[^1]` 不含本名。可補公司登記／正式媒體來源；在補前是 citation mismatch，不判定名字本身為假。
2. L71「案件曝光隔天」：TVBS 2021-10-18 寫案件當日曝光，尊亦同日發限動；「隔天」是時間錯誤。應改「案件曝光當天」或「案件曝光後」。
3. L71 直接引語「沒有要和小玉切割，他依然是我哥哥不會變」：TVBS HTML 沒有整句 exact。鏡週刊同日頁 exact，可加來源；否則去引號改間接敘述。
4. L95「副頻道里程碑發生在他二十六歲」：`[^8]` metadata 不含 DOB／年齡；沒有現有 footnote 能完成算術 base verification。
5. L109/L127「二十七歲的新家／國二開始拍片的人到了二十七歲」：同理，`[^7]` 只證影片日期與標題，不證年齡。

### ⚠️ SOFT-FIX／UNVERIFIED（6）

1. 全文「十四年」：不是完全不可能（inclusive calendar-year count），但以 2012 到 2025 的 elapsed duration 算是約 13 年。應統一口徑。
2. L23「女友與貓」：女友有源，「貓」不在九腳註的 claim chain。
3. L75「限時動態二十四小時後便會消失」：宜加「通常」避免忽略 Highlights／典藏例外。
4. L101「2021 年的報導已經稱蘿倫為尊的女友」：研究檔有鏡週刊 URL，但正文 footnote 未附。
5. `[^6]` 官方 Q&A 無可下載字幕；正文 L99 的「停頓、吐槽與熟悉感」屬評論可保留，但不能當逐字 transcript 證據。
6. 本輪沒有可驗的官方 DOB；因此任何由生日導出的精確年齡一律維持 UNVERIFIED，而不是拿 Wikipedia 補洞。

### ✅ 可保留的高風險核心

- 2018：19 歲、120 萬、國二起拍、當時台灣最年輕、題材轉變、先機與包袱引語、漫畫夢。
- 2023：《口袋奇兵》五段影片、草率接案、撤廣告、加錢拒絕、下架引語。
- 2024 司法：119 人、1,000 萬餘元、83／36、不得易科 5 年＋另 1 年 8 月得易科。
- 2024-12-28 副頻道百萬問答 metadata。
- 2022-05-28 蘿倫 Q&A metadata，以及三天／無告白／四年半的 Newtalk 整理。
- 2025-12-13 新家影片的標題、頻道、公開狀態；正文沒有越界推定所有權。

## Findings（給主筆的最小修補序）

1. 先換 `[^2]` URL：`48444` → `49685`。
2. 把「案件曝光隔天」改為「案件曝光後／當天」。
3. 為「他依然是我哥哥不會變」補同日鏡週刊 exact source，或改間接敘述。
4. 在沒有正式 DOB source 前刪「二十六歲／二十七歲」，改為「六年後／七年後」最乾淨。
5. 統一「十四年」為「逾十三年」或「跨越十四個曆年」。
6. 本名若保留，補正式可追溯來源；不要讓 [^1] 假裝承載它。

若依以上 1-5 修補，核心故事與 9 個腳註架構可達 ship-safe；目前因 DEAD + HARD 未處置，依 pipeline hard gate 不應標全 PASS。

## 引語庫（本輪逐字結果）

- ✅ 「我會成功是因為我是最剛開始做的，說實力、我也沒什麼實力，但是我就是比較早抓到先機。」— https://news.housefun.com.tw/news/article/196239205065.html
- ✅ 「訂閱低什麼都敢拍，訂閱高會有一定的包袱，不敢拍很無聊、很爛的東西。」— https://news.housefun.com.tw/news/article/196239205065.html
- ✅ 「我想當個漫畫家，雖然畫畫沒有到很強，但我很喜歡畫畫。」— https://news.housefun.com.tw/news/article/196239205065.html
- ✅ 「我當時覺得還蠻容易做的就草率接下。」— https://newtalk.tw/news/view/2023-11-03/895065
- ✅ 「應該在那個時候就讓廣告商下架我的影片。」— https://newtalk.tw/news/view/2023-11-03/895065
- ✅ 「一時發生太多事情，我真的很累了。」— https://news.tvbs.com.tw/entertainment/1611575
- ⚠️ 「沒有要和小玉切割，他依然是我哥哥不會變」— 正文 footnote TVBS 無完整 Ctrl-F；exact 可見 https://www.mirrormedia.mg/story/20211018edi042

## Negative findings／沒找到

- 沒在九個正文 footnote 找到尊的正式 DOB；因此 26／27 歲不能由本輪來源鏈推出。
- 沒在 [^1] 找到「朱玉恩」；本名不能由該訪問承載。
- 沒在 TVBS HTML 找到完整「沒有要和小玉切割，他依然是我哥哥不會變」；只找到不切割的轉述與其他原句。
- 沒找到「案件曝光隔天」的依據；相反，TVBS 時間戳支持同日。
- 沒找到 `[^2]` 可用內容；它是明確 404，而非 403／暫時阻擋。
- YouTube 三支核心片沒有可下載官方字幕；本輪只把 metadata／標題當一手來源，不虛構時間碼。
- 沒找到新家所有權、房價、首購的可靠來源；正文正確地沒有做這些 claim。
- 沒把即時訂閱數、觀看數或留言數寫進驗證結果，避免數值隨平台變動造成 drift。

## 質地素材／給 writer

- 最穩的時間替代語：主頻道百萬「十九歲」有訪問明載；副頻道可寫「六年後」；新家可寫「又一年後」。這樣不需要 DOB，也保留成年時間感。
- 最穩的跨度語：「從約 2012 年的舊片，到 2025 年底的新家，公開影像橫跨逾十三年／十四個曆年。」
- 家屬回應最安全組合：先寫同日發文，再分開兩層——不否認兄弟關係（用 exact source）／哥哥做錯應自行承擔（TVBS exact）。
- 司法段落已經做得克制：5 年與 1 年 8 月分列，沒有誤加總；應維持。
- 新家段落的「只寫新家、不推所有權」是本篇最好的 source-boundary，可當其他 People 條目的示範。

## Final gate

**PASS/SOFT/HARD/DEAD summary：60 / 6 / 5 / 1。**

- URL gate：FAIL（1 DEAD）。
- 每 footnote 四維 gate：FAIL（[^2] 全 N；[^5]/[^7]/[^8] 局部 claim mismatch）。
- 直接引語 gate：FAIL（1 footnote-specific verbatim mismatch；另有可補 exact source）。
- 算術 gate：PASS for judicial numbers；SOFT/HARD for跨度與年齡 base。
- 時序 gate：FAIL（「曝光隔天」）。
- 文章核心主脊：大致可信，沒有發現司法數字、核心業配引語或官方影片日期的系統性幻覺。
- 最終 disposition：**CONDITIONAL FAIL，修完列出的 DEAD/HARD 後可重跑 Quick audit。**
