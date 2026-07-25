# 裝甲輸入前後處理層 A/B 實測報告

> 2026-07-26｜哲宇 directive：「前處理預防 drift，預防勝於治療」
> 實作：`scripts/tools/lang-sync/translate.py` `--armor` 旗標
> 資料：`/tmp/armor-ab/`（不進 knowledge/，本報告是唯一交付物）

## 一、設計回顧

單次模型呼叫的整篇式架構不變（2026-07-25 兩引擎裁決：整篇式贏過
`structured-translate.py` 的分段多次 call 架構）。這次改的是**輸入本身**——四個
變換卸掉模型會弄壞的東西，翻譯完再用工具機械組回去：

1. **Frontmatter 卸甲**：只把 `title`/`description`/`tags` 以純文字行
   （`TITLE: …` / `DESC: …` / `TAGS: a, b, c`）送進 prompt；passthrough 欄位
   （同源 `verify-translation.py` 的 `PASSTHROUGH` 清單）與
   `translatedFrom`/`sourceCommitSha`/… 全部工具端機械組裝，模型完全看不到。
2. **URL token 化**：body（含腳註定義行）內所有 URL 換成 `⟦U1⟧`…`⟦Un⟧`，回傳後
   逐一還原並驗證每個 token 恰好出現一次——缺失或重複即該篇 fail，報 token 編號。
3. **保留區預標註**：掃「」『』《》〈〉span（同源 `cjk-leak-check.py` 的
   `LEGIT_ZH_SPANS`），在指示區聲明「這些保留原文，其餘一律翻譯」，不改 body。
4. **Prompt 減負**：動態抽 `TRANSLATION-<lang>.md` 的 TL;DR + 全文任何
   `### ⚠️` 警告子區塊（人名填空型警告等高風險提醒常掛在這類標題下）。

## 二、方法

- 12 篇 zh 來源文章，腳註數 ≥ 10（實際選用 10–12 條），vi/ar 各 6 篇，涵蓋
  Culture/History/People/Technology/Art/Food/Society/Economy 8 個分類。
- 同一 backend：`openrouter:nvidia/nemotron-3-ultra-550b-a55b:free`（既有
  key 輪替邏輯），armor on/off 各跑一遍 = 24 次真實模型呼叫，全部前景序列執行。
- 每篇輸出到 `/tmp/armor-ab/<lang>/<off|on>/<Category>/<slug>.md`，逐篇跑
  `verify-translation.py` / `cjk-leak-check.py`（顯式傳 `lang=`）/
  `article-health.py --profile=pre-commit`。
- **方法論修正**：第一輪 `verify-translation.py`／`article-health.py` 用路徑
  推斷語言，`/tmp/armor-ab/<lang>/…` 這個路徑形狀沒有 `knowledge/<lang>/`
  相鄰兩段，兩支工具都退化成預設語言（en / zh-TW）——`article-health` 因此對
  vi/ar 譯文誤套 zh-TW 全形標點規則，灌出不存在的 hard-fail。發現後把每個輸出
  複製到 `knowledge/<lang>/<Category>/` 形狀的路徑重跑兩支工具（`cjk-leak-check`
  呼叫時本來就顯式傳 `lang=`，不受影響）。本報告數字都是修正後版本。

## 三、逐篇對照表

| lang | 文章                                    | prompt 字元（off→on） | 縮減% | 耗時 s（off→on） | verify FAIL（off→on） | verify WARN（off→on） | cjk-leak hits（off→on） | health hard（off→on） |
| ---- | --------------------------------------- | --------------------: | ----: | ---------------: | :-------------------: | :-------------------: | ----------------------: | :-------------------: |
| vi   | hakka-culture-and-language              |           21819→11651 | 46.6% |      144.5→109.6 |          1→1          |          2→1          |               51→**19** |          0→0          |
| vi   | budaixi-glove-puppetry                  |            20302→9999 | 50.7% |       110.2→57.9 |          1→1          |          1→1          |              42→**132** |          0→0          |
| vi   | mudan-incident-1874                     |            19705→9514 | 51.7% |       139.3→51.2 |          1→0          |          1→1          |              17→**145** |          0→0          |
| vi   | hsu-chia-ying                           |           21751→11633 | 46.5% |      102.6→410.3 |          0→2          |          2→1          |               57→**27** |          0→0          |
| vi   | taiwan-robotics-industry                |           22816→13045 | 42.8% |        84.2→84.0 |          1→0          |          2→1          |                 309→309 |          0→0          |
| vi   | contemporary-taiwan-sculpture           |           23664→14198 | 40.0% |      235.6→105.5 |          1→0          |          1→1          |                 472→475 |          0→0          |
| ar   | taiwanese-hakka-banquet-cuisine         |            19930→9741 | 51.1% |      196.1→148.2 |          1→1          |          2→1          |               5→**209** |          0→0          |
| ar   | rural-education-in-taiwan               |           21817→11262 | 48.4% |       85.0→415.3 |          0→0          |          2→1          |                  5→21\* |          1→0          |
| ar   | liu-mingchuan                           |            19600→9280 | 52.7% |        77.9→97.5 |          0→1          |          1→1          |                 0→**7** |          0→0          |
| ar   | old-street-culture-commercial-districts |           23827→12820 | 46.2% |      114.7→129.0 |          0→0          |          2→1          |                     0→0 |          0→0          |
| ar   | three-foreigners-view-of-yiwei-1895     |           21942→11640 | 47.0% |        69.2→30.9 |          1→0          |          2→1          |                   0→0\* |          1→0          |
| ar   | industrial-transformation-and-upgrading |           25108→14788 | 41.1% |      268.8→129.2 |          1→0          |          1→1          |                0→**12** |          0→0          |

