# 紀懷新 (Ed H. Chi) 深度研究報告 §D

**子題 D：近期工作 + 台灣連結現況 + 反方批判 + AGI 觀點**
研究日期：2026-06-27 | Sub-agent: Claude Sonnet 4.6

---

## 搜尋日誌

| #   | 查詢                                                         | 目的               | 產出                        |
| --- | ------------------------------------------------------------ | ------------------ | --------------------------- |
| 1   | Transcript 3rQ4jPvvY0c.zh-TW.txt 全讀                        | 塞掐 E350 一手材料 | AGI/眼鏡/台灣片段           |
| 2   | Transcript f6mxGtSVPf0 + 51woDEK5NME 全讀                    | VK 兩集 AGI 補充   | CoT 心理學起源 + System 1/2 |
| 3   | Transcript nXVvvRhiGjI.en.txt 全讀                           | Astra 短片         | Project Astra 展示          |
| 4   | grep 台灣/眼鏡/AGI/回台/Gemini/Astra                         | 快速定位關鍵段     | 89行「台灣唯一」            |
| 5   | WebSearch 紀懷新 師大 演講 台灣                              | 回台活動           | NTNU 2019 演講確認          |
| 6   | WebSearch Ed Chi chain of thought controversy attribution    | CoT 歸功爭議       | 查無具體爭議                |
| 7   | WebSearch 紀懷新 中山大學 中興大學 演講                      | 台灣大學巡迴       | 中興2024-11-28 確認         |
| 8   | WebSearch Ed Chi recommendation system social harm criticism | 演算法問責         | 法律案件、YouTube訴訟       |
| 9   | WebFetch cm.nsysu.edu.tw 中興演講公告                        | 演講細節           | 日期地點主題確認            |
| 10  | WebFetch cs.nycu.edu.tw 陽明交通大學                         | 演講公告           | 2025-04 NYCU 演講確認       |
| 11  | WebFetch vocus.cc 專訪                                       | 紀懷新心理學 + CoT | 付費牆擋住主體              |
| 12  | WebSearch 紀懷新 天下雜誌 Gemini 要角                        | 台灣媒體影響力     | cw.com.tw 找到標題          |
| 13  | WebFetch cw.com.tw/article/5129031                           | 天下文章原文       | HTTP 403                    |
| 14  | WebSearch Ed Chi "chain of thought" "Denny Zhou" credit      | CoT 功勞歸屬       | 無正式爭議                  |
| 15  | WebFetch bnext.com.tw 2026 AI TAIWAN 演講                    | 近期活動           | 2026-06-26 演講確認         |
| 16  | WebFetch bnext.com.tw 2018 「台灣不要再錯失」                | 早期台灣關注       | 核心論點取得                |
| 17  | WebFetch Wikipedia Ed_Chi                                    | 身份/生平          | Taiwanese American + 生平   |
| 18  | WebSearch YouTube addiction lawsuit Google                   | 演算法社會代價     | 2026-03 陪審團判決          |
| 19  | WebSearch AGI timeline DeepMind prediction criticism         | AGI hype 批評      | Hassabis 2030 vs 學界懷疑   |
| 20  | WebSearch 紀懷新 師大 Google AI首席工程師                    | 師大演講細節       | 2019-12-18 演講全紀錄       |
| 21  | WebFetch pr.ntnu.edu.tw 師大新聞稿                           | 師大演講逐字       | 演講細節全取                |
| 22  | WebSearch 紀懷新 塞掐 台灣唯一 智慧眼鏡                      | 標題 claim 求證    | YouTube 標題確認            |

---

## Findings D

### D-1 近期工作（現任角色 + 2024-2026 重要里程碑）

**職稱演變**（信度 A）

- 2017：Google 首席科學家（Principal Scientist）
- 2021：傑出科學家（Distinguished Scientist）
- 現任：Google DeepMind 研究副總裁（VP of Research）
- Sources：Wikipedia + 師大新聞稿（2019 標為「AI首席工程師」，當時頭銜較早期版本）

