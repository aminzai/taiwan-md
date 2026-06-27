---
sub_topic: C — Chain of Thought + 認知心理學血脈 + AI 貢獻
article: knowledge/People/紀懷新.md
stage: 1-research
date: 2026-06-27
search_count: 20
agent: research-fanout-subagent-C
falsification_flag: true
---

# 紀懷新研究報告 — 子題 C：CoT + 認知心理學血脈 + AI 貢獻

> 目標：餵養文章核心矛盾「讓 AI 學會推理的突破不是更多算力，是一個台灣人把人類心理學搬進機器」。falsification-first，每 claim 附信度。

---

## 搜尋日誌

| #   | 查詢主題                                             | 結果品質                                                          |
| --- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| 1   | arXiv 2201.11903 作者表                              | ✅ 確認 9 作者及順序                                              |
| 2   | Ed Chi senior author / Denny Zhou role               | ⚠️ 部分；確認 Denny Zhou 為 last author + Reasoning Group founder |
| 3   | Schema theory Piaget 1960-70s 來源                   | ✅ 確認 Bartlett 1932、Piaget 1952                                |
| 4   | Herbert Simon satisficing bounded rationality        | ✅ 諾貝爾獎年份、理論細節確認                                     |
| 5   | Kahneman Tversky prospect theory history             | ✅ 1979 論文、2002 諾貝爾獎確認                                   |
| 6   | Ed Chi biography CMU PARC                            | ✅ University of Minnesota PhD；PARC 1997-2011                    |
| 7   | Jason Wei CoT origin story interviews                | ⚠️ 無直接 originator 聲明；確認 Jason Wei 為第一作者              |
| 8   | CoT paper prior work precursors 2021                 | ✅ Ling 2017、Nye 2021、Cobbe 2021 確認                           |
| 9   | Stuart Card Alan Newell CMU PARC Applied Psychology  | ✅ 確認 Applied Information-Processing Psychology Project         |
| 10  | CoT NeurIPS 2022 impact citations                    | ✅ NeurIPS 2022 確認；影響力廣泛                                  |
| 11  | Ed Chi information foraging scent PARC               | ✅ 確認 Information Scent / Foraging 研究系譜                     |
| 12  | Chain of thought o1 reasoning foundation             | ✅ o1 明確基於 CoT 原理                                           |
| 13  | Self-consistency paper 2022 authors                  | ✅ 確認 arXiv 2203.11171 作者含 Ed Chi                            |
| 14  | Emergent abilities paper 2022                        | ✅ arXiv 2206.07682 作者確認含 Ed Chi                             |
| 15  | Ed Chi Google DeepMind VP 120-person team            | ✅ 2021 Distinguished Scientist + Sr. Lead；120 人團隊            |
| 16  | Denny Zhou Reasoning Group founded Google Brain      | ✅ 確認 Denny Zhou founded Reasoning Research Group               |
| 17  | Piaget assimilation accommodation schema Bartlett    | ✅ 系譜完整確認                                                   |
| 18  | Ed Chi Denny Zhou team "Danny" neural symbolic       | ⚠️ 沒找到外部來源確認；以 transcript 為主                         |
| 19  | Jason Wei chain of thought paper credit who had idea | ⚠️ 無明確公開聲明；Denny Zhou 為 last author（慣例 senior）       |
| 20  | CoT "greedy decoding" auto-regressive explanation    | ✅ 技術機制確認                                                   |

**搜尋總計：20 次**

---

## Findings C

### C-1：CoT 是什麼——給完全不懂 AI 的新手

**Chain of Thought（思維鏈）的核心概念：**

一般語言模型的做法是「貪婪解碼」（greedy decoding）：每次只選最可能的下一個詞，一路直達答案。問題是，遇到需要多步計算的問題（如數學、邏輯推理），直接跳到答案往往出錯。

CoT 的做法：**在給 AI 看的範例裡，加入「解題過程」**，引導 AI 在回答之前先把中間推理步驟寫出來。效果類似「讓 AI 先打草稿、再給答案」。

實驗結果（Wei et al. 2022）：在三個大型模型（GPT-3 規模以上）上測試算術、常識、符號推理，準確率大幅提升。**關鍵限制：模型必須夠大（約 100B 參數以上），小模型沒效。**

**信度：高**（論文原文驗證）

**為何重要？**

