# Newsroom 器官健檢報告 — 從誕生到 2026-08-06

- **觸發**：哲宇 2026-08-06 directive「完整深度研究 /semiont/newsroom 從正式開發出頁面到現在的狀態，盤點運作完整度，以及紀錄是否有正確進到流程歸檔報告＋自我進化」，並附兩個觀察：「很多文章沒出現在上面」「有寫完但後面階段都沒有顯示，卡在中間沒有執行完畢」。
- **方法**：主 session（Fable）踩點＋production 現場驗證，三個 Sonnet 平行研究席（歷史重建／資料管線稽核／歸檔迴路稽核），主 session 收斂並親自補查覆蓋率斷崖成因。
- **一句話結論**：**器官骨架健康、歸檔完整，但「餵養」與「反省」兩條迴路都斷了**——資料層有一個真 bug、三個結構性盲點、一次無人聞問的 35% 覆蓋率斷崖；HANDOFF 規則遵循率 ~5%；誕生 20 天沒被任何自我進化機制掃過。

---

## 一、身世：誕生與演化時間軸

| 時間                   | 事件                                                                                                                                                                         | 觸發                                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 2026-07-16 15:45–17:30 | **誕生日**：`83ba7a3b7` 器官誕生 → 1 小時 45 分內連迭三版（v1 kanban → v2 泳道表 → v3 暗色殼＋編輯室現場劇場），同波完成 making-of 頁、NewsroomTrail、nav 進站、runtime 容錯 | 哲宇 goal directive＋陳睨對話；v1→v3 全程哲宇截圖 callout 驅動 |
| 2026-07-16 當晚        | 大罷免 dogfood 端到端實跑，抓到 F1-F7 七條摩擦，**全部當天到隔天修完**                                                                                                       | 哲宇要求立即 dogfood                                           |
| 2026-07-24             | `402b256c9` 修 research-only 文章誤亮「編輯室現場」404 CTA（~166 篇假連結）                                                                                                  | 哲宇 callout                                                   |
| 2026-07-26 21:59       | `836dabd88` **wall-clock 帳本誕生**（`reports/newsroom/stage-events.jsonl`，bootstrap 693 列）——v9.5 產線節流波的副產品                                                      | 哲宇「pipeline 卡卡的幫我整個順過」                            |
| 2026-07-26 之後        | **11 天零程式碼演化**。帳本持續被 append（使用），骨架無人再碰（無演化）                                                                                                     | —                                                              |

**設計 vs 實作對照**：設計文件五個子目標中四個完成、一個半完成（編輯室自動化的攻防輪＋總編室 contract 落地並驗證，但「runner 一步化」腳本從未出現，實際由 Workflow 機制承擔）。設計文件明列的「後續構想」（Harvest per-stage 派發、看板互動化、陳睨的彈幕實驗）全部未做——且 Harvest 後端本身 7/12 起靜止，比 newsroom 誕生還早，「本機控制模式」按鈕從誕生起接的就是無人維護的後端。§九留給哲宇的 4 項決策，預設值全部無異議直接成為事實定案。

## 二、運作完整度盤點（評分：C+，可用但單張卡片不能盡信）

### 2.1 活著的部分

- derive-first 原則守住：不建第二本帳，全量掃描推導，正面憑證（frontmatter 欄位）優先於檔名猜測
- ship 偵測與 build-time 自動刷新正常：`prebuild:dashboard` 每次 deploy 重跑 generate，出刊層資料新鮮（8/6 中午推送後看板即顯示 v4 新標題）
- 每日 06:00 data-refresh routine（refresh-data.sh Step 10b）兜底，看板不會永久凍結
- 本週 7 篇深度文全部有進帳本，軌跡完整度良好（馬祖除外，見下）

### 2.2 一個真 bug（下一篇文章就會現形）

**verify 完成判定 key 對不上**：`generate-newsroom-data.py` L216 的 regex 捕捉 `5`/`6`，L339 寫入 key `stage5`/`stage6`，L342-345 的完成判定卻讀 `stage35`/`stage36`——**永遠讀到 None，verify status 永遠卡 `in-progress`**。實測 10 篇有 verify 記錄的文章 0 篇 done、0 篇 blocked，其中 8 篇兩審皆 PASS 仍顯示進行中。目前僥倖無感（全部已 ship，ship 短路優先），下一篇「兩審過但未出貨」的文章 next_step 就會誤導。

