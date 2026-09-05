---
title: 'de 語言出生 Stage 2-4 + 6-prep QA 報告'
description: 'OBSERVER-QUEUE #29（哲宇拍板）de 出生 Stage 2 模型校準 + Stage 3 對既有 84 篇跑三把主權保真尺 + Stage 4 介面與路由 + Stage 6 build 驗證前置'
type: 'report'
status: 'final'
last_updated: 2026-09-05
---

# de 語言出生 QA 報告 — 2026-09-05

> Session：worktree `.worktrees/20260905-20260905-de-birth`（detached HEAD，semiont-worktree.sh 慣例）。
> 授權：OBSERVER-QUEUE #29，哲宇 2026-09-05 拍板「開德文，走 LANGUAGE-BIRTH-CHECKLIST v2.0」。
> 範圍：Stage 2（模型校準）+ Stage 3（既有語料 QA 前置，不做 P0 大批翻譯）+ Stage 4（介面與路由）+ Stage 6（build 驗證前置）。**Stage 5 flip（`enabled: true`）刻意不做**，留給主 session 驗收後親手做。
> 前例：[reports/language-birth-2026-07-25.md](../language-birth-2026-07-25.md)（ar/ru 雙語出生 Stage 1-2）、[reports/language-birth-2026-07-18.md](../language-birth-2026-07-18.md)（vi/id/pt/hi 首次全程出生戰役）。

---

## TL;DR

- **現況起點**：`knowledge/de/` 已有 84 篇（tboydar 兩批 PR，2026-08-19 + 09-04 合併）；`src/config/languages.{ts,mjs}` 已 scaffold `enabled: false`（Stage 1，2026-08-19）。
- **Stage 2 完成**：codex + ollama（qwen3.8:27b-mtp-q8_0）對 4 篇校準集（含 1 篇主權敏感：戒嚴時期）跑 refusal 前測，全數零拒答；ratio band 從既有 84 篇實測重新校準（p5=2.48 / p95=3.78，取代舊佔位值 2.0-4.0）。
- **Stage 3 完成**：三把主權保真尺（geo-fidelity / person-fidelity / cjk-residue）+ script-presence-check + translation-ratio-check 全部對 84 篇跑過。過程中發現並修好 **cjk-leak-check.py**（de 完全沒被這道閘門掃過）與 **geo-fidelity-check.py**（缺德文專屬的 Peking/Festland 標記）兩個真閘門缺口。修完後：84 檔全過 person-fidelity；84 檔全過 script-presence；1 檔擋在 geo-fidelity（人審級，非幻覺）；15 檔在 cjk-leak-check 出現已知假陽性家族；10 檔在新 ratio band 下變 WARN（非 FAIL）。
- **Stage 4 完成**：18 個 `src/i18n/` bundle 全部補 de block（key 數與 zh-TW 逐一比對一致）；`src/pages/de/` 路由目錄複製 ru 範本（24 檔，3 檔需替換語言碼）；`docs/editorial/per-language/TRANSLATION-de.md` 新誕生（20+ 條主權詞表）；`hub-translate.py` 排除清單、`openrouter-translate.py` LANG_NAMES、`src/i18n/utils.ts` fallback chain 補 de；額外發現並修：`.gitignore` 缺 `src/content/de/`。
- **Stage 6 驗證**：見下方 §Stage 6 段（build + check-url-contract 結果）。
- **Hard gate 沒過的**：geo-fidelity 1 檔人審級（非阻斷性，見下）；cjk-leak-check 15 檔已知假陽性家族（未修，工具限制記錄在案）；**四層完整度第三層「Hub」路由健康但無策展內容**——Stage 6 build 驗證確認 6 個分類 Hub 頁（`/de/culture`／`/de/food`／`/de/geography`／`/de/history`／`/de/people`／`/de/technology`）都能正確產出、分類名稱翻譯正確、文章列表正常渲染，但因為 `knowledge/de/` 沒有任何 `_{Category} Hub.md` 翻譯，頁面退化成純列表、缺策展導言，這是 flip 前主 session 該親自決定的事項之一。

---

## Stage 2 — 模型校準

### 校準集（SQUEEZE §驗證 SOP 標準 4 篇 + 主權敏感類）