1. CoT 論文（2022）是後續所有 LLM 推理研究的源頭之一，包括 Self-Consistency（2022）、Least-to-Most Prompting（ICLR 2023）、Tree of Thoughts（2023）等。

2. OpenAI o1（2024）明確「based on chain of thought」——讓模型在回答前生成一個延伸的內部思維鏈，再配合強化學習優化。o1 在 IMO 數學競賽題中，從 GPT-4 的 13% 準確率跳升到 83%。也就是說，**CoT 是今天最強推理模型的直系前身**。

3. Denny Zhou 本人（X/Twitter, 2024）補充說：「Chain of thought 如今主要指的是生成一步一步的推理——term 從 prompting 普及而來，但概念更廣。」（信度：高；來源為 Denny Zhou 個人帳號）

**歷史地位的誠實校準（反 hype）：**

CoT 並非無中生有，有幾個重要前身：

- Ling et al. (2017)：首次提出用自然語言中間步驟解數學題（需要 fine-tuning，不是 prompting）
- Nye et al. (2021)：「scratchpad」概念——訓練模型在問題後生成過程性思考
- Cobbe et al. (2021)：建立 GSM8K 數學題資料集，微調 GPT-3

Wei et al. (2022) 的貢獻在於：**用 few-shot prompting（不需重新訓練模型）就能觸發推理能力，且証明這是大模型的 emergent 能力。** 這個「prompting 不用 fine-tuning」的洞見是真正的突破。

**信度：高**（多源確認）

---

### C-2：功勞歸屬——誠實並陳，不灌大也不貶低

**論文事實（高信度）：**

- 論文：「Chain-of-Thought Prompting Elicits Reasoning in Large Language Models」
- arXiv：2201.11903，提交日期 2022 年 1 月，NeurIPS 2022 正式發表
- 9 位作者：Jason Wei（第一）、Xuezhi Wang、Dale Schuurmans、Maarten Bosma、Brian Ichter、Fei Xia、Ed H. Chi、Quoc V. Le、Denny Zhou（最後）
- 計算資源：紀懷新自述「大概 5000 塊錢美金的算力」（transcript 51woDEK5NME [52:04]，中文字幕）

**作者角色分析（信度：中，主要依慣例 + transcript）：**

學術慣例：

- **第一作者**（Jason Wei）= 主執行人，負責大部分實驗與撰寫
- **最後作者**（Denny Zhou）= 資深研究者 / 指導者，慣例上為 PI 或 team lead
- **Ed Chi（倒數第三）** = 中間作者，表示重要貢獻者但非主導執行

Denny Zhou 身份確認：他是 Google Brain Reasoning Research Group 的創辦人兼領導人，CoT 是他帶領的研究方向核心。他後來的公開演講（「Teach Language Models to Reason」系列，2022-2023 Google DeepMind）中擔任主講人，顯示他在推理研究方向的主導地位。

**Ed Chi 的實際角色（根據 transcript 自述）：**

在訪談（51woDEK5NME [56:20]–[58:22]）中，他自述：

> 「那個故事——Danny（即 Denny Zhou）是我 team 裡面的一個 researcher，他當時加入我的團隊，然後他就跑來跟我講說我想要做 reasoning 這個方面的 research……我跟他聊了一下，我覺得 neural symbolic 這個 approach 好像不大 work，我們是不是考慮用其他的方法？……我們才慢慢的討論然後發現說也許可以用這種 schema 的 concept 來做這個東西。」

這段話揭示了他的角色：**他是 Denny Zhou 的直屬主管（manager / team lead）**，在關鍵方向選擇上，他否定了 neural symbolic approach，轉向 schema-based 思路——這個 pivot 最終導向 CoT。他是**創意孵化的場域提供者與關鍵轉向的促成者**，不是論文的主執行者。

**誠實結論（高信度）：**

- 他**不是** CoT 的「唯一發明人」——這是 Denny Zhou 主導、Jason Wei 執行的研究
- 他**是** Denny Zhou 的主管，提供方向轉換的關鍵否決（neural symbolic → schema），且將認知心理學視角帶入討論
- 他的貢獻更在於：把一個 20 年累積的認知科學視角帶進研究團隊文化，讓 Denny Zhou 有可能想到 schema 這條路
- 領域地位：他當時是 Google Brain 120 人研究團隊的 Senior Lead（後升為 VP of Research），CoT 團隊在他的建制範圍內運作

