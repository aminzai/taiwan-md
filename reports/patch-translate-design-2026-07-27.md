---
title: '章節級 diff-patch 引擎 — 2026-07-27'
description: '哲宇 directive：stale 部分可以比較 diff 後處理 patch。新工具 patch-translate.py（H2 章節對齊 + 只重翻被碰章節）+ 全站 642 篇 stale 統計 + 與整篇重翻耗時對照'
type: 'pipeline-report'
status: 'shipped'
---

# 章節級 diff-patch 引擎 — 2026-07-27

> **Session**：2026-07-27，哲宇 directive「stale 部分可以比較 diff 後處理 patch」
> **新工具**：[`scripts/tools/lang-sync/patch-translate.py`](../scripts/tools/lang-sync/patch-translate.py)
> **接線**：[`scripts/tools/lang-sync/babel-dispatch.py`](../scripts/tools/lang-sync/babel-dispatch.py) `process_task()` 對 `status=="stale"` 先試 patch，exit 2 fallback 全文
> **驗證產物**：`/tmp/patch-test/`（不寫 `knowledge/`，僅本報告 + 工具本體 + babel-dispatch.py 的接線進 repo）

---

## TL;DR

- **問題實測**：全站 642 篇 stale，抽樣 14 對的改動比例中位 2.8%（7 行/204 行），78% 改動 <10%。既有 dispatcher 對 stale 一律整篇重翻——為 3% 的改動燒 100% 算力。
- **新工具核心**：以 **H2 章節**為對齊單位（不是行）。讀譯文 `sourceCommitSha` → `git diff --unified=0` 取被改動的行號範圍 → 對照目前 zh 的 H2 邊界判定「哪些章節被碰過」→ 只把被碰章節的 zh 全文送模型 → 組回全文、未碰章節位元組不動。
- **兩道硬性 fallback 閘門**（都 exit 2，呼叫端退回既有全文重翻路徑，不是失敗）：章節數不對齊、被碰章節佔全文字元數 >50%。
- **全站 642 篇 stale 實測**（chapter-alignment 邏輯本身跑一遍，非抽樣）：**64.6%（415 篇）可以 patch**；退回全文的三大原因是章節數不對齊 16.7%、改動過大 17.1%、sha 不可解析 1.4%。
- **2 對實跑**（`openrouter:nvidia/nemotron-3-ultra-550b-a55b:free`，輸出到 `/tmp/patch-test/`）：三重驗證全過、未改動章節與原譯文**位元組完全相同**。耗時對照高度依「被碰章節數」而非字元占比——1 章節 7.2s（vs 站上同語言全文重翻均值 ~150-246s，省 ~95%+），4 章節 148.8s（跟均值幾乎打平，省不到）。**誠實揭露**：n=2 的真實計時樣本太小，不足以給出精確的「平均省 X%」數字，下方§六用兩個情境給範圍而非單一數字。
- **一個過程中發現、非本工具引入的既有盲點**：跨文章的內部連結（`[大罷免](/history/大罷免)` 這類 zh 相對路徑）目前的翻譯引擎（`translate.py` / `structured-translate.py`，本工具的章節翻譯邏輯沿用同一條 HARD RULE「URL 保留原樣」）都不會把它在地化成 `/en/history/...` 格式的 EN 網址——這是既有 `prepare-batch.py` 的 wikilink 解析只涵蓋 `[[wikilink]]` 語法、不涵蓋一般 markdown 連結的既有缺口，`CRON-ROUTINE.md` 已記載「broken cross-link」為已知可接受狀況（下一輪自然解決）。三重驗證不檢查這件事，不影響本工具的 gate 判定，但如實記錄。

---

## 一、為什麼是 H2 章節，不是行級 patch

哲宇的 directive 提到既有 `scripts/tools/lang-sync/diff-patch-prepare.py`——它已經做了行級 diff + Sonnet sub-agent 判斷怎麼 patch 的設計。**本工具刻意不沿用它的執行路徑**，理由：

