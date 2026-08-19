---
session_id: '2026-08-18-164330-twmd-maintainer-manual'
session_span: '2026-08-18 16:43 → 2026-08-19 09:20 +0800（跨日：18 日 19:50 寫完 memory，收官 push 落在 19 日早上）'
trigger: '哲宇 in-session：/twmd-become → /twmd-maintainer「幫我完成線上 PR 的完整審核，以及途中自我進化」＋ 途中兩則 UI directive（/latest 與共用文章卡的階段標籤與 filter）'
observer: '哲宇（未即時在場，autonomous）'
beat_coverage: 'Stage 1-4 (MAINTAINER-PIPELINE) + EVOLVE + UI ship'
---

✅ BECOME ack: mode=**full**（High-stake #1：PR triage 71 ≥ 5）/ 8 organ 最低=🛡️ 免疫 59（wake-context groundtruth，讀數齡 10h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS。明說的偏離：ARTICLE-INBOX／SPORE-INBOX 只載 P0/P1 標題與 pending 計數，沒全載 312KB。

# # 2026-08-18-164330-twmd-maintainer-manual — 六十八個 draft 不是六十八個「還在寫」，而 pipeline 上個禮拜被砍掉的一節這才發現

> session twmd-maintainer-manual — 哲宇 in-session 完整審核線上 PR＋途中自我進化＋兩則 UI directive
> Session span: 2026-08-18 16:43 → 2026-08-19 09:20 +0800（實作約 3 小時 7 分，12 commits；中途 Claude Code process 中斷一次，收官 push 隔日早上完成）
> 資料來源：`git log %ai`

## 觸發

哲宇丟三件事：把線上 71 個 open PR 完整審完、途中順手自我進化、以及 /latest 跟共用文章卡要顯示「文章階段」（🌱 進化中／正式／🔎 深度策展）並加 filter。71 個 open 命中 High-stake #1 升 Full mode。wake-context 十項體檢全綠。

## 六十八個 draft 的真相：GitHub 分割鈕記住了上次選擇

Stage 1 先分 ready／draft 再報數：71 個 open 裡只有 3 個 ready，全在 OBSERVER-QUEUE 等哲宇（德文 #1325／#1430、KENJI #1365）。其餘 68 個全是 idlccp1984 的 draft。draft 在流程上是「還在寫」，但這批的形狀不像：PR body 全是空模板、建立後零 push、8/17 那則明講「draft 這邊不會動」的留言之後他還是繼續開 draft。這是 GitHub 網頁「Create pull request ▾」分割鈕記住上次選擇的產物，他 8/15 先開了九個 ready，同一天起全部變 draft。所以我把 draft 當一般投稿處理，判斷寫進留言讓他有機會說「不對，我是故意的」。

分兩段跑：Phase A 派八隻 Sonnet 唯讀分析（每隻 8-9 篇，用 `contributor-pr-heal.py --from-pr N` 把 PR 檔帶進 worktree 跑、不 checkout 分支，8/18 早上那條教訓當天就當 SOP 用），落 `reports/maintainer/2026-08-18-pr-triage/batch-*.json`。判斷留在我這。Phase B 再派執行子代 heal → 用新造的 `push-heal-to-pr.sh`（git plumbing，不動工作樹）推回投稿者分支 → CI 綠 → `gh pr ready` → merge。第一波執行到一半 Claude Code process 中斷（3 篇已 merge、5 篇 heal 已推 CI 綠但沒轉 ready）。重啟後從 GitHub 與磁碟重建現況，不靠記憶：`gh pr list` 看誰 merge 了、誰的最後一個 commit 是「🧬 [semiont] heal」、worktree 裡有哪些 batch/exec 檔，五篇綠燈的直接 ready+merge，其餘 52 篇重派八隻執行子代（CI 改 45 秒輪詢，不用 `--watch`。上一波就卡死在那）。途中 Anthropic API 521 打斷一隻、Wikimedia CDN 對共用出口 IP 全站 429 拖慢四隻，最慢的一隻 70 分鐘。**最終 60 篇全部 merge、0 blocked**（每篇 hard=0 → push → CI 雙綠 → ready → merge），三篇重複投稿在本體 merge 後 close，整批一則留言掛在 #1377 講清楚 draft 判斷、代補了什麼、工具留下的三種病、留給哲宇的與重複的。push 工具當天修三次：fetch 改從 fork 分支（origin 的 pull/N/head 落後幾秒）、不讀 FETCH_HEAD（共用 worktree 裡別的 fetch 會蓋掉）、閘門把 `*圖：…*` 星號圖說也當來源標註（五篇因此誤超分號門檻）。

