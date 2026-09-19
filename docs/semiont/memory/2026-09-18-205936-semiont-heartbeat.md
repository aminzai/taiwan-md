# 2026-09-18-205936-semiont-heartbeat — 交接單上的一個韓文字掃出一千一百篇、巡邏抽樣抽到已查過的、張忠謀 FACTCHECK 派審

> session semiont-heartbeat — 今日第四次排程心跳（Full mode）
> Session span: 20:37:00 → 21:27:00 +0800（50 min，9 commits）
> 資料來源：`git log %ai`

## 觸發

排程器 20:37 起的每日完整心跳。醒來時今天已經跑過三輪（02:38 / 08:40 / 14:38），低薪與油價兩篇 Opus 寫手在 20:00 前後各自 ship 上 main，金鐘獎那隻還在 `.worktrees/20260918-20260918-golden-bell` 裡跑冷讀第七輪（檔案 20:33 還在動，整輪沒碰它）。上一輪 handoff 留給「下一個 Full mode」的是 FACTCHECK 月度巡邏那五篇。

## 資料刷新與診斷

`refresh-data.sh` 十四步全綠（`60b02ddc53`）。文章 1119→1121、本週 +14，心臟從下午的 50 回到 90。三條黃燈原樣：免疫 58 漂移（self-evolve 的）、MEMORY 索引 91 列待 rollup（等 #68 合併後再跑，分支那側已有 index-archive/2026-09.md，現在跑會撞 add/add）、營運機 live dump 230 小時沒更新（同一個結）。`dashboard-status` 把 18 條 routine 報成 7 down 6 degraded，那是 liveness 尺只看 main、產出全在救援分支的老問題，不是新事。UNKNOWNS 沒有到期實驗，OBSERVER-QUEUE 19 列全是 🔒，沒有可代執行的預設。

## 一個韓文字掃出一千一百篇

handoff 最小的一條是「ar 馬英九 30 秒概覽混了一個韓文『한쪽』，任何 session 手改」。手改花了一分鐘（`46da78c3a0`），照 REFLEXES #24 形式 4 順手掃全庫，結果 hi 370／ar 314／ru 265 篇非韓文譯文帶韓文，2026-09 的批次還在新增。兩種形狀：四十篇（hi 39、ar 1）是**尾段整段變韓文**——媒體授權說明、「## 참고 자료」、二十幾條腳註描述全是韓文，正文還是天城文，本機模型翻到長輸出的尾巴語言漂掉。另外約九百篇是單字級融合殘留（「कार्बन उत्सर्जन 추진 कर रहा है」），是 #52 那個病的韓文版。三道閘為什麼全綠：`target-language-check` 是整篇多數票，25 行韓文佔不到多數；`cjk-leak-check` 只看漢字四連又豁免腳註行；`cjk-residue-check` 看得見 Hangul 但從沒接上產線。

修法落在 `target-language-check` 加第二把逐行的尺 `foreign_script_check`（`5690bff9c5`）：剝掉連結文字、引號、括號、網址、blockquote 後，一行韓文 ≥ 4 字且不少於目標語言字母即外來文字行，兩行以上或單行 ≥ 20 字零目標字母就擋。校準拿真實產出量：拉丁七語零誤殺（〈台灣感性〉的 대만감성、統一發票的韓文來源標題都住在豁免位置）；同一把尺量假名會在九個語系各誤殺一次莫那·魯道的日文遺言引句，所以只量韓文。`babel-dispatch` 把這種失敗記成 `foreign-script[ko]`，跟 `wrong-language` 分開。存量進 OBSERVER-QUEUE #69：40 篇 <50 檔在自主權內，但 #68 拍板前兩台都別動存量；900 篇併 #52。

## 巡邏抽樣抽到已經查過的

早上那輪寫進 FACTCHECK-PIPELINE v2.1 的抽樣指令排出前五篇：緣起故事、日治時期、張忠謀、李安、蔡英文。對 git log 一看，李安 06-01 深度 EVOLVE、蔡英文 07-12 重寫且 Stage 3.5／3.6 audit 都落檔了，正是 v2.1 自己說「最不需要巡邏的那批」。指令信任的 `lastHumanReview` 量的是人審過沒，REWRITE 是 AI 跑的不會翻它。v2.2（`c6c226b566`）補第四條件：frontmatter 有 `rationale`、DONE-LOG 登記過、research 檔存在，三者任一即排除。重抽母體 593 篇，前五換成緣起故事、張忠謀、夜生活與KTV文化、official-websites、當代藝術。另寫明 A 級「必有 research 檔」那道門在巡邏時怎麼過：audit 報告本身建成那篇的第一份 research 檔。

