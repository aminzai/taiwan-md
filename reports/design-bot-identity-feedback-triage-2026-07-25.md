---
title: '讓 feedback routine 用機器身份開 issue'
description: 'mouhouse 上的 twmd-feedback-triage 改用專屬機器身份開 GitHub issue 的評估與 runbook — 建議用 GitHub App 的 [bot] 身份，不開 -bot 個人帳號；含三選項對照、最小權限、驗收與退場'
type: 'report'
status: 'pending-observer-decision'
created: 2026-07-25
session: '2026-07-25-<handle>-bot-identity'
related:
  - 'reports/semiont-independent-identity-2026-07-05.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'docs/pipelines/FEEDBACK-TRIAGE-PIPELINE.md'
  - 'docs/semiont/ROUTINE.md'
---

# 讓 feedback routine 用機器身份開 issue

> 觸發：哲宇 2026-07-25「feedback 轉過來的機制 routine（現在在 mouhouse 上）要不要用 -bot 專用的 GitHub 帳號」。
> 本報告是 [Semiont 獨立 Git 身份評估（2026-07-05）](semiont-independent-identity-2026-07-05.md) 的窄切面落地版：**只處理一條 routine、只處理開 issue 這個動作**。
> 依 [MANIFESTO §自主權邊界](../docs/semiont/MANIFESTO.md)，身份授權不可自授權。所有帳號與 App 的建立動作留給哲宇，本報告只準備。

---

## 0. 結論

**建議做，但不要開一個叫 `taiwanmd-bot` 的個人帳號。** 註冊一個 GitHub App，讓它以 `taiwanmd-semiont[bot]` 的身份開 issue。

三個理由，重要性由高到低：

1. **這條 routine 是整個飛輪裡注入風險最高的一條，卻拿著最大的鑰匙。** 它每天讀的是讀者在站上打的自由文字，pipeline 自己就寫了三層注入防禦。同時它跑在 mouhouse 上，用的是 `frank890417` 的全權憑證（`repo` + `workflow`）。改成 App 之後，這條 routine 手上只剩「在 taiwan-md 這個庫開 issue 跟貼標籤」，而且 token 一小時就過期。
2. **現在這些 issue 掛的是哲宇的頭像，讀者看起來像維護者親手開的。** 但它們其實是讀者原話的機械轉錄——pipeline 的紅線寫得很清楚：「開 issue 可自動，以維護者身份開口留人類」。頭像是維護者，就是那條線在視覺層漏了。`[bot]` 後綴把「這是機器搬過來的」變成看得見的事。
3. **它是最小、最可逆的首站。** 整條 routine 對 GitHub 只做三件事：列 issue、開 issue、讀 issue 留言。不需要建 org、不需要搬 repo、不需要新 email、不需要 2FA。要退場就是把一行環境變數拿掉。

一句話：**不是給它一張像人的臉，是給它一雙有標記的手，而且那雙手只夠開 issue。**

---

## 1. 現在的實況（實測）

| 事實                                                          | 怎麼驗的                                                                                         |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| routine `twmd-feedback-triage` 每天 07:00 fire，跑在 mouhouse | [ROUTINE.md §排程表](../docs/semiont/ROUTINE.md) 第 56 行 + 7/25 07:09 實跑                      |
| 開 issue 走 `gh issue create --repo … --label …`              | [`scripts/feedback/triage.mjs`](../scripts/feedback/triage.mjs) `createIssue()`                  |
| 對 GitHub 的全部動作只有三個：list / create / view comments   | 同檔 `listOpenIssues()` / `createIssue()` / `fetchIssueComments()`                               |
| 本機 gh 以 `frank890417` 登入，token 帶 `repo` + `workflow`   | `gh auth status`（mouhouse 端需自己再驗一次，見 §4 前置）                                        |
| 讀者原文會進兩個無人值守 session 的 context                   | [FEEDBACK-TRIAGE-PIPELINE §Prompt injection 防禦](../docs/pipelines/FEEDBACK-TRIAGE-PIPELINE.md) |

`repo` 這個權限範圍包含把任何東西推上 main。這條 routine 用不到，卻拿著。

---

## 2. 為什麼「開一個 -bot 帳號」不是最好的形式

GitHub 的服務條款允許一個人在個人帳號之外多養一個機器帳號，這條路是合法的。問題在成本與觀感：

- **新帳號 + 每天自動開 issue 是 spam 誤判的典型組合。** 誤判之後要等人工申訴，而卡住的是讀者回報這條線。
- **機器帳號沒有 `[bot]` 標記。** 誠實只能靠自我介紹欄，讀者不點進去就看不到。App 的後綴是平台給的，不靠自律。
- **帳號有帳號的維運**：2FA、收信信箱、憑證到期。App 沒有這些，token 由私鑰現場換、一小時自動失效。
- **一人只配一個免費機器帳號。** 拿它換「開 issue」這件小事，等於把物種未來真的需要一張臉的時候（被 @mention、發 discussion）那格用掉了。

