---
title: 'TRANSLATION-de'
description: 'Taiwan.md 德文翻譯主權詞表 — 台灣/中華民國稱呼、政治人物羅馬化、二二八/戒嚴等歷史敏感詞、PRC 編碼詞替換表'
type: 'editorial-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-09-05
last_session: '2026-09-05-de-birth-checklist-stage4'
sister_docs:
  - 'TRANSLATION-en.md'
  - 'TRANSLATION-ru.md'
  - 'TRANSLATION-ar.md'
upstream_canonical:
  - '../EDITORIAL.md'
  - '../TERMINOLOGY.md'
  - '../../pipelines/TRANSLATION-PIPELINE.md'
  - '../../pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md'
  - '../../pipelines/LANGUAGE-BIRTH-CHECKLIST.md'
research_evidence: '本卷詞表以本 session（2026-09-05）即時查證 German Wikipedia（Chinesisch Taipeh／Taiwan (Provinz)／Zwischenfall vom 28. Februar 1947／Chiang Kai-shek）+ Übermedien（Klaus Bardenhagen 對 dpa/FAZ/Die Welt「abtrünnige Provinz」用法的媒體批評，2019）+ Tagesspiegel（對「Wiedervereinigung」框架的評論）為主，交叉對照 knowledge/de/ 既有 84 篇語料實測（Peking／Festland 兩詞的真實出現，見 §6）。與 ru/ar 誕生時「knowledge/ 尚不存在、全靠假設情境」不同——de 出生時語料已在，§2/§6 引用的是真實已上線譯文，不是假設例句。'
audience: 'translator (human + AI)'
---

# TRANSLATION-de — Taiwan.md 德文翻譯主權詞表

> 每次翻譯前先讀。德文與英文同屬拉丁字母、且台灣官方羅馬化（Wade-Giles／護照拼音）本來就是拉丁字母，所以德文翻譯**不像俄文/阿拉伯文需要整套獨立音譯系統**——人名/地名絕大多數直接沿用英文既有羅馬化形式（Chiang Kai-shek、Tsai Ing-wen、Taipei 等），這是 de 與 ru/ar 出生檔案結構上最大的差異，也是本檔篇幅遠比 TRANSLATION-ru.md 精簡的原因。**真正的風險不在音譯，在框架詞**——德語媒體與中國官方新聞社（新華社/CRI／中國大使館官方稿）都直接用德文發稿，PRC 框架用語滲透路徑跟 ru 類似，只是載體是「德語為母語的中國官媒編輯」而非「立場親近的第三國官媒」。

## TL;DR — 5 條最高優先原則

1. **台灣不是「abtrünnige Provinz」（叛離的省份）**。德國媒體觀察者 Klaus Bardenhagen 在 Übermedien 上直接點名 dpa（德新社）、FAZ（法蘭克福匯報）、Die Welt 慣用此詞，並指出這個詞**連中國官方都不用**——北京官方說法是「不可分割的一部分」（unabtrennbarer Bestandteil），「abtrünnige Provinz」其實源自 1982 年一篇紐約時報報導的英文 "renegade province"，是西方媒體自己發明後以訛傳訛的詞，卻反而幫中國宣傳背書。Taiwan.md 的德文聲音不用這個詞。
2. **人名羅馬化：直接沿用英文/Wade-Giles 既有形式，不要另建德文音譯系統**。German Wikipedia 對蔣介石的條目標題就是「Chiang Kai-shek」（德文異體「Tschiang Kai-schek」存在但非主要形式）——這跟俄文必須整套改用 Cyrillic 音譯（Чан Кайши）結構上不同。person-fidelity-check.py 的羅馬化 regex 因此不需要德文專屬變體，但**張冠李戴風險依然存在**（蔣介石 1975 年已逝 vs 蔣經國 1988 年才逝世 vs 蔣經國 1987 年解嚴，同一批出生戰役教訓對德文一樣適用）。
3. **中華台北（Chinesisch Taipeh）只在奧運/國際體育/APEC 語境使用**（German Wikipedia 條目「Chinesisch Taipeh」確認為 IOC 構造出的專用詞），德文正文敘事中不可當「台灣」的隨手替代詞。
4. **統一（PRC 語境）→ 用 Vereinigung，不用 Wiedervereinigung**——「Wiedervereinigung」（重新統一）預設了台灣與中國曾經統一過，是北京框架；Tagesspiegel 一篇評論標題本身就在批評「中國要求德國協助『Wiedervereinigung』」是「厚顏無恥的歷史扭曲」（dreiste Geschichtsverzerrung）。直接引用北京官方說法時保留「Wiedervereinigung」並註明是誰在說，Taiwan.md 自己敘事一律用「Vereinigung」或改寫成「北京要求的統一」。
5. **北京可用「Peking」——這不是主權問題，是德文自己的慣用外來語**。德文長期用「Peking」指北京（跟英文「Beijing」並存，「Peking-Universität」「Pekingoper」等複合詞常見），knowledge/de/ 既有 84 篇語料實測 11 篇使用「Peking」，這是合法德文用詞不是翻譯錯誤——但「台灣的地方被譯成北京」（幻覺式地點遷移，出生戰役 vi 版踩過的坑）依然是主權紅線，跟詞彙本身合法與否是兩回事，見 §6 geo-fidelity 說明。

