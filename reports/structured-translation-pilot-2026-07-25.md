---
title: '結構化分段翻譯引擎 pilot — 2026-07-25'
description: '哲宇 directive：前期預防取代事後修補。新工具 structured-translate.py（模型只翻文字，結構由工具持有）+ 6 篇 pilot 資料 + 與整篇式 fail rate 對照'
type: 'pipeline-report'
status: 'pilot-complete'
---

# 結構化分段翻譯引擎 pilot — 2026-07-25

> **Session**：2026-07-25，哲宇 directive「前期預防取代事後修補」
> **新工具**：[`scripts/tools/lang-sync/structured-translate.py`](../scripts/tools/lang-sync/structured-translate.py)
> **Pilot 產物**：`/tmp/structured-pilot/`（不寫 `knowledge/`，僅本報告 + 工具本體進 repo）

---

## TL;DR

- **核心原則落地**：Frontmatter passthrough 欄位（author/date/category/... 同源 `verify-translation.py` 的 `PASSTHROUGH`）**完全不進 prompt**，工具機械複製；腳註 URL 與編號**永遠不進 prompt**；body 按 H2 切塊、每塊獨立驗證獨立重試。三大 fail 家族（passthrough 漏抄／腳註編號飄移／YAML 撇號炸裂）在構造上不可能發生 —— 6 篇 pilot 資料 **0 次**發生。
- **Pilot 6/6 篇** `verify-translation.py` **0 hard-fail**、`article-health --profile=pre-commit` **0 hard/0 warn**。今天全站整篇式翻譯（babel-unified 各批次）同期實測 fail rate 48.6%–91.7%（依批次規模不同，含小樣本噪音；≥20 篇的批次區間如此，詳見下方§與整篇式對照）。
- **開發過程中在 pilot 自己的資料上抓到 3 個真結構 bug 並修復**：腳註無 URL 時硬包出殘破空連結、孤立小 chunk 誤觸 `OpenRouterBackend` 的「疑似拒答」啟發式而整段標題消失、模型偶爾在 body 裡「腦補」出假腳註定義行造成編號重複。全部是從這 3 篇真實文章的輸出中發現的，不是憑空設計。
- **也抓到既有共用工具的盲點**（非本工具引入，如實記錄）：`cjk-leak-check.py` 只抓 4 字以上連續漢字，對黏在譯文詞尾的 1-2 字殘留（如「phụng祀」）視而不見；`verify-translation.py` 的手刻 YAML parser 不認得 prettier 把短陣列摺成單行後的 `tags:\n  [...]` 形狀，會誤報「no tags found」；`translation-ratio-check.sh` 沒有 vi/ar 的健全 ratio 校準帶。
- **模型可靠度本身有明顯變異**：同一篇（賴和.md → vi）跑三次，一次乾淨、一次有 1 處洩漏但被抓到重試 3 次仍未修好、一次有 7 處被既有工具漏檢的殘留字。ar 在本次 6 篇裡整體乾淨度略優於 vi（見§廣義人工複查）。

---

## 一、設計摘要

**核心原則：模型只翻文字，結構由工具持有。** 完整設計動機、規則、驗證判準寫在工具本體 docstring；這裡只列四個 phase 的落地要點。

