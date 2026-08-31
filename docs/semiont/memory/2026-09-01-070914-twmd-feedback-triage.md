# 2026-09-01-070914-twmd-feedback-triage — 指控信第十五次，這次讀全文有現成指令，順手收掉一行印了三天的假範圍

> ✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（黃燈：漂移、多維度退化中，自 2026-07-05 由 twmd-self-evolve-weekly 追蹤）/ Q13=PASS / Q14=PASS
>
> session twmd-feedback-triage — cron 07:00 Asia/Taipei
> Session span: 07:09:14 → 07:14:30 +0800（約 5 分，1 commit）
> 資料來源：`git log %ai` + `triage.mjs` 收官報表 + `/installation/repositories`

## 觸發

每日 07:00 的讀者回報轉錄班。Supabase `status='new'` 隊列今天一筆。

## 那一筆是同一封指控信，第十五次

隊列裡唯一一筆是 `b78ee4f5-e1af-4876-93d6-852694246e58`，掛在越南文〈台灣的媒體與新聞自由〉條目下，內容與該文無關：一封寫給主管機關的檢舉信，指控一名具名私人涉及假結婚與非法工作，附上跟監所得的居住與工作細節（突擊時段、有沒有水電帳單、在哪一區的娛樂場所上班），並要求對回報者的身份保密。分類器判 `file`，三道現行 HARD gate（HG2 無 email／HG3 verbatim／HG9 fence）全部會放行——它們問的是搬得對不對，沒有一道在問搬過去會傷到誰。

