# 2026-09-23-084836-twmd-maintainer-am — 三篇投稿譯文收下；一條死連結家族追到母稿的裸檔名寫法，修完順手把 09-07 留下的未解項量完

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity + broken-link audit）
> Session span: 08:30 fire → 08:35:31 第一個 merge → 08:37 致謝 → 09:1x 兩個 heal commit → 收官 +0800（3 merge + 2 heal + 2 LESSONS + 1 memory）
> 資料來源：`git log %ai` + `gh pr view --json mergedAt` + `gh api actions/runs`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，黃燈自 2026-07-05，最大缺口 review_coverage=19，少 20.25 分）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Stage 1 量 `main...origin/main` 得 `4 0`，本機純領先四個 babel commit，**沒有分岔**。3 個 ready PR（aminzai 第六天連續三篇，0 draft，未達 High-stake ≥5 門檻，Review mode 成立）、5 個 open issue（今天 0 新）、Discussions 最新 #1757 已於 09-20 由維護者逐條回過、`pr-ci-armed` 三個 PR 都 ARMED 三條 check 全過、main 四條 workflow 最新一次全綠。babel dispatcher 六個 writer 正在主工作樹寫（ACTOR_BUSY），全程沒動 destructive git（DNA #35）。

## 三篇投稿譯文（#1765 de／#1766 hi／#1767 id）

三篇都是單檔新增、CLEAN、無紅旗。先 `--add-assignee @me` 認領，再照 Stage 2 診斷紀律把 PR 內容檔帶進 main 樹跑（不 checkout PR 分支）：`article-health --profile=ci-deploy` 三篇 hard=0，結構對賬逐項對得上母稿（公園 11 段 4 連結／颱風假 12 段 20 腳註 29 連結／陳幸妤 9 段 10 腳註 17 連結，全部一比一，沒有摘要式壓縮），`target-language-check` 0 fail，陳幸妤另跑 `person-fidelity-check` 乾淨（政治家族條目是人名填空型幻覺的高風險格，per ar/ru 出生那條教訓），`sourceCommitSha` 三篇都對到母稿現在的 HEAD。frontmatter 的 `author` 逐一對過母稿，是忠實繼承不是紅旗 #7 偽造。

三篇 `gh pr merge --merge` 落地（`4d9346a7e`／`8622aec15`／`b1aa44d1a`），致謝照 burst 規則整批一則留在 #1765，另兩篇留指標。

`cjk-residue-check` 對 de 那篇報 2 行裸 CJK，查過是〈Referenzen〉裡 Vocus 與台北ナビ 的原始來源標題，書目標題照慣例不翻，屬合法豁免；留言裡主動跟投稿者講清楚，免得他下次看到檢查器報紅以為自己弄錯。

## 死連結：比例綠燈底下的一個十二語家族

`verify_internal_links.py` gated 0.34% < 7%，照閘門是過的。但照 09-07 那條教訓（比例閘門看不見家族），讀了按路徑前綴分組那張表，`music/hsien-ching-chen` 在**十二個語言各出現五次**，合計 60 條。

追上游：母稿 `Music/陳嫺靜.md` 的延伸閱讀寫成 `[台灣流行音樂](台灣流行音樂.md)` 這種裸檔名，瀏覽器拿文章自己的網址當基準解析，結果是 `/music/陳嫺靜/台灣流行音樂.md`，一律 404；譯文忠實地把連結結構一起翻過去，所以一篇母稿的五條在十二語變成 60 條。跟 09-21 data-refresh 交來的 `../Category/` 是同一個病的另一個形狀。

量根因類別而不是症狀位置：全庫母稿掃出三種相對連結，**裸檔名 22 條／9 篇**、`../Category/` 7 條／6 篇、第三類 220 條看起來最大，實跑驗是我自己的 regex 假陽性（`[label](<https://…(…)…>)` 這種角括號包住、網址裡本來就有括號的外部連結，regex 在第一個 `)` 就斷了）。真正要修的是第一類。第二類是指向 repo 內部研究報告的連結（`../../reports/research/…`），公開頁面不該引內部文件，跟 09-21 葉廷皓那條同類，但它需要逐句判斷怎麼改寫，本班沒碰，留交接。

22 條全部改成 `/category/slug`，九篇 `article-health --profile=ci-deploy` hard=0，commit `7255b3ab1`（scope 驗過 9 檔，dispatcher 正在旁邊寫，沒有互相掃到）。譯文不在這個 commit：母稿 source sha 變了，babel 會依既有流程自己追。

## 擋在路上的那個 prettier 陷阱，順便把 09-07 的未解項量完

九篇裡的口罩國家隊 commit 不進去。根因是 2026-09-07 那條教訓的同一個家族：整行圖說包在 `_..._` 裡、而圖片來源網址帶底線，pre-commit 的 prettier 把斜體重新解析、順手把網址裡的底線改成星號，一 commit 就弄壞三條 Wikimedia 連結。那條教訓當時明寫「**尚未量出全庫有幾篇這樣，不知道是偶發還是一個家族**」——本班量完了：**全庫母稿三篇**（口罩國家隊／台中捷運／林安泰古厝），八處，全部當班修掉（`7255b3ab1` + `d9ef16d5e`）。

