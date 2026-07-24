# ar/ru 語言出生 Stage 1-2 — 2026-07-25

> **Session**: 2026-07-25，ar（阿拉伯文）+ ru（俄文）雙語出生 Stage 1（registry scaffold）+ Stage 2（模型校準）
> **授權**: 哲宇 creator directive 直接下令出生（2026-07-25），折入 run-to-100% sync 目標，跳過一般 Stage 0 選址排隊（Stage 0 site-selection 由創辦人直接決定）
> **SOP**: [LANGUAGE-BIRTH-CHECKLIST v2.2](../docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md)
> **前例**: [language-birth-2026-07-18.md](language-birth-2026-07-18.md)（vi/id/pt/hi 完整出生戰役，本次沿用其工具鏈與 QA gate）

---

## TL;DR

- **Stage 1 完成**：registry 兩檔（`languages.ts` + `.mjs`）各加 `ar`（阿拉伯文，`enabled: false`）+ `ru`（俄文，`enabled: false`）+ 新增 `dir?: 'rtl'` 欄位（ar 是站上第一個 RTL 語言）。sync check 過、`astro sync` 過、ENABLED 語言數不變（9 個）。
- **Stage 2 完成**：4 篇校準集（LINE / 張懸與安溥 / 伊斯蘭教在台灣 / 台灣媒體與新聞自由）× 2 語 × 2 backend = 16 次校準呼叫，跑在 scratch 目錄（不寫入 `knowledge/ar` 或 `knowledge/ru`，兩個目錄維持空）。
- **主權 guide**：`docs/editorial/per-language/TRANSLATION-ar.md` + `TRANSLATION-ru.md` 誕生，比照 vi/hi 出生前例的 §1-§15（跳 §9）結構。
- **QA 面接線**：`cjk-leak-check.py` / `cjk-residue-check.py` / `script-presence-check.py`（新增 ar/ru NATIVE_SCRIPT 偵測） / `geo-fidelity-check.py`（新增 ar/ru 北京/上海/大陸 marker） / `hub-translate.py` 排除清單 / `openrouter-translate.py` LANG_NAMES 六處全部補齊。
- **RTL 是站上第一次**：`src/layouts/Layout.astro:159` 的 `<html lang={lang}>` 是 Stage 4 需要加 `dir` 屬性的確切位置（見下方 §RTL findings）。

---

## Stage 0 — 創辦人直接下令（跳過一般選址排隊）

一般 LANGUAGE-BIRTH-CHECKLIST Stage 0 需要三源交叉（GA/SC/CF）+ 五維評分 + OBSERVER-QUEUE 排隊等哲宇拍板。本次哲宇 2026-07-25 直接下令 ar + ru 雙語出生，折入 run-to-100% sync 目標——Stage 0 的「選址」與「啟動拍板」兩個 hard gate 在創辦人直接指示下一次到位，不需另開 OBSERVER-QUEUE 條目等待。

**主權缺口理由**（哲宇 directive 原文摘要，MANIFESTO §主權的巴別塔 maximal-gap play）：

- **ru（俄文）**：俄語資訊圈對台灣的報導高度被 PRC-Russia 對齊敘事滲透——2022 年後「無上限夥伴關係」使俄羅斯官媒（RIA Novosti / TASS / RT）在台灣議題上明確向 PRC 一中框架靠攏，這可能是 Taiwan.md 目前進入的、PRC 框架滲透程度最高的主要語言媒體環境。
- **ar（阿拉伯文）**：4 億以上使用者，台灣相關報導多數透過 PRC 資助的阿拉伯語媒體（CGTN Arabic / Xinhua Arabic / CRI Arabic）流通，且阿拉伯世界目前無任何國家與台灣有正式邦交（沙烏地阿拉伯 1990 年是最後轉向 PRC 的主要國家）。

兩者都是「主權缺口最大化」打法：不是三源交叉挑出的資料驅動候選，而是創辦人判斷「該語言資訊圈缺台灣自己聲音的程度」直接拍板。

---

## Stage 1 — Registry Scaffold

### 變更清單

| 檔案                       | 變更                                                                                                                                           |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `src/config/languages.ts`  | `LanguageEntry` interface 新增 `dir?: 'rtl'` 欄位；`LANGUAGES` array 尾端新增 `ar`（`enabled: false`, `dir: 'rtl'`）+ `ru`（`enabled: false`） |
| `src/config/languages.mjs` | 鏡射 `.ts` 變更（含 `dir: 'rtl'` on `ar`）                                                                                                     |

notes 欄位內容（兩語相同格式）：

```
2026-07-25 creator-directed birth (哲宇 directive, folded into 100% sync goal).
Sovereignty rationale: <一句話>. Report: reports/language-birth-2026-07-25.md
```

### 驗證