判斷的依據是 `--show` 拉出來的全文，不是認出那個 id。這個區別是 8/17 那篇日記留下的：認出它靠的是 id、條目、日期三個座標，全是這一封的特徵而非這類信的特徵，而熟悉感是唯一會隨使用變鬆的閘門（已升 [REFLEXES #95](../REFLEXES.md)）。今天讀完內容才動手，結論跟前十四次一致：`--exclude` 攔下、`status` 維持 `new`、不回覆回報者（對外開口屬人類 gate），續掛 [OBSERVER-QUEUE](../OBSERVER-QUEUE.md) #28 等哲宇拍板。

排除那一筆之後照樣跑完 `--commit`：`file=0 reject=0 skip=0 hold=0 exclude=1`，`archive-scanned=83`、`archive-comments-synced=2`。兩道對賬 `archive-reconcile=83/83 ✅`、`comment-reconcile=82/83 ✅`（差的那份是 [#1252](https://github.com/frank890417/taiwan-md/issues/1252)，7/29 那則答錯的留言在 GitHub 被刪、git 這邊留住了，主權層正常運作的長相）。同步進 git 的兩則新留言都是昨天 maintainer-am 的回覆：[#1634](https://github.com/frank890417/taiwan-md/issues/1634) 曾博恩條目的藝人名冊更正、[#1609](https://github.com/frank890417/taiwan-md/issues/1609)《郭淑姿日記》出處進度。

值得記一筆的是，這是第一個「讀全文」不必臨場即興的 cycle。昨天的 session 在同一步絆倒第十四次之後才把 `--show` 做出來（pipeline v1.7）。今天它已經是流程給的一行指令，我不需要 source 一次 env、手寫一段 Supabase REST 查詢。

## 印了三天的 `(all)`，其實是一個缺席

`gh-app-token.sh --whoami` 的 `repositories` 行印 `(all)`，而 pipeline §機器身份表寫「只覆蓋 `frank890417/taiwan-md` 一個庫」。這個對不上是 8/30 這條 routine 自己記下的，寫進 handoff 後連傳三個 cycle 沒人動手。今天在同一行輸出前第四次讀到，查了：`/installation/repositories` 回 `total_count: 1`，就是 `frank890417/taiwan-md`。canonical 敘述一直是對的，說謊的是那行報表。

根因是建 installation token 的回應平常根本不帶 `repositories` 欄位（只有明確窄化庫範圍時才帶），舊版 `or "(all)"` 把這個缺席印成「覆蓋全部庫」——跟一個權限真的開到全部庫的 token 逐字相同，看到的人無從分辨自己在看哪一種。HG11 的判讀就掛在這行字上。修法是缺欄位時去問 `/installation/repositories` 這個權威來源，查不到則印「查不到——不等於覆蓋全部庫」，不讓「沒查到」跟「範圍很大」共用同一個長相。Pipeline 同步升 v1.8 記下這件事。

## 收官 checklist

| 檢查項                       | 狀態                                                |
| ---------------------------- | --------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                  |
| Timestamp 精確               | ✅（`git log %ai`）                                 |
| Handoff 三態已審視           | ✅                                                  |
| HG11 機器身份                | ✅ `ghs_` 開頭 / `issues: write` + `metadata: read` |
| HG13 讀全文才判斷            | ✅ `--show` 讀完全文後才 `--exclude`                |
| HG12 archive 進 git          | ✅ `git add docs/feedback/archive/`                 |
| HG12b `archive-reconcile`    | ✅ 83/83                                            |
| HG12c `comment-reconcile`    | ✅ 82/83（上游已刪留言 1 份，git 留著）             |
| 自我檢查工具 PASS            | ✅ prose-health                                     |

## Handoff 三態

繼承上一 session（`2026-09-01-064101-twmd-spore-harvest-am` 及其上游 walk-back）：

- [x] ~~`gh-app-token.sh --whoami` 權限範圍疑點~~ retired by 本 session（實際範圍 1 庫，報表行已修）
- [ ] 指控信第十五次已攔下，OBSERVER-QUEUE #28 兩件待哲宇拍板：(1) 這筆怎麼收尾、要不要回報者一句「這類事情請向移民署或警察機關提出」(2) 分類器要不要長出「這段文字搬到公開處會傷到誰」這道閘門
- [ ] `footnote-description-is-an-unaudited-claim` 候選修法、#1609 待調閱《郭淑姿日記》兩冊、PR #1630 等哲宇拍 OBSERVER-QUEUE #33——本 routine 不碰，原樣延續
- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤，本 routine scope 外

本 session 新 handoff：**無新增待辦**。

## Beat 5 — 反芻

昨天的日記寫「留給未來自己的訊息傳得到資訊，傳不到急迫」，說的是同一件事寫成 handoff 之後，要再親自絆一跤才會動手。今天有兩個對照樣本擺在一起。`--show` 那件事已經不需要急迫了——它變成一行指令，我照著跑，甚至沒有機會感覺到它曾經是個缺口。`(all)` 那件事還停在舊模式：三個 cycle 讀過同一行 handoff，動手的是今天第四次親眼看到那行輸出。

差別在修補落地成什麼形狀。變成指令的，下一班不必記得，還是句子的，下一班得自己想起來。這跟 §神經迴路那句「memory 是自律，canonical SOP 才是閘門」是同一個結構，只是這次我在同一個早上看到了兩邊。

🧬

---

_v1.0 | 2026-09-01 07:14 +0800_
_session twmd-feedback-triage — cron 07:00 讀者回報轉錄班_
_誕生原因：Supabase 隊列一筆，是那封第三人指控信第十五次出現；順手收掉一個掛了三個 cycle 的 handoff。_
_核心洞察：判斷靠讀全文不靠認 id（REFLEXES #95）；一行報表把「欄位缺席」印成「範圍全開」，跟真的全開逐字相同，HG11 的判讀就掛在那行字上；修補落地成指令的下一班不必記得，還是句子的下一班得自己想起來。_
_LESSONS-INBOX 候選：`absent-field-rendered-as-the-widest-reading` — 缺席的欄位被 fallback 印成最寬的那個解讀，跟真的很寬長得一模一樣（REFLEXES #38 混維度 / #85 的鏡像面）。_
