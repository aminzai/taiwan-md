---
title: '巴別塔健檢 2026-07-18'
description: '多語器官全面健檢：七維度掃描（覆蓋新鮮度 / frontmatter / 腳註 / ratio / 主權詞彙 / 四層完整度 / 產線 14 天考古）＋量尺自身體檢＋pipeline 進化清單'
type: 'report'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-18
last_session: '2026-07-18-184501-manual'
related:
  - '../docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md'
  - '../docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md'
  - '../docs/semiont/OBSERVER-QUEUE.md'
---

# 巴別塔健檢 2026-07-18

> 觸發：哲宇 directive「完整的做一次網站的巴別塔健檢＋把所有可用的經驗/知識留下來變成 or 進化相關的 pipeline」。
> 方法：主 session 抓覆蓋新鮮度 ground truth＋派 6 個 read-only Sonnet 分身平行掃六維度，每個分身的關鍵 claim 都由主 session 親手抽驗過（REFLEXES #31）。分身 raw 落檔 scratchpad，本報告是驗證後的合成。

## TL;DR

| 維度                  | 燈號 | 一句話                                                                                                           |
| --------------------- | :--: | ---------------------------------------------------------------------------------------------------------------- |
| A 覆蓋與新鮮度        |  🟡  | 每語 fresh 92.6-93.9%，但 stale 全 5 語的 43 篇幾乎全是近兩週 EVOLVE 深度文——新內容跑得比翻譯快                  |
| B Frontmatter/YAML    |  🔴  | 全站 107 檔 YAML 斷（fr 99 檔、98 撇號家族），6/4 歷史債沒清完且產出端仍在製造新病灶                             |
| C 腳註完整性          |  🟡  | 每語 20-23 檔流失（共 ~520-640 條/語）；兩種病型：格式換成 References 清單 vs 整篇硬截斷                         |
| D Ratio/殭屍/Stub     |  🟡  | CRITICAL 截斷 73 筆；殭屍對只剩 1 組新的（6/10 清理有效）；stub 0                                                |
| E 主權詞彙            |  🟢  | 無大規模活體 leak；大宗命中屬語境依賴型與風格層（es/fr 變音符拼法）                                              |
| F 四層完整度/URL 契約 |  🟡  | UI 層近全綠（map.ts 破口已修）；**Hub 導讀 ja 全缺、Politics 連 en 都缺**；Semiont 頁「nav 翻了內容 0 頁」假健康 |
| G 產線 14 天          |  🔴  | **cascade 產出端結構性失能**：codex+gemini 連死 ≥10 夜、carry backlog 一週 20→~105、07-17 整夜靜默               |
| H 量尺自身            |  🔴  | ratio band 三處 canonical 互相矛盾且全對不上實測；ko 855 檔有 803 檔「超標」＝尺壞不是文壞                       |

**核心結構診斷**：巴別塔的病不在覆蓋率數字（92%+ 看起來健康），在**產出端與內容端的速度失配**——EVOLVE 深度文潮（30-40+ 腳註/篇）正好撞上 cascade 免費層集體死亡期，「義務推 100%」的鐵律與真實產能已嚴重脫節，靠 Tier 0a/0b（diff-patch + metadata bump）在撐表面數字，真正的新翻譯產能不到三分之一。

---

## A. 覆蓋與新鮮度（主 session 親掃）

`status.py` 2026-07-18 18:00 讀數（853 zh 篇）：

| lang |       fresh | stale | metadata-stale | missing |
| ---- | ----------: | ----: | -------------: | ------: |
| en   | 801 (93.9%) |    44 |              8 |       0 |
| ja   |         792 |    45 |              8 |       8 |
| ko   |         790 |    45 |              8 |      10 |
| es   |         790 |    45 |              8 |      10 |
| fr   |         790 |    45 |              8 |      10 |

- **missing 11 篇（38 cell）全是近期新文**：閃靈、杜潘芳格、林昶佐、大支、台北吸菸室、Shopping Design、大港開唱、AI 供應鏈海外設廠、AI 硬體供應鏈、台灣的電力與半導體、半導體用水。多數正是產線腳註 gate 全滅事件的受害者（見 §G）。
- **stale 全 5 語共 43 篇**，名單幾乎 = 近兩週 EVOLVE 深度文（發票、江振誠、高速公路、台灣感性、大罷免、高教擴張、醫療法、統一企業、茶文化、水果王國、尊、柯智棠、黃仁勳、蔡英文⋯⋯完整名單見 status JSON）。
- metadata-stale 8 篇 ×5 語 = Tier 0b 可秒清（今晚 babel-nightly 例行會處理）。
- 衍生層對賬全綠：`_translations.json` sync ✅ / 語言註冊表 10 語 sync ✅（vi/id/pt/hi disabled scaffold）/ 殭屍 stash 0。