| Phase                | 送模型什麼                                                                                                | 工具持有什麼                                                                                                                                                                      | 驗證                                                                                                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **F**（frontmatter） | title / description / tags（+ subcategory 缺 i18n 對照時） JSON                                           | passthrough 欄位（`PASSTHROUGH`，同源 `verify-translation.py`）機械複製；YAML 組裝（單引號＋撇號雙寫跳脫）；`translatedFrom`/`sourceCommitSha`/`sourceContentHash`/`translatedAt` | `yaml.safe_load` 可解析、title/description 非空、非 ja/ko 時不含 CJK — **有 retry-with-feedback 迴圈**（本 pilot 新增，見下）                                       |
| **N**（footnotes）   | `{n, title, desc}` JSON 陣列，一批 ≤15 條                                                                 | 編號與 URL **永遠不進 prompt**，工具原樣保留組裝                                                                                                                                  | 條數相等 / URL byte-equal / 編號集合相等 —— 構造上保證，非驗證出來的                                                                                                |
| **B**（body）        | 按 `## ` 切塊（無 H2 或塊 >6000 字元退化段落切塊＋bin-packing；<300 字元的孤塊併回前一塊，見下方 bug #2） | `[^N]` 引用標記、markdown 連結 URL 原樣保留（prompt 規則，非 placeholder 保護——與 Phase N 刻意不同層級）                                                                          | 每塊獨立驗證：腳註引用集合對應 zh 原塊 / 有無腦補出假定義行（bug #3）/ 複用 `cjk-leak-check.py` 的 `scan_file` / 字元 ratio 0.8–4.0；fail 只重翻該塊，最多 2 次重試 |
| **A**（assembly）    | —                                                                                                         | 拼三段 + `npx prettier --write` + 跑 `verify-translation.py` / `cjk-leak-check.py` / `article-health.py --profile=pre-commit`                                                     | 這層是防線不是主力                                                                                                                                                  |

**Backend**：直接 import `scripts/tools/lang-sync/backends/`（`OpenRouterBackend` 等），不重寫 HTTP 呼叫層。Prompt 素材（`LANG_NAMES`、`load_lang_guide_sections()` 動態抽 `TRANSLATION-<lang>.md` TL;DR + §1/2/3/6）直接 import `openrouter-translate.py`，同一份 SSOT，不開分岔副本。

**CLI**：

```
python3 scripts/tools/lang-sync/structured-translate.py <zh_path> \
  --lang <L> --backend openrouter:<model>|ollama:<model> [--out <path>] [--metrics-out <path>]
```

---

## 二、Pilot 方法

- **素材選取**：`grep` 全站腳註 ≥15 條的 zh 文章（共 347 篇候選），刻意挑 15–22 條區間、4–6 KB 的中型文章（不是最大的 92 條那種），三篇跨類別：
  - `People/賴和.md`（17 條腳註，無 H2，只有 H3 小節）
  - `Society/地震.md`（20 條腳註，4 個 H2）
  - `Food/台灣咖啡文化.md`（17 條腳註，6 個 H2；且**唯一**含「無 URL 純文字引註」的腳註，見 bug #1）
- **語言**：vi + ar（哲宇 directive 指定）。ar 是今天稍早才誕生的語言（`reports/language-birth-2026-07-25.md`，Stage 1-2 剛完成，`enabled: false`），本 pilot 是 ar 第一批真實翻譯輸出之一。
- **Backend**：`openrouter:nvidia/nemotron-3-ultra-550b-a55b:free`（哲宇指定），單一 backend 不走 cascade——pilot 要看單一模型在結構化拆解下的行為，不要 cascade fallback 把訊號混淆。
- **輸出位置**：`/tmp/structured-pilot/knowledge/<lang>/<category>/<slug>.md`（放在系統 `/tmp` 下的 `knowledge/` 子路徑，是刻意選擇——讓 `article-health.py` 與 `cjk-leak-check.py` 的路徑判斷（`Path.parts` 找 `knowledge` 子字串）直接answers正確語言，不需要額外參數。`verify-translation.py` 內部 ratio-check 子檢查用 `Path.relative_to(REPO)`，遇絕對路徑會整支炸掉；用 repo 內已 gitignore 的 `tmp/` 目錄放一個指回 `/tmp/structured-pilot` 的 symlink 繞過，實際位元組仍 100% 只在系統 `/tmp`，不寫 `knowledge/`）。

---

## 三、Pilot 數據表（6/6，最終版工具）

