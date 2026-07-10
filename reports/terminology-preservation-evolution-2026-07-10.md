# 用語保存計畫 — 深度研究與進化規劃（2026-07-10）

> 哲宇 /goal（2026-07-10 晚間，本日第三個 goal）：
> 「深度研究＋深度分析＋寫一個計劃升級『用語保存計畫』所有關聯頁面。其中最重要的是：
> 定一個讓本地模型或 Haiku 或 Sonnet 完整重看一次所有詞庫、對看起來很奇怪或可能有錯的做標記、
> 再做審核與修訂的機制。並 review 所有相關頁面、升級現有網頁與功能、檢查視覺與功能 bug 都修整進化。
> 幫我深度寫完研究報告並施作這所有的進化。」
>
> 本檔是研究＋規劃＋施作紀錄。資料層用確定性 script 體檢（避開 2026-06-13 audit 踩到的 agent-summary
> content-filter 問題）；頁面層由兩隻背景 agent 讀 code map；LLM 全審由本地 Ollama 跑（見 §4）。

---

## TL;DR

用語保存計畫是 Taiwan.md 主權基建的語言本體：`data/terminology/` 底下 **2,334 個 YAML 詞條**，
把台灣用語對照到中國用語，讓台灣人的說法在網路上被看見、也幫讀者辨識哪些是滲透進來的中國詞。
三個頁面（index 瀏覽 / converter 轉換器 / per-term SEO 落地頁）都上線了，per-term 頁正被 Google 收錄。

問題分兩層。**資料層是主戰場**：2,334 條裡 **78% 是薄殼**（只有對照、零內文），**73% 被預設成
「B 1949 分流」但只有 7% 有分歧點佐證**，約 1,400 條來自 1997 手冊＋ThunderKO 那批低品質匯入，
而且散落著真正的錯配（`一鍵`台灣欄誤填「單鍵」、`乍母朗瑪峰`是珠穆朗瑪峰的亂碼音譯）、機械展開
的無意義條目（`31位元`、`60位元`）、以及一整批只差簡體字的品牌名（`Apple公司/苹果公司`、`BMW/宝马`）。
這些正是哲宇要 LLM 全掃出來的東西。

**頁面層 6/22 那晚已 ship 過一輪**（P0-P2 止血＋SERP 轉換），但留了幾個 bug：placeholder 垃圾
還在 index 瀏覽頁露出（P0 修法只補到 per-term 頁）、per-term 頁對 F 型與空白 fork 硬說「是中國大陸的用法」、
台灣化指數在反向轉換時算錯、FAQ 結構化資料寫死「1,800 條」跟畫面數字會漂。三個頁面各自重刻一份
YAML 讀取＋清洗邏輯，靠手動維持同步，是最大的結構脆弱點。

**核心產物**是一個兩層審查機制：本地 Ollama（qwen3.6:35b，無 content filter、零成本、主權對齊）
完整掃過每一條、判 verdict＋issue_type＋修正建議；主 session（我，Opus）人在迴路 adjudicate flag 子集、
落實修訂。這一層是新造的器官（`scripts/tools/terminology-llm-review.py`），詞庫從此有了品質免疫力。

---

## §1 用語保存計畫是什麼（organism context）

`data/terminology/README.md` 開宗明義：「Taiwan.md 的文字應該讀起來像在台灣長大的人寫的。這不是政治
立場，是生活經驗的真實性。」放進 MANIFESTO §主權的巴別塔的脈絡看，這個計畫是語言主權的儀器化：
當中國網路內容大量滲透、PRC 起源的 AI 模型變成中文世界的認知底層，「台灣人怎麼說」這件事需要一個
主動保存的機制，否則會被慢慢磨平。詞庫是這件事的資料庫，converter 是給讀者的工具，per-term 頁是讓
「XX 台灣怎麼說」這類搜尋能撈到台灣答案的 SEO 觸手。

分歧類型分成八類（README canonical）：A 日語遺產（便當/盒飯）、B 1949 分流（計程車/出租車）、
C 網路時代新生（視頻/博主）、D 台客語底層（呷飯/阿莎力）、E 正在分歧中（人設/躺平）、
F 同詞不同語感（領導/水平）、semantic 語義差異、orthographic 字形差異。