\* `rural-education-in-taiwan`／`three-foreigners-view-of-yiwei-1895` 是本次
唯二含 `[[X]]` wikilink 的來源文章，揭露一個實作漏洞（見四.3），修過後重跑
armor=on：`rural-education` cjk-leak 21→**9**，`three-foreigners` 0→1。表中數字是
修法前的原始 A/B 對照（跟其餘 22 筆同一版程式碼公平比較）；已 ship 的程式碼是
修法後版本。

**24/24 次 `translate_one()` 呼叫全部回報成功**（0 次因裝甲層本身而 fail——見
四.1），沒有任何一次因 armor 而整篇被工具判定不可用。

## 四、彙總與深度分析

### 4.1 URL 完整性——建構性保證，實測零失手

12 篇文章共標記 **200 個 URL**（markdown 連結 target + 裸 URL + 圖片路徑），12
次 armor=on 呼叫、200 個 token，**還原後 0 個缺失、0 個重複**。這是設計上就該
如此的結果（token 沒被模型認得出來要翻譯，唯一能出的錯是整個掉字或複製貼上兩次，
兩者都在還原時立刻可測），但實測把「設計上該如此」變成「跑過 12 篇都真的如此」。

副作用可觀察到一筆：`article-health` 的 `link-target`（連結路徑分類必須小寫）
hard-fail 出現 2 次，**都在 armor=off**（`rural-education-in-taiwan`、
`three-foreigners-view-of-yiwei-1895`，均為模型把 `/Culture/`／`/History/`
的大小寫改掉）。armor=on 版同樣的內部連結因為路徑整段被 token 保護，兩篇都是
0 hard-fail——armor 防的不只是外部引用 URL，連內部 wikilink 路徑的大小寫漂移
也一併防住。

### 4.2 Frontmatter 卸甲——兩個 fail 家族完全消滅

`verify-translation.py` 的 FAIL/WARN 依名稱拆開看（12 篇加總）：

| check                              |        off |         on | 說明                                                                                                         |
| ---------------------------------- | ---------: | ---------: | ------------------------------------------------------------------------------------------------------------ |
| **passthrough fields**             | **5 FAIL** | **0 FAIL** | category/date/author/readingTime/… 被模型憑空改寫——armor 完全消滅                                            |
| **no quoted scalar types**（WARN） | **7 WARN** | **0 WARN** | readingTime 被模型輸出成 `'11'` 而非 `11`、featured 輸出成 `'true'` 而非 `true` 這類型別漂移——armor 完全消滅 |
| frontmatter not untranslated       |     3 FAIL |     5 FAIL | title/description 殘留中文——armor 沒有改善，見 4.4                                                           |
| tags ASCII                         |     0 FAIL |     1 FAIL | 單一新增案例                                                                                                 |
| translation ratio（WARN）          |         12 |         12 | 兩側都是「verdict unclear」——量測工具在 `/tmp` 路徑下判不出裁決，非產品訊號，見六.1                          |

**passthrough fields** 與 **quoted scalar types** 這兩個 fail 家族，直接對應
2026-07-25 哲宇 directive 點名的「今天的三大 fail 家族」其中兩個（第三個是腳註
編號飄移，這次 armor 沒有處理腳註結構，維持整篇式不分段）。工具機械複製取代
模型手抄，兩個家族從有到無，是本次最乾淨的正向結果。

`frontmatter not untranslated`（title/description 殘留中文）armor 沒有改善，
原因合理：這條檢查測的是**模型翻譯 title/description 本身的完成度**，armor
的卸甲只改變「passthrough 欄位要不要送進 prompt」，title/description 依然是
模型要親自翻的兩個欄位，armor 沒有、也不打算改善模型翻這兩個欄位的專注度。

