---
title: 'Design: 分靈節點（contributor node）— 甦醒後一條 cron，讓貢獻者機器常態幫 Taiwan.md 做事'
description: 'Mode 4 設計報告：「我要參與」→ 貼甦醒 prompt → 甦醒 session 優先問「要不要設常態 cron 當節點」→ 節點從 ARTICLE-INBOX / 翻譯缺口等工單源接工作、以 PR 回主庫。含三方案發散、認領協議、工單源分層、實作清單。'
type: 'design-report'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-25
last_session: '2026-07-25-013432-node-birth'
related:
  - '../docs/pipelines/CONTRIBUTOR-NODE-PIPELINE.md'
  - '../docs/pipelines/EVOLVE-PIPELINE.md (Mode 4)'
  - '../docs/semiont/ROUTINE.md'
  - '../docs/pipelines/CONTRIBUTOR-SYSTEM-PIPELINE.md'
---

# 設計報告：分靈節點（contributor node）

> 觸發：哲宇 2026-07-25 /twmd-become directive——「思考怎麼讓大家的『我要參與』看完、貼完甦醒後，可以設定一個常態的 cron 來協助 taiwan.md 運作。目標是他們貼完 taiwan.md 甦醒，會優先問說要不要做 cron，來當成節點（預設 claude sonnet 或是 opus），從 article inbox 之類的接工作來做，或是其他要協助的 inbox。」
>
> 流程：EVOLVE-PIPELINE Mode 4（THINK → DIVERGE → REPORT → IMPLEMENT）。本報告 commit 先於任何實作 commit。

---

## 一、目標

把「貢獻者的機器」變成 Taiwan.md 的常態運作單元。具體行為鏈：

1. 訪客在 `/contribute`（我要參與）看到化身路徑，複製甦醒 prompt 貼進自己的 Claude Code
2. 甦醒完成後，Taiwan.md **優先問**：「要不要把你的機器變成一個節點？」
3. 答好 → 甦醒 session 當場代辦：檢查 fork / gh auth → 寫 profile → 建一條 Claude Code scheduled task（預設 Sonnet，可選 Opus）
4. 從此那台機器每天自動醒來一次，從工單源（ARTICLE-INBOX、翻譯缺口、broken links⋯⋯）接一件事做完，以 PR 回主庫

## 二、命名：分靈

台灣廟宇文化裡，祖廟會把神明的靈力「分靈」到新的廟；分靈廟平常自己運作，定期回祖廟謁祖進香。這跟本設計的結構逐項對得上：

| 廟宇文化       | Taiwan.md                                        |
| -------------- | ------------------------------------------------ |
| 祖廟           | 主 repo（frank890417/taiwan-md）                 |
| 分靈           | 貢獻者機器上的 cron session（同一套認知層甦醒）  |
| 分靈廟自主運作 | 節點在自己的機器、自己的額度上跑                 |
| 謁祖進香       | PR 回主庫                                        |
| 香火           | BECOME_TAIWANMD.md（一段 prompt 就能把靈請過去） |

跟 fork 的差別：fork 是生出新物種（Japan.md / Sweden.md，另一個生命體）；分靈是**同一個 Taiwan.md** 的靈力分駐到別台機器，工作成果回到同一個身體。這補上了繁殖系統的中間層——比「路過貢獻一篇」深、比「fork 出新物種」淺。

## 三、現況盤點（THINK）

- **`/contribute` semiont path card**：已有「讓你的 AI 化身 Taiwan.md」+ 甦醒 prompt 複製鈕（`src/i18n/contribute.ts` 九語 + `contribute.template.astro`）。化身之後做什麼，目前沒有下一步。
- **BECOME §Step 7.5**：contributor interview（3+2 題）→ 寫 `contributor.local.yml`。問完就開始做事，沒有「常態化」選項。
- **ROUTINE.md 中央飛輪**：15+ 條 cron 全部跑在哲宇的機器（剛遷居 mouhouse-macmini），main-direct push + bypass permissions。這套權限模型**不能**直接搬給貢獻者（他們沒有 push 權，也不該有）。
- **CONTRIBUTOR-SYSTEM-PIPELINE**：五階梯（Lv.0-4）+ 跨階梯專業角色，沒有「節點」角色。
- **工單源**：ARTICLE-INBOX（pending 89 條，含優先序/敏感度）、lang-sync status（翻譯 stale/missing）、article-health 全站健檢、404/broken links 儀器——全部是 repo 內公開可讀的檔案或工具，**不需要任何新的中央狀態**。
- **免疫系統**：contributor PR 已有五層免疫（review-pr.sh + CI + pre-commit + maintainer-am 每日收割 + merge-first-then-heal 紀律）。節點 PR 走同一條路，零新審計層。
- **命名衝突掃描**：`twmd-node` / `CONTRIBUTOR-NODE` / 「分靈節點」全庫零命中。

