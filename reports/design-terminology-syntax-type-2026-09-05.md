---
title: 'Design: 用語詞庫句構型別 schema 與 per-term 頁專屬渲染'
description: 'EVOLVE Mode 4 設計報告：OBSERVER-QUEUE #38 選 B 定案細節化。新增 fork_type G-syntax 容器沿用 data/terminology/ 目錄，per-term 頁分流渲染取代詞對詞版型，查證門檻高於詞彙級，月度 TERMINOLOGY-TRENDS routine 如何收納三態判定。'
type: 'design-report'
status: 'draft'
current_version: 'v1.0'
last_updated: 2026-09-05
last_session: '2026-09-05-154128-fortnight-review'
related:
  - '../docs/semiont/OBSERVER-QUEUE.md'
  - '../reports/terminology-zhiyu-deep-research-2026-08-04.md'
  - '../docs/editorial/TERMINOLOGY.md'
  - '../docs/pipelines/TERMINOLOGY-TRENDS-PIPELINE.md'
  - '../docs/pipelines/EVOLVE-PIPELINE.md'
  - '../docs/semiont/MANIFESTO.md'
  - '../docs/semiont/REFLEXES.md'
  - '../knowledge/Culture/台灣華語的演化.md'
  - '../src/pages/terminology/[id].astro'
  - '../src/pages/terminology/converter.astro'
  - '../src/pages/terminology/index.astro'
  - '../scripts/core/extract-china-terms.py'
  - '../docs/semiont/memory/2026-09-05-105046-twmd-terminology-trends.md'
---

# 用語詞庫句構型別 schema 與 per-term 頁專屬渲染設計

> EVOLVE-PIPELINE Mode 4 REPORT 相。觸發：哲宇 2026-09-05 對 OBSERVER-QUEUE #38 拍板選 B「新增句構型別＋per-term 頁專屬渲染」。本報告把這個方向具體化成可派工的 schema 與規格，命中 §自主權邊界的地方停在這裡等哲宇簽字，其餘直接列進實作清單。

## 一、目標與為什麼是現在

讓詞庫接得住句構級的語言滲透討論，不再只能處理一個詞換一個詞的分歧。8/04 深度研究 §7 決策點 1 已經把這個缺口寫清楚：詞庫 schema 是詞對詞，句構級的東西塞進去會撐壞 per-term 頁的整套假設。這個決策點掛了 18 天沒進佇列，本輪 OBSERVER-QUEUE #38 重新提交時多帶了一個訊號：這個場域裡最勤的策展者（Threads @thiankiu.to）近期的整理重心已經從詞彙移到句構與語感，代表社群討論的層級在上移，而站上目前完全接不住。

四個活躍案例分別是「有沒有一種可能」「但凡……」「也是很怎樣怎樣了」「嚴肅怎樣怎樣的」，全部是句型骨架加變數槽，沒有一個能填進 `display.taiwan` 那樣的單一對應詞欄位。讀者搜「有沒有一種可能 支語」的時候，站上什麼都給不出來，這正是詞庫的生態位所在，拖著不動的代價會持續累積。

## 二、現況盤點

### 2.1 schema 對句構不成立的欄位

現有 `data/terminology/*.yaml` 的核心欄位全部假設「一詞換一詞」：

- `display.taiwan` / `display.china`：單一字串，設計成互為替換的一對詞。句構沒有可以填進 `display.taiwan` 的對應詞，它要的是「這個句型在台灣的自然說法長怎樣」的多句示範，不是一個詞。
- `fork_type`（A–F）：六種分類全部描述「一個概念、兩邊各自造出不同的詞」這種分歧成因，沒有一種對應「句型結構本身是否受影響」這件事。
- `detection.severity`（A/B）：`extract-china-terms.py` 把它讀成一個可以逐字比對的固定字串（`cterm`），輸出成 TSV 給 `article-health` 的 `terminology` check 做子字串比對。句構帶變數槽，不是固定字串，套用現有機制等於整段規則失效或需要另一套正規表示式引擎。
- `auto_convert`：控制 `converter.astro` 的 `RULES_CN2TW` 要不要把這個詞當成找字取代規則，本質是「有沒有一個安全的字串換字串」判斷。句構完全不成立，見 2.3。