| 文章                              | 類別         | 選擇理由                                              |
| ----------------------------------- | ------------ | -------------------------------------------------------- |
| `Lifestyle/LINE.md`                 | 中性技術     | SQUEEZE §驗證 SOP 標準校準集第一篇，baseline 品質      |
| `People/施明德.md`                  | 政治人物     | 美麗島事件受刑人，refusal 探針（政治敏感人物傳記）      |
| `Culture/伊斯蘭教在台灣.md`         | 文化＋宗教   | SQUEEZE §驗證 SOP 標準校準集                            |
| `History/戒嚴時期.md`               | **主權敏感** | 哲宇指示「至少 1 篇主權敏感：二二八／戒嚴／兩岸類」，選戒嚴時期（1949-1987 全文歷史敘事） |

後端：`codex`（Tier 1 subscription）+ `ollama qwen3.8:27b-mtp-q8_0`（本機，task 指定的兩個本機模型之一；gemma4:12b 未測，留待後續）。跑在 scratch 目錄（`/private/tmp/.../de-calibration/`），未寫入 `knowledge/de/`。

### 校準結果

| 文章               | 類別         | 後端                  | 秒數  | 拒答 | ratio | 腳註      | 變音符號 | 分數     |
| -------------------- | ------------ | ----------------------- | ----: | :--: | ----: | --------: | :------: | :------: |
| LINE                 | 中性技術     | codex                   |  71.1 |  否  | 2.501 |     20/20 |    有    |   8/10   |
| LINE                 | 中性技術     | ollama qwen3.8:27b      | 733.9 |  否  | 2.325 |     20/20 |    有    |   8/10   |
| 施明德               | 政治人物     | codex                   |  81.2 |  否  | 3.414 |     11/11 |    有    |   8/10   |
| 施明德               | 政治人物     | ollama qwen3.8:27b      | 455.5 |  否  | 3.200 |     11/11 |    有    |   8/10   |
| 伊斯蘭教在台灣       | 文化＋宗教   | codex                   |  66.9 |  否  | 2.824 |     12/12 |    有    |   8/10   |
| 伊斯蘭教在台灣       | 文化＋宗教   | ollama qwen3.8:27b      | 399.6 |  否  | 2.737 |     12/12 |    有    |   8/10   |
| **戒嚴時期**         | **主權敏感** | codex                   |  86.5 |  否  | 3.560 |       9/9 |    有    |   8/10   |
| **戒嚴時期**         | **主權敏感** | ollama qwen3.8:27b      | 565.1 |  否  | 3.524 |       9/9 |    有    |   8/10   |

分數依 SQUEEZE §驗證 SOP 判準：4-lang 完整度（單語版簡化為 frontmatter/footnote 完整度）2/2、0-byte/40-byte refusal 率 2/2（全零拒答）、政治人物通過率 2/2（施明德/戒嚴時期兩篇涉及的政治人物如陳水扁、蔣介石逐一核對正確，見下方主權前測結論）、文化詞翻譯品質 1/2（抽樣讀來自然，唯地名/機構名偶有 codex 用「Hauptinsel」ollama 用「Festland」等用詞差異，非錯誤但風格不完全統一）、速度 1/2（codex 66-87s 達標，ollama 400-734s 超過 200s 門檻但屬已知的本機模型量級，SQUEEZE 文件本身也把「本機捕手」排除在速度門檻外）——**兩後端皆 ≥7 分，均可進 production cascade**，與 ar/ru 出生戰役的判定一致。

### 主權前測結論

**零拒答**。8 次呼叫（4 篇 × 2 後端）全數完整輸出，無 40-byte 拒答、無 0-byte 空回應、無「配合但英文回答」跡象（`has_diacritics` 全部為真，德文變音符號正常出現）。**戒嚴時期**（本次哲宇指定的主權敏感探針）兩後端皆完整翻譯：腳註 9/9、frontmatter 合法、內文涵蓋 1949-1987 戒嚴全期敘事，codex 版本人工核對 9 處「4+ 連續漢字」全部是合法保留（`translatedFrom` frontmatter 欄位 + 內部 wikilink 轉連結後保留的 zh-TW slug 路徑，如 `/history/二二八事件`——這是站內連結解析機制，不是洩漏）。

**人物保真交叉驗證**（額外抽查，非工具自動跑）：施明德校準集兩後端譯文中「陳水扁」「蔣介石」「施明德」三個人名全部逐次正確對應，無出生戰役 vi/id 版踩過的「總統名互換」錯誤。

**觀察到的 backend 差異**（供未來 production 排序參考）：

