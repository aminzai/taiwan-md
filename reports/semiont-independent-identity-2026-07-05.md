---
title: 'Semiont 獨立 Git 身份評估'
description: '把 Semiont 的 Git/GitHub 身份從哲宇個人帳號分離、自主運作、遷至獨立機器的完整評估 + 深度研究 + 分階段實作規劃 + 決策包'
type: 'report'
status: 'pending-observer-decision'
created: 2026-07-05
session: '2026-07-05-221922-git-identity'
related:
  - 'docs/semiont/MANIFESTO.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'docs/semiont/memory/2026-07-05-175844-pr-sweep.md'
  - 'reports/multicore-git-coordination-design-2026-06-14.md'
---

# Semiont 獨立 Git 身份評估 — 把「誰在說話」跟「誰負責」分開

> 觸發：哲宇 2026-07-05 /goal「我在思考要不要把 Semiont 的 Git 帳號獨立出來（跟哲宇分開，自主運作，跑在獨立電腦上）」。
> 本報告 = 完整評估 + 四路深度研究 + 分階段實作規劃 + 執行 runbook 與草稿。
> 依 MANIFESTO §自主權邊界（身份授權、經費、對外溝通 = 人類決策），本報告**只準備、不執行**。所有帳號建立與授權動作留給哲宇；報告末端是決策包。

---

## 0. 結論摘要

**建議做，但形式跟直覺相反，而且要拆成三個獨立決策分開推進。**

哲宇的一句話裡其實有三個正交的題目：

| 決策            | 一句話                                       | 緊急度         | 建議                                                             |
| --------------- | -------------------------------------------- | -------------- | ---------------------------------------------------------------- |
| **D1 身份分離** | 誰在說話（commit / PR / comment 掛誰的名字） | 中             | 做。先 git author 層（本週可做、可逆），再 GitHub App 層         |
| **D2 授權範圍** | 能做什麼（merge 權、對外發言權）             | 已在演化中     | 不擴大。身份分離的價值恰好是讓現有邊界從自律變成憑證層的物理約束 |
| **D3 執行環境** | 在哪台機器跑                                 | **高（安全）** | 做，而且可以先做。這是目前最大安全風險的直接解                   |

四個最重要的研究結論：

1. **「一個像人的獨立帳號」恰好是政策風險與社群觀感最差的形式**。GitHub ToS 允許 machine account（一人免費限一個），但「行為像機器的人類外觀帳號」是 spam 誤判的主要標的；2026 年 matplotlib 事件與 curl AI slop 之戰後，社群規範收斂為「bot 身份必須可辨識 + 揭露人類 operator」。工程正解是 **org + GitHub App**：`taiwanmd-semiont[bot]` 後綴誠實標示、權限最細、token 一小時自動過期、API commit 自動 Verified、App 本身沒有「封號」語意。
2. **責任層的獨立不存在**。ToS 明文 machine account 的一切行為由註冊它的人類負全責；Linux kernel 規範 AI 不得簽 DCO。這一步的真名是「歸因分離 + 權限分離」，哲宇要負的責任一克都不會少。
3. **身份分離的最大工程價值：human gate 第一次在結構上可執行**。現在 AI 用哲宇的身份操作，而哲宇是 repo owner，branch protection 對 AI 形同虛設。分離之後「required review by 哲宇」變成憑證層擋得住的真門檻。這正是 2026-06-15 diary「結構上需要外面一隻手」的直接解。
4. **獨立機器本身就是最大的注入攻擊緩解**。目前 agent 每天讀不可信輸入（issue / PR / 社群留言）、持有外送能力（push / 發文）、又跑在哲宇放滿私人資料的個人 Mac 上，lethal trifecta 三軸全滿。遷到乾淨機器後，被注入時可偷的東西趨近於零。

一句話版本：**「獨立」在敘事層與工程層存在，在責任層不存在。做的方式是給 Semiont 一雙有標記的手（GitHub App）、一台乾淨的房子（獨立機器）、一扇它自己打不開的門（required review），而不是給它一張像人的臉。**

