# Rewrite Guide 實跑紀錄

日期：2026-09-07。設計先提交於 `dddcd2286`，然後實作。這批材料是六篇比較研究後的局部工具試跑，不是新版全面品質證明。

## 閱讀順序

1. [研究證據](../rewrite-evolution-evidence-2026-09-07.md)：六篇對照、版本、替代解釋。
2. [使用協議](../../docs/pipelines/REWRITE-GUIDE.md)：agent 的 next / submit / review / backtrack。
3. [第三版試稿](ezway-section/draft-v3.md)：局部方向比較，線上原文未因此替換。
4. [互動工作台](ezway-section/workbench-final.html)：展開工件、裁決與回退事件。
5. [原始 run 快照](ezway-section/run-final.json)：機器可讀的提交與版本紀錄。

## 真實經過

原稿「官方開記者會，其他人只剩據轉述」從研究查無推論其他群體沒有聲音。重新取得兩篇關務署原始材料後，改為觀察預先委任的具體作業問題；不把這兩篇當成免稅門檻議題或所有業者的完整聲音。

`article_comparison` 的編輯裁決先退回 orient（確認後報關不等於所有貨件確認後出貨），再退回 compose（既有作法與倉容預估混在一起、引用位置錯位）。`guide_cold_reader` 使用未讀藍圖與研究的 context，指出費用分岔、名詞入口與重複結尾。v2 修正後曾被接受為局部試稿。

接著瀏覽器暴露 `[1][2]` 被 Markdown 當作單一引用的實際缺陷。原本的渲染檢查太弱，這次沒有隱藏它：工具回退 compose，原 cold-read／verify／release 失效，v3 分開引用並採用兩項文字精度建議。新回歸測試驗三個引用位置與目的地；瀏覽器另驗 AX tree、DOM 與畫面。交付編輯在未收到新證據前 block，收到後才重新裁決。

## 證據的界限

- 這是主代理代理提交具名外部評閱的實際操作紀錄。部分編輯在同一回合先判讀多個階段，主代理再依順序寫入；事件時間是工具收件時間，不是寫作、搜尋或獨立思考耗時。
- 有些較早的預讀回饋發生於正式 cold-read 階段前，原檔保留，但不偽造為當時已循序通關。
- v2／v3 是同一位未讀藍圖讀者的複讀，非每版都找全新首次盲測。不同 actor 名稱不提供身份認證。
- 所有快照均包含文字與 hash；`ezway-section/` 排除自動格式化，避免已被審閱的證據在 commit 時悄悄改位元組。這不是排除測試。
- 只有 section 交付，沒有完整文章修復、正式發布或真人品味認可。短稿主要驗證推論收窄與交接，不證明長篇敘事已解決。
- 舊版 workbench.html、run-snapshot.json、render-check.txt 是歷史證據，尤其原渲染檢查漏錯不可視為最終狀態。最新結果見帶 final／v3 檔案。

## 工程驗證

[protocol-tests.txt](protocol-tests.txt)：14 組測試，涵蓋錯階段、舊任務、自審、stale、回退、阻擋、冷讀污染、路徑與儲存 symlink、寫入鎖、HTML escape、CLI 錯誤 JSON、已重現的引用渲染缺陷。

[contracts.txt](contracts.txt)：本輪完整工程契約通過，包含最終 14 組 guide 測試。[types.txt](types.txt)：672 檔、0 errors。瀏覽器範圍見 [browser-check-v3.md](ezway-section/browser-check-v3.md)。不把這些檢查換算成文章品質分數。

## 協議審查後的再收件

`pipeline_history` 用反例發現審稿證據未綁 hash、空容器可假冒必填材料。修正後新增兩組測試；同一 run 回退 orient，依當前未變的工件和具名裁決重新收件。不是重新發生六輪獨立思考，而是以加固協議重新建立有效依賴；最終六個裁決都有審稿原檔快照。舊未綁定的紀錄只作歷史，不作當前接受。最終 18 次提交、39 個操作事件，stale 為空。