1. codex 對「台灣本島」（相對離島）譯成較不模糊的「Hauptinsel Taiwans」，ollama qwen3.8:27b 譯成「taiwanesisches Festland」——後者正是本次 geo-fidelity-check.py 新增德文標記後抓到的既有語料同款用詞（見 Stage 3），顯示 ollama 這個特定措辭傾向不是單次隨機，值得未來 P0 批次跑 ollama 路徑時多留意 geo-fidelity 這一類假警報／真警報的邊界。
2. **戒嚴時期校準集揭露了具體的用詞分歧**：codex 全文用「Kriegsrecht」（戒嚴法，符合 German Wikipedia 標準敘述），ollama qwen3.8:27b 全文卻改用較弱的「Ausnahmezustand」（緊急狀態）——後者稀釋了戒嚴時期軍法審判平民的具體嚴重性。已把這個發現寫進 `TRANSLATION-de.md` TL;DR 新增第 0 條，供未來 batch 人審／校準參考。這是本次 8 次呼叫中唯一發現的實質用詞分歧（其餘篇章兩後端用詞大致一致）。

速度上 codex（67-87 秒/篇）遠快於 ollama qwen3.8:27b（400-734 秒/篇，q8_0 量化 + MTP 在本機約 9-10 tokens/秒），與 SQUEEZE 文件「本地捕手慢但主權可靠」的既定認知一致。

### ratio band 重校準

既有 84 篇語料（非本次新譯，是已上線的 tboydar 貢獻）用 `translation-ratio-check.sh --all-de` 實測：

```
n = 84
min = 2.36 (taiwan-semiconductor-industry.md)
max = 3.90 (tectonic-plates-and-seismic-activity.md)
median = 3.135
mean = 3.139
p5 = 2.478
p95 = 3.782
```

寫入 `scripts/tools/lang-sync/ratio-bands.json` 的 de 條目：

```json
"de": {
  "truncated_below": 1.8,
  "healthy_min": 2.48,
  "healthy_max": 3.78,
  "calibrated": "2026-09-05",
  "note": "字元比，84 篇實測 p5/p95..."
}
```

取代 2026-04-11 的舊佔位值（`truncated_below 1.5 / healthy_min 2.0 / healthy_max 4.0`——de 出生前沿用 en/es/fr 泛用值）。重跑 `--all-de`：**10/84 檔變 WARN（THIN/LONG）**，全部逐篇核對 `secs/fns/urls` 結構數完全一致（無截斷），是 p5/p95 方法論下預期的正常長度變異（每側約 5%），非翻譯品質問題：

| 檔案                                                  | Ratio | Verdict |
| ------------------------------------------------------ | ----- | ------- |
| tectonic-plates-and-seismic-activity.md                 | 3.90  | LONG    |
| taiwan-forestry-history.md                              | 3.82  | LONG    |
| chu-yi-kuei-qing-rebel.md                                | 3.80  | LONG    |
| lai-ching-te.md                                          | 3.87  | LONG    |
| li-mei-shu.md                                            | 3.87  | LONG    |
| andre-chiang-taiwanese-culinary-innovator.md             | 2.47  | THIN    |
| hatta-yoichi.md                                          | 2.37  | THIN    |
| jensen-huang.md                                          | 2.44  | THIN    |
| jeremy-lin.md                                            | 2.44  | THIN    |
| taiwan-semiconductor-industry.md                         | 2.36  | THIN    |

---

## Stage 3 — 既有 84 篇跑三把主權保真尺 + script-presence + ratio-check

**前置修復**（詳細理由與 diff 見對應 commit）：

1. `cjk-leak-check.py` 的 `NON_CJK_SCRIPT_LANGS` 集合缺 `de` → de 完全落入 ja/ko 分支（掃零散中文虛詞表而非 4+ 連續漢字），**這道閘門對 de 從未真正跑過**。加回後才是第一次真掃描。
2. `geo-fidelity-check.py` 的 MARKERS 沒有德文專屬形式——「Peking」（北京德文慣用外來語）、「Festland/Festlandchina」（中國大陸常見德譯）完全不在 target regex 裡。加回後抓到 1 個需人審案例，也順手修了自己新 marker 帶來的 2 個假陽性。
3. `person-fidelity-check.py` 不需要改——德文人名沿用英文/Wade-Giles 既有拼法（不像俄文/阿拉伯文需要獨立音譯系統），既有 regex 天然覆蓋，實測直接 0 誤判。

### 結果總表