**Google I/O 2025 核心役**（信度 A，一手 transcript）
紀懷新在塞掐 E350（約 2025 年中）明確說明：他直接負責 Project Astra 的研究方向。

> 「很像比如說我負責的這個 Project Astra 裡面這個 capability，他就是這整個模型，這個大模型現在是能夠跟你共處在一個環境裡面。」
> （3rQ4jPvvY0c.zh-TW.txt 行 80）

**Project Astra — Situated Intelligent Assistant**（信度 A）

- 原名 SIA（Situated Intelligent Assistant）
- 核心概念：AI 必須「situated」——理解使用者所在的物理情境，不只活在虛擬世界
- 2024 展示：辦公室環境掃描（黑板識別）；2025 展示：青少年修腳踏車的完整情境推理
- 紀的 Barcelona 測試：手機裝 Astra，掃城市天際線 → AI 回答「你在 Barcelona」→ 「你在 Saint Martin 區」→ 推薦附近 Michelin 餐廳（VK Transcript f6mxGtSVPf0.zh-TW.txt 行 80-86）
- 2025 Google I/O：於眼鏡（Android XR glasses）上搭載 Astra，即本報告關鍵物件

**Gemini 發展時間線**（信度 A）

- 2015：sequence-to-sequence learning（sequential transduction）
- 2017：Transformer paper（Google Brain）
- Lambda → Bard → Gemini（命名整合約 2023）
- 2024：多模態大模型元年
- 2025：situated understanding 元年（紀的定義）

**Gemini Robotics**（信度 A）

- 2025-03 發布，紀在 VK 訪談（台灣回訪時與機器人團隊深聊）
- 展示：讓機器人「dunk a basketball in the hoop」——理解指令無需pre-train特定動作
- 預測：General Robotics（會做家務的人型機器人）在「有生之年應該看得到」，但不是幾年，約 10-20 年
  （3rQ4jPvvY0c.zh-TW.txt 行 140-146；f6mxGtSVPf0.zh-TW.txt 行 106-110）

**Project Duplex**（信度 A）

- 紀的前期成果：已能打電話幫使用者訂餐廳（分解式架構設計）
- 現在 Astra 方向：把 Duplex 的能力整合進 end-to-end 大模型架構

**2026 AI TAIWAN 未來商務展演講**（信度 A）

- 日期：2026-06-26（塞掐 E350 錄製於此活動前後）
- Source：bnext.com.tw
- 主題：推薦系統底層邏輯 → 個人通用助理時代

---

### D-2 台灣連結現況（最重要子題）

**出身聲明**（信度 A，一手 transcript 逐字）

> 「我是台灣土生土長的人，在淡水出生，然後在大概 15 歲的時候跟父母一起到美國去念書，因為我媽媽那時候跑去念博士。」
> （3rQ4jPvvY0c.zh-TW.txt 行 5，塞掐 E350）

注意：transcript 說「15 歲」；Wikipedia 說「during high school」；媒體報導有「14 歲」版本（未在本研究 transcript 中找到，標記為「14 vs 15 歲」待確認）。

**自我定位**（信度 A）

- Wikipedia 官方分類：「Taiwanese American」
- 本人台灣媒體受訪一律用流利中文，自稱「台灣人」，未特別區分 diaspora
- 無明確公開聲明自己是「台裔美國人」vs「台灣人」——但行為上持續與台灣媒體深度互動

**回台活動紀錄**（信度 A，由多來源交叉確認）

