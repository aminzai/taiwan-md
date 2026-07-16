# Article-health 儀器擴充校準報告

日期：2026-07-16
範圍：`ai-residue` (新) / `attribution-vague` (新) / `prose-health` Tier 4 (a)-(f) / `score-budget` 真閘門化 / `memory-diary` profile

全站語料：855 個 zh-TW `knowledge/*.md`（`--all` 掃描結果）

---

## 1. prose-health 全站 score 分佈（改動前 vs 改動後）

比對方式：把改動前的 `prose_health.py` / `article-health.py` / `article-health.config.toml`
（`git show HEAD:...`）複製到隔離目錄，對**同一份現有語料**分別跑
`--all --check=prose-health --output=json --quiet`，再比對兩份 JSON 的 score。

| 指標                                    | 數值        |
| --------------------------------------- | ----------- |
| 掃描檔案數                              | 855         |
| score 完全不變的檔案                    | 827 (96.7%) |
| score +1 的檔案                         | 27          |
| score +2 的檔案                         | 1           |
| delta 中位數                            | 0           |
| delta 平均                              | 0.034       |
| delta 最大值                            | 2           |
| 全站 pass(≤3) 改動前                    | 517/855     |
| 全站 pass(≤3) 改動後                    | 513/855     |
| 全站因 Tier4 從 pass(≤3) 翻 fail 的檔案 | 4（見下）   |

全站翻 fail 的 4 篇（score 3→4，budget=3 情境下）：

- `knowledge/Technology/東亞文字輸入法.md`
- `knowledge/Art/台灣漫畫.md`
- `knowledge/People/陳映真.md`
- `knowledge/Food/客家飲食文化.md`

這 4 篇不在「近期高品質文章 15 篇」抽樣範圍內，且比例很小（4/855 ≈ 0.5%），
是新增 Tier4(a)-(f) 六個維度的合理副作用（本來就會讓少數壓線在 3 分的文章
多算 1 分過線）。分佈本身健康：96.7% 檔案完全不受影響，最大增量只有 2 分。

---

## 2. 近期高品質文章 15 篇抽樣（`git log --since=2026-06-15`）

篩選：`git log --since=2026-06-15 --name-only -- knowledge/` 去重後取前 15 篇
zh-TW 正文（排除譯文 `.en/.ja/.ko/.es/.fr.md` 與 Hub）。

| 檔案                                        | 改動前 score | 改動後 score | delta |
| ------------------------------------------- | -----------: | -----------: | ----: |
| knowledge/History/台灣民主轉型.md           |            4 |            4 |     0 |
| knowledge/History/民主化.md                 |            8 |            8 |     0 |
| knowledge/Society/台灣政治環境與選舉制度.md |            3 |            3 |     0 |
| knowledge/Society/社會運動與公民參與.md     |            3 |            3 |     0 |
| knowledge/History/大罷免.md                 |            3 |            3 |     0 |
| knowledge/Lifestyle/吉祥物.md               |            1 |            1 |     0 |
| knowledge/History/史前時代與原住民.md       |            3 |            3 |     0 |
| knowledge/Culture/台灣YouTuber產業與文化.md |            3 |            3 |     0 |
| knowledge/Culture/無名小站.md               |            3 |            3 |     0 |
| knowledge/People/尊.md                      |            1 |            1 |     0 |
| knowledge/People/阿神.md                    |            3 |            3 |     0 |
| knowledge/Culture/巴哈姆特.md               |            5 |            5 |     0 |
| knowledge/People/Howhow.md                  |            2 |            2 |     0 |
| knowledge/People/蔡阿嘎.md                  |            4 |            4 |     0 |
| knowledge/Economy/AAMA台北搖籃計畫.md       |            3 |            3 |     0 |

**結論：中位數 delta = 0（遠低於 ≤1 門檻），平均 delta = 0，最大 delta = 0，
15 篇中沒有任何一篇因新維度 pass→fail 翻轉。** 通過驗收條件。

---

## 3. ai-residue 全站掃描

| check      | 全站 hits | 命中檔數 | top 10 檔案 |
| ---------- | --------: | -------: | ----------- |
| ai-residue |         0 |        0 | （無命中）  |

**校準判斷**：855 篇全零命中。這符合預期——鐵證級 AI 殘留物（URL 追蹤參數 /
citation token / PUA 字元 / 對話殘留句）本來就是低頻事件，且既有編輯流程
已經會擋掉最明顯的案例。零命中不代表偵測器失效，已用合成測試檔驗證四類
pattern 全部正確觸發：

合成測試（`/private/tmp/.../residue_test/`）注入 7 處已知殘留，結果 7/7 全部
命中且分類正確：