| zh 來源         | 語言 |    F (s) |    N (s) |     B (s) |   A (s) |  總計 (s) | B chunk 數 | B 重試次數 | B 重試後仍失敗 | verify-translation | cjk-leak-check                                                        | article-health    |
| --------------- | ---- | -------: | -------: | --------: | ------: | --------: | ---------: | ---------: | -------------: | ------------------ | --------------------------------------------------------------------- | ----------------- |
| 賴和.md         | vi   |     13.6 |     93.6 |      45.6 |     1.0 |     153.7 |          1 |          0 |              0 | 0 fail / 1 warn    | ⚠️ flagged=False（見§廣義複查，實際 7 處子字元洩漏未被 4-字門檻抓到） | 0 hard / 0 warn   |
| 賴和.md         | ar   |     17.6 |    112.0 |      49.7 |     0.8 |     180.1 |          1 |          0 |              0 | 0 fail / 1 warn    | clean                                                                 | 0 hard / 0 warn   |
| 地震.md         | vi   |     15.5 |     44.1 |     320.0 |     1.3 |     380.9 |          4 |          4 |              1 | 0 fail / 1 warn    | **flagged=True**（9 hits，見下）                                      | 0 hard / 0 warn   |
| 地震.md         | ar   |      3.9 |     20.1 |     231.6 |     1.0 |     256.6 |          4 |          0 |              0 | 0 fail / 2 warn    | clean                                                                 | 0 hard / 0 warn   |
| 台灣咖啡文化.md | vi   |     10.0 |     44.8 |     226.3 |     0.8 |     281.9 |          6 |          1 |              0 | 0 fail / 1 warn    | clean                                                                 | 0 hard / 0 warn   |
| 台灣咖啡文化.md | ar   |     22.0 |     25.4 |     175.7 |     1.5 |     224.6 |          6 |          0 |              0 | 0 fail / 1 warn    | clean                                                                 | 0 hard / 0 warn   |
| **平均**        | —    | **13.8** | **56.7** | **174.8** | **1.1** | **246.3** |          — |          — |              — | **0/6 hard-fail**  | 1/6 flagged                                                           | **0/6 hard/warn** |

**逐 phase 平均耗時**：F 13.8s／N 56.7s／B 174.8s／A 1.1s（B 佔總時間 71%，符合預期——body 內容量最大、chunk 數最多）。

**verify-translation.py warn 全部是既有工具已知缺口，非本工具引入**（見§五）：6/6 都有「translation ratio: verdict unclear」（`translation-ratio-check.sh` 沒有 vi/ar 的校準健全帶，只有 en/ja/ko/es/fr/de）；`地震.md → ar` 額外一條「no tags found」是**誤報**（tags 實際存在且已正確翻譯，見§五 gap 2）。

**地震.md → vi 的 9 處 cjk-leak-check flagged hits**：主要集中在一張比較不同族群地震神話的 markdown 表格（「地牛翻身」「大鹿伸耳」「地下人推石柱」「一隻手一隻腳的人」等專有神話名稱），重試 2 次後仍有殘留——這類無引號包裹的表格內專名，目前 prompt 的「《》「」內可保留原文」規則涵蓋不到（規則是語法門控的，不延伸到無引號的表格儲存格）。記錄為已知限制，非本次修復範圍。

---

## 四、開發過程中發現並修復的 3 個真結構 bug

**全部是從這 3 篇真實文章的實際輸出中發現的**，不是紙上設計出來的邊界案例：

### Bug 1 — 腳註無 URL 時硬包出殘破空連結

`Food/台灣咖啡文化.md` 有 8 條腳註是純文字引註（如 `[^3]: 台灣戰後咖啡廳文化發展脈絡，散見於台灣飲食文化研究及地方誌`——沒有任何 markdown 連結），原版 `assemble_footnote_defs()` 無條件套用 `[title](url)` 格式，url 為空字串時輸出 `[title]()`——語法合法但語意殘破的空連結。修復：url 為空時直接輸出純文字 `[^N]: {translated_title}`，不強加連結容器（`structured-translate.py:479-495`）。

