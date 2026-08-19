---
session_id: '2026-08-16-084103-twmd-maintainer-am'
session_span: '08:41:03 → 09:10 +0800'
trigger: 'cron routine twmd-maintainer-daily (am 08:30)'
observer: 'none (cron)'
beat_coverage: 'Stage 1-4 (MAINTAINER-PIPELINE) + CORRECTION-PIPELINE 全 5 stage'
---

✅ BECOME ack: mode=review→**強制升 full**（High-stake #1：PR triage 24 ≥ 5）/ 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，讀數齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# 2026-08-16-084103-twmd-maintainer-am — 九個 PR 敗在同三道門檻，而指南教的是看不見那些門檻的指令，外加五月天勘誤十二語同步

> session twmd-maintainer-am — cron maintainer 巡邏
> Session span: 08:41:03 → 09:10 +0800（約 29 分鐘，4 commits）
> 資料來源：`git log %ai`

## 觸發

Cron 08:30 開跑。BECOME 判 Review mode，但 Stage 1 掃到 24 個 open PR，命中 High-stake #1（PR triage ≥ 5）強制升 Full mode 重載。昨天 feedback-triage 留了一條 handoff：issue [#1390](https://github.com/frank890417/taiwan-md/issues/1390) 五月天鼓手學歷勘誤待查核。

## 五月天勘誤 — 讀者只寫一句話，拆掉的是一整段敘事

讀者 Sybil Kwok 回報「冠佑不是師大附中的，他是國光藝校的」。跨三源查證成立（維基劉冠佑條目 + 兩輪搜尋聚合），而且錯得比回報範圍大：文章的 description 與第一個 H2 都寫「五個師大附中的高中生」，把 1999 年才入團的冠佑算進 1997 年報名野台開唱的那批人裡。

照 CORRECTION-PIPELINE 走完五階。§清單外連帶修那條抓出另外四處同族錯誤：鼓手更替只寫了錢佑達一人（實際錢佑達、陳泳錩、任柏璋都短暫待過，冠佑是第四任）、簽約段寫「五個還沒畢業的年輕人」（冠佑當時 26 歲、已是 Why Not 的鼓手）、腳註 `[^5]` 指向維基的**消歧義頁**而不是本人條目、〈文章如何誕生〉引用五月天當寫作範例時也寫了同一句。

§跨語言健檢那條收穫最大：同一句錯誤活在全部 11 個語言版本。順手撞見兩個獨立的翻譯缺陷——韓文把「附中」譯成「중학교」（國中）、越南文把台北高中生寫成「người Việt」（越南人）。十二語一起改，`33d5db012`，全部檔案 `ci-deploy` hard=0。

值得記一筆的是這條錯誤從 2026-03-23 建檔就在，站上掛了近五個月，期間走過 babel 十二語翻譯、走過各種閘門，沒有任何一支儀器叫過。抓到它的是一個讀者的一句話。

## 追上游 — 三天同一道閘門，第三天才問對問題

九個 ready PR 全部敗在 `frontmatter-gate`。這是連續第三天同型（8/13 六個、8/14 八個、8/15 二十四個），前兩天都追過上游也都修了東西，今天還是九個。

拆開失敗分布才看懂前兩天修的不是同一層：全形分號超標命中 7 篇、外部圖片熱連結 6 篇、缺 subcategory 只剩 3 篇（8/14 補 CONTRIBUTING 範本確實有效，從 8 降到 3）。真正的當家問題換人了，而**分號與圖片熱連結這兩道硬門檻在貢獻者讀得到的任何文件裡都不存在**。

更直接的是指南自己教錯：CONTRIBUTING 兩處都叫貢獻者跑 `--check=prose-health`，而那個模式**看不到**這兩道門檻。照著做會在本機拿到 `hard=0`、送上來還是被擋。這正是同一個人連續三天卡在同一個地方的機制。

修了兩層（`bcc91eeb7` / `68131f309`）。文件層：§3 品質檢查改教 `--profile=ci-deploy`、列出五道會擋 merge 的門檻與各自修法、說明 fork PR 要去 Actions Summary 看清單（token 唯讀收不到 PR 留言）。閘門層：加一條數值對賬測試，從 `article-health.config.toml` 讀 `semiont_hard_over` / `emdash_hard_over` 去比對 CONTRIBUTING 寫的數字，門檻改了而指南沒跟上就 CI 紅。**有實際驗過會紅**——把 config 暫時改成 9，測試如預期失敗，再還原。它掛在既有的 `contributor-frontmatter-template.test.mjs` 裡，跟 `pr-frontmatter-gate` 一起跑，不必另外接線。

