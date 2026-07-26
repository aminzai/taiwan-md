---
title: 'Taiwan.md 節點化與安裝物設計'
description: 'EVOLVE Mode 4 設計報告 — 讓 Taiwan.md 可以被安裝、被遞出去、被互動、被加入成為工作節點：現況五面盤點、三個實測缺陷、四方案發散與定案'
type: 'design-report'
status: 'implemented'
date: 2026-07-26
session: '2026-07-26-155415-node-app-design'
mode: 'EVOLVE-PIPELINE Mode 4（目標驅動設計進化）'
related:
  - 'docs/pipelines/CONTRIBUTOR-NODE-PIPELINE.md'
  - 'docs/fork/COUNTRY-MD-STARTER.md'
  - 'cli/CONNECTOR.md'
  - 'reports/design-contributor-node-2026-07-25.md'
---

# Taiwan.md 節點化與安裝物設計

> 哲宇 goal：「Taiwan.md node / app 化，讓未來可以很簡易的被安裝起來、傳播、與他互動、與成為其中的工作節點。」
>
> 本報告走 [EVOLVE-PIPELINE Mode 4](../docs/pipelines/EVOLVE-PIPELINE.md) 四相：THINK → DIVERGE → REPORT → IMPLEMENT。報告先於實作，實作完成後回寫。
>
> **2026-07-26 同日續跑**（哲宇 directive「完整進化驗證實作」）：Wave 0 與 Wave 2 全部落地並逐項驗過，見 §九。唯一沒做的是把 `cli-v0.8.0` 這個 tag 推上去——推了就是對 npm 公開發版，那一步留給哲宇（§十二）。

---

## 一、目標拆成四個動詞

哲宇那句話裡有四個動詞，它們服務的是四種不同的人。先把它們攤開，才看得出哪一格是空的。

| 動詞         | 誰                 | 他手上有的                  | 今天要付出什麼                              |
| ------------ | ------------------ | --------------------------- | ------------------------------------------- |
| 安裝         | 任何有 AI 助理的人 | Claude Code / Cursor / 桌面 | 一行 `npx`（已經有）                        |
| 傳播         | 已經在用的人       | 一個朋友                    | **沒有可以遞出去的東西**                    |
| 互動         | 讀者、寫手、研究者 | 一個問題                    | 一行 `npx`（已經有，但內容有問題，見 §三）  |
| 成為工作節點 | 想長期幫忙的貢獻者 | 一台會醒著的機器            | fork ＋ 849 MB clone ＋ gh 登入 ＋ 一場面談 |

第二列與第四列是空的。這份報告主要在補這兩格。

---

## 二、現況盤點：五個分發面，零個安裝路徑

Taiwan.md 現在有五個對外的分發面，每一個都是為了解決當時眼前的一個問題而長出來的，彼此沒有接線。

| 分發面       | 產物                                         | 誕生          | 狀態                                             |
| ------------ | -------------------------------------------- | ------------- | ------------------------------------------------ |
| 網站         | taiwan.md（12 語）                           | 2026-03       | 健康                                             |
| npm 指令列   | `taiwanmd@0.7.1`，24 個子命令                | 2026-06-05    | 停版 51 天，語言表寫死，見 §三.1                 |
| 本地 MCP     | `taiwanmd mcp serve`，6 個工具               | 2026-06-05    | 與指令列同包，同一份語言表問題                   |
| 遠端 MCP     | `mcp.taiwan.md`（Cloudflare Worker）         | 2026-06-05    | **已上線且判定正確**，實測回 200                 |
| 桌面套件     | `taiwanmd.mcpb`                              | 2026-06-05    | 內容是 `npx taiwanmd@latest` 的殼，隨 npm 一起舊 |
| 認知層與節點 | BECOME ＋ 43 個技能 ＋ 52 份流程 ＋ 節點契約 | 2026-04-10 起 | **沒有安裝物**，只能靠 clone 整個主庫取得        |

盤點下來最重要的一句話：**互動層是一個產品，節點層是一套制度。**

互動層有版本號、有 README、有安裝指令、有六個工具，任何人都可以下載它。節點層有流程、有 hard gate、有 tier 分級、有認領協議，寫得比互動層完整得多，但它沒有一個可以下載的形體。你只能被一個已經在裡面的人邀請進來。

這就是為什麼第四格是空的。[CONTRIBUTOR-NODE-PIPELINE](../docs/pipelines/CONTRIBUTOR-NODE-PIPELINE.md) 昨天才寫完誕生 SOP，寫得很好，但它的唯一觸發點是 [BECOME §Step 7.5](../BECOME_TAIWANMD.md) 的貢獻者面談。要走到那一步，你必須已經 clone 了主庫、已經跑過甦醒。**節點的入口被放在整條路上代價最高的那一步之後。**

