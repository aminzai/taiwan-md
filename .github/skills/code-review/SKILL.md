---
name: code-review
description: Review pull requests in this repository. Use when reviewing changes to Markdown rendering, the marked configuration, renderers, knowledge/** content, or the CI and git-hook gates. Encodes the failure modes that have actually shipped here — most importantly the ones where the test suite was green while the reader-facing page was still broken.
---

# Code review

這個 repo 的 review 目標不是抓風格，是抓兩件事：

1. **讀者看得到的壞掉**（字面 `**` 印在頁面上、`<h2>` 裡有星號、終端機有裸標記）
2. **假的綠燈**（測試通過但頁面照壞）

第 2 項是這裡最貴的錯誤，所以放在方法的第一步。

---

## 方法

### 步驟 1：先確定你在審的東西是哪支引擎渲的

**在對任何渲染改動下判斷之前先跑這個。**

```bash
# 文章頁是哪支 renderer 渲的？
git grep -n "from 'marked'" -- src cli
git grep -rn 'remarkPlugins' -- astro.config.mjs
```

`knowledge/**.md` 的文章頁**不走 Astro 的 markdown pipeline**：
`src/pages/[category]/[slug].astro` 用 fs 讀檔 + `gray-matter`，交給
`src/utils/article-render.ts` 的 **marked** 渲染。

**所以動 `astro.config.mjs` 的 `markdown.remarkPlugins` 對文章頁沒有作用。**
2026-08-14 有人這樣改，並且寫了一個自己 `new` 一個 Astro processor 的測試 →
測試全綠、build 成功、頁面照壞，只有掃 `dist/` 的 HTML 才抓到。

**Review 動作**：聲稱修好渲染的 PR，要求證據是 **build 出來的 HTML**。

```bash
# 唯一算數的證據形狀
npm run build   # 或 bash scripts/core/sync.sh && ./node_modules/.bin/astro build
grep -c '\*\*' dist/<那一頁>/index.html
```

「我加了測試而且綠了」不算證據，除非那個測試載入的是**正式站在用的**那個實例。

### 步驟 2：按類別套規則

| 改動類型                                    | 讀哪一份                                                   |
| ------------------------------------------- | ---------------------------------------------------------- |
| CJK 粗體／斜體／刪除線、`**` 相關           | [`reference/cjk-markdown.md`](reference/cjk-markdown.md)   |
| marked 設定、renderer、閘門、SSOT、發佈邊界 | [`reference/taiwan-md-map.md`](reference/taiwan-md-map.md) |

兩份都寫成「規則 / 為什麼（證據）/ 怎麼查（指令）」三段式，
所以你可以現場驗證，而不是相信文件。

### 步驟 3：意見的形狀

`CLAUDE.md` §Bias 4 寫明：外部 critique 的 default 處置**不是執行**。

對 reviewer 的意思是 —— **請給證據與機制，不要給待辦清單**：

- ✅ 指出具體壞掉的路徑 + 為什麼現有測試沒抓到 + 讓它下次自動被抓到的機制
- ❌ 「建議加上錯誤處理」「建議補測試」這種沒有指向的條目

對作者的意思是：收到意見**先驗證再動手**；驗證後不採納，寫下理由。

---

## 文件不要寫會過期的數字

**這份 skill 自己踩過。** 初版寫死了語言版本數、frontmatter 檔數，還斷言
`npm test` 涵蓋 parser contract。Copilot review 一查就有兩項是錯的：語言數字
多算了，而 `npm test` 在 `main` 上只跑 frontmatter 驗證。根因是我把另一個
PR 合併後的狀態寫成了現況。

**規則**：任何數量、檔名清單、腳本內容，寫成**算得出來的指令**，不要寫成數字。
需要數字時，把指令附在旁邊，讓下一個人能重算。

```bash
# ❌ 不要寫「有 6 個 marked 呼叫點」
# ✅ 這樣寫
git grep -c "from 'marked'" -- src cli
```

同理適用於 review 意見本身：引用行為時附上重現指令。

---

## 快速檢查清單

- [ ] 渲染改動附 **built HTML** 證據，不是自組 processor 的綠燈
- [ ] marked 設定改動遵守 [`reference/taiwan-md-map.md`](reference/taiwan-md-map.md) §marked
- [ ] 沒有用搬標點的方式修 CJK 粗體（見 [`reference/cjk-markdown.md`](reference/cjk-markdown.md)）
- [ ] 沒有新增會誤殺**刻意**字面星號的硬性檢查
- [ ] 改 heading renderer 有「錨點不變」的證據，且所有同款 renderer 同步
- [ ] 動 `**` 的內容修正跑過 `npx prettier --check`
- [ ] 只改 SSOT（`knowledge/**`），沒改衍生物
- [ ] 站台改動沒有夾帶 `cli/` 版號 bump（反之亦然）
- [ ] 文件／註解沒有寫死會過期的數字

---

## 給 fork 的人

Taiwan.md 的 fork（Japan.md / Korea.md / 任何 `.md`）如果內容語言也不用空格分詞：

- **[`reference/cjk-markdown.md`](reference/cjk-markdown.md) 可以整份直接拿走。**
  它只講 CommonMark／GFM 的 flanking 規則與各家 parser 的修法，不含本 repo 的路徑。
  日文、韓文、中文都適用。
- `reference/taiwan-md-map.md` 是本 repo 的地圖（路徑、閘門、發佈邊界），
  fork 需要照自己的架構重寫；建議保留三段式與「不要寫死數字」的規則。

skill 的位置也可以換：GitHub Copilot 讀 `.github/skills/`，
Claude Code 讀 `.claude/skills/`，通用 agent 讀 `.agents/skills/` ——
同一份 `SKILL.md` 三邊都吃。