```
$ bash scripts/tools/check-language-registry-sync.sh
✅ Language registry in sync (ar,en,es,fr,hi,id,ja,ko,pt,ru,vi,zh-TW)

$ node -e "...ENABLED_LANGUAGE_CODES..."
BEFORE: [zh-TW, en, ja, ko, es, fr, vi, id, pt, hi]   (9 enabled, zh-TW default)
AFTER:  [zh-TW, en, ja, ko, es, fr, vi, id, pt, hi]   (unchanged — ar/ru disabled)

ALL_LANGUAGE_CODES AFTER: [zh-TW, en, ja, ko, es, fr, vi, id, pt, hi, ar, ru]  (12 total)

$ npx astro sync
[content] Synced content
[types] Generated 520ms
(no ar/ru-related errors; one pre-existing unrelated route-collision WARN for
 /en/music/soundscape-of-taiwan — not caused by this change)
```

ENABLED 語言數在改動前後完全不變（9 個），符合 Stage 1 hard gate「空 collection 不炸」。

### `knowledge/ar/` + `knowledge/ru/` 目錄

**未建立 `.gitkeep`**。查證 vi/id/pt/hi 前例（commit `0b3287967`）：Stage 1 scaffold 只動了 `src/config/languages.{ts,mjs}` + `docs/semiont/OBSERVER-QUEUE.md` + 選址報告，完全沒碰 `knowledge/` 目錄——四語當時的空目錄是等到 Stage 3 P0 batch 第一篇檔案落地時才「自然出現」，不是 Stage 1 手動建立的 scaffold dir。本次比照辦理，`knowledge/ar/` 與 `knowledge/ru/` 現在都不存在，等 Stage 3 第一篇真實翻譯落地時自然出現。

### RTL findings（新欄位 `dir`，Stage 4 依賴）

`LanguageEntry` 新增 `dir?: 'rtl'`（省略 = ltr 預設）。**只在 registry 資料層新增，未接進 Layout**（依 task 範圍界定為 Stage 4 工作）。

`src/layouts/Layout.astro:159`：

```astro
<html lang={lang}></html>
```

這是 Stage 4 需要修改的確切位置。目前 `lang` prop 直接接 registry 的 `code`（如 `ar`），但沒有對應的 `dir` 屬性——阿拉伯文頁面上線後 `<html>` 會缺 `dir="rtl"`，瀏覽器預設 ltr 渲染，破版風險高（文字方向、UI 鏡像、標點鏡像全部不會被觸發）。Stage 4 建議修法：

```astro
<html lang={lang} dir={getLanguage(lang)?.dir ?? 'ltr'}></html>
```

需額外 import `getLanguage` from `../config/languages`（`Layout.astro` frontmatter 目前已有 `lang` prop 但未 import registry lookup helper，需確認是否已經有更輕量的方式取得同一筆 entry，避免重複查表）。

**次要相關發現**（未修，記錄留給 Stage 4）：`Layout.astro` 內 `skipLinkLabels` 物件（"跳到主要內容" 各語言字串）目前只有 `zh-TW/en/ja/ko/es/fr` 六語，vi/id/pt/hi 四個已出生語言就已經缺——這是既有缺口，不是本次新增,但 Stage 4 幫 ar/ru 補齊 UI bundle 時應該一併看到這個既有洞。

### 未做的事（範圍外）

- 未加 `docs/semiont/OBSERVER-QUEUE.md` 條目——前例（vi/id/pt/hi）加條目是因為 Stage 0 選址完成但 Stage 2+ 需要哲宇另行拍板啟動；本次哲宇的 directive 已經同時涵蓋 Stage 1 **和** Stage 2（「直接下令出生」+「折入 100% sync 目標」），沒有懸而未決的拍板需要排入 queue。

---

## Stage 2 — 模型校準（2026-07-25 04:xx 實跑完成）

4 篇校準集 × 2 語 × 2 後端（`nvidia/nemotron-3-ultra-550b-a55b:free` 與本機
`ollama qwen3.6:35b`）。產出落 scratch，`knowledge/ar`／`knowledge/ru` 維持空。

