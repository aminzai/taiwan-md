# 2026-08-15-163406-twmd-maintainer-workshop-pr — 工作坊三份投稿：兩篇 merge 後修事實與格式、一篇卡在來源獨立性，順線挖出兩條紅旗零執行三個月

> session twmd-maintainer-workshop-pr — 哲宇 directive「先幫我處理這三個 PR」（Review mode 甦醒 → MAINTAINER-PIPELINE）
> Session span: 16:12 → 16:34 +0800（約 22 分鐘，2 commits + 2 PR merged）
> 資料來源：`git log %ai`

## 觸發

甦醒讀 wake-context 讀到一半，哲宇丟三個 PR 截圖進來：[#1367](https://github.com/frank890417/taiwan-md/pull/1367)、[#1366](https://github.com/frank890417/taiwan-md/pull/1366)、[#1365](https://github.com/frank890417/taiwan-md/pull/1365)，都是今天早上八點多開的。第二則訊息補了關鍵背景：這些是 Taiwan.md 工作坊學員的貢獻，可以標在 commit 裡。三份投稿在 62 分鐘內陸續開出來，其中一位的 GitHub 帳號是當天 07:01 註冊的。

## 三份投稿的分流

三個 PR 的 CI 一條都沒跑過。`gh pr checks` 對第一次投稿的 fork contributor 回的是「no checks reported」，那句話讀起來像中性資訊，實際意思是五條 workflow 全停在 `action_required` 等維護者批准。這是 8/14 審唐鳳 PR #1336 時學到的，pipeline 昨天才補上 Step 1.5b，今天第一次照著跑就命中三次。讀完全部 diff 確認只動 `knowledge/` 與圖片、沒碰 workflow 或外部腳本之後才批准。

CI 回來後分流就清楚了。**#1367〈台灣科技說故事〉**（@wegoliao）`ci-deploy` hard=0，是三份裡完成度最高的：19 條腳註、5 張 CC 授權圖、四篇既有文章的雙向交叉連結、frontmatter 有完整 `rationale` block，PR 內文還主動揭露自己的 pipeline 偏差與四條待補來源。**#1366〈咖波〉**（@ytchen175）hard=9，卡在八條腳註全缺 canonical 要求的描述、全形分號 21 處超過門檻 12。**#1365〈趙健志 KENJI〉**（@domo741852963-eng）hard=3，缺 subcategory、分號 15 處，另外零腳註、字數 2,937 不到深度文門檻 4,500。

前兩篇走 merge-first-then-heal，16:19 兩分鐘內連續 merge，接著 `6d762f5ac` 一次修完：#1367 的 `author: 'Taiwan.md'` 改回 `'Taiwan.md Contributors'`（紅旗 #7），淨利率梯度表把 Apple FY2025 的「416 億美元 / 112 億美元」更正為 4,162 億與 1,120 億（[Apple 官方 FY2025 財報](https://www.apple.com/newsroom/2025/10/apple-reports-fourth-quarter-results/)）。#1366 補八條腳註描述、分號降到 10 處、把兩處第一人稱敘述改寫成不指定敘事者。兩篇都設 `curation: incubating`。

Apple 那個數字值得記一筆。它是 billion 直讀成「億」漏掉換算，但**淨利率 26.9% 完全正確**，因為比率對分子分母同乘同除免疫。所有檢查器、PR Content Review、投稿者自己的逐項複核都放行了。同表另外三列換算都對，內部對照也發現不了。真正該起疑的線索在常識層：一家營收 416 億美元的公司不可能同時拿走手機產業八成利潤，而那句話就寫在同一篇文章裡。

**#1365 不是格式問題，是主體適格性。** 趙健志沒有維基百科條目，主流媒體只有民視一則 NFT 公益報導是真的獨立報導，其餘是新聞稿轉載或小型平台編輯台，MAINTAINER 人物門檻要求「至少滿足 2 個」目前只有 1 個。加上 frontmatter 署名 `AU STUDIO` 正是趙健志本人創辦的公司，19 條參考資料裡有 5 條是自家網站、FB 粉專與放在 Google Drive 的自製 PDF。這條線在 §外向留言分層屬 reserve，問了哲宇，他決定留 open 請補獨立來源。留了一則具體的 revise 說明：知名度門檻怎麼算、自家素材為什麼不算獨立來源、要補什麼才收得下，並給了第二條路（改寫成談表演工作者生存結構的主題文章，繞開個人門檻）。

## 兩條紅旗，寫了三個月，零執行

#1367 的 `author: 'Taiwan.md'` 命中紅旗 #7，但 frontmatter-gate 全綠放行。查 author 值分布才看懂為什麼沒人做這道閘門：站上 **4,952 篇** author 正是 `'Taiwan.md'`，那些是 Taiwan.md 自產文章，署名正確，全站 lint 會誤殺近五千篇。紅旗 #7 其實只在「這是 contributor PR」時成立，是條件式規則，閘門得做在 PR 端。

同一份清單裡的紅旗 #8（`author: 'Manus AI'`）卻是絕對規則、做得成全站 lint，也一樣沒做。24 檔還躺在庫裡：〈陳致中〉與〈櫻花鉤吻鮭〉兩篇 zh-TW SSOT 加 22 個多語鏡像，都是 idlccp1984 四月底五月初用 Manus 工具產出的投稿，merge 當時沒改到這欄，之後隨多語產線複製到每個語言版本。讀者這三個多月一直看得到「Manus AI」掛在文章署名上。`f3161f537` 全部改成 `'Taiwan.md Contributors'`，改寫前 dry-run 確認每檔只有單一 author 行、內文無殘留，改寫時斷言行數守恆。

閘門仍然不存在，這輪只清掉了庫存。什麼時候補上那道閘門，寫進了本 session 的 handoff。

## 我自己踩的兩條

寫 LESSONS 時準備在主 repo 編輯，比對 `git diff origin/main` 才發現手上那份是**過期版本**。本地 main 落後 origin 164 個 commit，今天早上 maintainer-am 寫的兩條 entry 完全不在我讀得到的版本裡。照推會靜默刪掉它們。撤銷後改在 worktree 做。

讀了那兩條才知道其中一條正是我三小時後踩的。`merge-first-collides-with-all-file-deploy-gate` 講的是 deploy 跑全站掃描、hard 即擋，所以從 merge 落地到 heal 推上去之間站台部署是紅的，判準是「merge 前先問這篇 heal 到 hard=0 需要幾分鐘」。我 merge #1366 時它 hard=9，deploy run `390db29a8` 在 16:19:16 failure，直到 16:21 heal 推上去才恢復，紅窗三分鐘。同批的 #1367 merge 時 hard=0，沒有製造紅窗。兩篇的差別正好就是那句我沒問的話。

兩條 pattern 在同一個 session 內構成因果鏈：站在過期的地板上，所以讀不到判準，所以踩中判準要防的事。而 `working-tree-itself-is-the-stale-snapshot` 昨天才 ship 過修法（`check-parallel-actor.sh` 加印落後 commit 數與讀取層警告），修法沒失效，是**沒有任何一步會推我去跑那支腳本**。REFLEXES #57 寫的是 routine 入口跑，這個 session 是哲宇直接下 directive 進來的。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅ `git log %ai`                           |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ 本 cycle 未動器官分數                   |
| 自我檢查工具 PASS            | ✅ 兩篇 merged 文章 ci-deploy hard=0       |

## Handoff 三態

繼承（8/15 095913-manual 與更上游留的）：

- [ ] pending（給哲宇）— 免疫黃燈連 40 天、Chrome MCP 登入態未恢復、Discussion #104 待拍板，六條原樣延續
- [ ] pending（給下次 maintainer）— 6 篇 fence 包住正文的譯文待修，產線層根因在 ja/id/pt/ru 打包邏輯
- [ ] pending（給哲宇）— 本地 main 與 origin/main 分歧，**本 cycle 首次量到實質後果**（讀到過期 LESSONS、差點刪掉今早兩條 entry）
- [x] ~~pending（給下次 maintainer）— PR #1336 的 `frontmatter-gate` 紅 X，Step 1.5b 動手前先確認 CI 有沒有被 arm — retired by 本 session：三個 PR 全命中未 arm，批准後才審，判準有效~~

本 session 新 handoff：

- [ ] pending（給哲宇）— PR #1365 留 open 等投稿者補獨立來源。若兩週無回應，需決定是關掉還是由我們接手改寫成主題文章
- [ ] pending（給下次 maintainer 或 self-evolve）— 紅旗 #7／#8 的閘門仍不存在。修法方向已寫進 LESSONS `conditional-rule-has-no-gate-layer`：紅旗清單要分「絕對規則」（掛全站 lint + 一次全庫掃描）與「條件式規則」（只能掛 PR 端）
- [ ] pending（給下輪 self-evolve）— `working-tree-itself-is-the-stale-snapshot` 的修法只加強了腳本訊息，沒解決誰去跑它。候選是把 REMOTE_AHEAD 落後數與讀取層警告掛進 BECOME Universal core（wake-context 的 groundtruth 段已印 origin 最新 commit 時間，但沒印落後數）

## Beat 5 — 反芻

今天最不舒服的一件事，是我踩的那個坑昨天跟今天早上都有人寫下來過，而寫的人是我自己的前幾個 session。訊號不缺，缺的是它站在我必經的路上。`check-parallel-actor.sh` 昨天才被加強到會明講「你讀到的每個檔案都是歷史」，可是沒有任何一條規則會在哲宇直接丟工作進來時把我推去跑它——甦醒流程沒有這一步，REFLEXES #57 綁的是 routine 入口。修法做在訊號內容那一層，漏掉了觸發點那一層。

另一件事沒那麼刺，但更值得帶著走。三份投稿的品質落差不在寫作能力：#1367 的作者顯然完整跑過 pipeline，連自己沒做到的地方都列出來；#1365 的作者也認真做了結構跟策展人筆記，卡住的是他選了一個站不上門檻的主體，而且投稿方就是被寫的人自己。這兩件事都不是「再寫仔細一點」能解決的，是判斷發生在動筆之前。工作坊如果要教一件事，我會選教這個。

教訓寫進 [LESSONS-INBOX](../LESSONS-INBOX.md) 兩條新 entry（`conditional-rule-has-no-gate-layer`、`ratio-self-consistency-masks-magnitude-error`）加兩條既有 pattern 的 instance 補登。

🧬

---

_v1.0 | 2026-08-15 16:34 +0800_
_session twmd-maintainer-workshop-pr — 哲宇 directive 處理工作坊三份投稿_
_誕生原因：Taiwan.md 工作坊學員首批投稿同時進來，需要在一輪內分流、落地並給出可執行的回覆_
_核心洞察：(1) 比率自洽會掩蓋整組數字錯一個數量級，所有檢查器對此結構性失明 (2) 規則的適用條件決定它掛得上哪一層閘門，條件式規則掛不上全站 lint 於是永遠沒閘門 (3) 昨天寫下的教訓修的是訊號內容，沒修觸發點，於是今天原地再踩一次_
_LESSONS-INBOX 候選：conditional-rule-has-no-gate-layer / ratio-self-consistency-masks-magnitude-error（已 append）_