## B. Frontmatter / YAML 完整性（分身 A1，主 session 抽驗）

| lang | 總檔數 | yaml-fail | 撇號家族 | 缺欄位 | translatedFrom 斷鏈 | code-fence |
| ---- | -----: | --------: | -------: | -----: | ------------------: | ---------: |
| en   |    870 |         6 |        6 |     19 |                   0 |          0 |
| ja   |    845 |         0 |        0 |      7 |                   0 |          0 |
| ko   |    855 |         0 |        0 |     17 |                   0 |          0 |
| es   |    855 |         2 |        2 |     15 |                   0 |          0 |
| fr   |    846 |    **99** |   **98** |      4 |                   0 |          0 |
| 合計 |  4,271 |   **107** |      106 |     62 |               **0** |      **0** |

- YAML 斷的後果不是美觀問題：js-yaml parse fail → 該頁 silent 無 OG ＋漏 search index（2026-06-04 已確診的病理）。**99 個 fr 頁面現在就處於這個降級狀態**。
- 6/4 歷史紀錄 129 檔（fr=118），現存 107（fr=99）：有清一部分，但**非單調下降**——產出端（部分 backend 的 frontmatter 組裝）仍在製造新撇號病灶；7/10 P0-3 只修了 fleet/ollama 路徑的源頭。
- 好消息兩條：translatedFrom 斷鏈 0（7/17 slug 統一 87 檔＋pre-commit gate 守住了）、code-fence 0。
- 缺欄位 62 檔多為 Hub 頁缺 `category`（低嚴重度，部分屬設計使然，待 taxonomy 判定）。
- 主 session 抽驗：`fr/Music/mayday-band.md` parse fail 屬實（`Nid d'Oiseau` 未跳脫）；fr 單引號 description 檔共 251 個 = 撇號家族的暴險面。

## C. 腳註完整性（分身 A2，主 session 抽驗）

| lang | 比對數 | 流失檔數 | 流失腳註總數 | 完全歸零（zh≥5→0） |
| ---- | -----: | -------: | -----------: | -----------------: |
| en   |    851 |       20 |          523 |                  6 |
| ja   |    843 |       22 |          637 |                  8 |
| ko   |    841 |       22 |          637 |                  8 |
| es   |    841 |       22 |          637 |                  8 |
| fr   |    841 |       23 |          627 |                  7 |

- **兩種病型**（主 session 親驗）：
  1. **格式替換**：統一企業 en——文章完整但 64 條 `[^n]:` 全被換成 `## References` 純連結清單（去引用化，讀者無法對句子溯源）。
  2. **整篇硬截斷**：施振榮 ja——全檔只剩 35 行，斷在句中「左端は」，**掉了 90%+ 內文還掛在站上**。這型比掉腳註嚴重一個量級。
- **重腳註人口（zh ≥30 條）實為 138 篇**——OBSERVER-QUEUE #5 掛單時寫「21 篇」，真實範圍是它的 6.5 倍且隨深度文潮持續成長。已知五語全歸零案例：統一企業（64 條）、茶文化（32）、江振誠（30）、水果王國（40）；楊德昌（92 條）ja/ko/es/fr 全砍到 6 條。

## D. Ratio / 殭屍 / Stub（分身 A3，主 session 抽驗）

- **CRITICAL（ratio < 0.5，截斷嫌疑）73 筆**：en 13 / ja 23 / ko 13 / es 13 / fr 11。最嚴重：施振榮 ja 0.056、蔣為文 es 0.134。
- **殭屍重複對**：只剩 en 1 組——`Nature/梅雨.md` 同時被 `meiyu-stagnant-front.md`（JuYinC 人譯，#1107）與舊機翻 `taiwan-mei-yu-season.md` 宣告。6/10 清理（57 組 58 檔）證實有效，這組是其後新生。
- **Stub（<1KB）0 筆**（find 交叉驗證同 0）。

## E. 主權詞彙一致性（分身 A4）