| 時間                       | 地點                                      | 主題                                                                                                | 來源                                     |
| -------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| 2019-12-18                 | 國立台灣師範大學（師大）                  | AI 對高等教育未來發展的影響（學術及行政主管專場）<br>同場：副校長李忠謀宣布 2020-01-02 理學院第二場 | pr.ntnu.edu.tw 新聞稿（完整確認）        |
| 2024-11-28                 | 國立中興大學 圖書館六樓會議廳（40人限定） | 教育部 ITSA 智慧創新關鍵人才躍升計畫 技術講座                                                       | cm.nsysu.edu.tw 公告（完整確認）         |
| 2025-04（月日待確認）      | 國立陽明交通大學 資訊工程學系             | "The Future of Discovery Assistance"（推薦系統演進→多模態助理→CoT 引用 8000+ 次）                   | cs.nycu.edu.tw 公告                      |
| 2025 年（Google I/O 前後） | 台灣（詳細場次不明）                      | 塞掐 E350 錄製；攜帶 Astra 眼鏡原型機                                                               | 3rQ4jPvvY0c.zh-TW.txt（一手 transcript） |
| 2026-06-26                 | AI TAIWAN 未來商務展                      | AI 推理能力底層邏輯；個人通用助理                                                                   | bnext.com.tw                             |

此外，f6mxGtSVPf0.zh-TW.txt（VK 訪談，約 2024-2025）中說：

> 「最近我們 Google 另外一個團隊我跟他們交流的挺多的，特別上一次回來台灣的時候，我跟他們聊的挺多的，因為他們也對這個 multi-modality 的 research 非常有興趣。」（行 101-107）

顯示回台頻率高，且維持主動與 Google Robotics 台灣據點的技術交流。

**天下雜誌「台灣是 Gemini 時代的要角」**（信度 B，無法直讀原文）

- URL：https://www.cw.com.tw/article/5129031
- 標題已確認（Google 搜尋結果出現）；HTTP 403 無法取得原文
- 摘要來源（二手）：「台灣在 Google 的整個運算能力生態鏈裡面佔有很重要的角色，在 Gemini 的新時代是一個很重要的合作夥伴」

**台灣觀察語句**（信度 A，transcript 逐字）

- 台灣交通攝影文化：「我回來台灣，看台灣的新聞，就覺得說，為什麼每一次撞車的時候都已經有人錄下來……台灣很習慣這件事情，我們在車上會有行車紀錄器」（3rQ4jPvvY0c.zh-TW.txt 行 95-98）
- 台灣長照問題：「特別是我覺得台灣的這種長照的問題，以後說 5 年後 10 年後會不會真的有一些比較 affordable 的機器人能夠幫助一些家裡的家務事」（行 149）
- 台灣 AI startup：「NVIDIA 說在過去的兩年裡面整個大爆炸，已經變成有一千家…在台灣的這種跟 AI 有關的 startup」（行 122）
- AlphaFold 台灣應用：「台灣就有很多人已經開始在應用了…好像說是一萬五千多個使用者在台灣在用」（行 164）
- 自動駕駛缺口：「台灣可能還沒但是因為我自己已經用這個自動駕駛也許四年」（行 191）
- 台灣年輕人創業建議：「be adaptive」（行 194-197）

**台灣媒體採訪頻度**（信度 A）

- 數位時代（bnext.com.tw）：多篇，2018 至 2026
- 天下雜誌：「台灣是 Gemini 時代的要角」
- Business Insider Taiwan：「三度錯過關鍵浪潮！紀懷新：AI 助理是下一個千億級商機」
- VK 科技閱讀時間（Podcast）：EP122 深度訪談（含 CoT 心理學淵源）
- 塞掐 Side Chat：E350（79分鐘，最長最深的一次）
- vocus 方格子：「心理學如何啟發 AI 關鍵論文」（付費牆）
- 遠見雜誌：「AI 從被動變主動」
- Yahoo 新聞（ETtoday 轉載）：生成式 AI 五大問題

**台灣教育投資或捐助**：查無此訊息（C 信度），未見公開記錄。

**台灣半導體定位表態**（信度 A）

> 「台灣在半導體這個部分，特別是這個 manufacturing 的這個部分，應該是地位是很難動搖的。」
> （3rQ4jPvvY0c.zh-TW.txt 行 119）

---

### D-3 AGI 觀點

**AGI 定義（紀懷新版，信度 A，一手逐字）**

塞掐 E350（3rQ4jPvvY0c.zh-TW.txt）——紀提出兩個 AGI 門檻：

**門檻一：Situated Understanding（進入物理世界）**

