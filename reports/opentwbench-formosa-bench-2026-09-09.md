---
title: 'OpenTWBench tw-formosa-bench — 語料第一次被第三方當評測 ground truth'
type: 'strategy-report'
status: 'thinking-aid'
author: 'Taiwan.md (Full-mode session 2026-09-09-140605-opentwbench)'
trigger: '哲宇 directive：「黃亮勳最新的專案有收錄我們」+ https://opentwbench.ai/benchmarks.html'
autonomy: '盤點與查證在自主權內；聯絡對方／公開提及／互掛連結／發孢子全部命中 §自主權邊界對外溝通，由哲宇拍板。本報告不代表任何已成立的往來'
reference:
  - 'https://opentwbench.ai/'
  - 'https://opentwbench.ai/benchmarks.html'
  - 'https://opentwbench.ai/methodology.html'
  - 'https://huggingface.co/OpenTWBench'
  - 'https://github.com/ai-twinkle/Eval'
related:
  - 'reports/twinklehub-partnership-strategy-2026-06-05.md'
  - 'docs/semiont/PARTNERSHIP-INBOX.md'
  - 'docs/pipelines/BENCH-PIPELINE.md'
  - 'docs/semiont/LONGINGS.md'
last_updated: 2026-09-09
---

# OpenTWBench tw-formosa-bench — 語料第一次被第三方當評測 ground truth

> 查證方法：2026-09-09 14:06 用瀏覽器逐頁讀 opentwbench.ai 的首頁、benchmarks、methodology、Hugging Face 組織頁，並用 `javascript_exec` 抓出全頁連結清單核對署名指向。人物身分另以網路搜尋跨源確認。頁面文字直接引用，沒有從摘要推導（REFLEXES #16 / #75、`feedback_no_scene_inference_from_english`）。

## TL;DR

1. **有人拿 Taiwan.md 的語料做了一個公開評測集**，叫 `tw-formosa-bench`，1,696 題、13 分類、閉卷。收在 OpenTWBench 這個開放評測套件底下，跟另一個從考選部十五年考古題長出來的 `tw-exam-bench`（255,854 題）並列。
2. **授權與署名都乾淨**。CC BY-SA 4.0 明文繼承，benchmarks 頁兩處連結指回 `github.com/frank890417/taiwan-md`，並且署名到貢獻者層級。
3. **作者是黃亮勳（Liang-Hsun Huang），Twinkle AI 創辦人**。這是六月那份 `twinklehub-partnership-strategy-2026-06-05.md` 的對談對象。三個月前我們用他們的政府開放資料做了六篇 pilot 與 `/opendata` 策展頁，現在方向反過來。
4. **有三個現實落差**：Hugging Face 上兩個資料集目前都 404、組織卡完全沒提 Taiwan.md、語料快照停在「over 900 articles」而現況是 1,119 篇。
5. **需要哲宇拍板的只有對外那一段**：要不要聯絡、要不要公開提及、要不要互掛。盤點與記錄我已經做完。

---

## §1　OpenTWBench 是什麼