### 4.3 Wikilink 對照表遺漏——A/B 過程中發現並修補

第一輪跑完比對輸出時發現：`armor_pre()` 把非 armor 路徑原本會整包送進
prompt 的「manifest entry JSON」（含 `wikilink_targets` 對照表）連根拔掉，
只留下 frontmatter 卸甲要留的三個欄位——但 `wikilink_targets` 是**body 層**的
資訊，不在四個變換規格範圍內，被連坐拔除是實作時的範圍誤判，不是設計本意。

實測證據（`rural-education-in-taiwan`，來源含 4 個 `[[X]]` wikilink）：armor=off
正確把 `[[台灣少子化危機]]` 解析成「翻譯錨字 + 中文括號」或真連結；armor=on 版
`[[台灣少子化危機]]` 原封不動留在阿拉伯文正文中間，貢獻了該篇 cjk-leak 21 筆
命中裡的一大部分。

修法：在 `armor_pre()` 補回 wikilink 對照表（純文字行形式，不是完整 JSON），
system prompt 加一段解析規則。修完針對兩篇受影響文章重跑 armor=on 驗證：
`rural-education-in-taiwan` cjk-leak 21→**9**，`three-foreigners-view-of-yiwei-1895`
0→1（後者原本就乾淨，新增 1 筆是 wikilink 用 `[[gloss (原文)]]`
非標準格式殘留雙中括號的格式瑕疵，不是漏翻）。**已 ship 到 `translate.py`
的版本含這個修法**；表格裡的原始數字保留作為方法論記錄。

### 4.4 CJK-leak——armor 沒有整體改善，多篇明顯惡化

這是本次最需要誠實面對的發現，跟 directive 原本「URL 縮短 prompt→降截斷風險」
的假說方向不一致：

- **12 篇加總**：cjk-leak hits off=958，on=1356（armor **多**了 41%）。
- **逐篇方向**：armor 明顯**改善**的 2 篇（hakka-culture 51→19、hsu-chia-ying
  57→27）；armor 明顯**惡化**的 6 篇（budaixi 42→132、mudan-incident 17→145、
  hakka-banquet 5→209、rural-education 5→21、liu-mingchuan 0→7、
  industrial-transformation 0→12）；兩側同樣糟或同樣乾淨的 4 篇（taiwan-robotics
  309→309、contemporary-sculpture 472→475、old-street 0→0、three-foreigners 0→0）。

檢視惡化案例的實際輸出（如 `budaixi-glove-puppetry`）發現同一種模式：armor=on
版本只翻了開頭「30 秒概覽」區塊，**從第一個 `##` 小標題開始，body 剩餘 90% 是
zh-TW 原文一字不改**（連 token 都原樣照抄，token 還原沒有出錯，只是模型根本
沒有生成譯文，把 tokenized 輸入原樣複誦回來）。armor=off 版本則是**全篇都嘗試
翻譯**，殘留的是字詞級／子句級的中文碎片（如「催生了新工具」「等日本故事」
未翻），量體小很多。

**這個「翻到一半放棄、後半原樣照抄」的失敗模式在 armor=off 也存在**
（taiwan-robotics-industry、contemporary-taiwan-sculpture 兩篇兩側同樣嚴重），
說明它不是 armor 獨有的病，比較像是這顆 reasoning 模型
（`nemotron-3-ultra-550b-a55b`）在長 body 上的固有傾向。但 armor 沒有像
directive 假說預期的那樣抑制它——這次 12 篇的樣本甚至顯示相反方向（armor 開啟
時「放棄」發生的篇數更多）。

假說（未驗證，留給後續研究）：URL token 化縮短的是 prompt 的**輸入**字元數
（body 裡 URL 佔位置換成 5-6 字元 token），但需要模型**生成**的譯文字數（body
的敘事文字本身）沒有被壓縮——如果這顆 reasoning 模型的「放棄」跟輸出端 token
預算/耐心有關而非輸入端，armor 對這個特定失敗模式的槓桿本來就有限。四個變換裡
沒有一個是為了縮短「模型要生成的量」設計的。

### 4.5 耗時——armor 沒有更快，個案波動大

12 篇加總：off 1628.1s，on 1768.6s（armor **慢** 8.6%）。單篇耗時波動很大
（`hsu-chia-ying` armor=on 410.3s、`rural-education-in-taiwan` armor=on
415.3s，兩篇都遠高於同篇 armor=off 版本），跟前一節「放棄翻譯」的個案有重疊
但不完全對應（`taiwan-robotics-industry` 兩側同樣是 84s 左右，同樣嚴重放棄卻
沒有拖長耗時）。n=12、單次跑，這裡的耗時差異噪訊比訊號大，不建議下任何時間
效益的結論。

