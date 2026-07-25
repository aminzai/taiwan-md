# mouhouse 孤兒譯文隔離區（2026-07-26）

## 這批是什麼

2026-07-25 深夜在營運機 mouhouse 的工作樹撈到 24 個未追蹤檔，逐檔對過 `origin/main`
**一個都不在 git 裡**——是 babel 暫停前產出、dispatcher 沒 commit 就停了的譯文。
如果那台被 `git clean` 或重裝，這批就沒了。

指揮部把它們搬回來過閘：先跑 `heal-passthrough-fields.py` 補機械欄位（image /
imageCredit / difficulty / category 全部沒抄過去），再跑三道閘。

- **16 篇 hard=0 已落地**（唯一的 warn 是 `translation ratio: verdict unclear`——
  hi / vi / id / pt 這四個新語言的 ratio band 還沒校準，即 OBSERVER-QUEUE #19）
- **6 份留在這裡**（下方逐筆）

## 為什麼隔離而不刪

`raw 永不刪除`。這些是真實產出，只是沒過閘；刪掉等於把「哪裡出錯」的證據一起丟了。
修好之後從這裡搬回 `knowledge/{lang}/...` 即可，不需要重翻。

## 逐筆

| 檔案                                                                         | hard fail                                                                   | 怎麼修                                                                                                                 |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `hi__Technology__mini-taiwan-pulse-civic-tech.md`                            | tags 10 個有 5 個沒翻（公民科技／開放資料／資料視覺化／開源專案／人工智慧） | 翻 tags 後重跑 verify                                                                                                  |
| `pt__People__zun.md`                                                         | tags 6 個有 1 個沒翻（人生肥宅）                                            | 同上                                                                                                                   |
| `vi__People__andre-chiang-taiwanese-culinary-innovator.md`                   | tags 7 個有 6 個沒翻（人物／江振誠／名廚／米其林／餐飲）                    | 同上                                                                                                                   |
| `id__Culture__taiwanese-tea-culture-and-living-aesthetics.md`                | `frontmatter not untranslated: description`                                 | ⚠️ **可疑的假陽性**：description 實際是印尼文（`Pada zaman Qing, para tuan tan…`）。要先查檢查器判準是什麼，不要照著改 |
| `vi__Economy__industrial-transformation-from-manufacturing-to-innovation.md` | 同上                                                                        | ⚠️ 同上，description 是越南文（`Cấu trúc ngành công nghiệp Đài…`）                                                     |
| `id__Culture__taiwan-tea-ceremony-and-aesthetic-living.DUPLICATE.md`         | 非 fail，是**重複**                                                         | 本機算力軍團用分段引擎重譯了同一篇（15,188 bytes），mouhouse 這份 16,379 bytes。留新的、存舊的；要比對品質時看這份     |

## 下一步

tags 那三筆是機械性缺口，`--slug-map` 那種等級的修補。description 那兩筆先查檢查器
再動手——**兩個獨立檔案同時觸發同一條規則，比較像規則有問題而不是兩篇同時寫錯**。