## PR 與 issue 處置

`--fix` 對這批的實際效果量過一輪：#1368 hard 36→5、#1370 36→3、#1371 3→0，其餘落在 1~4。只有 #1371〈生活市集〉能到 hard=0，其他殘留的全是分號（要改寫散文）與圖片熱連結（要逐張判授權），兩者都不該由維護者代決。

#1371 走 §1b 的 P1 路徑而不是 P0：`maintainerCanModify` 是 true，所以把 heal 推回投稿者分支、等 CI 轉綠再 merge，**全程沒有製造紅色部署窗**。這是照昨天那條 `merge-first-collides-with-all-file-deploy-gate` 的判準做的——先問「這篇 heal 到 hard=0 要幾分鐘」，答案在同一個 push 週期內才 merge。

[PR #1365](https://github.com/frank890417/taiwan-md/pull/1365)（domo741852963-eng，〈KENJI 趙健志〉）撞到 8/14 才補進 pipeline 的 Step 1.5b：`checks=0` 而四條 run 卡在 `action_required` — 第一次投稿的 fork 貢獻者 CI 預設一條都不跑。核准後只剩一個 hard（中國用語「視頻」）。但人物門檻與來源獨立性是另一回事：投稿帳號在送 PR 前**一小時**才註冊、單一用途，約七十個腳註裡二十多個是 YouTube/FB/IG/個人站，維基條目查無。升 OBSERVER-QUEUE #30，不自行決定收或不收，但給了投稿者一個有解除條件的答案（補第三方深度報導會改變判斷）。

issue [#1389](https://github.com/frank890417/taiwan-md/issues/1389) @idlccp1984 指〈台灣豆漿與早餐店〉與〈台灣早餐文化〉該一起整理，核對屬實：三組 H2 直接對撞。兩篇體質差很多（一篇場景式敘事、一篇清單式百科腔），所以合併方向不是隨便留一篇。排進 ARTICLE-INBOX P1，沒當場動手是因為兩篇都有多語譯文，合併會產生孤兒譯文。

留言照 Step 3.7 的 burst 紀律走累積式：整批共同 pattern 一次講完放 #1376，#1371 只留簡短致謝，不逐篇轟炸。

## 收官 checklist

| 檢查項                       | 狀態                                             |
| ---------------------------- | ------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                               |
| Timestamp 精確               | ✅ 從 `git log %ai`                              |
| Handoff 三態已審視           | ✅                                               |
| CONSCIOUSNESS 反映最新狀態   | ✅ 無需更動（本 cycle 未改器官分數維度）         |
| 自我檢查工具 PASS            | ✅ 改動檔 `ci-deploy` 全 hard=0，斷鏈 0.27% < 7% |

| Quality gate（routine 6 條）           | 狀態                                     |
| -------------------------------------- | ---------------------------------------- |
| open issues 都有 status label          | ✅ 3 條全有                              |
| open PRs ≤ 5d age 都有 review comment  | ✅ 累積式一則涵蓋整批 + #1365 個別回覆   |
| broken-link ratio < THRESHOLD_PERCENT  | ✅ 0.27%（門檻 7%）                      |
| build green                            | ✅                                       |
| BECOME ACK 一行記憶體頂                | ✅ 見檔首                                |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ⏭️ 不適用（本 cycle 有真 backlog，vc=0） |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ #1390 修完 close，#1389 落檔＋回覆    |

## Handoff 三態

繼承上一 session（`2026-08-16-070922-twmd-feedback-triage`）：

- [x] ~~pending（給 `twmd-maintainer-am`）— #1390 五月天冠佑學歷勘誤待查核~~ — retired by 本 session：查證成立，十二語同步修完，issue 已 close
- [ ] pending（給哲宇）— 心臟分數與零產出的矛盾（`twmd-rewrite-daily` disabled 三週）。原樣延續
- [ ] pending（給哲宇或到期 session）— EXP-2026-07-25-alias 到期日 2026-08-24。原樣延續
- [ ] pending（給下次 evolve/rewrite session）— roadmap §六之二 三項桶 2 finding，P0 仍 0/3。原樣延續
- ⏳ blocked（給哲宇）— OBSERVER-QUEUE #29 德文決策、#28 第三人指控信。原封不動
- [ ] pending（給哲宇）— SPORE-INBOX pending 45 的三選一路線。原樣延續
- [ ] pending（給下次 review/maintainer session）— REFLEXES #86-91 尚未經第二個獨立 session 驗證使用。原樣延續
- [ ] pending（給哲宇，延續）— #1264 seo-meta 多語言門檻、#1184 justfont 白名單、免疫黃燈連續多日
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換
- [ ] pending（給哲宇，Bucket D）— #171 X 回覆 @TaiwanAny 策略疑慮
- [ ] pending（給哲宇，連續第六天）— X 端瀏覽器登入態自 8/12 起未恢復
- [ ] pending（給下次 harvest）— #170/#171 D+6（2026-08-17）續追

本 session 新 handoff：

- [ ] pending（給哲宇）— OBSERVER-QUEUE #30 人物門檻：PR #1365 單一用途新帳號投來的在世人物條目收不收。這是兩天內第二篇卡在同一條門檻的人物稿（8/15 workshop 那篇仍 open），門檻明確化之前每篇都要重判一次
- [ ] pending（給下次 maintainer）— idlccp1984 八個 ready PR 留 open，殘留 hard 全是分號與圖片熱連結。累積式修法已在 #1376 講完。若下個 cycle 他推了新 commit，先跑 `--profile=ci-deploy` 確認再處理。另有 17 個 draft 尚未轉 ready，不主動碰
- [ ] pending（給下次 rewrite session）— ARTICLE-INBOX 新增早餐雙篇整併 EVOLVE（P1），動筆前要先定合併方向並處理多語譯文孤兒問題

## Beat 5 — 反芻

今天最該記住的一句話：**第三天才問對問題**。

8/13 修「閘門的話送不出去」，8/14 修「範本沒寫 subcategory」，兩次都是真的根因，也都真的有效——subcategory 從八篇降到三篇。但兩次都停在「這批 PR 為什麼失敗」，沒問「**下一批會為什麼失敗**」。於是今天分號跟圖片熱連結接手當家，而它們在文件裡從來就不存在，跟 subcategory 當初的狀況一模一樣，只是還沒輪到它們現形。

`doc-and-validator-drift-has-no-reconciler` 那條 LESSONS（8/14 寫的，vc=1）說對了病，但它的候選處置只寫了 frontmatter 那一半的對賬。散文與媒體那半沒人守，因為前一天現形的是 frontmatter——**修補範圍被症狀現形的位置決定，不是被根因的類別決定**。這句話本身就寫在 `pr-frontmatter-gate.yml` 的註解裡（8/08 修 husky 沒帶到 CI 那次），我今天讀過它，然後又踩了一次同型。

所以今天補的對賬刻意做寬，驗的是「config 裡的門檻值有沒有出現在 CONTRIBUTING 裡」這整層，而非單獨盯住分號那一條。下次有人新增第三道 prose 硬門檻而忘了寫文件，這條會叫。它擋不住「新增門檻卻連 config key 都沒進對賬清單」那層，但至少往上游挪了一格。

另一件事：五月天那條錯誤掛了近五個月，走過十二語翻譯與各種形式閘門，沒有一支儀器叫過，最後是讀者一句話拆掉的。這跟今天上半場是同一個形狀——**形式閘門查得出格式，查不出「這句話說的是不是真的」**，而後者目前唯一可靠的來源仍然是共生圈外圍那些真的在讀的人。

🧬

---

_v1.0 | 2026-08-16 09:10 +0800_
_session twmd-maintainer-am — cron 巡邏：勘誤 + 追上游 + PR triage_
_誕生原因：cron 08:30 fire，接住昨天 feedback-triage 留的 #1390 勘誤 handoff，並撞上連續第三天的同閘門批次失敗_
_核心洞察：修補範圍被症狀現形的位置決定，而不是被根因的類別決定——連續三天各修一層真根因，仍每天長出新的同型失敗，因為每次都只問「這批為什麼敗」沒問「下一批會為什麼敗」_
_LESSONS-INBOX 候選：`fix-scope-follows-symptom-not-root-class`（vc 候選，跟既有 `doc-and-validator-drift-has-no-reconciler` 同族但更上游）_