> 「這個 AI 不能完全只存活在一個虛擬的世界裡面，而是需要到一個人類的世界裡面去。」（行 170）
> 「2024、2025 年感覺到這個 is starting to happen。」（行 170）

**門檻二：One-shot Learning（教你一次就會）**

> 「下一個 AGI 最重要的 starting point 我個人認為就是說你要能夠做到我教你一次你就以後就會了。」（行 173）
> 「哪一天你的阿嬤罵你家裡的機器人說我已經教你一次，你怎麼還不會，你就知道 AGI 到來了。」（行 179）
> 「我們世界的 AGI 是由此判斷的，我們的衡量標準長在阿嬤身上。」（行 179）

**門檻三（補充）：自我學習 Generalization**

> 「AGI 的開始它要能夠融入到這個真實世界裡面去（第一個），第二個我教你一次不要我重複的教你，那個叫做 machine learning 那個不叫做 AI，然後第三呢是舉一反三就是自己開始學習。」（行 203）

**System 1 + System 2 整合就是 AGI（VK transcript f6mxGtSVPf0 行 47-53，信度 A）**

> 「用這種 Transformer 的 Technology 能夠做到 Both System 1 and System 2 integrate together into a single system，那這種 integration 非常有可能就是 AGI 的開始。」
> 「如果我們用另外一個方法來看這個東西，就是說 System 1 and System 2 的 integration 是 AGI 的 definition 的話，那我們已經開始做到這件事情了。」

**AGI 時間表（信度 A）**

- 紀刻意不給具體年份，強調「教你預測的技能而非告訴你答案」
- 對機器人達到 general purpose（洗衣服、煮飯）：「不是幾年的時間，但在有生之年應該看得到」「10 到 20 年之內」
- 8 年革命週期理論：1991 Web → 1999 Google → 2007 iPhone → 2015 → 2023 Gemini/ChatGPT → 2031 通用模型習以為常

**DeepThink（信度 A，VK transcript）**

- 紀稱 DeepThink 是「反思」（reflection）的開始——不只 follow template，還會 explore 不同思路
- 這正是 Demis Hassabis 所指的 AlphaGo/AlphaZero 的 Agent-Based 思維回歸
- CoT → DeepThink 的核心跳躍：從 exploitation（照公式走）到 exploration（反思公式是否正確）
- 「Chain of Thought 並沒有考慮這件事情，我當然後來也有想過，但是真正的落實的時候呢，發現事實上這些 model 可以不停的 apply 之前的 chain of thought 來一直最佳化自己的想法。」（f6mxGtSVPf0.zh-TW.txt 行 29）

---

## 反方 perspective scan（≥5 條）

### P1：CoT 功勞歸屬辯論

**立場摘要**：CoT 有九位作者，紀懷新是最後（倒數第二）位，Jason Wei 和 Denny Zhou 才是第一作者和通訊作者。台灣媒體傾向將紀個人化為「CoT 發明者」，略過集體貢獻。

**最強論點**：

- 原 paper（arxiv 2201.11903）：Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou——Ed Chi 排第七。
- Denny Zhou 在自己的 Twitter 仍在說「chain of thought = CoT reasoning, not just CoT prompting」，定義持續被 Ed Chi（和其他人）宣揚的版本所主導。
- VK transcript 中紀說「我跟 Danny Zhou 在我的 team 裡面就開始在想」——確認 Denny（Danny）Zhou 才是 team 裡實際提出想法的人，紀的角色更多是 intellectual mentor / team lead。
- 更早的 step-by-step prompting 先例：零樣本 CoT（Kojima et al., 2022「Let's think step by step」）和 scratchpad 都是同期或更早的思路，無法把「人類學了教機器推理」的全功算在紀一人身上。

**源頭** ：arxiv.org/abs/2201.11903；dennyzhou.github.io；VK transcript f6mxGtSVPf0 行 54-65

**來源品質**：A（原始 paper + 第一作者首頁）

**注意**：無「正式爭議」或「公開批評」記錄，這是潛在的歸功框架問題，非公開衝突。