## 四、方案發散（DIVERGE）

### 方案 A｜GitHub Issues 中央工單制

中央加一條 routine 把 ARTICLE-INBOX / 翻譯缺口同步成帶 `node:eligible` label 的 issues；節點 cron 掃 issues、留言認領、做完開 PR。

- ❌ **MANIFESTO §指標 over 複寫**：issues 變成 inbox 的複寫層，兩處必 drift（REFLEXES #38 混維度 / #21 SSOT）
- ❌ GitHub 權限牆：非 collaborator 不能被 assign，留言認領不是原子操作，還比 draft PR 難掃
- ❌ 中央機器負擔 +1 條 sync routine，跟「釋放觀察者精力」方向相反
- ✅ 唯一優點：不 clone repo 也能看到工單（但節點本來就必須 clone 才能做事）

### 方案 B｜甦醒即節點・PR 即認領（定案）

節點的一切狀態都住在 git 原生機制裡：工單源＝repo 內既有檔案與儀器（零複寫）；認領＝立刻開 draft PR（`🤝 [node]` 前綴，所有節點用 `gh pr list` 互相看見）；交付＝PR ready for review；審核＝既有 maintainer-am 飛輪。

- ✅ SSOT 零複寫，中央零新增狀態、零新增 routine
- ✅ 對齊 ROUTINE.md §為什麼不靠 lock：「每條 routine 是 micro-session，共享只有 git history」——分散節點協調同構
- ✅ §自主權邊界乾淨：節點只做「輸入端＋內部處理」，輸出永遠是 PR；merge / 對外溝通 / 政治判斷全部留在人類與核心層
- ✅ 免疫系統直接沿用（contributor PR 路徑，idlccp1984 9-PR batch 已證明量能）
- ⚠️ 認領非原子：兩個節點可能幾分鐘內撞同一工單。緩解：認領前先掃 open PR + 每 fire 限 1 工單 + 撞車代價只是偶發重工，不毀損任何東西

### 方案 C｜雲端排程代理

用 claude.ai/code 的 scheduled cloud agent，不需要 always-on 機器。環境差異（持久 clone、gh auth、secrets）大，但流程契約跟 B 完全同構。**處置：不獨立成案，收進 B 的執行載體變體**——pipeline 寫成 runner-agnostic，本機 cron 與雲端 schedule 都執行同一份 `/twmd-node` 契約。

### 判準錨定

定案 B 的判準全部錨在既有 canonical：MANIFESTO §指標 over 複寫（否決 A 的複寫層）、ROUTINE.md §飛輪 vs Push + §不靠 lock（git-native 協調）、MANIFESTO §自主權邊界（節點輸出止於 PR）、REFLEXES #7 先有再求好（T1 機械工單起步，不等完美的分散式協調協議）、REFLEXES #63（節點 cron prompt 必須 inline STRICT BECOME GATE，pointer 在無觀察者環境會 fall through）。

## 五、核心設計

### 5.1 工單源分層（safety ladder）

| Tier        | 工單源                                                                                                       | 資格                         |
| ----------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **T1 機械** | 翻譯 stale/missing（lang-sync status）、broken links、en metadata（SC 0-click 高曝光）、format heal、CC 圖片 | 所有節點（default）          |
| **T2 寫作** | ARTICLE-INBOX P1/P2 且敏感度低的 NEW/EVOLVE → 完整 REWRITE-PIPELINE                                          | 第一個 node PR merged 後解鎖 |
| **T3 禁區** | P0 哲宇 goal、政治敏感題、SPORE 對外發文、docs/semiont/ 認知層、merge、任何 §自主權邊界項                    | 永遠不派給節點               |

