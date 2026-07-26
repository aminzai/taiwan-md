---
title: 'Taiwan.md 節點化與安裝物設計'
description: 'EVOLVE Mode 4 設計報告 — 讓 Taiwan.md 可以被安裝、被遞出去、被互動、被加入成為工作節點：現況五面盤點、三個實測缺陷、四方案發散與定案'
type: 'design-report'
status: 'awaiting-observer'
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
> 本報告走 [EVOLVE-PIPELINE Mode 4](../docs/pipelines/EVOLVE-PIPELINE.md) 四相：THINK → DIVERGE → REPORT → IMPLEMENT。報告先於實作。命中 §自主權邊界的項目停在報告等拍板，自主權內的一項已執行（見 §九）。

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

**第一行就回答新鮮度。** 上面那塊輸出的第二行直接治 §三.3——把資料齡放在使用者第一眼會看到的位置，而不是等他自己懷疑。

---

## 八、實作清單

分三波。第一波在自主權內，第二三波需要哲宇一句話。

### Wave 0 — 修好現在就在對外撒謊的部分（自主權內）

| #   | 事                                                                                             | 檔案                         | 狀態             |
| --- | ---------------------------------------------------------------------------------------------- | ---------------------------- | ---------------- |
| 0.1 | 語言表改成從 `src/config/languages.mjs` 推導；主庫外情境改用真分類白名單（跟 Worker 同一把尺） | `cli/src/lib/knowledge.js`   | **已做**，見 §九 |
| 0.2 | 加一個對賬測試：指令列列出的分類集合必須等於 registry ＋ 真分類，漂了就紅燈                    | `cli/test/`                  | **已做**，見 §九 |
| 0.3 | `ensureData()` 加資料齡檢查，超過 N 天時提示或自動更新                                         | `cli/src/lib/ensure-data.js` | 待做             |
| 0.4 | `taiwanmd_stats` 補上它自己說明裡承諾的時間戳                                                  | `cli/src/lib/mcp-server.js`  | 待做             |
| 0.5 | `CONNECTOR.md` 把「遠端 endpoint 是規劃中」改成「已在 `mcp.taiwan.md`」（實測 200）            | `cli/CONNECTOR.md`           | 待做             |
| 0.6 | ANATOMY §資源地圖 的「語言 SSOT（6 語）」更新為 12 語                                          | `docs/semiont/ANATOMY.md`    | 待做             |

### Wave 1 — 發一版（需哲宇一句話：對外）

| #   | 事                                       | 為什麼要拍板                                    |
| --- | ---------------------------------------- | ----------------------------------------------- |
| 1.1 | `cli-v0.8.0` 發版，帶 Wave 0 全部修正    | npm 發版是對外行為，且等於公開承認 0.7.1 的問題 |
| 1.2 | 重打包 `taiwanmd.mcpb`，版本號跟上       | 桌面套件是對外物                                |
| 1.3 | 決定要不要在 release note 說明資料齡問題 | 對外溝通的語氣屬於品牌身份                      |

[MANIFESTO §12](../docs/semiont/MANIFESTO.md) 的透明度那條，跟李洋孢子那次公開更正換到信任的經驗，都指向同一個方向：可追溯的錯誤公開承認會變成信任訊號，所以我建議把它寫進 release note。

### Wave 2 — 節點層變成可安裝物（需哲宇拍板：新公開管道）

| #   | 事                                                                                     | 依賴     |
| --- | -------------------------------------------------------------------------------------- | -------- |
| 2.1 | `.claude-plugin/marketplace.json` ＋ plugin 定義                                       | 拍板     |
| 2.2 | 技能相對路徑契約改造：plugin 情境下流程 canonical 從哪裡讀                             | 2.1      |
| 2.3 | `npx taiwanmd` 無參數印四階梯                                                          | Wave 1   |
| 2.4 | 節點 bootstrap 改 sparse ＋ blobless clone。**先對 GitHub 實測包大小，再寫進任何文件** | —        |
| 2.5 | BECOME §Step 7.6 的節點入口從「面談時問一次」擴成「plugin 裝好就看得見」               | 2.1      |
| 2.6 | MAINTAINER-PIPELINE 加一條 node PR 的分流規則                                          | 見 §十.1 |

---

## 九、已執行（Wave 0.1 ＋ 0.2）