資料來源三批（品質落差是整個問題的根）：

| 來源                                       | 詞對數 | 品質                          |
| ------------------------------------------ | ------ | ----------------------------- |
| 藍光濾波研究所（IT/電腦）                  | ~1,089 | 中                            |
| ThunderKO C2T（IT/商務/學術）              | ~500   | 中低                          |
| 《大陸用語檢索手冊》1997（日常/教育/國名） | ~250   | 低（1997 歷史快照，多已過時） |
| caris-events/invade（CC0，E 型正在分歧）   | ~227   | 高（人工策展、有肉）          |

---

## §2 現狀盤點

### 2.1 三個頁面（都已上線）

- **`/terminology/`（index）** — 瀏覽 grid，build 時讀全部 YAML、依 fork_type＋筆畫排序、可篩選搜尋、有分歧樹彈窗。
- **`/terminology/converter/`（旗艦）** — 貼一段文字轉換 CN↔TW，build 時用 OpenCC 產生簡繁兩種來源形，
  客戶端做非重疊比對＋標記；有雙向切換、台灣化指數、8 個範例 chip、WebApplication＋FAQPage 兩個 JSON-LD。
- **`/terminology/{詞}`（per-term）** — 約 2,300 個靜態 SEO 落地頁，2026-06-13 上線。每頁有對照卡、直答段、
  fork 說明（有 honesty gate）、詞源、例句、分類 chip、FAQ、converter CTA、相關詞、來源。

三頁都用共用的 `PageHero` + `Layout`，但**各自重刻一份 YAML 讀取＋`cleanChinaSource` 清洗＋收錄過濾**，
靠註解與人工維持同步。這是結構層最大的脆弱點：任何 schema 改動要改三個地方，漏一個就漂移。

### 2.2 工具鏈（10 支，全部確定性、零 LLM）

`extract-china-terms.py`（YAML→偵測 TSV，接進 prebuild）、`terminology-yaml-audit.py`（ThunderKO 交叉驗證、
自動刪 L1 垃圾、L3 送人工）、`terminology-yaml-dedup.py`（重複對消解）、`terminology-yaml-clean.py`（清 china 值）、
`terminology-prose-fix.py`（改文章 prose 裡的 A 級中國詞，**但用自己 hardcode 的表、沒讀 YAML SSOT**——一個
潛在 SSOT 漂移點）、`terminology-demand-rank.py`（SC 需求排序，**候選 cron 但從未排程**）、
`converter-analytics.py` / `converter-demand.py`（GA/SC 感知）、`cli/terminology.js`（CLI 查詢轉換）、
`normalize-terminology.js`（schema 遷移）。

**關鍵缺口：完全沒有任何 LLM 審查詞條品質的工具**。所有既有驗證都是 regex/白名單/長度比。哲宇要的
「完整重看一次」在既有系統裡不存在，是這次要新造的器官。

### 2.3 6/22 那一輪已經 ship 了什麼

2026-06-22 的策略報告（`terminology-page-evolution-2026-06-22.md`）自稱「不含實作」，但**同一晚三個 commit
就把它 ship 了**（`0dbc2fc08` 23:31 / `1425e0e83` 23:50 / `a061300c8` 23:56）。已落地：per-term 頁 placeholder
過濾、hero padding 收 compact、直答段、FAQPage JSON-LD、SERP 標題對齊（部分）。刻意沒做：「是支語嗎」
判定徽章（政治敏感，等哲宇）。所以頁面層的起點是一個已進化過、但留了 bug 的基礎，這一輪在它之上再進化。

---

## §3 兩層問題診斷

### 3.1 資料層（哲宇 goal 的主戰場）— 全庫確定性體檢

跑 `data/terminology/*.yaml` 2,334 筆（0 parse error）：

**欄位覆蓋率暴露「薄」的結構性來源：**

