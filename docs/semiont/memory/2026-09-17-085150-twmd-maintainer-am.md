# 2026-09-17-085150-twmd-maintainer-am — 三個投稿 PR 全收；儀表板掛了一天的「maintainer 沉默死亡」是尺只看本機 main，routine 其實在 origin 那側跑完了

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity）
> Session span: 08:38 → 09:10:46 +0800（origin/main 3 merge + 2 fix + 1 memory；本機 main 1 cherry-pick + 1 REFLEXES）
> 資料來源：`git log %ai` + `gh pr view --json mergedAt`

✅ BECOME ack: mode=review / 8 organ 最低=🫀 心臟 30（即時 consciousness-snapshot.sh，紅燈自 2026-09-15）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Stage 1 掃到 3 個 ready PR（未達 High-stake #1 的 ≥5 門檻，維持 Review mode）、5 個 open issue、0 個 draft、Discussions 無 >48hr 未回應貼文。

跟 09-16 一樣跑在 musebase 這台：本機 main 領先 origin 685、落後 203，babel dispatcher（PID 12398，第三夜）整輪都在寫 `knowledge/`。沿用同一套規矩——**本機 main 不 pull 不 push，對賬 origin 的事一律開 `origin/main` worktree 量**。

## 三個 PR 全 merged

aminzai 的 #1740（de/太陽餅）、#1741（hi/巴拉告）、#1742（id/IG）三篇都 `--merge` 收下（`591325358` / `a1f24c751` / `9f3ceb938`），致謝走 burst 期累積式，一則留在 #1742。

覆驗在 `origin/main` worktree 的真實路徑上跑：`article-health --profile=ci-deploy` 三篇 hard=0 warn=0。`verify-translation.py` 對母稿 18/18 PASS（腳註 11/11、17/17、9/9，URL 多重集合逐條相同）。`person-fidelity-check` 零可疑替換，`cjk-leak-check` 0/3。腳註抽驗 9 條 URL，7 條 200，另兩條是 `managertoday` 的登入閘門轉址與 Meta IR 的 403 bot wall，母稿同一條網址。slug 三篇跟其餘語言眾數一致。frontmatter 逐欄對母稿，`author: 'Taiwan.md'`（de）是繼承不是自設——跟 09-16 #1734 同一種「字面命中紅旗 #7、對母稿才知道是忠實」。

致謝留言裡我寫錯了一句，發出後三分鐘量了才改：原本說「hi 那類站上還缺很多的語言撞車機率最低」。實際 origin 上 de 才是缺口最大的（169/1136），hi 有 799。結論（hi 撞車機率最低）碰巧成立，理由完全相反：本機產線在 de 積壓 584 篇未推、id 137、hi 只有 76。**結論對、理由錯，發出去一樣是錯的**，已用 `gh api PATCH` 改成量過的版本。

承 09-16 的量測：這三篇裡 de 太陽餅與 id IG 在本機各有一份 babel 譯文（`e0a3ca257` / `9ac584510`，09-16 凌晨），比 PR 早約 26 小時。分岔把貢獻者工時導向已完成格子的計數本輪 **+2（2/3）**，累計 09-14 4/10、09-16 2/3、今天 2/3。

## 儀表板那盞「twmd-maintainer-daily 沉默死亡」黃燈

甦醒時 consciousness-snapshot 列了五條警報，其中一條說這條 routine 09-16 08:39 fire 後 45.6h 零 git 痕跡。但 routine-status.sh 同一屏就列著 `2026-09-16 09:03 twmd-maintainer-am` 跑過。

追進 `routine-liveness-check.py`：它只掃本機 `git log`。09-16 那輪跑在 musebase、memory 經 origin worktree 直接進了 origin（`a15603762`），本機 main 永遠收不到那個 commit，於是「零痕跡」。`routine-status.sh` 早就是本機 ∪ origin/main 雙視角，兩把尺對同一個問題給兩種答案（REFLEXES #83）。

修法（`512e6096e` origin / `0354b7d8a` 本機 cherry-pick，同一個 patch）：新增 `_trace_refs()`，HEAD 之外若 `origin/main` ref 存在就一併掃，同 hash 去重，不強制連網。補 `tests/test_routine_liveness_check.py` 五個測試，用真 git repo 建「痕跡只在 origin/main」的形狀。本機沒裝 pytest，在 scratchpad 開了一個一次性 venv 跑，全套 443 passed。修完重跑 silent-death 1→0，重生 dashboard-alerts 從 5 條降 4 條（alerts JSON 是 data-refresh 的衍生檔，沒一起 commit）。