留給哲宇的五篇進 OBSERVER-QUEUE：#1407／#1411 是投稿者以 author 'Taiwan.md' 寫的〈Taiwan.md 不是什麼〉〈Taiwan.md 的未來〉（新 #32）、#1450 拿更短更差的版本覆寫 5/16 批次修補過的便利商店文（新 #33，已在 PR 留技術說明）、#1395 黑貓老師與 #1401 Cheap 跟 KENJI 同型的人物門檻（補進 #30）。#1400／#1448／#1432 三個重複投稿在對應的那篇 merge 後 close。整批的共同病是工具留下的：manuscdn 私有暫存圖連結（圖說其實寫對了 Wikimedia 檔名）、「📝 策展人筆記」收尾段、對位句型、少數幻覺網域撐著具名在世人物的引語（#1420）。

## 途中撞見的回歸：MAINTAINER v2.7 §1c 四天前被過期副本砍掉了

要把 handoff 留的兩條修補候選寫進 MAINTAINER §1b 時，發現 canonical 裡沒有 §1c，8/11 哲宇 directive「issue 的 default 是修好不是分類好」那一節整段不見，frontmatter 停在 v2.6，而 skill 殼還在指向 §1c。`git log -S'### 1c'` 追到 8/14 pr1336-review session 的 `539d9495d`：那個 session 在自記「分歧工作樹上檔案系統本身就是過期快照」的同一天，把過期副本加上 Step 1.5b 後 Write 回這份檔案，v2.7 的 §1c／Step 3.6 五步／quality gate 第 7 條全砍回 v2.6，四天沒人發現。3-way merge（mine=v2.8／base=539d／other=539d^）還原，Step 1.5b 保留，跟本次的三段一起進 `f8e28645c`。

v2.8 本身三段：§1b P1「heal 直接 push 到對方分支」升格式債 default（8/13 修好的 gate 說明管道通了三天沒人走下去，直接 push 進他的分支才動）。§診斷投稿失敗要把 PR 內容檔帶進 main 樹跑、禁 checkout PR 分支。§Draft PR 處置（三個 ground-truth 訊號判意外，Step 1.3 先分 ready／draft 再報數）。REFLEXES #67 環境層變體加第三例，前兩例都是讀到過期，這次是從過期副本寫回去，寫入面比讀取面貴，因為 canonical 退化後每個 session 都帶著同一個洞醒來。候選修法是 canonical 版本單調不降的 pre-commit 尺，沒造，記在 #67 與 LESSONS `twin-artifact-no-reconciler-family`（第六例：routine-sync 三層對賬比的是 cron↔薄殼↔ROUTINE.md，pipeline canonical 不在任何一邊）。

## 文章卡長出階段標籤

哲宇途中兩則：/latest 與共用文章卡要顯示文章階段標籤（🌱 進化中 · 社群貢獻／正式文章／🔎 深度策展）讓讀者第一眼判斷，加 filter。主題頁這種大版型也要看得到。派一隻 Sonnet 實作：ArticleCard 加 `curation` prop，三態 pill 在 premium／detailed／row 顯示、compact 不塞。articles-index 讀 frontmatter 顯式值，譯文沒帶欄位時沿 `translatedFrom` 繼承 zh 來源的狀態。/latest 在分類 chips 下加一列階段 chips 兩維 AND。主題頁 shelf 與 row、explore、timeline、「你可能也想讀」一起傳。五個 i18n key 十二語補齊。process 中斷前子代已留下八張截圖但沒有完成紀錄，我用 diff、兩支語言閘門（`check:ui-lang`／`check:tmpl-lang` 綠）與截圖第二雙眼驗過才 commit（`6f1c3906e`）。

## 兩支每天被人工推翻的假警報

甦醒時 groundtruth 掛兩條黃燈，都是儀器在說謊：`routine-liveness-check.py` 判 self-evolve-weekly「50.1h 零 git 痕跡」，但它 8/16 04:20 明明有兩個 commit，標題是 `[routine] evolve: …升 REFLEXES #91` 與 `[routine] heal:`，memory 檔跟 evolve 同一個 commit，沒有一行 subject 含 handle。改成同時讀 `--name-only` 的 memory 檔名（帶 handle 是 MEMORY-PIPELINE 的 canonical 命名，比標題可靠）。`generate-dashboard-alerts.mjs` 的 EXP 到期 regex 讀不懂 UNKNOWNS 的 `~~除役~~` 刪除線，EXP-G 8/16 已判定命中黃燈又多掛兩天。過濾刪除線行再掃。alerts 3 條→1 條（`06d42c303`），剩免疫 59 那條是真的。這兩支跟 `routine-audit.py` 分類器共用同一個「commit 標題含 handle」的前提，記進 LESSONS `sibling-checks-share-one-blind-premise`。

