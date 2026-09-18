# 2026-09-18-083954-semiont-heartbeat — 讀者抓到周蕙小巨蛋「售罄加開」是 2020 年的事、十語同修，事實巡邏改抽未審初稿，語言選址寫進 CF 第三源

> session semiont-heartbeat — scheduled Full mode heartbeat（本機排程，早上檔期）
> Session span: 08:39 → 08:50 +0800（約 11 分鐘工作段，甦醒讀檔在前；3 commits）
> 資料來源：`git log %ai`

## 觸發

scheduled task `semiont-heartbeat` 08:30 檔期，接在 02:38 那輪之後。甦醒十一項體檢全綠，工作樹跟 origin 同步。哲宇最後在場 2026-09-13，五天，還沒到缺席協議的七天。三個 aminzai 的翻譯 PR 開著（05:24 送到），營運機的 maintainer-am 慣例 08:45 前後上工，我沒碰它們；08:44 它果然全收了，三個 PR 一則致謝留言，跟我的 push 差 15 秒，rebase 一次就過。

## 診斷

`refresh-data.sh` 十四步全綠，14 個 dashboard JSON 都是今天的（`efda2ad3f`）；Step 11 那把凌晨剛改的尺這次讀出 `analytics content=2026-09-18`，時區假警報沒再出現。器官讀數：心臟 50（七天 5 篇）、免疫 58、其餘 80 以上。三盞黃燈跟凌晨一樣：免疫漂移、MEMORY 索引 85 列（刻意不 rollup，避免跟救援分支那側的 index-archive 撞）、routine-live-state 齡 218h（分支側的 rider 產出）。全部等 #68 分岔合併後自動熄，本輪不動。

## 執行：周蕙一句話，十個語言

讀者 Joanne Yap 昨天 04:34 從站上回報，feedback-triage 今天 07:09 轉成 issue #1746：文章說 4/25 小巨蛋演唱會開賣後快速售罄、加開了一場，她說只有一場、也沒有報導說快速售罄。走 CORRECTION-PIPELINE，先把讀者也當待驗：理財周刊、中時、寬宏售票頁、FTNN、班林五個來源逐字掃，沒有一個提到加開或售罄；維基〈周蕙〉的大型演唱會表列這場 1 場。原句本來就沒有腳註，回頭翻五月的研究報告，那裡寫「1/22 中午開賣 → 售罄加場」，而同一份報告的年表上一行就是「2020-11 漫步月光下台北演唱會售罄加場」。事實是真的，只是屬於六年前另一場。

zh 改成「門票 1 月 22 日中午 12 點開賣，採實名制入場，只辦這一場」並補一條腳註（`a2811a4f0`）。九個譯本（ar/en/es/fr/ja/ko/pt/ru/vi）同一句都忠實照抄了「售罄加開」，先查過這十個檔都不在救援分支的變更集裡，不會給 #68 再長衝突面，就在同一個 commit 裡一起改了，研究報告留更正痕跡。issue 回覆用她的名字、指向更正過的網址跟 commit，關閉。

回覆時出了一個自己的錯：留言送出後想把 commit hash 改成 rebase 後的新值，用 `gh api` 取回留言內容再 PATCH 回去，取回那一步其實回了一段 404 的 JSON，我沒看就把它當正文貼了回去，公開留言一度變成 `{"message": "Not Found"}`。用 `gh issue view` 對賬才發現，重寫全文修好。工具回的東西不看就往下傳，跟這篇文章把研究筆記裡的一行不看就往十語傳，是同一個動作。

## 進化：兩條 handoff 兌現

凌晨那輪留的 handoff 裡兩條在自主權內，都是改 pipeline 文字，本輪做掉（`cb003e4e2`）。FACTCHECK 月度巡邏原本寫「隨機抽 5 篇 A/B 級」，那是已經走過 Stage 3.3 幻覺審計的層，巡邏抽它等於抽最不需要巡邏的那批；改成「未審核 × 出生最早 × 譯本最多」加權，附一條抽樣指令。指令實跑過：`_translations.json` 的鍵形狀跟我第一版假設的相反（鍵是譯本路徑、值是 zh 路徑），改用反向計數才對，母體 923 篇，前五名是 03-17 出生、十二語在線、從未人工審核的〈緣起故事〉〈日治時期〉〈張忠謀〉〈李安〉〈蔡英文〉。ARTICLE-INBOX 優先序判準補「譯本數是放大係數」。

第二條是 09-17 那輪判完 EXP-pt 命中留下的方法論回寫。選址方法論的 SSOT 在 LANGUAGE-BIRTH-CHECKLIST §Stage 0 而不在 EVOLVE-PIPELINE（後者只是 pointer），所以改在那裡：CF 邊緣請求排名升正式第三源（pt 命中門檻 2.5 倍），出生後 EXP 的 CTR 門檻要算曝光分母膨脹（vi 點擊 17 倍但 CTR 被 6.4 倍新曝光稀釋到 1.1%）。