**「他只是掛名嗎？」的誠實答案：** 不是掛名，但也不是論文核心執行者。他的角色更接近「思想氣候的提供者 + 關鍵方向轉向的授意者 + 認知科學血脈的攜帶者」。

---

### C-3：認知心理學血脈——最重要，文章靈魂

這是文章最深的一層，也是他本人最願意談的部分。以下逐一還原那條血脈的學術正確性。

#### 血脈鏈：Herbert Simon → Kahneman-Tversky → Piaget Schema → CoT

**第一節：Herbert Simon（赫伯特·賽門）**

- 生卒：1916-2001；CMU 教授（政治學、心理學、計算機科學）
- 諾貝爾經濟學獎：1978 年
- 核心概念：
  - **有限理性（bounded rationality）**：人的決策受到認知能力、資訊、時間的限制，無法做出「完全理性」選擇
  - **滿意度（satisficing = satisfy + suffice）**：人不求最佳解，求「夠好就行」的解。Satisficing 一詞由 Simon 在 1955 年論文「A Behavioral Model of Rational Choice」首創
- 他與 Allen Newell 合著影響深遠的《Human Problem Solving》(1972)，創立「資訊處理」視角——把人腦類比為一個資訊處理系統，問題求解是在問題空間中搜尋
- **與 CoT 的連結（信度：中；依紀懷新自述連結）**：Simon 的「問題解決 = 分步搜尋問題空間」框架，直接預示了 CoT 的「分步推理」精神。人不直接跳到答案，而是在中間步驟中搜尋解法。

**第二節：Kahneman 與 Tversky**

- Daniel Kahneman（1934-2024）、Amos Tversky（1937-1996，已過世）
- **前景理論（prospect theory）**：1979 年論文，提出人對得失的感受是不對稱的——失去 X 帶來的痛苦大於得到 X 帶來的快樂（loss aversion，損失厭惡）
- Kahneman 因此獲 2002 年諾貝爾經濟學獎（Tversky 過世未能同得）
- Kahneman 晚年著作《快思慢想》（Thinking, Fast and Slow, 2011）：提出 **System 1（直覺、快速、自動）vs System 2（理性、慢速、費力）** 思維框架
- 行為經濟學基礎

紀懷新在訪談中（51woDEK5NME [16:59]–[18:05]）明確說：「Chain of Thought 加上 fine tuning 加上 next token prediction，似乎是 the beginning of reasoning machine，也就是所謂的 System 2 thinking——就是 Tversky、Kahneman 講的啦。」他明確把 CoT 連結到 System 2 thinking 的啟動。

**信度：高**（他本人的明確自述）

**第三節：Piaget Schema 理論**

- Jean Piaget（1896-1980）：瑞士心理學家、兒童認知發展理論奠基者
- Schema（基模）：Piaget 自 1920-30 年代起發展，1952 年在《The Origins of Intelligence in Children》中系統闡述
- **Schema 定義**：組織化的知識結構，用來理解和應對外界
  - **Assimilation（同化）**：把新資訊套入現有 schema
  - **Accommodation（調適）**：遇到現有 schema 無法解釋的資訊時，修改或新建 schema
- **更早源頭**：Fredric Bartlett（英國心理學家）1932 年在《Remembering》中最早提出記憶的 schema 概念；但讓 schema 廣為人知的是 Piaget

**Learning Science / Schema Theory（60-70 年代）：**

1970-80 年代，一批教育心理學者（如 Richard Anderson 等）把 Piaget 的 schema 概念系統化為「Schema Theory」，用來解釋閱讀理解、知識習得。這就是紀懷新所說「60-70 年代的 learning science」所指的傳統。

**與 CoT 的連結（信度：高；他本人自述）：**

紀懷新（51woDEK5NME [09:47]–[10:47]）：

> 「這個 idea 事實上是從一個認知心理學，特別是在學習，我們所謂叫做 learning science 的一個學者所發出來，在 60 年代 70 年代發出來的一個 idea，叫做 schema theory。他的 idea 基本上就是說，如果你可以——一個人如果可以用一個 template 來 solve 一個 problem 的話，那也許我們也可以，我們可以用這種方法來教導機器來學習。所以 Chain of Thought 事實上是從這個 idea 剛剛開始。」

他接著確認來源：「就是 Piaget 的 schema 嗎？對，就是 Piaget 的 schema 的 idea。」