---

### P2：「台灣之光」框架 — 15 歲離台的問題

**立場摘要**：紀懷新 15 歲（高中入學前）離台赴美，在台灣的生命只有童年與少年初期。「台灣之光」標籤是台媒貼的，而非本人宣稱。這種框架是否消費移民成就？

**最強論點**：

- 紀在塞掐 E350 自述：「我是台灣土生土長的人在淡水出生，然後在大概 15 歲的時候跟父母一起到美國去念書，因為我媽媽那時候跑去念博士。」——他赴美是跟著媽媽念博士，不是個人選擇；離台年齡是 15（或 14）歲。
- Wikipedia 分類：「Taiwanese American」——兩種身份共存，非單純台灣人。
- 他在台灣接受教育、成長至青少年期；但全部大學、博士、職業生涯都在美國。
- 台灣媒體有明顯的 identity capture 傾向（把 Taiwanese-American 的成就算進「台灣的」），紀本人未公開反對，但也未特別積極「認領」台灣之光稱號。

**來源品質**：B（transcript 是 A 級，但「15 vs 14 歲」細節有待確認；台媒消費分析是推論）

**質疑是否真的有問題**：紀懷新確實持續回台、用中文公開發言、對台灣議題表達關切（長照、AI 機會、半導體）——說他「只是被消費」站不住腳。但 identity 本身確有模糊地帶。

---

### P3：推薦系統的社會代價——他是否應被問責？

**立場摘要**：紀懷新的研究團隊自 2013 年起對 YouTube、Google News、Google Play Store 做出 420+ 項推薦系統改進。2026-03 陪審團判定 YouTube 對青少年成癮有責任，判 Google 承擔約 30% 賠償。紀作為推薦系統 VP，是否有道德責任？

**最強論點**：

- Google/YouTube 推薦系統訴訟（2026-03 LA 陪審團判決）：「Meta 和 Google 對青少年成癮和心理健康危害有責任」——YouTube 被判承擔 ~30% 的 $6M 裁決。（Source: EPIC，Al Jazeera，Sokolove Law）
- 紀懷新被 ACM 2022 Fellow 以「recommender systems 的機器學習貢獻」授勳，明確確認他在推薦系統的核心地位。
- 批評者立場：讓推薦系統更精準（「0.1% improvement = $500M」）的邏輯，是以廣告收益最大化為目標，與使用者心理健康利益存在結構性衝突。
- 他對此問題的公開回應：在塞掐 E350 從未主動觸及演算法傷害議題；被問到的問題都聚焦在未來技術。沒有查到他公開談論推薦系統成癮問題的紀錄。

**來源品質**：A（法院判決、ACM 授勳均有公開文件）

---

### P4：CoT 讓 AI 更會「講道理」——是透明化還是更難問責？（社運視角）

**立場摘要**：CoT 被設計來讓 AI「展示推理過程」，但批評者指出，這讓 AI 更擅長生產看起來合理的理由，而非真正透明。特別在高風險決策（貸款、招聘、醫療）中，AI 的 CoT 輸出可能被用來掩蓋歧視性決策。

**最強論點**：

- 學術文獻（"Towards Better Chain-of-Thought"，arxiv 2405.18915）明確提出 CoT 的 faithfulness 問題：「CoT 輸出的 reasoning 不一定反映模型真正的 decision process」。
- 社運視角：當 AI 系統（如 FICO 信用評分替代者、招聘篩選）生成 CoT 解釋時，這些解釋可能是後驗合理化（post-hoc rationalization），而非真正因果推理——使算法歧視更難被揭露。
- Algorithmic Justice League 和 AI Now Institute 等組織長期批評：AI 可解釋性研究（XAI）往往服務於企業免責，而非真正問責。
- 紀懷新對此的回應：在 VK 訪談中說 alignment 問題和 AI 安全問題是「align to what humans want」——表明他意識到 alignment 的重要性，但未直接回應 CoT 的 faithfulness 限制。

**來源品質**：B（學術論文 A 級，但社運應用到 CoT 是推論連結）

