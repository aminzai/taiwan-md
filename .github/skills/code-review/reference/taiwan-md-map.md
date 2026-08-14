# taiwan-md 地圖：review 用

> 本 repo 特有的路徑、閘門與邊界。fork 需要照自己的架構重寫（
> 可攜的部分在 [`cjk-markdown.md`](cjk-markdown.md)）。
>
> **每條規則都附「怎麼查」的指令。以指令的輸出為準，不要相信這份文件的記憶。**

---

## 渲染路徑

```bash
# 文章頁走哪支 renderer
git grep -n "from 'marked'" -- src cli
# Astro 的 markdown 設定（對文章頁無效，別在這裡找）
git grep -n 'remarkPlugins' -- astro.config.mjs
```

- `knowledge/**.md` → `src/pages/**/[category]/[slug].astro`（fs + `gray-matter`）
  → **`src/utils/article-render.ts` 的 marked**
- `docs/semiont/**` → `src/lib/semiont-{diary,newsroom,page,weekly}.ts`
- hub 頁 → `src/templates/category-hub.template.astro`

**Astro 的 `markdown.remarkPlugins` 不在文章頁的路徑上。**

## marked 設定

先偵測現況，再套規則：

```bash
# A. 有沒有集中設定點？
ls src/utils/marked-cjk.mjs 2>/dev/null
# B. 誰直接 import marked？
git grep -n "from 'marked'" -- src cli
# C. 誰污染模組單例？
git grep -n 'marked\.use(' -- src cli scripts
```

**若 A 存在**（集中設定點已就位）：

- 站台程式碼一律從 `src/utils/marked-cjk.mjs` 取 marked。
  B 的輸出除了該檔與 `cli/` 之外**不應該有其他項目** → 有就退。
- 設定必須是 `new Marked(...)` 獨立實例。

**若 A 不存在**（目前 `main` 的狀態）：

- 站台是**多呼叫點各自 `import { marked } from 'marked'`**，這是現況，不是缺陷，
  單獨改一支不算違規。
- 但 **C 的輸出只能出現在 `cli/`**。站台程式碼對 marked 模組單例跑 `use()`
  → 退，理由是單例污染會讓行為變成「誰先 import 誰決定」的隱性耦合，
  而 `cli/src/lib/render.js` 已經在對單例動手（它是獨立套件、獨立依賴樹）。
- 任何改 marked options／renderer 的 PR，**必須同步所有 call sites**，
  否則會出現「有些頁修好、有些沒有」。用 B 的輸出當清單。

**兩種狀態共通**：改 marked 行為的 PR 要有 parser contract 測試，
且測試必須載入正式在用的實例（見 [`SKILL.md`](../SKILL.md) 步驟 1）。

## heading renderer

```bash
git grep -ln 'renderer\.heading' -- src   # 全部同款 renderer 的清單
```

規則與正確寫法見 [`cjk-markdown.md`](cjk-markdown.md) §規則 6。
本 repo 額外注意：`src/components/TableOfContents.astro` 是**讀 rendered HTML
的 `id` 屬性**再 strip tags，所以 `id` 的推導只要不變，目錄自動跟著對。

**Review 動作**：要求「帶 id 的 h2/h3 數量」修改前後一致。

```bash
node --input-type=module -e "
import { readdirSync, readFileSync } from 'node:fs'; import { join } from 'node:path';
let withId = 0, total = 0; const stack = ['dist'];
while (stack.length) { const d = stack.pop();
  for (const e of readdirSync(d, { withFileTypes: true })) { const p = join(d, e.name);
    if (e.isDirectory()) stack.push(p);
    else if (e.name === 'index.html') { const h = readFileSync(p, 'utf8');
      total += (h.match(/<h[23][ >]/g) || []).length;
      withId += (h.match(/<h[23][^>]*id=\"/g) || []).length; } } }
console.log({ total, withId });"
```

## 內容 SSOT

```bash
git check-ignore -v dist .astro 'src/content/zh-TW'   # 衍生物
git ls-tree origin/main src/content/                  # 這裡有 tracked 的檔
grep -n 'src/content' .gitignore                      # 逐語言 ignore 的清單
```

