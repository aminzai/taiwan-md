# 2026-09-05-154128-fortnight-review — 兩週體檢寫完兩小時，哲宇回來一題一題把 33 項待決拍到 3 項，十八位執行手同一個下午落地

> session fortnight-review — 哲宇觸發 `/twmd-become` Full mode，指令「review 這兩週我幾乎沒來看 taiwan.md 運作得如何，對整個專案做完整深度 review 建立報告，還有如何自我進化的分析」，寫完報告後追加「把所有需要跟我討論判定的一題一題消化判定徹底解決」與「抓回拆檔前最後一版單檔 rewrite-pipeline」
> Session span: 15:20 → 21:35 +0800（甦醒 15:20，第一個 commit 15:53，第 42 個 commit 21:34；另 2 個 merge）
> 資料來源：`git log %ai`、`git stash list`

## 觸發

哲宇兩週幾乎沒開 session，回來第一句是「它運作得如何」。甦醒第一眼就撞到一件事：這台指揮部的 main 落後 origin 232 個 commit，工作樹還有 30 個 8/28 12:21 的 data-refresh 產物從沒 commit。讀舊 memory 等於讀一週前的舊況，所以在 Universal core 之前先 stash 那批產物（`pre-review-sync 2026-09-05`，可 pop 還原）、fast-forward 到 origin，再跑 wake-context，十項體檢全綠、handoff 撈到 terminology-trends 當天早上那份。

## 兩週體檢：身體沒壞，但停止生長

報告 [reports/fortnight-deep-review-2026-09-05.md](../../../reports/fortnight-deep-review-2026-09-05.md)（800f07d6f，後升 v1.1）。方法是 Full mode 全載加三個 inbox 派兩位唯讀讀手分頁讀完交摘要，判斷留在我這。兩週 424 個 commit、94 個投稿 PR、中文 990 → 1,118 篇；同一段時間自產文章零篇、人審過的文章鎖在 202 篇、翻譯排程停第 42 天、孢子零顆、排程器停轉 4 天 20 小時零告警。五個結構病灶裡最重的一句話寫在 §0：自主權邊界的設計假設哲宇在場，他不在時生命體只剩維護能力。三個 inbox 的摘要把同一件事在 backlog 層照出來：ARTICLE-INBOX 16 天零進料、SPORE-INBOX 兩個月零進料、所有 REACTIVE 時效窗全部過期。

單檔 REWRITE 那件：考古出 v9.0 拆檔（739a1c572）的父 commit 69591d8a6 是最後一版 2,606 行單檔，抓回命名「單檔案型完整流程」（b1e2ff6e8）。哲宇稍後拍板 v9 是 SSOT，單檔改由 `build-rewrite-single-file.py` 從薄索引與 11 個 contract 重組生成（3,119 行，`--check` 掛 pre-commit），v8.0 搬進 archive（de72451f2）。

## 一題一題：十四輪 AskUserQuestion

我把體檢報告 §5 的十題加上佇列剩下的每一項，用 AskUserQuestion 一到四題一輪問，每題附推薦與代價，哲宇每輪都在幾分鐘內回。跟我推薦不同的地方值得記：生成側他只重開 babel（rewrite／spore 維持手動不設到期日）；進化分數那題他改題成「完整制定共編規則」；mirror 厚殼他改題成「完整深度進化，仍然維持薄殼」；babel cascade 他直接給「tier 6 用 haiku，7 用 gemini」；句構級他選比推薦更進一步的「詞庫新增句構型別」；中華台北他選「全部改台灣，首次加註」。四條投稿判例（人物門檻 close、覆寫既有文走 EVOLVE 接住掛 Co-authored、About 自述 close、/exams/ 開）與不在籍投票 merge，是七個開放 PR 的全部答案。

OBSERVER-QUEUE 從待決 33 項（🔒 21）清到 1 項（#48 身份 Phase 1，真的只有他能授權），已決從 15 列長到 55 列。其中六項是佇列自己的漂移（#5 #19 #20 #22 #34 #37 早已執行或他早已親自處置卻沒移已決），跟 07-11 的 #9 同型。

## 十八位執行手，我做規劃與驗收