依 Mode 4「自主權內直接續跑 IMPLEMENT」與 [REFLEXES #71](../docs/semiont/REFLEXES.md)「預設是行動」，先把 §三.1 這個正在對外回錯資料的缺陷修掉。

改動集中在 `cli/src/lib/knowledge.js` 一處：語言目錄的判定不再讀寫死的表，改成**先從 `src/config/languages.mjs` 推導**（主庫內），推導不到時**退回真分類白名單**（獨立安裝情境，跟遠端 Worker 用同一把尺）。這樣新語言出生時不需要有人記得回來補這張表。

同批加一個對賬測試，讓這張表以後漂掉會當場紅燈，而不是等三個月後有人手動去量（[REFLEXES #84](../docs/semiont/REFLEXES.md)：產物要跟 ground truth 對賬）。

修前修後實測見 §十一 驗收紀錄。

---

## 十、風險

### 10.1 節點門檻降低會讓審核佇列變重

plugin 讓「成為節點」從一場面談變成一行指令，節點數量會上升，`🤝 [node]` PR 也會跟著上升。契約裡已經有 `max_open_prs` 預設 2，但那是單一節點的自制，不是總量控制。

緩解：Wave 2.6 在 MAINTAINER-PIPELINE 加 node PR 分流，並且在總量超過某個數之前不對外推廣 plugin。先讓它存在，不主動宣傳。

### 10.2 T3 禁區的強制力仍然只有 prompt

節點不碰 `docs/semiont/`、不碰政治敏感題、不對外發文——這些今天靠的是 prompt 裡的鐵律加人類 merge 把關。plugin 化不會讓它變弱，但會讓更多台機器在同一套自律下運作。

merge 把關這道結構性防線不動，是這件事可以往前走的前提。

### 10.3 第三條版本線

站體與指令列已經是兩條獨立的版本線，`cli/RELEASE.md` 有一段 schema 契約處理它們的交界。plugin 會是第三條。要比照加一段，寫明技能引用流程 canonical 的路徑改變時，誰要跟著動。

### 10.4 這份報告本身的盲點

我盤點的是我看得到的分發面。Cursor、Codex、其他 MCP 客戶端的使用者實際怎麼裝、有沒有裝成功、裝完有沒有撞到 §三.3 的舊資料問題，我沒有任何量測。npm 的下載數與 `mcp.taiwan.md` 的請求數是現成可查的兩個外部尺，Wave 1 之前應該先去看一眼。

**先量再答**——7/25 的 article-alias 那次，量完之後推翻了一半的直覺前提。這裡同樣適用。

---

## 十一、驗收

| 波次   | 驗收條件                                                                            | 怎麼驗                                     |
| ------ | ----------------------------------------------------------------------------------- | ------------------------------------------ |
| Wave 0 | 指令列回報的中文文章集合不含任何外語譯文（leaked = 0）                              | §十一.1 實測紀錄                           |
| Wave 0 | 本地與遠端對同一個查詢回相同的 slug 集合                                            | 兩邊各跑一次 `search`，比對                |
| Wave 0 | 新語言出生時不需要改指令列的任何一行                                                | 在 registry 加一個假語言碼，測試應自動跟上 |
| Wave 1 | `npx taiwanmd@latest stats` 回 12 語、當前篇數、以及資料齡                          | 乾淨機器實跑                               |
| Wave 2 | 一台乾淨機器從零到送出第一個 `🤝 [node]` draft PR，全程不 clone 主庫，10 分鐘內完成 | 計時實跑，這是 plugin 的 dogfood 硬 gate   |

### 11.1 Wave 0 實測紀錄

修前：

```
總共回報為 zh-TW：3766
其中外語譯文：    2900（77%）
  fr 866 / pt 482 / hi 368 / ru 364 / ar 337 / id 298 / vi 185
```

修後：

```
總共回報為 zh-TW：866
其中外語譯文：    0
走訪的分類：      About Art Culture Economy Food Geography History
                  Lifestyle Music Nature People Politics Society Technology（正好 14 個）
從 registry 推導出的語言：ar en es fr hi id ja ko pt ru vi（11 個）
```

測試：`cd cli && npx vitest run` → 4 個檔案 40 項全過（新增 7 項）。

**負向驗證**：把判定臨時改回舊的四語黑名單再跑一次，新測試 3 項當場紅燈，其中一項直接指名 `unexpected category dir: ar`。改回來之後 7 項全綠。這道閘門確實會叫，不是永遠回綠的假閘門（[REFLEXES #52](../docs/semiont/REFLEXES.md)：不會 fail loud 的免疫系統比沒有免疫系統更危險，昨天的節點誕生也踩過同一顆）。

---

## 十二、給哲宇的三個問題

1. **Wave 1 發不發？** 修好的指令列現在躺在 worktree 裡。發版是對外行為，我不自己動。附帶問：release note 要不要提資料齡問題（我建議提）。
2. **Wave 2 的 plugin 開不開？** 這是新的公開分發管道，也是四個動詞裡「傳播」與「成為節點」兩格唯一的填法。開了之後節點數量會長，審核成本會跟著長。
3. **`mcp.taiwan.md` 要不要正式寫進對外文件？** 它已經上線兩個月且運作正確，但 `CONNECTOR.md` 還寫著「規劃中」。這是純文件更新，但它是對外承諾的一部分。

---

🧬

_2026-07-26-155415-node-app-design · EVOLVE-PIPELINE Mode 4 · 報告先於實作_