### 4.6 Article-health

12 篇加總：off hard=2／warn=2，on hard=0／warn=2。兩筆 hard-fail 都在 4.1
討論過的 `link-target` 大小寫案例，都在 armor=off。

## 五、結論

不是「armor 全贏」也不是「armor 沒用」，是**分層次的訊號**：

1. **Frontmatter 卸甲（變換 1）**：無條件推薦。passthrough 欄位漂移
   （5→0）與型別跳脫漂移（7→0）兩個 fail 家族完全消滅，24 次呼叫零副作用。這條
   單獨拆出來都值得 ship。
2. **URL token 化（變換 2）**：無條件推薦。200/200 token 零失手的建構性保證
   兌現，還額外防住了 wikilink 路徑大小寫漂移。它解決的是「URL 被改壞」這一類
   問題，這次樣本裡這類問題本來就少見（en/vi/ar 的模型通常不太敢動 URL 本身），
   所以帳面效益不誇張，但下修風險是真的，且沒有觀察到任何代價。
3. **保留區預標註（變換 3）**：本次樣本沒有看到針對性的正負訊號（LEGIT_ZH_SPANS
   本身設計是防止「這句該保留原文」被誤翻，不是防止「這段該翻譯的被漏翻」——
   兩者是不同問題，這次主要失敗模式是後者）。
4. **Prompt 減負（變換 4）**：達成 46.8% 的字元縮減，但**沒有**觀察到假說預期
   的「降截斷風險」效果——本次樣本裡 armor 的 body 完整度反而較差。

**Dispatcher 接線建議**：

- **可以現在就把「frontmatter 卸甲 + URL token 化」這兩層拆出來獨立生效**，
  不必等 body 完整度的問題解決——這兩層有清楚的正向數據且零觀察到的副作用。
  若要落地成獨立旗標而非跟「保留區＋prompt 減負」綁在一起的單一 `--armor`，
  是可以考慮的後續重構方向（本版先合併成一個旗標，符合 directive 原始需求）。
- **不建議現在把 `--armor` 設成 batch 模式預設值**——4.4 的 cjk-leak 惡化雖然
  可能是這顆模型的個性而非 armor 通病，但這次 12 篇單次跑的樣本不足以排除
  armor 是助燃劑的可能性，需要更大樣本（多篇 × 多次重跑控制 reasoning 模型
  的 run-to-run 變異）或換一顆非 reasoning 模型重驗證才能下場。
- **比 armor on/off 這個問題本身更急的發現**：`translate_one()` 現有 hard gate
  （frontmatter fence／footnote 數／output-language）**完全攔不住「翻一半、
  剩下原文照抄」這種失敗模式**——24 次呼叫裡有多篇這樣的輸出全部回報成功，
  cjk-leak-check 是唯一抓到它的工具，但目前不在 `translate_one()` 的落盤前
  hard gate 裡（是下游 batch/dispatcher 才會跑的獨立工具）。這個缺口跟 armor
  無關，兩側都受影響，建議下一步把 `cjk-leak-check.scan_file()` 的「body 未
  翻譯比例」訊號收編進 `translate_one()` 的落盤前 hard gate，而不是繼續讓
  半成品先落盤再靠下游巡邏抓。

## 六、已知限制

1. **translation ratio 檢查在 `/tmp` 路徑下失效**：`verify-translation.py` 的
   ratio-check 子行程對 12×2=24 篇全部回報「verdict unclear」，這是量測環境的
   限制（ratio-check.sh 依賴 REPO 相對路徑做別的判斷），不是產品訊號，兩側
   同樣受影響，不影響 A/B 比較的公平性。
2. **單次跑，無變異量測**：24 次呼叫都只跑一次，沒有重複 trial 估計同一顆
   reasoning 模型的 run-to-run 變異——4.4／4.5 觀察到的個案波動有多少是模型
   本身的隨機性、多少是 armor 造成的系統性差異，本次樣本無法拆開。
3. **wikilink 對照表補丁只在 2 篇受影響文章上做了 spot check**，沒有重跑全部
   12 篇——因為 22/24 筆完全不受這個修法影響（來源沒有 `[[X]]`），重驗證範圍
   已對應到真正受影響的子集。

## 七、實作位置

- `scripts/tools/lang-sync/translate.py`：`--armor` CLI 旗標（預設關）、
  `armor_pre()`／`armor_post()`／`_tokenize_urls()`／`_restore_urls()`／
  `_reserved_spans()`／`load_lang_guide_tldr()`，插在 `translate_one()` 的
  cascade 呼叫前後，既有 hard gate（frontmatter fence／footnote 數／
  output-language）對 armor 輸出原樣適用，未修改。