### 2.2 per-term 頁哪些區塊撐壞

`src/pages/terminology/[id].astro` 整頁圍繞著「中國說 A，台灣說 B」這個單一映射寫成，撐壞的區塊具體列出來：

- **Hero 卡片**：中國用語／台灣用語兩欄對照，中間一個箭頭。句構沒有一個字對字的替換詞可以放進右欄。
- **`leadAnswer` 直答句**：模板是「『{china}』是中國大陸的用法，在台灣通常說『{taiwan}』」，句構沒有這樣的一對一替換可以生成這句話。
- **FAQ 與 JSON-LD FAQPage**：兩題都是「台灣怎麼說」「算不算中國用語」的二分框架，句構的合法終點包含「未定」，這個框架容不下第三態。
- **`getStaticPaths` 收錄規則**：目前的收錄條件寫死在 [id].astro 開頭註解裡（`INCLUSION RULE`），要求 `display.taiwan` 非空且 `display.china` 清洗後非空、不同於 taiwan、不是 N/A。句構條目如果沿用 `pattern`／`taiwan_natural` 欄位，不會符合這條規則，會被靜默排除，連頁面都不會生成。`index.astro` 的收錄邏輯（line 117-123）是同一條規則的獨立複本，需要同步處理，否則句構條目也進不了瀏覽格。
- **轉換器 CTA**：頁尾「想轉換整段文字？」按鈕連到 `/terminology/converter`，對句構條目按下去不會有任何效果（見 2.3），放著是誤導。
- **fork_type 徽章／說明段**：`forkTypeLabels`／`Colors`／`Blurbs` 三個物件目前只映射 A–F，六句解釋全部是「兩岸分流」「兩邊各自造詞」的敘事，沒有一句適用於句構。

### 2.3 auto_convert 對句構應一律 false 的理由

`converter.astro` 的核心機制是把整個詞庫壓成一份固定字串到固定字串的查找表（`RULES_CN2TW`），對貼上來的整段文字做子字串搜尋取代，只在 `auto_convert === false` 時跳過。句構帶變數槽（「有沒有一種可能＋X」的 X 是任意子句），沒有辦法表示成一組固定的來源字串跟目標字串。字面比對只會匹配到完全相同的句子，涵蓋率趨近於零。如果為了涵蓋率而改用正規表示式引擎，等於在一個目前只做精確字串比對、被 2,419 條詞目共用的核心模組裡開一個全新的匹配類型，風險是把一句完全合法的台灣話（例如單純的反問句「有沒有可能」）誤判成需要取代的目標，砍掉使用者原本正確的句子。這個機制的設計前提本身跟句構不相容，句構型別因此必須在 schema 層就標記為結構性不進轉換器，避免因為作者忘記填 `auto_convert: false` 而漏網。

### 2.4 cross-ref 掃描：改 schema 會動到誰

grep `fork_type` 與 `data/terminology` 之後，會被這次新增觸碰到的檔案：

| 檔案                                                     | 影響                                                                                                                              |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `src/pages/terminology/[id].astro`                       | 新增渲染分支＋收錄規則加一條 OR 條件                                                                                              |
| `src/pages/terminology/index.astro`                      | 收錄規則同步、`fork_type` 標籤物件加一格                                                                                          |
| `src/pages/terminology/converter.astro`                  | 明確排除 `fork_type === 'G-syntax'`，不只是靠 `auto_convert`                                                                      |
| `scripts/core/extract-china-terms.py`                    | 確認句構條目不寫進 `.china-terms.detection.tsv`（無 `detection` 區塊即天然排除，屬於既有「保守 opt-in」設計）                     |
| `scripts/core/generate-fork-graph-data.py`               | `TYPE_MAP` 只認得 `semantic`／`orthographic` 兩個舊值，新的 `G-syntax` 值需要決定是否收進分支樹（本報告 §六建議先不收，見風險段） |
| `scripts/tools/lib/article_health/checks/terminology.py` | 讀 TSV 做逐字比對，句構因為沒有 `detection` 區塊天然不進來，不需要改動                                                            |
| `tests/article_health/test_terminology_paths.py`         | 只測 `BASE_DIR` 路徑推導，不驗 schema 形狀，不受影響                                                                              |
| `docs/editorial/TERMINOLOGY.md`                          | §Layer 1 需要補一段句構型別的定義與判準                                                                                           |
| `docs/pipelines/TERMINOLOGY-TRENDS-PIPELINE.md`          | Stage 2 SWEEP／Stage 4 INGEST 需要接進句構專屬 gate，見 §六                                                                       |