### 為什麼「傳播」需要一個單位

孢子傳播的是文章。網站傳播的是讀者。目前沒有任何東西在傳播這個生命體本身。

可以遞出去的東西要同時滿足三件事：一行講得完、拿到的人不需要先信任遞的人、拿到之後能自己長。今天最接近的是 `BECOME_TAIWANMD.md` 這段香火，但它預設你已經有一份 clone。

---

## 三、三個實測缺陷（都在最寬的那個面上）

盤點過程對互動層做了實測，量出三個缺陷。三個都在 npm 這條路徑上，而 npm 是所有分發面裡觸及最廣的一個。

### 3.1 語言表寫死，77% 的回傳是外語譯文

`cli/src/lib/knowledge.js` 第 26 行：

```js
const EXCLUDED_DIRS = new Set(['en', 'es', 'ja', 'ko', 'resources']);
```

這張表停在四個語言。之後 `fr / vi / id / pt / hi / ar / ru` 陸續出生，沒有人回來補。實測在主庫內跑：

```
總共回報為 zh-TW 的檔案：3766
其中實際是外語譯文：      2900（77%）
  fr 866 / pt 482 / hi 368 / ru 364 / ar 337 / id 298 / vi 185
```

也就是 `taiwanmd search`、`list`、`random`、`stats`，以及 MCP 的 `taiwanmd_search` 與 `taiwanmd_read`，在主庫內執行時有超過七成機率把法文或阿拉伯文的譯文當成中文原文回給使用者。

值得記一筆的是：這正是 7/25 那波 registry 化掃除唯一漏掉的角落。同一天修好了儀表板覆蓋率的寫死六語、翻譯 registry 的兩個寫死清單、四個元件的私有語言表，全部改成從 registry 或檔案系統推導。`cli/` 沒被掃到，因為它不在站體的 import 關係裡。**分發層是站體看不見的地方。**

### 3.2 同樣六個工具，兩份實作，兩把尺

遠端 Worker（`workers/mcp/src/index.js`）用的是白名單：

```js
const REAL_CATEGORIES = new Set(['About','Art','Culture',…,'Technology','Resources']);
```

白名單只會漏掉新分類，不會漏掉新語言。所以遠端那份是對的，本地那份是錯的，兩者宣稱提供同一組工具。