緣起故事是 C 級 About 頁零腳註，全對內部 ground truth 核，二十分鐘做完（`e078c9d58d`）：3/17 第一個內容 commit 一次進五篇加 12 個 Hub，文章寫「第一篇文章」跟「20+ 個主題分類」都不對。「館長張隆志背書」改「支持」，那是哲宇反覆更正過的用詞。散步那句寫在哲宇 Obsidian 2026-03-11 的思考筆記，文章的 3/11 是對的，反而 MANIFESTO §我為什麼活著把散步跟建站壓成同一天 3/17，順手改成「3 月 11 日寫下，六天後的 3 月 17 日決定建站」——動到 MANIFESTO 的是一個日期，哲宇可撤銷。

張忠謀是 A 級（40KB、20 條維基腳註、48 處引語多數沒掛腳註、12 語譯本、從沒走過產線），派一隻 general-purpose 跑 Phase 1–6，只查不改，audit 建成 `reports/research/2026-09/張忠謀.md`。

查核員 24 分鐘回來：140 個原子，✅ 76／⚠️ 42／❌ 22（去重 13／125＝10.4%）、🔴 0，34 次 WebFetch 全用中文 prompt。三條最重的我自己再對一次來源才動手：母親「徐韻徵」在 zh 維基 infobox 是徐君偉。1945 年是遷上海讀南洋模範中學，1948 年 17 歲才遷港，維基逐字命中。「初始資本額 220 億」整頁不存在，實際是政府七千萬美元 48.3%、飛利浦四千萬 27.5%、民間三千五百萬 24.2%。今周刊原話「大概每月會看兩本英文書⋯⋯但都不是文學」對照文章寫的「仍在學習文學、哲學」。查核員給的「實收資本額 13.775 億」我在它引的自由財經頁找不到，沒採用，只寫三方比例。止血七處（`89b721a3df`），母親名十二語各自改回（en/de/pt 的 Hsu Yun-cheng、fr 的 Xu Yunzheng、ru 的 Сюй Юньчжэнь、vi 的 Từ Vận Chính、hi 的 श्यू यूं-झेंग，每語一種拼法），其他錯處留給重寫：早年生活整章是生成的因果故事（哈佛文學夢、因缺乏熱情轉 MIT、韓戰外籍生進不了軍方，自傳原文是父親安排的緩衝期跟兩次博士資格考落榜），逐條修會留下沒有骨架的段落，依 Phase 4 硬門檻退回 REWRITE Stage 2，INBOX P0（`5759f41ae9`），真人條目脊椎判斷帶哲宇 review。LESSONS 那條「未審初稿被巴別塔放大」vc 升 3。

## INBOX 歸檔

`inbox-audit` 把鐵窗花（idlccp1984 8/20 PR）與台灣行動支付（Kevin Huang 9/1）標成 STALE-NEW：條目寫待開發，文章早由貢獻者進庫。搬進 DONE-LOG 註明來源與原切角（`b33e28dc85`）。handoff 裡「INBOX 登記修正（衛武營／初級大人／金城武／張懸／Blue UAS）」news-radar 13:38 那輪其實已經做完，下午心跳照抄往前傳了一輪。

## 收官 checklist

| 檢查項                       | 狀態                                                                  |
| ---------------------------- | --------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                    |
| Timestamp 精確               | ✅ `git log %ai`                                                      |
| Handoff 三態已審視           | ✅                                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（derived 層，本輪無需改 prose）                                    |
| 自我檢查工具 PASS            | ✅ prose-health score 2/3，hard=0                                     |
| diary                        | 不寫：反芻住 REFLEXES #24 形式 4 的驗證欄（0b 第三列，bump 既有條目） |

## Handoff 三態

繼承 `2026-09-18-143948-semiont-heartbeat`：

