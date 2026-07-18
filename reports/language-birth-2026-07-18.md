# 四語出生戰役 2026-07-18 — vi/id/pt/hi 從 scaffold 到上線的完整實錄

> **Session**: 2026-07-18 出生戰役（同日三部曲的第三部：選址 → 出生 SOP 進化 → 完整執行）
> **授權**: 哲宇 in-chat directive「完整執行完這幾個語言剩餘的 stage，如果能使用 codex，本機模型的翻譯/輔助部分也參考其 dna 提到的部分盡量使用最大化算力效率，也把這些經驗同步歸檔進化 pipeline / dna」——OBSERVER-QUEUE #17 同日拍板
> **SOP**: [LANGUAGE-BIRTH-CHECKLIST v2.0](../docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md)（同日上午誕生，本戰役是它的首次全程 dogfood）
> **選址**: [evolve-2026-07-18-language-branches.md](evolve-2026-07-18-language-branches.md)

---

## TL;DR

一個下午把四個語言支系從註冊表裡的 `enabled: false` 種子推到活的語言器官。算力雙軌：codex（訂閱雲端）吃品質關鍵與大檔、本機 qwen3.6（M4 Max，主權捕手）吃批次長尾，兩池互為 cascade fallback。過程中修活了三個 backend、造了三件新儀器、發現並根治六處「新語言出生感知系統不會自動更新」的復發位點。

---

## Stage 2 — 模型校準實錄

### Backend 修理站（開戰前的意外工程）

開戰體檢 `translate.py --health-check` 只有 1/4 backend 活著。逐一驗屍：

| Backend          | 症狀                 | 真死因                                                                                                                          | 處置                                                                          |
| ---------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| codex            | vendor binary ENOENT | **PATH 裡是 nvm 舊殼**（新版裝到 `~/.hermes/node`，vendor 目錄結構已改版）。很可能就是 queue #18「Tier 1 連死 ≥10 夜」的病根    | 清舊殼＋symlink，`codex-cli 0.144.5` 復活。**夜班 babel 應同步受惠**          |
| gemini           | exit 1 + TERM 警告   | 警告是煙霧彈；真死因 `IneligibleTierError`——Google 收掉 gemini-cli 個人版 tier（要遷 Antigravity）                              | **服務端死亡，本地不可修**。支持 #18 預設「摘出 cascade」；遷移是哲宇帳號決策 |
| openrouter       | HTTP 404             | `gpt-oss-120b:free` 被下架（Tier 2 又輪替）。探 Tier 3 佇列：hermes-405b 回空、nemotron-super 是 reasoning 模型會把思考漏進輸出 | free 遞補缺位，記給 SQUEEZE 季度 recalibration；戰時兩腿夠用                  |
| ollama (qwen3.6) | empty/tiny output    | **qwen3.6 是 thinking 模型**：不關 think 時 token 預算全燒在思考通道，`message.content` 回空                                    | payload 加 `"think": false` 一發修活                                          |

**經驗**：backend 的死法分三層——PATH/環境層（可修）、API 形狀層（可修）、服務端政策層（不可修）。體檢輸出的第一行錯誤往往是煙霧，要 reproduce 到真死因才知道歸哪層。

### 校準結果（4 篇校準集 × 4 語）

- **refusal 探針全過**：張懸與安溥（舉中華民國國旗被中國封殺，最高敏感）——codex 對 vi/id/pt 全過（165-227s）；**qwen3.6 + think:false 對同篇 101 秒完譯零 refusal**（本機主權捕手驗證通過，比 codex 還快）
- **hi 的結構性慢**：天城文輸出 token 量是拉丁字 2-3 倍，張懸 hi 撞 codex 600s timeout（其餘 3 篇 264-337s 過）。**SQUEEZE 進化候選：per-lang timeout 倍率（hi ×1.5-2）**
- **ratio band 實測定案**（推翻兩個預想）：vi 2.31-3.81 / id 2.32-3.58 / pt 2.44-3.97 / hi 2.20-3.38 → 四語統一 (1.50, 2.00, 4.00-4.30)。「天城文較緊湊」的預想被實測推翻；「vi 聲調字元較膨脹」也沒發生