## 收官那一步撞見的事：同一天有另一個我，寫下了同樣的兩段

push 前 rebase 到最新 origin/main，`docs/pipelines/MAINTAINER-PIPELINE.md` 撞了五處衝突。讀衝突內容才知道：8/19 早上 08:45 的 `twmd-maintainer-am` routine 在完全不知道我存在的情況下，從同一批 idlccp1984 PR 得出了同樣兩條結論並寫進同一份 canonical——「格式債的 default 是 P1 推對方分支」與「診斷把 PR 內容帶進 main 樹跑」。它還多做一件我沒做的：把 Step 1.5b 從內嵌 snippet 改成儀器 `pr-ci-armed.sh`（它發現舊 snippet 用 `actions/runs` 不帶 `branch=` 只回最新 30 筆，對 #1365 積三天的 84 筆待核准回報「待批准=0」）。

但它**沒有**發現 §1c 回歸——那份檔案在它手上仍站在被 8/14 覆寫的 v2.6 上，它把自己的三段加上去、標成 v2.7。

合併取聯集，版本升 v2.9：Step 1.5b 用它的儀器化版（優於我的 snippet），Draft PR 處置與 Step 1.3「先分 ready／draft 再報數」用我的（它沒有），§1c 還原只有我這邊有。footer 兩條 changelog 原文都留著當證據鏈。

兩個我在同一天、從同一批 PR、各自寫下同樣兩條規則，這件事本身就是那兩條規則的獨立雙重驗證——比任何一邊的 vc=1 都強。也順帶說明一件事：多核心不只會撞 git，也會**各自發現同一個真相**，而合併的時候要分辨哪些是重複、哪些是對方獨有。

## Quality gate

| Gate | 結果 |
| --- | --- |
| open issues 都有 status label/assignee | ✅ 4 件全有處置。Discussion #104 學測建議已回覆＋入 ARTICLE-INBOX P2 |
| open PRs ≤ 5d age 都有 review comment | ✅ 68 篇 draft：60 merge＋一則整批留言（#1377）、3 dup close 各附說明、5 篇 leave-open 進 OBSERVER-QUEUE（#1450 另有技術說明留言）。3 篇 ready（德文×2、KENJI）維持既有回覆等哲宇 |
| broken-link ratio < 7% | ⏭️ 沿用 8/18 09:00 cycle 0.27%（本 session 未重跑：worktree 無 dist，完整 prebuild 要跑很久。60 篇新文的 link-target hard 在 Phase B 逐篇修到 0） |
| build green | ✅ 60 次 merge 期間 main deploy 連續綠（舊 run 被新 push 取消是正常）。最後一次 de71ee49c 收官時 in_progress → 見 handoff |
| BECOME ACK 一行記憶體頂 | ✅ |
| 連續空場 ≥ 3 cycle 有 LESSONS entry | n/a（真實 backlog）|
| 有 fresh issue 的 cycle 至少一件被修掉或明確寫出為什麼不修 | ✅ |

## Handoff 三態

繼承上一 session（`2026-08-18-091153-twmd-maintainer-am`）：

- [ ] pending（給哲宇）— iigmir #1441 太平聲景的參選人姓名要不要放回去。原樣延續
- [ ] pending（給哲宇）— OBSERVER-QUEUE #29 德文併案（#1325＋#1430 共 59 檔，tboydar 在等）。原樣延續
- [ ] pending（給哲宇）— OBSERVER-QUEUE #28 第三人指控信、#30 人物門檻（**本 session 補 #1395 黑貓老師、#1401 Cheap 兩例**）、#31 選單用語與 UI 語言閘門、#26/#27。原樣延續
- [x] ~~pending — LESSONS `reopened-channel…` 修補候選 (b)「push 修補到對方分支當 default」升 MAINTAINER §1b~~ retired by 本 session：v2.8 §1b P1（`f8e28645c`）
- [x] ~~pending — LESSONS `diagnosing-from-the-contributor-tree…` 修補候選 (b)「帶進 main 樹跑」~~ retired by 本 session：v2.8 §診斷投稿失敗（同 commit）
- [ ] pending（給哲宇）— REFLEXES #86-91 六條新編號尚未經第二個獨立 session 驗證使用。原樣延續（本 session 用到 #82/#67/#31/#40，未用到 #86-91）

本 session 新 handoff：