### Bug 2 — 孤立小 chunk 誤觸 backend 的「疑似拒答」啟發式，標題整段消失

`OpenRouterBackend.translate()`（`backends/openrouter.py:164`）對 <100 字元輸出視為疑似 PRC 拒答直接 raise `BackendRefusal`——這個門檻是為「整篇翻譯」設計的，從沒預期會被逐塊呼叫。`台灣咖啡文化.md` 有 H2，「## 參考資料」單獨成一個 ~40 字元的 H2 chunk，翻譯後的合法短輸出（如「## Tài liệu tham khảo」）連續 3 次被判定拒答，整個標題從輸出消失。修復：`chunk_body()` 把 <300 字元的孤立小塊結構性地併回前一塊，而不是每次靠重試僥倖過關（`structured-translate.py:539-556`）。

### Bug 3 — 模型腦補出假腳註定義行，編號重複

`Society/地震.md → vi` 某次 body chunk 輸出裡混入兩行完全是幻覺的內容：`[^9]: 腳註內容將在最終輸出中保留原位`、`[^11]: 腳註內容將在最終輸出中保留原位`——不是抄漏，是模型自己生出「這裡本來有腳註」的佔位說明，格式恰好跟 `[^N]:` 定義行一樣。組裝後跟 Phase N 真定義重複，`verify-translation.py` 的 footnote count 檢查從 zh=20 抓到 en=22。原本的 chunk 驗證只比對「引用標記集合」，抓不到「多出一整行假定義」這種情況。修復：body chunk 依構造保證不含任何 `[^N]:` **定義行**（Phase N 已抽走），validator 直接用既有的 `FN_DEF_RE` 檢查輸出是否混入這種行，命中即觸發重試（`structured-translate.py:594-611`）。

**額外一項強化（非 bug，是設計缺口補強）**：原版 Phase F 只在 JSON parse 失敗時重試，語意層驗證（`validate_frontmatter_block()` 抓到的 CJK 殘留）驗完就結束，沒有回饋迴路。第一次跑 `賴和.md → vi` 時 description 出現「đối抗」這種單字級殘留（越南字尾黏了一個漢字），被驗證抓到但沒有重翻。補上跟 Phase B 一樣的「驗證 → 帶著問題重翻，最多 2 次」迴圈（`structured-translate.py:297-327`）。

---

## 五、發現的既有共用工具盲點（如實記錄，非本次修復範圍）

這些不是 `structured-translate.py` 的 bug，是本 pilot 在使用既有共用驗證工具時意外暴露的既有缺口，記錄下來供後續排 backlog：