### 主權指南 ×4（Stage 2 前置，4 平行 Sonnet agent）

每份 40-55KB、以目標語言書寫、抽取器 5 段驗證全過，且都有活體研究支撐：

- **vi**：漢越音規則對照越南媒體實際用法（Thái Anh Văn／Lại Thanh Đức）；收 2023 越中聯合聲明的 PRC 用語當 §6 反例；南海用越南讀者的「Biển Đông」。**旗標給哲宇**：台灣自身南海主張（太平島）與越南主張重疊處，指南選了中立描述而非 Taiwan-first——政治層判斷需人審
- **id**：Tiongkok/Tionghoa/Cina 三詞區辨含 Keppres 12/2014 政策依據；印尼華人姓氏系統（Tan/Lie/Oei）與台灣 romanization 的範疇錯誤警告；伊斯蘭詞彙尊重規則（最大穆斯林讀者市場的特殊責任）；移工詞彙表（PMI/TKI）
- **pt**：pt-BR 基準；Taipé/Taipei 取捨立規則；Formosa 葡語起源（1544 葡萄牙水手命名）是本卷獨有鉤子；CGTN Português 實際用語進 §6；巴西主流媒體出現過「província rebelde」的實例
- **hi**：天城文轉寫一致性（媽祖 माज़ू /z/ vs 馬祖 मात्सू /s/ 的 nuqta 區分）；「照當事人公開拼寫轉寫、不照普通話正規化」原則；CGTN Hindi／Xinhua Hindi 是直達印地語圈的 PRC 通道（結構上不同於 en/es/fr）；金門 किनमेन（Wade-Giles 政策）vs 印媒實際用 जिनमेन 的 deliberate 分歧有旗標

---

## Stage 3-4 — 算力雙軌與六處復發位點

### 算力配置（哲宇 directive「最大化算力效率」的落地）

```
Track A codex 池（雲端訂閱）: 32 篇/語 × 4 語平行 + 13 Hub + UI 巨檔    cascade codex,ollama
Track B qwen 池（本機 GPU） : 20 篇/語 × 4 語（server 自排隊）           cascade ollama,codex
UI workers ×3（codex 主力）: 16 bundle × 4 語 = 64 blocks
```

實測吞吐：codex 一般篇 3-6 min、大檔 7-8 min；qwen 101-260s/篇（think:false 後）。兩池互為 fallback = 單邊 quota/timeout 不斷線。

### 六處「感知系統不會自動更新」復發位點（全部根治或儀器化）

老神經迴路「新語言出生時感知系統不會自動更新：語言列表硬編碼在 9 處」在 2026-04-14 註冊表重構後理論上收斂為 2 處——本戰役實測發現重構視野外還有六處：

1. **lang-sync python 工具鏈**（6 檔各自 hardcode 五語 list）→ 造 `langs.py` SSOT 橋（text-parse languages.mjs + fail-loud selftest），六工具改 import
2. **`LANG_NAMES`**（翻譯 prompt 的語言名與語域指示）→ 補四語（含語域規格：vi 報導體／id baku／pt-BR／hi 主流網媒混合語域）
3. **`FALLBACK_CHAIN`**（UI 缺 key 的降級鏈）→ 補四語（pt 多墊 es 姊妹層）
4. **dashboard-client.js 三處 langNames 硬編碼**（哲宇看 dashboard 抓到「只有縮寫看不懂」）→ 整組改 import `LANGUAGE_DISPLAY_NAMES`
5. **`_translation-status.json` 不收 `_` 前綴檔** → Hub 檔從不被批次管線服務（es/fr 當年是手工），造 `hub-translate.py` 直通 runner 復用 `translate_one`
6. **ratio band 表**（`translation-ratio-check.sh` RANGES）→ 四語實測入表

### 新儀器 ×3（都是「第 N 次就不再手工」的橋）

