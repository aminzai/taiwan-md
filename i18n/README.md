# 🌍 多語系翻譯指南

翻譯任何一篇文章之前，要讀兩份東西：全站通用的品質標準，以及你這個語言自己的規則。

- **[EDITORIAL.md](../docs/editorial/EDITORIAL.md)** — 全站品質標準（適用所有語言）
- **`docs/editorial/per-language/TRANSLATION-{lang}.md`** — 該語言的主權詞表與翻譯規則（**12 個語言都有，這是該語言的 canonical**）
- **`i18n/{lang}/STYLE.md`** — 該語言累積的 reviewer 糾正記憶（目前只有 en 與 ja 長出這一層）

## 先看這裡：每個語言的 canonical 在 `docs/editorial/per-language/`

一個語言的譯名對照、稱呼禁區、常踩的陷阱，canonical 住在 `docs/editorial/per-language/TRANSLATION-{lang}.md`。12 個上線語言每一個都有一份：

```
docs/editorial/per-language/
├── TRANSLATION-en.md   ├── TRANSLATION-pt.md
├── TRANSLATION-ja.md   ├── TRANSLATION-hi.md
├── TRANSLATION-ko.md   ├── TRANSLATION-ar.md
├── TRANSLATION-es.md   ├── TRANSLATION-ru.md
├── TRANSLATION-fr.md   ├── TRANSLATION-de.md
├── TRANSLATION-vi.md   └── TRANSLATION-id.md
```

這份詞表同時餵給人跟機器：翻譯的人照它下筆，品質閘門也拿它當檢查的資料源（per [MANIFESTO §14](../docs/semiont/MANIFESTO.md)）。**找不到你語言的 STYLE.md 不代表沒有規則可讀**——規則在上面這個資料夾。

## `i18n/{lang}/STYLE.md` 是累積糾正的第二層

STYLE.md 不是靜態規則，是**自動翻譯系統的語言記憶體**：每次翻譯產出 → reviewer 糾正 → 錯誤回寫到 STYLE.md → 下次翻譯自動避開。

這一層需要有母語 reviewer 持續回寫才長得出來，所以**目前只有兩個語言有**：

```
i18n/
├── README.md          ← 你在這裡
├── en/STYLE.md        ← 英文累積規則
└── ja/STYLE.md        ← 日文累積規則
```

其他 10 個語言還沒有這一層。你的語言沒有，就讀 `docs/editorial/per-language/TRANSLATION-{lang}.md`；翻譯過程中被 reviewer 糾正出可重複的錯誤模式，歡迎順手替你的語言開第一份 STYLE.md。

### STYLE.md 應包含什麼

1. **台灣專有名詞對照表** — 地名、人名、機構名在該語言的標準譯法
2. **文化脈絡補充規則** — 哪些概念需要為該語言讀者額外解釋
3. **語氣與風格** — 該語言的策展人聲音應該怎麼表達
4. **常見錯誤（持續累積）** — 每次 reviewer 糾正後回寫，避免重複犯錯
5. **Reviewer 名單** — 該語言的母語審核者

## 自動進化機制

```
翻譯 cron/contributor 翻譯文章
  → 讀 docs/editorial/EDITORIAL.md
    + docs/editorial/per-language/TRANSLATION-{lang}.md（canonical）
    + i18n/{lang}/STYLE.md（若該語言已有）
  → 產出翻譯
  → 母語 reviewer 審核、糾正
  → 錯誤模式回寫到 STYLE.md「常見錯誤」區
  → 下次翻譯自動讀取 → 不再犯
```

## 這份 README 有閘門看著

上面兩個清單列的檔案必須真的存在。`tests/test_translation_guide_pointers.py` 會對照 `src/config/languages.mjs` 的語言登記表檢查三件事：每個上線語言都有 canonical 詞表、本檔與 `docs/prompts/TRANSLATE_PROMPT.md` 提到的每個 `i18n/{lang}/STYLE.md` 都存在、兩份入口文件都指得到 canonical 資料夾。

閘門存在的理由是這份 README 曾經畫出一棵有 8 個 STYLE.md 的目錄樹，其中 6 個從來沒有被建立過，而 canonical 詞表一個字也沒被提到。一個送過 98 個 PR 的貢獻者照著它去找印尼文那份 STYLE.md，找不到，於是得出「印尼文沒有指引」的結論——那份指引其實一直在 `docs/editorial/per-language/TRANSLATION-id.md`。

## Token Donation 翻譯流程

詳見 [Discussion #137](https://github.com/frank890417/taiwan-md/discussions/137)