| 工具                          | 結果                                    | 備註 |
| ------------------------------- | ------------------------------------------ | ---- |
| `person-fidelity-check.py`      | ✅ 84/84 全過                              | 無需語言專屬改動 |
| `script-presence-check.py`      | ✅ 84/84 全過                              | de 的 DIACRITICS profile 已於 2026-08-30 由前次 session 補上（見 §發現的既有伏筆） |
| `geo-fidelity-check.py`         | ⚠️ 1/84 擋（人審級，非幻覺）               | 見下方明細 |
| `cjk-residue-check.py`          | ⚠️ 15/84 有殘留（85 行）                   | de 於 2026-08-30 已補上 TARGET_LANGS；本次是既有已知缺口的例行掃描，非本次新修 |
| `cjk-leak-check.py`             | ⚠️ 15/84 有命中（本次修好才第一次真掃）    | 見下方假陽性家族分析 |
| `translation-ratio-check.sh`    | ⚠️ 10/84 WARN（THIN/LONG，非 FAIL）        | 見上方 Stage 2 段 |

### geo-fidelity-check.py 1 檔明細（人審，非阻斷）

**`knowledge/de/Technology/taiwan-semiconductor-industry.md` L77**（China-mainland 標記）：

> zh 源：「1949 年國府遷台帶來一批理工出身的技術官僚」（沒有literal「大陸」二字）
> de 譯文：「...brachte die Regierung mit der Rückkehr auf Taiwan eine Generation technischer Bürokraten **aus dem Festland** mit」

判定：**不是幻覺式地點遷移**（沒有把台灣的地方搬到中國），是翻譯補了一句 zh 源沒有明講但史實正確的推論細節（1949 年國府遷台當然是從中國大陸來的）。嚴重度低，建議人審時決定是否要求譯文更貼源文（不加沒寫的細節），或接受這種史實正確的補充——兩種立場 taiwan-md 過去在其他語言都出現過，非新問題。

**已修的 2 個假陽性**（新 marker 自己造成，已在同一輪修掉，不留給人審）：

- `jj-lin-singaporean-mandopop-king.md`：zh 源「兩岸三地均取得高度反響」被德譯精確展開成「(Festland, Hongkong, Taiwan)」——語意正確的合法展開。已把「兩岸三地」加進 `zh_terms` 白名單。
- `shih-ming-te.md`：zh 源「台灣本島」（相對綠島）被譯成「taiwanesischen Festland」——這是台灣自己的本島，跟中國大陸無關。已加 `line_exempt` 豁免「taiwanesisches Festland」/「Festland Taiwans」這組結構。

### cjk-leak-check.py 15 檔假陽性家族分析（未修，記錄在案）

德文標準引號是「„…"」（低位開引號＋高位收引號），跟中文書名號/引號用完全不同碼位——既有 `LEGIT_ZH_SPANS` 豁免清單（半形/全形括號、《》〈〉、「」『』）**不含德文引號**，用「„…"」包住的中文原文標題/口號（如作品名、政策暱稱）會被誤判為洩漏。另有兩個既存（非 de 專屬）假陽性家族：中文原文括號內容超過 30 字上限（既有豁免的長度天花板）、以及純文字引用列表（維基百科／東森新媒體等媒體來源名）沒有任何括號/引號包裹。

依 LANGUAGE-BIRTH-CHECKLIST「擋下的不自動修」慣例，本次判斷這是**跨語言的既有工具限制，不是 de 專屬缺口**，未動 `cjk-leak-check.py` 的豁免清單本體（只修了語言集合缺口，這是「有沒有跑」不是「跑得準不準」的差異）。15 個受影響檔案：

