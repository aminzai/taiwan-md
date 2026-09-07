---
title: 'Rewrite Guide：可回頭的 AI 編輯工作台'
description: '從六篇對照與歷史失敗設計可互動、可恢復、可稽核的 agent 寫作協議'
type: 'design-report'
status: 'draft'
current_version: 'v1.0'
last_updated: 2026-09-07
last_session: '2026-09-07-164559-audit-upgrade'
---

# Rewrite Guide 設計

## 目標與證據

把 REWRITE 從需要 agent 記住所有步驟的文件，變成會交付當前任務、接收工件、請編輯裁決、允許退回並記住修訂原因的工具。使用者要的是聰明引導者逐步帶 AI 寫文章；程式負責可信的狀態，執行中的 AI 負責閱讀、研究與編輯判斷。不能用欄位齊全、搜尋次數或漂亮進度條冒充智慧。

研究材料與邊界見 [證據紀錄](rewrite-evolution-evidence-2026-09-07.md)。六篇是偏好樣本而非隨機樣本；不能推論退步比例，也不能歸因於單檔／拆檔或特定模型。黃魚鴞早期已有研究代理，七月拆檔前也已有形式全過而意思不對的紀錄。

確認的失敗鏈：EZ WAY 的查無結果被投影升成社會缺席、再被主編接受；演算藝術的中段平淡被「符合藍圖」合理化；黃崇仁及 EZ WAY 修訂後曾出現舊檢查仍綠但新稿錯誤的情況。食安文同樣以研究找不到推測公共討論不存在。好的早期文章讓人物與事件逐步改變讀者的理解，不只反覆證明開場的漂亮命題。

## 現況與接點

既有 `scripts/twmd.mjs` 是命令路由，`generate-newsroom-data.py` 推導文章工件與 first-observed 事件。研究報告與編輯室健康檢查器驗格式、來源登記完整度；它們沒有資格證明事實正確或讀者看懂。

2026-09-07 掃描 docs/scripts/.github/.husky/src/.claude/skills 共 431 檔提到 REWRITE 主流程或 stage。保留現有路徑、stage 錨點及歷史紀錄，主流程增加新版入口與相容關係；不批次改寫歷史日記。新 run ledger 只記工具真正發生的動作，與 newsroom 的 first-observed 時間分開。

## 發散與定案

| 方案                           | 能解決什麼                                   | 代價與盲點                                       | 決定                             |
| ------------------------------ | -------------------------------------------- | ------------------------------------------------ | -------------------------------- |
| A 瘦身單檔 prompt              | 較易整體閱讀，編輯有自由                     | 仍靠記憶交接、容易跳步，舊驗證不能自動失效       | 保留為可匯出的說明，不作執行核心 |
| B 可回頭的狀態機＋AI 編輯角色  | 任務按需發出、版本可追、每次裁決具體、可恢復 | 程式不能自行判斷文學性；需校準 AI 評閱與真人回饋 | 採用                             |
| C 全自動多代理競賽與分數排行榜 | 可平行多稿探索                               | 成本高、可能共同盲點、易把得分當作品目的         | 本版不採，未來以實際品質效益決定 |

定案依 MANIFESTO 認知負荷、外部尺與 SSOT 原則，以及 REFLEXES 69/82 的機械合規不等於意義。任務沒有 XP 或自動品質總分；遊戲感來自明確目標、可選行動、回饋與進度，獲勝條件是交出有理由推薦給讀者的成品。

## 工作協議

六個工作階段：orient（讀者問題與候選角度）→ investigate（帶來源材料與反證）→ compose（全篇草稿）→ cold-read（只看稿的讀者回述）→ verify（來源核對與機械檢查）→ release（交付決定）。每階段有 task prompt、必要輸入與 structured submission template。整篇與局部試寫 scope 分開；局部試寫永不標成文章完成。

CLI：`twmd rewrite start <article> --scope article|section`、`next <run>`、`submit <run> <json>`、`review <run> <json>`、`backtrack <run> <stage> --reason ...`、`status <run>`、`export <run> <html>`。預設 JSON 可被任意 agent 呼叫；人可直接閱讀文字與匯出工作台，不綁雲端模型、不新增 API 費用。

submit 保存工件快照與 SHA-256、提交者、當前任務版本，轉成 awaiting-review；review 必須是不同的 actor，記錄 accept/revise/block、具體理由與證據位置。不同 actor 是協議分工而非可驗證的人格獨立，不把它宣稱真正盲評。cold-read 的任務輸入只列文章，不提供作者論點；共享歷史的主代理不能宣稱自己為獨立盲讀者。