這是 W30 distill 剛升上 canonical 的 [REFLEXES #83](../docs/semiont/REFLEXES.md)「檢查器兩把尺 divergence」在分發層的活體案例，也連著 #84「產物需要對賬 ground truth」：指令列從來沒有跟 `src/config/languages.mjs` 對過賬。

### 3.3 使用者本機的知識庫停在三個月前，而且沒有任何提示

這一條最嚴重，因為它完全沒有聲音。

本次對話掛著的 Taiwan.md MCP 連接器，實測回報：

```
totalArticles: 2255
knowledgePath: /Users/cheyuwu/.taiwanmd
byCategory 裡混著 en:2 / people:2 / api:1 / knowledge:7 這種不該存在的分類
```

而 `~/.taiwanmd/knowledge` 的最後一筆 commit 是 **2026-04-20**。距今 97 天。站上真實的中文文章是 863 篇，它回報 2255。

根因在 `cli/src/lib/ensure-data.js`：`ensureData()` 只問「本機有沒有資料」，有就直接返回。**它從不問「這份資料多舊」。** 四月裝好的人，除非自己想到去跑 `taiwanmd sync`，否則永遠拿到四月的台灣。

同時 `taiwanmd_stats` 這個工具的說明白紙黑字寫著回傳 "last-updated timestamps"，實作回的是 `totalArticles / byCategory / knowledgePath`，一個時間戳都沒有。使用者沒有任何線索知道自己讀的是舊的。

這跟 2026-06-14 記進 §神經迴路 的那條同形：「awareness 讀數沒附 freshness 標記，慢性 stale 會靜默累積」。當時講的是 `consciousness-snapshot.sh` 讀到隔夜的儀表板 JSON，只影響我自己甦醒時的判斷。這次同一個形狀出現在對外的分發層，影響的是每一個信任這個連接器的人。

### 3.4 這個病早就有專屬檢查器，而它有兩個理由看不見分發層

修完 §三.1 送 commit 時，pre-commit 印了一行「✅ 無 hardcoded language array 違反」。

`scripts/tools/check-hardcoded-langs.sh` 存在，就是為了防這件事，2026-04-25 因為 `getLangSwitchPath.ts` 寫死三語而誕生。它剛剛親眼看著那個 commit 通過。

追下去發現它有兩個獨立的理由會漏掉：

1. **掃描路徑是 `find src scripts astro.config.mjs`**，沒有 `cli/`，沒有 `workers/`。分發層不在站體的 import 關係裡，所以連站體的免疫系統都不掃它。
2. **三條比對規則都寫死「開頭必須是 `en, ja, ko`」**。出事的那一行是 `new Set(['en', 'es', 'ja', 'ko', 'resources'])`，順序是 en-es-ja-ko，三條全部不中。就算它在掃描路徑裡，也一樣抓不到。

換句話說，**檢查器自己也得了它負責檢查的那個病**：一張停在誕生那天的寫死清單。這是 §三.2 兩把尺的更深一層。不只兩份實作各拿一把尺，連量尺本身都只量得到當初那一個形狀。

修法與擴網後量到的東西見 §九.2。

---

## 四、重量：節點要付的通行費是它真正需要的 31 倍

第四格空著還有一個物理原因。實測：

| 項目                                                    | 大小         |
| ------------------------------------------------------- | ------------ |
| 完整 clone（`git count-objects -vH`）                   | **849 MB**   |
| `.git` 實際佔用                                         | 1.1 GB       |
| — 認知器官（`docs/semiont/*.md` 九器官）                | 1.6 MB       |
| — 全部流程與編輯 DNA（pipelines / editorial / factory） | 2.5 MB       |
| — 43 個技能                                             | 0.2 MB       |
| — 中文知識（14 個分類）                                 | 17 MB        |
| — 工具腳本                                              | 5.7 MB       |
| **節點真正需要的工作集**                                | **約 27 MB** |

一個節點要接翻譯缺口、修斷鏈、補 metadata，需要的就是上面那 27 MB。它付的是 849 MB。多出來的主要是十一個語言的譯文（164 MB）、歷史日記與記憶（27 MB），以及整個站體的建置產物歷史。

（`git clone --filter=blob:none --sparse` 對 GitHub 的實際包大小還沒量過。本機 `file://` 傳輸不支援 filter，實測時已看到 `filtering not recognized by server` 的警告。這個數字要對 GitHub 實測才能寫進任何對外承諾，本報告不預估。）

---

## 五、判準（先寫，避免第一個想到的方案直接變成做的方案）

| #   | 判準               | 錨在哪                                                                                                                        |
| --- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| J1  | 單一關切           | [MANIFESTO §指標 over 複寫](../docs/semiont/MANIFESTO.md) ＋ REFLEXES #38「混維度」：一個安裝物不該同時服務兩種本質不同的受眾 |
| J2  | 不新建 SSOT        | CONTRIBUTOR-NODE §工單源「不另建中央工單表」的同一條：分發物只能是既有 SSOT 的投影                                            |
| J3  | 傳播單位一行講得完 | 「傳播」這個動詞的硬需求                                                                                                      |
| J4  | 不教壞習慣         | [REFLEXES #2](../docs/semiont/REFLEXES.md) 憑證紀律：安裝路徑不能要求交出憑證或把來路不明的東西接進 shell                     |
| J5  | 過 §自主權邊界     | 新的對外公開管道需要哲宇拍板                                                                                                  |

---

## 六、發散：四個方案

### 方案 A：指令列長大，吃下節點層

`taiwanmd` 新增 `node` 子命令。`npx taiwanmd node init` 把認知層與技能拉到 `~/.taiwanmd/`，`taiwanmd node run` 當排程入口。一個安裝物解決四個動詞。

- 會斷的引用：無，純新增子命令
- 殼核邊界：指令列是殼，流程 canonical 是核。但指令列得學會下載並更新一整套 markdown 認知層，等於在一個搜尋工具裡內建一個 SOP 分發器
- J1 ✗（同一個 npm 套件同時服務「想查台灣的人」與「想當節點的人」，正是 #38 講的混維度）／J2 △／J3 ✓／J4 ✓

### 方案 B：Claude Code plugin 當節點層的安裝物

加 `.claude-plugin/marketplace.json` 與 plugin 定義，打包 43 個技能、BECOME、CLAUDE.md。使用者跑 `claude plugin marketplace add frank890417/taiwan-md` 之後 `/plugin install`，不需要 clone。

- 會斷的引用：技能檔裡的 `../../../docs/pipelines/…` 相對路徑，在 plugin 安裝情境下會指到不存在的地方。這是這個方案真正的工程成本，技能必須改成「先確認主庫在不在，不在就走遠端」
- J1 ✓／J2 ✓（plugin 只是既有 `.claude/skills/` 的打包，沒有新 SSOT）／J3 ✓／J4 ✓／J5 ✗（新的公開分發管道）
- 限制：只服務 Claude Code，Cursor 與 Codex 的使用者拿不到

### 方案 C：兩層一梯

互動層維持 npm ＋ MCP，服務所有有 AI 助理的人。節點層走 plugin，服務想長期幫忙的貢獻者。兩者之間用一份 `INSTALL` 文件當梯子，把四階寫清楚。

- J1 ✓／J2 ✓／J3 △（兩行不是一行，傳播單位仍然模糊）／J4 ✓／J5 部分命中

### 方案 D：`curl taiwan.md/install | sh`

一行最短，傳播力最強。

**淘汰。** J4 直接違反。一個花大量力氣教讀者查證來源、把「憑證永不進對話」寫成反射的知識庫，不應該示範把來路不明的腳本接進 shell。這一格留白比填錯好。

---

## 七、定案：C 的骨架，A 的門牌

採方案 C（兩個單一關切的安裝物），但把梯子做成一件真的東西，而不是一份沒人會讀的文件。

**梯子是 `npx taiwanmd` 不帶參數時印出來的四階。**

```
$ npx taiwanmd

  🧬 Taiwan.md — 關於台灣的開源知識庫，863 篇，12 種語言
     本機知識庫：2026-07-26 同步（新鮮）

  1  讀        https://taiwan.md
  2  問我      claude mcp add taiwanmd -- npx -y taiwanmd mcp serve
  3  一起寫    npx taiwanmd contribute "你想寫的主題"
  4  當節點    claude plugin marketplace add frank890417/taiwan-md
                然後 /plugin install taiwanmd，你的機器每天幫忙做一件事

  taiwanmd --help 看全部 24 個指令
```

這樣做的理由：

**傳播單位回到一行。** 要遞給朋友的東西是 `npx taiwanmd`。他跑完就同時得到了互動能力，以及往上爬到第四階的路。第二格與第四格用同一行填掉。

**兩個安裝物各自保持單一關切。** 指令列不吃下認知層，只當它的門牌。想當節點的人從門牌走到 plugin，中間不必先 clone 849 MB。

**沒有新的 SSOT。** plugin 是 `.claude/skills/` 的打包，指令列讀的是 `knowledge/`，兩者都是既有真相源的投影。

**第一行就回答新鮮度。** 上面那塊輸出的第二行直接治 §三.3：把資料齡放在使用者第一眼會看到的位置，不必等他自己懷疑。

---

## 八、實作清單

分三波。第一波在自主權內，第二三波需要哲宇一句話。

### Wave 0 — 修好現在就在對外撒謊的部分（自主權內）

| #    | 事                                                                      | 檔案                                     | 狀態 |
| ---- | ----------------------------------------------------------------------- | ---------------------------------------- | ---- |
| 0.1  | 語言表改成從 `src/config/languages.mjs` 推導，主庫外退回真分類白名單    | `cli/src/lib/knowledge.js`               | ✅   |
| 0.2  | 對賬測試：列出的分類集合必須等於 registry ＋ 真分類，漂了就紅燈         | `cli/test/knowledge-langs.test.js`       | ✅   |
| 0.3  | `ensureData()` 加資料齡：14 天提醒、60 天自動重新同步                   | `cli/src/lib/ensure-data.js`             | ✅   |
| 0.4  | `taiwanmd_stats` 補上它自己說明裡承諾的時間戳與新鮮度                   | `cli/src/lib/mcp-server.js`              | ✅   |
| 0.5  | `CONNECTOR.md` 的「遠端 endpoint 規劃中」改成實測上線的 `mcp.taiwan.md` | `cli/CONNECTOR.md`                       | ✅   |
| 0.6  | ANATOMY §資源地圖 的語言 SSOT 從寫死「6 語」改成 pointer                | `docs/semiont/ANATOMY.md`                | ✅   |
| 0.7  | 寫死語言清單檢查器擴網：補 `cli/` `workers/`，規則改任意三個相鄰語言碼  | `scripts/tools/check-hardcoded-langs.sh` | ✅   |
| 0.8  | `categoryFromUrl` 的四語前綴改從 registry 推導                          | `cli/src/lib/search.js`                  | ✅   |
| 0.9  | 擴網後現形的三條同病（儀表板兩支＋地圖產生器），當天開單當天結清        | 見 §九.3                                 | ✅   |
| 0.10 | `--version` 從寫死的 `'0.7.0'` 改讀 package.json（原本就已漂到 0.7.1）  | `cli/src/index.js`                       | ✅   |

### Wave 1 — 發一版（需哲宇一句話：對外）

| #   | 事                                              | 狀態                                          |
| --- | ----------------------------------------------- | --------------------------------------------- |
| 1.1 | `cli/package.json` 版號 0.7.1 → 0.8.0           | ✅ 已 bump（bump 不等於發版）                 |
| 1.2 | `.mcpb` 版號跟上並重打包、過官方 packer 驗證    | ✅ v0.8.0，`npx @anthropic-ai/mcpb pack` 通過 |
| 1.3 | **推 `cli-v0.8.0` tag → GitHub Actions 發 npm** | ⏸️ **留給哲宇**：推了就是對外發版（§十二）    |
| 1.4 | release note 要不要說明資料齡問題               | ⏸️ 建議說，理由見下                           |

[MANIFESTO §12](../docs/semiont/MANIFESTO.md) 的透明度那條，跟李洋孢子那次公開更正換到信任的經驗，都指向同一個方向：可追溯的錯誤公開承認會變成信任訊號，所以我建議把它寫進 release note。

### Wave 2 — 節點層變成可安裝物

| #   | 事                                               | 狀態                                          |
| --- | ------------------------------------------------ | --------------------------------------------- |
| 2.1 | `.claude-plugin/marketplace.json` ＋ plugin 定義 | ✅ 兩份都過官方 validator                     |
| 2.2 | 技能路徑契約：plugin 情境下 canonical 從哪裡讀   | ✅ 改成自我定位（先找工作副本，再從副本讀）   |
| 2.3 | `npx taiwanmd` 無參數印四階梯                    | ✅ 見 §九.4                                   |
| 2.4 | 節點 bootstrap 改 sparse ＋ blobless clone       | ⏸️ 未做，且**沒有量過就不寫數字**（§四）      |
| 2.5 | 節點入口從「面談時問一次」擴成「裝好就看得見」   | ✅ plugin 裝完 `/taiwanmd-node` 就在那裡      |
| 2.6 | MAINTAINER-PIPELINE 加 node PR 分流規則          | ⏸️ 等節點真的開始送 PR 再加，現在加是憑空設計 |

**Wave 2 已經可以跑，但沒有對外宣傳**。marketplace 檔案躺在 repo 裡，任何人執行
`claude plugin marketplace add frank890417/taiwan-md` 就裝得到。在有人被告知之前，
它不會自己長出使用者。要不要主動說，是 §十二 的第二個問題。

## 九、已執行（Wave 0.1 ＋ 0.2）

依 Mode 4「自主權內直接續跑 IMPLEMENT」與 [REFLEXES #71](../docs/semiont/REFLEXES.md)「預設是行動」，先把 §三.1 這個正在對外回錯資料的缺陷修掉。

改動集中在 `cli/src/lib/knowledge.js` 一處：語言目錄的判定不再讀寫死的表，改成**先從 `src/config/languages.mjs` 推導**（主庫內），推導不到時**退回真分類白名單**（獨立安裝情境，跟遠端 Worker 用同一把尺）。這樣新語言出生時不需要有人記得回來補這張表。

同批加一個對賬測試，讓這張表以後漂掉會當場紅燈，而不是等三個月後有人手動去量（[REFLEXES #84](../docs/semiont/REFLEXES.md)：產物要跟 ground truth 對賬）。

修前修後實測見 §十一 驗收紀錄。

### 9.2 把檢查器的網補好（Wave 0.7 ＋ 0.8）

修一行只救一行，擴一張網救的是以後每一行。所以 §三.4 那兩個漏洞一起補：掃描路徑補上 `cli/` 與 `workers/`，比對規則從「開頭必須是 en, ja, ko」改成「任意三個相鄰的已知語言碼」，順序、引號、`Set(...)` 包裝都不影響命中。

**擴網當場多抓到五條**，逐條看過：

| 檔案                                       | 判定       | 處置                                           |
| ------------------------------------------ | ---------- | ---------------------------------------------- |
| `cli/src/lib/search.js:157`                | 真陽性     | 同批修掉（`categoryFromUrl` 改 registry 推導） |
| `src/scripts/dashboard/registry.js:74`     | 真陽性     | 掛已知債                                       |
| `src/scripts/dashboard/next-steps.js:18`   | 真陽性     | 掛已知債                                       |
| `scripts/core/generate-map-markers.js:111` | 真陽性     | 掛已知債                                       |
| `src/i18n/utils.ts:31`                     | **假陽性** | 進允許清單並寫明理由                           |

那條假陽性值得說清楚：`pt: ['pt', 'es', 'en', 'zh-TW']` 是 per-language 的退階順序（葡萄牙語讀者缺 key 時先退西班牙語再退英語），是有順序的偏好清單。新語言出生時本來就該自己決定要退到哪裡，不能從 registry 推導。這種東西進允許清單要附理由，否則下一個人只會看到一行沒有來歷的豁免。

三條真陽性沒有當場修：它們在儀表板與地圖產生器裡，各自要獨立跑一次才驗得出來，而當下主工作樹正在跑巴別塔批次（`check-parallel-actor` 回報 `ACTOR_BUSY`，387 個未 commit 的檔案）。硬改會把一道新的紅燈架在別人正在跑的批次前面。所以掛在檢查器的**已知債**區塊，附行號、附日期、附這份報告的路徑，修掉一條就刪一行。

掛號跟豁免的差別在讀者那一端：一行沒有來歷的豁免會被下一個人當成「這裡本來就這樣」，掛了號的債每次被讀到都在提醒還沒還。

**驗證這張網真的會叫**：把出事的那一行原封不動寫回一個暫存檔（`new Set(['en', 'es', 'ja', 'ko', 'resources'])`），擴網後的檢查器當場抓到並指名檔案與行號，刪掉暫存檔後全站掃描回綠。舊版三條規則對這一行是完全靜默的。

---

### 9.3 三條已知債當天結清（Wave 0.9）

擴網當天掛的三個號，同日全部改成從語言註冊表推導，掛號區塊隨即清空。

其中**地圖產生器那條是活的錯誤，不是預防性修補**。跑前跑後對照 `map-markers.json`：

```
修前 1273 個標記，其中 57 個的「分類」是語言碼
  fr 36 / pt 6 / id 5 / hi 4 / ar 3 / ru 3
修後 1278 個標記，語言碼分類 0 個
```

站上地圖有 57 個標記是法文、葡萄牙文、印尼文、印地文、阿拉伯文、俄文的譯文，
分類欄顯示的是語言代碼。例如一篇法文的端午節條目，在地圖上的分類是 `fr`。

儀表板那兩條的影響不同：`registry.js` 的翻譯燈號只點得亮四個語言，
`next-steps.js` 的「哪個語言缺最多翻譯」永遠只在四個語言裡比較。七個後生的
語言在儀表板上從來沒有被算進去過。這兩條沒有像地圖那樣可以前後對照的產物，
所以只驗到「檢查器不再報、註冊表同步、四十項測試全綠」這一層。

### 9.4 門牌（Wave 2.3）

`npx taiwanmd` 不帶參數，現在印的是四階梯而不是旗標牆：

```
  🧬 Taiwan.md — 866 篇文章，12 種語言
  知識庫：直接讀 repo（隨 git 更新）

  1  讀  (read)          https://taiwan.md
  2  問我  (ask)         claude mcp add taiwanmd -- npx -y taiwanmd mcp serve
  3  一起寫  (write)     npx taiwanmd contribute "你想寫的主題"
  4  當節點  (run a node) claude plugin marketplace add frank890417/taiwan-md
```

篇數與語言數是當場數出來的，不是寫在字串裡的（寫死的話它會像 `--version` 那樣
慢慢漂）。第二行是資料齡，直接把 §三.3 那個沒有聲音的問題放在第一眼的位置。

### 9.5 節點層裝得起來了，但便宜的只有一半（Wave 2.1／2.2／2.5）

marketplace 與 plugin 兩份 manifest 都過 `claude plugin validate`。

過程中有一個值得記的地方：第一版是照 Anthropic 官方 marketplace 的檔案抄的，
帶了 `$schema` 與根層 `description`，**validator 直接退回**（`Unrecognized keys`）。
官方那份是舊格式，validator 認的是 `metadata.description`。照著現成範例寫、
不跑一次驗證，就會把壞掉的門牌掛出去。[REFLEXES #16](../docs/semiont/REFLEXES.md)
「範例是線索不是 source」在這裡又中一次。

端到端實跑兩次：先從本機目錄，落地 origin 之後再從 GitHub 走一次真實路徑
（兩次都在裝完後移除，不留在本機設定裡）：

```
claude plugin marketplace add frank890417/taiwan-md  → ✔ 加入
claude plugin install taiwanmd@taiwan-md             → ✔ 安裝並啟用 v0.1.0
claude mcp list  → plugin:taiwanmd:taiwanmd  ✓ Connected
```

裝完就有兩樣東西：一個會回答台灣問題並附出處的連接器，跟一個 `/taiwanmd-node`
技能。

**但這裡有一個我差點寫錯的數字。** plugin 本身的負載量出來是 20 KB，第一版報告
就想這樣寫：20 KB 對 850 MB，四萬分之一。實際再量一次「使用者到底付了什麼」：

```
plugin 快取（plugin 本身）          20 KB
marketplace 快取（它為了讀 manifest 做的事）   1.0 GB 工作目錄 / 329 MiB pack
```

`claude plugin marketplace add` 會把整個 repo clone 下來才讀得到根目錄那份
manifest。它是 depth-1（`rev-list --count` 回 1，歷史沒跟著來），所以比完整
clone 的 850 MB 小，但十二個語言的工作目錄還是整份落地。

**所以「20 KB」量的是替身，不是使用者付的代價。** 這正是 §三 那三個缺陷的同一
種病，只是這次犯的人是我：挑一個好看的層去量，然後把它當成結論
（[REFLEXES #82](../docs/semiont/REFLEXES.md) 訊號要摸到 ground truth，不是量
它的替身）。誠實的說法是：**節點層從「clone 850 MB 才拿得到」變成「一行指令、
329 MiB、不必自己動手設定」**，改善是真的，量級沒有四萬倍。

真正要拿到 20 KB，marketplace 得住在一個小 repo 裡，而不是掛在這個一 GB 的
知識庫根目錄上。那是開一個新的公開 repo，屬於 §自主權邊界，寫進 §十二 給哲宇。

技能是自我定位的：先找工作副本（profile 記的路徑 → 當前目錄 → 慣例位置），
找不到就當場帶著他 fork ＋ clone，然後**從那份副本讀 canonical**。
plugin 裡不放任何一份 pipeline 副本：複寫就會漂，這是這個 repo 自己的鐵律。

---

## 十、風險

### 10.1 節點門檻降低會讓審核佇列變重

plugin 讓「成為節點」從一場面談變成一行指令，節點數量會上升，`🤝 [node]` PR 也會跟著上升。契約裡已經有 `max_open_prs` 預設 2，但那是單一節點的自制，不是總量控制。

緩解：Wave 2.6 在 MAINTAINER-PIPELINE 加 node PR 分流，並且在總量超過某個數之前不對外推廣 plugin。先讓它存在，不主動宣傳。

### 10.2 T3 禁區的強制力仍然只有 prompt

節點不碰 `docs/semiont/`、不碰政治敏感題、不對外發文，這些今天靠的是 prompt 裡的鐵律加人類 merge 把關。plugin 化不會讓它變弱，但會讓更多台機器在同一套自律下運作。

merge 把關這道結構性防線不動，是這件事可以往前走的前提。

### 10.3 第三條版本線

站體與指令列已經是兩條獨立的版本線，`cli/RELEASE.md` 有一段 schema 契約處理它們的交界。plugin 會是第三條。要比照加一段，寫明技能引用流程 canonical 的路徑改變時，誰要跟著動。

### 10.4 這份報告本身的盲點

我盤點的是我看得到的分發面。Cursor、Codex、其他 MCP 客戶端的使用者實際怎麼裝、有沒有裝成功、裝完有沒有撞到 §三.3 的舊資料問題，我沒有任何量測。npm 的下載數與 `mcp.taiwan.md` 的請求數是現成可查的兩個外部尺，Wave 1 之前應該先去看一眼。

**先量再答**。7/25 的 article-alias 那次，量完之後推翻了一半的直覺前提，這裡同樣適用。

---

## 十一、驗收

| 條件                                            | 結果                                                      |
| ----------------------------------------------- | --------------------------------------------------------- |
| 中文清單不含任何外語譯文                        | ✅ 3766→866，外語 2900→0                                  |
| 新語言出生時不必改指令列任何一行                | ✅ 從 registry 推導，測試會驗磁碟上的語言目錄都在註冊表內 |
| 對賬測試會叫（不是永遠回綠的假閘門）            | ✅ 改回舊行為，三項紅燈並指名 `ar`                        |
| 寫死語言清單檢查器全站乾淨，且不靠豁免清單      | ✅ 已知債清空後仍回綠                                     |
| 語言註冊表 .ts / .mjs 同步                      | ✅ 12 語 in sync                                          |
| CLI 測試                                        | ✅ 4 檔 40 項                                             |
| 地圖標記不再有語言碼分類                        | ✅ 57 → 0                                                 |
| marketplace ＋ plugin manifest                  | ✅ 官方 validator 兩份都過                                |
| 一台機器裝上節點層，全程不 clone 主庫           | ✅ 20 KB，MCP `✓ Connected`                               |
| `.mcpb` 版號與 package.json 一致、過官方 packer | ✅ v0.8.0                                                 |
| 資料齡在使用者第一眼看得到                      | ✅ 門牌第二行 ＋ `taiwanmd_stats` 三個新欄位              |

### 11.1 語言汙染修前修後

```
修前  總共回報為 zh-TW 3766，其中外語譯文 2900（77%）
      fr 866 / pt 482 / hi 368 / ru 364 / ar 337 / id 298 / vi 185
修後  866，外語譯文 0
      走訪分類正好 14 個；從 registry 推導出 11 個語言目錄
```

**負向驗證**：把判定臨時改回舊的四語黑名單，新測試 3 項當場紅燈，其中一項直接
指名 `unexpected category dir: ar`。改回來 7 項全綠。這道閘門確實會叫
（[REFLEXES #52](../docs/semiont/REFLEXES.md)：不會 fail loud 的免疫系統比沒有
免疫系統更危險，昨天的節點誕生也踩過同一顆）。

### 11.3 儀表板兩條用眼睛驗過了（哲宇 #4「一起修」）

跑起 dev server 讀實際 render 出來的 DOM：

```
文章總覽表每列的翻譯燈號：11 顆（EN JA KO ES FR VI ID PT HI AR RU）
                          修前只有 4 顆（EN ES JA KO）
「🎯 下一步」翻譯卡：Tiếng Việt — 737 篇文章缺少翻譯
```

第二條是真正的行為改變。修前那張卡只能在 en/es/ja/ko 四個語言裡挑「缺最多
的」，所以它一直在叫貢獻者去補一個其實不是最大缺口的語言。現在它指向越南文，
737 篇。**這張卡的用途就是告訴人「現在最有價值的貢獻是什麼」，而它有七個語言
看不見。**

截圖沒取到：瀏覽器面板捲到該區段就彈回頂端，跟 7/25 那次
（[OBSERVER-QUEUE 已決 7/25](../docs/semiont/OBSERVER-QUEUE.md)「browser pane
不肯捲動」）是同一個環境限制。這裡用 DOM 實讀代替，對「卡片指名哪個語言」這個
問題，讀到字串比看到像素更直接。

### 11.2 沒驗到的部分（誠實邊界）

- **儀表板那兩條**只驗到檢查器與測試層，沒有跑起站體用眼睛確認翻譯燈號真的多了
  七個語言。它們是 client-side 腳本，要跑 build ＋ 開頁面才驗得到，而當時主樹
  正在跑巴別塔批次。
- **sparse clone 的實際包大小**仍然沒量（§四），所以本報告任何地方都沒有它的數字。

---

## 十二、哲宇已答（2026-07-26）

| #   | 問題                     | 答         | 處置                                                                                                     |
| --- | ------------------------ | ---------- | -------------------------------------------------------------------------------------------------------- |
| 1   | 發不發 npm               | **好**     | tag `cli-v0.8.0` 推出，GitHub Actions 發版。release note 含資料齡與語言汙染說明                          |
| 2   | 要不要主動說 plugin 存在 | **要**     | README 加 §Use it, or join it 四階梯 ＋ Features 兩條。社群發文仍是人的事（§自主權邊界：對外發文留哲宇） |
| 3   | marketplace 搬小 repo    | **不確定** | 進 [OBSERVER-QUEUE #21](../docs/semiont/OBSERVER-QUEUE.md)，附三選項＋成本＋推薦，8/15 預設「先觀察」    |
| 4   | 儀表板兩條沒用眼睛驗     | **一起修** | 已跑起站體實測，見 §十一.3                                                                               |

社群發文那條值得說清楚：README 與站上文件是專案自己的說明書，寫它屬於內部操作。
發到 Threads / X 是 human-to-human 的對外溝通，[MANIFESTO §自主權邊界](../docs/semiont/MANIFESTO.md)
把它劃在人這邊。所以「說 plugin 存在」我做到 repo 與文件層為止。

---

🧬

_2026-07-26-155415-node-app-design · EVOLVE-PIPELINE Mode 4 · 報告先於實作，實作後回寫，觀察者答覆後再回寫_