1. **燒 Claude token**：diff-patch-prepare.py 的下游是把整份 diff 丟給 Sonnet sub-agent 判斷怎麼改，直接違反本專案「不用 Claude token 翻譯」的原則——babel-dispatch 的四條產線全部走 OpenRouter free tier / 本機 Ollama，沒有一條經過 Claude。
2. **行對行映射跨語言不可靠**：中文一行可能對應譯文兩行、半行，或因為 reflow 完全找不到對應行。行級 diff 天生假設「行」是穩定的翻譯單位，跨語言時這個假設不成立。
3. **H2 章節邊界本來就是既有的對齊單位**：`verify-translation.py` 第 10 項檢查就是在比 zh 與譯文的 `## ` 數量（±1 容忍），代表這條專案已經公認「章節數大致對齊」是翻譯品質的訊號之一。把它升格成 patch 的**硬性**對齊條件，是延伸既有判準，不是發明新概念。

代價：章節是比行粗的顆粒度，一個章節裡出現一個字的改動，也要整章重翻（見下方§四的 ja/瘂弦.md 案例——6 個單字級標點修正，因為分散在 5 個不同章節，被碰章節占比高達 52.4%，超過門檻 fallback 回全文）。這是刻意的取捨：章節內部的行級對齊在跨語言場景不可靠到不值得做，寧可在「改動很分散」時整篇退回全文，也不要冒行級錯位的風險把一句話塞進錯的段落。

---

## 二、Algorithm

```
1. 讀譯文 frontmatter 的 sourceCommitSha (old_sha)
   → 缺 / pre-toolkit / 格式不對 / git 裡找不到 → exit 2

2. git diff --unified=0 <old_sha>..HEAD -- knowledge/<zh_path>
   → 用 --unified=0（零 context 行）取精確的 hunk 新檔行號範圍，
     避免 context 行把 hunk 洩到相鄰未改動章節

3. 用「目前」zh 的 H2 邊界切章節（intro + 每個 `## ` 各一章）
   同樣邏輯切譯文（intro + 每個 `## ` 各一章）
   → 章節數（含 intro）與 H2 數兩者都要相等，否則 exit 2

4. 對照 hunk 行號範圍 vs 每個章節的行號範圍，判定哪些章節被碰過
   frontmatter 是否需要重翻，不是看行號重疊，是看 title/description/
   tags/subcategory 這幾個「唯一會送模型」的欄位語意上是否真的變了
   （old zh frontmatter vs 目前 zh frontmatter）——避免 date/image
   這類機械複製的 passthrough 欄位變動也觸發一次 LLM 呼叫

5. 被碰章節字元數 / 全文字元數 > 50% → exit 2（patch 沒有效益，退全文）

6. 只把被碰章節的 zh 全文送模型：
   - 一般章節：H2 heading + 內文一起送，帶語言 guide TL;DR
     + 前後章節既有譯文各 200 字當語境（讓銜接不突兀）
   - 含 [^n]: 定義行的章節（多半是「## 參考資料」）：heading + prose
     + 所有 footnote {n,title,desc} 包進同一次 JSON 呼叫（見下方§三的
     <100 字元誤判 refusal 問題）

7. 組回全文（未碰章節的行原封不動）→ npx prettier --write →
   既有三重驗證（verify-translation.py / cjk-leak-check.py /
   article-health.py --profile=pre-commit）→ 任一 fail 不寫檔、exit 1；
   全過才寫檔、exit 0