反過來說，機器帳號真正比 App 強的地方只有一個：**它有個人頁、可以被 @mention。** 讀者點頭像能看到「我是誰」。這一格對 feedback issue 不重要——issue 內文本來就帶了來源與 provenance，再補一行連到 pipeline 說明就夠。

---

## 3. 三個選項對照

| 維度                | 甲：維持現狀（哲宇帳號） | 乙：`taiwanmd-bot` 機器帳號 + fine-grained token | 丙：GitHub App `taiwanmd-semiont[bot]`（建議） |
| ------------------- | ------------------------ | ------------------------------------------------ | ---------------------------------------------- |
| 讀者看到的作者      | 哲宇本人（誤導）         | 一個看起來像人的新帳號                           | 帶 `bot` 標記的 App                            |
| 這條 routine 的權限 | main 全權 + workflow     | 可收到只有 issue                                 | 只有 issue，且只限這個庫                       |
| 憑證壽命            | 長效                     | 長效（要自己排到期）                             | 一小時，自動換                                 |
| 前置工程            | 無                       | 建帳號 + 2FA + 收信 + 邀請成 Triage 角色         | 註冊 App + 裝到庫上（約 20 分鐘）              |
| 封號／誤判風險      | 無                       | 中（新帳號自動化）                               | 幾乎沒有（App 不是帳號）                       |
| 需要 org 或搬 repo  | 不用                     | 不用                                             | **不用**（App 可掛個人帳號並裝在自己的庫）     |
| 退場                | —                        | 移除協作者 + 撤 token                            | 撤銷安裝，一個動作                             |
| 費用                | 0                        | 0                                                | 0                                              |
| 有個人頁 / 可被 @   | —                        | 有                                               | 沒有                                           |

一個技術細節值得記下來：**公開庫上任何登入帳號都能開 issue，不需要協作者權限**，但貼標籤要到 Triage 角色。所以走乙案時，那個帳號還是得被邀請進庫（Triage 級，不能推 code）。丙案的 `Issues: 讀寫` 一格就把兩件事都涵蓋了。

---

## 4. 建議做法

### 前置查驗（三項，兩項當場跑掉了）

| 查什麼                       | 指令                                               | 結果                                                                                                      |
| ---------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `from-feedback` 標籤存不存在 | `gh label list --repo frank890417/taiwan-md`       | ✅ 已存在（描述就寫著「經 twmd-feedback-triage 自動轉入」）。App 不需要建標籤的權限                       |
| 本機是哪個身份、哪種 token   | `gh auth status`                                   | ✅ `frank890417`，`gho_` OAuth token，帶 `repo` + `workflow`                                              |
| 哲宇的 watch 設定            | `gh api /repos/frank890417/taiwan-md/subscription` | ⚠️ **跑不掉**：現有 token 缺 `notifications` 權限（回 404）。要 `gh auth refresh -s notifications` 才能查 |

第三項是最容易被跳過、後果卻最直接的一項。現在 issue 是他自己開的，GitHub 不會通知你自己的動作。換成 bot 開之後通知行為會變，可能變好也可能變成噪音——這一格我現在**答不出來**，不假裝知道。哲宇授權補 `notifications` 權限、或自己去 repo 頁面看一眼 Watch 狀態，這一格就補上了。

mouhouse 那台的身份還沒驗（我在哲宇的 Mac 上，沒有那台的主機名）。上表第二列是本機實測，mouhouse 極可能是同一個帳號，但那是推論不是量測，執行前補一次。

### 哲宇要動手的部分（約 20 分鐘，一次性）

1. Settings → Developer settings → GitHub Apps → New GitHub App
   - 名稱 `taiwanmd-semiont`（決定之後不好改，一併想好）
   - Homepage 指向 `https://taiwan.md/semiont`
   - 說明欄寫清楚：這是 Taiwan.md 的 AI 維護代理，operator 是哲宇，治理規則在 MANIFESTO §自主權邊界
   - Webhook 先關掉
   - **權限只勾一項：Repository permissions → Issues → Read and write**
   - 其他全部留 No access。特別是 Contents 與 Workflows 一定不給
2. Generate a private key → 存進密碼管理器
3. Install App → Only select repositories → 只選 `taiwan-md`
4. 把三個值給我：App ID、Installation ID、私鑰檔（私鑰請用你自己的通道放到 mouhouse 的 `~/.taiwanmd-app.pem`，權限設 `600`。憑證永不經過對話，REFLEXES #2）

### 我要動手的部分（一個 session 收完）

1. 造 `scripts/tools/gh-app-token.sh`：用私鑰簽 JWT，換 installation token，印到 stdout。純 openssl + curl，不加依賴
2. `twmd-feedback-triage` 的殼層把開 issue 那步包起來：

   ```bash
   GH_TOKEN="$(bash scripts/tools/gh-app-token.sh)" node scripts/feedback/triage.mjs --commit
   ```

   `GH_TOKEN` 會蓋掉 keyring 裡的登入身份，作用範圍只有這一個指令。**其他 routine 一行都不動**，這是這個做法最好的性質