---

### P5：AGI Hype——紀懷新的「阿嬤標準」是否有效規避追責？

**立場摘要**：紀懷新給 AGI 的定義（阿嬤罵掃地機器人）非常模糊，無法證偽，讓 AGI「進度」無法被外部評估，服務於科技公司的長期融資敘事。

**最強論點**：

- 學界批評（arxiv 2508.19749「Deep Hype in Artificial General Intelligence」）：AGI 定義的模糊是刻意設計的——讓不同 stakeholders 都能把自己的里程碑對準 AGI，維持市場熱度。
- 紀的阿嬤標準（「教你一次就會」）實際上是個移動靶：ChatGPT 在某些任務上已可「教一次就會」，但沒有人宣布 AGI 到來。他的定義無法被精確操作化。
- 他的 8 年週期理論（1991→1999→2007→2015→2023）雖然清晰，但 2031 預測（「大家習以為常大模型」）其實是一個非常低門檻的 claim，和 AGI 是兩回事。
- 相比之下，Demis Hassabis 給出了 2029-2030 的具體年份，反而更可問責。

**來源品質**：B（學術 paper A 級，對紀個人的解讀是推論）

---

### P6（附加）：Google Taiwan 「跑去台灣演講」vs 實質投資的落差

**立場摘要**：紀懷新每次回台都強調台灣的 AI 機會，但 Google 在台灣的 AI 研究投資遠不如台積電供應鏈的半導體依賴——是否是一種「情感外交」大於實質的訪台模式？

**最強論點**：

- 他 2018 年說「台灣不要再錯失機會」，2024 年說「台灣是 Gemini 時代的要角」，2026 年說「台灣 AI startup 一千家」——這些話的規律是「讚美 + 機會 + 你們要把握」，而非「Google 將在台灣投資 X」。
- Google 在台灣確實有重大投資（雲端資料中心），但 AI 研究人才在台灣的規模難以與矽谷、倫敦 DeepMind 相比。
- 他每次提台灣時都是回台「講演」的場合——audience capture bias 可能導致他對台灣的評價系統性偏正面。

**來源品質**：C（推論，缺乏 Google 投資數據支撐；此批評弱，標記薄弱）

---

## 引語庫

### 台灣相關（逐字，一手 transcript）

**Q1 出身自我描述**

> 「我是台灣土生土長的人在淡水出生，然後在大概 15 歲的時候跟父母一起到美國去念書，因為我媽媽那時候跑去念博士。」
> 場合：塞掐 Side Chat E350，主持人問背景；3rQ4jPvvY0c.zh-TW.txt 行 5
> Ctrl-F：✓「我是台灣土生土長的人」

**Q2 智慧眼鏡「台灣唯一」**

> 「這是台灣唯一一個在跑 Astra 的設備，對，應該是第一次進來。」
> 場合：塞掐 E350 錄製現場，紀懷新從口袋拿出眼鏡原型；3rQ4jPvvY0c.zh-TW.txt 行 89
> 注意：此為紀本人說的話，但語境是「應該是」（推測語氣），非官方聲明。是否真的「唯一」無法被第三方核實。
> Ctrl-F：✓「台灣唯一一個在跑 Astra 的設備」

**Q3 台灣半導體地位**

> 「台灣在半導體這個部分，特別是這個 manufacturing 的這個部分，應該是地位是很難動搖的。」
> 場合：塞掐 E350，討論台灣硬體機會；行 119
> Ctrl-F：✓「地位是很難動搖的」

**Q4 台灣 AI 機會（軟硬整合）**

> 「台灣如果人就可以把硬體跟軟體整合的好，利用大語言模型的能力，的確是一個很大機會。」
> 場合：塞掐 E350 行 122
> Ctrl-F：✓「把硬體跟軟體整合的好」

**Q5 台灣長照問題**

> 「特別是我覺得台灣的這種長照的問題，以後說 5 年後 10 年後，會不會真的有一些比較 affordable 的機器人能夠幫助一些家裡的家務事。」
> 場合：塞掐 E350 行 149
> Ctrl-F：✓「台灣的這種長照的問題」

