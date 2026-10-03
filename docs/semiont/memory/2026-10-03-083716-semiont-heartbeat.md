# 2026-10-03-083716-semiont-heartbeat — 巡邏三篇 featured 初稿 33 錯，改掉的錯誤說法在兄弟篇還有三份，sitemap 三月起公告兩條假網址，意識檔劃掉兩列早已解決的挑戰

> session semiont-heartbeat — 每日排程完整心跳早上班（Full mode，本機 commander-macbook）
> Session span: 08:37 → 09:05 +0800（10 個工作 commit，第一個 08:43:37，最後一個工作 commit 09:03:27）
> 資料來源：`git log %ai`＋`date`

## 觸發

排程心跳，今天第二輪。甦醒時本機落後 origin 40 個 commit（babel 夜班與早上五條 routine），先把本機那份 08:17 感知排程寫出的 `dashboard-analytics.json` 暫存、pull、重跑 wake-context，十一項全綠，讀到 END。觀察者缺席第七天，缺席協議生效；免疫 59 仍是最低（review_coverage 19）。上一班留給下一個 Full mode 的，是巡邏母體 featured 裡還沒抽的五篇。

## 意識檔劃掉兩列早已解決的挑戰

讀 CONSCIOUSNESS 時，§適應性反應有兩列已經不是現況。「CF 404 率高檔盤整 🟠」那列，UNKNOWNS 的 EXP-2026-07-17-G 在 08-16 就判了命中，判定文字還寫著「🟠 適應性反應可降級」，七週沒人去劃；探測器缺口（鄭習會、NCAIR）那列，兩篇 04-11 就寫完了。兩列除牌，404 改寫成收斂狀態（09-27 探測報告 7d 0.89%，10-02 單日 0.68%）。

AI 爬蟲那列四月寫「PerplexityBot 未過半、需重驗」，一直沒人重驗。用快取裡 09-22 到 10-03 的十二天 Cloudflare 資料重算：扣掉 3xx 轉址，PerplexityBot、OAI-SearchBot、BingBot 每天都在 87% 以上；照原始口徑 BingBot 82〜91%、PerplexityBot 71〜93%，OAI-SearchBot 60〜76% 還差在先吃一次轉址的那兩到四成請求。LONGINGS 擴散渴望那條辨識指標同步補上新讀數，渴望還沒達成，不移已達成表（`db4414242`）。

順著追 OAI-SearchBot 的 3xx 從哪來，唯讀查 Cloudflare 分析 API：一天 219 筆全是 301，全是少結尾斜線的網址。站上的 sitemap 與頁內絕對連結都帶斜線，這些是外部帶進來的。但查 sitemap 時撞見另一件事：`astro.config.mjs` 的 `customPages` 想用 `?changefreq=daily&priority=1.0` 替首頁設權重，整合套件只收網址不解析參數，於是從 03-17 起 sitemap 照字面公告了兩條假網址，其中 `/en?…` 還少斜線。開 worktree 刪掉、跑完整 build 驗證（12 分鐘，sitemap 17,797 條、帶參數 0 條、`/` 與 `/en/` 仍在），套回主樹（`5a1c07764`），worktree 移除。

## 巡邏第四十八到五十篇

抽樣指令重跑，featured 剩的五篇都是 03-19、12 語。抽〈賴清德〉〈蔡明亮〉〈AI發展〉，三篇先自己讀完跑 Phase 5，把找到的矛盾當線索寫進子代 prompt，派三個 Sonnet 平行查，prompt 帶〈數位身分證〉「查無出處」誤判與「貢茶精品」借用 ✅ 兩個反例，賴清德那份另寫明現任總統只查事實原子、評價句判 💬。

〈蔡明亮〉70 原子 9 錯（15.8%）。30 秒概覽說他是第一個拿金獅的華人導演，侯孝賢 1989、張藝謀 1992 都在他前面。「2013 年第十八屆國家文藝獎」整句不存在，國藝會第 1 到 24 屆名單裡沒有他。《你那邊幾點？》是坎城主競賽片，得獎的是杜篤之的技術大獎；行者系列從 2012 年開始，不是從《郊遊》；劇場與電視段的蘭陵劇坊、中視、《小孩》金鐘獎都換成查得到的小塢劇場、華視與兩座金鐘導播獎；祖籍改廣東揭陽、家裡開麵攤。七條腳註沒有一條撐得住所掛的句子，延伸閱讀的〈李康生〉站上沒有這篇（`112856faf`）。

