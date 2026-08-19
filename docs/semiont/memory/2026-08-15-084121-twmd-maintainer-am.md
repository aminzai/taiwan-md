---
session_id: 2026-08-15-084121-twmd-maintainer-am
session_span: 2026-08-15 08:41 – 09:15 (Asia/Taipei)
trigger: routine twmd-maintainer-daily (am 08:30)
observer: none (cron)
beat_coverage: MAINTAINER-PIPELINE Stage 1-4
---

✅ BECOME ack: mode=review→**強制 Full**（PR triage 25 ≥ 5 命中 High-stake #1）/ 8 organ 最低=🛡️免疫 59（即時 consciousness-snapshot.sh）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# twmd-maintainer-am @ 2026-08-15

## Stage 1 SCAN

| 項目             | 值                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------ |
| open PR          | 25（24 = idlccp1984 單批，1 = tboydar #1325 德文）                                         |
| open issue       | 2（#1184 justfont、#615 UI umbrella），兩則最新留言皆維護者、無新跟進                      |
| past 24hr commit | 10 條 routine fire（embeddings / routine-sync / data-refresh / harvest / feedback-triage） |
| past 48hr commit | 55 條                                                                                      |
| build status     | green（deploy 持續在跑；本 cycle 中途一次 failure 見下）                                   |
| broken-link      | gated 0.27% < 7% ✅（all-langs 0.25%）                                                     |
| 免疫器官         | 59（yellow，自 2026-07-05，未動）                                                          |

進場即命中 High-stake #1（PR triage ≥ 5）→ 強制升 Full mode，非 routine 預設的 review。

## 追上游：三天三個根因，這次走到回報的聚合層

24 個 PR 全部敗在 `frontmatter-gate`。這是連續第三天同一個投稿者、同一道閘門：
8/13 的根因是「閘門的話送不出去」（fork PR token 唯讀 → 補 Job Summary），
8/14 是「CONTRIBUTING 範本沒寫 subcategory」。兩個都已修好，PR 照樣全紅。

本 cycle 往上游再走一層，發現的不是新的內容問題，是**回報本身沒有形狀**：

閘門報出來的最大宗是「腳註格式不合規範」，16 個檔案各報 9 到 28 條，合計 **353 條**。
逐條讀每一條都像獨立問題。實際成因是產生工具在**每個 markdown 連結的網址尾巴留了一個空格**
（`](https://…?cumid )`）。CommonMark 容許它，連結照樣打得開，畫面完全正常——但腳註格式是
`[^N]: [Title](URL) — desc`，多一個空格就不匹配，於是每個受影響的腳註各自回報一次。

一個上游缺陷，被拆成三百多份寄出。沒有人會讀到第三百條，於是它被讀成「這批投稿品質很差」。

**修法（f71bdae8c）**：`link-url-mangle` 新增 HARD + 自動修——它本來就是在管「網址被某個工具
寫壞了」（原本管 prettier 把斜體 caption 的 `_` 翻成 `*`）。新規則**逐行回報一次並帶該行處數**，
不逐條洗版；`--fix` 一併清掉；角括號 `](<url with space>)` 是 CommonMark 給空白的正當出口，
明確跳過。

**校準**：對現行 12 語系全庫掃過 **零命中**——這條 HARD 只對新缺陷亮，不會把既有內容照紅
（REFLEXES #66 用真實產出校準，不憑想像設）。新增 5 條 whitespace 家族測試，既有 prettier
家族 7 條全數續綠。

## Stage 3 ACT

**merge #1346 帝雉**（+ heal `0b38889d6`）：唯一一篇能收到 `hard=0` 的。做了三件 polish——
全形分號 20 → 門檻內（17 處的後半本來就能獨立成句，拆成句號句，語意一字未改）、
補 `curation: incubating`（8/04 查證狀態分層拍板後的預設）、
以及 commit 當下才冒出來的第三件：**pre-commit 的 prettier 把兩條 Commons 圖片連結弄壞了**
（斜體圖說裡網址結尾 `_01.jpg`，底線被配對成斜體結束符 → `*01.jpg`，連結當場 404）。
這正是 `link-url-mangle` 六月為它誕生的那個 bug，這次它自己在 pre-commit 攔下、自己修好。
本地 ci-deploy 先跑是綠的，是 hook 裡的 prettier 才引入損壞——**先驗後改的順序本身會漏掉這一類**。

**close #1347**：跟 #1346 同一個檔案（`Nature/帝雉.md`），重複投稿，附說明關閉。

**其餘 22 篇留 open**，並發一則**累積式留言**（#1362，per Step 3.7 burst 紀律：同一人 48hr 內
≥3 PR 不逐篇各發一份，同一件事講 22 次對雙方都是噪音）。內容：我這邊修掉了什麼（空格，不用他管）、
剩下要他出手的兩項（subcategory 9 篇、全形分號大部分）、可複製的本地指令、
author/featured 欄位的個別修正、以及一句說明——他以前只看得到沒有理由的紅 X，是我們的管道斷掉，
不是他沒在看。

**#1325 德文**：CI 三條全綠，但 `de` 不在 `ENABLED_LANGUAGE_CODES`。已在 OBSERVER-QUEUE #29
掛哲宇拍板（新語言 = §自主權邊界大規模架構重構），本 cycle 不動，per REFLEXES #79 預設 reserve。

## 為什麼只 merge 一篇，不整批 merge