```

---

## 三、實作中發現的三個真問題（不是紙上設計）

1. **`body_lines[0]` phantom 行陷阱**：對 raw string 做 `content[end+4:]` 式切片再 `.splitlines()`，字串開頭殘留的換行符號會在結果裡產生一個不對應任何真實行的空字串，讓後續所有「body_lines[j] ↔ 全檔行號」的算法差一行——這種一行之差在行號比對場景是致命的（會把 hunk 誤判到相鄰章節）。改成先對整檔 `.splitlines()` 再切片列表，徹底避開這個陷阱（`parse_frontmatter_and_body()`）。

2. **`OpenRouterBackend` 的 <100 字元「疑似 refusal」啟發式對章節顆粒度是新風險**：`structured-translate.py` 翻整篇時每個 chunk 通常有上千字元，這個啟發式幾乎不會誤觸；但 patch 只翻**一個**章節，如果那個章節剛好是「## 參考資料」這種幾乎只有標題 + 腳註列表的短章節，單獨翻標題（十幾字元）極容易被誤判成拒答。解法：把 heading + prose + 所有 footnote 條目包進**同一次** JSON 呼叫（`translate_footnote_chapter()`），輸出天生比較長，穩定閃過這個誤判——這是本工具沒有直接重用 `structured-translate.translate_footnotes()`（它會把 heading 拆開單獨處理）的原因。

3. **測試環境的 lang 誤判連帶炸出一個假陽性 gate fail**：第一次實跑時 `article_health` 回報 `hard: 2`，其中一項是 zh-TW 專屬的「半形括號應全形」規則打在一段英文譯文上（因為 `/tmp/patch-test/xxx.md` 這種路徑沒有 `knowledge/<lang>/` 字樣，`lib/article_health/langs.py` 靠路徑字串猜語言，猜成 `zh-TW`）。修法跟 `structured-translate.py` pilot 報告記載的作法一致（symlink 讓路徑「lexically」落在 `knowledge/<lang>/` 底下），但這次額外把同一個 symlink 也套用到 `article-health.py` 的呼叫（原本 pilot 只套用在 `verify-translation.py` 的 ratio-check），因為兩邊都會被路徑字串誤導，只修一邊會漏一個。**這是測試方法論的修正，不是工具邏輯的 bug**——babel-dispatch 呼叫時 `--out` 永遠是真的 `knowledge/<lang>/...` 路徑，不會踩到這個陷阱。

---

## 四、Dry-run 章節判定結果（3 對，涵蓋三種情境）

| zh / lang                   | 改動                             | 章節判定                                                 | 結果                                                  |
| --------------------------- | -------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- |
| `History/民主化.md` → en    | 尾端「相關主題」清單加 1 行      | 1/11 章節被碰（`## 相關主題`），231/5692 字元 = **4.1%** | 判定 patch，實跑驗證見§五                             |
| `People/鄭愁予.md` → en     | 4 處段落內容更新                 | 4/14 章節被碰，3141/9512 字元 = **33.0%**                | 判定 patch，實跑驗證見§五                             |
| `Food/台灣水果王國.md` → es | （既有 es 譯文結構已與 zh 分岔） | zh 10 個 H2、es 譯文 **28** 個 H2                        | **exit 2 fallback**（章節數不對齊，硬性閘門正確攔下） |

第三個案例是真實資料裡挖出來的——這篇 es 譯文的章節結構跟目前 zh 源已經徹底分岔（可能是舊版翻譯或不同世代 pipeline 產物），硬性閘門正確判定「不該 patch」而不是憑空猜章節怎麼對應，退回全文重翻是唯一安全的選擇。

另外抓到一個**真實但反直覺**的案例：`People/瘂弦.md` → ja，diff 只有 6 處**單字級**標點修正（全形破折號「——」改冒號「：」，MANIFESTO §11 書寫節制的收斂），但這 6 處分散在 9 個章節裡的 5 個，被碰章節占比算到 **52.4%**，超過 50% 門檻，正確地 fallback 回全文重翻。這暴露章節顆粒度 ratio 的一個已知限制：**「改動有多分散」跟「改動有多大」是兩件事**，本工具目前只看前者（被碰章節數 × 各章節大小），沒有另外量測「hunk 本身改了幾個字元」。下方§七會列為後續風險。

---

## 五、實跑驗證（2 對，`openrouter:nvidia/nemotron-3-ultra-550b-a55b:free`，輸出 `/tmp/patch-test/`）

| zh / lang                | 被碰章節                    | 三重驗證                                                                    | 未碰章節位元組比對                           | 耗時       |
| ------------------------ | --------------------------- | --------------------------------------------------------------------------- | -------------------------------------------- | ---------- |
| `History/民主化.md` → en | 1/11（`## Related Topics`） | verify-translation fails=0 / cjk-leak flagged=false / article-health hard=0 | 10/10 章節（含 intro）**byte-identical**     | **7.2s**   |
| `People/鄭愁予.md` → en  | 4/14                        | verify-translation fails=0 / cjk-leak flagged=false / article-health hard=0 | 10/10 未碰章節（含 intro）**byte-identical** | **148.8s** |

兩對都用 Python 直接比對「按 H2 切開後逐章節字串是否相等」驗證未碰章節，不是肉眼抽查——結果精確符合預期（只有被判定為 touched 的章節內容不同，其餘每一個字元都沒有變動）。