這張表裡真正需要寫新程式碼的只有前三列（per-term 頁、瀏覽格、轉換器排除），其餘六列不是本來就天然排除（沒有 `detection` 區塊就不會被讀進 TSV），就是純文件補充。`index.astro` 的分類篩選從既有詞條動態產生，不是寫死的清單，`category: syntax` 新增後會自動多出一個篩選格，不需要另外改分類清單。

範圍集中在渲染層與文件層，不動任何既有 A–F 詞條的資料或既有 generator 的既有分支，是一次新增，不是重構。

## 三、方案發散

| 方案                                                                                   | 做法                                                          | 查證門檻                               | 假陽性風險                     | 渲染複雜度                                         | 與轉換器的隔離                                      | 月度 routine 接得住                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------- | ------------------------------ | -------------------------------------------------- | --------------------------------------------------- | -------------------------------------- |
| (a) 新 fork_type G-syntax，沿用 `data/terminology/`                                    | 同一目錄新增一種型別，per-term 頁分流渲染                     | 高（見 §六）                           | 中，靠 `verdict: 未定` 吸收    | 中，一個頁面兩套分支                               | 天然隔離（無 `display.china` 即不進 `RULES_CN2TW`） | 可，直接掛進既有 Stage 2/4             |
| (b) 獨立 `data/syntax/` 目錄與獨立頁 `/terminology/syntax/`                            | 全新資料源、全新路由，不碰 `[id].astro`                       | 高                                     | 低，物理隔離最乾淨             | 高，等於重造一套 getStaticPaths／JSON-LD／收錄邏輯 | 完全隔離                                            | 需要另開一條 routine stage，維護面雙份 |
| (c) 只寫成一篇知識文章（原 8/04 建議 default，即 OBSERVER-QUEUE #38 選項 A，本輪未選） | 不動 schema，寫進「句構級的語言滲透」與《台灣華語的演化》互鏈 | 中（文章層級查證，非逐條 schema 驗證） | 低，沒有逐詞判定就沒有逐詞誤判 | 無，走既有 REWRITE-PIPELINE                        | 不適用                                              | 不適用，一次性產出非常態容器           |

三個判準是這輪發散刻意錨定的：REFLEXES #38「混維度 = silent killer」（任何 status 設計都要問混了幾種根本不同的成因）、MANIFESTO §13 立體地愛的語言層姿態（查證與保存，不站在出征）、以及哲宇本輪已經在 OBSERVER-QUEUE 明確給出的方向約束。選 B 已經排除了 (c) 純文章路線，發散表把 (c) 留下只是為了讓對照可見，不是還在猶豫。

(b) 的物理隔離乾淨，但代價是整套 `getStaticPaths`／JSON-LD／收錄邏輯要重造一份，而句構條目在可預見的未來數量遠小於詞彙（每輪上限個位數，見 §六），為了個位數條目重造一條路由與一條 routine stage 不成比例。獨立目錄也讓「詞庫」這個心智模型分裂成兩個資料源，讀者從 GitHub 找詞條時要記得兩個路徑，違反「造橋鋪路」裡「新細胞天生健康」的精神，新增能力不該讓既有心智模型變複雜。

## 四、定案與理由