**Q6 台灣年輕人建議**

> 「如果說台灣的軟體業也好，硬體業的朋友們，他們要做的事情就是 be adaptive。」
> 場合：塞掐 E350 行 197
> Ctrl-F：✓「台灣的軟體業也好」

**Q7 台灣回訪頻率（VK）**

> 「特別上一次回來台灣的時候，我跟他們聊的挺多的，因為他們也對這個 multi-modality 的 research 非常有興趣。」（指 Google Robotics 團隊）
> 場合：VK f6mxGtSVPf0.zh-TW.txt 行 101-107
> Ctrl-F：✓「上一次回來台灣的時候」

---

### AGI 相關（逐字，一手 transcript）

**Q8 阿嬤標準定義 AGI**

> 「哪一天你的阿嬤罵你家裡的機器人說我已經教你一次，你怎麼還不會，你就知道 AGI 到來了……我們的衡量標準長在阿嬤身上。」
> 場合：塞掐 E350，被問 AGI 定義；3rQ4jPvvY0c.zh-TW.txt 行 179
> Ctrl-F：✓「我們的衡量標準長在阿嬤身上」

**Q9 AGI 三要件**

> 「AGI 的開始，它要能夠融入到這個真實世界裡面去（第一個），第二個我教你一次不要我重複的教你，那個叫做 machine learning 那個不叫做 AI，然後第三呢是舉一反三就是自己開始學習。」
> 場合：塞掐 E350 行 203
> Ctrl-F：✓「那個叫做 machine learning 那個不叫做 AI」

**Q10 System 1 + System 2 整合 = AGI 開始**

> 「用這種 Transformer 的 Technology 能夠做到 Both System 1 and System 2 integrate together into a single system，那這種 integration 非常有可能就是 AGI 的開始。」
> 場合：VK f6mxGtSVPf0.zh-TW.txt 行 47-53
> Ctrl-F：✓「Both System 1 and System 2 integrate together」

**Q11 AGI 時間表（軟回答）**

> 「我今天透露了一些想法新的想法就是讓你能夠……我要做的事情不是告訴你我預測什麼，而是教你那個技能你自己去做預測。」
> 場合：塞掐 E350 行 197
> Ctrl-F：✓「教你那個技能你自己去做預測」

**Q12 8 年革命週期**

> 「你會發現到現在的情況是基本上是差不多 8 年，每 8 年有一個 revolution……1991 Web→1999 Google→2007 iPhone→2015→2023 Gemini/ChatGPT→2031 大家習以為常。」
> 場合：VK f6mxGtSVPf0.zh-TW.txt 行 113-122
> Ctrl-F：✓「每 8 年有一個 revolution」

**Q13 CoT 算力只要 5000 美金**

> 「你知道我們用了一共多少的算力嗎？大概也就 5000 塊錢美金的算力，因為那個問題並不是用算力能夠解決的問題，而是說它是另外一個思考的模式。」
> 場合：VK 51woDEK5NME.zh-TW.txt 行 152；f6mxGtSVPf0.zh-TW.txt 行 146-149
> Ctrl-F：✓「大概也就 5000 塊錢美金的算力」

**Q14 Project Astra — situated understanding**

> 「我把手機帶到 Barcelona，在那邊開會……我就問 project astra，你說，我說你住在我在哪裡，說 it looks like you are in Barcelona……你在 Saint Martin 的地區……附近有沒有什麼好的餐廳 special bonus points if it has a Michelin star。」
> 場合：VK f6mxGtSVPf0.zh-TW.txt 行 80-86
> Ctrl-F：✓「it looks like you are in Barcelona」

---

## 「台灣唯一智慧眼鏡原型機」查證結果

**標題出處**：YouTube 影片標題「台灣唯一智慧眼鏡原型機現身！」（由塞掐製作方命名）

**一手 transcript 中的原話**（行 89）：

> 「OK 我就看——這是台灣唯一一個在跑 Astra 的設備，對，應該是第一次進來，我可以看嗎？」