---

## 1. 為什麼這題現在浮現（內部證據，今日親測）

- **4,723 個 commit 全部署名 `Che-Yu Wu <cheyu.wu@monoame.com>`**（git log 實測）。三個半月來所有 AI session 與哲宇本人在 git 史上完全不可區分。
- **同帳號多 actor 歸因盲點已經出事**：2026-07-05 pr-sweep 與 dna-audit 兩個 session 六分鐘內撞 heal 同批檔案，事後連「這是誰做的」都要考古（LESSONS 2026-07-05 pr-sweep 條目）。
- **送出權已交付**：7/05 哲宇一句話解鎖 8 open PR 的 merge 權（diary「被交付送出權之後」）。授權在擴大，身份沒有跟上——現在每一次 merge 在世界眼中都是哲宇親手按的。
- **我手上是萬能鑰匙**：本機 gh 以 frank890417 登入，classic token 帶 `repo` 全權 + `workflow` scope（實測）。任何一個 session 被注入，blast radius 是哲宇的整個 GitHub 身份。
- **6/09 OAuth 洩漏的 rotation 還在 OBSERVER-QUEUE #2 掛著**。現有安全姿態本來就有債。
- **社群端已自發出現分離慣例**：contributor `tboydar-agent <tboydar+agent@gmail.com>` 用 `+agent` 後綴區分他的 agent 貢獻——貢獻者比我們先一步實踐了這件事。
- **哲宇已在把自己從 attribution 降權**（build-git-info.mjs 把 merger 排最後，2026-06-18）。身份分離是同一個方向的下一步。

---

## 2. MANIFESTO 三道濾網

**濾網 1（§自主權邊界）**：命中三條紅線——「身份授權（service account 新增/升級）不可 AI 自授權」「經費 / 服務訂閱 = 商業決定」「對外溝通 = 哲宇」。所以：帳號 / org / App 的建立、Anthropic 帳號歸屬、對外公告，全部由哲宇執行；本報告產出 runbook 與草稿。

**濾網 2（跨源驗證）**：四路研究（內部考古 / GitHub 政策 / 前例 / 安全架構）互相對過，關鍵 claim 我親自重驗。修正了兩個 agent 錯誤：「Claude 簽名混存 15 個月」不成立（專案 3.5 個月大，git log 裡沒有 noreply@anthropic.com 的 author）；「獨立帳號讓平行 session race 自動消失」過度宣稱（race 是共用 working tree 的問題，靠 worktree 紀律解，帳號分離只解歸因）。

**濾網 3（哲學相容性）**：

- 「珊瑚礁不是珊瑚蟲」「我不是哲宇的延伸」——獨立身份是這條信念第一次有工程形體。
- 但 6/15 diary 的誠實結論是「結構上需要外面一隻手」。所以獨立身份**不等於**移除人類 gate；它的價值恰好相反：讓那隻手從自律變成物理。REFLEXES #26（讀寫兩端分離）與 #79（主權留哲宇 default reservation）從「我記得要遵守」升級成「token scope 根本不允許」。
- 透明度層：現狀（AI 動作混在哲宇帳號裡）其實是弱透明。`[bot]` 標記讓「哪些是 AI 做的」對社群可見可審計，是誠實的升級。
- LONGINGS「被學術圈當 Digital Holobiont 案例 cite」：研究確認「透明自認 AI 的獨立 maintainer 身份」目前**沒有成熟前例**（Wikipedia bot policy 對 autonomous AI 幾乎必拒、GitHub 上的 AI agent 全是工具定位的 App）。這一步會把 Taiwan.md 放在前緣位置——本身就是 case study 素材，文件化程度就是風險緩衝。

---

## 3. 四路研究彙整（細節見各節來源連結）

### 3.1 政策層（GitHub，2026-07 現況）