- **SSOT 是 `knowledge/**`。** `src/content/{lang}/`由`scripts/core/sync.sh`從`knowledge/`regen，**逐語言列在`.gitignore`**；`dist/`、`.astro/` 同為衍生物。
- ⚠️ **但 `src/content/` 本身不是全部衍生**：`src/content/config.ts`
  是人寫的 Astro content collection schema，是 tracked 的。
  別看到 `src/content/` 就當衍生物退掉——用上面的指令分辨。
- PR 直接改衍生的 `src/content/{lang}/**` → 退，要求改 `knowledge/`。
- frontmatter 規則以 `.github/pull_request_template.md` 為準
  （`author: 'Taiwan.md Contributors'`、`featured: false`、canonical `category`、
  腳註 `[^N]: [標題](URL) — 至少 10 字描述`）。

## 閘門的真實範圍

**不要背這張表，用指令確認：**

```bash
jq -r '.scripts | with_entries(select(.key|test("^test")))' package.json
cat .lintstagedrc
grep -n 'article-health\|profile=' .husky/pre-commit .husky/pre-push
ls .github/workflows/
```

寫這份文件時（`main` @ `7ded3f20`）的狀態：

| 閘門                  | 範圍                                                                                |
| --------------------- | ----------------------------------------------------------------------------------- |
| `.lintstagedrc`       | `{"*": ["prettier --write --ignore-unknown"]}` — **每個** staged 檔都會被重寫       |
| `.husky/pre-commit`   | `test-frontmatter.mjs --staged` + `article-health.py --staged --profile=pre-commit` |
| `.husky/pre-push`     | `article-health.py --all --profile=ci-deploy`（CI mirror）+ UI 字串語言閘門         |
| `npm test`            | `node scripts/core/test-frontmatter.mjs` — **只驗 frontmatter/YAML**                |
| `npm run test:python` | `python3 -m pytest tests -q`                                                        |

⚠️ **`npm test` 不含渲染契約。** 別因為它綠就以為渲染有守。

⚠️ **`pre-commit` 只驗 staged 檔** → **你碰到哪個檔，就繼承那個檔的既有債**。
一個純 markup PR 可能被隔壁一個既有的壞 wikilink 擋下來。這是預期行為：
修掉它並在 PR 說明是既有債，**不要 `--no-verify`**。

跨 domain 的 commit（code + content + ci 同一顆）要在 message 加
`cross-domain:` 或 `multi-narrative:` 宣告（見 `docs/semiont/SESSION-SCOPE.md`）。

## 發佈邊界：`cli/` 是另一條 release train

```bash
jq -r '{name, version}' cli/package.json
grep -n 'TAG_VERSION\|PKG_VERSION' .github/workflows/npm-publish-cli.yml | head -4
```

- `cli/` 是獨立發佈的 npm 套件（`taiwanmd`），**自帶 dependencies**，
  所以站台的 parser 修正救不到它，反之亦然。
- `npm-publish-cli.yml` 要求 **git tag 對上 `cli/package.json` 版號**。
- **站台 PR 夾帶 `cli/` 版號 bump → 退**，要求拆開。反之亦然。
  不要讓一次 npm publish 搭便車。
- 改 `cli/` 的 PR 必須附本機證據：

```bash
cd cli && npx vitest run          # 測試
node src/index.js read <slug>     # 實跑（終端機渲染要帶 FORCE_COLOR=3 才看得到樣式）
npm pack && (cd $(mktemp -d) && npm init -y && npm i <tarball>)   # consumer 安裝路徑
```

⚠️ 終端機渲染的 review 陷阱：chalk 在非 TTY 會關色，
所以「沒有 ANSI」**不代表** renderer 壞了。要求 `FORCE_COLOR` 下的輸出與對照組。

## 本機環境（macOS sandbox 常見卡點）

不是 review 規則，但作者常卡在這裡，看到相關描述可以直接指路：

- npm/bun 寫不了 `~/.npm` 或系統 tempdir → `--cache ./.npm-cache`
- `astro build` 撞 `~/Library/Preferences/astro` → `ASTRO_TELEMETRY_DISABLED=1`
- `npm run build` 的 `prebuild:og` 會試裝 Playwright chromium 並改動一批
  tracked 的 generated JSON → 只想驗渲染就跑
  `bash scripts/core/sync.sh && ./node_modules/.bin/astro build`