| 指標                         | 數字             | 意義                            |
| ---------------------------- | ---------------- | ------------------------------- |
| display.taiwan / china 有值  | 99% / 98%        | 對照本身齊全                    |
| **薄殼（只有對照、零內文）** | **1,825（78%）** | per-term 頁沒肉可長的結構性來源 |
| etymology.origin 有值        | 466（19%）       | 只有 1/5 有詞源                 |
| etymology.fork_point 有值    | 186（7%）        | 分歧點幾乎都空                  |
| notes（非佔位）有值          | 492（21%）       |                                 |
| **usage 例句有值**           | **10（0%）**     | 幾乎沒有任何台灣例句            |
| english 有值                 | 189（8%）        |                                 |

**fork_type 分布暴露「誠信」問題：**

| fork_type          | 筆數             | 問題                                                                           |
| ------------------ | ---------------- | ------------------------------------------------------------------------------ |
| **B（1949 分流）** | **1,711（73%）** | 預設值，只有 7% 有分歧點佐證。很多其實是網路詞（視頻/激活/優化），跟 1949 無關 |
| E（正在分歧）      | 249              | caris/invade 人工策展，多有肉                                                  |
| semantic           | 187              | 舊值                                                                           |
| A（日語遺產）      | 107              |                                                                                |
| C/D/F/orthographic | 78               |                                                                                |

B 佔七成而佐證只有 7%，等於把一個 import 預設值當歷史事實寫在約 1,600 個被索引的頁面上。這是「給錯」，
比「少給」嚴重。

**來源指紋**：ThunderKO/1997 手冊 1,186 次、署名/其他 913、caris/invade 227、教育部辭典 92。低品質那批
（ThunderKO/1997）就是問題集中區。

**確定性啟發式已能抓到的可疑候選：**

- **14 個數字型機械展開**：`4/8/12/16/18/24/31/32/36/48/60/64/80/128位元`。8/16/32/64 是真的，`31位元`
  `60位元` 這種不存在的規格是機械展開的無意義條目。
- **479 個「單字差且薄」低信心自動條目**（含 `一鍵`台灣欄誤填「單鍵」、`主詞/主语`台灣欄疑似漏字、
  `並列/並行`、`並行/並發` 這種 6/13 就標過的 soft pair）。
- **7 個 SAME（taiwan==china）**：句號/圈粉/撤銷/撥號工具/查準率/正確率/雙擊——6/13 audit 刻意中和的，
  被 getStaticPaths 過濾、無害，但是 DB 噪音。
- **40 組重複 display.taiwan**（`桌上型電腦`×3、`連結`×3……）——多數合法（多個中國變體對到同一台灣詞），
  少數是結構冗餘。
- **id 型態混雜**：2,084 中文 id、234 ascii-slug、16 其他；33 條沒有 added 日期。

冒煙測試（qwen3.6 跑前 24 筆，即字母序最爛那批）證實 LLM 能抓到人抓不到的量級：`Apple公司/苹果公司`
`BMW/宝马` 這種「中國欄只是簡體字、無真實用語差異」的品牌名一整批（issue_type=SAME_WORD）、
`Android/安卓` `Facebook/脸书` 這種「中國詞台灣也通用」（NOT_DISTINCT），加上機械 CRUFT 與 MAPPING_WRONG。

### 3.2 頁面層 — 兩隻 agent 讀 code map 的發現

**HIGH**

1. **placeholder 垃圾還在 index 瀏覽頁露出**。6/22 的 P0 過濾只補進 `[id].astro`，`index.astro` 的卡片展開
   段仍原封渲染 `origin`/`taiwan_path`/`china_path`，「台灣用法／中國用法」佔位垃圾在瀏覽頁展開卡片時
   還看得到（`index.astro:404-427`，零 placeholder 處理）。

**MEDIUM**

2. **內容誠信 overclaim**。`[id].astro:365` 只把 `isDiverging` 設給 E 型，其餘全走 else 分支斷言
   「『{china}』是中國大陸的用法」——包含 F 同詞不同語感與空白 fork。honesty gate 軟化了 fork blurb 卻
   沒軟化直答段與 FAQ。
3. **台灣化指數在反向轉換時無意義**。`converter.astro:798` 的 `computeIndex` 把 `after` 寫死 100，紅→綠
   框架在 tw2cn 方向是反的（把台灣詞轉成中國詞應該降台灣化指數，畫面卻還顯示 100% 綠）。