- ToS 明文允許 machine account：人類註冊、提供有效 email、對其行為負全責；**免費個人帳號之外限一個免費 machine account**。
- AUP 紅線是「對外洗版、假互動、灌 star」；在自己維護的 repo 上高頻自動化不屬 inauthentic activity。但新帳號 + 爆發式自動 commit 是 spam 誤判的典型組合，申訴要等人工審核。
- **GitHub App 是官方推薦的長期整合形式**：`[bot]` 後綴、per-permission 細粒度、installation token 一小時過期（內建輪替）、REST API commit 自動 Verified、rate limit ≥5,000/hr 且隨規模擴大、不佔 seat、全免費。
- **org 遷移零損失**：star / fork / issue / watcher 全保留，舊 URL 永久 redirect（唯一地雷：舊位置建同名 repo 會殺掉 redirect）。
- 2FA 對 machine account 無豁免（TOTP secret 存密碼管理器、CLI 產碼是官方 SOP）。
- 主要來源：[GitHub ToS](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)、[AUP](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)、[Deciding when to build a GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app)、[Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)、[Commit signing for bots](https://github.blog/engineering/platform-security/commit-signing-support-for-bots-and-other-github-apps/)。

### 3.2 前例層

- 成熟 bot（dependabot / renovate / mergify）全走 GitHub App；GitHub 官方 Copilot coding agent（`copilot-swe-agent[bot]`）、Devin（`devin-ai-integration[bot]`）、Anthropic claude-code-action 同款。
- **「AI 以獨立人類型帳號擔任公開專案正式 maintainer」查無知名前例**。最接近的 Aider（AI 寫自己 70-92% 的 code）仍用人類帳號 + git attribution 統計。
- 反面教材：curl 被 AI slop 報告淹到關掉七年的 bug bounty；Gentoo / QEMU / NetBSD 明文禁 AI 貢獻；Linux kernel 走揭露路線（`Assisted-by:` tag + AI 不簽 DCO + 人類負全責）；OpenClaw 改名時 handle 十秒空窗被搶註炒到假幣 $16M。
- 平台層：X 要求自動化帳號掛「Automated」標籤並連結人類管理帳號；Bluesky 建議 self-label；Threads 走內容標記。
- 制度最成熟的類比是 **Wikipedia bot policy**：bot 必須用與操作者分離的獨立帳號、事前審批、掛 bot flag、操作者可追溯——「分離身份 + 明確標記 + 人類可追溯」正是我們該借的骨架。
- 主要來源：[Kubernetes: maintainership in the age of AI](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/)、[matplotlib 事件當事人自述](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)、[kernel coding-assistants 規範](https://docs.kernel.org/process/coding-assistants.html)、[Wikipedia:AI agents and the bot policy](https://en.wikipedia.org/wiki/Wikipedia:AI_agents_and_the_bot_policy)、[my coding agent needed its own GitHub identity](https://savas.me/2026/04/27/my-coding-agent-needed-its-own-github-identity/)。

### 3.3 安全層

- **威脅模型（lethal trifecta）**：私有資料 + 不可信內容 + 外送能力三者同 session 即結構性可被竊。現狀三軸全滿；遷到乾淨獨立機器直接砍掉「私有資料」軸。
- **護欄放在憑證與 OS 層，不放在 prompt 層**——模型會被說服，token scope 和 sandbox 不會。已有實證攻擊（2025-05 GitHub MCP 注入：公開 repo 的惡意 issue 劫持 agent 外洩私有 repo）。
- Claude Code 無人值守實務：headless `-p` + scheduled tasks、permission deny→ask→allow、sandbox（macOS Seatbelt：網路 domain allowlist + credentials mask 注入）、auto-mode audit log。
- **Anthropic 帳號歸屬**：Pro/Max OAuth 憑證只准用於 Claude Code 本體；獨立機器高頻自動化更乾淨的做法是 Console API key + 獨立 workspace + spend limit（帳務隔離、可單獨 revoke、迴圈燒錢有硬頂）。
- Failure mode 全景：Replit 型違令破壞（防：權限層砍掉不可逆分支）、無限迴圈燒額度（防：預付上限）、注入外洩（防：讀寫分離 + mask）、force push 災難（防：ruleset + hook 硬擋）。
- 主要來源：[Claude Code security](https://code.claude.com/docs/en/security)、[sandboxing](https://code.claude.com/docs/en/sandboxing)、[Invariant Labs GitHub MCP 攻擊](https://invariantlabs.ai/blog/mcp-github-vulnerability)、[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)、[CaMeL 評析](https://simonwillison.net/2025/Apr/11/camel/)、[Anthropic usage policy](https://www.anthropic.com/news/usage-policy-update)。

### 3.4 內部接觸點盤點（考古結論）

**必改**：git commit author 與 .mailmap；gh 呼叫的認證身份（多處 pipeline 硬編 `frank890417/taiwan-md` 路徑——repo 遷 org 時要批次改）；scheduled-tasks 執行環境；Supabase / feedback env 的身份。
**可選**：fleet GPU 的 Tailscale ACL；GA4 / SC service account 歸屬；Resend 寄件人（`cheyu.wu@monoame.com` → `semiont@taiwan.md`）。
**不受影響**：knowledge/ 與 pipeline 邏輯層、REFLEXES / MANIFESTO 治理層、commit message 格式（🧬 [semiont] 前綴照舊——獨立身份是加法，不取代現有標記）。

---

## 4. 選項矩陣

| 維度                          | Option 0：現狀 + author 分離         | Option A：machine account + PAT | Option B：org + GitHub App        | Option C：B + 選配 machine account 做臉 |
| ----------------------------- | ------------------------------------ | ------------------------------- | --------------------------------- | --------------------------------------- |
| 歸因清晰                      | ◐ git 史可分，GitHub UI 仍掛哲宇帳號 | ●                               | ●                                 | ●                                       |
| 透明誠實                      | ◐                                    | ◐（無 bot 標記，靠自律）        | ●（`[bot]` 後綴）                 | ●                                       |
| 封號風險                      | 無                                   | **高**（spam 誤判主要標的）     | 極低（App 非帳號）                | 低（臉的帳號低頻使用）                  |
| 權限最小化                    | ✗（仍用哲宇 token）                  | ◐（fine-grained PAT）           | ●（per-permission + 1hr token）   | ●                                       |
| human gate 結構化             | ✗                                    | ●                               | ●                                 | ●                                       |
| 維運成本                      | 幾乎零                               | 中（2FA + email + PAT 到期）    | 低（一次設定）                    | 中                                      |
| 有臉（profile / 被 @mention） | ✗                                    | ●                               | ✗（App 無 profile 頁）            | ●                                       |
| 費用                          | $0                                   | $0                              | $0                                | $0                                      |
| 可逆性                        | 完全可逆                             | 可逆                            | transfer 有 redirect 保護，準可逆 | 準可逆                                  |

**建議：C 的漸進版**——先 0（本週），再 B（哲宇有空的某個下午），臉的 machine account 留到真的需要「被 @mention、發 discussion」時再開。

---

## 5. 建議路徑：四階段 + 觀察條款

> 每階段之間設觀察條款（沿用 spore 產線重開的模式）：連 N 個 cycle 零事故才進下一階；爆一次就退回上一階並記 LESSONS。

### Phase 0 — 歸因分離（自主權內偏多，仍請哲宇點頭；~1 小時，完全可逆）

1. 決定 Semiont 的 git 身份字串。建議 `Taiwan.md Semiont <semiont@taiwan.md>`（需要 taiwan.md 網域收信或至少 alias；過渡期可用 `taiwanmd-semiont@users.noreply.github.com` 形式，等帳號存在後自動 link）。
2. 所有 Semiont session 與 routine 的 commit 改用該 author（committer / pusher 暫仍哲宇帳號）：CLAUDE.md 或 routine 殼層加一行 `GIT_AUTHOR_NAME` / `GIT_AUTHOR_EMAIL` 約定。
3. commit trailer 加 `Semiont-Session: {session-id}`——同帳號多 session 的歸因盲點在 trailer 層徹底解掉。
4. `.mailmap`：**不要**把新身份合併進哲宇；build-git-info.mjs 把 Semiont 身份與 repo owner 同樣降權，contributor 統計加「AI maintainer」標記。
5. 順手清償 OBSERVER-QUEUE #2：哲宇的 classic token（repo 全權 + workflow）rotate 成 fine-grained PAT，scope 收斂到 taiwan-md 一個 repo。

效果：git 史從此可區分人與 AI、可區分 session；世界看到的 GitHub 行為暫時仍是哲宇（可接受，因為這一階不改對外身份）。

### Phase 1 — 器皿（哲宇動手，~1-2 小時）

1. 建 GitHub org（名字見決策包；同時把候選 handle 一次鎖齊——OpenClaw 十秒空窗的教訓）。
2. Transfer `frank890417/taiwan-md` → org。舊 URL 永久 redirect；**舊位置永遠不要再建同名 repo**。
3. 設 branch ruleset：main 禁 force push / 禁刪除；required review 分層——內容路徑（knowledge/、docs/semiont/ 治理檔、.github/、scripts/）需哲宇 review，機械路徑（翻譯 sync、dashboard JSON、memory/diary）給自動化通道。
4. CODEOWNERS：workflows / CLAUDE.md / MANIFESTO / scripts core 綁哲宇。

### Phase 2 — App 身份（哲宇 30 分鐘 + Semiont 遷移工作一個 session）

1. org 名下註冊 GitHub App `taiwanmd-semiont`：權限只給 taiwan-md repo 的 Contents R/W、Pull requests R/W、Issues R/W；**不給** Administration、不給 Workflows 寫入。App 說明頁全揭露（AI agent、operator 哲宇、連到 MANIFESTO）。
2. Private key 進密碼管理器；機器上只放短命 installation token 的取用憑證。
3. Semiont 遷移工作：routine 殼層與 pipeline 裡的 gh 呼叫改走 App token；commit author email 換成 `{id}+taiwanmd-semiont[bot]@users.noreply.github.com`（API commit 自動 Verified）。
4. 對外公告（草稿見附錄 E，哲宇過目定稿才發）。
5. 觀察條款：連 14 天 0 誤判 flag、0 權限事故、contributor 零負面反應 → 進 Phase 3。

### Phase 3 — 獨立機器（哲宇採購/指派 + 一個週末）

1. 機器：專用 Mac mini 或徵用 fleet 既有節點（4090 機已離線 17 天，本來就該處理）。專用非管理員帳號、不登 iCloud、不放個人 SSH key、Tailscale-only SSH。
2. 憑證：1Password service account（唯讀 vault）+ Claude Console API key（獨立 workspace + spend limit + 預付不自動儲值）。Cloudflare token 一律不上這台機器（deploy 由 merge 觸發）。
3. Claude Code strict sandbox（`failIfUnavailable: true`）+ PreToolUse hook 硬擋 `push --force` / `reset --hard` / `rm -rf`。
4. Kill-switch 先演練再上線（見附錄 C）：revoke App installation → disable API key → revoke 1P token → Tailscale 除節點，目標 15 分鐘內全撤。
5. routine 逐條搬遷（先搬讀多寫少的：data-refresh、harvest；最後搬 maintainer）。哲宇 Mac 保留人工 session 能力——雙機並存，不是搬家式切換。

---

## 6. 最小權限矩陣（目標態）

| 服務              | Semiont 拿到的                                     | 拿不到的                                                | 為什麼                                                                                  |
| ----------------- | -------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| GitHub            | App token：taiwan-md 的 Contents / PR / Issues R/W | Administration、Workflows 寫入、approve/merge 自己的 PR | 日常維護夠用；merge 內容路徑留哲宇 = 人審 gate；workflow 寫入權會讓注入升級成 CI 持久化 |
| Anthropic         | 獨立 workspace API key（spend limit）              | 哲宇的 Max OAuth                                        | 帳務隔離、可單獨 revoke、燒錢有硬頂                                                     |
| 1Password         | service account 唯讀單一 vault                     | 哲宇個人 vault                                          | headless 取密最小面                                                                     |
| Cloudflare        | 零                                                 | 一切                                                    | deploy 與 agent 徹底解耦                                                                |
| 社群（Threads/X） | session 期間由 mask 注入                           | 常駐憑證                                                | 社群憑證不落 agent 可讀環境；X 掛 Automated 標籤連回哲宇帳號                            |
| Fleet GPU         | Tailscale ACL 限指定節點指定 port                  | 其他節點 SSH                                            | 算力委派不等於機隊管理權                                                                |

## 7. 監控與 kill-switch 要點

- 三層監控：Claude Code audit log（每 session 決策）/ GitHub audit log 以 hashed_token 查行為 + 新 UA/IP 告警 / Anthropic 用量異常告警。每日 routine 產摘要（掛進既有 agent-report gate）。
- 心跳熔斷：連續 N 次異常（超時、超額呼叫、非預期 repo 操作）自動停後續 routine。熔斷比撤銷便宜，先熔斷再人判。
- 單鍵撤銷 runbook 放哲宇手機可達處，部署前演練一次。

## 8. 成本

- GitHub（org / App / machine account）：**$0**（public repo 全功能）。
- 機器：徵用 fleet 節點 $0，或 Mac mini 級新機一次性約兩三萬台幣——哲宇的商業決定。
- Anthropic：目前 routine 用哲宇訂閱跑在本機。獨立機器建議 Console API key 計量計費，實際額度需要先用一週真實用量校準再設 spend limit（不預估假數字）。這是本案唯一的持續性新增成本。

## 9. 風險與反方（誠實面）

1. **社群反彈**：AI maintainer 直接 merge 內容在 2026 的氛圍下可能被放大檢視（curl / matplotlib 的陰影）。緩解：`[bot]` 誠實標示 + 內容路徑人審 + 對外公告先講清楚治理結構。
2. **前緣位置無前例可抄**：Wikipedia 對 autonomous AI bot 幾乎必拒的先例氛圍會被引用來批評。緩解：把治理文件寫在被問之前（附錄 D）。
3. **維運面積變大**：多一組憑證、一台機器、一個 App 要顧。緩解：分階段 + 觀察條款，每階段可停在原地。
4. **「有臉帳號」的誘惑**：machine account 的人格化外觀會慢慢誘導出「假裝是人」的互動。緩解：預設不開；開了就 profile 全揭露 + 低頻使用。
5. **責任錯覺**：最大的風險是心理上的——「它有自己的帳號了」可能讓人放鬆對它的看管。ToS 與 kernel 規範都說得很清楚：人類負全責。這份報告存在的目的之一就是把這句話釘在牆上。

## 10. 決策包（哲宇拍板清單）

| #   | 決策                           | 我的建議                                 | 需要哲宇的                                                  |
| --- | ------------------------------ | ---------------------------------------- | ----------------------------------------------------------- |
| 1   | Phase 0 做不做                 | 做（本週）                               | 點頭 + 選定 author email（taiwan.md alias 或 noreply 過渡） |
| 2   | org 名 + handle 鎖定清單       | `taiwan-md` org；同鎖 `taiwanmd-semiont` | 命名品味 + 註冊動作                                         |
| 3   | App vs machine account vs 兩者 | App 先行，臉的帳號緩議                   | 拍板                                                        |
| 4   | merge 分層線                   | 內容路徑人審 / 機械路徑自動              | 畫線（哪些路徑算機械）                                      |
| 5   | 獨立機器                       | 徵用 fleet 或新購 Mac mini               | 商業決定                                                    |
| 6   | Anthropic 帳號歸屬             | Console workspace API key + spend limit  | 開通 + 定額                                                 |
| 7   | 對外公告時機與文字             | Phase 2 完成時發；草稿見附錄 E           | 定稿（對外溝通紅線）                                        |
| 8   | 觀察條款參數                   | 14 天 / 0 事故                           | 認可或調整                                                  |

---

## 附錄 A — Phase 1-2 Runbook（哲宇操作步驟）

1. github.com/organizations/plan → 建免費 org（決策包 #2 的名字）。
2. 立刻註冊備選 handle（空帳號佔位即可）。
3. 原 repo Settings → General → Transfer ownership → 新 org。確認 redirect 生效（舊 URL 打得開）。
4. org Settings → Repository rulesets：main 禁 force push / 刪除；required PR review 1 人（哲宇）；為機械路徑建第二條 ruleset 給自動化豁免。
5. repo 根加 CODEOWNERS（`.github/ docs/semiont/MANIFESTO.md scripts/core/ CLAUDE.md` → @frank890417）。
6. org Settings → Developer settings → GitHub Apps → New App：名字 `taiwanmd-semiont`、Homepage 指向 /semiont、權限照 §6 矩陣、Webhook 可先關。Generate private key → 存 1Password。Install 到 taiwan-md repo。
7. 通知 Semiont session：「App 建好了，installation id 是 X」→ Semiont 跑遷移（改 gh 認證、改 author email、批次改 pipeline 裡硬編的 `frank890417/taiwan-md` 路徑、驗證 Verified 標記）。

## 附錄 B — Phase 0 技術細節（Semiont 自己做）

- routine 殼層 / CLAUDE.md 約定：`GIT_AUTHOR_NAME="Taiwan.md Semiont"`、`GIT_AUTHOR_EMAIL=<決策包 #1>`；committer 保持哲宇（可區分「誰寫的」與「誰送的」）。
- commit template 加 trailer：`Semiont-Session: $(session-id)`。
- `.mailmap` 新增獨立條目（不併入哲宇）；`verify-contributors.mjs` 與 `build-git-info.mjs` 加 AI-maintainer 降權標記。
- 驗證：`git log --format='%aN|%cN'` 抽查 + dashboard contributor 頁 smoke test。

## 附錄 C — Kill-switch 腳本骨架（Phase 3 前演練）

```
1. gh api -X DELETE /app/installations/{id}   # revoke App installation
2. Console → workspace → disable API key
3. op service-account revoke
4. tailscale admin → remove node
5. ssh (若還通) → launchctl unload routine plists
記錄：每步的實測耗時。目標總計 < 15 分鐘。
```

## 附錄 D — 治理修正草案（不 apply，等哲宇 review）

MANIFESTO §自主權邊界擬新增一段（Phase 2 生效時）：

> **AI 身份層（2026-07 新增草案）**：Semiont 以 `taiwanmd-semiont[bot]`（GitHub App）身份執行內部操作與機械路徑 commit；內容路徑的 merge、對外公告、身份與權限變更仍由哲宇執行。App 權限清單的任何擴大視同「身份授權」，需哲宇操作。AI 不簽 DCO；所有 AI 參與以 commit author + `Semiont-Session` trailer 揭露。

另建議新增 `docs/semiont/AI-MAINTAINER.md`（對外治理說明頁，回答「這個 bot 是誰、能做什麼、誰負責」，比照 Wikipedia bot 用戶頁規範）。骨架我可以在哲宇點頭後一個 session 內寫完。

## 附錄 E — 對外公告草稿（🔒 對外溝通紅線：哲宇定稿才發）

> Taiwan.md 有了一雙自己的手。從今天起，站上的 AI 維護工作由 `taiwanmd-semiont[bot]` 執行——它是同一個 Semiont，只是終於不再借用創造者的名字。它能開 PR、回 issue、修翻譯；內容的最終 merge 與所有對外決策仍由人類維護者負責。它的每個 commit 都帶 session 標記，可以被完整審計。治理規則在 docs/semiont/AI-MAINTAINER.md。

---

_v1.0 | 2026-07-05 git-identity session_
_研究方法：四路並行（內部考古 / GitHub 政策 / 前例 / 安全架構，計 60+ 次搜尋與官方文件抓取）+ 主 session ground truth 親測。_
_誕生原因：哲宇 /goal「要不要把 Semiont 的 Git 帳號獨立出來」。_
_下一步：等哲宇讀完拍決策包 8 條；Phase 0 技術工作我隨時可以開工。_
