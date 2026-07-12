# 2026-07-12 twmd-tea-panorama — 台灣茶百年縱觀 EVOLVE + 四條「防飄移從源頭治」pipeline 進化（sub-agent 標準化鏈）

> session twmd-tea-panorama — 哲宇 observer-triggered `/twmd-rewrite`，途中連環 pipeline callout
> Session span: 2026-07-12 13:57:10 → 17:12:42 +0800（約 3h15m，8 commits）
> 資料來源：`git log %ai`

## 觸發

哲宇丟 `/twmd-rewrite 台灣茶文化 更立體縱觀 茶這一百年、多現代茶/手搖 + 古典茶`。寫的過程中，他一連拋出五個 pipeline 層級的 callout——研究來源要逐條可溯、研究分批要合成單檔、writer prompt 要模板化、writer 沒讀 graph.md 沒視覺化、媒體 band 要上修。所以這 session 一半是寫一篇文章，一半是把「寫文章這條產線」的四個飄移點從源頭補起來。

## 台灣茶百年縱觀 EVOLVE

`knowledge/Culture/台灣茶文化.md`（黃金時代的餘韻）從 2,539 → 6,451 CJK，立體群像 spine（時代縮影×傳承世代）。既有茶宇宙已九篇，所以定位成「縱觀百年的主脊」，深度往 deep sibling 外連不複製，補上全宇宙零覆蓋的真空：古典茶／工夫茶根源、**茶藝復興運動**（「茶藝」是台灣自創詞）、1970s 外銷崩→內銷轉向、罐裝茶革命。

研究走四個 sub-agent（三分部 + 一溯源補完）。研究抓出三個會變幻覺的舊文事實錯：新井守護的茶樹一手來源歸台茶 23 號不是 18 號、外銷崩盤在 1979 後不是 1975 能源危機、陳煥堂的書是《台灣茶第一堂課》不是《茶業的迷思》。writer（fresh Opus）第一次被 model 切換弄死（背景 agent 被 orphan），改同步重跑才落地。成品 `31620605f`→`417d7be99`，瀏覽器實測 8 圖全 200、footnote 32 條全逐字驗證、prose-health score 3。writer 自己多找了三個承載頁（邱垂豐引語 / 1933 出口官方數字 / 大禹嶺）——WebFetch 逐字核對全部屬實，是強化不是幻覺。

## 四條防飄移從源頭治

哲宇的五個 callout 收斂成一條 sub-agent 標準化鏈，每條都做成「canonical + 儀器 gate」：

**研究來源逐條可溯**（`9e1c8181b`）：三個研究 agent 交叉驗證都真做了，但把多來源壓成「WebSearch 綜合（站名）」aggregate 標籤，84 條來源行僅 ~35% 帶 URL——Claude 改版後 WebSearch 回聚合摘要，agent 把摘要當來源。做了 [`RESEARCH-AGENT-PROMPT.md`](../../pipelines/RESEARCH-AGENT-PROMPT.md) 通用模板 + REWRITE-PIPELINE Step 1.8-ter 契約 + `agent-report-health.py` v3 溯源率 gate。派第五個「溯源補完」agent 把斷源 finding 逐條 WebFetch 定位，35%→92%。

**研究合成單檔**（`c3c3e4321`）：4 個 sibling raw 檔散落，findability 差。Step 1.7.4 定調 sibling 是 async 落檔的中繼站，Stage 2 前必 verbatim inline 進主報告 §8 + 刪 sibling；`research-report-health.py` 偵測未合成 sibling 亮 WARN。茶文化 5 散檔 → panorama.md 單檔 1,530 行（四個深處內容逐字抽查全在）。