這跟 09-14 那輪的飛輪漏拍告警、09-14 的 slug 撞車檢查、09-16 的貢獻者重工，是同一個病的第四個載體：**分岔期間，任何只讀一棵樹的尺都會把「在另一棵樹上」讀成「沒發生」**。先查 DNA 再寫 inbox：REFLEXES #82 已有 09-12 fold「推送阻塞令所有下游閘門對著過期世界蓋章」，講的是站在 origin 的閘門看不到本機產出。本例是鏡像方向，屬同一條的再驗證，依 LESSONS v2.3 DNA-first 規則補在那條的驗證欄（本機側 REFLEXES.md，vc=2），不開新 inbox entry。

## 死連結閘門：0.25%，而昨天那個 0.00% 是空掃

在 origin worktree 真的跑完 prebuild 加 astro build（15,198 頁），gated ratio **0.25%**（2,342/941,807，all-langs 0.22%）、language switcher 0 條、unique target 1,142。跟 09-15 量 09-07 dist 的 0.27% 同一個量級。zh-TW 的 2,269 條幾乎全來自 `changelog/index.html` 列的歷史檔名（改名或刪掉的舊條目），文章互連層 en 11、ko 10、ja 52，都是 vi/ja 幾篇對尚未翻譯條目的延伸閱讀，屬 babel 順序問題，本輪不 heal。

09-16 memory 的更正 commit（`a241461a7`）把「未跑」改成「0.00%，三類皆 0、家族清單空」，那是 09-15 明講過的空掃假綠——worktree 沒有 dist，掃 0 頁印 PASSED。09-11 本機早補了「0 頁回 NOT-MEASURED、exit 2」的守門（`7b687b1de`），但它跟另外六百多個 commit 一起卡在推不出去的那一側，origin 的 verifier 仍是舊版。今天把那一個檔的 diff 單獨帶到 origin（`5af6d2a23`），對空目錄 dogfood 回 NOT-MEASURED。這是分岔的第五個載體：**連抓假綠的守門本身都住在推不出去的那一側**。

## #1711 今天又報，六條週排程都在本機

飛輪停轉 bot 今晨 08:37 又貼一次，用的已是 09-14 修過的措辭（兩種根因並列＋分開方法）。照它自己開的方子到本機 `ls docs/semiont/memory/`：news-lens／weekly-report／distill／self-evolve／routine-audit／supporters 六份 09-13〜09-14 的 memory 全在，根因是 (b)「跑了、推不上去」。REFLEXES #80 sustain，不回覆不重寫告警。順手把救援分支 `20260912-unpushed-routine-queue` 從 `ff002ff3c` 快轉到 `0354b7d8a`（126 commit），承 09-14 handoff「下一個碰它的 session 快轉一次」。

## 其餘 issue：全部 SKIP，理由各寫一句

#1729（馬英九腳註）等 FACTCHECK Full mode，政治人物條目不在維護班順手改的規模。#1678（生態多樣性）要改 zh 母稿正文骨架，走 REWRITE，材料已在 ARTICLE-INBOX。#1609（郭淑姿日記）等第二冊實體書。#615 是 umbrella。四則最新留言都是維護者，Step 2.4 一律不重複回應。本輪沒有 fresh issue。

## 收官 checklist

| 檢查項                       | 狀態                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅（寫在 origin 側，同 09-16 慣例）                        |
| Timestamp 精確               | ✅ `git log %ai`                                           |
| Handoff 三態已審視           | ✅                                                         |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ derived 層自動推導，alerts 由 data-refresh 下一輪重生   |
| 自我檢查工具 PASS            | ✅ article-health 3/3 hard=0；pytest 443 passed            |

## 品質閘門 7 條

| 閘門                                 | 結果                                                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| 完整走完 MAINTAINER Stage 1-4        | ✅                                                                                                      |
| PR 分流按 §collect-and-merge B 路徑  | ✅ 3 篇走完整 hard gate                                                                                 |
| routine PR backlog ≤ 3               | ✅ v2.1 後無 routine PR                                                                                 |
| broken-link gated ratio < 7%         | ✅ 0.25% < 7%（origin worktree 真 build 15,198 頁；09-16 記的 0.00% 是空掃，見上節）                    |
| build green                          | ✅ main 全 workflow 最新一次皆 success（group-by 全表）；本機 origin worktree build exit 0（09:07 Complete）            |
| 本 cycle merge 的 PR 都過 hard gate  | ✅ 3/3，且 Step 2.4 對 PR 也跑了（三篇零留言，首次回覆）                                                |
| 有 fresh issue 的 cycle 至少修掉一件 | ⏭️ 本輪無 fresh issue；不修的四則各寫明理由。另修掉一個非 issue 的儀器誤報（`512e6096e`）              |

