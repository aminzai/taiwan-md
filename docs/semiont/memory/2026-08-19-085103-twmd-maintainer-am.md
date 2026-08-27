---
session_id: '2026-08-19-085103-twmd-maintainer-am'
session_span: '08:30 → 08:55 +0800'
trigger: 'cron routine twmd-maintainer-daily (am 08:30)'
observer: 'none (cron)'
beat_coverage: 'Stage 1-4 (MAINTAINER-PIPELINE)'
---

✅ BECOME ack: mode=review（PR triage 3 < 5，未觸發 High-stake 升 Full）/ 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，讀數齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# 2026-08-19-085103-twmd-maintainer-am — 我拿去問「這個 PR 有沒有跑過 CI」的那支儀器，只看得見最近六小時

> session twmd-maintainer-am — cron maintainer 巡邏
> Session span: 08:30 → 08:55 +0800（約 25 分鐘）

## Stage 1 掃描

| 項目                    | 實數                                                                        |
| ----------------------- | --------------------------------------------------------------------------- |
| open PR                 | 10（draft 7 / 待審 3）                                                      |
| open issue              | 4（#1440 / #1389 / #1184 / #615，全部前輪已有處置）                         |
| open discussion 未回應  | 0（11 條全數有維護者回覆，最新 #104 8/18 剛回）                             |
| 過去 24hr routine fires | 10 條（embeddings / routine-sync / data-refresh / harvest / triage 各就位） |
| 過去 48hr commits       | 264                                                                         |
| build / CI              | ✅ deploy 最近三次 success                                                  |
| broken-link gated ratio | ✅ 0.27%（all-langs 0.25%，門檻 7%）                                        |
| 免疫器官分數            | 🛡️ 59（八器官最低，chronic 自 7/05）                                        |

三個待審 PR 都不是今天才出現的，而且三個的下一步都不在我手上：#1430 + #1325（tboydar 德文兩批 59 檔）等 OBSERVER-QUEUE #29 的 `de` 語言啟用決定；#1365（趙健志）等 #30 的人物門檻決定。照舊寫法這會是一個「effective empty」的 cycle。

它不是。

## 這個 cycle 真正做完的事

### 一支專門抓「存在 ≠ 有跑」的偵測器，自己是盲的

`gh pr checks 1365` 回「no checks reported on the 'agent/add-kenji-zhao-profile' branch」。commit 的 check-runs API 回 `total_count: 0`。

MAINTAINER Step 1.5b 就是 8/14 為了這種情況造的，判準寫「`checks=0` 且 `待批准>0` → 這個 PR 沒有任何 CI 跑過」。照它寫的指令跑：

```
待批准 = 0
```

零。所以照判準，這個 PR 不算 UNARMED，只是「沒配置 CI」。

加上 server-side `?branch=<head>&per_page=100` 之後，同一個問題的答案是 **84**。最早一筆從 8/15 卡到現在，整整三天。

差別在哪：原本那段指令用 `gh api repos/…/actions/runs` **不帶 branch 參數**，再用 jq 過濾 `head_branch`。那個 endpoint 預設只回**最新 30 筆** run——實測這個 repo 的 30 筆涵蓋 **6 小時 20 分**（babel 整點 commit、deploy 頻繁）。一支要抓「卡很久沒人管的 PR」的偵測器，視野只有六小時。**適用範圍跟它的目標對象完全互斥。**

而它失效的方式不是報錯，是回答「安全」。三天內每一輪 maintainer 都拿它問過同一個問題，每次都得到沒事。

### 修法：搬進儀器，判準拆三態

造了 [`scripts/tools/pr-ci-armed.sh`](../../scripts/tools/pr-ci-armed.sh)，把取數邏輯從文件裡的可貼 snippet 搬進工具（同 BECOME §1.3 殼層取數鐵律：可貼的 snippet 會腐爛，儀器會被 dogfood）。判準從一句話升三態，把原本混成同一格的兩種「零檢查」拆開：

| state           | 意思                               | 處置                   |
| --------------- | ---------------------------------- | ---------------------- |
| **ARMED**       | head sha 上有 check-run            | 綠紅可信               |
| **UNARMED**     | 零 check-run **且**有 run 卡待核准 | 被擋住，有人要按核准   |
| **NO-WORKFLOW** | 零 check-run **且**零待核准        | 沒被觸發，paths 不匹配 |

這兩種的處置完全不同，混在一起就是 REFLEXES #38。dogfood 全站 10 個 open PR：#1365 UNARMED（唯一），其餘 9 個 ARMED。

核准指令也改了——只放 head sha 那批。#1365 若照舊寫法把整條分支的待核准全放出去，等於為了看一次結果燒掉 84 筆 runner。

### 第二個發現：核准不是對投稿者永久生效

**8/16 的 cycle 已經核准過一次**、跑出結果、告訴投稿者 `terminology hard=1`（「視頻」）。投稿者修好又推了四次——四批 run 全數退回 `action_required`。

原本 pipeline 的敘述（「GitHub 對第一次投稿的 fork contributor 預設不自動跑 CI」）讀起來像核准一次就過關。實際上每一次新 push 都要重新確認 armed。已補進 Step 1.5b 觸發段。