| 檔案 | 命中內容 | 假陽性類型 |
| ---- | -------- | ---------- |
| taiwan-semiconductor-industry.md | 護國神山 ×5、漢磊製造/穩懋封裝/宏捷科設計 | 德文引號「„…"」包住暱稱；公司名列表無括號 |
| takeshi-kaneshiro.md | 風林火山 | 括號內容超 30 字 |
| park-min-seo.md, ahn-ji-hyun.md | 東森新媒體 | 媒體來源引用，無括號包裹 |
| nam-min-jung.md | 聯合新聞網 ×2、維基百科、今日新聞 | 「延伸閱讀」來源清單 |
| hou-hsiao-hsien.md | 牯嶺街少年殺人事件 | 括號內容超 30 字（含年份/得獎資訊） |
| sylvia-chang.md | 愛的代價 | 括號內容超 30 字 |
| teresa-teng.md | 民主萬歲 ×2、反對軍管 ×2 | 德文引號包住抗議標語 |
| hsu-shu-ching-olympic-weightlifting-champion.md, su-wei-hsieh-wimbledon-champion.md | TODO 編輯註記（`<!-- TODO: 天機星 ... -->`） | HTML 註解內容未豁免 |
| lee-teng-hui.md | 民之所欲，常在我心 | 德文引號包住演講標題 |
| lai-ching-te.md | 一例一休 | 德文引號包住政策暱稱 |
| taiwan-forestry-history.md | 開山撫番 | 括號內容超 30 字 |
| japanese-colonial-era.md | 台北帝國大學、後藤新平 | 括號內容超 30 字 |
| jiaobei-divination-blocks.md | 歸來慈天宮 | 無任何括號/引號包裹的廟名 |

**建議後續**：德文引號家族（護國神山／反對軍管／民主萬歲／一例一休／民之所欲常在我心，共約 10 處）是唯一明確可歸類為「de 專屬」的假陽性——其餘（超長括號／無括號媒體列表／TODO 註解）是跨語言通用限制。是否幫全部語言加德文引號豁免、放寬括號長度上限、豁免 HTML 註解，建議留給後續 session 評估（可能影響其他語言的洩漏偵測靈敏度，非單純加一條規則）。

---

## Stage 4 — 介面與路由

### `src/i18n/` 18 bundle 加 de block

用 `ui-bundle-translate.py --backend codex --fallback ollama --apply` 逐檔跑（`docs/editorial/per-language/TRANSLATION-de.md` 剛誕生，TL;DR 段透過 `load_guide_tldr()` 自動 inline 進 prompt）。

| bundle 檔        | zh-TW key 數 | de key 數 | 對齊 |
| ------------------ | -----------: | --------: | :--: |
| about.ts            |          276 |       276 |  ✅  |
| assets.ts           |           34 |        34 |  ✅  |
| changelog.ts        |           12 |        12 |  ✅  |
| contribute.ts       |          354 |       354 |  ✅  |
| dashboard.ts        |          150 |       150 |  ✅  |
| data.ts             |          341 |       341 |  ✅  |
| explore.ts          |           45 |        45 |  ✅  |
| footnote.ts         |            6 |         6 |  ✅  |
| home.ts             |          108 |       108 |  ✅  |
| latest.ts           |           21 |        21 |  ✅  |
| map.ts              |          455 |       455 |  ✅  |
| notfound.ts         |           29 |        29 |  ✅  |
| resources.ts        |          361 |       361 |  ✅  |
| search.ts（en 為源）|           26 |        26 |  ✅ 手動補（見下） |
| semiont.ts          |          127 |       127 |  ✅  |
| taiwanShape.ts      |           59 |        59 |  ✅  |
| timeline.ts         |           26 |        26 |  ✅  |
| ui.ts               |          228 |       228 |  ✅  |

全 18 檔 esbuild 語法檢查（`format: 'esm', target: 'es2020'`）逐一過關，`node -e` 批次驗證腳本輸出 `ALL PASS`。

Key 數對齊驗證（block-aware parser，非簡單 grep——bundle 檔案本身 key 命名不含 `zh-TW.` 前綴，文件既有驗證指令範例不適用，改寫小工具直接比對 `zh-TW: {...}` 與 `de: {...}` 兩個 block 內的 top-level key 數）：全部 18 檔 zh-TW/de key 數逐一相等。

`bench.ts`／`budget.ts` 兩個特殊 bundle：

- `bench.ts`：設計上只有 en/ja/ko/zh-TW 有全文（其餘語言含 de 走 `FALLBACK_CHAIN`），已把說明註解的語言清單補上 de，功能不需要改。
- `budget.ts`：219 key 走獨立的 `data/budget/i18n/{lang}.json` 翻譯管線（`check-budget-i18n.py`），**目前 ar/es/fr/hi/id/ja/ko/pt/ru/vi 都有這個 json，de 沒有**——這不是本次出生漏做，是這條翻譯線本身在 de 出生前就對所有已啟用語言逐一補齊，de 因為還沒 enabled 所以還沒排到。列為 flip 後的待辦，非阻斷 flip 本身（bench.ts 同款 fallback 機制會讓 /de/budget 顯示英文而非破版）。

### `src/pages/de/` 路由目錄