修法是把「圖片來源／原始圖片與授權說明」那段移出斜體，圖說本文仍是斜體；同篇其他圖說一起改，免得一篇之內兩種樣子。**先試過用角括號包網址，沒有用**：林安泰古厝同一條網址，在清單行帶角括號沒事、在斜體行同樣帶角括號照樣被改——會出事的是斜體這層容器，不是網址缺跳脫。

量它的時候尺錯了兩次，兩次都靜默：

- 第一把尺比對網址**集合**，回 0 命中。原因是同一條網址在腳註也有一份、那份不在斜體裡不會被改，集合因此不變，而圖說那一份已經壞了。0 命中沒當成答案（REFLEXES #99），拿已知會壞的那篇跑正控制才發現是尺瞎了；改成比對每條網址的**出現次數**才看得見。
- 第二把尺是候選網（斜體內含帶底線網址），撈出 139 篇／343 處，看起來是個大家族；用 prettier 逐篇實跑驗完，真正會壞的只有 3 篇。**候選網不是量測結果**。

同一篇還有一對躺在檔尾 `[^21]` 後面、HEAD 裡就有的無意義反引號，prettier 因此把那條腳註折成縮排續行，`footnote-format` 判不合格，一併刪掉。

## 兩把尺的事：pipeline 指名的 profile 不是閘門那一把

九個檔在 `--profile=ci-deploy` 全部 hard=0，照 `MAINTAINER-PIPELINE` §Step 3.5 與 Top-5 那條「`--profile=ci-deploy` 必帶」走完，commit 仍被擋——pre-commit 跑的是 `--profile=pre-commit`，檢查集合不同，口罩國家隊在那把尺是 hard=1。那條規則沒寫錯，只是不完整：它防的是「漏跑 ci-deploy」，沒防「只跑 ci-deploy」。進 LESSONS `prescribed-profile-is-not-the-gate-profile`。

## 五則 open issue 的判斷

今天 0 則新 issue。四則舊的逐一核過阻塞還在不在，並且**驗了它們宣稱的東西有沒有真的落進會動手的那一層**（per `held-fact-never-crosses` vc=5）：

- **#1678**（生態多樣性，09-05）— 09-06 已實質回覆並 ship 過一條連結修補；剩下的是母稿骨架重寫，屬 REWRITE 不屬 maintainer heal。查過 `ARTICLE-INBOX` 第 445 行那條 entry 真的在，`P1` `pending`，研究（陳貞志 25 倍數字、四個來源）全部預先寫好，接手的人不用重查。**留開有據，不是沉默不修。**
- **#1609**（郭淑姿日記，08-27）— 三輪回覆（08-28／08-31／09-14）把查證範圍從「兩冊」收到「第二冊優先」，卡在數位影像須到館調閱。查過 `data/terminology/無語.yaml` 不只有散文誠信標註，還有結構化 `pending_verification` 欄位，而 `TERMINOLOGY-TRENDS-PIPELINE` Stage 1.5 REVISIT + 兩條 hard gate 真的在讀它（`terminology-pending-verification.py`）。**對讀者的承諾有落到會動手的那一層**，不是只寫在 GitHub 留言裡。
- **#1729**（馬英九腳註）— 仍等 Write mode FACTCHECK Full；#615 是 umbrella。
- **#1761**（登入過期）— 看門狗開的，assignee 是哲宇，動作只有他能做。**登入日 08-28，預估 09-26～27 過期，距今四天**，收官提醒一次。

四則最新留言都是維護者且無新 follow-up，Step 2.4 SKIP，不補罐頭回覆。

## 收官時的分岔：本班自己造的，本班併掉

Stage 1 量到的是 `4 0` 純領先，而收官 push 被拒，重量是 `9 6` —— **真分岔，而且是這一班自己造的**：origin 那六個是今早三篇投稿的 commit 加上我在 GitHub 上按的三個 merge，本機那九個是 babel 六個批次加上我自己的三個。PR 在 GitHub 上 merge、本機同時繼續 commit，兩邊就各自往前走了。

照 §Step 1.1b 當班修，不留交接。先量 base 起的檔案交集是 **0**，再量 origin 要進來的三個檔跟工作樹髒檔的交集也是 **0**，確認無衝突面之後用 merge 不用 rebase（babel 六個 writer 正在寫，rebase 會改寫我自己那三個 commit 的 sha，per DNA #35 不在 sub-agent 跑期間做會改寫歷史的 git 操作）。`1d0615369` 併入，push 過，`0 0`。接著補 `sync-translations-json.py` 讓翻譯登記表收下那三篇（`b37f5d068`）。

