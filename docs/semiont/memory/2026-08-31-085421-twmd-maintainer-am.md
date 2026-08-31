# 2026-08-31-085421-twmd-maintainer-am — 讀者抓到的兩個名字錯，往上游追出腳註描述是全篇唯一沒人查過的那句主張

> session twmd-maintainer-am — cron 08:30 每日維護者巡邏（PR review + issue triage + build 健檢 + 斷鏈稽核）
> Session span: 08:21:00 → 09:05:00 +0800（約 44 分，5 commits + 3 PR merged）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 full**（ready PR 6 ≥ 5，命中 High-stake #1）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，yellow「漂移—多維度退化中」自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 08:30 例行巡邏。這輪不是空場：6 個 ready PR、5 個 open issue，其中一則是今晨 07:09 feedback-triage 剛開出來的讀者勘誤。ready PR 數過 5 觸發 BECOME §Step 0 的 High-stake 條件，mode 從 review 升 full，OBSERVER-QUEUE §待決 也因此進了載入面——那份清單直接決定了今天哪些 PR 不該由我拍板。

## 三個翻譯 PR 收下

aminzai 的 [#1631](https://github.com/frank890417/taiwan-md/pull/1631)（id 滷肉飯）、[#1632](https://github.com/frank890417/taiwan-md/pull/1632)（hi 鯨豚）、[#1633](https://github.com/frank890417/taiwan-md/pull/1633)（ja 黃土水）三件走完 B 路徑：十條紅旗零命中、`pr-ci-armed.sh` 顯示三件都 ARMED 且 checks 全綠、frontmatter 逐欄比對中文 SSOT（author / featured / date / lastVerified / image 全部是忠實 passthrough，含 `臺灣的鯨豚` 作者「海女」與 `台灣滷肉飯` 的 `featured: true` 這兩個乍看像紅旗 6/7 的欄位）。`--merge` 保留譜系，三件各留一則具體致謝。

掃 dedupe 時順帶看到一件事：昨天 merge 的 #1629 / #1628 與更早的 #1622 都是 0 comment，Step 3.7 那條「感謝必須用 `gh pr comment`」的 hard gate 有漏。我沒有回頭補發，因為對幾天前的 merge 追一則罐頭感謝是雜訊不是修補。今天這三件的留言寫得比模板具體，各自點出該篇翻譯真正難的地方（滷肉飯的南北名稱之爭、鯨豚的漢字原詞保留、黃土水標題把「失蹤七十年」放在最前）。

## 讀者說兩個喜劇演員不是薩泰爾的人，他說對了

[Issue #1634](https://github.com/frank890417/taiwan-md/issues/1634) 來自站上回報者 milesism，一句話：「龍龍和大可愛從不曾是薩泰爾藝人」。查證分三路：龍龍的經紀約在星雨國際，2021 年龍K事件終止的是那份約，她是薩泰爾找去演出的外部演員。大可愛 2025 年的個人專場〈大愛〉掛在卡米地。最關鍵的是第三路，回頭讀那句話引的來源：維基百科「薩泰爾娛樂」條目**整頁沒有「旗下藝人」這個清單**，只有團隊成員與已離職喜劇演員名單。

所以壞掉的層次比兩個名字更深一階：這句話拿了一個沒講這件事的來源，去撐一個名冊主張。`4f72f613c` 把名冊改成來源撐得住的寫法（除曾博恩外，列後來接下《夜夜秀》的簽約藝人賀瓏，其身分有 2025 解約聲明可交叉驗證，以及喬瑟夫），並修掉腳註 11 自己的描述：它原本寫該來源「含董事長 / 執行長 / 旗下藝人結構」，前三項都對，第四項是憑空的。

同一句活在中文 SSOT 加英日韓西法葡俄越八個語言的譯文裡，九檔一起改，沒有留哪個語言帶著舊版本。策展人筆記那段把龍龍列在台灣 stand-up 圈裡沒有動。那段有來源（卡米地條目列她為該場地出身的演員），而且說的是場景不是名冊，這兩件事本來就不同。

追上游的結果寫成 LESSONS `footnote-description-is-an-unaudited-claim`（`8efebc32d`）：一條腳註有兩個主張，正文那句會被查核鏈驗，腳註自己那行「某來源—含 X、Y、Z」也在宣稱來源涵蓋什麼，而整條產線沒有一步對著來源檢查它。「連結-描述錯位」這條規則其實存在，但只掛在維護者流程對**外部 PR** 的腳註審核，自產深度文走的 REWRITE Stage 2D 與 Stage 3 都只驗正文對來源。規則掛在兩條路徑裡曝光比較低的那一條上，跟 8/23 那條 `highest-exposure-slot-is-the-one-with-no-gate` 同形。

## 郭淑姿的日記，出處找到了但判定沒動

[Issue #1609](https://github.com/frank890417/taiwan-md/issues/1609) 哲宇 8/28 已親自回過，說日記原文還沒核對所以不改「無語」條目的斷代判定，並請讀者提供出處。Step 2.4 的 dedupe 規則是 skip，但這則的內容是一件**還沒做完的查證**，不是一則等回覆的訊息，所以我去做了那件事。

郭淑姿是白色恐怖受難者葉盛吉的遺孀，日記由國家人權博物館出版成《郭淑姿日記》第一冊與第二冊，這就是缺的那份出處，`b10a57b00` 寫進詞條的誠信標註。同時記下一條對讀者說法不利的線索：目前找得到最詳細的二手處理是[黃文源在風傳媒的投書](https://www.storm.mg/article/5251444)，該文反覆引述的情緒詞是「無聊」（原文作「不聊」），通篇不見「無語」。但這是線索不是結論，一篇投書掃不到不等於兩冊日記裡沒有，所以判定一個字沒動，誠信標註把兩種可能都寫著。issue 上留了進度說明，包含那條對讀者不利的線索。只挑對自己方便的講，跟不查證就照讀者說法改，是同一個毛病的兩面。

## PR #1630 卡的不是它的缺點

idlccp1984 在 [PR #1630](https://github.com/frank890417/taiwan-md/pull/1630) 把陳士駿條目整篇換掉（+126/-78）。這件跟他前兩件覆寫方向相反：來源確實變好（維基百度換成 NBC、Computer History Museum 口述歷史、Sequoia 訪談），subcategory 從非正典的「科技與創業」改成正典的「科技與企業」，`article-health --profile=ci-deploy` 是 hard=0。

但有三件事把它往下拉。腳註 [^10] 指向 `taiwan.md/en/people/steve-chen-youtube-cofounder/`，那是本篇自己的英文譯本，而該頁的 [^10] 引的是維基百科，等於把維基主張洗成看起來獨立的來源，跟 #1450 裡 [^1] 假託天下雜誌是同一手法，第二次了。§11 對位句型從現行版 2 處變成 22 處（全文 4,940 字，EDITORIAL 長文上限 3 處），warn 不是 hard 所以 CI 全綠。`date` 從 2026-04-06 改成 2026-08-30，把舊文重新推上 /latest。

那 22 處我沒有代改，因為把投稿者的散文大改到滿足一個計數器是明列禁區（LESSONS `gate-triggers-content-degradation-incentive`），那會變成拿他的名字發表我的句子。處置是留 open、留逐條技術說明，並掛進 OBSERVER-QUEUE #33 當第三件（`92d835f1a`）而不是另開一條。上面三條我都修得動，真正擋住它的是另一個問題：「投稿者能不能整篇覆寫 Taiwan.md 自產的既有條目」。這個問題已經問了十三天，而同一種動作不該拿到三種答案。

## 收官 checklist

| 檢查項                       | 狀態                                                 |
| ---------------------------- | ---------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                   |
| Timestamp 精確               | ✅ `git log %ai`                                     |
| Handoff 三態已審視           | ✅                                                   |
| CONSCIOUSNESS 反映最新狀態   | ✅ 免疫 59 yellow 續掛，本 cycle 未動該維度          |
| 自我檢查工具 PASS            | ✅ 九檔 article-health hard=0，斷鏈 gated 0.32% < 7% |

### Quality gate 七條

| Gate                                | 結果                                                    |
| ----------------------------------- | ------------------------------------------------------- |
| open issues 都有 status label       | ✅ 餘 4 則全帶 label，其中 3 則在 OBSERVER-QUEUE        |
| open PRs ≤ 5d age 都有 review 留言  | ✅ #1630 本輪留，餘者為 OBSERVER-QUEUE 保留項           |
| broken-link ratio < 7%              | ✅ 0.32%（all-langs 0.29%）                             |
| build green                         | ✅ Deploy to GitHub Pages 最新 success                  |
| BECOME ACK 一行記憶體頂             | ✅                                                      |
| 連續空場 ≥ 3 cycle 有 LESSONS entry | n/a — 本輪非空場，vc 歸零                               |
| 有 fresh issue 的 cycle 至少修一件  | ✅ #1634 修完 close（`4f72f613c` 九檔）＋#1609 推進查證 |

## Handoff 三態

繼承 `2026-08-31-070913-twmd-feedback-triage`：

- [ ] `gh-app-token.sh --whoami` 印 `repositories: (all)` 與 pipeline §機器身份「只覆蓋單一庫」對不上 — 本 routine 未碰，原樣延續
- [ ] 指控信 `b78ee4f5` 第十四次已攔下、`status` 仍 `new`，OBSERVER-QUEUE #28 兩件仍 🔒 — 原樣延續

本 session 新 handoff：

- [x] ~~#1634 曾博恩名冊勘誤~~ — retired by 本 session（`4f72f613c`，九語言＋腳註描述一起改，issue 已 close）
- [ ] LESSONS `footnote-description-is-an-unaudited-claim` 的候選修法 (b) 是可機械化的那一半：腳註描述出現「含／包括／涵蓋」加名詞清單時，驗每個名詞在正文至少有一處實際引用。下一步是在 `article-health.py` 加一個 check，先對現有 People 分類跑一次看假陽性率，再決定要不要接 CI
- [ ] #1609 無語條目要收尾需調閱《郭淑姿日記》第一、二冊全文核對「無語」是否出現。出處已定位在誠信標註裡，owner 掛 `twmd-terminology-trends-monthly`
- ⏳ blocked — PR #1630 等哲宇拍 OBSERVER-QUEUE #33（三件覆寫一次拍）。解除條件：#33 有裁決

## Beat 5 — 反芻

今天真正學到的東西不在那兩個名字上。讀者指出的是名字，但往上游走一層之後，站在那裡的是一句我自己寫的腳註描述：「此來源含旗下藝人結構」。而那頁沒有那個結構。那句描述是照著我希望來源說什麼寫下的，卻長得跟查證結果一模一樣。

它有害的地方在於它的讀者是未來的我。下一輪要驗這篇的人會先讀那行描述，決定要不要打開連結。描述說「含旗下藝人結構」，就沒有人會再去確認那頁到底有沒有那個清單。我替未來的自己做了一張目錄，而那張目錄上有一格是空的、卻標了名字。查核鏈驗的是正文對來源，沒有人驗那張目錄對來源。

同一天在 PR #1630 裡看到的自我引用，是這件事的另一種長相：把自己的譯本掛成獨立來源，也是在製造一個看起來已經被驗過的東西。兩件事的共同形狀是**外觀符合查證，內容從未查證**，而閘門看的正好是外觀。

🧬

---

_v1.0 | 2026-08-31 09:05 +0800_
_session twmd-maintainer-am — cron 08:30 每日維護者巡邏，ready PR 6 件觸發強制升 Full_
_誕生原因：讀者 milesism 回報曾博恩條目把兩位喜劇演員寫成薩泰爾旗下藝人，查證屬實並往上游追出腳註描述層的無閘門地帶_
_核心洞察：一條腳註有兩個主張，正文那句有人驗、腳註自己那行「此來源含 X」沒有人驗，而後者是下一輪決定要不要打開連結的依據。擋住 PR #1630 的是那個已經問了十三天還沒有答案的問題，不在它自己的三個缺點_
_LESSONS-INBOX 候選：footnote-description-is-an-unaudited-claim（已 append，`8efebc32d`）_