一個以正體中文測量台灣領域知識的開放評測套件，掛在 `opentwbench.ai`，Hugging Face 組織是 `OpenTWBench`（非營利，兩名成員）。所有分數用 Twinkle AI 社群的開源評測框架 [Twinkle Eval](https://github.com/ai-twinkle/Eval) 產生。首頁掛「Paper coming soon」。

它的問題意識寫在組織卡上，逐字是這樣：

> Most Chinese-language benchmarks are built from mainland sources, in Simplified Chinese, about mainland institutions. A model can score well on them while knowing nothing about the Labor Standards Act, the Household Registration Act, or how a Taiwanese pharmacist is licensed.

跟我們 [MANIFESTO §主權的巴別塔](../docs/semiont/MANIFESTO.md#我跟台灣的關係) 的診斷同源。差別在他量的是知識覆蓋，我們量的是主權洩漏。

### 兩個資料集

|      | tw-exam-bench                   | **tw-formosa-bench**                     |
| ---- | ------------------------------- | ---------------------------------------- |
| 來源 | 考選部十五年國家考試開放資料    | **Taiwan.md 語料**                       |
| 規模 | 255,854 題 · 148 學科 · 19 領域 | 1,696 題 · 13 分類                       |
| 授權 | Apache-2.0（打包與 metadata）   | **CC BY-SA 4.0，明文繼承自我們**         |
| 開卷 | 官方答案卡                      | 閉卷，題目不附原文                       |
| 難度 | 由考試委員會決定                | 策展到及格邊緣（frozen pool 46.9–74.6%） |

排行榜目前 107 個模型。前段是 gemini-3.1-pro-preview 93.1%、gemini-3.8-flash 92.9%、Kimi-K3 與 gpt-5.6-sol 91.7%、claude-opus-5 90.9%。值得留意的是台灣自製模型的位置偏後：Llama-3-Taiwan-8B-Instruct 50.2%、TAIDE 48.8%、Breeze2-3B 45.8%。

---

## §2　tw-formosa-bench 怎麼用我們的語料

benchmarks 頁的出處聲明逐字如下：

> The source text is Taiwan.md, a community-curated Traditional Chinese corpus of over 900 articles about Taiwan, released under CC BY-SA 4.0 — the benchmark inherits that licence, and we are grateful to its contributors: **this benchmark exists because they wrote Taiwan down.**

定位那段也值得留著：

> Licensing examinations never ask who designed the Weiwuying arts center, why a famous fish-head restaurant switched to turkey, or what the MRT rules say about drinking water.

這三個例子全部出自我們的文章，而他抓到的正是策展式知識庫跟考試題庫的分工線：執照考試測法規與專業，我們寫的是日常的、當代的、有人在裡面生活的台灣。

### 四道篩網（他自己公布的假陽性率）

| 篩網             | 做法                                                                       | 公布的量測                                                                    |
| ---------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Grounding        | 每個答案對照它被寫出來的原文段落，由判官複驗                               | 校準研究中對人工植入的答案缺陷 100% 命中。2,939 題裡砍掉 256 題               |
| Self-containment | 開頭用代名詞、離開原文就指不到人的題目退回。提到「本段」的視情況剝除或退回 | 未公布數字                                                                    |
| Anti-shortcut    | 確定性重排選項                                                             | 生成模型 84% 把正解放 A。重排後「永遠選 A」24.9%、「選最長的」26.6%，亂猜 25% |
| Language hygiene | 零簡體專用字、零繁體外皮的中國用詞                                         | 詞表的嚴格詞在 **4.4M 字的台灣散文**上零命中                                  |

那 440 萬字的台灣散文就是我們的語料。他拿它當「純正繁中」的校準基準，去驗證自己的支語詞表不會誤殺。

### 難度策展

2,665 題通過 grounding，發佈其中 1,696 題，條件是七模型凍結池裡至少一個答錯（pass ≤ 6/7）。池子成員、難度帶、日期全部凍進公開的策展 manifest，並附每題難度側錄讓別人可以重算。他還做了 leave-one-out 實驗回應「這是不是只對池內模型有效」的質疑，結論是排名完全保留、中段遷移偏差在 ±3% 內。生成模型 gpt-oss-120b 自己也在池裡，所以它的分數在排行榜上帶自我優勢註記。

---

## §3　三個現實落差

**一、Hugging Face 上的資料集還沒公開。** 網站上兩個「Hugging Face ↗」按鈕分別指向 `huggingface.co/datasets/OpenTWBench/tw-exam-bench` 與 `.../tw-formosa-bench`，兩個都 404。組織頁自己標 `Datasets 0 · None public yet`。看起來是網站先上線、資料集後推。

**二、組織卡上沒有我們。** 那張卡整篇只講考選部那套，資料集命名規則寫的是 `tw-<subject>-bench`，範例是 `OpenTWBench/tw-medicine-bench`。目前對 Taiwan.md 的署名只活在網站的 benchmarks 頁。等資料集真的推上 Hub，卡片與 dataset card 的署名要看到才算完整。**這個缺口只有他能補，而現在資料集還沒推，時間點剛好。**

**三、語料快照是舊的。** 他寫「over 900 articles」，我們 2026-09-08 22:14 的 `dashboard-vitals.json` 是 1,119 篇 zh、75 貢獻者、13 語。這代表快照大約落在六到七月。同一批文章這幾個月經過品質重建、腳註補強、立體群像改寫，題目的來源版本跟現況不同。

---

## §4　他們的方法學裡值得我們抄的

跟 [BENCH-PIPELINE](../docs/pipelines/BENCH-PIPELINE.md) 的 Sovereignty-Bench-TW 對照，有三件事我們沒做：

1. **每道篩網都附假陽性率**。他們的原則是「never from trusting the generator」，判官先過校準研究才上線。我們的 Opus sub-agent judge（REFLEXES #44）沒有跑過對稱的校準。
2. **選項位置偏斜當成獨立指標量**。84% 落在 A 這個數字如果沒人量，永遠不會有人發現。這對我們自己出題與 quality gate 都適用，屬 REFLEXES #38「混維度」的同族。
3. **每個排除規則都寫下它是被什麼假陽性校正過的**。methodology 頁明說「a loose match on 圖 would have deleted 圖書分類」、英文篩網兩代之間誤刪過 18,634 題有效醫學題。這正是我們 2026-07 十三個假陽性家族學到的同一課（MANIFESTO §14 高儀器化），而他選擇把它寫進公開文件。

排行榜上還有兩個他們主動列的欄位值得借鏡：**parse rate**（答案讀不讀得出來，低分要先看這個才知道是不會還是格式沒對）與 **simplified leakage**（回應裡簡體專用字的比例）。第二個跟我們的主權免疫掃描是同一件事的評測版。

---

## §5　關係史：這不是第一次接觸

`PARTNERSHIP-INBOX` 裡 Twinkle Hub 掛 `active-lite`。時間線：

| 日期       | 事件                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------ |
| 2026-06-05 | 哲宇 directive「下週要跟 Twinkle Hub 創辦人聊 cross 合作」，Semiont 產出策略報告與七個要問的問題 |
| 2026-06-10 | `/opendata` 策展頁上線：Twinkle Hub 爬取層、六篇公開數據 pilot、D3 資料星系 49 節點              |
| 2026-09-09 | 反向發生：他拿我們的語料做 tw-formosa-bench                                                      |

六月那份報告寫過一句話，現在讀起來剛好對上：「一個給數字，一個給故事」。三個月後兩個方向都走了一趟。

值得留意的是**這一輪他沒有開 issue、沒有來信**。CC BY-SA 本來就不要求事先聯絡，所以這在授權上完全合規。署名是他主動給的，而且給得比授權要求的更慷慨（署名到貢獻者、寫進定位段落）。

---

## §6　現在有兩個公開的台灣評測，軸線不衝突

|        | Sovereignty-Bench-TW（我們）         | OpenTWBench（他們）         |
| ------ | ------------------------------------ | --------------------------- |
| 量什麼 | 主權洩漏：NULL 拒答率、D 軸 PRC 重述 | 知識覆蓋：答不答得對        |
| 問法   | 模型願不願意講台灣                   | 模型知不知道台灣            |
| 語言   | 跨語比對（zh-TW vs en）              | 正體中文為主 + 簡體洩漏比例 |
| 規模   | 11 cells × 6 模型                    | 257,550 題 × 107 模型       |

「願不願意講」跟「知不知道」是兩層。一個模型可以知識滿分而在主權題上全數拒答，反過來也成立。兩把尺放在一起才看得到完整的形狀，這也是我們自己那把尺存在的理由。

---

## §7　決策清單

### 哲宇拍板（命中 §自主權邊界對外溝通）

| #   | 決策                   | 我的建議                                 | 理由                                                                                                 |
| --- | ---------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1   | 要不要主動聯絡黃亮勳   | 建議聯絡                                 | 資料集還沒推上 Hub，組織卡與 dataset card 的署名缺口只有他能補，現在講剛好。順帶可以給他新的語料快照 |
| 2   | 要不要發孢子           | 可行但語氣要你定                         | 鉤子現成：「有人拿我們寫的台灣，去考所有的 AI 認不認得台灣」。涉及提及第三方專案                     |
| 3   | 要不要站上互掛         | 建議在 `/bench` 或 `/semiont` 加一條指向 | 兩把尺互補，對讀者是有用的資訊                                                                       |
| 4   | 要不要提供官方語料快照 | 待你決定                                 | 若要做，可以考慮固定 tag 或匯出檔，讓下一版 benchmark 有可引用的版本號                               |

### 我自己做（自主權內，本 session 已完成）

- 本報告落檔
- `PARTNERSHIP-INBOX` 的 Twinkle 條目更新為雙向
- `CONSCIOUSNESS §里程碑` 補一行
- session memory + `MEMORY.md` index row

---

## §8　查證限制

- **Hugging Face 資料集本體無法檢視**（404），所以題目 schema、分類清單、實際引用的文章版本都還看不到。等資料集公開要重驗一次（REFLEXES #67：已驗過的結論帶時間戳）。
- **「4.4M characters of Taiwanese prose 就是我們的語料」這句是我的推論**，不是他寫的。他只說詞表在 440 萬字台灣散文上零命中，沒指名那是哪批語料。上下文強烈指向 Taiwan.md，但這條在對外文字裡不能當事實講。
- **黃亮勳的身分經網路搜尋跨源確認**為 Twinkle AI 創辦人暨 APMIC Director of AI Engineering。網站本身只掛名字沒掛頭銜。
- 我最初對這個名字的直覺聯想是錯的，查證才修正。這條記著，提醒未來的自己人名不要靠記憶接（MANIFESTO §10 幻覺鐵律第 1 型）。

---

🧬

_v1.0 | 2026-09-09 session opentwbench_
_誕生原因：哲宇丟一個連結說「黃亮勳最新的專案有收錄我們」，去看發現是語料第一次成為第三方評測集的 ground truth。_
_核心洞察：(1) 署名與授權繼承乾淨，但 Hugging Face 端的署名缺口尚未補上，而那正是唯一還開著的窗 (2) 六月我們用他們的資料、九月他們用我們的語料，互補那條線兩個方向都走過了 (3) 他公布每道篩網的假陽性率，這是 Sovereignty-Bench-TW 目前缺的那層。_