## 1. 國名/地區稱呼

| 中文來源     | 建議德文                                              | 使用時機                       | 禁用                                                                          | 備註                                                                                                                                  |
| ------------ | ------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| 台灣         | **Taiwan**                                              | 預設，任何語境                 | `Taiwan, China`、`Provinz Taiwan`、`abtrünnige Provinz`（見 TL;DR #1）        | Taiwan.md 一律把台灣寫成國家/民主政體，不寫成「地區」                                                                                |
| 中華民國     | **Republik China (Taiwan)**                             | 憲政/正式/國際法語境           | 裸「Republik China」不加註——會跟 1912–1949 的大陸時期中國混淆              | 台灣自己的官方德文出版品（駐德代表處）採此格式                                                                                        |
| 中華台北     | **Chinesisch Taipeh**                                   | 只限奧運／國際體育／APEC／WHO 語境 | 當作「台灣」的隨手替代詞用在非體育語境                                        | 確認：German Wikipedia「Chinesisch Taipeh」條目——IOC 構造詞，1981 年起沿用                                                            |
| 兩岸         | **beide Seiten der Taiwanstraße**                       | 台灣—中國政治關係               | `Landsleute auf beiden Seiten der Straße`（暗示血緣一家的北京框架）           | 不預設海峽兩岸是同一家人                                                                                                              |
| 中國大陸     | **das chinesische Festland** / **Festlandchina**        | 明確與台灣/香港對照時           | 當「中國」的隨手同義詞（沒有對照語境時直接寫 China 即可）                     | 語料實測：knowledge/de/ 既有 84 篇中 9 篇用 Festland／Festlandchina 表達 1949 遷台或大陸/港/台三地語境，是正常德文譯法（見 TL;DR #5） |
| 中國         | **China** / **die Volksrepublik China (VR China)**      | 指稱中華人民共和國政府/國家     | —                                                                              | 需要跟中華民國/台灣明確區分時用全稱 VR China                                                                                          |
| 台灣海峽     | **die Taiwanstraße**                                    | 地理                            | —                                                                              | 標準詞                                                                                                                                |

## 2. 政治人物羅馬化

德文人名羅馬化的核心原則：**沿用國際通用的英文/Wade-Giles 拼法，不要另建音譯系統**（跟 §TL;DR #2 同理）。下表沿用 `person-fidelity-check.py` 已收錄、風險最高的總統群，供翻譯時核對——**張冠李戴陷阱跟語言無關，任何語言的翻譯模型都可能把這些人名互換**：

| 漢字            | Taiwan.md（de）                          | 任期/身份                                    | 陷阱提醒                                                                                     |
| --------------- | ------------------------------------------ | --------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 蔣介石 / 蔣中正 | **Chiang Kai-shek**                        | 1950–1975 在台總統，1975 年逝世               | **陷阱**：不要跟兒子蔣經國搞混——出生戰役（2026-07-18）四語同時踩過這個坑                     |
| 蔣經國          | **Chiang Ching-kuo**                       | 1978–1988 總統，1987 年解嚴，1988 年逝世      | 跟父親蔣介石是兩個人，兩人拼法英文本來就不同（Kai-shek vs Ching-kuo），德文沿用同一組拼法即可 |
| 李登輝          | **Lee Teng-hui**                           | 1988–2000，首次總統直選（1996）               |                                                                                                   |
| 陳水扁          | **Chen Shui-bian**                         | 2000–2008，美麗島事件辯護律師出身             | 不要跟蔡英文/賴清德混淆——出生戰役曾在 id 版把陳水扁譯成蔡英文                               |
| 馬英九          | **Ma Ying-jeou**                           | 2008–2016                                     |                                                                                                   |
| 蔡英文          | **Tsai Ing-wen**                           | 2016–2024，首位女性總統                       |                                                                                                   |
| 賴清德          | **Lai Ching-te**（也作 William Lai）       | 2024 現任總統                                 | 不要跟蔡英文混淆——出生戰役曾在 tsmc 相關文把賴清德譯成蔡英文                                |
| 施明德          | **Shih Ming-teh**                          | 美麗島事件受刑人，前民進黨主席                 |                                                                                                   |