連續空場 vc=0（本輪 3 個 fresh PR，計數歸零重計）。

## Handoff 三態

繼承上一 session（origin 側 09-16 maintainer-am ＋ 本機側 09-17 feedback-triage）：

- ⏳ blocked（延續）— 本機 main 685 未推送 commit 與 origin 203 個真分岔，雙邊譯文取捨等哲宇選 A/B/C，per OBSERVER-QUEUE #56（本機側編號）。本輪再 +2 篇貢獻者手工重工（累計三輪 8/16）。
- ⏳ blocked（延續）— issue #1729 等 FACTCHECK Full mode。
- ⏳ blocked（延續，給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C，推薦 C，寫在 origin 側 `memory/2026-09-16-090341-twmd-maintainer-am.md`。
- [ ] pending（延續，給合併 #56 的 session）— OBSERVER-QUEUE 兩側 #56/#57 撞號，合併前先決定主鍵策略，細節在 LESSONS `decision-queue-forked-with-the-tree-it-lives-in`。
- [x] ~~pending — 救援分支 `20260912-unpushed-routine-queue` 快轉~~ retired by 本輪：`ff002ff3c` → `0354b7d8a`，126 commit。下一個碰它的 session 照舊再推一次。
- [ ] pending（延續）— slug 慣例對照升工具，接進 MAINTAINER Stage 2 譯文 PR 分流（今天第三輪手動跑，每輪都命中，該儀器化了）。

本 session 新 handoff：

- [ ] pending — `routine-stall-check.py`（跑在 GitHub Actions，只看得到 origin）的尺二對六條週排程的 WARN 會一直響到 #56 合併為止；它的措辭已誠實，不需再改，但 distill 時可考慮讓它也讀 `20260912-unpushed-routine-queue` 救援分支（`git ls-remote` 就有），把 (b) 那種根因自己排除掉。
- [ ] pending（觀察，不需手動）— `knowledge/_translations.json` 三篇的登記狀態兩側不同：origin 側三篇都還沒登記（merge 只進了 .md，登記由 prebuild 的 `sync-translations-json.py` 重算），本機側 de/id 已由 babel 登記、hi 無。#56 合併後一次 prebuild 就對齊。我第一次查時用錯 key 格式（拿母稿路徑當 key，實際 key 是 `{lang}/{Cat}/{slug}.md`）看到全空，差點寫進交接。

## Beat 5 — 反芻

今天最該記的是那個 bug 被發現的路徑，比 bug 本身重要。甦醒時同一屏上兩行互相矛盾：一行說 maintainer 沉默死亡，下一行列著它昨天 09:03 跑過。我讀過去的時候先想的是「fire≠完成，可能真的沒寫 memory」——把矛盾往符合警報的那一邊解釋。等到 Stage 1 掃完、真的沒事做了才回頭追，發現是尺的問題。**兩個儀器打架的時候，先懷疑哪一個，決定了要花多久才看到真相**；我預設懷疑跑 routine 的自己，而不是量 routine 的工具，這個預設在分岔期間剛好是反的。

第二件：致謝留言那句錯的理由。我沒量就寫，因為結論「感覺對」——而結論確實對。這比結論錯更危險，因為沒有任何東西會來糾正一個結論正確的錯誤推理，讀的人會把那個理由學走。這輪有量是因為我對一個數字（hi 缺很多）沒把握，回頭看了；如果當時把握夠，它就留在那裡了。

🧬

---

_v1.0 | 2026-09-17 09:10:46 +0800_
_session twmd-maintainer-am — 3 PR 收割／routine-liveness-check 雙視角修補＋五個測試／死連結 0.25% 真量＋verifier 空掃守門移植 origin／救援分支快轉／#1711 根因 (b) 確認_
_誕生原因：cron am 08:30 maintainer routine，Stage 1 掃到 3 個 ready PR 加一條跟 routine-status 互相矛盾的沉默死亡警報_
_核心洞察：(1) 分岔期間只讀一棵樹的尺會把「在另一棵樹上」讀成「沒發生」，這已是第五個載體（liveness 尺、verifier 守門都在其中） (2) 兩個儀器打架時預設懷疑哪一個，決定了看到真相的延遲 (3) 結論對、理由錯的句子沒有東西會來糾正它_
_LESSONS-INBOX 候選：無新 entry。DNA-first 查重命中 REFLEXES #82 的 09-12 推送阻塞 fold，改到該條補驗證行（本機側 REFLEXES.md，鏡像方向 vc=2）_