個人連結：「那個東西事實上是我在念高中的時候，大學的時候因為幫助我媽媽寫她的教育心理學方面的 PhD thesis 的時候學到的東西，所以就後來慢慢的這些東西就串在一起了。」（[10:47]）

**信度：高**（他本人一手自述）

**血脈鏈完整整理：**

```
Herbert Simon（CMU）
  ├── bounded rationality / satisficing（人不求最佳解）
  ├── Human Problem Solving: 問題求解 = 在問題空間搜尋
  └── Allen Newell（共同研究者）
      └── Stuart Card（博士生）→ Xerox PARC Applied Psychology Unit
          └── 紀懷新（加入 PARC 1997/1999）

Piaget（1920s-1952）
  └── Schema theory（60-70s learning science）
      └── 「template 解題」框架
          └── 轉化為「讓機器用 template 學習」→ CoT

Kahneman & Tversky（1979 prospect theory）
  └── System 1 / System 2（Kahneman 2011 book）
      └── 紀懷新：CoT = System 2 thinking 的起點
```

**所有這些，在紀懷新身上的交匯點：**

他高中、大學時幫媽媽寫教育心理學 PhD 論文（學到 Piaget schema）→ PARC 受 Stuart Card / Newell-Simon 傳統薰陶 → 帶著這套認知科學視角進 Google → 當 Denny Zhou 來談 reasoning 時，他能說「別用 neural symbolic，考慮用 schema」。

---

### C-4：Xerox PARC 認知科學研究根基

**Applied Information-Processing Psychology Project（AIP）的正式名稱確認：**

Stuart Card 於 1974 年加入 Xerox PARC，與 Allen Newell、Tom Moran 共同建立研究單位，正式名稱為 **Applied Information-Processing Psychology Project (AIP)**（非 "Applied Psychology Unit" 這個口語說法）。

Card 的 PhD 是在 CMU 完成（1978），導師即 Allen Newell。Newell 與 Simon 共獲 1975 年 ACM Turing Award。

**紀懷新在 PARC 的師承（transcript 確認）：**

他稱自己的老闆是「Stewart Cart」（誤植，正確是 Stuart Card）。訪談原文：「我自己的老闆那時候叫是 Stewart Cart，他是 Alan Newell（Allan Newell，即 Allen Newell）的學生。」（51woDEK5NME [05:41]）

他在 PARC 的主要研究：**Information Scent** 和 **Information Foraging**——把認知心理學（食物覓食理論 foraging theory）應用到人們如何在網路上找資訊。這就是他「跨領域橋接」的早期實踐。

**信度：高**（Wikipedia / Franklin Institute 傳記確認 Stuart Card 背景；PARC 研究確認）

---

### C-5：他的其他 LLM 貢獻——「長弧」立體化

| 研究                          | 年份         | 紀懷新角色           | arXiv      | 貢獻說明                                              |
| ----------------------------- | ------------ | -------------------- | ---------- | ----------------------------------------------------- |
| Chain-of-Thought Prompting    | 2022         | 共同作者（倒數第三） | 2201.11903 | CoT 基礎論文                                          |
| Self-Consistency Improves CoT | 2022         | 共同作者             | 2203.11171 | CoT 取樣多條推理路徑，選最一致的答案；改善貪婪解碼    |
| Emergent Abilities of LLMs    | 2022         | 共同作者             | 2206.07682 | 揭示大型模型在特定規模出現「突現能力」                |
| LaMDA / Bard / Gemini 推理    | 2021 onwards | 領導/監督            | —          | 在 Google Brain/DeepMind 120 人團隊下推進對話系統推理 |

自述補充（51woDEK5NME [44:56]）：

「從 2015 年的 sequence to sequence learning，到 2017 年的 Transformer，到後來我們 LaMDA 的 Chatbot 的 development，到 Chain of Thought、Post-training 這些東西，我們一直這種 research 的基礎都達得非常的好。」

**信度：高**（arXiv 論文作者表可公開查證）

---

### C-6：從 CoT 到 DeepThink——他怎麼定義這個延伸

訪談（51woDEK5NME [11:47]–[12:48]）：

> 「DeepThink 這方面的 research 有一點點不只是在 follow 這個 template，而是說它像你剛剛講的，它會有一些反思的動作……Chain of Thought 並沒有考慮這件事情，我當然後來也有想過，但是真正的落實的時候呢，發現事實上這些 model 可以不停的 apply 之前的 chain of thought 來一直最佳化自己的想法，這個……其中一個 definition of machine intelligence 就是它會自己這個反思自己的這個 thought pattern。」