**耗時對照基準**：從近 5 個正在跑的 `babel-unified-*` run 的 `report.jsonl` 抓 `ok=true` 的整篇重翻耗時，`en` 語言均值 152.1s（n=3，樣本小），跨全部語言混合均值 246.2s / 中位數 169.1s（n=69）。

- 1 章節案例：7.2s vs ~152-246s 基準，**省 95%+**
- 4 章節案例：148.8s vs ~152-246s 基準，**幾乎打平，沒省到**（甚至可能因為 4 次獨立 LLM round-trip 各自的固定開銷，比整篇一次翻完還略慢）

**誠實結論**：patch 的效益主要跟「被碰章節數」掛鉤，不是跟「字元占比」線性相關——每個被碰章節是一次獨立的 LLM 呼叫（含最多 3 次重試),有固定的往返開銷。全站 642 篇 stale 裡，可 patch 的 415 篇平均被碰 **2.91 個章節**（見下方§六），介於本次兩個實測樣本之間；用兩點粗略內插，415 篇的平均節省落在**「顯著但不到 95%」**的區間，精確數字需要更大樣本（n=2 無法給出可信的單一百分比，見§七後續風險第一條）。

---

## 六、全站 642 篇 stale 統計（非抽樣，跑一遍完整章節對齊邏輯）

```
patchable（會走 patch 路徑）: 415 / 642 = 64.6%
fallback（exit 2，退回既有全文重翻，不是失敗）: 227 / 642 = 35.4%
  - 章節數不對齊（chapter_count_mismatch）: 107 / 642 = 16.7%
  - 改動過大（ratio_too_large，被碰章節 >50%）: 110 / 642 = 17.1%
  - sourceCommitSha 不可解析（sha_not_resolvable，多半是 rebase/squash）: 9 / 642 = 1.4%
  - 無 diff（極少數 edge case）: 1 / 642 = 0.2%
```

**415 篇 patchable 的章節觸碰分布**：被碰章節字元占比均值 21.2%／中位 17.1%；被碰章節數均值 2.91／全文章節數均值 11.73（≈ 觸碰 25.2% 的章節數）。

**預估節省**（基於§五兩個真實計時點做保守 / 樂觀兩種情境，不假裝有更精確的數字）：

| 情境                                         | 假設                                                                       | 415 篇 patchable 的預估耗時 vs 全文重翻 415 篇 |
| -------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------- |
| 保守（貼近 4 章節樣本）                      | 多數文章跟均值 2.91 章節的真實開銷接近 148.8s 樣本                         | 節省有限，可能只有 10-30%                      |
| 樂觀（貼近 1 章節樣本 + 章節數與耗時亞線性） | 固定開銷佔比隨章節數增加而攤薄，且 78% stale 原本改動 <10%（哲宇原始抽樣） | 節省 60-85%                                    |

227 篇 fallback 的耗時跟今天完全一樣（本工具在它們身上只多花一次 `git diff` + 章節切分的本地運算，不到 1 秒，沒有 LLM 呼叫，等於零成本安全網）。

---

## 七、Fallback 條件總表

| 條件                                                                      | exit code | 對應行為                                                                |
| ------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------- |
| 找不到既有譯文 / frontmatter 無法解析                                     | 2         | 呼叫端全文重翻                                                          |
| `sourceCommitSha` 缺失 / `pre-toolkit` / 格式不對 / 在 git 裡找不到       | 2         | 同上                                                                    |
| zh 與譯文的章節數（含 intro）或 H2 數不相等                               | 2         | 同上（§四 es/台灣水果王國.md 案例）                                     |
| 沒有 diff / hunk 無法解析 / hunk 沒對應到任何章節或 frontmatter           | 2         | 同上                                                                    |
| 被碰章節字元數 / 全文字元數 > 50%                                         | 2         | 同上（§四 ja/瘂弦.md 案例）                                             |
| 章節翻譯重試 3 次後仍有驗證問題                                           | 1         | 不寫檔，呼叫端走既有 gate-fail 處理（記入 fail_counts，同一輪不再重試） |
| frontmatter 驗證不過                                                      | 1         | 同上                                                                    |
| 組裝後 H2 數與 zh 不符（構造上幾乎不可能，防禦性檢查）                    | 1         | 同上                                                                    |
| 三重驗證（verify-translation / cjk-leak-check / article-health）任一 fail | 1         | 同上                                                                    |

---

## 八、後續風險

