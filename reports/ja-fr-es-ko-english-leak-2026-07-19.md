---
title: 'ja/fr/es/ko 68 檔「宣稱已譯實為英文」— 發現、根因、補洞'
description: '讀者揭露單一 ja 檔的人名誤植 → 追查擴大到 4 語 68 檔的 translatedAt 合法但本文零目標語言文字系統的系統性洩漏；補上 script-presence-check gate + translate.py 即時攔截 + cross-lang-audit 盲點合併'
date: 2026-07-19
type: 'incident-report'
status: 'gate-shipped, retranslation-pending'
---

# ja/fr/es/ko 68 檔「宣稱已譯實為英文」

## 起點

讀者在使用 hi 造山者文章時，回報 `knowledge/hi/Art/mountain-makers-tsmc-documentary.md` 把張忠謀誤植成蔣介石（已由更早的 heal pass `df9e8d13d` 修好，本次複驗確認 13 處全清）。同一輪回報也帶了 id/pt 兩個獨立錯誤（皆已由 `5da213be2`/`643f116c5`/`df9e8d13d` 修好，本次只補了一句漏網的 id 交接句：`5c64008a3`）。

在幫 id 檔案交查 ja/es/fr/ko 手足檔案時，發現 `knowledge/ja/History/taiwan-democratization.md` 的 `translatedAt` frontmatter 顯示已譯，但本文完全是英文——而且不是 en 版的複製，是另一次獨立措辭的英文改寫。這不是「翻譯品質差」，是翻譯根本沒發生，只是被寫進了 ja 的目錄。

## 擴大查證

寫了 `script-presence-check.py`：非拉丁字母語言（ja/ko/hi）檢查目標文字系統字元數是否為零；有變音符號的拉丁語言（fr/es/pt/vi）檢查變音符號數是否為零（body ≥ 300 字才判定，避免誤殺短文）；id 用功能詞頻率比對（英文常見功能詞 ≥ 10 次且 ≥ 印尼文常見功能詞 3 倍）。

全站掃描結果：

| 語言        | 受影響檔案 | 總檔案數                                            |
| ----------- | ---------- | --------------------------------------------------- |
| ja          | 26         | 845                                                 |
| ko          | 18         | 855                                                 |
| es          | 14         | 855                                                 |
| fr          | 10         | 846                                                 |
| hi/id/pt/vi | 0          | 39/54/54/54（新生語言，本次出生戰役已過 heal pass） |

**68 個唯一檔案，44 篇文章**（多篇跨語言重複中鏢）。4 篇文章四語同時中鏢：`taiwan-generations`、`complex-life-festival`、`huang-shan-liao`、`psychological-warfare`。3 篇三語中鏢：`za-share`、`united-front-tour-groups`、`taiwan-white-terror`。

## 意外發現：偵測工具已經存在，但發現沒被行動

repo 裡已經有 `cross-lang-audit.py`（2026-07-18 出生戰役期間建的，比對 5 個維度：slug 一致性、translatedFrom 格式、body 語言、frontmatter 完整性、orphan check），而且 `reports/cross-lang-audit-2026-07-19.json` 已經存在——**已經跑過，已經抓到 ja=27/ko=19，但這份報告從沒被 commit，發現也沒被行動**。detection 有了，但沒有人把它接到「然後呢」。

更重要的結構性盲點：`cross-lang-audit.py` 的 body-lang 偵測法對 en/es/fr 統一套用「Latin 字母占比 ≥ 70%」門檻——但英文本身就是拉丁字母，一篇假裝法文/西文的英文文章 latin_pct 一樣會落在 99% 附近，完全通過這道檢查。這就是為什麼它只抓到 ja/ko（有獨立文字系統，容易分辨）卻完全漏掉 es/fr（同為拉丁字母，這道檢查法結構上分辨不出「這是拉丁字母但語言不對」）。`hi`（天城文）也沒有正確的 expected_lang_dominance() 條目，會誤用 Latin fallback——結構上也抓不到 hi 的同類錯誤。

## 修的東西