### 2.3 三個結構性盲點

**盲點 A：覆蓋率斷崖（哲宇觀察 1 的主因）——月槽視窗髮引觸發。**
生成器取「最新 3 個月份目錄」當觀測窗。8/3 15:18 當月第一個研究檔（黃崇仁）落進 `2026-08/`，隔天 routine 一跑，視窗 [05,06,07]→[06,07,08]，**2026-05 整月 129 份研究檔一夜滑出**，上板數 270→176（-35%）。每月月初的第一個 Stage 1 commit 都會重演一次。此退化被 data-refresh routine 每日如實記錄（176→180→182→183），**11 天無一次升級為異常**——freshness gate 只驗 JSON mtime 是當天，不驗覆蓋率合理性。對照組：同期免疫評分 60→57 的小鬆動被明確標記「首次鬆動，值得診斷型 routine 接手」。

**盲點 B：slug 身份分裂＋帳本凍結語義（哲宇觀察 2 的主因）。**

- 全板 6 組分裂身份，5 組是無害重複卡（出刊數膨脹），1 組有害：`matsu-biennial`（卡在「去做 projection」）與`馬祖國際藝術島`（已出刊）並存，各持半條軌跡。分裂根因：`knowledge/Art/馬祖國際藝術島.md` **缺 `researchReport:` frontmatter**，research→ship 反向橋接搭不起來。
- 帳本 dedup 語義「同 (slug,stage,status) 只記第一次」→ 8/6 的 v4 全篇重寫與 r2 修訂（兩次 ship，status 都是 done）**一行都沒進帳**，dashboard 仍顯示定稿於 8/5。重寫史在帳本上不存在。副作用：`stage_deltas_min` 出現 -2880 分鐘這種負值（首次觀測時序與真實產線順序脫鉤）。

**盲點 C：幽靈列＋多版本藍圖抓錯。**

- 產線看板 6 列中 4 列（`台灣行道樹-closing`／`苯駢芘食安事件-closing`／`-evolve-blocks-0728`／`台灣感性-factcheck`）是**工作檔被誤認成獨立文章**，永遠卡在「寫作●」——「卡在中間沒執行完畢」的視覺主力。
- projection 區塊不認 `supersedes` 欄位、無版本比較（room 區塊有），同文多藍圖時**由 `os.listdir()` 檔案系統枚舉順序決勝**——實測抓到被三席打回的 v3 而非實際拿來寫的 v4，不可重現。後果在 production 可見：文章頁「編輯台足跡」連到 `/semiont/newsroom/matsu-biennial-v3/`，展示被否決的藍圖＋「目前沒有找到編輯室審查紀錄」——而這篇是全站編輯過程最厚的一篇（三輪編輯室、13+ 席、兩輪外行冷讀、兩張修復單，全部在 repo 裡，只是 key 對不上）。**編輯台的存在目的是公開思考過程，編輯過程最深的文章在編輯台上顯示成「沒走過編輯室」。**

### 2.4 其他

- wall-clock 精度覆蓋僅 14/183（7.7%），其餘為日粒度 legacy 推導
- 4 條陳年 warning：3 條為命名慣例的結構性噪音（codename vs 中文標題、evolve 後綴），1 條（吳明益 room 檔缺 `slug:`）一行可修；另有 **10 份 room 檔同樣缺 slug 但連 warning 都不發、靜默跳過**（更隱蔽的缺口類型，暫無實質資料流失）
- `ARTICLE-DONE-LOG.md` 停在 8/3（黃崇仁），本週 5 篇出刊全部沒補——`recent_done` 區塊的獨立資料源落後 3 天，維運缺口非程式 bug
- CI build 時 generate 也會跑，但 build 環境蓋的 ledger 時間戳不會 commit 回 repo——兩條寫入路徑，一條會蒸發

## 三、歸檔＋自我進化稽核：**歸檔面接得很好，進化面斷了**

**接好的**：