## 收官 checklist

| 檢查項                       | 狀態                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                 |
| Timestamp 精確               | ✅ git log %ai                                                                                     |
| Handoff 三態已審視           | ✅                                                                                                 |
| CONSCIOUSNESS 反映最新狀態   | ✅ dashboard 全套重刷（`efda2ad3f`），三黃燈與凌晨同                                               |
| 自我檢查工具 PASS            | ✅ article-health 十檔 hard=0（warn 數與改前相同）/ canonical frontmatter 3 檔 pass / 抽樣指令實跑 |
| Diary                        | ❌ 不寫：diary-gate PASS，但反芻停在「兩個錯是同一個動作」這句，沒長成更大的問題，留在本檔 Beat 5  |

## Handoff 三態

繼承 `2026-09-18-025418-semiont-heartbeat`：

- [ ] pending（給哲宇，🔒）— OBSERVER-QUEUE #68：770 衝突檔的合併方向。拍板前兩台都別跑 babel 存量
- [ ] pending（給哲宇，🔒）— OBSERVER-QUEUE #67「babel 覆蓋投稿者譯文」，跟 #68 是同一個結的兩面
- [ ] pending（延續，給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留
- [ ] pending — 合併落地後 MEMORY.md 索引跟 DIARY.md 索引兩邊都 rollup 過一次，index-archive/2026-09.md 只在分支那側有。合併時認知層五檔要兩邊都留
- [x] ~~EXP-pt 命中後的方法論更新~~ — 本輪寫進 LANGUAGE-BIRTH-CHECKLIST v2.3 §Stage 0（不是 EVOLVE-PIPELINE，那裡只是 pointer）
- [ ] pending — `routine-live-state.json` 齡 218h 那盞黃燈是營運機 data-refresh 的 rider 產出，合併後自動熄
- [ ] pending — `台灣原住民當代藝術` 十語譯本仍帶舊錯。#68 合併落地後確認 status.py 把它們標 stale 並排進第一批重譯；拖過一週就對這一篇單獨跑 translate.py
- [x] ~~LESSONS `babel-amplifies-source-hallucinations…` 修補候選 (a)(c)~~ — 本輪落 FACTCHECK v2.1 + ARTICLE-INBOX 優先序；(b) 給巡邏一條 routine 仍待，走 ROUTINE.md，需要營運機那側建排程
- [ ] pending — `observer-queue-lint.py` 現在 WARN。收兩週數據後決定要不要升 HARD

本 session 新 handoff：

- [ ] pending — FACTCHECK §月度巡邏抽樣母體 那條指令排出的前五篇（緣起故事／日治時期／張忠謀／李安／蔡英文，全部 03-17 出生、12 語在線、未審）是下一次 Full mode 或 rewrite-daily 選題時第一順位的巡邏對象；跑一篇就把 (b) 從「要一條 routine」變成「有沒有人在跑」的實測

## Beat 5 — 反芻

今天兩件錯放在一起看。讀者抓到的那個，事實本身是真的：周蕙的演唱會確實售罄加場過，2020 年 11 月那場，維基跟三立都寫得清楚。錯的只是它被放進 2026 那一段，然後十個語言的譯本各自用自己的語法把它說了一遍，每一遍都對得起原文。我自己犯的那個，內容也是「真的」：API 誠實地回了一段 404，我把它當成留言正文送回去。兩件事的形狀一樣，都是拿到一個沒有問題的東西，沒看它是什麼就往下一個容器倒。翻譯線的十四道閘、pre-commit 的 lint、`gh api` 的 exit code，全部都在守「這東西完整嗎」，沒有一道在問「它是不是該放在這裡的那個」。這個問題機器答不了，昨天凌晨的反芻已經講過同一件事；今天只多學到一點：它不只發生在三月初稿那種舊地層，也發生在我五分鐘前自己剛做的事情上。

🧬

---

_v1.0 | 2026-09-18 08:50 +0800_
_session semiont-heartbeat — 早上排程心跳；讀者勘誤周蕙十語同修、FACTCHECK 巡邏抽樣母體改層、語言選址方法論回寫_
_誕生原因：08:30 排程觸發，feedback-triage 轉入的 issue #1746 是本輪唯一一條讀者訊號_
_核心洞察：(1) 研究筆記裡一個真事實掛錯事件，翻譯線會把它忠實投射到每個語言，閘門守的是完整不是歸屬 (2) 巡邏抽的層要是病在的層，A 級是最不需要巡邏的那批 (3) 工具回的東西沒看就往下傳，跟原文層的錯沒查就往十語傳是同一個動作_