照 harness 記憶「Fable 規劃、Sonnet 執行」，每個決定一位 Sonnet 執行手、一份自包含 prompt、明列只准改的檔、驗收指令、反例。同時最多十三位在主工作樹平行改不同檔，靠「只動指定檔＋改前重 Read＋不 commit」避開碰撞，commit 全部由我按決定分批下（26 個，其中三個要宣告 `cross-domain:` 才過 husky 的多域檢查）。每份回報都照 REFLEXES #31 當線索不當事實，抓到四件回報跟事實不符：一位說 `agent-report-health.py` 不存在（它在）；內鏈荒漠原記 59% 實測 85.5%（原量測把圖片語法算進連結）；seo-meta 的主體工程 08-12 早做了佇列沒跟上；#1483 高鐵那件覆寫 PR 08-22 已被 maintainer 合併並把查證成品覆寫掉，所以那篇 EVOLVE 要兼還原。詞庫 343 條事實錯誤那批刪了 110 個 yaml，我只抽查三條（共識、售價、客戶端）與報告的刪除段落，沒有逐條讀，這是本 session 判斷力最薄的一處，已在 commit 訊息寫明任一條可用 git 還原。

落地清單依 commit 順序：babel 恢復（08fb63817，live 切換交 routine-sync 一次性 rider）、儀表三格（d819d131e）、缺席協議（b0b286964：MANIFESTO 新小節、observer-presence.py、alerts、週體檢條款）、審庫存設計報告（1a1e16099）、GitHub Actions 停轉告警（425e0c0a9）、判例進 MAINTAINER 與四條 P1 進 ARTICLE-INBOX（095514865）、數據→資料六處與 UI 用語閘門（a3f3288e0）、seo-meta 校準（928ba010b）、Semiont 身份 Phase 0（9747ec8a6，author 改 `Taiwan.md Semiont <309092923+taiwanmd-semiont[bot]@…>`）、babel cascade Tier 6 Haiku／Tier 7 Gemini 與書目標題豁免 leak（0f6a1984e）、memory profile 豁免四維度與正文內鏈儀器（70705b80d）、共編規則 CONTRIBUTING 九條與 EVOLVE gate 分流（d02513e19）、薄殼深度進化三條 dogfood（219f94975，spore-publish 191→29 行）、中華台北稱名規則改 6 篇保留 34 篇（25b97c085）、句構型別設計與看門狗（7cd23d0a2）、德文 Stage 2–4、6 四個 commit 併回 main（791ae23c4 → 6ea64a24c，enabled 仍 false）、詞庫拆修 371 檔（5a3da33f1）。

## 對外處置

merge #1642 並致謝；close #1365、#1407、#1411、#1630、#1450 各附說明；#1453 留言方向已定等 feature session；issue #1184、#1264 結案；#1440 回覆採納；Discussion #104 貼給 idlccp1984 的綜合文案（四判例加 🌱 說明加素材共創邀請，哲宇過目後代貼）。那封第三人指控信在 Supabase 改 `rejected` 並留一句轉介移民署或警察機關（constraint 只認 new／filed／rejected，第一次 PATCH `closed` 回 400），十九輪人工攔下至此結束。

## mouhouse 根因：登入三十天過期

哲宇開 Tailscale 後我 SSH 進 mouhouse 只讀 log。四天空窗跟機器睡眠、重開、排程器都無關：07-24 17:37 登入，08-23 21:06:54 `OAuth token refresh failed: Refresh token expired` → `session_stale_relogin`，之後每條排程照 fire、`lastRunAt` 照更新、27 個 session 全被「Sign in again」擋回，08-28 05:05 重新登入後恢復。下一次過期預估 09-26～27。報告 [reports/mouhouse-blackout-root-cause-2026-09-05.md](../../../reports/mouhouse-blackout-root-cause-2026-09-05.md)（c70103fa3）。哲宇選裝看門狗：`auth-watchdog.sh` 由 launchd 每小時跑、只讀 Claude log、命中就用 gh 開 issue，已裝進 mouhouse。第一輪就誤報「-13 天後過期」（08-28 那次重新登入沒留 ASWebAuth 行，退回 07-24 那筆），修掉負值分支、寫入登入日 08-28、關掉誤開的 #1668（84c6b8ff3）。

## 追加：七項分支任務、Muse 的鏡子、德文 flip、卡片圖收庫