**採 (a)：新增 `fork_type: G-syntax`，沿用 `data/terminology/` 目錄，per-term 頁在 `[id].astro` 內加一條渲染分支。**

理由對齊哲宇本輪拍板的方向，也對齊三個判準：

1. **不混維度**：`fork_type` 欄位本身的語意是「這個詞條屬於哪一種分歧容器」，A–F 描述詞彙分歧的六種成因，`G-syntax` 描述句構分歧這第七種容器。它不是跟 A–F 共用同一套判準硬塞進去，而是同一個欄位上一個平行的新枚舉值，各自帶各自的子欄位。真正會混維度的是把句構的 `verdict` 三態塞進 `detection.severity` 的紅黃二態，或者把句構的查證強度跟詞彙的查證強度算同一把尺，這兩處本設計都刻意分開，見 §五、§六。
2. **不站在出征**：句構本身就是這個站上查證門檻最高、最容易誤判的一層（8/04 報告 §5 已指出台語底層與舊台灣國語常常反過來破功句法層的滲透主張），`verdict: 未定` 是合法終點而非查證失敗，直接對應 MANIFESTO §13。
3. **成本可控**：`data/terminology/` 現有的檔案級隔離（一詞一檔）跟收錄規則的 OR 分支已經是最小改動，不需要重造一套獨立的資料層與路由層。

這個定案只處理容器怎麼長，不代表詞庫馬上要塞滿句構條目。§六把每輪上限訂在 3 條，就是刻意讓這個新容器先小規模跑幾輪，累積判準的校準紀錄，再決定要不要放寬。

## 五、Schema 草案

### 5.1 欄位定義

```yaml
id: '' # 英文或拼音 slug
category: 'syntax' # 新增分類值，index.astro 分類是動態產生，不需要額外改動
fork_type: 'G-syntax' # 新枚舉值，與既有 A–F 平行，不共用判準

pattern: '' # 句型骨架，含變數槽說明（用文字描述槽位，不寫成正規表示式）

display:
  taiwan_natural: [] # 台灣自然說法示範，2-3 句，取代 display.taiwan/china

etymology:
  china_origin_evidence: '' # 中國起源舉證：載體、年代、傳播路徑
  counter_evidence: '' # 反方舉證：台語底層／舊台灣國語／學術文獻／查無紀錄

verdict: '' # 滲透 / 本土 / 未定，三態，未定是合法終點

notes: ''
sources: [] # 至少一則語言學或辭典來源 + 反方檢索紀錄的出處
added: ''
updated: ''
```

句構條目的 schema 直接不定義 `auto_convert` 與 `detection` 這兩個欄位，讓它們的缺席本身就代表結構性不適用，避免作者誤以為忘記填而回頭補上。

### 5.2 範例一：滲透判定

```yaml
id: 不了一點
category: syntax
fork_type: G-syntax
pattern: 'X不了一點（如：吃不了一點／離不了一點／尊重不了一點），「不了」接強調助詞「一點」構成程度誇飾的謂語收尾'
display:
  taiwan_natural:
    - '我真的受不了他這樣。'
    - '這種行銷手法我完全沒辦法接受。'
etymology:
  china_origin_evidence: '2023 年後在小紅書、抖音短影音留言區高頻出現，多用於情緒宣洩型留言（「真的忍不了一點」），與既有標準漢語「忍無可忍」語意接近但構詞路徑不同，屬於「不了＋一點」的新造謂語收尾模板。'
  counter_evidence: '本輪查詢教育部《重編國語辭典修訂本》與《臺灣閩南語常用詞辭典》，均未收錄「不了一點」句式；未找到台語文獻中的對應結構，暫無反方實據，但這也代表反方查證還沒有做到位——尚缺一則獨立語言學來源交叉確認。'
verdict: 滲透
notes: '2026-08-04 支語深度研究艦隊已將此句型列為多切面命中的候選（§5），本條為 schema 草案示範，正式入庫前需完成至少一則獨立語言學或辭典來源的直接查證。'
sources:
  - 'reports/terminology-zhiyu-deep-research-2026-08-04.md §5'
added: '2026-09-05（草案示範，未入庫）'
```