這條值得記一筆：**分岔不一定來自別台機器**，「在 GitHub 上收 PR」跟「在本機 commit」是兩個寫入點，同一班同時用就會分岔。代價很小（交集 0、一次 merge），因為它只活了十幾分鐘——這正是 Step 1.1b「每班 Stage 1 看到就修，分岔不會活過一天」那句話的反面驗證。

## 收官 checklist

| 檢查項                                           | 狀態                                                                                                                   |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee         | ✅ 5 則都有 label；#1761 有 assignee，其餘為留開待他層                                                                 |
| open PRs ≤ 5d age 都有 review comment            | ✅ 3 則全 merge 並留言（burst 規則整批一則）                                                                           |
| broken-link gated ratio < 7%                     | ✅ 0.34%（all-langs 0.31%）；家族表另追出一個十二語家族                                                                |
| build green                                      | ✅ main 四條 workflow 最新一次全 success                                                                               |
| BECOME ACK 一行記憶體頂                          | ✅                                                                                                                     |
| 連續空場 ≥ 3 cycle 有 LESSONS entry              | ✅ 不適用——本輪 3 個 fresh PR，**空場 vc 歸零**                                                                        |
| 有 fresh issue 的 cycle 至少一件被修掉或寫明原因 | ✅ 今天 0 則 fresh issue；四則舊 issue 逐一寫明阻塞層                                                                  |
| 本機與 origin 無真分岔                           | ⚠️→✅ Stage 1 是 `4 0` 純領先；收官時因本班自己兩個寫入點變成 `9 6` 真分岔，當班 merge 併掉（`1d0615369`），最終 `0 0` |

## Handoff 三態

繼承 `2026-09-23-070943-twmd-feedback-triage`：

- ⏳ blocked（延續）— issue [#1729](https://github.com/frank890417/taiwan-md/issues/1729) 馬英九腳註 2/2 對不上（已擴散 12 語），仍 open，等 Write session 帶哲宇 review 的 FACTCHECK Full mode。本班核過狀態未變。
- [x] ~~pending（給 08:30 maintainer-am，資訊）— `from-feedback` 仍 open 兩則 #1678／#1609~~ — **本班核完並驗了兩者的登記層**（ARTICLE-INBOX entry 真在、`pending_verification` 欄位真被 pipeline 讀），兩則都是有據留開，不需要再每天原樣往下傳。狀態有變（有人動手或哲宇拍板）時再進交接。
- [ ] pending（延續，1-file 候選，給 distill）— LESSONS `held-fact-never-crosses-into-the-layer-that-acts-on-it` vc=5，候選機械化「出口完整性檢查」仍未做。
- [ ] pending（指定席位 09-27 `twmd-self-evolve-weekly`）— `routine-sync.py` 對賬前 `git fetch`。
- [ ] pending（延續）— build perf 143 ms/page、`monitor-404.py` unknown 46.2% 剩探路檔名。

本 session 新 handoff：

- [ ] pending（**儀器候選，給 self-evolve／任何能改 article-health 的班**）— prettier 改壞斜體內網址這件事，本班是靠手跑 prettier 比對才發現的，庫裡沒有任何一道尺在看它。候選：`article-health` 加一個 plugin（或併進 `link-url-mangle`），對檔案跑一次 prettier 比對**每條網址的出現次數**，差異即 hard。確定性、便宜、每次 commit 都在，比靠人記得「斜體裡不要放帶底線的網址」可靠（MANIFESTO §14）。LESSONS `italic-span-defeats-url-escaping` 修補候選 (a)。
- [ ] pending（**未量，同條 (c)**）— 上述只掃了母稿。譯文層是否也帶同形圖說、babel 重翻時會不會被 prettier 改壞，本班沒查。
- [ ] pending（**1-file，給任何一班**）— 六篇母稿的正文仍有 7 條指向 repo 內部研究報告的連結（`Art/數位荒原`、`Art/笠詩社` ×2、`People/林良`、`People/王福瑞`、`Society/台灣災難志工文化`、`Technology/台灣BIM與營建科技`）。公開頁面不該引內部文件，09-21 葉廷皓那條是先例。需要逐句判斷怎麼改寫（不是刪連結了事，句子會少一塊），所以本班沒動。
- [ ] pending（給 maintainer／routine-sync）— `MAINTAINER-PIPELINE` §Step 3.5 與 Top-5 的「`--profile=ci-deploy` 必帶」要補成「兩把都跑，或直接 `--staged --profile=pre-commit`」。LESSONS `prescribed-profile-is-not-the-gate-profile` 修補候選 (a)。
- ⏳ blocked（給哲宇，**四天內**）— [#1761](https://github.com/frank890417/taiwan-md/issues/1761) mouhouse 登入 08-28 起算，預估 09-26～27 過期。08-23 那次過期讓十三條 routine 準時 fire、`lastRunAt` 照樣更新、實際四天零產出，而任何拿 `lastRunAt` 當依據的檢查都看到一台準時上工的機器。只有哲宇能重新登入。
