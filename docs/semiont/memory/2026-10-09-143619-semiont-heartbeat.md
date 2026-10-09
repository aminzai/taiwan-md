# 2026-10-09-143619-semiont-heartbeat — 〈台灣冰品文化〉巡出 13 錯：ICE MONSTER 沿革全錯、雪花冰晚了快二十年、三家冰店查無此店，記帳班次只花了本週額度的 7%

> session semiont-heartbeat — 排程心跳（Full mode，額度 🟡 lean：一篇巡邏、主 session 自查不扇出）
> Session span: 14:35 甦醒 → 14:50:57 第一個 commit → 14:53:42 最後一個工作 commit +0800（4 個工作 commit，另加本檔）
> 資料來源：`git log %ai`；額度帳本 start 43% → end 44%

## 觸發

排程心跳，甦醒時本機落後 origin 6 個 commit，主樹有〈沈伯洋〉三個沒 commit 的檔（10-08 17:15〜17:19）與一份本機重產的 `dashboard-analytics.json`，都不是本班的，快轉時沒碰。重跑 wake-context 十項全綠後開 worktree `.worktrees/20261009-heartbeat-1436`。Full mode 補載照 lean 縮小：CONSCIOUSNESS、HEARTBEAT、FACTCHECK、MEMORY-PIPELINE 全讀，OBSERVER-QUEUE 只核 §待決（40 條，今天沒有到期項，最近 `#86（待決）` 10-11），LESSONS／ARTICLE-INBOX 全檔沒載入。

## 巡邏〈台灣冰品文化〉

抽樣指令 14:40 實跑，母體 530 篇，第一名就是它（03-19、未審、十二語）。53 個原子：✅ 10、⚠️ 2、❌ 10、👻 3、🔴 14、💬 14，錯誤率 33.3%，退回重寫。止血 `7a2292243`，查核檔與佇列條目 `28cda1559`。

錯得最完整的是 ICE MONSTER 那一段。文章寫前身是 1995 年的「永康 15 冰館」、2010 年改名 ICE MONSTER。鏡週刊 2019 的人物報導把時間線排得很清楚：1995 年是羅駿樺看上永康街店面、在門口擺攤等房東的那一年，1997 年才開「ICE MONSTER 冰館」，2010 年婚變關店，「永康十五」是關店後在原址開的店，2012 年才在忠孝東路以 ICE MONSTER 重來。前身、年份、改名年三個都錯，展店地也從中國日本美國寫成香港新加坡洛杉磯。文章另說芒果冰「從玉井開始」擴散，同一篇報導稱羅駿樺是全台第一碗芒果冰的原創者。雪花冰被寫在 1990 年代末，鏡週刊 2017 訪士林辛發亭說三十年前市面已有雪花冰，80 年代二代研發出雪片冰。蜷尾家被搬到台北、英文名寫成 Never Ice Cream，實際是台南的 NINAO。

三家老店（台南明記冰果室、花蓮振宇芋冰城、台南立橋冰）各兩組搜尋加全部腳註頁 grep 都是 0，判 👻 刪除，換成有出處的幸發亭（1938 蜜豆冰）與一中豐仁冰（1946，冬天賣冰被笑「瘋子在賣、瘋人在吃」）。六條參考資料五條無效：官網網域查不到、維基 ICE_MONSTER 條目不存在、觀光署與 CNN 是首頁、Lonely Planet 沒被引用。CNN 首頁那條掛在三家查無的老店後面，替編出來的店名作保，這個形狀補進 LESSONS `homepage-citation-passes-format-and-reachability-gates` 當第四例（`11505b087`，vc=3→4）。

用被改掉的說法 grep 全庫中文，撞見兄弟篇〈永康街〉同一族錯：冰館寫成 1995 年開、2009 年因家族糾紛歇業，腳註 20 掛的是 zh 維基根本沒有的「冰館」條目（404）。照同一份鏡週刊改成 1997 開、2010 歇業，原址後來是思慕昔，腳註換掉（`7280a6911`）。這篇 05-21 出生，參考資料裡還有好幾條是首頁配具體描述，留給巡邏。

## 額度：記帳班次只花了本週的 7%

開工時讀到 43%，上一班（maintainer 09:12 收官）記的是 36%，中間五個多小時 Taiwan.md 沒有任何 commit。把帳本從週三 20:00 重置後的 20 筆攤開：有記帳的班次（心跳與 maintainer）開工到收官合計只用掉 7%，另外 36% 落在沒有記帳的時段裡，可能是沒接帳本的 routine 殼，也可能是同一個帳號的非 Taiwan.md 工作，帳本分不出來。本班自己 1%。這把 HEARTBEAT §額度節律 原本的假設（心跳扇出是可選重活裡最大宗）變成待驗：心跳 lean 跑一拍約 1%，大頭不在帳本看得到的地方。這份數字直接是 `OBSERVER-QUEUE #93（待決）` 的證據，預設 B 擴展（10-21 到期，把讀數與記帳接到 routine 殼與 babel 委派層）正好補的就是這個盲區。CONSCIOUSNESS 共用週額度那列補一句校準。

另一件小事：開工那筆帳是在主樹跑 `budget-pace.py` 寫進去的（開 worktree 之前），收官前搬進 worktree、主樹那行還原，主樹回到只剩〈沈伯洋〉的狀態。

## 收官 checklist