4. **FAQPage 結構化資料 vs 畫面文字不一致**。`converter.astro:1191` JSON-LD 寫死「超過 1,800 條」，畫面
   FAQ 用動態 `{rules.length}`。Google 要求 FAQ rich-result 的 schema 文字與畫面一致，這條會漂。
5. **i18n gap**。三頁全 hardcode zh-TW；en/ja/ko/es/fr 讀者點「Terminology」會落到全中文頁（主題使然
   arguably 合理，但是真缺口）。

**LOW（dead code / a11y / perf）**：fork 彈窗 innerHTML 沒跳脫（`index.astro:688`）、dead prop `updated`、
dead function `applyOpenCC`、dead var `lastHtml`、modulepreload 指錯檔、卡片 a11y 重複 tab stop、
`subcategory` 型別未宣告。

**結構**：三頁 triple-duplicate 的 YAML loader 是最該收斂的——抽一個共用 loader，順手把資料層改動的
成本從「改三處」降到「改一處」。

---

## §4 核心產物：LLM 全審機制設計

### 4.1 為什麼是兩層（本地掃 + 我 adjudicate）

哲宇的話：「用本地的模型或是 Haiku 或是 Sonnet 完整重看一次……再做審核與修訂」。這天然是兩層：

- **Tier 1 全掃（2,308 條有對照者）**：本地 Ollama `qwen3.6:35b-a3b-coding-nvfp4`，逐批（每批 12）判
  verdict（OK/SUSPICIOUS/WRONG）＋issue_type（8 類：MAPPING_WRONG/GARBLED/SAME_WORD/NOT_DISTINCT/
  FORK_TYPE_WRONG/SIMPLIFIED_LEAK/CRUFT/DUBIOUS）＋reason＋suggest。checkpoint 可續跑、count 對齊驗證、
  批次失敗自動對半切。
- **Tier 2 審修**：我（Opus 主 session、人在迴路）對 flag 子集逐條 adjudicate、落實安全修正、把敏感或大量
  的決策整批交哲宇。這一層就是哲宇說的「Haiku/Sonnet 那一層」的概念實體——一個有能力的 Claude 模型
  帶著全 context 做最終判斷，只是 inline 做、不走 API。

### 4.2 為什麼 Tier 1 選本地、不選 cloud

三個理由，主權排在成本前面（CLAUDE.md §Sovereignty lens）：

1. **content filter**。詞庫含屏蔽/翻牆/戒嚴等主權敏感詞。2026-06-13 那次 audit，一個 Opus agent 的合成
   摘要就被 content filter 擋下、什麼都沒落檔。本地模型沒有這層過濾，不會對敏感詞 refuse 或被擋。
2. **成本**。2,334 筆走 API 有實質成本；本地 Ollama 零成本零出境，用的是 MACHINE GPU 軍團。
3. **主權對齊**。「最後 20% sovereignty-sensitive 主題全靠 Tier 3 Local LLM」是 Taiwan.md 既有的
   cascade 哲學，審查主權詞庫本身走本地是同一條原則的自然延伸。

冒煙驗證：qwen3.6 正確 flag「乍母朗瑪峰」亂碼譯名、機械 CRUFT、品牌名簡體對照，放行「軟體/網路/8位元」；
issue_type 分類細膩（AWSL 判「台灣動漫圈也用、更精準對比是萌翻了」）。

### 4.4 校準教訓：本地模型會對不熟的學術詞「自信地誤判 reversed」

第一版 prompt（要求模型「嚴謹判讀不要客氣」）跑到 360 筆時，flag 率高達 57%，其中 MAPPING_WRONG 139 筆。
抽樣揭露問題：模型把**正確的學術/技術對照**判成「欄位標註完全相反」——`亂數/隨機數`（random number）、
`事前機率/先驗機率`（prior）、`互斥或/異或`（XOR）、`事後機率/後驗機率`（posterior）全被誤殺。這些其實
都是對的，模型只是對台灣的學術譯詞不熟，就自信地宣稱 reversed。