任務欄位完整只代表可收件；工具永不以欄位存在自動 accept。review 是外部 AI 或人給的具名判斷。缺證據的社會缺席命題、來源錯配、虛構場景等靠具體指令與人工裁決辨別，不造偽語意 regex。verify 分列機械執行紀錄及語意來源核對。release 只允許 ready-for-publication，沒有 deploy URL、commit 與實際遠端驗證就不稱 published；本工具不自動 git merge／社群發文。

任何被引用的工作檔改變，next/status 都能報 stale；提交及接受前重新計算依賴 hash。回退時下游接受全部失效，保留事件歷史，讓修訂能改研究問題與結構。每次交接有 run_id、attempt、event timestamp、工件 digest。單次寫入用鎖及 atomic rename，崩潰不留半份 state；錯誤輸入與未知 stage fail loud。run_id 限安全字元，工件只讀專案內正規路徑，拒絕符號連結逃逸及超大工件；不執行 JSON 內任意 shell 指令。

## 引導者怎麼問

- orient：讀者為什麼會打開？有哪些至少兩種可被材料推翻的角度？題目本身是什麼，不能只剩評論它的語言。
- investigate：每個關鍵主張由哪個原始段落支撐？哪份材料讓你改變原先想法？查無只記搜尋範圍與日期。
- compose：讓材料決定順序，必要時 backtrack 改論點；刪掉什麼及其原因另記，正文保留作者聲音與人物動作。
- cold-read：用自己的話說主題、哪個場景改變理解、哪裡困惑／重複／被強推結論；不以完成藍圖給分。
- verify：核數字的對象、單位、時間與分母，直接引語與腳註描述都對原文；矛盾先成立再判哪邊錯，檢查圖表是否誤導。
- release：為什麼值得推薦、還有哪些不確定、哪些真由人看過；若未達品質，選回退而非補一段自我辯護。

## 實作範圍與驗收

1. Node 核心、CLI、prompt registry、結構化範例與使用說明；無新增 runtime dependency。
2. 匯出有設計一致性的互動 HTML 工作台：任務地圖、工件、裁決與修訂時間線，可切換詳細內容；清楚標記 read-only snapshot。使用既有 Island Lines icon，資料一律 HTML escape，不用不可信 innerHTML。
3. 主流程與 twmd 路由接新工具；newsroom 放入口，既有發布帳本保留。
4. 協議測試涵蓋失敗路徑：錯 stage、同 actor 自審、stale、回退、錯誤 JSON、路徑穿越、並行寫入、完成前跳關。
5. EZ WAY 的「查無→不存在」段落做 section dogfood：保留原文、來源範圍、修稿與具名評閱。六篇只做可追溯失敗回放，不能以測試 replay 宣稱新文章品質普遍改善。
6. 驗收新增工具與既有命令、CI contracts、UI；完整收官記錄實際部署與尚缺的人類品質回饋。

## 風險與研究依據

工具可強制版本與程序一致性，不能保證評閱者誠實或文學品味。多代理相同模型仍可能同錯；人工偏好需要持續收回，不能讓自我打分取代使用者。

Anthropic 的 [agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) 區分執行軌跡與最終結果，並建議結合程式、模型、人類評估與真實案例；本版因此不以任務完成率作文章品質。[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) 建議只在有清楚標準與可改善的回饋時使用 evaluator–optimizer，並按需求增加複雜度。[Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/) 是 2024 年檢索與問答的 context 位置效應研究，支持按需材料設計的動機，不能直接證明本專案寫作退步的原因。

## 實作後記

本檔先提交於 `dddcd2286`，再實作四個 Node 模組、twmd 路由、13 組負向／回歸測試、說明文件與 newsroom 文件入口，無新增 runtime 依賴。

EZ WAY 局部實跑保留具名退件與 v1→v2→v3；v2 曾接受後又因瀏覽器發現引用顯示缺陷而回退，證實下游裁決失效機制有被實際使用。工件與解讀界限見 [實跑報告](rewrite-guide/README.md)。工程契約與型別檢查通過，手機工作台 390px 未水平溢出。

實作中，cold-read 允許誠實提交「已讀研究」但禁止接受，讓污染能留下 block 紀錄；未讀研究的同一讀者複讀另有 `draft-only-reread` 聲明。CLI 不驗證 actor 真實身份；這一限制保留。

品質結論限於本短節：推論與來源對位、讀者入口及引用顯示已有具體修正。未取得使用者對新稿的品質評價，未證明完整長篇的普遍提升，也未將試稿替換站上原文。

最後協議審查發現 review evidence 只有文字定位與 required field 空容器漏洞，已修為檔案快照/hash依賴與 registry 欄位型別驗證，並新增真實反例測試。當前 run 以新契約重新收件，沒有把舊未綁定裁決當完整證據。