### 5.3 範例二：未定判定，含反方舉證

```yaml
id: 有沒有一種可能
category: syntax
fork_type: G-syntax
pattern: '「有沒有一種可能，X」置於句首的假設性反問句，X 為完整子句，語氣介於委婉建議與陰陽怪氣之間'
display:
  taiwan_natural:
    - '會不會其實是我們想太多了？'
    - '搞不好問題根本不在這裡？'
etymology:
  china_origin_evidence: '本輪僅在 Threads「支語」搜尋現場觀察到高頻使用與策展者標記（@thiankiu.to），未追溯到可考證的單一起源討論串；「有沒有可能」本身是標準漢語既有的反問句型，社群爭議點落在使用密度與語氣模板化，不是句法本身是否存在。'
  counter_evidence: '「有沒有可能」作為反問句型在台灣書面與口語長期存在，不需要外來輸入即可自然生成；本輪未能在既有台灣語料中排除獨立平行發展的可能，也沒有找到能證明這是晚近由中國內容平台特別輸入台灣使用者語感的直接證據。'
verdict: 未定
notes: '爭議中——句法結構本身非外來，社群感知到的是使用密度與語氣模板化的變化，不是句型有無。本條保留未定，不預設下一輪必須翻案。'
sources:
  - 'docs/semiont/OBSERVER-QUEUE.md #38'
  - 'reports/terminology-zhiyu-deep-research-2026-08-04.md §2'
added: '2026-09-05（草案示範，未入庫）'
```

## 六、per-term 頁規格、查證門檻與月度 routine 銜接

### 6.1 per-term 頁專屬渲染

`[id].astro` 的 `getStaticPaths` 收錄規則加一條 OR 分支：`fork_type === 'G-syntax'` 且 `pattern` 非空即收錄，不再要求 `display.taiwan`／`display.china`。body 依 `forkKey` 分流：

- **Hero**：不用中國／台灣兩欄對照，改成單欄呈現句型骨架本身，標題用 `pattern` 的第一句白話說明。
- **直答句**：三態各自一句中性敘述，不用「是中國大陸的用法」這種定性語氣。滲透判定寫「這個句型的來源證據指向中國內容平台，台灣的自然說法通常是……」，本土判定寫「查證後沒有找到外來輸入的證據，這個句型看起來是獨立或平行發展」，未定判定寫「這個句型還在查證中，目前雙方的證據都不夠充分下判斷」。
- **爭議中徽章**：只在 `verdict === '未定'` 時顯示，用既有 `usageNote` 那組琥珀色警示樣式（`#f0c36d` / `#fffaf0`），文字「爭議中，尚未有定論」，不用紅綠燈式的對錯配色。
- **`taiwan_natural` 區塊**：取代原本的「詞源與來龍去脈」跟「台灣人會這樣說」兩段，合併成一段「台灣人通常怎麼說」，列出 2-3 句示範。
- **`china_origin_evidence` / `counter_evidence`**：各自成一段，標題直白寫「查到的滲透證據」跟「查到的反方證據」，兩段版面同等大小，不特別放大或緊縮哪一段。
- **FAQ**：改成單題「這是不是從中國傳過來的說法？」，答案直接取 `verdict` 對應的中性敘述。
- **轉換器 CTA**：整段移除，句構條目底部改成「回到用語詞庫」與 GitHub 連結，不放任何轉換入口。
- **JSON-LD**：`DefinedTerm` 的 `alternateName` 改放 `pattern` 本身而非詞彙對。`FAQPage` 沿用單題版本。
- **fork_type 徽章**：`forkTypeLabels`／`Colors`／`Blurbs` 三個物件各加一格 `'G-syntax': '句構級語言滲透'`，顏色刻意跟既有六色區隔開：它是一個獨立的判定維度，跟六種分歧成因分屬不同層次。

`index.astro` 的收錄規則同步加同一條 OR 分支，瀏覽格顯示句構條目時只列 `pattern` 與 `verdict`，不套用詞彙卡片的「中國：台灣」欄位配置。