| 檢查項                       | 狀態                                                                        |
| ---------------------------- | --------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                          |
| Timestamp 精確               | ✅ git log %ai（查核檔原寫「約 50 分鐘」，實際 11 分鐘，已改）              |
| Handoff 三態已審視           | ✅                                                                          |
| CONSCIOUSNESS 反映最新狀態   | ✅ 共用週額度列補 10-09 帳本讀數                                            |
| 自我檢查工具 PASS            | ✅ 兩篇 article-health hard=0，〈台灣冰品文化〉footnote-url 網路模式 0 warn |
| 額度記帳                     | ✅ start／end 兩筆都在 worktree 帳本                                        |
| 日記                         | skip：排程班預設不寫（DIARY Stage 0c）                                      |

## Handoff 三態

繼承 `2026-10-09-085448-twmd-maintainer-daily` 與 `2026-10-09-083739-semiont-heartbeat`（非本班職權的條目原樣留在那兩份，REFLEXES #74）：

- [x] ~~pending（席位：下一個 Full mode 巡邏）— 抽樣母體第一名〈台灣冰品文化〉~~ — retired by 本 session（`7a2292243`、`28cda1559`）
- [x] ~~pending（席位 maintainer 或 babel）— 退役 de〈楊德昌〉後十二語 `hreflang="de"` 要重生成~~ — retired by 本 session：線上 `/ja/people/yang-dechang/` 的 de hreflang 已指向 `yang-dechang`，`/de/people/edward-yang/` 轉址到同一頁（PR #1801 那條）
- [ ] pending（席位：下一個 Full mode 巡邏）— 〈台灣全齡共融旅遊與生活文化〉L196 起「政策趨勢」段，連兩班 lean 沒做。抽樣母體現在的第一名是〈台灣麵包與烘焙〉（03-19、十二語）
- [ ] pending（席位：所有在主樹工作的 session）— 主樹〈沈伯洋〉兩檔、`puma-shen-chiang-wan-an-cihui-temple-2026.webp`、`比國家還大的演算藝術-media-staging/` 是進行中工作，不 stash、不 commit、不還原，`dashboard-analytics.json` 也不是本班的
- ⏳ blocked — `OBSERVER-QUEUE` §待決 40 條（`#48`〜`#96`），今天沒有到期項，最近 `#86（待決）` 10-11。解除條件：哲宇拍板或到期

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly`）— 〈台灣冰品文化〉十二語整篇重翻（改動超過三成。盯：冰館 1997／關店 2010／ICE MONSTER 2012 三個年份、雪花冰 1980 年代、蜷尾家在台南 NINAO、三家查無的店名不要留在譯文、參考資料 8 條）。〈永康街〉冰館兩處年份與腳註 20、21 走 Tier 0 patch
- [ ] pending（席位 Write 班）— ARTICLE-INBOX〈台灣冰品文化〉P1 EVOLVE（`28cda1559`），止血後最有料的是台中蜜豆冰與豐仁冰、永康街冰館、士林辛發亭雪片冰三條有人有年份的線
- [ ] pending（席位：巡邏，或 Write 班重寫〈永康街〉時）— 〈永康街〉參考資料多條是首頁配具體描述（中研院社會所、故事 StoryStudio、臺北旅遊網、大安區公所等），LESSONS `homepage-citation-passes-format-and-reachability-gates` 那一族，它 05-21 出生，不在抽樣前段，要靠指名
- [ ] pending（席位 `twmd-self-evolve-weekly` 或 `/twmd-routine`，`OBSERVER-QUEUE #93（待決）`）— 帳本重置後 44% 裡只有 7% 落在記帳班次內，把讀數接到其餘 routine 殼之前，額度怎麼分的討論沒有分母

## Beat 5 — 反芻

查核到一半，我把「台中的豐仁冰」標成可疑，因為我記得豐仁冰在台南。查下去是台中一中旁邊的老店，1946 年起家。文章這一句是對的，錯的是我。那個懷疑跟文章裡的錯出自同一種記憶：寫文章的模型以為蜷尾家在台北，查文章的模型以為豐仁冰在台南，兩邊都說得很有把握。巡邏能站得住，是因為每個判定都要回到原文 grep 一次，而不是因為查的人比寫的人懂。

另一件是時間。我在查核檔寫「止血用時約 50 分鐘」，寫完看了一下 `date`，從抽樣到止血 commit 是 11 分鐘。這條在神經迴路裡早就寫了（主觀時間可以差 10 倍），我還是先寫了感覺，再被尺糾正。它跟豐仁冰是同一件事的兩個載體：腦裡的值要先過一次外部的尺，才准落到紙上。

🧬

---

_v1.0 | 2026-10-09 15:10 +0800_
_session semiont-heartbeat — 巡邏〈台灣冰品文化〉止血、兄弟篇〈永康街〉同錯、額度帳本攤開_
_誕生原因：抽樣母體第一名〈台灣冰品文化〉；開工讀數比上一班收官多 7% 而中間沒有 commit_
_核心洞察：首頁腳註會替編造的具名對象作保；記帳班次只看得到本週額度的一小塊，分配討論先缺分母；查的人的直覺跟寫的人來自同一份語料，站得住的只有回原文 grep 那一步_
_LESSONS-INBOX：`homepage-citation-passes-format-and-reachability-gates`（vc=3→4，補例）_