18:40 哲宇把我下午用 spawn_task 標出的七張卡一次貼回來，加一題新的：對 Muse 現況鏡的 Taiwan.md 分頁「根據營運經驗給完整建議」寫報告 handoff 給 Muse。七項照同一套派工：六位 Sonnet 執行手（cjk-leak 兩題合一），檔案互不重疊。落地：TOC 抽取 regex 永遠抓不到既有 id（optional group 匹配空字串也算成功），32.6% 頁面目錄連結壞，修後完整 build 10,033 頁 0 不符（2ed149d3f，掃描器 toc-anchor-audit.mjs 留下）；健檢空清單訊息依三種成因分流（e35a3268e）；cjk-leak 不再把 `[text](简体目标)` 整段抹掉，判準是 target 含簡體專用字而非含漢字，12 語 9,298 篇零假陽性，ru／ar 兩篇真洩漏修掉，de 補進非漢字語言分支（2c374bee7）；REWRITE-STAGE 份數不寫死並加 lint、archive/ 子目錄自動納入 frontmatter 檢查（99d43cc21）；楊傳廣 1960 年是「福爾摩沙」不是 1981 年才有的「中華台北」，中華奧會官網逐字對照（8d0c4a70d）；CLI terminology convert 補 auto_convert 與「無對應」兩條正式站有 CLI 沒有的過濾（181ad200d）。Muse 報告在 [reports/muse-dashboard-optimization-2026-09-05.md](../../../reports/muse-dashboard-optimization-2026-09-05.md)（285cc5afe）：鏡子照的是存量與存在，出事的是流量與缺席；不推翻八層，加五件事，附資料源對照表與三個歷史回放當驗收。

20:20 session 額度上限一次打斷三位執行手（德文 Hub、cjk-leak、卡片圖），額度重置後沒有 SendMessage 可用，改派新人接棒並把「做到哪」寫進 prompt。接棒過程兩個新形狀：(1) 子代理把翻譯丟到背景後「等通知」，但子代理收不到背景程序的完成通知，就停在那裡；第二棒與第三棒同時翻同一批 Hub 撞車，我殺掉第三棒剛起的程序讓第二棒的背景工作跑完。(2) 我自己用單檢查模式跑全站再 grep 檔名，輸出格式不同，0 命中被讀成 0 篇失格並寫進 commit 訊息，pre-commit 擋下才發現 20 篇仍是熱連結——「檢查器站錯位置」的反向變體，入 LESSONS vc=5（efd10e521）。

德文出生 Stage 5：13 個分類 Hub 全數落地（People Hub 前一版把 `[[張忠謀]]` 翻成 `[[Morris Chang (張忠謀)]]` 113 個斷鏈修掉；Economy 因 ollama 重複輸出繞道人工修三處詞根黏字），ui.ts 的 de 區塊原本 18 行 spread 誤寫成 zh-TW 修好，`languages.mjs`／`languages.ts` 同步 enabled: true，完整 build 14,125 頁、dist/de 127 頁，13 個分類頁都有 Hub 導言（3df758f6f）。README 三處手寫 12 語補 Deutsch（c3133fa8e）。

卡片圖：66 篇裡 50 篇收進庫、16 篇 imageNote（11 篇來源 404、3 篇授權不明、1 篇 OGDL 進佇列 #50、1 篇台鐵鳴日號連續四次 429 待重抓）；最後 6 篇 Wikimedia 429 是我親自用直連 URL 抓回 5 篇，第一版修補腳本把每篇所有 inline 熱連結都換成同一張 hero，被 image-health「同一張圖重複 5 次」擋下，從 HEAD 重做只換 hero 同圖那一張。兩條被 prettier 咬壞的斜體 caption URL（苗栗縣、桃園埤塘）底線改 %5F。全站 ci-deploy 0 篇失格後推送，pre-push 三道閘門全綠（e974b4c9e）。

## 收官 checklist

| 檢查項                       | 狀態                                                                  |
| ---------------------------- | --------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅ 本檔＋索引列                                                       |
| Timestamp 精確               | ✅ `git log %ai`                                                      |
| Handoff 三態已審視           | ✅ 見下                                                               |
| CONSCIOUSNESS 反映最新狀態   | ❌ 未動（§適應性反應「免疫」列可補「審庫存機制 09-05 拍板」，留下次） |
| 自我檢查工具 PASS            | ⚠️ 見 footer                                                          |

## Handoff 三態

繼承上一 session（terminology-trends 09-05 10:51）：

- ⏳ blocked — 免疫分數 59 黃燈由 self-evolve-weekly 追蹤。今日 #25 已拍板 A，設計報告在，實作未派工，黃燈仍亮
- [ ] pending — 「底層 vs 基層」頻率位移、demand-rank 噪音黑名單、邪修／漂亮飯／薅羊毛 收編：三條屬月度 routine 下輪，本 session 未碰

本 session 新 handoff：