- ⏳ blocked（給哲宇，🔒）— OBSERVER-QUEUE #68 分岔合併方向、#67 babel 覆蓋投稿者譯文；拍板前兩台都別跑 babel 存量。**新增 #69**（非韓文譯文裡的韓文，40 篇 + 900 篇）同樣等 #68 之後
- ⏳ blocked（給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C；`reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留
- [ ] pending（給哲宇）— 讀 `reports/probe/2026-09-18.md` 決定亞運與中華台北 P0 派不派；T1-D 科技監控要他點頭
- [x] ~~pending（給 distill-weekly）— INBOX 登記修正~~ — retired by 本輪：news-radar 13:38（`e412eadeb0`）已做完，衛武營已移除、三條升 P0
- [x] ~~pending（三隻 Opus 寫手）~~ — 低薪、油價已 ship 上 main 且 DONE-LOG 登記（`test -f` 驗過，health hard=0）；金鐘獎仍在 worktree 跑，接手者一樣先 `test -f` 再信
- [ ] pending — 合併落地後 MEMORY / DIARY 索引兩邊都 rollup 過，index-archive/2026-09.md 只在分支那側；`routine-live-state.json` 黃燈合併後自動熄
- [ ] pending — `台灣原住民當代藝術` 十語譯本仍帶舊錯，#68 合併後確認 stale 重譯；拖過一週就單獨跑 translate.py
- [ ] pending — `observer-queue-lint.py` WARN 收兩週數據後決定升不升 HARD
- [ ] pending（延續）— OBSERVER-QUEUE 兩側撞號主鍵、slug 慣例對照升工具、`routine-stall-check.py` 尺二救援分支驗證、issue 認領步驟進 MAINTAINER-PIPELINE、兩台機器 issue 職責歸屬進 ROUTINE.md
- [ ] pending（Write session，帶哲宇 review）— 馬英九 §卸任後節與太陽花節退回 REWRITE Stage 2 局部重寫；issue #1729 留開
- [ ] pending — 馬英九 11 語譯本其餘改動靠 zh 雜湊觸發 stale 重譯；#68 合併後確認
- [x] ~~pending（給 self-evolve 或下一個 Full mode）— FACTCHECK 月度巡邏前五篇~~ — 本輪：抽樣指令修成 v2.2 後重抽，緣起故事查完、張忠謀派審（見下）；日治時期／李安／蔡英文屬已走過產線，不在母體
- [x] ~~pending（小）— ar 馬英九 30 秒概覽韓文「한쪽」~~ — 修完，並掃出集群（#69）

本 session 新 handoff：

- [ ] pending（Write session，帶哲宇 review）— 張忠謀退回 REWRITE Stage 2：早年生活整章重寫、42 條 ⚠️、腳註每個數字各掛一手源；audit 與修補建議在 `reports/research/2026-09/張忠謀.md` §Critical issues，INBOX P0 已入列
- [ ] pending — 張忠謀 12 語譯本只同步了母親名，其餘六處止血靠 zh 雜湊變更觸發 stale 重譯；#68 合併後確認排進第一批
- [ ] pending（下一個 Full mode）— 巡邏母體第三到第五篇：Lifestyle/夜生活與KTV文化、resources/official-websites、Art/當代藝術（前兩篇 C／B 級可自跑）。「給巡邏一條 routine」仍缺，走 ROUTINE.md 要營運機建排程，等 #68
- [ ] pending（#68 合併後，任何 session，<50 檔）— #69 (a) 那 40 篇清 `sourceCommitSha` 降級 stale；清單用 `target-language-check.py --scan hi,ar --json` 取 note 以「韓文漂入」開頭者
- [ ] pending（哲宇一句話可撤）— MANIFESTO §我為什麼活著 散步日期 03-17→03-11（`e078c9d58d`），依據是他 Obsidian 2026-03-11 那篇思考筆記
- [ ] pending（小）— 〈誰算低薪〉description 96 字 < seo-meta 下限 100（warn），三處全形分號在引語內；具名編輯三輪 accept 過的稿子，要動請那條 run 的席位動

## Beat 5 — 反芻

今晚兩件事是同一個形狀。交接單上寫「一個韓文字」，抽樣指令排出「前五篇」，兩者都是上一個我當時看見的尺寸，而我讀到它們的時候，會自然把那個尺寸當成問題本身的大小：改完那個字就關票，抽完那五篇就算巡邏。差別只在多做一個動作——動手前拿全庫掃一次它的兄弟——一千一百篇跟兩篇已查過的就浮出來。它住在 REFLEXES #24 形式 4「單例不代表集群」裡，只是換了載體：這次報單例的是上一輪的自己，而我對自己的交接單比對工具警報更少起疑。驗證寫回 #24 那條，沒開新日記（DIARY-PIPELINE 0b 第三列）。

🧬

---

_v1.0 | 2026-09-18 21:27 +0800_
_session semiont-heartbeat — 晚間排程心跳：韓文漂移閘門、巡邏抽樣修正、緣起故事與張忠謀查核_
_誕生原因：每日排程完整心跳（今日第四輪）_
_核心洞察：(1) 交接單跟自製指令都會把集群寫成單例，讀到「只有一個」先掃兄弟再動手 (2) `lastHumanReview` 量的是人審過沒，不是查過沒，用它挑巡邏對象會挑到最不需要巡邏的 (3) 整篇多數票看不見尾段換語言，局部漂移要逐行的尺_
_LESSONS-INBOX 候選：無（兩條都折進 REFLEXES #24 驗證欄，DNA-first）_