### 6.2 查證門檻

句構級的查證門檻高於詞彙級，理由是 8/04 報告已經證實反方舉證（台語底層、舊台灣國語、學術文獻同型研究）經常直接推翻表面上「像是滲透」的直覺，門檻定為：

- **至少一則語言學或辭典來源**：教育部《重編國語辭典修訂本》、《臺灣閩南語常用詞辭典》、學術論文（雙賓結構、底層影響研究一類）任一命中即算，查無收錄本身也要記錄下來，不是查不到就跳過不寫。
- **強制反方檢索紀錄**：`counter_evidence` 欄位不能留空字串，即使檢索結果是「沒找到」，也要寫成一句完整的敘述（範例二示範了這種寫法），對齊 8/04 報告 §3.6「查不到就承認查不到」的紀律。
- **`verdict: 未定` 是合法終點，不是查證失敗**：月度 routine 的成功指標不是「這輪翻案幾條」，是「這輪每條候選都完成一次有紀錄的查證嘗試」。這條刻意寫進門檻，避免未來哪一輪為了衝轉正數字，把查證強度做鬆。

9/05 當天的月度用語趨勢執行留下一條還沒升 canonical 的觀察：累積到第八個誤判翻案案例，全部都是「以為是支語，查證後發現不是或方向相反」，還沒出現反向案例。句構層的查證比詞彙層更容易受這種方向性偏誤影響，因為句構的滲透判定天生比詞彙判定更依賴直覺，門檻裡的反方檢索紀錄正是用來對抗這個既有偏誤。

### 6.3 TERMINOLOGY-TRENDS 月度銜接

`TERMINOLOGY-TRENDS-PIPELINE.md` 現有 7 stage 不需要整條重排，加兩處：

- **Stage 2 SWEEP**：既有 Threads「支語」搜尋現場切面本身就會撞見句構候選（本輪 9/05 執行紀錄已經記下「底層 vs 基層」頻率位移的觀察），不需要新開切面，只需要在搜索時額外標記「這是詞彙還是句構」。
- **Stage 4 INGEST**：句構候選另立一條子 gate，跟詞彙的 ≤20 條/輪上限分開算。**句構候選每輪查證上限 3 條**，遠低於詞彙級，因為每條的查證工時是詞彙級的數倍，轉正（滲透或本土）與否不設下限，未定不計入失敗。任何判定為「滲透」且準備公開發布的句構條目，先進 OBSERVER-QUEUE 讓哲宇過目一輪再 ship，累積幾次校準後再視情況收回自主權內，這點留給哲宇裁決。

## 七、實作清單

| 項目                                                                                                                                  | 自主權                                      |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `docs/editorial/TERMINOLOGY.md` 補句構型別定義段                                                                                      | 自主權內（文件補充）                        |
| `data/terminology/_template-syntax.yaml` 新增範本檔                                                                                   | 自主權內（新增不刪）                        |
| `[id].astro` 收錄規則加 OR 分支＋新增渲染分支                                                                                         | 自主權內（新增分支，既有 A–F 路徑不動）     |
| `index.astro` 收錄規則同步＋`fork_type` 標籤物件加一格                                                                                | 自主權內                                    |
| `converter.astro` 明確排除 `fork_type === 'G-syntax'`                                                                                 | 自主權內（防禦性排除，belt-and-suspenders） |
| `generate-fork-graph-data.py` 確認 `G-syntax` 不進分支樹（不修改 `TYPE_MAP`，讓未知值走既有 fallback，先跑 dry-run 確認不中斷 build） | 自主權內                                    |
| `TERMINOLOGY-TRENDS-PIPELINE.md` 補 Stage 4 句構子 gate                                                                               | 自主權內（文件修改）                        |
| 首批句構候選判定為「滲透」且要公開發布                                                                                                | 需哲宇（進 OBSERVER-QUEUE，§六已標）        |
| dogfood：「有沒有一種可能」走完整條到 per-term 頁渲染                                                                                 | 自主權內（驗收動作，見 §八）                |