1. **`script-presence-check.py`**（新檔）——獨立 CLI + 可重用的 `check_text(body, lang)` 函式，補上 cross-lang-audit 的拉丁-對-拉丁盲點。
2. **`translate.py` 即時 hard gate**——`translate_one()` 在既有 frontmatter/footnote/size 三道結構閘之後，新增第四道呼叫 `check_script_presence()`，任何未來的 backend 輸出「語意流暢但語言不對」的內容會在寫檔前被攔截、回傳失敗讓 cascade 換下一個 backend重試，不會再靜默落地。
3. **`cross-lang-audit.py` 合併**——委派同一套 `check_text()` 邏輯（新增 `script_presence_english_leak` issue type），兩支檢查器不再各自維護會漂移的判準。合併後複驗：`script_presence_english_leak` 精確找到 ja=26/ko=18/es=14/fr=10，與獨立跑 `script-presence-check.py --lang all` 完全一致。
4. **`docs/semiont/DNA.md`**：新增語言真偽檢查基因條目。
5. **`docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md`**：Stage 3「三道語意 QA gate」升級為「四道」，新增 gate 5 說明。

## 根因：為什麼英文會通過所有既有閘門

`translate.py` 既有的三道 hard gate（frontmatter fence/YAML、footnote 數量、檔案大小）全部只檢查**結構**，從不檢查輸出**是不是目標語言**。一篇語意流暢、footnote 完整、frontmatter 合法的英文假翻譯，會直接通過每一道既有檢查存活到 commit——因為它根本沒被判定為「翻譯失敗」，而是被系統當成「一篇正常長度、正常格式的翻譯」收下。

至於 backend 為什麼會產出英文而不是目標語言：`build_translation_prompt()`（`openrouter-translate.py`）的系統提示只寫「Translate zh-TW articles to {LANG_NAMES.get(lang, lang)}」，沒有一句話明確要求「輸出文字本身必須是該語言的文字系統/書寫」——對模型來說，「翻譯」跟「用英文摘要/複述後回答」在字面指令層次是可以混淆的，尤其當來源內容政治敏感時。

觀察到的相關性（非確定因果）：受影響最集中的文章主題高度重疊在主權敏感題材——統戰（united-front-tour-groups）、白色恐怖（taiwan-white-terror）、心理戰（psychological-warfare）、認知作戰（poisoned-potato-cognitive-warfare-taiwan）、中華台北（chinese-taipei）、法輪功（falun-gong-in-taiwan）。es/fr 是同一批次時間戳（`2026-05-29T00:35:00+08:00`），但 ja 是三週後的獨立 production run（`2026-06-09`），仍然命中高度重疊的文章清單（6 篇三語甚至四語同時中鏢）。這排除了「單一批次腳本 bug 導致」的簡單假設——更像是這些特定 zh 來源文章的內容屬性（可能是主權敏感度、也可能是純粹的長度/格式複雜度）持續讓某些 backend「配合但用英文回答」而非依指示輸出目標語言，跨越不同批次、不同時間、可能不同 backend 都重現。**根本原因未完全鎖定**（缺當時的 per-backend call log），留給重譯批次時搭配 `--health-check` 與 per-backend 標記做進一步歸因。

## 尚未做的事（留給下一步決策）

**68 檔重譯**——用 `translate.py` cascade 重新翻譯，逐檔過 script-presence-check + cjk-residue + geo-fidelity + person-fidelity 四道 gate 才能落地。這是實質的翻譯運算量（每篇視 backend 200-900 秒），且很可能需要人工抽讀確認語意品質（不只是「有沒有出現該文字系統」），比本次的偵測與補洞工作大得多，需要哲宇決定排程與優先序（哪些語言先、要不要先修復高重疊的 6-7 篇再擴大到剩餘篇目、要不要另開 worktree 平行跑）。

`frontmatter_missing`（42 檔）、`slug_mismatch`（2 檔）——`cross-lang-audit.py` 順帶抓到的既有問題，跟本次英文洩漏無關，未列入本次修復範圍。