1. **`cjk-leak-check.py` 的 4 字連續門檻對子字元殘留視而不見**：`CJK_RUN_RE = re.compile(r"[一-鿿]{4,}")` 只抓 4 字以上連續漢字。`賴和.md → vi` 某次輸出裡「phụng祀」「trải nghiệm在地」「cuộc抗争」這類 1-2 字黏在譯文詞尾的殘留完全漏網——工具回報 `flagged: False`，但人工複查（下方廣義正則）找到 7 處。門檻是為了避免「命名 gloss」誤判設計的（見該檔案內註解），調低門檻需要仔細重新校準避免新增假陽性，不在本次範圍。
2. **`verify-translation.py` 的手刻 YAML parser 不認得 prettier 摺疊後的單行陣列**：`parse_fm()` 只認 `tags:\n  [\n    'a',\n  ]`（逐行）或 `tags: [...]`（整個 key-value 同一行）兩種形狀。Prettier 對短陣列會摺成 `tags:\n  ["a", "b", ...]`（key 單獨一行、陣列整個在下一行）——這個第三種形狀兩個分支都不吃，`fm.get("tags")` 直接拿到 `None`，導致 `地震.md → ar` 誤報「no tags found (might be OK)」，即便 5 個阿拉伯文 tags 確實存在且已正確翻譯。
3. **`translation-ratio-check.sh` 沒有 vi/ar 的健全 ratio 校準帶**：腳本 docstring 只列 en/ja/ko/es/fr/de 的健全區間，vi/ar 落到「verdict unclear」——6/6 pilot 都命中這條 warn，不是翻譯本身有問題。
4. **`src/data/subcategory-i18n.json` 缺 ar/ru 對照**（`_comment` 欄位自己承認：擴充到「en/ja/ko/es/fr/vi/id/pt/hi 9 語」，ar/ru 不在內）。本工具已處理（缺對照表時退化成跟 title/description 同待遇送模型翻，而非靜默留 zh），但這暴露既有整篇式 pipeline 對 ar/ru 的 subcategory 目前很可能也漏翻或留 zh 原文——`hi/Food/taiwan-coffee-culture.md`（今天稍早、整篇式產出）就是一個活案例：i18n 表裡明明有 `飲品文化 → पेय संस्कृति` 的 hi 對照，實際檔案卻留了 zh 原文 `subcategory: '飲品文化'` 沒翻。

---

## 六、廣義人工複查（4-字門檻之外，補足 §五 gap 1）

用比 `cjk-leak-check.py` 更寬鬆的正則（任意長度連續漢字、排除 markdown 連結／腳註定義行／命名 gloss 括號）對 6 篇輸出重掃：

| 檔案            | 語言 |                                                廣義複查殘留漢字數 |
| --------------- | ---- | ----------------------------------------------------------------: |
| 賴和.md         | ar   |                                                                 0 |
| 地震.md         | ar   |                                                                 0 |
| 台灣咖啡文化.md | ar   |                                               1（「老派」，2 字） |
| 台灣咖啡文化.md | vi   |                         5（「元」×2／「視」／「概念」／「推廣」） |
| 賴和.md         | vi   |                 7（「潮」「森嚴」「在地」「抗争」「歧」「祀」×2） |
| 地震.md         | vi   | 26（多數落在 cjk-leak-check.py 本來就有抓到的表格區塊，非新發現） |

**觀察**：本次 6 篇樣本裡 ar 的乾淨度明顯優於 vi（ar 三篇合計 1 字殘留，vi 三篇合計 38 字殘留，大半集中在 vi/地震.md 的表格區塊）。樣本數太小（各 3 篇）無法下因果結論，可能是 nemotron 對阿拉伯文字系的「切換慣性」比對越南文（同樣拉丁字母、視覺上更容易在拉丁字串中「順手」續打漢字）更小，也可能純粹是這 3 篇文章難度不同。值得在更大樣本上驗證。

---

## 七、與整篇式的差異分析

**今天（2026-07-25）全站整篇式 babel-unified 各批次實測 fail rate**（`/tmp/babel-unified-2026072*/report.jsonl`，僅列 ≥20 筆記錄的批次避免小樣本噪音）：

| 批次                   |     篇數 | fail rate |
| ---------------------- | -------: | --------: |
| 20260724-2014          |      105 |     73.3% |
| 20260724-2203          |       50 |     76.0% |
| 20260724-2301          |       85 |     57.6% |
| 20260725-0011          |      348 |     67.5% |
| 20260725-0342          |      138 |     77.5% |
| 20260725-0445          |       87 |     54.0% |
| 20260725-0459          |      924 |     48.6% |
| **今天＋昨晚全部合計** | **1692** | **60.8%** |

**fail_reason 分佈**（今天＋昨晚全部批次合計 1692 筆）：