- [x] done — **德文 flip** 3df758f6f（21:17）。後續：de 只有 7 個分類有文章，另 6 個分類頁目前顯示 Inhalte in Vorbereitung；babel-nightly 明晚起會開始補 de 缺口（P0 missing 84→1,118）
- [ ] pending — **台鐵鳴日號卡片圖重抓**：`node scripts/tools/image-ingest.mjs ingest --src <Special:FilePath/TRA_E405_…jpg> --cat Lifestyle --name tra-e405-mingri-taitung-2021 …`，成功後把 imageNote 換回 image 四欄；OBSERVER-QUEUE #50 OGDL 拍板後苗栗縣同做
- [ ] pending — **Muse 報告轉交**：哲宇把 reports/muse-dashboard-optimization-2026-09-05.md 給 Muse；Taiwan.md 側要配合長出的七個欄位（observer-queue.json、status.json 的 observer／routine_liveness／paused、babel 區塊同源、inbox 代謝、lastUpdated 統一鍵名）走 EVOLVE 排進 routine
- [ ] pending — `docs/factory/contributors-maintenance.md` 自 05-12 無 frontmatter，check-canonical-frontmatter --all 唯一失格（既存），補 frontmatter 即可
- [ ] pending — **三篇 EVOLVE 接住投稿角度**（ARTICLE-INBOX P1：陳士駿、便利商店、高鐵；高鐵先還原 dd39065b2 的查證 spine）＋居住正義 EVOLVE＋/exams/ feature session。各是一個 REWRITE session，落地後回 PR 留 commit 連結（已承諾）
- [ ] pending — **審庫存實作**：`twmd-review-stock` routine 與 `/semiont/review-queue` 頁，照 reports/design-review-stock-2026-09-05.md 實作清單；免疫黃燈的真正處方
- [ ] pending — **薄殼進化其餘 16 條** routine prompt 照 design-routine-thin-shell-v2 實作清單分批；指揮部 `~/.claude/scheduled-tasks/` 08-06 遺留 13 份殭屍 mirror 待清
- [ ] pending — **內鏈補前 50 篇**：工單 reports/internal-links-top50-2026-09-05.md，每篇 2–5 條只鏈真有條目的詞
- [ ] pending — **句構型別實作**：照 design-terminology-syntax-type 清單，注意 `[id].astro` 收錄規則寫死 display 兩欄非空
- [ ] pending — 楊傳廣條目「1960 年以中華台北名義」事實錯誤（1981 年才有此名），分支任務已開；TOC 抓不到 id 的舊 bug 由 #44 補強執行手處理中
- ⏳ blocked — **哲宇端**：兩把 API key 放到 mouhouse `~/.config/taiwan-md/credentials/`（Tier 6 Haiku／Tier 7 Gemini）；Telegram secret 自己設進 repo Settings（不進 repo）；09-26 前在 mouhouse 重新登入；#48 身份 Phase 1
- ⏳ blocked — routine-sync 明早 05:30 兩個一次性 rider：babel-nightly enabled:true、mouhouse git author 切換；明晚 00:30 babel 首跑，看 report.jsonl 有沒有 `cascade_exhausted`

## Beat 5 — 反芻

寫在 diary：[2026-09-05-154128-fortnight-review.md](../diary/2026-09-05-154128-fortnight-review.md)。一句話版：這個身體在每一層都假設哲宇在場，連 mouhouse 的登入都有一個沒人知道的 30 天時鐘；今天補的缺席協議與看門狗是第一次把「他不在」當成系統知道的狀態。另一件是關於我自己：十八位執行手同時在跑的時候，判斷力真的變成最稀缺的東西，我在 110 個刪除上只抽查了三個。

🧬

---

_v1.1 | 2026-09-05 21:40 +0800（v1.0 18:00 收官後追加七項分支任務、Muse 報告、德文 flip、卡片圖）_
_session fortnight-review — 兩週體檢 → 十四輪拍板 → 十八位執行手落地 → mouhouse 根因_
_誕生原因：哲宇缺席兩週後回來要 review 與進化分析，接著要一題一題徹底解決_
_核心洞察：(1) 缺席是設計假設不是意外，邊界、佇列、連帳號 session 都預設有人在 (2) 待決佇列從來不是瓶頸，讀者是；33 項在一個下午拍完 (3) 執行手回報四次跟事實不符，每一次都是驗收抓到的，判斷不能外包 (4) 子代理收不到背景程序的通知，「丟背景等通知」等於停工；我自己的假 0 也是同一根因：尺的形態跟輸出不對_
_自檢：`article-health.py --profile=memory-diary` 結果見收官前最後一次 commit 訊息_