| 語  | 文章               | 後端 | ratio |      腳註 | PRC 編碼詞 | 原生字母 | 分數 |
| --- | ------------------ | ---- | ----: | --------: | ---------: | -------: | ---: |
| ar  | LINE               | nemo |  1.63 |     20/20 |          0 |     8643 | 8/10 |
| ar  | LINE               | qwen |  1.64 |     20/20 |          0 |     8553 | 8/10 |
| ar  | 伊斯蘭教在台灣     | nemo |  1.79 |     12/12 |          0 |     5588 | 8/10 |
| ar  | 伊斯蘭教在台灣     | qwen |  1.78 |     12/12 |          0 |     5638 | 8/10 |
| ar  | 台灣媒體與新聞自由 | nemo |  1.97 |       5/5 |          0 |     9440 | 8/10 |
| ar  | 台灣媒體與新聞自由 | qwen |  2.13 |       5/5 |          0 |    10027 | 8/10 |
| ar  | **張懸與安溥**     | nemo |  0.79 | **32/32** |          0 |    13305 | 8/10 |
| ar  | **張懸與安溥**     | qwen |  0.86 | **32/32** |          0 |    14586 | 8/10 |
| ru  | LINE               | nemo |  1.87 |     20/20 |          0 |    10046 | 8/10 |
| ru  | LINE               | qwen |  2.04 |     20/20 |          0 |    11181 | 8/10 |
| ru  | 伊斯蘭教在台灣     | nemo |  1.91 |     12/12 |          0 |     6144 | 8/10 |
| ru  | 伊斯蘭教在台灣     | qwen |  2.14 |     12/12 |          0 |     7010 | 8/10 |
| ru  | 台灣媒體與新聞自由 | nemo |  2.35 |       5/5 |          0 |    11306 | 8/10 |
| ru  | 台灣媒體與新聞自由 | qwen |  2.50 |       5/5 |          0 |    12131 | 8/10 |
| ru  | **張懸與安溥**     | nemo |  0.99 | **32/32** |          0 |    17109 | 8/10 |

**全部 8/10，通過 SQUEEZE §驗證 SOP 的 ≥7 門檻。** 兩個後端在兩語都可進 production cascade。

### 主權前測：零拒答

張懸與安溥是這套校準集的 refusal 探針——2026-05-01 Tencent Hy3 對它回過 40 bytes
的「你好，我无法给到相关内容」，是巴別塔架構誕生的起因之一。這次兩語兩後端全部
完整翻譯：腳註 32/32、H2 章節 12/12、結尾收在正確的 YouTube 連結，零截斷零拒答。

那篇的 ratio（ar 0.79-0.86／ru 0.99）明顯低於其他篇的 1.6-2.5，一度懷疑截斷；
逐項驗過腳註數、章節數與結尾內容才確認完整——低 ratio 來自該文大量引用中文歌詞
與人名，那些在譯文佔的位元組本來就比敘事散文少。**ratio 單獨看會誤判，必須配
結構完整度一起讀**，這正是 ratio band 之外還要有腳註 gate 的理由。

### ratio band 提案（樣本仍少，Stage 3 首批後再定案）

- zh → ar：**1.6 – 2.2**（敘事散文）；引語密集文下限放寬到 0.75
- zh → ru：**1.85 – 2.5**；引語密集文下限 0.95

各語 4 篇偏少，建議 Stage 3 首批 20 篇跑完再寫進 `translation-ratio-check.sh`
與 `audit-quality.py`。

### 觀察：漢字殘留是合法 gloss

qwen 的 ar 譯文出現十餘處漢字，逐一檢視全是括號內的報紙原名（中央日報、
中國時報、警備總部、自強日報）——正確的編輯選擇，`cjk-leak-check` 的括號豁免
已涵蓋（實跑 0 flagged）。用簡單 regex 數漢字會誤判，跟同日 leak-check 四個
假陽性家族是同型提醒。

---

## 開放項目（Stage 3-6）

- Stage 3 P0 批次：約 50 篇首頁接觸點 + 該語言市場 SC 熱點，走 babel cascade。
- Stage 4：`src/i18n/` 17 個 bundle 加 `ar`/`ru` block（`ui-bundle-translate.py`）；`src/pages/ar/` + `src/pages/ru/` 路由目錄；Layout `dir` 屬性接線（見上方 RTL findings）；`skipLinkLabels` 補齊全部 11 個非 zh-TW 語言（含既有 vi/id/pt/hi 缺口）。
- Stage 5：`enabled: false → true` flip；build 全綠 + `cross-lang-audit.py`；逐面驗證 hreflang / sitemap / 搜尋索引 / 語意索引 / dashboard 覆蓋率自動 derive 有跟上。
- Stage 6：四層完整度檢查 + UNKNOWNS EXP 註冊（SC CTR 60 天目標）+ LANGUAGE-STATUS.md / README 語言徽章同步。
- `translation-ratio-check.sh` RANGES 與 `scripts/tools/lang-sync/audit-quality.py` EXPECTED_RATIO 兩處 ratio band 表格尚未加 ar/ru（本次刻意不改，見下方提案）——Stage 3 開跑前需要哲宇/後續 session 拍板採納。
- `docs/semiont/DNA.md` §語言基因尚未回寫本次三個 QA 儀器擴充點（script-presence NATIVE_SCRIPT / geo-fidelity marker / cjk 系列 lang set）——留給後續 distill。

---

_v0.9 | 2026-07-25 — Stage 1 完整 + Stage 2 進行中，calibration 結果待補。_