- 誕生日 memory×2／diary×2／設計報告×2 全部落檔、`reports/INDEX.md` 正確索引、7/26 設計報告（design-rewrite-throughput）同樣在檔在索引
- 誕生日 dogfood 七條摩擦全數閉環，無遺留
- HANDOFF 規則在 REWRITE-PIPELINE §三條派發鐵律＋全部 10 個 stage contract 逐字一致

**斷掉的**：

1. **HANDOFF 遵循率 ~5%**（7/26 以來 43 個 rewrite commit，僅 2 個照規則同 commit 帶上帳本，且都是 8/5 馬祖）。實況：時間戳常有近即時蓋到，但帳本行被不相干的批次 commit 掃走；馬祖 verify/ship 遲 10-36 小時事後補登，**v9.5 想量的「每站真實 wall-clock」已被補登污染**。真正撐住看板的是每日 routine 兜底，不是設計初衷的每站即時。
2. **零反省記錄**：器官自身的問題（覆蓋率斷崖、遵循率、verify bug）無一進 LESSONS-INBOX；REFLEXES 無對應迴路；dna-audit 最後一次跑在誕生前 11 天，從未掃過它；self-evolve-weekly 至今無一份報告檢討過它。EVOLVE Mode 3 拿 stage-events 當儀器審「別的站」的成本，沒人拿同把尺回頭審這個儀器自己。**7/26 設計正是為了修「stage 產物不落 commit」根因，但藥方本身沒人吃的事實無任何機制在追蹤。**
3. **範圍空白未明文**：SPORE／MAINTAINER／BABEL 全無編輯台掛鉤。不掛可能正確（資料模型不合），但設計文件對此隻字未提——是遺漏不是劃界。

## 四、哲宇兩個觀察 → 機制對照

| 觀察                     | 機制                                                        | 條目   |
| ------------------------ | ----------------------------------------------------------- | ------ |
| 「很多文章沒出現在上面」 | 月槽視窗髮引滑動：5 月整月 129 檔於 8/4 滑出，-94 篇        | 盲點 A |
| 同上                     | 觀測窗設計本身（3 個月）從未對讀者或觀察者說明              | 盲點 A |
| 「寫完但卡在中間」       | 幽靈列：工作檔誤認成文章，永卡「寫作●」（現板 4/6 列）      | 盲點 C |
| 同上                     | 身份分裂：已出刊文章的 codename 卡片顯示「去做 projection」 | 盲點 B |
| 同上                     | 帳本凍結：revise/in-progress 蓋章後，後續完成不重蓋         | 盲點 B |
| 同上                     | verify 判定 key bug：兩審全過仍永遠 in-progress             | §2.2   |

## 五、修復 roadmap（建議優先序；均未動工，待哲宇拍板）

| #   | 修復                                                                                                                                               | 量級    | 效果                                 |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------ |
| 1   | verify key bug（L342-345 `stage35`→`stage5`）                                                                                                      | 一行    | 修掉唯一的純程式錯誤                 |
| 2   | 幽靈列過濾：`-closing`／`-factcheck`／`-evolve-blocks` 等工作檔後綴不生獨立卡片（或歸併到母文章）                                                  | 小      | 產線看板立即從 6 列降到 2 列真實在製 |
| 3   | projection 版本感知：讀 `supersedes` 或比照 room 區塊取最新                                                                                        | 小      | making-of 不再展示被否決的藍圖       |
| 4   | slug 歸戶：ship 時補 `researchReport:` frontmatter 進 knowledge 檔（REWRITE Stage 4 checklist 一條）＋為現有 6 組分裂補欄位                        | 小＋SOP | 消除身份分裂                         |
| 5   | 月槽視窗改「滑動 90 天」或至少月界平滑＋覆蓋率 sanity gate（前次 -20% 即 alert）                                                                   | 中      | 斷崖不再無聲                         |
| 6   | 帳本語義：同 status 重做時以內容雜湊變化產生新事件（或記 `reship` 事件）                                                                           | 中      | 重寫史可見、wall-clock 不失真        |
| 7   | HANDOFF 規則二選一：承認現實改為「daily routine 兜底即可」（減法），或做成 post-commit hook 自動化（加法）——現在的「寫了沒人遵守的鐵律」是最差狀態 | 決策    | 誠實                                 |
| 8   | 10 份靜默跳過的 room 檔補 `slug:`；`ARTICLE-DONE-LOG` 補到當日                                                                                     | 維運    | —                                    |
| 9   | 設計文件補一段「範圍邊界」：SPORE/MAINTAINER/BABEL 明文不在 scope                                                                                  | 一段    | 空白變劃界                           |