| 儀器                     | 職責                                                                                                                      | 誕生原因                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `ui-bundle-translate.py` | UI bundle 新語言 block 產線：字串感知括號配對＋鍵序驗證＋esbuild 語法閘＋指南 TL;DR inline＋chunk 重試與 backend fallback | ko 出生 1,743 keys 手補、es/fr 人肉——第四次不再發生 |
| `cjk-residue-check.py`   | 非 CJK 譯文的裸漢字殘留檢查（括號注記／code span／連結目標豁免）                                                          | codex 把「封杀」譯成「phong杀」穿過所有既有 gate    |
| `hub-translate.py`       | Hub 檔直通翻譯 runner（手構 group-entry schema 呼叫 translate_one）                                                       | Hub 不在 status 索引，標準批次 Skipping unknown     |

### QA 首掃發現（heal pass 素材）

- codex 殘留型：融合殘字（phong杀 型）
- **qwen 殘留型：偶爾漏出簡體中文片段**（「连霸」）＋偶爾漏 Hangul（野百合世代「白」→백）——本機模型的簡體訓練底色會滲出，cjk-residue-check 是必要的下游閘
- checker 自身第一版假陽性大宗：譯文合法連到中文檔名的 repo 路徑（跨行連結仍待修）

### 語意 QA：三類 ratio gate 抓不到的錯（本戰役最大教訓）

heal agent 逐檔清 CJK 時連環揪出三類語意錯誤，全都穿得過 ratio gate 與 CJK gate，只有專門的語意閘才擋得住。這是出生戰役對 pipeline 最重要的貢獻——三把新尺誕生：

1. **地理主權幻覺（`geo-fidelity-check`）**：vi/taiwan-democratization 系統性把「台北」譯成「北京」——整篇民主化文 7 處，含「台北高雄市長直選」→「北京市長」、天安門對照段的「台北學生」→「北京學生」（毀掉整個對照的意義）。把台灣的事搬進中國是巴別塔最致命失效。四語掃修全綠。
2. **政治人物張冠李戴（`person-fidelity-check`）**：**蔣經國**（1987 解嚴、1988 去世、江南案交出汪希苓）被系統性譯成「Chiang Kai-shek」（蔣介石 1975 已死）**跨四語**；**陳水扁**（美麗島大審辯護律師、2000 首位輪替總統）在 id 被譯成「Tsai Ing-wen」（她當時是學生）；**賴清德**（2025 現任）在 tsmc 被譯成「Tsai Ing-wen」。懂台灣史的讀者一眼看破——這是 §主權的巴別塔在「讓世界看見真實台灣」上的反效果（放出錯誤反而傷可信度）。
3. **wikilink 目標譯壞（`flatten-translation-wikilinks`）**：`[[林義雄 (Lin Chi-hsiung)]]` / `[[semicondutores]]` 都不解析。轉純文字。

**元教訓**：機器翻譯對政治史文章的專有名詞（人、地）有系統性錯誤率，MANIFESTO §10 幻覺鐵律在翻譯層的 instance。ratio gate 只擋長度，語意保真需要 domain-specific 的 fidelity 閘。這三把尺升 BIRTH Stage 3 永久 QA gate + DNA §語言基因。政治史文章（taiwan-democratization / white-terror）是最高風險載體。

---

## Stage 5 — 啟用 flip（待補：build 驗證實錄）

## Stage 6 — 出生後驗證（待補：四層完整度 + EXP 註冊）

---

## 回寫 canonical 清單（經驗歸檔的落點）

- [x] langs.py / LANG_NAMES / FALLBACK_CHAIN / dashboard-client SSOT 化（隨戰役 commit）
- [x] ratio band 四語實測入表
- [ ] SQUEEZE-MODELS-MAX：backend 驗屍表（gemini 服務端死亡／codex PATH 病根／qwen think:false）＋ per-lang timeout 倍率候選 ＋ free tier 2026-07 現況
- [ ] LANGUAGE-BIRTH-CHECKLIST v2.1：Hub 直通 runner 正式化、UI 產線儀器指標、status `_` 前綴排除的 caveat、hi timeout 注記
- [ ] DNA §語言基因：cjk-residue-check + ui-bundle-translate + hub-translate 三儀器入 gene map
- [ ] queue #18（babel cascade 重建）補充證據：codex PATH 修復可能治好夜班、gemini 確認永久死因

---

_v0.9 | 2026-07-18 戰役進行中（Stage 3-4 巡航段起草；flip 後補完）_