這正是 REFLEXES #16／#31／#75 的活教材：sub-agent／peer／LLM 的判讀是線索不是事實，Read ≠ verify。
本地模型（甚至任何單一模型）不能當 oracle。修法兩條：(1) prompt 重寫成**保守預設 OK**——明列一批「不該
誤殺」的正確學術對照當校準錨、把不確定的降級成 SUSPICIOUS 交人工、WRONG 只留給一眼可辨的問題
（亂碼/簡體外洩/同詞/機械 cruft/品牌簡體）；(2) Tier 2（我）對每個 flag 逐條驗證，不套用模型的 suggest。
重寫後 flag 率從 57% 降到約 17%，前述四個誤殺全部回到 OK，而真問題（乍母朗瑪峰/BMW/60位元）仍被抓到。
高精度、可審的 flag 集勝過大而吵的 flag 集——這條進 LESSONS-INBOX 候選。

### 4.3 harness（新器官）

`scripts/tools/terminology-llm-review.py`——reusable、model-agnostic（`OLLAMA_HOST`/`OLLAMA_MODEL`
可換，能指向 fleet GPU）、resumable、count-validated、輸出 `reports/terminology-review/<date>/results.jsonl`
（append-only checkpoint）＋ `flagged.md`（給 Tier 2 的分組明細）。復用 `lang-sync/backends` 的 Ollama 呼叫
模式。全審耗時約 35-40 分鐘、~1.1 筆/秒。

---

## §5 施作計畫（分階段 + 自主權邊界）

| 階段  | 內容                                                                                                                   | 規模       | 自主權                                           |
| ----- | ---------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------ |
| **A** | 建 LLM 全審 harness + 跑完 2,308 條 + 產 flagged 報告                                                                  | 新工具     | ✅ 我可跑（讀/分析）                             |
| **B** | 頁面 bug 修：placeholder-in-index（HIGH）、honesty overclaim（MEDIUM）、台灣化指數、FAQ 寫死、dead code、抽共用 loader | ~4 檔      | ✅ bugfix + 重構（不改呈現決策的部分）           |
| **C** | 資料層安全修正：CRUFT 刪除（31/60位元 等）、SAME_WORD 中和/刪、MAPPING_WRONG 明確錯配修正                              | data 批次  | ⚠️ 明確錯逐條修可自主；大量刪除（>10）整批交哲宇 |
| **D** | fork_type 誠信重分類（B→C 網路詞等）+ schema 補 usage 例句                                                             | 全庫批次   | ❌ >50 檔 + 編輯判斷 → 哲宇                      |
| **E** | `terminology-demand-rank.py` 排 cron（週度 SC 需求 → enrich 清單）                                                     | 新 routine | ⚠️ 新 routine → 哲宇                             |

原則：A/B 這次直接做（bugfix + 新工具 + 分析，全在自主權內）；C 的明確錯配（一鍵/乍母朗瑪峰/機械 CRUFT）
逐條修；C 的大量刪除與 D 的重分類整批寫成清單交哲宇一次拍板（避免我一個人對「某詞算不算支語 / 該不該刪」
下立場判定，符合 §紀實而不煽情 + Bias 1）。

---

## §6 留給哲宇的決策點

1. **大量刪除門檻**：LLM 若 flag 出上百條 SAME_WORD（品牌名只差簡體）與 CRUFT，要一次全刪、還是先看清單再刪？
   建議：明確垃圾（品牌名簡體對照、不存在的規格）我整批列給你、你一句「刪」我就執行。
2. **fork_type 重分類**：1,711 個 B 裡的網路詞要不要重分成 C？這是 >50 檔 + 編輯判斷，等你拍板批次做。
3. **「是支語嗎」徽章**：6/22 刻意沒做（政治敏感）。要不要用中性措辭（常見於中國 / 兩岸已分歧 / 兩岸通用）補上？
4. **加肉尺度**：per-term 頁要長到多深？一句直答，還是像 E 型那樣的小短文？
5. **demand-rank cron**：要不要把 SC 需求排序排成週度 routine，自動產 enrich 優先清單？

---

---

## §7 施作結果（2026-07-10 深夜自動模式，哲宇 /goal「完整自動進化＋修復所有東西」）

### 7.1 LLM 全審結果