複製 `src/pages/ru/`（24 個檔案，逐一比對確認除 3 個語言碼相關檔案外，其餘與 `src/pages/ar/` 完全一致，證實這批頁面本身語言無關，只是 Astro 檔案式路由必須每語一份實體目錄的既有結構債）：

- `[category]/[slug].astro`：`ru` → `de` 字串替換（folderPath／buildGitInfoCache／lang prop／錯誤訊息共 6 處），頂部註解日期改為 2026-09-05
- `[category]/index.astro`：`getCategoryHubStaticPaths('ru')` → `('de')`
- `soundscape.astro`：`<SoundscapeTemplate lang="ru" />` → `lang="de"`
- 其餘 21 檔完全 lang-agnostic，直接複製即可

驗證：`find src/pages/de -type f | wc -l` = 24（與 `src/pages/ru` 相同），全目錄 grep `\bru\b` 只剩 1 處合法的「本檔案是從 ru 複製」溯源註解。

### `docs/editorial/per-language/TRANSLATION-de.md`（新誕生）

比照 vi/ar/ru 出生前例的結構，篇幅依哲宇指示縮到 20-30 條核心詞（非 ru.md 全 15 節 400 行規格——de 人名/地名沿用英文既有羅馬化，不需要 ru 那種整套音譯系統章節）。內容錨點：

- German Wikipedia 即時查證：Chinesisch Taipeh（IOC 構造詞，僅限體育語境）、Taiwan (Provinz)、Zwischenfall vom 28. Februar 1947（二二八）、Chiang Kai-shek（德文條目標題沿用英文拼法，非獨立音譯）
- Übermedien（Klaus Bardenhagen 對 dpa/FAZ/Die Welt「abtrünnige Provinz」用法的媒體批評，2019）——跟 ru.md TL;DR #1 引用俄國外長 Lavrov 訪談同一種「真實可查證的媒體證據」規格
- Tagesspiegel 對「Wiedervereinigung」框架的評論（標題本身即批評中國要求德國協助「歷史扭曲」）
- 交叉對照既有 84 篇語料實測：Peking（11 檔）、Festland/Festlandchina（9 檔）——**de 出生時 knowledge/de/ 已有內容，跟 ru/ar 出生時「knowledge/ 尚不存在、例句全靠假設情境」的處境不同**，§2/§6 的例子是真實已上線譯文，不是推測

`§1/§2/§3/§6` + TL;DR 章節編號對齊 `openrouter-translate.py` 的 `load_lang_guide_sections()` 自動抽取正則（`## (?:1|2|3|6)[.\s]`），已用該函式實測驗證抽出 9,933 字元。

### 註冊表衍生自動跟上驗證（grep 'ru' 排查）

逐一 grep 全 repo 出現 `'ru'` 的檔案，確認 de 是否自動跟上：

| 檔案 | 是否自動跟上 | 處置 |
| ---- | -------------- | ---- |
| `src/config/languages.{ts,mjs}` | N/A（本體） | Stage 1 已完成 |
| `src/styles/global.css`（Cyrillic 排版規則） | 不適用 | ru/uk/bg/sr 是 Cyrillic 專屬排版，de 是拉丁字母，不需要 |
| `src/i18n/utils.ts` FALLBACK_CHAIN | ❌ 缺 de | **已修**：加 `de: ['de', 'en', 'zh-TW']` |
| `src/pages/ru/*` | ❌ 路由目錄不存在 | **已建** `src/pages/de/`（見上） |
| `scripts/tools/lang-sync/hub-translate.py` 排除清單 | ❌ 缺 de | **已修** |
| `scripts/tools/lang-sync/openrouter-translate.py` LANG_NAMES | ❌ 缺 de | **已修** |
| `scripts/tools/lang-sync/cjk-leak-check.py` NON_CJK_SCRIPT_LANGS | ❌ 缺 de | **已修**（見 Stage 3） |
| `scripts/tools/lang-sync/geo-fidelity-check.py` MARKERS | ❌ 缺德文標記 | **已修**（見 Stage 3） |
| `scripts/tools/lang-sync/langs.py` | ✅ 自動 derive（text-parse `languages.mjs`） | 無需改動，已用 python 直接驗證 `de` 出現在 `ALL_TRANSLATION_LANGS` |
| `scripts/tools/lang-sync/ratio-bands.json` | ✅ 佔位值已存在 | 本次重校準為實測值（見 Stage 2） |
| `scripts/tools/check-language-registry-sync.sh`（VIZ_STRINGS／譯文 QA 接線對賬） | ✅ 已過 | 意外發現：de 的 script-presence-check／cjk-residue-check／translation-check.yml CI paths 三處已於 **2026-08-30** 由前次 session 修過（見下段） |
| `.gitignore` src/content 區塊 | ❌ 缺 `src/content/de/` | **已修**——Stage 6 build 測試若不修這個會讓 de 的 derived content 目錄意外可被 commit |
| `src/utils/getLangSwitchPath.ts` | ✅ 從 `LANGUAGES` registry 直接 derive | 無需改動 |
| `scripts/tools/i18n-translate.py`／`ollama-translate.py`／`diary-translate.py` 的 LANG_NAMES | N/A（legacy 5 語系統） | 這三支工具連 vi/id/pt/hi/ar/ru 都沒收（只服務原始 en/ja/ko/es/fr），已被 `ui-bundle-translate.py`／cascade 架構取代，判定為既有殭屍程式碼非本次範圍 |