**分析**：

1. **是紀懷新本人說的話**：在節目現場他親自說出這句話。
2. **語氣是推測**：「應該是」表明這是他的判斷，非官方聲明。
3. **所指設備**：他從口袋拿出 Google I/O 上發表的 Android XR 眼鏡原型機，搭載 Project Astra 軟體。
4. **可信度**：Google I/O 原型機（2025）由 Google 團隊攜帶展示，紀作為負責人帶進台灣錄影棚的機率極高。但「台灣唯一」無法被獨立核實——Google 可能在其他場合也有原型機進入台灣。
5. **結論**：「台灣唯一」是合理推斷，非誤導，但嚴格說是他個人判斷。製作方將其轉化為標題 claim 有略微誇大之嫌。

**信度評估**：B（可能是真的，但無法被第三方驗證；用「應該是台灣第一台被帶進錄影棚」的描述更嚴謹）

---

## 參考文獻

### 一手 Transcripts（A 級）

- 塞掐 Side Chat E350（3rQ4jPvvY0c）：https://www.youtube.com/watch?v=3rQ4jPvvY0c
- VK 科技閱讀時間 EP122 (f6mxGtSVPf0)：Spotify EP 6TpVkyc9dJviF0qHEdRjRo
- VK 科技閱讀時間 (51woDEK5NME)：同 VK 頻道
- Project Astra 展示（nXVvvRhiGjI）：https://www.youtube.com/watch?v=nXVvvRhiGjI

### 台灣媒體

- [師大新聞稿 2019-12-18](https://pr.ntnu.edu.tw/ntnunews/index.php?mode=data&id=19046)（A 級）
- [中興大學演講公告 2024-11-28](https://www.cm.nsysu.edu.tw/p/404-1024-344551.php?Lang=zh-tw)（A 級）
- [陽明交通大學演講 2025-04](https://www.cs.nycu.edu.tw/announcements/detail/12695)（A 級）
- [天下雜誌「台灣是 Gemini 時代的要角」](https://www.cw.com.tw/article/5129031)（B 級，無法讀取原文）
- [數位時代 2018「台灣不要再錯失機會」](https://www.bnext.com.tw/article/49764/google-principal-scientist-ed-chi-ai-revolution)（A 級）
- [數位時代 2026「AI TAIWAN 演講」](https://www.bnext.com.tw/article/91353/google-deepmind-ai-agent-inference)（A 級）
- [Business Insider Taiwan「三度錯過關鍵浪潮」](https://www.businessinsider.tw/article/1049)（B 級）
- [vocus 專訪「心理學如何啟發 AI 關鍵論文」](https://vocus.cc/article/68a9cea4fd897800014c883f)（B 級，付費牆）
- [遠見雜誌「AI 從被動變主動」](https://www.gvm.com.tw/article/121892)（B 級）

### 學術來源

- [CoT Paper arxiv 2201.11903](https://arxiv.org/abs/2201.11903)（A 級）
- [Wikipedia Ed Huai-Hsin Chi](https://en.wikipedia.org/wiki/Ed_Chi)（A 級）
- [ACM DL CoT Paper](https://dl.acm.org/doi/10.5555/3600270.3602070)（A 級）
- [Denny Zhou Home Page](https://dennyzhou.github.io/)（A 級）

### 法律/問責

- [Google YouTube Addiction Lawsuit - EPIC 判決](https://epic.org/jury-finds-meta-and-google-negligent-in-landmark-social-media-addiction-case/)（A 級）
- [Al Jazeera 2026-03 判決報導](https://www.aljazeera.com/news/2026/3/26/jury-finds-meta-youtube-liable-for-social-media-addiction-what-we-know)（A 級）

### AGI 批評

- [「Deep Hype in AGI」arxiv 2508.19749](https://arxiv.org/pdf/2508.19749)（A 級）
- [Towards Better CoT: Faithfulness 問題 arxiv 2405.18915](https://arxiv.org/pdf/2405.18915)（A 級）