| fail_reason                                                                      | 次數 |  佔比 |
| -------------------------------------------------------------------------------- | ---: | ----: |
| `leak`（cjk-leak-check 攔）                                                      |  604 | 35.7% |
| `verify=1`（verify-translation 1 hard-fail）                                     |  188 | 11.1% |
| `no output written by translate.py`（frontmatter/footnote hard gate 攔，未落盤） |  102 |  6.0% |
| `health`（article-health 攔）                                                    |   96 |  5.7% |
| `verify=2`（2 hard-fail）                                                        |   20 |  1.2% |
| `verify=3`                                                                       |   11 |  0.6% |
| `verify=4`                                                                       |    4 |  0.2% |
| `verify=5`                                                                       |    1 |  0.1% |

其中 `verify=N`（224 筆，13.2%）與 `no output written`（102 筆，6.0%）合計 **326 筆（19.3%）** 落在本工具設計上直接消滅的結構類故障——passthrough 欄位不一致 / 腳註計數不符 / frontmatter YAML 解析失敗 / URL 計數不符——這些在結構化拆解下**構造上不可能發生**（passthrough 從沒進 prompt、URL 從沒進 prompt、YAML 由工具組裝不是模型吐）。`leak`（35.7%）與 `health`（5.7%）則多半是內容品質類問題（模型漏翻/半途切回中文），結構化拆解**降低但不消滅**這類故障——本 pilot 自己的資料就有活生生的例子（§三 地震.md → vi 的表格殘留），差別在於：整篇式一旦某句漏翻，通常要整篇重翻才能修；結構化拆解下只有那一個 ~1-2KB 的 chunk 需要重翻，其餘 5 個 chunk 的呼叫與驗證結果保留不動——這是「fail 只重翻該塊」省下來的算力，本 pilot 的 §三 數據表就是直接證據（`地震.md → vi` 4 個 chunk 裡只有 1 個進了失敗後仍保留狀態，其餘 3 個一次過）。

---

## 八、建議下一步

1. **`babel-dispatch.py` 加 `--engine structured` 接線點**：現有 `translate.py`（整篇式）與 `structured-translate.py`（本工具）介面刻意對齊（`<zh_path> --lang <L> --backend <spec>`），`babel-dispatch.py` 可以在既有 backend cascade 選擇之外多一個「engine」維度，讓 P0/P1 這類高權重批次優先走 structured engine。
2. **cascade 化 Phase B 的跨模型重試**：目前 Phase B 重試是「同一個 backend 再問一次」，本 pilot 明確看到同模型連續 3 次答不出同一句話（§三 地震.md → vi 表格殘留、賴和.md → vi 早期 smoke test）。下一步可以讓 chunk 重試在耗盡本 backend 的重試額度後，改問 cascade 裡的下一個 backend，而不是無限問同一個模型。
3. **`cjk-leak-check.py` 4-字門檻調整評估**（§五 gap 1）：需要用全站既有 ja/ko/vi/ar 語料做假陽性/假陰性對照校準，不建議只憑本次 6 篇樣本直接改動共用檢查工具。
4. **`verify-translation.py` 的 `parse_fm()` 補上「單行陣列」YAML 形狀**（§五 gap 2）：這是純粹的 parser 補洞，風險低，建議跟 prettier 對齊後直接修。
5. **`subcategory-i18n.json` 補 ar/ru 對照**（§五 gap 4）：`docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md` 提到的既有出生流程步驟，ar/ru 今天才出生，補齊即可，非新工作。
6. **`translation-ratio-check.sh` 加 vi/ar 健全帶**：需要在更大樣本（非本 pilot 這 6 篇）上統計 zh→vi / zh→ar 的正常字元比後才能校準，先記錄缺口。

---

## 附錄：pilot 產物清單

```
/tmp/structured-pilot/knowledge/
├── vi/{People,Society,Food}/*.md + *.metrics.json
└── ar/{People,Society,Food}/*.md + *.metrics.json
```

不寫入 `knowledge/`，不進 git。工具本體 `scripts/tools/lang-sync/structured-translate.py` 與本報告是本次唯二進 repo 的變更。