- `utm_source=chatgpt.com` URL 殘留 → 命中
- `referrer=grok.com` URL 殘留 → 命中
- `citeturn0search3` 引用佔位殘碼 → 命中（整個 token 一次比對，見下方調整）
- `turn2search5` 引用佔位殘碼 → 命中
- U+E012（PUA 字元）→ 命中
- 「以下是修改後的版本」對話殘留 → 命中
- 「希望這對你有幫助」對話殘留 → 命中

**校準調整**：原始 regex `turn\d+search\d+|citeturn\d+` 會把
`citeturn0search3` 拆成「citeturn0」+ 未比對的殘留「search3」兩截。收緊為
`(?:cite)?turn\d+search\d+|citeturn\d+`，讓帶 cite 前綴的完整 token 一次
比對到，不影響判定結果（兩種切法都會 HARD 命中），純粹讓 violation 訊息
更準確。誤報率：0/7（合成測試裡沒有誤殺任何正常文字）。

**沒有調整閾值**——目前的 regex 集合維持題目給的四類 pattern 原樣（(b) 的
`turn\d+search\d+` 從單一 `\d` 放寬成 `\d+` 以涵蓋多位數索引，屬於題目允許的
工程判斷，已在程式碼註解說明）。

---

## 4. attribution-vague 全站掃描

### 第一輪（未收緊）

| check                  | 全站 hits | 命中檔數 |
| ---------------------- | --------: | -------: |
| attribution-vague (v1) |         9 |        8 |

Top 命中檔案：
knowledge/Society/台灣省籍矛盾.md(2) / knowledge/Society/颱風假.md(1) /
knowledge/Nature/台灣海洋生態與珊瑚礁保育.md(1) / knowledge/People/楊丞琳.md(1) /
knowledge/Food/台灣素食文化.md(1) / knowledge/Food/茶文化.md(1) /
knowledge/Food/營養午餐.md(1) / knowledge/Geography/台灣溫泉地景.md(1)

**人工判斷 3 個 hit（第一輪）**：

1. `台灣省籍矛盾.md` L104「中研院研究員**王甫昌**的研究指出，1970 年代...」
   → **假陽性**。有具名人物（王甫昌）+ 機構（中研院），只是「中研院」是
   縮寫，沒有匹配到 `_RE_INSTITUTION` 清單裡的全稱「研究院」。
2. `knowledge/Geography/台灣溫泉地景.md` L36「**台大地質科學系宋聖榮教授**的
   研究顯示，台灣地熱蘊藏量高達 33.64 GW」→ **假陽性**。同樣是具名教授 +
   機構縮寫（台大），縮寫沒進機構後綴清單。
3. `knowledge/Society/颱風假.md` L68「他們面臨的處境比**數據顯示**的更複雜」
   → **假陽性**。這裡「數據顯示」是被名詞化的比較句賓語（「比...更複雜」），
   不是「數據顯示，X」這種鋪墊句型，語法角色完全不同。

**誤報率：3/3 抽樣 = 100%（明顯超過 30% 門檻）→ 當場收緊。**

### 收緊動作

在既有「同段落腳註」「50 字窗口引號/機構全稱」判準之外，加入兩條句法判準：

1. 命中詞緊接在「的」**前面**（`X的研究顯示/指出`）→ 放行。「的」前面
   語法上一定是具體的所有格主詞（人名/頭銜/機構，含縮寫），從寬視為已具名。
2. 命中詞緊接在「的」**後面**（`研究顯示的...`）→ 放行。這代表整個片語被
   名詞化成句子的比較/修飾對象，不是引用鋪墊句型。

### 第二輪（收緊後）

| check                  | 全站 hits | 命中檔數 | top 檔案 |
| ---------------------- | --------: | -------: | -------- |
| attribution-vague (v2) |         5 |        5 | 見下     |

- knowledge/Nature/台灣海洋生態與珊瑚礁保育.md (1)
- knowledge/People/楊丞琳.md (1)
- knowledge/Food/台灣素食文化.md (1)
- knowledge/Food/茶文化.md (1)
- knowledge/Food/營養午餐.md (1)

**人工判斷 3 個 hit（第二輪）**：

1. `台灣海洋生態與珊瑚礁保育.md` L133「台灣白海豚的基因研究顯示，牠們與
   中國大陸的中華白海豚已經分化為不同族群」→ **真陽性**。沒有具名研究/
   團隊/期刊，也沒有腳註，是一個應該可查證卻沒給來源的物種分類學論斷。
2. `knowledge/People/楊丞琳.md` L72「但研究顯示那是沒有因果的都市傳說」→
   **真陽性**。用來反駁一個流傳說法，但反駁本身完全沒引用來源，讀者無從
   查證這個「研究」是誰做的。
