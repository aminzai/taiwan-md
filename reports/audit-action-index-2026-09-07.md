# 深度檢查行動索引（2026-09-07 快照）

這份索引只提供入口，不複製排程、審稿或部署規則；各入口所指文件仍是唯一規範來源。完成證據與限制見[本輪實作紀錄](design-audit-upgrade-2026-09-07.md)。

| 要做的事       | 唯一入口                                                   | 本輪使用方式                     |
| -------------- | ---------------------------------------------------------- | -------------------------------- |
| 甦醒與選擇模式 | [BECOME](../BECOME_TAIWANMD.md)                            | 揭露實際載入範圍，不冒稱完整通過 |
| 檢查問題與投稿 | [MAINTAINER](../docs/pipelines/MAINTAINER-PIPELINE.md)     | 以具體失敗與復現驗收             |
| 改善工程與設計 | [EVOLVE](../docs/pipelines/EVOLVE-PIPELINE.md)             | 設計稿先落檔，再實作             |
| 查核文章       | [FACTCHECK](../docs/pipelines/FACTCHECK-PIPELINE.md)       | 原住民歌手逐項來源處置           |
| 重寫文章       | [REWRITE](../docs/pipelines/REWRITE-PIPELINE.md)           | 補鏈與重寫分開記錄               |
| 校正翻譯       | [TRANSLATION](../docs/pipelines/TRANSLATION-PIPELINE.md)   | 來源變更保留待同步標記           |
| 更新儀表板     | [DATA-REFRESH](../docs/pipelines/DATA-REFRESH-PIPELINE.md) | 擷取時間、資料日期、生成時間分開 |
| 管理排程       | [ROUTINE](../docs/semiont/ROUTINE.md)                      | 三條手動決策由同檔機器區塊提供   |
| 記錄交接       | [MEMORY](../docs/pipelines/MEMORY-PIPELINE.md)             | 已部署、待驗證、登入阻塞分開     |
| 記錄反思       | [DIARY](../docs/pipelines/DIARY-PIPELINE.md)               | 反思回扣文章，不抄工程日誌       |

## 甦醒載入成本

對本輪 `.taiwanmd/wake-context.latest.md` 做 UTF-8 體積量測：[原始數值](project-deep-audit-2026-09-07/wake-load-cost.json)。共 1,333 行、231,906 bytes；11 個區段裡，neural 為 71,190 bytes，manifesto-core 為 59,468 bytes。兩段合計約占 56%。這是檔案體積，沒有換算成模型 token，也不代表已完整讀過。

先改善入口的精準度：依任務讀規範、必要上下文與繼承交接，記錄讀取範圍。若再做甦醒流程瘦身，應拿同一任務比較漏讀率與決策正確率，不能只追求較小檔案。本輪尚未完成 Full BECOME 全套載入與 14 題自測，因此不記完整甦醒綠燈。

## 綠燈名稱

「型別檢查通過」只表示三個工程專案的編譯契約通過。「依賴稽核通過」指此次 npm 公告資料庫未回報漏洞。「前置資料驗證通過」指欄位與命名契約。「字串存在率」不代表翻譯正確。「能力指標」不代表執行健康。「正式部署通過」必須有版本與真實請求證據。這些名稱不可互相替代。