1. **n=2 的真實計時樣本太小**：§五的節省估計區間很寬（10-85%），需要在 babel-dispatch 接線跑起來、累積 report.jsonl 裡標了 `engine=patch` 的真實記錄後，用幾十筆重新估計，不是這次兩篇就能定案的數字。

2. **章節顆粒度對「分散但微小」的改動不友善**（ja/瘂弦.md 案例實測）：6 個單字級標點修正，因為分散在 5 個章節裡，觸發 >50% fallback，改成整篇重翻反而燒更多算力去翻沒變的內容。真正的改進方向是**額外量測「hunk 本身的字元變動量」**（不只是被碰章節的字元數），對「多章節但每章節只變 1-2 個字元」的案例放寬 fallback 門檻——這是一個新的判準維度，不是調整現有的 0.5 常數就能解決，需要另外設計，這次沒做（範圍控制）。

3. **章節數不對齊占 16.7%，比預期高**：這代表全站有相當比例的既有譯文，其 H2 結構已經跟目前 zh 源分岔（舊版翻譯 / 不同世代 pipeline / 人工編輯過的譯文）。這批文章即使 patch 引擎再怎麼優化都吃不到——它們需要的是**先把譯文結構拉回與 zh 對齊**（可能是一次性全文重翻，之後才能進入 patch 循環），本工具的硬性閘門正確識別了這批文章，但沒有解決它們。

4. **跨文章內部連結在地化缺口**（§〇 TL;DR 已提及，這裡重申風險等級）：本工具的章節翻譯邏輯沿用 `structured-translate.py` 的 HARD RULE「URL 保留原樣」，對於 zh 相對路徑的內部連結（非 `[[wikilink]]` 語法）不會在地化成 `/en/...` 格式。這是**既有引擎共有的行為**，不是本工具引入的退化，但值得注意：patch 路徑「重翻」的章節如果剛好包含這類連結，寫出來的連結格式跟同一篇文章裡其他（舊、正確在地化的）章節不一致。三重驗證目前不檢查這件事。

5. **backend 免費額度的效能變異**：本次實跑兩個樣本的每章節耗時差異很大（單章節案例的 chapter 呼叫本身很快，多章節案例平均每章節約 37s），可能是 OpenRouter free tier 的排隊/限速造成的雜訊，不完全是章節本身複雜度的訊號。

---

## 九、接線

`babel-dispatch.py` 的 `process_task()` 對 `status == "stale"` 的任務，在既有的 `engine="whole"`／`engine="structured"` 分派**之前**先試 `patch-translate.py`：

- exit 2 → log 一行、fallback 到既有全文路徑（`whole` 或 `structured`，依 `--engine` 參數不變）
- exit 0 / exit 1 → 直接把 `patch-translate.py` 的 subprocess 結果當作 `proc`，沿用下游既有的 prettier / heal-passthrough / verify_one / disposition / commit 全套邏輯（不重寫，只是多一個上游來源）
- 新增 `--no-patch` CLI 旗標可整條產線停用這個路徑（回到今天的行為）
- log 行新增 `engine=patch|whole|structured` 標記，方便之後從 `master.log` / `report.jsonl` 統計 patch 命中率與耗時

**沒有重啟正在跑的四條產線**——它們跑完自然過渡，下次重啟才吃到新程式碼（哲宇既有規範）。

---

## 十、驗證方法論備忘（給下次維護的人）

- 未碰章節「byte-identical」驗證：把譯文按 `^## ` 切開（intro 算一塊），逐塊字串相等比對，不是人工抽查。
- 三重驗證在 `/tmp` 路徑跑會踩兩個坑：`verify-translation.py` 的 ratio-check 對絕對路徑 `.relative_to(REPO)` 會炸；`article-health.py` 的 lang 偵測靠路徑裡有沒有 `knowledge/<lang>/` 字串。兩個都要用同一條 symlink 鏈路修（`_verify_arg_path()`），只修一邊會漏一個──本次真的因為只修第一個而在实跑時炸出一次假陽性 gate fail（§三第 3 點）。
- 全站統計腳本（642 篇跑一遍完整章節對齊邏輯，非抽樣）沒有進 repo（一次性分析用途），邏輯已經是 `patch-translate.py` 本體函式的直接呼叫，之後要重跑可以直接 import 該模組。