**需要哲宇拍板的**：#5 的視窗語義（3 個月是產品決策不是 bug）、#7 的規則路線（減法 vs 自動化）、以及是否把「編輯台自身健康」加進 weekly 反省迴路（self-evolve-weekly 加一條 newsroom 覆蓋率 sanity 檢查）。

## 附錄：關鍵檔案

`src/pages/semiont/newsroom.astro`(807)／`newsroom/[slug].astro`(718)／`src/components/NewsroomTrail.astro`(181)／`src/lib/newsroom-lookup.ts`(119)／`semiont-newsroom.ts`(524)／`scripts/core/generate-newsroom-data.py`(590)／`reports/newsroom/stage-events.jsonl`(748 行)／設計 SSOT `reports/newsroom-orchestration-design-2026-07-16.md`／dogfood `reports/dogfood-v9-first-run-2026-07-16.md`／v9.5 設計 `reports/design-rewrite-throughput-2026-07-26.md`

---

_研究執行：2026-08-06，主 session（Fable）＋3 Sonnet 研究席。發現中「帳本補登污染 wall-clock」「v3/v4 多版本藍圖」兩項的肇因包含本 session 自己 8/5-8/6 的馬祖工作——如實記錄。_

---

## 六、修復落地記錄（同日，/goal 完整自我進化）

哲宇以 `/goal 完整自我進化` 授權閉環。roadmap 執行狀態：

| #   | 修復                                     | 狀態                                                                                                                                                                                                                   |
| --- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | verify key bug                           | ✅ 修復並實測（行道樹／蔡英文／大罷免 verify=done）                                                                                                                                                                    |
| 2   | 幽靈列過濾                               | ✅ 五張幽靈卡歸戶母 slug，看板產線從 6 列降到 2 列真實在製                                                                                                                                                             |
| 3   | projection 版本感知（supersedes＋mtime） | ✅ 馬祖 artifact 實測指向 v4                                                                                                                                                                                           |
| 4   | slug 歸戶                                | ✅ 馬祖補 `researchReport:`（副效果：QF1 逐字保真檢查從此常駐啟動，並回寫 6 條修訂輪引語進 SSOT §9）；Stage 4 checklist 加一條；殘卡降級為無害重複（shipped），誤導消除。重複卡合併留待生成器 identity merge（future） |
| 5   | 視窗＋sanity 儀器                        | ✅ RESEARCH_MONTHS 3→4（覆蓋回升 273，斷崖前 270 之上）＋`board-count.log` 每 run 落地、跌 >20% 發 ⚠️（已壓力測試觸發）。完整 rolling-window 留 future                                                                 |
| 6   | 帳本 reship 語義                         | ✅ ship 站記 content sha12，變更即 append 新事件；向前生效、不回填不灌水                                                                                                                                               |
| 7   | HANDOFF 路線                             | ✅ 裁決：規則保留＋誠實註記寫進 REWRITE-PIPELINE §派發鐵律（首測遵循率 5%、daily 兜底為實況、**禁止跨日事後補登**）                                                                                                    |
| 8   | 維運補登                                 | ✅ 吳明益＋10 份靜默 room 檔補 slug/room frontmatter；靜默跳過改 warning；ARTICLE-DONE-LOG 補 5 條至當日                                                                                                               |
| 9   | 範圍邊界明文                             | ✅ generator docstring 補記（SPORE/MAINTAINER/BABEL 不在 scope 及原因）                                                                                                                                                |

自我進化迴路同步閉合：LESSONS ×2（`degradation-logged-daily-never-escalated`／`remedy-compliance-unmeasured`）、本報告歸檔、canonical 回寫（REWRITE-PIPELINE＋STAGE-4）、全部修補經主 session 獨立驗收（非 self-report 採信）。