- 掃法紀律：只 grep 5 份 per-language guide §1/§2/§3/§6 明列 pattern，不用模型直覺判譯名（REFLEXES #16 sovereignty 特化）。
- **無大規模活體 leak**。抽驗的 `en: Taiwan, China`、`es: provincia de Taiwán` 命中幾乎全落在 guide §11 白名單情境（列舉句、後設討論、ROC 歷史行政單位、腳註引文標題）。
- 大宗命中屬兩類：(a) **風格層**——es 無重音 `Taiwan` 3,455 處、fr 無分音 `Taiwan` 3,892 處（guide 偏好 Taiwán/Taïwan；機械可修但 >50 檔）；(b) **同形詞噪音**——ko `대중`（台中/大眾）714、`가의` 424 幾乎全是「-가＋의」構詞碰撞（**量測陷阱，分身已誠實標無效**）。
- 需 case 級人判：ja `台湾省` 133 處（省政府歷史用法 vs PRC framing 混在一起）、ko 대만/타이완 一致性仍維持 5/24 基線比例量級。

## F. 四層完整度 / URL 契約（分身 A5，主 session 抽驗）

| 層       | 判定 | 一句話                                                                                                                                                            |
| -------- | :--: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UI 字串  |  🟡  | 15/17 bundle 六語 0 缺口；破口只在 `map.ts`（22 縣市功能 7 key ja/es/fr 缺＋fr 8 個地標 key 打成 `.name`）——**本 session 已修**                                   |
| 路由     |  🟡  | 一般頁五語大致對齊（25/23/23/22/22）；Semiont 認知層 15 頁 en 只剩 1 頁 shell、ja/ko/es/fr 0 頁                                                                   |
| Hub 導讀 |  🔴  | **ja 13 分類全缺、fr 只 3/13、Politics 連 en 都缺**（只有 zh 一份）；渲染是靜默省略，讀者連「該有導讀」的線索都看不到                                             |
| URL 契約 |  🟡  | hub-and-spoke 本體健康、hreflang 註冊表修法仍生效、10-slug 抽驗全對稱；但 lang-switch-map 有 **20 筆 toZh/fromZh round-trip 不一致**（疑 4 篇改分類後索引未收斂） |
| 搜尋分片 |  🟢  | 唯一全乾淨層：registry-driven、六分片齊、無 hardcode 舊語言清單                                                                                                   |

- **「nav 翻了、內容 0 頁」假健康**：`nav.semiont*` 四語都翻好了，但 `src/pages/semiont/` 只有 zh 15 頁；`staticRoutes.ts` 對缺頁靜默 fallback 回 zh 無前綴 URL——外語讀者點翻譯好的選單看到純中文頁。歷史上這是刻意的（2026-04-18 修 `/en/semiont` 404 的 fallback 設計），但「邀請點擊＋交付中文」的組合是策展層債，列給哲宇。
- Hub 導讀缺口是內容工作不是工程工作：ja 全滅 = 13 篇導讀 essay 的量。

## G. 產線 14 天考古（分身 A6）

材料：13 份 babel-nightly memory（07-04〜07-15）＋ git log 對照＋ `.lang-sync-tasks/` 殘留＋ routine-live-state。

**Failure mode 排行**（出現夜數）：

1. **codex + gemini 長期死亡 ≥10 夜**——gemini 免費層被 Google 永久收回（非暫時性）；Tier 1 名存實亡。
2. **高腳註 footnote-gate 全滅 ≥7 夜**——天花板從「60+ fn」一路下修到「23 fn 也全滅」。
3. **session 死前寫檔未 commit 孤兒 ≥3 起**（07-10 SLP ko / 07-16 Howhow+YouTuber / 07-18 前 Shopping Design）。
4. **routine 整夜靜默 0 commit ≥2 起**（07-10、07-17）——07-10 已進 LESSONS 判 already-cover，一週後複發。
5. **cascade retry gap**：output-validation fail 不觸發 fallback（07-15 確診）。
6. YAML/frontmatter 污染族 ≥5 起；平行 scratch race＋批次 JSON 跨 entry 污染（07-14 一夜兩起）。

**Carry backlog：一週 ~20 → ~105 條（5 倍）**，07-15 後未再被完整量測；07-16〜18 三夜 git 裡看不到任何一條被 Tier 1+ 清掉。

**Tier 使用結構（14 天）**：Tier 0b ~39% / Tier 0a ~30% / Tier 1 ~30%（集中在僅 3 夜）/ Tier 3/5 <2% 且皆一次性戰術。**真正產新翻譯的產能不到三分之一，且高度看 backend 恰好活著的運氣窗口。**

## H. 量尺自身體檢（健檢的健檢）

