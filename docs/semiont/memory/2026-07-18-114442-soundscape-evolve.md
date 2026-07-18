# 2026-07-18-114442-soundscape-evolve — /soundscape 完整進化：六語補齊、iigmir 孤兒錄音救援、sound_play 埋點、en 同名雙文分家

> session soundscape-evolve — 哲宇 `/twmd-evolve 完整進化 https://taiwan.md/soundscape/` 觸發，Full mode BECOME
> Session span: 11:44:42 → 12:09:19 +0800（約 25 分實作 + 前段 35 分甦醒與三源診斷，4 commits + 收官）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=full / 8 organ 最低=免疫 60（wake-context groundtruth 齡 0h）/ Q5/Q6/Q13/Q14=PASS

## 觸發

哲宇點名 /soundscape/ 頁完整進化。走 EVOLVE-PIPELINE observer mode：三源數據先行，診斷出的每個訊號直接執行，不進 INBOX 排隊。

## 三源訊號與診斷

GA 30d：/soundscape/ 320 views、跳出率只有 12.8%、有機 facebook 分享 36 users，頁面本身是健康漏斗；/en/soundscape/ 讀者平均停留 92 秒，但所有深度文章連結都通往中文文章。事件面 376 次 page_view 只有 11 次泛用 click，21 段錄音的播放行為完全沒被量測。SC 90d：/en/music/taiwan-soundscape/ 384 次曝光點閱率 0.5%（排名 8.4），跟 /en/culture/ 的同名新文互相蠶食；已改名的舊 slug soundscape-of-taiwan 還握著 87 次曝光、全數 404。GitHub 面挖出這次最值得處理的一條：PR #559（iigmir，2026-04-19 merged）的台中大里街聲錄音躺在 legacy `assets/sounds/` 三個月從未上頁，因為那裡的 README 還在教貢獻者把檔案放進網站不讀的資料夾。另 GA 的 `/soundscape/靜宜校園聲景地圖：https://…` 鬼 URL 4 views 查無 repo 內生成源，判定外部殘響不修。

## 執行

頁面本體（`8d70e4736`）：fr/es 各 89 個欄位在地化由 Sonnet 分身完成、我逐項驗收，驗收時抓到 es 頁殼寫著 `lang="fr"` 的複製貼上 bug——過去雙語都 fallback 中文所以隱形，今天翻譯補齊反而會讓西語頁說法文，在上線前攔下。六分類文章連結改語言感知（`articlePath()` 解析統一 slug），urban 與捷運分類改指向聲景研究者共創的新文，hero 雙鏈兩篇姊妹作。iigmir 的錄音搬進 public/、以他自己在 README 表格裡寫的描述上頁（六語），legacy README 改寫成指向正路的告示。sound_play 埋點一次播放一發、`once` 防重複，dev 實測 param 全對。

儀器與文章層（`a468b4279` + `014520246` + `7b9151d00`）：sound_file/sound_category 進 register-ga4 SSOT 且 GA4 Admin 維度已實建，instrumentation-audit 掃描清單納入聲景 template、靜態對賬零 ERROR。en 舊文改題 Taiwan's Sound Landscape 與新文分家、description 直接回答搜尋意圖，兩篇 zh 文互鏈補齊並都加 /soundscape 入口，soundscape-of-taiwan 兩條 301 進 redirect。完整 build 7,902 頁、URL 契約 0 dead，暗色模式與 zh/en/ja/fr/es 五語頁瀏覽器逐一驗過。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅（git log %ai）                          |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官級變化，不需更新）               |
| 自我檢查工具 PASS            | ✅（prettier / article-health / URL 契約） |

## Handoff 三態

繼承 2026-07-18-110122-manual：

- [x] ~~68 檔近 2 萬行未 commit 改動需哲宇過目~~ retired by soundscape-evolve：查證該批已在 `9c5ad569a`（經濟奇蹟三篇合一）落地，主 wd 殘餘為派生檔 regen 與他人 session 的 shopping-design 未追蹤檔
- [ ] task_bd7ae318（26 篇延伸閱讀連結格式壞掉）仍待認領
- [ ] veto 清單四項在 dogfood 報告尾端等哲宇（highered-evolve 承諾，續 carry）

本 session 新 handoff：

- [ ] sound_play 維度 D+2 對賬：部署兩天後跑 `ga-query.py --dims customEvent:sound_file --metrics eventCount` 確認資料進來（GA4 維度已建，歷史不回補）
- [ ] 主 wd 有他人 session 的 `knowledge/{en,ja}/Culture/shopping-design.md` 未追蹤檔＋派生檔 regen 未 commit，本 session 未碰，下個進主 wd 的 session 先 `git status` 釐清
- [ ] es 殼 `lang="fr"` 這種複製貼上錯誤全站可能還有同型（六語 × 多 feature 頁的 lang prop 無 lint），造尺候選

## Beat 5 — 反芻

這次三源交叉最值錢的訊號不在數據源裡，在 GitHub 的舊 PR 堆裡：一個被好好感謝過的貢獻者，作品被系統的門牌指進沒人看的房間三個月。詳細反芻寫進 diary〈[兩個洞都是被善意藏起來的](../diary/2026-07-18-114442-soundscape-evolve.md)〉：fallback 讓 es 殼的錯 lang 隱形、merge-first 讓孤兒錄音隱形，兩個洞共享同一種結構。

🧬

---

_v1.0 | 2026-07-18 12:10 +0800_
_session soundscape-evolve — /soundscape 完整進化（六語、互鏈、埋點、SEO 分家、孤兒救援）_
_誕生原因：哲宇 /twmd-evolve 點名聲景頁_
_核心洞察：(1) fallback 與 merge-first 這類善意機制同時是盲區製造機 (2) 貢獻入口的過時指引比沒有指引更傷（會主動把人導進死路）(3) 翻譯補齊會讓潛伏的 lang 錯置從隱形變可見，補齊前驗一次殼_