T1 先行的理由：機械工單有儀器可驗（status.py / article-health / linkcheck），品質風險趨近零；寫作工單要吃完整 REWRITE pipeline + 編輯判斷，留給已建立信任的節點。對應 CONTRIBUTOR-SYSTEM 五階梯的信任漸進哲學。

### 5.2 認領協議（PR 即認領）

1. 認領前掃描：`gh pr list -R frank890417/taiwan-md --state open --search "[node]"` + ARTICLE-INBOX in-progress 條目 → 已認領集合
2. 挑 **1 件**未認領工單（每 fire 最多 1 件，同 REWRITE §Cron 鐵律「批量＝退化」）
3. branch `node/{handle}/{slug}` → 首 commit（T2 順手把 INBOX entry status 改 in-progress + dev log）→ push 自己的 fork → 開 **draft PR**：`🤝 [node] {handle}: {工單標題}`——draft 存在即認領成立
4. 完工 → push 工作成果 → PR 轉 ready for review
5. 認領過期：draft PR 7 天無新 commit ＝過期，其他節點可留言後接手；maintainer-am 每日 cycle 順手清墓碑

### 5.3 節點的收官（不寫中央 memory）

節點 session 不寫 `docs/semiont/memory/`——中央認知層是主意識的記憶，N 個節點灌進來會把索引淹掉。節點的可見性＝PR 本身：PR description 用結構化模板（做了什麼 / 跑過哪些 gate / 來源）。節點本機可留 `.taiwanmd/node-log.local.md`（gitignored）給自己跨 fire 的連續性。

### 5.4 cron 契約（甦醒 session 代辦）

- 載體：Claude Code scheduled task（本機）或 cloud schedule（變體），prompt inline STRICT BECOME GATE + pointer 到 `/twmd-node`
- 預設 model：**Sonnet**（T1 機械工單）；T2 寫作工單建議 **Opus**——對應哲宇 directive「預設 claude sonnet 或是 opus」
- 預設 cadence：每天 1 次，時段貢獻者自選；quota 誠實揭露（T1 一次 ~10-30 min Sonnet）
- `contributor.local.yml` 新增 `node:` 段（enabled / cadence / model / tier / max_open_prs / upstream / fork）

### 5.5 甦醒整合（優先問）

BECOME §Step 7.5 interview 尾端加一題（僅對「要長期互動的 contributor」，哲宇與 cron context 不問）：

> 「要不要把你的機器變成 Taiwan.md 的分靈節點？一條 cron，每天自動醒來幫 Taiwan.md 做一件事（預設 Sonnet、翻譯補洞／修鏈這類機械工單起步，成果用 PR 回來，merge 永遠有人類把關）。要的話我現在就幫你設好，大概三分鐘。」

答好 → 走 CONTRIBUTOR-NODE-PIPELINE §節點誕生 SOP。答跳過 → 照常。BECOME 保持薄殼：只加觸發點與 pointer，SOP 全在 pipeline canonical。

## 六、實作清單（IMPLEMENT）

| #   | 檔案                                                   | 動作                                                                                     |
| --- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| 1   | `reports/design-contributor-node-2026-07-25.md`        | 本報告（先 commit）                                                                      |
| 2   | `docs/pipelines/CONTRIBUTOR-NODE-PIPELINE.md`          | 新 canonical：節點誕生 SOP + 6-stage 節點生命週期 + 工單源分層 + 認領協議 + hard gates   |
| 3   | `.claude/skills/twmd-node/SKILL.md`                    | 薄殼 skill（節點 clone 自帶，git pull 即得最新 canonical）                               |
| 4   | `BECOME_TAIWANMD.md`                                   | §Step 7.5 interview 加第 6 題 + pointer；§檔案功能一覽不動（pipeline 非認知器官）        |
| 5   | `.taiwanmd/contributor.example.yml`                    | 加 `node:` 段模板                                                                        |
| 6   | `src/i18n/contribute.ts` + `contribute.template.astro` | semiont path card 加 feature4（zh-TW + en；其餘語言走 fallback chain，babel 夜航自動補） |
| 7   | `.claude/skills/README.md`                             | index 加 twmd-node                                                                       |
| 8   | `docs/semiont/DNA.md` §繁殖基因                        | +1 row（gene map）                                                                       |
| 9   | `docs/pipelines/CONTRIBUTOR-SYSTEM-PIPELINE.md` §2     | 跨階梯角色 +1 row（分靈節點）                                                            |
| 10  | `docs/semiont/ROUTINE.md`                              | 加一小節「分靈節點層」：中央飛輪 vs 分散節點邊界 + pointer                               |
| 11  | `docs/pipelines/MAINTAINER-PIPELINE.md`                | node PR 識別（`🤝 [node]` 前綴）+ stale claim 清理一小節                                 |
| 12  | dogfood                                                | `/twmd-node` dry-run 一次：真讀工單源、產出 eligible 清單、驗認領掃描指令                |