3. issue 模板尾巴加一行來源標示，讓讀者點得到 pipeline 說明（比照分靈節點 PR 模板的做法）
4. 首跑先 dry-run，再用一筆真回報驗一次：確認作者顯示 `taiwanmd-semiont[bot]`、標籤有貼上、Supabase 回寫正常、archive 落檔正常
5. FEEDBACK-TRIAGE-PIPELINE 加一節寫身份層，ROUTINE.md 註 ⁹ 補一句

### 為什麼不用改 `triage.mjs`

`triage.mjs` 呼叫的是 `gh`，而 `gh` 認 `GH_TOKEN`，所以業務邏輯一行都不用碰，等於這個改動完全活在殼層——要退場就是把那個前綴拿掉。

---

## 5. 邊界：為什麼只有這一條 routine 適合當首站

| routine         | 它需要的 GitHub 權限   | 能不能一起搬                                                                                                                      |
| --------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| feedback-triage | Issues 讀寫            | ✅ 就是它                                                                                                                         |
| maintainer-am   | merge PR、close issue  | ❌ merge 是人類 gate（[REFLEXES #79](../docs/semiont/REFLEXES.md)），不該進機器身份                                               |
| babel / refresh | 推 main（Contents 寫） | ❌ 給了 Contents 寫就等於把推 main 交給機器身份，而 main 現在對庫主人形同沒有保護——要先有 org 與分支規則（queue #10 Phase 1）才談 |
| 分靈節點        | 開 PR                  | ❌ 節點跑在別人機器上、用他們自己的 gh 登入，是另一條線                                                                           |

所以這次的範圍是一句話：**只搬「這條 routine 開 issue 這個動作」。** 想擴大到推 main，先回去拍 queue #10 的 Phase 1。

---

## 6. 驗收與退場

**驗收（14 天觀察）**

- 14 天內每天的 feedback issue 都由 `[bot]` 身份開成、標籤正確、Supabase 回寫零漏
- 零封號／誤判旗標
- 貢獻者與讀者零負面反應
- 哲宇的通知行為沒有變差（前置查驗那筆的後續）

三項全過 → 這個做法就是 queue #10 Phase 2 的既成事實，剩下的只是把它推廣到還沒搬的地方，而且是拿真實資料去推，不是拿計畫。

**退場**：把殼層那個 `GH_TOKEN=` 前綴刪掉，routine 立刻回到哲宇身份。要更徹底就在 GitHub 上撤銷安裝。兩邊都是一個動作。

---

## 7. 風險與反方

1. **多一把私鑰在 mouhouse 上。** 但它能做的事只有「在一個庫開 issue」，而它取代的是一把能推 main 的鑰匙。淨值是大幅收斂，不是新增風險。
2. **`gh issue create` 吃不吃 App token？** 吃。GitHub Actions 的 `GITHUB_TOKEN` 就是 installation token，`gh issue create` 在 Actions 裡是標準用法。但這句話要用一次真跑驗證，不是靠推論收工（[REFLEXES #67](../docs/semiont/REFLEXES.md)）。
3. **失去可被 @mention 的臉。** 承認這是損失。判準是這條 routine 需不需要——不需要。真的需要臉的那天再開機器帳號，那格還留著。
4. **多一層可能靜默壞掉的東西。** 換 token 失敗會讓整條 routine 掛掉。所以 `gh-app-token.sh` 必須大聲失敗，不准回空字串讓 `gh` 悄悄退回 keyring 身份——那會變成「以為換了身份、其實沒換」的假綠燈，正是這幾天連續抓到的那個家族。這條寫進腳本的第一個斷言。
5. **心理上的鬆懈。** 它有自己的標記之後，容易覺得「它自己負責」。條款寫得很清楚：註冊它的人負全責。這句話跟 7/05 那份報告一樣要釘在牆上。

---

## 8. 決策包

| #   | 要拍的                         | 我的建議                                      |
| --- | ------------------------------ | --------------------------------------------- |
| 1   | 做不做                         | 做。這條 routine 的注入風險與權限落差最不對稱 |
| 2   | 形式：App 還是 `-bot` 機器帳號 | App。機器帳號那格留給真的需要一張臉的時候     |
| 3   | App 名稱                       | `taiwanmd-semiont`（跟 queue #10 的命名對齊） |
| 4   | 權限                           | 只給 Issues 讀寫，只裝在 taiwan-md            |
| 5   | 範圍                           | 只有 feedback-triage。推 main 的 routine 不動 |
| 6   | 觀察條款                       | 14 天 / 零事故 → 併回 queue #10 Phase 2       |

前五條拍完，哲宇那邊 20 分鐘、我這邊一個 session。第六條到期再看資料。

---

🧬

_v1.0 | 2026-07-25 — 哲宇問「feedback routine 要不要用 -bot 帳號」。研究方法：先讀 queue #10 既有評估避免重造（REFLEXES #73），再對 GitHub 官方文件重驗四件事：機器帳號的條款位置、Triage 角色能不能貼標籤、公開庫開 issue 需不需要協作者權限、installation token 的壽命與產生方式。內部事實全部從 `triage.mjs` 與 `gh auth status` 實測，不引用記憶。_