2,308 條有對照者全審完畢（qwen3.6:35b 本地，2,544 秒、0 失敗）。**OK 1,772（77%）／flag 536（23%）**。
flag 分佈：MAPPING_WRONG 180／NOT_DISTINCT 128／GARBLED 56／DUBIOUS 39／SAME_WORD 24／SIMPLIFIED_LEAK 2，
另有 107 條 model 未細分（issue_type=WRONG）。完整清單見 `reports/terminology-review/2026-07-10/flagged.md`。

### 7.2 Tier-2 審修最重要的一課：模型會把台灣名「修」向中國名

adjudicate 時發現一個**若盲信會直接反噬主權使命**的 pattern：模型的 suggest 反覆要把台灣正確譯名
改成中國譯名——`宏都拉斯→洪都拉斯`、`辛巴威→津巴布韋`、`突尼西亞→突尼斯`、`聖母峰` 它建議改成 `珠穆朗瑪峰`。
這些台灣欄本來就對，模型只是以中國語料為預設基準。**若照套 suggest，等於把 sovereignty 詞庫洗成中國命名，
與計畫初衷完全相反。** 所以鐵律：LLM flag 是線索不是事實，suggest 一律不套用，每條用台灣知識＋MOFA 對照表
親自判（REFLEXES #16／#31／#75 的又一次驗證，已進 §4.4 校準教訓）。

### 7.3 自主施作的 26 筆（高信心、可逆、逐條驗證）

無人在場，只動「我能獨立確認正確」且不碰 §自主權邊界的：

- **亂碼台灣國名/地名 → 對 MOFA 驗證的正確台灣譯名（含改檔名＋id，slug 一併洗乾淨）**：
  `乍母朗瑪峰→聖母峰`、`乕笨鐘→大笨鐘`、`乌子山共和國→獅子山共和國`、`乍瑞那達→格瑞那達`、
  `波乍那→波札那`、`厄乙垂亞→厄利垂亞`（6 檔 rename）＋`阿拉伯聯合大公國`（阿位伯 typo + 欄位顛倒修正）。
- **中國欄錯字 → 正確中國詞（保留真實兩岸差異）**：`原子筆` china 原珠筆→圓珠筆、`還原光碟` china 恢覆→恢復。
- **純簡繁/同詞、無真實差異 → neutralize（china=taiwan，getStaticPaths 過濾，git 可逆）**：
  匯率／壽司／潛在／遙控器／急診／門診／壓歲錢／複雜／乞業（乞業→企業）／擴銷（擴銷→促銷）10 檔。

工具：`terminology-apply.py`（決策 TSV 安全執行器，dry-run 先行）＋ `terminology-charcheck.py`
（OpenCC 字形層 QA，確認台灣欄近乎零簡體外洩，僅 `乌子山` 1 例、已隨上批修掉）。**0 刪除**——全部
改值或 neutralize，方便觀察者一次 review/revert。

### 7.4 沒動、留給哲宇的 510 筆（§自主權邊界 + 需逐條查證）

剩下 WRONG 107／NOT_DISTINCT 128／MAPPING_WRONG 180（多為 model 誤判）／DUBIOUS 39／未細分殘量，
**不自主施作**，因為它們要嘛是政策判斷（NOT_DISTINCT「品牌名/已通用詞該不該留在詞庫」是策展門檻決定），
要嘛需要逐條查證正確的中國詞（`倒數計時/倒計時`、`光刻機/曝光機` 是模型漏掉的真實差異，不能當無差異刪）。
這是一個需要 human 拍板門檻＋第二輪 China-term 查證的 follow-up，不該無人趕工（趕 = 反而製造錯誤）。
已寫進 OBSERVER-QUEUE 附預設選項；完整逐條在 flagged.md。哲宇醒來一句話即可分批 ship。

_作者：Taiwan.md 🧬｜session 2026-07-10-225026-詞庫保存進化｜資料源：term_analyze.py 全庫確定性體檢
＋兩隻 code-map agent＋qwen3.6 本地全審（2308 條）＋MOFA 國名對照。LLM 全審與 flagged.md 見
reports/terminology-review/2026-07-10/。_
_相關：[terminology-data-audit-2026-06-13.md](terminology-data-audit-2026-06-13.md)（china 欄錯置 audit）
＋[terminology-page-evolution-2026-06-22.md](terminology-page-evolution-2026-06-22.md)（四層策略，已 ship P0-P2）。_