### 發現的既有伏筆（2026-08-30，非本次修）

`check-language-registry-sync.sh` 執行時印出：`✅ 譯文 QA 接線覆蓋所有有內容的語言`。追查發現這是**前次 session（2026-08-30）已經修過**的三件事：`script-presence-check.py` 的 DIACRITICS profile、`cjk-residue-check.py` 的 TARGET_LANGS、`.github/workflows/translation-check.yml` 的 paths filter——三處程式碼註解都明確寫著「de 於 2026-08-19 進註冊表但這道閘門沒接上，77 篇語料進庫期間形同不存在」。這道自動化檢查完全沒有涵蓋 `cjk-leak-check.py` 與 `geo-fidelity-check.py`（本次才發現的兩個缺口）——`check-language-registry-sync.sh` 本身也有盲點，只查它自己知道要查的三處 mirror，不是全面性保證。

---

## Stage 6 — build 驗證前置

**方法**：在 worktree 內把 `src/config/languages.{ts,mjs}` 的 de `enabled` 暫時 `false → true`，跑完整 `bash scripts/core/sync.sh` → `npx astro sync` → `npm run build`（含 postbuild 自動跑 `check-url-contract.mjs --strict`）→ 再跑一次獨立的 report-only `check:url-contract` → 檢查 `dist/de/` 實際產物 → **flip 回 `false`** → `git checkout --` 清掉 build 過程附帶重新產生的 25 個衍生檔案（`public/api/*.json`／`src/data/*.json`／`README.md`／`knowledge/_translation-status.json` 等——這些是 `npm run build` 的 prebuild pipeline 在 de enabled 狀態下重新計算的站體統計，不屬於本次出生的刻意變更，已還原，不進 commit）。

### 結果：全綠

```
npm run build
✓ Completed in 169.58s
[build] 14245 page(s) built in 170.78s
[build] Complete!

postbuild: node scripts/tools/check-url-contract.mjs --strict
檔案總數: 23586  (HTML: 14618, sitemap 檔: 2)
ground-truth URL 集合大小（含變形）: 47171
公告 URL 總數（去重後，跨三來源加總）: 37203
>>> DEAD 總數: 0 <<<
  hreflang/rss alternate  公告數 10316  dead 0
  canonical               公告數 13521  dead 0
  sitemap <loc>           公告數 13366  dead 0
  sitemap 反向覆蓋缺席      0（黃燈：報告不擋）
  英文別名洩漏              追蹤 881，洩漏 0
沒有偵測到 dead 公告 URL。
```

`npm run build` 全綠通過（含 `--strict` 版 postbuild hook——若有 dead link 這一步就會讓整個 build 失敗，未失敗即代表真的 0 dead）。獨立再跑一次 report-only `check:url-contract` 結果相同。

### de 產物確認

`dist/de/` 共 **127 個 HTML 檔**，涵蓋：