他在 Piaget 框架下：DeepThink 的「反思」= Piaget 的 **accommodation**（調適），而 CoT 的「按 template 解題」= **assimilation**（同化）。這是他把教育心理學語言帶進 AI 的一個具體範例。（訪談 [14:55]–[15:00]：「這個在 Piaget 的認知學裡面，或者說 learning science 裡面，他會把這個東西叫做 assimilation 跟 accommodation。」）

---

## 引語庫（逐字 + [MM:SS] + 校正註）

以下引語來自 transcript 51woDEK5NME.zh-TW.txt，auto-caption 誤植嚴重，已依校正規則修正。

---

**引語 1：CoT 起源最核心自述**

> 「我跟 **Denny Zhou** 在我的 team 裡面就開始在想說可不可以用認知心理學的方法來教導機器來學習。所以這個 idea 事實上是從一個認知心理學，特別是在學習，我們所謂叫做 learning science 的一個學者所發出來，在 60 年代 70 年代發出來的一個 idea，叫做 **schema theory**。他的 idea 基本上就是說，如果你可以——一個人如果可以用一個 template 來 solve 一個 problem 的話，那也許我們也可以，我們可以用這種方法來教導機器來學習。所以 Chain of Thought 事實上是從這個 idea 剛剛開始。」

來源：51woDEK5NME.zh-TW.txt [09:47]–[10:05]

校正：

- 原文 `Danny Zhou` → **Denny Zhou** ✓（已知誤植）
- 原文 `schematotheory` → **schema theory** ✓（已知誤植）

Ctrl-F 原文比對：`可不可以用認知心理學的方法來教導機器來學習` → 可在原文找到 ✓

---

**引語 2：Piaget schema 的明確確認**

> 「就是 **Piaget** 的 schema 嗎？對，就是 **Piaget** 的 schema 的 idea。那個東西事實上是我在念高中的時候，大學的時候因為幫助我媽媽寫她的教育心理學方面的 PhD thesis 的時候學到的東西，所以就後來慢慢的這些東西就串在一起了。」

來源：51woDEK5NME.zh-TW.txt [10:31]–[10:47]

校正：

- 原文「就是皮亞傑的schema嗎」/ 「Piaget's schematal」→ 正確為 Piaget schema ✓

Ctrl-F 原文比對：`幫助我媽媽寫她的教育心理學方面的PhD thesis` → 可找到 ✓

---

**引語 3：Herbert Simon → Kahneman-Tversky → behavioral economics 連結**

> 「Herb Simon 事實上他的認知學上面的一些 research，他在 psychology 上面的一些 research，後來跟在其他認知學裡面——像這個 **Daniel Kahneman** 跟 **Tversky** 的 research，有關於 loss aversion 或者是 prospect theory 這些 idea——他基本上就是說人並不是一個完全 rational 的一個 thinker，他事實上是會叫做……satisfying，就是你只要滿足就行了的這樣子的一種思考。」

來源：51woDEK5NME.zh-TW.txt [07:45]–[08:30]

校正：

- 原文 `Daniel Cunningham` / `Dana Cunningham` → **Daniel Kahneman** ✓（已知誤植）
- 原文 `Ellen Kay` 在本段未出現，但訪談別處有 → Alan Kay ✓
- satisfying 應為 satisficing（Simon 創詞，語境明確）

Ctrl-F 原文比對：`後來跟在其他認知學裡面像這個Daniel Cunningham跟Tversky的research` → 可找到 ✓

---

**引語 4：CoT = System 2 thinking 最有力陳述**

> 「Chain of Thought 加上 fine tuning，加上這個 next token prediction，似乎是 the beginning of reasoning machine，也就是所謂的 **System 2 thinking**——就是 Tversky、**Kahneman** 講的啦。不是 Tversky，因為 Tversky 不幸地已經走了，所以 Kahneman 在後來他寫的一本書裡面，叫做 _Fast and Slow Thinking_（Thinking, Fast and Slow），就提到這個心理學裡面已經講過很多人都知道的事實，就是 System 1 跟 System 2 thinking。」

來源：51woDEK5NME.zh-TW.txt [16:59]–[17:47]

校正：

- 原文「Callahan」→ **Kahneman** ✓（已知誤植）
- 書名原文「Fast and Slow Thinking」= 正確書名《Thinking, Fast and Slow》（2011）✓
- Tversky 去世年份：1996 年（胰臟癌），此說法正確 ✓