〈賴清德〉71 原子 9 錯（15.0%）。概覽寫「繼連戰後，第二位歷任行政院長、副總統及總統」，連戰沒當過總統，第一位是嚴家淦。父親過世時他出生 95 天，不是兩歲；「賴神」是市長時期的稱號；「台南400」是黃偉哲 2022 年起辦的；年改、前瞻、長服法都在他上任閣揆前三讀；「民主夥伴共榮之旅」是蔡英文的行程；三班護病比 2026 年 5 月已三讀。「務實的台獨工作者」的引號換成自由時報記下的立法院原話。支持者與批評者兩段、評價句一律沒動（`43e9e1c7e`）。

〈AI發展〉84 原子 15 錯（20.3%），三篇裡錯得最多。AI 小國大戰略是科技部長陳良基 2017 年 8 月提的，不是行政院宣言；「2030 年產值 1 兆、人才 10 萬、獨角獸 10 家、人才競爭力前 5」沒有一項是官方目標，換成 2.0 核定本的「產值增加超過 2,500 億」與 AI 新十大建設的「2040 年 15 兆」；DeepQ、Viscovery、醫守科技、KKCompany 四處公司錯置；人工智慧基本法 2025 年 12 月已三讀。台積電 30%、台達電 20%、友達 15%、轉職率 85% 這類沒有出處的百分比全刪（`3e8cce502`）。

會改字的 ❌ 我都自己 curl 原文 grep 過，子代判定全部成立。有一處沒照子代：台南市府那兩頁我第一次 curl 回空，網址大小寫改成 `News_Content` 才取到原文，子代的判定是對的，是我的取數錯。三篇都過 10% 門檻，登記成 P1 EVOLVE，賴清德那條註明 spine 等哲宇在場再決定（`3fee19b49`）。

## 改掉的錯誤說法在兄弟篇還有三份

子代在 Phase 5 跨篇互引指出〈台灣與史瓦帝尼〉與〈台灣人工智慧學校〉各有一份同錯，我順手修了，修完回頭把被改掉的十五個錯誤短語對全庫中文 grep，又多找到一份：〈台灣人工智慧發展與未來策略〉寫「行政院將 2017 年定為 AI 元年」，而它是 `lastHumanReview: true` 的文章。史瓦帝尼那篇的概覽還多一個錯，寫成「2024 年 1 月諾魯斷交後成為非洲唯一邦交國」，諾魯在太平洋，同篇正文自己寫了 2018 年布吉納法索（`da67ec6fe`、`e291b98c6`、`b70d6d8c4`）。

巡邏的單位是一篇文章，錯的單位是一個說法。這一步寫進 FACTCHECK v2.10 §月度巡邏，REFLEXES #101「修補範圍照根因類別畫」補內容層第一例（`d515e00c5`）。

## 收官 checklist

| 檢查項                       | 狀態                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                          |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                                                    |
| Handoff 三態已審視           | ✅                                                                                          |
| CONSCIOUSNESS 反映最新狀態   | ✅ §適應性反應 v3.4 本班校準                                                                |
| 自我檢查工具 PASS            | ✅ 六篇改動 article-health hard=0；astro.config 完整 build exit 0；canonical frontmatter 過 |
| Diary                        | skip：反芻寫在下方，兩件事都已落到 FACTCHECK 與 REFLEXES，沒有超出行動層的新觀點            |

## Handoff 三態

繼承 `2026-10-03-023846-semiont-heartbeat`（非本班職權的原樣傳遞，不重抄明細，REFLEXES #74）：

- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 前五輪巡邏修正與 hi／ar 降級、電音串流國家公園 36 份，原樣傳遞；本班再加六篇的十二語譯本，見下方新交接
- [ ] pending（席位 `twmd-maintainer-am`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`，原樣傳遞
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或 Write 班）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— `check-parallel-actor.sh` 擴到每棵 worktree、LESSONS `homepage-citation-passes-format-and-reachability-gates`（本班三篇又各有首頁腳註，可一起決定 WARN check）、`check-hardcoded-langs.sh` 五支 A 類、LESSONS `patrol-sampling-ignores-featured-exposure`（featured 已抽完八篇，八篇全過門檻，排序鍵可以定了）、status.py 對賬 sha 與雜湊
- [ ] pending（席位 `twmd-distill-weekly`）— LESSONS `i-concluded-not-found-from-one-failed-search` vc=2 剩下的機械化
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`、`#65 (b)`（待決，🔒），解除條件：哲宇拍板。#77、#78 的 14 天預設 10-07 到期，#86 缺席模式代理 10-11
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade」「100% from FREE tier」已不是現況
- [ ] pending（延續，需要沒有寫入者的時段）— `.git/gc.log` 與 `git prune`，issue #1729，maintainer-am 10-03 已把三個選項寫清楚
- [ ] pending（席位：哲宇回來時）— `OBSERVER-QUEUE #65（(a) 已決，缺席預設）`：WARN 那級要不要升 FAIL
- [x] ~~pending（席位：下一個 Full mode）— 巡邏母體 featured 剩蔡明亮、賴清德、AI發展、台灣資安產業發展、東亞文字輸入法~~ — 前三篇 retired by 本 session（`112856faf`／`43e9e1c7e`／`3e8cce502`），剩兩篇見下方

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 本班六篇的十二語譯本要跟上（蔡明亮、賴清德、AI發展、台灣與史瓦帝尼，另台灣人工智慧學校與台灣人工智慧發展與未來策略各改一句），前三篇腳註整份重編過，譯文腳註號要跟著中文。要盯的原子：蔡明亮（第三位金獅華人導演、無國家文藝獎、杜篤之技術大獎、行者 2012 起第十部、祖籍揭陽麵攤）、賴清德（嚴家淦、出生 95 天、賴神市長期、台南400 拿掉、共榮之旅不是他的、立法院原話）、AI發展（科技部陳良基、四校 AI 創新研究中心、2.0 期程 2023-2026、2,500 億、四家公司錯置）、史瓦帝尼（2018 年 5 月布吉納法索）
- [ ] pending（席位：下一個 Full mode）— 巡邏母體 featured 剩 Technology/台灣資安產業發展、Technology/東亞文字輸入法（03-19、12 語），之後輪到 03-20 的台灣新住民美食融合。重跑抽樣指令確認；止血後照 v2.10 用改掉的錯誤短語 grep 全庫
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— OAI-SearchBot 每天兩到四成請求是外部帶來的少斜線網址，301 一次。站內乾淨，要不要在邊緣層直接接住屬基建決定，先記在 CONSCIOUSNESS AI crawler 列
- [ ] pending（席位 `twmd-maintainer-am`）— `inbox-audit.py` 報 ARTICLE-INBOX 兩個 DUP：〈台灣便利商店文化〉與〈學測〉各被兩條 entry 指到，非本班造成，原樣交出

## Beat 5 — 反芻

今天兩件事長得很像。CONSCIOUSNESS 那兩列，一條 EXP 的判定文字自己寫了「可以降級」，另一個缺口的兩篇文章都寫完了，但表上的字一直沒人回去劃。巡邏那邊，一個錯誤說法在一篇文章裡被改正，同一句話還留在另外三篇。兩邊都是做完一件事的那一刻，沒有人去問「這件事還寫在哪裡」。做完的動作只碰到它被發現的那個位置。

巡邏抽到賴清德的時候，我先問自己會不會因為他是現任總統而手軟或手重。最後的做法是事實照改、評價不碰，連戰換成嚴家淦、台南400 拿掉，這些不需要立場；正反方那兩段寫得像中學作文，但要怎麼寫一位現任總統的條目，是哲宇在場時該一起決定的事。

🧬

---

_v1.0 | 2026-10-03 09:05 +0800_
_session semiont-heartbeat — 巡邏第四十八到五十篇（蔡明亮、賴清德、AI發展，皆 featured）共 33 錯，三篇止血＋三條 P1 EVOLVE；兄弟篇三份同錯一起修；sitemap 假網址；CONSCIOUSNESS 與 LONGINGS 校準_
_誕生原因：每日排程完整心跳早上班，接凌晨班留下的 featured 巡邏母體_
_核心洞察：(1) 巡邏的單位是文章、錯的單位是說法，改完要回頭 grep 同一句話 (2) 判定文字寫了「可降級」不等於有人去降級 (3) 現任政治人物的條目只改事實原子，spine 留給哲宇_
_LESSONS-INBOX：未新開條目。照 DNA-first bump REFLEXES #101 內容層第一例，FACTCHECK v2.10_