所以投稿者的體感是：照著回饋改完，然後就沒有下文了。三天。

### 實際處置

核准 head sha 那兩筆 run，兩條全綠（`frontmatter-gate` pass / `PR Content Review` pass）。另外照今天新立的診斷紀律，把 PR 的內容檔帶進 main 樹用 main 的檢查器量一次：

```
article-health.py --profile=ci-deploy → hard=0  warn=44  info=9  passed=True
TWMD_VALIDATE_FILES=… node scripts/core/test-frontmatter.mjs → 1/1 OK
```

**「視頻」確認修掉了，硬門檻 0。技術面現在完全沒有東西擋著這篇。**

回覆投稿者：道歉、講清楚是我們的指令有 bug 而不是他的問題、貼出檢查結果、列出剩下的 warn（§11 對位句型約 5 處、全形分號 12 處、description 48 字偏短）當作可選的改進。門檻決定原封不動留在 #30，沒有猜結論也沒有承諾時間。同步把 #30 條目裡「只有一個 hard」那句更新成現況——那句已經是三天前的事實，留著會讓拍板的人拿舊資料判斷。

### 順手收掉昨天交給今天的兩條

昨天 handoff 留了兩條 pipeline 明文化候選，都已寫進 canonical：

1. **§1b 新增〈格式債的 default 是 P1〉**——`maintainerCanModify == true` 時直接把格式修補 push 進對方分支，不是留說明等他自己修。依據是 idlccp1984 七篇卡三天：閘門說明改寫進 `$GITHUB_STEP_SUMMARY` 之後理由讀得到了，但要對方主動點進 Actions 才看得見，三天零修正，直到有人直接推修補才動。邊界寫明：P1 只推格式，內容判斷不推。
2. **Stage 2 新增〈診斷紀律〉**——把 PR 內容檔帶進 main 樹跑，禁 checkout PR 分支後在那棵樹上讀檢查器。依據是 8/18 在 `pr/1372` 的樹上「發現」三個早已修好的缺陷，差點對 212 篇提批次重構。

MAINTAINER-PIPELINE v2.6 → v2.7。

## 一句話說今天學到什麼

新造一道閘門去抓某種盲點時，那道閘門自己的取數口也會有同一種盲點——而且更難發現，因為它每次都有跑、有回答，回答還是安全的那一邊。`待批准=0` 同時代表「查過了沒有」跟「我根本看不到那麼遠」，這兩件事共用一個符號（REFLEXES #85）。

## Quality gate

| Gate                                   | 結果                                                                                     |
| -------------------------------------- | ---------------------------------------------------------------------------------------- |
| open issues 都有 status label/assignee | ✅ 4 件全有處置（#1440/#1184 → OBSERVER-QUEUE、#1389 已進 ARTICLE-INBOX、#615 umbrella） |
| open PRs ≤ 5d age 都有 review comment  | ✅ 三個待審 PR 全有；#1365 本 cycle 新回一則狀態                                         |
| broken-link ratio < 7%                 | ✅ 0.27%（all-langs 0.25%）                                                              |
| build green                            | ✅ deploy 最近三次 success                                                               |
| BECOME ACK 一行記憶體頂                | ✅                                                                                       |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | n/a — 本 cycle 非空場（3 待審 PR + 一個真實缺陷修掉）                                    |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ 無 fresh issue；改為修掉 Step 1.5b 偵測器本身 + 解掉 #1365 卡三天的 CI 積壓           |

## Handoff 三態

- [ ] pending（給下一個 maintainer cycle）— `pr-ci-armed.sh` **沒有掛在任何自動路徑上**，靠 Stage 1 手跑。UNARMED 的 PR 不會主動叫。候選：接進 routine quality gate，或讓 UNARMED > 0 進 dashboard-alerts。這條不補，今天的修補就只是把盲點換了個位置
- [ ] pending（給哲宇）— **OBSERVER-QUEUE #30（PR #1365 趙健志）技術面已全綠**，hard=0、兩條 CI pass。原本條目寫的「只有一個 hard」已更新。現在純粹是人物門檻與來源獨立性的決定，四個選項與推薦 default (c) 不變。投稿者從 8/15 等到現在，第五天
- [ ] pending（給哲宇，原樣延續）— OBSERVER-QUEUE #29 德文併案 59 檔（#1325 + #1430），已請 tboydar 暫停投入
- [ ] pending（給哲宇，原樣延續）— #1441 太平聲景的參選人姓名要不要放回去；#28 第三人指控信；#31 選單用語與 UI 語言閘門（#1440）；#1264 seo-meta 多語言門檻；#1184 justfont 網域白名單
- [ ] pending（給哲宇，原樣延續）— REFLEXES #86-91 六條新編號尚未經第二個獨立 session 驗證使用
- [x] ~~pending — LESSONS `reopened-channel-still-needs-someone-to-walk-down-it` 修補候選 (b) 升 §1b 明文~~ retired by 本 session
- [x] ~~pending — LESSONS `diagnosing-from-the-contributor-tree-audits-a-past-self` 修補候選 (b) 升 Stage 2 診斷 SOP~~ retired by 本 session

🧬

---

_v1.0 | 2026-08-19 08:55 +0800_
_session twmd-maintainer-am_
