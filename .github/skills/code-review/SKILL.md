---
name: code-review
description: Taiwan.md 的 PR 審查規則。審 taiwan-md 的 pull request 時使用——特別是動到 markdown 渲染、marked 設定、renderer、knowledge/** 內容、或 CI／hook 閘門的改動。內含這個 repo 特有的陷阱（文章不走 Astro markdown pipeline、CJK 強調 flanking、prettier 與 marked 互相打架、刻意保留的字面星號），這些陷阱曾經讓「測試全綠」與「頁面其實壞的」同時成立。
---

# Taiwan.md code review

審查目標不是抓風格，是抓**讀者看得到的壞掉**與**假的綠燈**。

以下每一條都是真實踩過的坑（皆有 commit／頁面可查），不是假想。

---

## 0. 先確定你在審的東西是哪支引擎渲的

**這個 repo 最容易犯的錯，是修一個沒有在跑的設定。**

- 文章頁（`knowledge/**.md` → `/`、`/{lang}/{category}/{slug}/`）**不走 Astro 的 markdown pipeline**。
  `src/pages/[category]/[slug].astro` 直接用 fs 讀檔 + `gray-matter`，交給
  **`src/utils/article-render.ts` 用 `marked`** 渲染。
- 所以動 `astro.config.mjs` 的 `markdown.remarkPlugins` **對文章頁毫無作用**。
  （2026-08-14 有人這樣改，還寫了自己 new 一個 `createMarkdownProcessor` 的測試，
  6 個測試全綠、build 成功、頁面照壞。）

**Review 動作**：任何聲稱修好渲染的 PR，要求證據是 **build 出來的 HTML**
（`dist/**/index.html`），不是作者自己組的 parser。
「我加了測試而且綠了」不構成證據，除非那個測試載入的是正式站在用的實例。

---

## 1. marked 只有一個設定點，而且必須是獨立實例

- 唯一設定點：**`src/utils/marked-cjk.mjs`**，內容是
  `new Marked(markedCjkFriendly())`。
- 站台程式碼**不准**出現 `import { marked } from 'marked'`，一律 import 上面那支。
- **不准**對 marked 模組單例跑 `marked.use()`。單例污染會讓行為變成「誰先 import
  誰決定」的隱性耦合；`cli/src/lib/render.js` 已經對單例跑 `markedTerminal()`
  （它是另一個 npm 套件 `taiwanmd`，自帶 marked，所以目前不同進程——但不要再種一個）。
- `tests/markdown-cjk.test.mjs` 有一條測試斷言全域單例維持原廠行為。
  **看到那條測試被改掉或刪掉，要求解釋。**

**Review 動作**：`grep "from 'marked'"`。除了 `marked-cjk.mjs` 與 `cli/`，出現即退。

---

## 2. CJK 強調（`**`）：不要用移標點的方式「修好」

病根是 CommonMark／GFM 的 delimiter flanking 規則：收尾 `**` 前面是「。」「」」
後面接漢字時不算 right-flanking，整組 `**` 就原封不動印給讀者
（commonmark/commonmark-spec#650，2020 年開到現在）。**這是引擎缺口，不是作者錯字。**

- ❌ 把句末標點搬到強調外面（`**句**。` 取代 `**句。**`）——那會改變哪些字被加粗，
  而且下一位作者照原本語感寫又會壞。
- ❌ 「改用 GFM 就好」——GFM 是 CommonMark 的 strict superset，flanking 規則照抄；
  stock `markdown-it` 同樣會漏。
- ✅ 引擎層修（見 §1）。

**Review 動作**：看到 PR 在內容檔裡搬標點來修粗體，問「引擎修了嗎」。

---

## 3. 字面星號有一部分是刻意的——不要加常駐硬性檢查

全站有 14 處字面星號是**刻意**的，分兩類：

- 塗銷書名：`Memoirs of \*\*\*\*`（多語版都有）
- 審查過的粗話：`F**k`、`f*** …`、`F*** you`、`« **** ta mère »`

（本節刻意不用粗體包住含星號的 code span——那個寫法會讓 prettier 的
delimiter 解析與作者預期不一致，把 code span 裡的星號轉義掉。見 §5。）

- 轉義後的合法字面星號在 AST 裡就是 text node，**做不出**「壞的 vs 刻意的」區分。
- 所以這個 repo **刻意沒有**常駐的 literal-`**` hard gate；守法是
  §1 的 parser contract test。
- 若你要掃描，intentional 白名單至少涵蓋：`\*\*\*\*`、`F\*\*k`、`f\*\*\*`、`F\*\*\*`。
  （少一個大寫變體就會把 `F*** you!` 誤報成缺陷。）

**Review 動作**：看到 PR 新增「文章不得出現 `**`」的 lint／CI 規則 → 退，理由如上。

---

## 4. 標題 renderer：`function`、`parseInline(tokens)`、id 取原文

marked v5+ 的 `text` 是**未解析原文**，直接吐會把 `**` 印進 `<h2>`。

```js
// 必須是 function（要拿 marked 綁的 this.parser），不能是 arrow
renderer.heading = function ({ text, tokens, depth }) {
  const id = text
    .toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[^\w\u4e00-\u9fff-]/g, '')
    .slice(0, 60);
  return `<h${depth} id="${id}">${this.parser.parseInline(tokens)}</h${depth}>`;
};
```

- `id` **必須繼續由原文計算**，否則錨點與既有 TOC 連結會偏移
  （`TableOfContents.astro` 讀 rendered HTML 的 `id` 屬性再 strip tags）。
- 共有 5 支 heading renderer 同款：`src/utils/article-render.ts` +
  `src/lib/semiont-{diary,newsroom,page,weekly}.ts`。**改一支就要改五支。**

**Review 動作**：改了 heading renderer 但沒有錨點不變的證據（h2/h3 帶 id 的數量）→ 要求補。

---

## 5. prettier 會改寫你的修正（lint-staged 是 `prettier --write` 全檔）

`lint-staged` 對**每個** staged 檔跑 `prettier --write --ignore-unknown`。

已知衝突：`**220 millions de NT$**.` 在真實長段落裡，prettier 會把收尾轉義成
`NT$\*\*`（於是又漏字面星號）。prettier-stable 且渲染正確的寫法是
`**220 millions de NT\$**.`（轉義 `$`）。

**Review 動作**：任何動到 `**` 的內容修正，要求作者說明跑過
`npx prettier --check <file>`。沒跑過的修正會在下次 commit 被靜默 revert。

---

## 6. 內容 SSOT 與衍生物

- **SSOT 是 `knowledge/**`**。`src/content/`、`dist/`、`.astro/` 是衍生／gitignored。
- PR 直接改衍生物 → 退。
- `knowledge/` 的 frontmatter 規則（見 `.github/pull_request_template.md`）：
  `author: 'Taiwan.md Contributors'`（不是 AI 名字）、`featured: false`（維護者統一管）、
  canonical `category`、腳註 `[^N]: [標題](URL) — 至少 10 字描述`。

---

## 7. 閘門的真實範圍（別把「綠」讀太寬）

| 閘門                                                                    | 範圍                                                       |
| ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| `.husky/pre-commit` → `article-health.py --staged --profile=pre-commit` | **只驗 staged 檔**                                         |
| `.husky/pre-push`                                                       | 全站 `article-health`（ci-deploy mirror）+ UI 字串語言閘門 |
| `article-health.py --all --profile=ci-deploy`                           | 全站，deploy 用                                            |
| `npm test`                                                              | frontmatter 4407 檔 + markdown parser contract             |

**pre-commit 只驗 staged** 的後果：**你碰到哪個檔，就繼承那個檔的既有債**。
一個純 markup PR 可能被隔壁一個既有的壞 wikilink 擋下來。這是預期行為，
修掉它並在 PR 說明是既有債，不要 `--no-verify`。

跨 domain 的 commit（例如 code + content + ci 同一顆）要在 commit message 加
`cross-domain:` 或 `multi-narrative:` 宣告，否則 pre-commit 會警告
（見 `docs/semiont/SESSION-SCOPE.md`）。

---

## 8. 跨套件邊界：`cli/` 是另一條 release train

`cli/` 是獨立發佈的 npm 套件（`taiwanmd`，自帶 dependencies），
`.github/workflows/npm-publish-cli.yml` 的發佈條件是 **git tag 必須對上
`cli/package.json` 的版號**。

**Review 動作**：站台 PR 夾帶 `cli/package.json` 的版號 bump → 退，
要求拆成獨立 PR。反之亦然。不要讓一個 npm publish 搭便車。

---

## 9. 這個 repo 對 review 意見本身的態度

`CLAUDE.md` §Bias 4：外部 critique 的 default 處置**不是執行**。

對你（reviewer）的意思是：**請給證據與機制，不要給待辦清單**。
一條好的 review 意見長這樣——指出具體壞掉的路徑、說明為什麼現有測試沒抓到、
提出讓它下次自動被抓到的機制。

對作者的意思是：收到意見先驗證再動手；驗證後若不採納，寫下理由。

---

## 快速檢查清單

- [ ] 渲染改動有 **built HTML** 證據，不是自組 processor 的綠燈
- [ ] 沒有新的 `import { marked } from 'marked'`；沒有對單例 `marked.use()`
- [ ] 沒有用搬標點的方式修 CJK 粗體
- [ ] 沒有新增會誤殺刻意字面星號的硬性檢查
- [ ] 改 heading renderer 有錨點不變的證據，且五支同步
- [ ] 動 `**` 的內容修正跑過 `prettier --check`
- [ ] 只改 SSOT（`knowledge/**`），沒改衍生物
- [ ] 跨 domain commit 有 `cross-domain:` 宣告
- [ ] 站台改動沒有夾帶 `cli/` 版號 bump