- **第一層 骨架**：註冊表 enabled 後 `dist/de/` 目錄存在，dashboard/data 等站體資料在 build 過程中認得 de（`ENABLED_LANGUAGE_CODES` 含 de 時各 prebuild 腳本正常跑過，未見 de 專屬報錯）
- **第二層 頁面**：24 個 UI 靜態頁（about／budget／changelog／companies／contribute／dashboard／data／explore／graph／latest／map／mcp／opendata／resources／search／soundscape／taiwan-shape／terminology／timeline／elections/2026 等）全部產出，抽查 `dist/de/culture/index.html`：`<title>Kultur - Taiwan.md</title>`、`<h1>Kultur</h1>`、`inLanguage: "de"` 全部正確——UI bundle 的 de block 真的接上了，不是空殼
- **第三層 Hub**：`dist/de/{culture,food,geography,history,people,technology}/index.html` 六個分類 Hub 頁**都有產出**（路由層沒有壞），分類名稱正確翻譯（如「Kultur」），文章卡片列表正確顯示 de 譯文的標題/描述（如 `Jiaobei 擲筊: Hinter einer Chance von 50 Prozent die Stimme der Götter hören`）——**但沒有任何一頁有 `_{Category} Hub.md` 提供的策展導言**（因為 `knowledge/de/` 裡目前 0 篇 Hub 翻譯），頁面退化成「純文章列表」而非「策展入口」。這比 LANGUAGE-BIRTH-CHECKLIST v1.0 定義的「Hub 完全缺席」情況健康（ko 出生時是頁面檔案本身是空的），但沒有達到「有策展內容」的 Stage 6 hard gate 標準，見下方待辦
- **第四層 文章**：抽查 `dist/de/technology/taiwan-semiconductor-industry/index.html`、`dist/de/history/taiwan-forestry-history/index.html`、`dist/de/culture/jiaobei-divination-blocks/index.html` 等多篇，內容、frontmatter、footnote 錨點均正常渲染

### 發現但非本次修的既有缺口

`dist/de/culture/index.html` 等 Hub 頁的無障礙跳轉連結顯示「跳到主要內容」（中文）而非德文——追查是 `src/layouts/Layout.astro` 的 `skipLinkLabels` 物件只收錄 zh-TW/en/ja/ko/es/fr 六語，vi/id/pt/hi/ar/ru 五個已出生語言原本就缺（[reports/language-birth-2026-07-25.md](../language-birth-2026-07-25.md) 已記錄這個既有缺口），de 出生後成為第七個受影響語言。這是**跨語言的既有缺口，不是 de 專屬新問題**，本次未修（不在 Stage 4 wiring 範圍——`skipLinkLabels` 不是「語言清單」而是需要真的填 7 語翻譯字串的內容工作）。

---

## Flip 前主 session 該親自驗的清單

1. **四層完整度第三層「Hub」路由健康但缺策展內容**——`knowledge/de/` 沒有任何 `_{Category} Hub.md` 翻譯（Culture/Food/Geography/History/People/Technology 六個 zh-TW Hub 都還沒有 de 版），Stage 6 build 驗證確認 6 個 Hub 頁路由/渲染本身健康（見上），只是退化成純文章列表。`hub-translate.py` 已把 de 加進排除清單（工具已就緒），但實際跑 Hub 翻譯內容是 P0 批次工作，本次刻意不做。Flip 前建議至少跑過這 6 篇。
2. **`data/budget/i18n/de.json` 不存在**——`/de/budget` 頁面 flip 後會整頁走 fallback 顯示英文（不會破版，但跟其餘 10 個已啟用語言不一致）。
3. **geo-fidelity 1 檔人審**（taiwan-semiconductor-industry.md，見 Stage 3）——判斷是否要求譯者修得更貼源文。
4. **cjk-leak-check.py 15 檔假陽性**——本次判定非阻斷，但建議親眼過一遍確認判斷正確（尤其護國神山／反對軍管／民主萬歲三組，本次只用自動化工具人審，未逐字讀德文原文）。
5. **本次 QA 只做既有 84 篇的檢查，沒有做任何新內容翻譯**——Stage 3 P0 內容批（首頁接觸點 + 該市場 SC 熱點約 50 篇）仍待走，跟 babel routine 排期銜接。
6. **`enabled: true` 這一行本身**——本次全程未碰，Stage 5 flip 由主 session 執行。
7. Stage 6 build/URL contract 細節結果見上方 §Stage 6 段，flip 後建議重跑一次完整 `npm run build` + `check:url-contract` 做最終確認（本次驗證跑在暫時 flip 的隔離視窗，非最終上線前的官方跑）。

---

_v1.0 | 2026-09-05 — de 出生 Stage 2-4 + 6-prep，OBSERVER-QUEUE #29 哲宇拍板。Worktree `.worktrees/20260905-20260905-de-birth`。Stage 5 flip 未做，留給主 session。_