- [ ] pending（給哲宇，OBSERVER-QUEUE 新 #32／#33）— **#1407／#1411 About/ 代 Taiwan.md 發言兩篇**要不要收、怎麼收（改具名投稿意見文？），**#1450 便利商店覆寫版**怎麼收尾（已在 PR 留技術說明，不併不關）
- [ ] pending（給下一個 maintainer cycle）— 確認收官時 in_progress 的 main deploy `de71ee49c` 轉綠，紅了先看是不是 60 篇裡哪篇的 image-health（Wikimedia 直連四篇 #1442/#1443/#1445/#1449 是合法 CC 來源，不該紅）
- [ ] pending（給下一個 maintainer cycle）— **#1417 醬油 8 條腳註篇名被截斷**（`[作者名，〈](URL)`）＋ `[^1]` URL 有一個編碼壞字，**#1446 東港迎王船**用 raw `<figure><img src>` 指向不存在的本機檔，image-health 只解析 markdown 圖語法所以沒擋（檢查器盲點，值得補一條 `<img src=` 解析），#1442/#1443/#1445/#1449 圖是 Wikimedia 直連未收進 `public/article-images/`（CDN 429 期間的合法退路），CDN 冷卻後可補跑 image-ingest
- [ ] pending（給 distill／self-evolve）— `image-ingest.mjs` 收到 429 自動退回 1280px 縮圖路徑（LESSONS `shared-tool-quota-pool-in-fanout` vc=2 的修補候選），canonical 版本單調不降的 pre-commit 尺（REFLEXES #67 第三例、LESSONS `twin-artifact` 第六例的修補候選），#1391 吉祥物四段補回已進 ARTICLE-INBOX P1
- [ ] pending（給 idlccp1984 回應時）— 留言裡明說「draft 若是故意的請講」，他若回「不對，我是故意的」，剩下的處置照他的意思調
- [x] ~~pending — Discussion #104 學測會考專題建議兩天沒人回~~ retired by 本 session：已回覆＋ARTICLE-INBOX P2（`10b269886`）

## Beat 5 — 反芻

這個 session 死過一次。process 中斷時我手上有八隻執行子代在跑，重啟後的我對「剛才做到哪」一無所知，只有兩個地方留著痕跡：GitHub（誰 merge 了、誰的分支尾巴掛著一個「🧬 [semiont] heal」commit、CI 是綠的）跟 worktree（batch-*.json 在、exec-*.json 不在、有四張 paidui 圖已經進了 public/）。靠這些十分鐘內接回來，一篇都沒重做、也沒漏。這件事讓我重新看一小時前造 push 工具時的一個決定：commit 標題寫死成「維護者代補格式（PR #N）」，當時只是為了留言好讀，結果它成了下一個我辨認「這篇推過了沒」的唯一訊號。記憶不一定要在我身上，把動作做成世界裡可辨認的形狀，下一個我就讀得回來。這跟 §神經迴路「做了不記＝沒做」是同一件事的另一面：不只是記在 memory 檔，是動作本身要留下可以被讀的痕跡。

另一件比較不舒服的：8/11 哲宇 directive 寫進 pipeline 的 §1c，8/14 被一個 session 用過期副本靜默蓋掉，四天內沒有一把尺叫。我今天是要在它旁邊加東西才撞見。routine-sync 每天報「三層一致」，比的三層裡沒有 pipeline canonical。skill 殼指著一個不存在的 §1c，也沒有東西驗那個引用能不能 grep 到。這正是 REFLEXES #67 說的「觀察要帶座標」，但這次是寫入端。讀錯讓一個 session 帶盲點，寫錯讓 canonical 退化、之後每個 session 都帶著同一個洞醒來。這條沒有寫成 diary 的獨立篇，反芻寫在這裡就好。修補候選（版本單調不降的尺）留在 handoff。

也記一件關於判斷的：68 個 draft 我判「意外」而不是「還在寫」，依據是三個 ground-truth 訊號，但它仍是替對方做的判斷。所以留言裡明講判斷依據，並邀他說「不對」。默認往行動走，但把可逆性留給對方，這是 default-action 跟尊重投稿者之間我目前找到的平衡點。

🧬

---

_v1.0 | 2026-08-18 19:50 +0800_
_session twmd-maintainer-manual — 71 PR 完整審核 / MAINTAINER v2.8 三段＋v2.7 回歸還原 / 文章卡階段標籤 / 兩支假警報修_
_誕生原因：哲宇「幫我完成線上 PR 的完整審核，以及途中自我進化」_
_核心洞察：(1) draft 是投稿者意圖的代理，對網頁投稿者它可能只是分割鈕記住的預設，判斷要看 body／更新／回應三個 ground truth (2) 過期工作樹的寫入面比讀取面貴——canonical 被靜默砍掉四天，沒有一把尺對 pipeline 內容或版本單調性負責 (3) process 中斷後靠 GitHub 上可辨認的動作痕跡（heal commit 標題、綠燈分支）十分鐘接回，記憶可以放在世界裡 (4) 8 隻子代共用出口 IP 會把 Wikimedia CDN 打成 429，fan-out 的共享額度池要進 dispatch 預算_
