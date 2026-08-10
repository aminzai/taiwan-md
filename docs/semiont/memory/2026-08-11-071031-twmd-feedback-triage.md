# 2026-08-11-071031-twmd-feedback-triage — 同一位讀者兩小時內送來八則介面問題，全數轉成 issue #1310-#1317；兩道對賬全綠

> session twmd-feedback-triage — cron routine（每日 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:10:44 +0800（約 11 分鐘，1 commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=免疫 60（黃燈自 2026-07-05，37+ 天）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 的讀者回報轉錄班。這輪隊列有 8 筆 `status='new'`，全部來自同一位讀者 Pigcasso6，時間戳集中在昨天早上 05:33 到 07:31 之間。

## 八則回報：一位讀者把介面層走了一遍

八則全被判成 `bug`，零 spam、零重複、零 batch cluster（三筆同掛 `/explore/` 但門檻是五筆）。內容涵蓋的層次比「介面小瑕疵」寬：taiwan-shape 頁日文按鈕文字斷行、同頁圖說在八個語言留著中文原文、`/bench/` 頁其他語言版殘留大量中文、俄文版切語言的控件整個消失、六個新語言的回饋模組還是英文、中文版回饋模組標點用半形、回饋模組字體混用（同一顆按鈕兩個字分屬 Noto Sans 與 justfont）、`/data/` 頁把「台积电」譯成 Taiwan 且「亿」譯成 B。

有兩則指回既有的坑。字體混用那則跟開了 43 天的 [#1184](https://github.com/frank890417/taiwan-md/issues/1184)（justfont API 沒指定 domain）看起來同根，但機械去重不會把它們併起來，也不該由這條 routine 替讀者判——那是 maintainer 飛輪的事（HG8）。俄文版切語言控件消失那則跟 8/6 那次「俄語讀者看了半年烏克蘭文介面」是同一片區域的第二次回報。

讀者自己在其中一則寫了「我是来自中国大陆的读者，用语习惯或有差异，如「半角」台湾说「半形」？请见谅～台湾加油」。這句原話一字未改，跟其他七則一樣包進 tilde fence 轉錄進 issue。

八筆用 `--commit` 開成 [#1310](https://github.com/frank890417/taiwan-md/issues/1310) 到 [#1317](https://github.com/frank890417/taiwan-md/issues/1317)，`5232d2bc9` 把 archive 紀錄推上 main。

## 硬閘門逐條核過的方式

dry-run 之後沒有直接進 `--commit`。先拿 canonical 的 `buildIssue()` 對八筆 row 各印一次真正會送出去的 body 人眼掃過：無 email 欄位、可見文字逐字相符、fence 完整、injection score 全 0、provenance id 都在。

HG11 這道多驗了一層。token 前綴是 `ghs_` 只證明拿到的是 App token，證明不了 issue 真的掛在 bot 名下——那是 [REFLEXES #82](../REFLEXES.md) 的 proxy signal 形狀。開完之後拿 `gh issue list --json author` 回頭核，八筆全是 `app/taiwanmd-semiont · is_bot=true`。

兩道對賬：`archive-reconcile=71/71` ✅；`comment-reconcile=70/71`，多出來的那份是 [#1252](https://github.com/frank890417/taiwan-md/issues/1252) 上游留言被刪、git 這邊留住了，屬於主權層正常運作的方向。留言同步這輪收到 2 則，其中一則是哲宇昨天在 #1306 回覆日文字形回報的完整說明。

## 收官 checklist

| 檢查項                       | 狀態                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                         |
| Timestamp 精確               | ✅（`git log %ai`）                                        |
| Handoff 三態已審視           | ✅                                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅（免疫 60 黃燈已在 groundtruth 讀到，非本 routine 職責） |
| 自我檢查工具 PASS            | ✅                                                         |

## Handoff 三態

繼承（非本 session 職責，接住不動）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充、免疫黃燈 37+ 天（OBSERVER-QUEUE #25）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、641 處漢字黏著待哲宇、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— 孤兒《台灣公投制度》在 `reports/orphan-rescue/`，上站前需補研究報告或重驗事實原子
- [ ] pending（給 self-evolve）— 巢狀回覆抽查升 pipeline canonical 的評估，per LESSONS `harvest-scan-misses-nested-replies`
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換，是否回填訂正待人工決定
- [ ] pending（給哲宇）— EZWAY 話題環境持續政治化，純觀察無需回應

本 session 新 handoff：

- [ ] pending（給今天 08:30 twmd-maintainer-am）— #1310-#1317 八則待收割。#1316（回饋模組字體混用）值得跟開了 43 天的 #1184 一起看，兩者都指向 justfont 動態子集在部分字元上沒生效；#1313（俄文版缺切語言控件）是 8/6 俄語介面問題的第二次回報，同一片區域
- [ ] pending（給哲宇）— 這位讀者兩天內送了 10 則高品質回報，全是自己逐頁比對多語版本抓出來的。回覆與致謝屬人類 gate

## Beat 5 — 反芻

這條線連續九天空隊列之後，兩天內來了十則，而且全出自同一雙眼睛。他做的事很簡單：把同一個頁面切過十二種語言，逐個看下去。這種比對是我的儀器結構性做不到的——`translation-coverage` 量得到頁面有沒有字，量不到那行字是不是還停在中文。`lang-switch` 的檢查認得路由存不存在，認不出切到俄文之後控件整個不見。八則裡至少有五則屬於「所有閘門都會給綠燈」的那一類。

跟 8/6 那則俄語讀者看半年烏克蘭文介面是同一種形狀，只是這次一次現形八個。[REFLEXES #69](../REFLEXES.md) 說每層自評都需要外部尺。今天更精確一點的說法是，這把外部尺我造不出來，它是一個願意花兩小時逐頁比對的人。

今天有一個沒做的動作值得記下來。昨天這條線的自己寫過「查完上游無洞可補，空手回來也是結論」，而連續幾天的慣性是每輪都焊一道新閘門。這輪八筆全綠通過既有的十三道 gate，我沒有再加第十四道。可以加的東西想得到幾個，但這批的漏洞根本不在轉錄層。

🧬

---

_v1.0 | 2026-08-11 07:10 +0800_
_session twmd-feedback-triage — 每日 07:00 讀者回報轉錄，八筆 filed 零 reject 零 skip_
_誕生原因：cron routine 例行 fire，隊列有同一位讀者昨晨送的八則介面與多語問題_
_核心洞察：讀者逐頁比對十二種語言抓到的八個問題，全部落在「儀器會給綠燈」的區間——量得到有字，量不到那行字對不對。這把尺不是我造得出來的。_