Ctrl-F 原文比對：`chain of thought加上fine tuning 加上這個next token prediction 似乎是the beginning of reasoning machine` → 可找到 ✓

---

**引語 5：算力 $5000——反 hype 的有力彈藥**

> 「我們當時像比如說做 Chain of Thought 那篇 paper，當然我是其中作者之一，但我可以說那篇 paper 非常的 influential，但是你知道我們用了一共多少的算力嗎？大概也就 **5000 塊錢美金的算力**，因為那個問題並不是用算力能夠解決的問題，而是說它是另外一個思考的模式。所以我們當時在做那個 research 的時候，剛開始的時候基本上就是沒有經費，就是我們自己憑空想出來的東西。」

來源：51woDEK5NME.zh-TW.txt [52:04]–[52:55]

校正：無需校正

Ctrl-F 原文比對：`大概也就5000塊錢美金的算力` → 可找到 ✓

---

**引語 6：assimilation / accommodation — CoT 到 DeepThink 的 Piaget 框架**

> 「這個在 **Piaget** 的認知學裡面，或者說 learning science 裡面，他會把這個東西叫做 **assimilation** 跟 **accommodation**。所以你問了這個我還挺驚訝的，就是說跟你聊你居然會聊到這麼深，不過真的從科學家的角度來看的話，這個是一種 assimilation 跟 accommodation 的動作，所以機器的這種 machine intelligence，這種真正的機器學習似乎已經真正已經開始了。」

來源：51woDEK5NME.zh-TW.txt [14:55]–[15:16]

校正：無需校正

Ctrl-F 原文比對：`assimilation跟accommodation所以你問了這個我還挺驚訝的` → 可找到 ✓

---

**引語 7：Denny Zhou 加入 team + neural symbolic pivot 自述（功勞歸屬關鍵段落）**

> 「Danny（即 **Denny**）是我 team 裡面的一個 researcher，他當時加入我的團隊，然後他就跑來跟我講說我想要做 reasoning 這個方面的 research。然後他在我團隊之前，他做 reasoning 的時候是用一個比較 traditional 的 technique，叫做 **neural symbolic approach**。……我就跟他講說我覺得neural symbolic 這個 approach 好像不大 work，我們是不是考慮用其他的方法？然後他因為那個原因才真正就是有去——他就開始思考其他的方法，然後我們才慢慢的討論，然後發現說也許可以用這種 **schema** 的這種 concept 來做這個東西。所以那五六個月吧，……就後來發現說這種比較 template based 的 capability 可以 change 這個 auto-regressive model 的 greedy decoding 的這種很簡單的這種思維的走向的方法。」

來源：51woDEK5NME.zh-TW.txt [57:21]–[58:22]

校正：

- 原文 `Danny Zhou` → **Denny Zhou** ✓
- 原文 `Neil Sambala` / `Neurosymbolic` → **neural symbolic** ✓（上下文確認）

Ctrl-F 原文比對：`Danny是我team裡面的一個researcher他當時加入我的團隊` → 可找到 ✓

---

## 反例護欄

### 功勞別灌大

1. **不可說「紀懷新發明了 Chain of Thought」**
   - 正確說法：他是 9 人共同作者之一；第一作者 Jason Wei，last author（慣例 senior PI）Denny Zhou
   - 他的角色：認知科學視角的攜帶者 + Denny Zhou 的主管 + 從 neural symbolic 轉向 schema 的關鍵否決者

2. **不可說「他是 AI 之父 / 推理 AI 的發明人」**
   - CoT 有學術前身（Ling 2017、Nye 2021 等），不是完全的無中生有

3. **不可說「他在 CMU 學習」**
   - 正確：他在 University of Minnesota 完成 BA/MA/PhD（1994-1999）；與 CMU 的連結是透過 PARC 的 Stuart Card（CMU 博士），不是他本人就讀 CMU

4. **不可說「他在 Xerox PARC 跟 Herbert Simon 一起工作」**
   - 正確：Simon 主要在 CMU，紀懷新透過 Stuart Card 間接受 Simon-Newell 傳統影響；Simon 過世時（2001）紀懷新雖還在 PARC，但直接師承是 Stuart Card / Peter Pirolli，不是 Simon 本人