`deploy.yml` 跑的是 `article-health --all --profile=ci-deploy`（全站掃描、hard 即擋）。
所以**從 merge 落地到 heal 推上去之間，站台部署是紅的**。本 cycle 實測：#1346 於 00:58 落地
→ deploy `3008fc6d` **failure**；00:59 推 heal → `0b38889d` **success**。78 秒的紅，
如實留在 Actions 紀錄上。

另外 22 篇沒有任何一篇能靠機械修復到 hard=0：分號要改寫散文（最多 49 處），
外部圖片熱連結要逐張授權判斷（最多 12 張）。整批 merge 的紅窗口會是幾小時到幾天，
不是七十八秒。MAINTAINER §Step 3.3 決策表「> 30 min 純格式 → merge + 排 polish 進 backlog」
這一行沒有考慮全站閘門的存在——已寫進 LESSONS。

## 兩次自己的量尺說謊（同 cycle，REFLEXES #65 self-apply）

1. 我用 `grep -E "內部研究|未公開|私人通訊"` 掃虛構來源紅旗，命中 #1344 / #1350。
   逐條讀 → **兩則都是誤報**：「並未公開」「未公開的特徵」是正常散文。
2. 我用 `grep -o '；' | wc -l` 統計全庫分號，得到「930 篇中 125 篇超標」，
   差點據此升級「閘門對貢獻者內容系統性不友善」的結構性結論。實際上閘門**只算可編輯正文**
   （blockquote / 腳註 / 書名 / 圖說不計，`_uneditable_punct_predicate` SSOT），
   全庫真實超標數是 0——main deploy 一直是綠的就是證據。

兩次都是我自己臨時寫的尺，兩次都比儀器鬆或緊，兩次都差一步就把錯的東西送出去。
第二次尤其值得記：我在同一個 cycle 裡才剛寫下「我的 checker 跟我共享盲點」，然後立刻又犯一次。

## Stage 4 Quality gate

| Gate                                   | 結果                                                   |
| -------------------------------------- | ------------------------------------------------------ |
| open issues 都有 status label/assignee | ✅ 2 則皆最新留言為維護者、無新跟進 → Step 2.4 SKIP    |
| open PRs ≤ 5d age 都有 review comment  | ✅ 累積式留言涵蓋整批 24 篇 + #1347 個別說明           |
| broken-link ratio < 7%                 | ✅ 0.27%                                               |
| build green                            | ✅ 收官時 `0b38889d` success（中途 78 秒紅已如實記錄） |
| BECOME ACK 一行記憶體頂                | ✅                                                     |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | n/a — 本 cycle 25 PR，非空場                           |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ 353 處缺陷根治 + 補閘門 + merge 1 篇 + close 1 重複 |

## Handoff 三態

繼承上一 session（`2026-08-15-071908-twmd-feedback-triage`）：

- [ ] pending（給下次 maintainer）— 6 篇 fence 包住正文的譯文待修，清單在 spawned task `task_a6914e9f`。原樣延續
- [ ] pending（給下次 maintainer）— PR #1336 的 `frontmatter-gate` 紅 X 會永遠留在紀錄上（rerun 不套用新 workflow）。原樣延續
- [x] ~~pending — #1339 已給逐項修法，等 idlccp1984 推新 commit~~ retired by 本 session：改為整批累積式留言涵蓋（含 #1339），逐篇 handoff 不再需要
- [ ] pending（給哲宇）— [OBSERVER-QUEUE #29](../OBSERVER-QUEUE.md) 要不要開德文，三選項待拍板。原樣延續（#1325 CI 全綠但 `de` 不在註冊表）
- [ ] pending（給哲宇）— `cli/package.json` 已在 main 上是 0.8.1，要上 npm 需打 `cli-v0.8.1` tag。原樣延續
- [ ] pending（給下次 data-refresh-am 或 distill-weekly）— MEMORY.md 索引 inline 已 93 rows（>80 黃燈），owner 是 distill-weekly。原樣延續
- [ ] pending（給哲宇，Bucket D）— #171 X 回覆 @TaiwanAny 的策略疑慮，per §自主權邊界政治立場條款不自動回覆。原樣延續
- [ ] pending（給哲宇，連續第五天）— X 端瀏覽器登入態自 8/12 起未恢復。原樣延續
- [ ] pending（給下次 harvest）— #170/#171 D+5（2026-08-16）續追。原樣延續
- [ ] pending（給哲宇，第 3 個 cycle）— OBSERVER-QUEUE #28 第三人指控信：(a) 要不要長偵測器 (b) 要不要回覆回報者。原樣延續

本 session 新 handoff：

- [ ] pending（給下次 maintainer）— idlccp1984 22 篇 open PR 等他推新 commit。修法已在 #1362 累積式留言講完（subcategory 9 篇 + 全形分號大部分 + author/featured 個別項）。**不要逐篇再發建議**（burst 紀律）；他推上來後逐篇驗 `--profile=ci-deploy` hard=0 再 merge
- [ ] pending（給下次 maintainer）— 22 篇裡的**外部圖片熱連結**（最多 12 張／篇）需逐張授權判斷，不是機械修復。8/14 的既有做法是「只留授權清楚的那張」，可沿用
- [ ] pending（給 distill-weekly / self-evolve-weekly）— 本 cycle 兩條 LESSONS：`per-instance-reporting-buries-the-single-cause`（閘門設計判準，值得升 plugin 撰寫規範）／`merge-first-collides-with-all-file-deploy-gate`（MAINTAINER §Step 3.3 那行需要但書）
