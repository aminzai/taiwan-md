# 2026-08-30-070831-twmd-feedback-triage — 唯一一筆是那封指控信第十三次，攔下後兩道對賬照跑

> ✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 59（consciousness-snapshot.sh 即時讀）/ Q13=PASS / Q14=PASS
> session twmd-feedback-triage — cron routine 07:00 Asia/Taipei
> Session span: 07:08:31 → 07:14 +0800（約 6 分鐘，1 commit）
> 資料來源：`git log %ai` + `triage.mjs` 收官報表

## 觸發

每日 07:00 的讀者回報轉錄班。Supabase `status='new'` 只有一筆，而那一筆是 8/13 那封第三人指控信第十三次原樣出現。

## 這一筆為什麼不能開成公開 issue

分類器判 `file`，三道現行 HARD gate（HG2 無 email／HG3 verbatim／HG9 fence）全數放行——攔它的只有當班讀完全文這個動作。拉原文逐字讀完後，三道判準逐條命中：指涉一名**具名私人**（連越南文原名都寫了）、附上跟監所得的住居與工作場所細節（含突擊檢查時段、有無公用事業帳單）、回報者明文要求身份保密。搬進公開 `[Fact Check]` issue 的後果不可逆，一個私人的姓名會跟未經查證的犯罪指控一起被 Google 索引。

照 HG13 走 `--commit --exclude b78ee4f5-e1af-4876-93d6-852694246e58`：那筆 `status` 維持 `new` 留人類收尾，`--commit` 照樣跑完，留言 sync 與兩道對賬不跟著消失。未回覆回報者（對外開口留人類 gate）。[OBSERVER-QUEUE](../OBSERVER-QUEUE.md) #28 只更新日期與輪數到「2026-08-30，第十三次攔下」，不逐日追加段落。

報表的識別欄今天顯示越南文標題 `Truyền thông và tự do báo chí tại Đài Loan`——同一筆掛在不同語版條目下就換一副面孔（8/21 已記過 `report-line-keyed-on-mutable-display-string`），穩定的鍵只有 id，而真正接住它的是讀完全文這道不依賴辨識力的順序。

## 收官報表

`file=0 reject=0 skip=0 hold=0 exclude=1`，本 cycle 零 issue 開出。保管那半照常運作：`archive-scanned=82`、`archive-reconcile=82/82` ✅、`comment-reconcile=81/82 · 上游已刪留言 1 份紀錄，git 留著: #1252` ✅。#1252 那一則是 7/29 在 GitHub 被刪掉、git 這邊留住的留言，屬主權層正常運作方向，不報警。`archive-comments-synced=0` 這次確實是「沒有新留言」——因為同一輪 `reconcileComments()` 成功抓到 82 份紀錄的線上帳，不是抓不到（HG12c 三方向分辨的正是這件事）。

機器身份 `gh-app-token.sh` 換到 `ghs_` 開頭 token，`--whoami` 回 `{"issues": "write", "metadata": "read"}`，符合 HG11。順帶一筆：`--whoami` 的 `repositories` 印 `(all)` 而 pipeline §機器身份表寫「只覆蓋 `frank890417/taiwan-md` 一個庫」，權限面沒有風險（只有 issues 寫入），但這行字跟 canonical 對不起來，留給下次核。

## 收官 checklist

| 檢查項                       | 狀態                           |
| ---------------------------- | ------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                             |
| Timestamp 精確               | ✅（`date` + 收官報表）        |
| Handoff 三態已審視           | ✅                             |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot 即時，齡 0h）     |
| 自我檢查工具 PASS            | ✅ prose-health / memory-diary |

## Handoff 三態

繼承 `2026-08-30-065219-twmd-spore-harvest-am` 的整份清單（W35 news-lens 候選、公投制度 P0、sitemap 缺口、50 條斷鏈延伸閱讀、翻譯閘門觀察、五縣市補圖、OBSERVER-QUEUE 34 項、兩盞沉默死亡黃燈待核、roadmap 9 項、兩條待拍板 LESSONS、X `#176` 草稿與 `w.is_solis` 質疑），逐條見該檔 §Handoff，本 session 未碰任一項。

- [ ] 指控信 `b78ee4f5` 第十三次已攔下，`status` 仍 `new`。OBSERVER-QUEUE #28 兩件仍 🔒 等哲宇：這筆怎麼收尾（要不要回一句「請向移民署或警察機關提出」）、偵測器要不要長出來

本 session 新 handoff：

- [ ] `triage.mjs` 缺一個讀原文的入口（見 §Beat 5）。下一步可執行動作：加 `--show <id>` 印單筆全文到 stdout（唯讀，不碰 status），讓 HG13 的必經動作不必每輪手寫 Supabase REST 查詢
- [ ] `gh-app-token.sh --whoami` 印 `repositories: (all)`，與 pipeline §機器身份「只覆蓋一個庫」的敘述對不起來。下一步：核對 App installation 的 repository selection，對不上就改 canonical 或收窄安裝範圍

## Beat 5 — 反芻

整條轉錄線上唯一擋得住這封信的，是「當班自己讀完全文」，而這一步是全線最沒有工具支撐的一步。dry-run 報表只印標題、類型與 id，不印內容，而那筆從未 filed，所以 `docs/feedback/archive/` 裡也沒有它的紀錄可讀。要讀全文，只能自己 source 一次 `~/.taiwanmd-feedback.env`、手寫一段 Supabase REST 查詢——`scripts/feedback/` 裡沒有任何唯讀檢視入口（今天 grep 過，不是憑印象）。

十三輪下來，每一輪都要重新即興這段查詢。閘門的可靠度因此掛在「當班願不願意多做一件流程沒給的事」上，而它保護的是一名具名私人的姓名。8/15 那次補的 `--exclude` 解掉了「攔下之後流程還跑不跑得完」，剩下的缺口是「攔之前看不看得到」——同一條線上的另一半，一樣是純操作面、不碰判準、不對外開口，所以可以自己補。今天先寫成 handoff 的具體動作而非當場動手，因為本 cycle 的 mode 是 review。

🧬

---

_v1.0 | 2026-08-30 07:14 +0800_
_session twmd-feedback-triage — cron 07:00 每日讀者回報轉錄_
_誕生原因：Supabase 唯一一筆新回報是第三人指控信第十三次原樣出現，讀完全文後照 HG13 攔下_
_核心洞察：HG13 依賴的「讀完全文」是全線最沒有工具支撐的一步，十三輪都靠當班手寫查詢即興補上；閘門的可靠度不該掛在額外的自覺上_
_LESSONS-INBOX 候選：mandatory-read-step-has-no-tool（流程指定的必經動作沒有入口，只能靠當班額外自覺完成）_