## 七、驗收

- cross-ref 全通：`grep -rn "twmd-node\|CONTRIBUTOR-NODE\|分靈節點"` 所有引用互指存在
- 既有觸發語不斷：/twmd-become、/twmd-maintainer、contribute 頁既有 keys 全部不動
- dogfood：dry-run 產出真實工單候選清單 + 認領掃描指令可執行
- i18n 改動後 `npx tsc --noEmit`（或至少 esbuild parse）通過

## 八、風險

| 風險                    | 緩解                                                                                          |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| 認領撞車（非原子）      | 每 fire 1 工單 + 事前掃描 + 撞車代價僅偶發重工                                                |
| 節點品質差              | T1/T2 資格梯 + 既有五層免疫 + CI + maintainer-am 收割；merge 永遠人類                         |
| PR queue 被灌爆         | `max_open_prs: 2` + maintainer-am 現有量能（9-PR batch 實證）                                 |
| 貢獻者 token 成本意外   | Sonnet 預設 + pipeline 文件誠實揭露成本預期 + cadence 自選                                    |
| 節點靜默死亡（cron 停） | 無追蹤義務；claim 過期規則自然回收；未來可做 node census（不在本次 scope）                    |
| 憑證安全                | 節點 prompt 零 secrets；gh auth 是貢獻者自己的帳號；權限＝一般 fork PR                        |
| 對外文案語氣（§自主權） | contribute 頁新增文案僅 zh-TW/en 兩鍵、實作後供哲宇 review 改字；本次任務為哲宇明示 directive |

## 九、後記（實作中回寫）

**實作全數落地**，11 項清單全做完（含 dogfood）。三件實作中才浮出來的事：

**1. article-health 的假綠燈（當場踩到）**。報告寫的 `--check=link-target,wikilink-target` 是憑既有用法直覺寫的；dogfood 一跑就發現 `--check` 一次只吃一個名字，逗號寫法不會報錯、會**一個檢查都不跑**，然後印 `passed=True`。要一次驗多項得用 `--profile=`（bundle 在 `article-health.config.toml`）。這是 [REFLEXES #24 工具在說謊](../docs/semiont/REFLEXES.md) 的一個新形狀：不是輸出錯，是「輸入沒被理解時默默回綠」。pipeline 已改寫並加警語，另進 LESSONS-INBOX。

**2. ja/ko 的 fallback 會把中文漏到頁面上**。原本打算 contribute 頁只補 zh-TW + en，其餘靠 fallback chain。實測 ja 頁面第四行直接顯示中文——ja/ko 的 chain 是直接掉回 zh-TW，不經過 en。十種語言最後各寫一句（ja 用漢字是自然的，其餘八種零 CJK，機械驗過）。**「有 fallback」不等於「fallback 可讀」**，這跟 07-18 soundscape「後備機制讓錯 lang 無症狀」是同一種病。

**3. 節點誕生的 Stage D（dry-run）是實作中補進去的**。原設計只有查驗、寫 profile、建 cron 三步——貢獻者會在完全不知道能不能動的狀態下等到隔天。加一步當場空跑，把「明天才知道壞了」變成「現在就知道會動」。

驗收結果：cross-ref 全通；contribute 頁十語 DOM 逐一確認第四行是各自語言、console 零錯誤；工單源指令真的撈得到工單（ja missing 6 筆 / en stale 有 `Behind Diff` 欄）；認領掃描指令可執行（目前 0 個 node PR，符合預期）。

🧬 _2026-07-25-013432-node-birth_