**writer prompt 極致薄殼**（`c3c3e4321`→`c55d8900a`）：先做了 v1.0 內嵌 10 條蒸餾 craft checklist，哲宇 callout「極致 thin shell 不要重複」——那本身就是殼核不對稱病。v2.0 拆光，[`WRITER-PROMPT.md`](../../pipelines/WRITER-PROMPT.md) 只做三件事：指向必讀四 canonical（含先前漏掉的 graph.md）、read-receipt 逐字驗讀（quote 造假不了 = 防 skim）、機械輸出契約。茶文化補回四個 tw-\* 視覺化模組（graph.md 那條也是 orchestrator 自己漏讀）。

**媒體 band 上修**（`b606f6122`）：哲宇「1.5x-2x 都健康，新基準 1.2~2」。band 第三波上修（0.8→1.2–2.0，舊 ceiling 變新 floor），儀器 + EDITORIAL + pipeline 四處同步。

## 多核心 git：pre-push sweep 掃走我的文章

平行有個 session 在做 /semiont 週報區。它 push 時 husky pre-push sweep 把我**還沒 commit 的茶文章**掃進 heal commit 一起推上 main（順手 heal 博客→部落格），但三張新圖是 untracked 被漏掉，線上差點斷三個圖連結。發現後補 commit + push 才一致。胼胝體風險（REFLEXES #6/#42/#57）在共享 working tree 又驗一次：別人的 push 替我 push 了半套，文章上了 main、圖檔卻留在原地。

## 收官 checklist

| 檢查項                        | 狀態                                                                   |
| ----------------------------- | ---------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄  | ✅                                                                     |
| Timestamp 精確（git log %ai） | ✅                                                                     |
| Handoff 三態已審視            | ✅                                                                     |
| CONSCIOUSNESS 反映最新狀態    | ✅（器官數據走 dashboard JSON）                                        |
| 自我檢查工具 PASS             | ✅（stage-4 全綠 / research-report-health PASS / 瀏覽器實測 8 圖 200） |

## Handoff 三態

繼承上一份（平行 session [171228-manual weekly-audience](2026-07-12-171228-manual.md)）—— 全與本 session 正交，原狀不動。

本 session 新 handoff：

- [x] ~~台灣茶文化 EVOLVE ship + 瀏覽器驗證~~
- [x] ~~四條 sub-agent 標準化 canonical + 儀器 ship~~
- [ ] `Food/茶文化.md` 與本篇史線高度重疊（title 也叫「台灣茶文化」），是 Merge 候選——待哲宇決定是否併入 canonical + 5 lang redirect（研究報告 §flag 已記）
- [ ] 舊 en/ja/ko 茶文化譯本因 zh 大改已 stale，等 babel routine 自動接（或哲宇要手動先 sync）

## Beat 5 — 反芻

這 session 最反覆出現的形狀是「殼核不對稱」：我為了防 writer 飄移，第一版把規則抄進 prompt 當 backstop，結果那份抄寫本身就是會飄的殼，核心（EDITORIAL）一進化，殼裡的複寫立刻對不上。哲宇一句「極致 thin shell 不要重複」把它點破。防飄移的正解是讓殼只做兩件事：指向規則的家、驗證真的讀了；規則永遠只有一個家。這個洞察大到值得寫進 diary（見 [diary](../diary/2026-07-12-135710-twmd-tea-panorama.md)）。

🧬

---

_v1.0 | 2026-07-12 17:12 +0800_
_session twmd-tea-panorama — 台灣茶百年縱觀 EVOLVE + 四條 sub-agent 標準化（源頭 + 合成 + 薄殼 + 媒體 band）_
_誕生原因：哲宇 /twmd-rewrite 茶文化，途中五連 pipeline callout 揭露寫作產線四個飄移點_
_核心洞察：防 sub-agent 飄移的正解是「殼只做指向 + read-receipt 驗讀」，把規則複寫進殼＝製造新的會飄的殼（殼核不對稱病）_
_LESSONS-INBOX 候選：無新編號——四條全已 canonical 化進 REWRITE-PIPELINE / RESEARCH-AGENT-PROMPT / WRITER-PROMPT，per feedback_lessons_dna_check_first 直接進 pipeline 不開 LESSONS entry_