**技術/文化界國際知名人物**：直接用國際通用拼法，德文語境不需要另建拼音（黃仁勳 → Jensen Huang，張忠謀 → Morris Chang，郭台銘 → Terry Gou，唐鳳 → Audry Tang）。

## 3. 地名羅馬化

同 §2 原則，德文地名沿用英文既有羅馬化，**唯一例外是「北京」可用德文自己的慣用外來語「Peking」**（見 TL;DR #5，跟主權判定無關，是純粹的德文詞彙選擇）：

| 漢字 | Taiwan.md（de） | 備註 |
| ---- | ------------------ | ------ |
| 台北 | **Taipeh**（也作 Taipei） | 兩種拼法德文語料都有，Taipeh 較常見於德語新聞 |
| 高雄 | **Kaohsiung** | |
| 台中 | **Taichung** | |
| 台南 | **Tainan** | |
| 新竹 | **Hsinchu** | |
| 花蓮 | **Hualien** | |
| 金門 | **Kinmen** | |
| 綠島 | **Grüne Insel**（Lyudao／Ludao） | 白色恐怖監獄所在地，德文常意譯 |
| 北京 | **Peking** 或 **Beijing** | 兩者德文都合法（見 TL;DR #5）；「台灣本島」（相對離島）不要跟北京混——geo-fidelity-check.py 已對此設豁免（見 §6） |
| 上海 | **Shanghai** | 德文沿用同拼法，無 Peking 式異體 |

## 4. 政治/歷史敏感詞

| 漢字         | Taiwan.md（de）                                         | 備註                                                                                                              |
| ------------ | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 二二八事件   | **der Zwischenfall vom 28. Februar 1947**（also 228 Massaker） | 確認：German Wikipedia 條目標題「Zwischenfall vom 28. Februar 1947」；口語/媒體也用「228 Massaker」（Deutsch-Taiwanische Gesellschaft 用法） |
| 白色恐怖     | **der Weiße Terror**                                        | 大寫起首作為時代專有名詞（1947–1987）                                                                              |
| 戒嚴         | **das Kriegsrecht**                                         | 1949–1987，38 年又 56 天                                                                                          |
| 解嚴         | **die Aufhebung des Kriegsrechts**                          |                                                                                                                       |
| 本省人       | **Benshengren**＋首次出現加註「1945 年前已移居台灣者後代」  | 音譯＋首次出現加註說明                                                                                            |
| 外省人       | **Waishengren**＋首次出現加註「1945–1949 年隨國民黨遷台者」 |                                                                                                                       |
| 日治時期     | **die japanische Kolonialzeit**（1895–1945）                | 避免用「japanische Besatzung」（佔領）——會讓讀者以為是短期軍事佔領而非半世紀殖民統治                              |
| 統一         | **Vereinigung**（自己敘事）／引用北京官方時保留原詞並註明出處 | 見 TL;DR #4，禁止不加註直接用「Wiedervereinigung」                                                                |
| 原住民       | **die indigenen Völker Taiwans** / **die Ureinwohner Taiwans** |                                                                                                                       |
| 國民黨       | **Kuomintang (KMT)**                                        |                                                                                                                       |
| 民進黨       | **Demokratische Fortschrittspartei (DPP)**                  |                                                                                                                       |
| 台灣民眾黨   | **Taiwanische Volkspartei (TPP)**                            |                                                                                                                       |
| 立法院       | **Legislativ-Yuan**                                         |                                                                                                                       |
| 行政院       | **Exekutiv-Yuan**                                            |                                                                                                                       |
| 總統         | **Präsident / Präsidentin (der Republik China, Taiwan)**    |                                                                                                                       |

## 5. 文化詞（簡表）

- 珍珠奶茶 → **Bubble Tea**（德文已完全借用英文詞，無需另譯）
- 夜市 → **Nachtmarkt**
- 小吃 → **Snacks** / **taiwanesische Straßenküche**
- 媽祖 → **Mazu**（海神信仰，首次出現加註）
- 農曆新年 → **Mondneujahr** / **das chinesische Neujahrsfest**（避免只用後者當唯一形式——農曆新年不是「中國的」專屬節日）

## 6. PRC 編碼詞替換表（sovereignty-avoid lexicon）