3. `knowledge/Food/台灣素食文化.md` L66「研究顯示，適當的素食能降低心血管
   疾病、糖尿病等慢性疾病的風險」→ **真陽性**。典型健康功效論斷缺乏來源，
   正是這個 pattern 設計要抓的案例。

**誤報率（第二輪）：0/3 抽樣 = 0%**。收斂後的誤報率遠低於 30% 門檻，維持
現狀不再收緊。

**已知取捨（寫在 plugin docstring 裡）**：收緊規則 1（`X的`+phrase 放行）
連帶會放掉「台灣政治學者的研究顯示」這種「的」前面是泛稱（不是具名個體）
的案例——這是刻意的「難判就從寬」選擇：假陽性（誤傷具名段落）比假陰性
（漏掉泛稱偽裝成有主詞）更傷這個工具的可信度，優先降假陽性。

---

## 5. score-budget 真閘門化（第 4 項的必要配套修正）

在讀 `runner.py` + `article-health.py` 判斷 `fail_on = "score-budget"` 怎麼判時
發現：**這個分支從來沒有真的檢查過 score**——舊碼是
`if fail_on == "score-budget": return 1 if total_hard else 0`，跟
`fail_on == "hard"` 完全同義；`prose_health.py` 訊息裡寫的「≤ 3 = pass」
只是一句話，從未被任何程式碼實際拿來當閘門判準（`REWRITE-STAGE-3-VERIFY.md`
§4 寫「quality-scan ≤ 3 + build」自動驗證，但這個自動驗證其實從未真正生效）。

修正（`scripts/tools/article-health.py`）：

- 新增 `_resolve_prose_health_options` / `_resolve_score_budget` /
  `_prose_health_score` 三個 helper，鏡射 `runner._resolve_options` 的
  options 解析順序（profile override > config override > 預設 3）。
- `_effective_passed` 對 `fail_on == "score-budget"` 新增真正的
  `score ≤ budget` 判斷（原本落到跟 `fail_on == "hard"` 一樣的分支）。
- `main()` 的 exit code 分支同步换成真的逐篇判斷，不再是 `total_hard` 假閘門。
- JSON / human 輸出都補上 `score_budget` 欄位方便除錯。

這個修正只影響 `fail_on == "score-budget"` 這一條路徑（目前只有既存的
`rewrite-stage-3` 跟新增的 `memory-diary` 兩個 profile 使用），完全不影響
`pre-commit` / `ci-deploy` / `release-pr` / `dashboard`（它們用
`fail_on = "hard"` / `"warn"` / `"never"`，邏輯路徑沒變）。

驗證（合成文章，score=7）：

| profile         | budget | 訊息                                 | passed | exit code |
| --------------- | -----: | ------------------------------------ | ------ | --------: |
| rewrite-stage-3 |      3 | `prose-health score: 7 (≤ 3 = pass)` | False  |         1 |
| memory-diary    |      8 | `prose-health score: 7 (≤ 8 = pass)` | True   |         0 |

---

## 6. 修改/新增檔案清單

- `/Users/cheyuwu/Projects/taiwan-md/scripts/tools/article-health.config.toml`（修改，新增 `[profiles."memory-diary"]`）
- `/Users/cheyuwu/Projects/taiwan-md/scripts/tools/article-health.py`（修改，score-budget 真閘門化）
- `/Users/cheyuwu/Projects/taiwan-md/scripts/tools/lib/article_health/checks/prose_health.py`（修改，score_budget 選項 + Tier4 (a)-(f)）
- `/Users/cheyuwu/Projects/taiwan-md/scripts/tools/lib/article_health/checks/ai_residue.py`（新增）
- `/Users/cheyuwu/Projects/taiwan-md/scripts/tools/lib/article_health/checks/attribution_vague.py`（新增）

## 7. 測試

`python3 -m pytest tests/article_health/ -q`：214 passed, 8 skipped, 4 failed。
這 4 個失敗（`test_frontmatter_title.py` ×2 / `test_frontmatter_title_parity.py`
×1 / `test_phase6.py` ×1）用 `git stash` 驗證過**改動前就已經失敗**，跟本次
五項改動無關（屬於 `frontmatter_title.py` / `image_health.py` 既有 drift，
不在本次任務範圍內，未動這兩個檔案）。

`python3 scripts/tools/article-health.py knowledge/People/阿神.md` 冒煙測試：
全 27 個 checks（含新增的 2 個）跑完無例外，尾三行：

```
      info : 字數統計：4500 CJK chars (100% of 4500 門檻)

Summary: hard=0  warn=2  info=4  passed=False (fail_on=warn)
```