5. **「satisficing」一詞的正確解釋**
   - transcript 多次出現 "satisfying" 字幕 → 應為 **satisficing**（Simon 1955 創詞）

### 已知誤植清單（transcript 自動字幕）

| 誤植                                | 正確                                              | 出處                                     |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------- |
| Danny Zhou / Danny                  | Denny Zhou                                        | 51woDEK5NME [57:21] 等多處               |
| Daniel Cunningham / Dana Cunningham | Daniel Kahneman                                   | 51woDEK5NME [08:00]、f6mxGtSVPf0 [05:17] |
| Callahan / Cannahan                 | Kahneman                                          | 51woDEK5NME [16:59]、[19:09]             |
| schematotheory / schematotherapy    | schema theory                                     | 51woDEK5NME [09:47]、f6mxGtSVPf0 [07:09] |
| Stewart Cart                        | Stuart Card                                       | 51woDEK5NME [05:41]、f6mxGtSVPf0 [03:04] |
| Alan Newell                         | Allen Newell                                      | 51woDEK5NME [05:41]                      |
| Ellen Kay                           | Alan Kay                                          | 51woDEK5NME [03:06]（主持人語）          |
| Information Forging                 | Information Foraging                              | 51woDEK5NME [08:45]、f6mxGtSVPf0 [06:06] |
| Neil Sambala                        | neural symbolic（neuro-symbolic）                 | 51woDEK5NME [57:21]                      |
| LaMDA（Lambda 轉寫混淆）            | LaMDA（Language Model for Dialogue Applications） | 無嚴重誤植，但注意大小寫                 |
| Demons（Demis 的字幕誤植）          | Demis Hassabis                                    | 51woDEK5NME [12:48]                      |

---

## 參考文獻

### 一手 transcript（核心）

- 51woDEK5NME.zh-TW.txt（VK Podcast EP122「AI 演進、AGI 雛型、很多心理學」）— CoT 起源自述最完整
- f6mxGtSVPf0.zh-TW.txt（VK「AI 能像人類思考？」）— 輔助確認，相同故事另一版本

### 論文（已驗證）

- Wei et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. NeurIPS 2022. arXiv: [2201.11903](https://arxiv.org/abs/2201.11903)
- Wang et al. (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. arXiv: [2203.11171](https://arxiv.org/abs/2203.11171)
- Wei et al. (2022). Emergent Abilities of Large Language Models. TMLR. arXiv: [2206.07682](https://arxiv.org/abs/2206.07682)

### 傳記資料

- Wikipedia: [Ed Huai-Hsin Chi](https://en.wikipedia.org/wiki/Ed_Huai-Hsin_Chi) — 確認 U-Minnesota PhD 1999、PARC 1997-2011
- Google Research People: [Ed H. Chi](https://research.google/people/edchi/)
- Ed Chi personal site: [edchi.net](https://www.edchi.net/resume)

### 學術背景（已驗證）

- Herbert Simon: [Wikipedia](https://en.wikipedia.org/wiki/Herbert_A._Simon) — satisficing 1955、bounded rationality、1978 Nobel
- Kahneman & Tversky: Prospect theory 1979 paper; Kahneman 2002 Nobel; Tversky 1996 過世
- Piaget schema: 1952 "The Origins of Intelligence in Children"；Bartlett 1932 首提 schema 記憶概念
- Stuart Card: [Wikipedia](https://en.wikipedia.org/wiki/Stuart_Card) — CMU PhD under Allen Newell, 1974 joined PARC, AIP Project
- Denny Zhou: [Personal page](https://dennyzhou.github.io/) — founder of Reasoning Research Group, Google Brain
- Denny Zhou on CoT: X/Twitter [@denny_zhou](https://x.com/denny_zhou/status/1872366450020659483) (2024) — "chain of thought now primarily refers to step-by-step reasoning"

### 前身文獻（已驗證）

- Ling et al. (2017): 最早用自然語言中間步驟解數學題（需 fine-tuning）
- Nye et al. (2021): "scratchpad" 概念
- Cobbe et al. (2021): GSM8K 資料集，GPT-3 fine-tuning

### o1 與 CoT 延伸

- OpenAI o1 System Card. arXiv: [2412.16720](https://arxiv.org/abs/2412.16720)
- [Founding Minds: Chain-of-Thought Reasoning: The Magic Behind the o1 Model](https://www.foundingminds.com/chain-of-thought-reasoning-the-magic-behind-the-o1-model/)