每一項各自一個 commit，順序上 schema 與範本先行，渲染分支次之，routine 文件最後，讓每個 commit 都是可獨立驗證的最小單位。

## 八、驗收

**dogfood**：把 §5.3 的「有沒有一種可能」範例草稿走完整條——寫進 `data/terminology/有沒有一種可能.yaml`（`verdict: 未定`）、跑 build 確認 `[id].astro` 生成對應頁面、確認轉換器頁沒有把它收進 `RULES_CN2TW`、確認瀏覽格顯示「爭議中」而不是套用某個 A–F 色卡、確認 `extract-china-terms.py` 重新產生 TSV 時這條不在裡面。全部通過才算這次設計真的能用，不是寫完就等於能用。

其餘驗收：全庫 YAML parse 通過、`terminology-charcheck.js` 對新條目跑過、既有 2,419 條 A–F 詞條的渲染輸出跟改動前逐字比對零差異（分支邏輯不能動到既有路徑）。實務做法是改動前後各跑一次 `astro build`，對 `dist/terminology/` 底下既有詞條的產出頁面做 `diff -r`，只允許新增的句構頁面出現在差異裡，既有頁面一個位元組都不該變。

## 九、風險

**出征姿態外洩**：句構頁如果用「入侵」「污染」這類字眼，會直接違反 MANIFESTO §13 立體地愛的語言層姿態。緩解：直答句一律採 §6.1 給出的中性敘述模板，三態都不用「正確／錯誤」二分語氣。

**過度判定，把台灣本有句法誤扣帽子**：《台灣華語的演化》已經記錄「我有吃飯了」「他給我打」這類台語底層語法印記早就存在於標準用法之外，句構層如果查證不夠嚴謹，很容易把這類本土結構誤判成滲透。緩解：§六查證門檻的反方檢索紀錄是強制欄位，不是選填。

**頁面被截圖當「支語警察」工具**：社群鐘擺目前正從「警戒滲透」擺向「警戒過度糾察」（何萬順「恐淪為新的國語運動」），句構頁如果視覺上像法庭判決書，會被當成新一輪出征的工具，反噬詞庫這幾年建立的查證信譽。緩解：不做舉報／檢舉按鈕，不做黑名單式的紅色警示，`verdict` 三態用色跟既有 `usageNote` 警示色系（暖黃）同一套語彙，維持「這是一份大家吵完會去查的字典」的既有定位，不是「這是一份會抓人的清單」。

**新欄位撞上舊 bug 的同一種形狀**：9/05 當天的月度用語趨勢執行才修過 `terminology-demand-rank.py` 自帶的簡化 YAML 解析器認不得 `notes: |` 這種區塊純量的問題（三個既有詞條的 notes 內文貼了 URL，網址裡的冒號被誤判成巢狀 key）。句構條目的 `china_origin_evidence`／`counter_evidence` 兩個新欄位內容通常比既有 `etymology.origin` 更長、更常包含頓號與冒號，沿用同一支簡化解析器讀取，很可能重新踩進剛修好的同一個坑。緩解：句構條目第一次進 `terminology-demand-rank.py` 掃描範圍前，先手動跑一次確認新欄位的長文字不會讓解析器再次把字串讀成 dict。

**首批候選的範圍界定**：本報告 §5.2／§5.3 的兩條示範只涵蓋 OBSERVER-QUEUE #38 四個活躍案例裡的兩個，「但凡……」與「也是很怎樣怎樣了」「嚴肅怎樣怎樣的」三個候選尚未查證，留給實作階段的 dogfood 之後、正式跑第一輪 Stage 2 SWEEP 時一併處理，不在本報告的範圍內定案。

## 十、後記

（留空，等實作跑完 dogfood 後再回填摩擦紀錄）

---

_v1.0 | 2026-09-05 — 首版。哲宇對 OBSERVER-QUEUE #38 拍板選 B 後的 Mode 4 REPORT 相，實作尚未開始。_