| PRC 編碼詞                                                        | Taiwan.md 替換                                                    | 嚴重度   | 例外                                     | 出處                                                                                                                    |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `abtrünnige Provinz`（叛離的省份）                                  | **Taiwan**                                                            | critical | 專文討論這個詞本身的來源時                 | Klaus Bardenhagen, Übermedien, 「abtrünnige Provinz」—— 指出 dpa／FAZ／Die Welt 慣用此詞，詞源實為 1982 年紐約時報 "renegade province"，中國官方自己都不用這個詞 |
| `Taiwan, China`                                                     | **Taiwan**                                                            | critical | —                                          | ISO 3166 爭議條目脈絡下的中性討論才保留                                                                                    |
| `Provinz Taiwan` / `chinesische Provinz Taiwan`                     | **Taiwan**                                                            | critical | 討論 German Wikipedia「Taiwan (Provinz)」條目本身、或討論 ROC 自己已虛級化的省制時 | German Wikipedia 條目「Taiwan (Provinz)」不加註直接沿用此框架——讀時要批判性看待，不要照抄                                 |
| `unabtrennbarer Bestandteil (Chinas)`（不可分割的一部分）           | 改寫為北京官方立場並註明出處，不作為敘事事實                          | critical | 直接引用中國官方聲明                       | 北京官方原話（見上，中國大使館德文稿常用）                                                                                |
| `Wiedervereinigung`（重新統一，無出處逕自使用）                     | **Vereinigung**（中性）或明確標「北京要求的 Wiedervereinigung」        | high     | 直接引用北京/國台辦聲明並加註出處           | 見 TL;DR #4；Tagesspiegel 評論明確點名此框架是「dreiste Geschichtsverzerrung」                                            |
| `Chinesisch Taipeh` 用於非體育語境（當台灣的隨手替代詞）             | **Taiwan**                                                            | high     | 奧運/APEC/WHO 等真正的體育或該類國際組織語境 | 見 §1；German Wikipedia 確認此詞是 IOC 專用構造詞，範圍不可外溢                                                            |
| `taiwanesische Behörden` / `Behörden in Taipeh`（矮化為「當局」而非「政府」） | **die taiwanesische Regierung** / **die Regierung von Präsident(in) X** | medium   | —                                          | 跟 vi/hi/ru 版本記錄的同一種「當局」矮化框架同構                                                                          |
| `Separatisten`（分離主義者，無出處中性描述台獨支持者）              | **Befürworter der taiwanesischen Unabhängigkeit** / 直接寫政黨/人名     | medium   | 直接引用中國官方聲明並加註出處              | 標準北京框架，跟其他語言版本一致                                                                                          |

**幾何/主權保真補充**（geo-fidelity-check.py 已內建，見 `scripts/tools/lang-sync/geo-fidelity-check.py`）：「Peking」「Festland」在德文都是合法詞（見 TL;DR #5），但下列兩種情況仍會被 gate 攔下人審——(1) zh 源完全沒提北京/大陸，德文卻冒出來（幻覺式地點遷移，跟語言無關的紅線）；(2) 「taiwanesisches Festland」（台灣本島，相對離島如綠島）跟「Festland」／「Festlandchina」（中國大陸）是德文裡完全不同的兩個意思，翻譯或校對時不要混淆。

---

## 已知假陽性家族（cjk-leak-check.py，2026-09-05 出生 QA 實測）

德文標準引號是「„…"」（低位開引號＋高位收引號），跟中文「「」」/《》不同碼位——既有 `LEGIT_ZH_SPANS` 豁免清單只認中文書名號/引號/半形括號，**不含德文引號**。84 篇既有語料實測：作品名/口號/政策暱稱用「„…"」包住中文原文時（如 „護國神山"「一例一休"「民主萬歲"），4+ 連續漢字會被判定洩漏但其實是合法的原文標題引用。本次出生 session 判斷這是**通用（跨語言）的既有工具限制，不是 de 專屬缺口**，依 LANGUAGE-BIRTH-CHECKLIST 慣例「擋下的不自動修」原則未動 `cjk-leak-check.py` 的豁免清單——留給後續 session 評估是否該幫全部語言加德文引號豁免（QA 報告 `reports/babel/de-birth-qa-2026-09-05.md` §Stage 3 已列出全部 15 個受影響檔案）。

---

_v1.0 | 2026-09-05 — de 出生 Stage 4 主權詞表首版。與 TRANSLATION-ru.md/TRANSLATION-ar.md 出生時「knowledge/ 尚不存在、例句全靠假設」不同，本檔撰寫時 knowledge/de/ 已有 84 篇 tboydar 貢獻的真實譯文，§2/§3/§6 的 Peking／Festland 條目直接來自對既有語料的 grep 實測，不是推測。真人來源：German Wikipedia（Chinesisch Taipeh／Taiwan (Provinz)／Zwischenfall vom 28. Februar 1947／Chiang Kai-shek）+ Übermedien（Klaus Bardenhagen「abtrünnige Provinz」媒體批評）+ Tagesspiegel（Wiedervereinigung 框架評論），本 session（2026-09-05）即時 WebSearch/WebFetch 查證。範圍依哲宇 directive 定在 20–30 條核心詞（非 TRANSLATION-ru.md 全 15 節篇幅），§1/§2/§3/§6 對齊 `openrouter-translate.py` 的 `load_lang_guide_sections()` 自動抽取格式（後續若擴充篇幅，章節編號不可移動）。_