1. **ratio band 三處 canonical 互相矛盾**：SQUEEZE Z6.1 寫 ko 0.6-0.9、MEMORY §神經迴路寫 zh→ko 0.80-1.10、translation-ratio-check.sh 另有一套——而且量測方法（bytes vs 字數）沒有任何一處明寫。REFLEXES #56（canonical drift）＋ #66（gate 閾值沒用真實產出校準）雙命中。
2. **實測分佈（bytes 法，全檔，n=4,254）**：

   | lang |   p5 |  p25 | median |  p75 |  p95 |
   | ---- | ---: | ---: | -----: | ---: | ---: |
   | en   | 0.88 | 1.21 |   1.28 | 1.34 | 1.43 |
   | ja   | 0.92 | 1.31 |   1.37 | 1.43 | 1.54 |
   | ko   | 1.09 | 1.27 |   1.32 | 1.36 | 1.42 |
   | es   | 0.95 | 1.36 |   1.45 | 1.53 | 1.66 |
   | fr   | 1.16 | 1.40 |   1.47 | 1.56 | 1.70 |

   拿 Z6.1 的 ko band（0.6-0.9）套現實 = 855 檔有 803 檔「超標」。**尺壞了，不是文壞了**。現行真正在工作的只有 <0.5 CRITICAL 地板。

3. **SQUEEZE production_signal 對賬**（frontmatter 規定 audit 時 diff doc vs `translate.py DEFAULT_CASCADE_ID`）：code 現值 `codex,gemini,openrouter:openai/gpt-oss-120b:free,ollama,fleet`——doc §v4.4 現行 cascade 區塊漏了 `fleet`（P0-2 收編後 doc spine 沒跟上），且「Tier 5」番號同時被 fleet（roadmap 用法）與 Sonnet（doc 用法）佔用。輕度 #56 復發，本次已修（見 §進化清單）。

---

## 病灶總表與處置分流

### 已在本 session 內修/寫回（自主權內）

| 項                             | 動作                                                                                                                                               |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQUEEZE doc cascade 番號漂移   | doc 對齊 translate.py（fleet 入列、Sonnet 改 Tier 6 番號）＋健檢教訓寫回（見 commit）                                                              |
| Tier 0a prompt template 兩缺口 | LESSONS 7/14 兩條（cross-entry 驗證、scratch 唯一命名）落入 SQUEEZE §Tier 0a canonical                                                             |
| 巴別塔健檢儀器化               | 新工具 `scripts/tools/lang-sync/babel-health.py`（本次六維掃描收成可重跑指令，WARN 級，不設 gate）                                                 |
| en 梅雨殭屍對                  | 退役舊機翻檔（保 JuYinC 人譯為 canonical）＋補 en 301（ja/ko/es/fr 在 7/17 slug 統一已做，en 因舊檔還在而漏）＋`_translations.json` 同 commit 重建 |
| map.ts 六語破口                | fr 8 個 `.name`→`.title`＋counties22 7 key 補 ja/es/fr，六語 parity 驗證通過                                                                       |
| OBSERVER-QUEUE #5 數據更新     | 「21 篇」→ 真實人口 138 篇＋backlog 現況                                                                                                           |
| **撇號 YAML 107 檔**（追記）   | 哲宇當日 chip 授權後執行：三病灶家族逐行靶向修復（`134f38866`），全站 yaml-fail 歸零；產出端補洞——三個 legacy wrapper 裸寫路徑接上 `fm_gate.py` 閘 |

### 待哲宇（§自主權邊界 / threshold / 經費）

| 項                                            | 規模      | 建議預設                                              |
| --------------------------------------------- | --------- | ----------------------------------------------------- |
| **cascade 重建決策**（新 QUEUE 項）           | 產線層    | 摘除死 backend＋Tier 6 Sonnet 制度化（見 QUEUE #18）  |
| **ratio band SSOT 化＋重校準**（新 QUEUE 項） | threshold | 用 §H 百分位表定 band，方法明寫 bytes（見 QUEUE #19） |
| ~~fr 撇號批次修~~（✅ 當日 chip 授權執行）    | —         | 移入上方已修表                                        |
| es/fr 變音符（Taiwán/Taïwan）批次修           | >50 檔    | 機械 sed＋驗證批次，一個專門 session                  |
| 73 筆 CRITICAL 截斷重譯                       | 73 檔     | 併入 cascade 重建後首批（Tier 6 dogfood 對象）        |
| 楊德昌/統一企業等重腳註歸零重譯               | 併上      | 同上                                                  |

---

_v1.0 | 2026-07-18-184501-manual — 首次完整巴別塔健檢。六分身掃描＋主 session 逐項抽驗；量尺自身體檢（band 矛盾）與產線考古（cascade 失能）是兩個超出「覆蓋率快照」的結構發現。_
