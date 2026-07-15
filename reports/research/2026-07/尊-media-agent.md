# 「尊」媒體素材與官方頻道查核（2026-07-15）

> 任務範圍：只查核「尊／朱玉恩」可用媒體素材，不修改 `knowledge/People/尊.md`。重點是官方 YouTube 主頻道、第二頻道、蘿倫本人頻道，以及公開可靠媒體中可溯源的新聞圖像。本文所有「仍可播放／可嵌入」判斷均是 **2026-07-15（Asia/Taipei）即時狀態**，未來仍可能因創作者改隱私或平台政策而失效。

## 一、結論先行

1. **官方主頻道**是 [人生肥宅x尊 `@loserzun`](https://www.youtube.com/@loserzun)，channel ID `UC6VKHP606ee6ffKwKmBHSig`；不是 `@zun`。2026-07-15 在 YouTube rendered DOM 中顯示「已通過驗證」、177 萬訂閱、262 部影片。官方影片索引可由 `/videos` 讀取。
2. **官方第二頻道**是 [人生魯宅x尊-第2頻道 `@nerdzun`](https://www.youtube.com/@nerdzun)，channel ID `UC-ujeda5rDgCe-910J5keTg`。rendered DOM 顯示 129 萬訂閱、835 部影片，頻道說明為「PVC公仔開箱,日常,廢文」，首頁也直接連回主頻道 `UC6VKHP606ee6ffKwKmBHSig`，這是雙向官方身分證據。
3. 最適合文章的 6 支影片都仍 public、`playable_in_embed=true`：早期黑歷史 `OUZB30lyGcc`、小玉入監前同框 `Tkf8_8_nl68`、雙百萬／獄中問答 `m5Za_ARPRx0`、蘿倫 Q&A `BDxeiny76y4`、韓國探女友 `wZCCV85V9dc`、新家 `twgMJSxS-H8`。
4. **口袋奇兵業配道歉沒有可用的官方 YouTube 道歉影片。**原始聲明是 IG 限時動態，現已過期；Newtalk、CTWANT 等新聞頁只保留翻攝截圖。不可把第二頻道 2019 年的惡搞／短片〈2年沒更新頻道的道歉申明〉誤作 2023 年爭議道歉。
5. **沒有找到可安心作 hero 的自由授權尊本人照片。**Wikidata `Q28410710` 沒有 P18、沒有 Commons category；Commons 搜尋命中的「Zun」全是青銅器等同名誤結果。官方 YouTube thumbnail、IG 圖與新聞翻攝圖均無 CC 授權。最穩策略是 hero 使用自製／委製抽象視覺；人物內容用 YouTube 原生 embed，不下載 thumbnail。
6. 若編輯堅持靜態人物圖，只能做**狹義評論性 fair use 主張**，且應選「正被評論之影片的縮圖／單幀」放在對應段落、低解析、完整署名與連結；不應拿爭議截圖當通用 hero，也不應把新聞社圖片寫成「官方授權」。

## 二、官方身分與 rendered-DOM 查核

### 2.1 主頻道

- URL：<https://www.youtube.com/@loserzun/videos>
- channel ID：`UC6VKHP606ee6ffKwKmBHSig`
- rendered DOM（2026-07-15）：heading「人生肥宅x尊，已通過驗證」、handle `@loserzun`、177 萬位訂閱者、262 部影片。
- rendered DOM 當日可見影片卡包含：
  - `twgMJSxS-H8`〈【尊】我 ! 的 ! 新 ! 家 !〉，頁面顯示約 94 萬次、7 個月前；
  - `wZCCV85V9dc`〈【尊】因為兩個月沒見到蘿倫,所以我直接飛去韓國找她 ! !〉，頁面顯示約 236 萬次；
  - 頻道首頁外部連結指向 `facebook.com/loserZUN`，與影片 description 的社群連結一致。
- 以 `yt-dlp --flat-playlist` 讀 `/videos` 得 256 個長影片條目；rendered DOM 的 262 是 YouTube 當下 UI 口徑，兩者差異可能是 newly indexed／直播／內容類型分類，不應把 CLI 個數寫成「官方總影片數」。
- `@zun` 解析到同一 channel ID 的 vanity 痕跡但顯示沒有 videos tab；**文章與來源應固定用 `@loserzun`**，避免把不穩定／占用 handle 當主網址。

### 2.2 第二頻道

- URL：<https://www.youtube.com/@nerdzun/videos>
- channel ID：`UC-ujeda5rDgCe-910J5keTg`
- rendered DOM（2026-07-15）：heading「人生魯宅x尊-第2頻道」、handle `@nerdzun`、129 萬位訂閱者、835 部影片；說明「PVC公仔開箱,日常,廢文」。
- 頻道 header 的 `YouTube` 外部連結直接指回主頻道 `https://www.youtube.com/channel/UC6VKHP606ee6ffKwKmBHSig`，可視為官方交叉認證。
- `yt-dlp --flat-playlist` 的 `/videos` 長影片索引為 658 筆；UI 的 835 很可能含 Shorts 等其他口徑。寫作時只需稱「第二頻道」，不要用離線索引數硬推已刪影片數。

### 2.3 蘿倫本人頻道

- [蘿倫 Lauren `@laurenveur`](https://www.youtube.com/@laurenveur)，channel ID `UCFtsJIdfOcIycTPCbvBm-FA`。
- `BDxeiny76y4` 的頻道、handle、description 社群連結彼此一致；description 明寫「本頻道影片皆無授權搬運」，因此只能原生 embed／連結，不可下載重傳。

## 三、優先可嵌入影片清單

所有日期來自 YouTube 公開 metadata 的 `upload_date`，不是新聞刊登日；播放狀態由 `availability=public`、`playable_in_embed=true`、`age_limit=0` 交叉確認。觀看數只保留作查核軌跡，會變動，不建議寫進文章正文。

| 用途                             | 影片 ID／官方連結                                            | 標題                                                                                  |   上傳日期 |  長度 | 2026-07-15 狀態                               | 編輯建議                                                                                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------- | ---------: | ----: | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 早期「黃毛豬／抄阿神」黑歷史     | [`OUZB30lyGcc`](https://www.youtube.com/watch?v=OUZB30lyGcc) | 〈【尊】把五年前的黑歷史影片翻出來了!?〉                                              | 2018-05-05 |  7:08 | public；可 embed；無年齡限制；約 282.6 萬觀看 | **最推薦早期段 inline embed。** description 自述「邁向拍片的第六年」與舊片合計不到兩千點閱，且影片本身由尊回看、評論自己的舊作，比二手媒體更直接。                                                                                        |
| 小玉入監前、尊談慌張與家人承擔   | [`Tkf8_8_nl68`](https://www.youtube.com/watch?v=Tkf8_8_nl68) | 〈【尊】我找了小玉一起來看小玉梗圖...【第二頻道】〉                                   | 2024-06-22 | 18:53 | public；可 embed；約 285.5 萬觀看             | 適合「不切割但不替罪行辯護」段。鏡新聞 2024-06-23 直接連回此片，報導記錄尊稱那是「人生最慌的期間」，小玉勸世不要犯罪。不要只把它形容成梗圖片。                                                                                            |
| 第二頻道百萬／獄中小玉／探監問答 | [`m5Za_ARPRx0`](https://www.youtube.com/watch?v=m5Za_ARPRx0) | 〈【尊】直接跑去監獄問小玉 ! ! 百萬訂閱,回答觀眾的你問我答30個問題 ! ? 【第二頻道】〉 | 2024-12-28 | 13:14 | public；可 embed；約 251.1 萬觀看             | **最推薦全篇核心 embed。**標題直接把「監獄」與「百萬訂閱 Q&A」放在一起；description 寫「第三個百萬頻道QA：小玉直接在我旁邊回答」，可承接雙百萬／書信式回覆。切勿寫成攝影機真的帶進監所拍小玉。                                            |
| 關係公開的一手 Q&A               | [`BDxeiny76y4`](https://www.youtube.com/watch?v=BDxeiny76y4) | 〈怎麼交往的？會結婚嗎？誠實回答50題！五萬訂閱Q&A Ft. @loserzun ｜蘿倫 Lauren〉       | 2022-05-28 | 18:15 | public；可 embed；約 137.4 萬觀看             | **蘿倫段最適合。**不是尊兩頻道上傳，而是女友本人頻道的一手素材。description 有完整 timecodes：01:13 相識、02:06 在一起、04:24 結婚、11:23 某 J／某玉事件。現有文章註腳寫 2022-05-29，metadata 是 **2022-05-28**，應校正時區／上傳日表述。 |
| 穩定關係與分隔兩地               | [`wZCCV85V9dc`](https://www.youtube.com/watch?v=wZCCV85V9dc) | 〈【尊】因為兩個月沒見到蘿倫,所以我直接飛去韓國找她 ! !〉                             | 2024-12-14 | 14:44 | public；可 embed；約 236.1 萬觀看             | 若文章要從「Q&A 公開」推進到長期日常，這支比一般情侶挑戰更有敘事性；主頻道 rendered DOM 也實際看到此卡。與 Q&A 二擇一即可，避免影音過密。                                                                                                 |
| 買房／新家                       | [`twgMJSxS-H8`](https://www.youtube.com/watch?v=twgMJSxS-H8) | 〈【尊】我 ! 的 ! 新 ! 家 !〉                                                         | 2025-12-13 | 16:10 | public；可 embed；約 94.4 萬觀看              | **新家段首選。**主頻道 rendered DOM 可見；description 自嘲「頻道上的第80個新家開箱影片」。標題與 description 本身沒有「買下第一棟房」字樣，所以若正文要斷言「購屋」須再用影片口述／其他可靠來源，不可只靠標題推論。                       |

### 次選／只適合補充

| 影片 ID                                                      | 標題與日期                                               | 判斷                                                                                                                                        |
| ------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [`eeWDNdaEgIE`](https://www.youtube.com/watch?v=eeWDNdaEgIE) | 〈【尊】我又又又又搬新家啦!!!〉，2020-06-28              | public、可 embed。description 說是紀錄當時住家並自稱「全台灣最會搬家的選手」。可與 2025 新家形成「多次搬租屋 → 新家」對照，但不是買房證據。 |
| [`gurH6B41S5k`](https://www.youtube.com/watch?v=gurH6B41S5k) | 〈【尊】2年沒更新頻道的道歉申明【第2頻道】〉，2019-11-29 | public、可 embed、僅 1:18。這是第二頻道停更復更內容，**不是口袋奇兵道歉，也不是小玉案道歉**；除非文章談頻道復活，否則不採用，避免標題誤導。 |

### 建議 embed 寫法

站內若支援既有 YouTube 元件，優先沿用元件；原始 iframe 例：

```html
<iframe
  src="https://www.youtube-nocookie.com/embed/m5Za_ARPRx0"
  title="【尊】直接跑去監獄問小玉：百萬訂閱 Q&A"
  loading="lazy"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen
>
</iframe>
```

採 `youtube-nocookie.com` 僅降低載入前追蹤，不代表影片變成可自由重製；著作權仍屬上傳者／權利人。

## 四、「百萬」與「雙百萬」的素材判斷

### 4.1 第一個百萬（2018）

- 好房網／聯合影音在 2018-08-23 至 08-24 報導尊 19 歲、主頻道約 120 萬訂閱，稱「全台最嫩百萬訂閱 YouTuber」。聯合影音頁仍在：<https://video.udn.com/news/927944>，頁面日期 2018-08-23 18:03。
- 官方主頻道現存長影片索引裡，未找到一支題名明確為「100 萬訂閱達成／百萬 Q&A」的 2018 官方影片。以關鍵詞掃 256 支主頻道與 658 支第二頻道長影片，命中的是後來的泛百萬題名、第二頻道 Q&A，不是主頻道達標影片。
- 因此第一百萬段：**事實用可靠媒體文字來源，影音用 2018-05-05 的自揭黑歷史片當人物轉折**。不要假造「百萬紀念片」。聯合影音自有 player 可作外連來源，但不是尊的官方 YouTube 上傳，亦不應擷取其畫面作 hero。

### 4.2 第二頻道百萬／雙百萬

- 官方最直接素材就是 `m5Za_ARPRx0`（2024-12-28），標題直接寫「百萬訂閱」；上傳在 `@nerdzun`，可 embed。
- 這支片的 title／description 足以證明「此第二頻道在做百萬 Q&A」，再配合當時主頻道早已破百萬，可合理稱雙頻道百萬。
- 「金紙龍船、月薪 900 元」是新聞報導與影片內容層級的細節，寫作必須把「官方影片可見」與「媒體轉述」分開。現有文章註腳所列 UDN URL `https://udn.com/news/story/7321/8492810` 在本輪 web fetch 無法安全開啟；搜尋可見 Taiwan.md 自己的摘要與後來二手站轉述，但不應用二手 SEO 文替代一手。**重寫前最好人工播放 `m5Za_ARPRx0` 核對龍船出現的確切時間點，或找到可正常開啟的 UDN 正式頁。**
- 不要把標題「直接跑去監獄問小玉」寫成監所內拍攝；實際上公開探監通常不能帶攝影器材，這是包裝語法，可能是透過信件／接見後整理答覆。

## 五、道歉與爭議素材：能用與不能用

### 5.1 2023「口袋奇兵」業配

- [Newtalk 2023-11-03](https://newtalk.tw/news/view/2023-11-03/895065) 頁面仍可讀，明確寫：賴鴻麟指控多人替《口袋奇兵》用同一支畫面配音、尊未實際遊玩；尊以 IG 限動道歉，說草率接下、把關疏忽、後來知道是「糞 game」且應更早要求下架。
- Newtalk 圖說：主圖「圖：翻攝自尊IG」；另兩張寫「翻攝自Dcard」。這些不是 Newtalk 授予 Taiwan.md 的可重用照片，更不是 CC 圖。
- 官方雙頻道題名／索引沒有 2023 年對應的「口袋奇兵道歉」影片；IG Story 已過期。**negative finding：沒有可嵌入官方道歉影片。**
- 寫法建議：用新聞文字連結與極短必要引文；若要圖，只能在該爭議段以小尺寸截圖、明確圖說「尊 2023-11-02 IG 限時動態道歉，畫面由 Newtalk 翻攝留存」並附來源，做新聞評論性 fair-use 主張。不要存成 hero、不要去背、不要裝飾性重用。

### 5.2 2021 小玉 Deepfake 案爆發後聲明

- 尊的原始回應同樣是 IG 限時動態，新聞（ETtoday、鏡週刊等）保留全文／截圖；官方 YouTube 沒有以道歉或聲明為題的長影片。
- `Tkf8_8_nl68` 是 2024-06-22、判決定讞及入監前的回看／告別，不是 2021 即時道歉。文章可 embed 它作「多年後如何面對」，但日期與功能必須分清楚。
- **negative finding：沒有仍存的官方 2021 道歉影片或永久 IG 貼文可作 iframe。**只能引用可靠媒體留存的聲明文字。

## 六、靜態圖盤點與授權處置

### 6.1 自由授權搜尋結果

- Wikidata entity `Q28410710`：沒有 `P18`（image），也沒有 `P373`（Commons category）。
- Wikimedia Commons API 以「人生肥宅x尊 OR 朱玉恩」搜尋 namespace 6，前十筆全是 `Bronze Zun`、`Jade Zun` 等「尊」器物同名結果，沒有本人。
- 中文維基頁面也標記「本地和維基數據均無相關圖片」。
- **結論：沒有找到 CC BY／CC BY-SA／CC0／公有領域的尊本人圖。**不可把同名青銅器結果誤用。

### 6.2 YouTube thumbnails

下列官方 CDN 位址在查核時可取得，但 metadata 的 `license=null`，亦即沒有 CC 授權訊號，實務上按 YouTube Standard License／權利人保留處理：

- 黑歷史：`https://i.ytimg.com/vi/OUZB30lyGcc/maxresdefault.jpg`
- 小玉入監前：`https://i.ytimg.com/vi/Tkf8_8_nl68/maxresdefault.jpg`
- 雙百萬探監：`https://i.ytimg.com/vi/m5Za_ARPRx0/maxresdefault.jpg`
- 新家：`https://i.ytimg.com/vi/twgMJSxS-H8/maxresdefault.jpg`
- 韓國找蘿倫：`https://i.ytimg.com/vi/wZCCV85V9dc/maxresdefault.jpg`
- 蘿倫 Q&A：`https://i.ytimg.com/vi/BDxeiny76y4/sddefault.jpg`

**授權處置：**

1. 最佳：只用原生 YouTube embed，縮圖由 YouTube player 載入，不下載進 repo。
2. 次佳：若站內需要 poster，先向創作者／魔競娛樂取得書面授權；留存授權範圍、期限、媒體、可否裁切。
3. 風險接受下的 fair use：僅在評論該特定影片時，保存最低足夠解析、單次使用、附「Video thumbnail: 人生肥宅x尊／YouTube，影片連結」；不要當人物通用 hero，不做社群二次宣傳，不移除浮水印／標題文字。
4. YouTube thumbnail URL 是技術可取用，不等於法律授權；不得在 credit 寫「Courtesy YouTube」假裝 YouTube 授權內容。

### 6.3 新聞圖片

- Newtalk 口袋奇兵頁主圖是「翻攝自尊IG」，另圖翻攝 Dcard：只能在評論該爭議時主張必要引用，不能當清流／人物形象 hero。
- [鏡新聞 2024-06-23](https://www.mnews.tw/story/20240623nm011) 的小玉圖標為「資料畫面」，頁腳為鏡電視版權所有；沒有開放授權。可連結文章，不可下載搬運，除非取得鏡電視授權。
- [聯合影音 2018-08-23](https://video.udn.com/news/927944) 的新聞圖片／影片 frame 屬聯合報系；頁面沒有 CC 聲明。可引作來源，不可直接作 hero。
- IG 照片即使是本人公開發布，也仍由拍攝者／帳號權利人保有著作權；「官方頁」不等於「自由素材庫」。

### 6.4 Hero 建議（由低風險到高風險）

1. **低風險推薦：自製抽象 hero。**以「雙頻道」為概念，兩個播放視窗／兩條時間軸／百萬計數器／金紙龍船的抽象剪影組合；不得直接臨摹官方 thumbnail 或人物肖像。credit：`Illustration: Taiwan.md`。
2. **可談授權：向尊或經紀窗口索取官方 press kit portrait。**影片 description 的合作信箱為 `just8080666@gmail.com`；2023 年曾有魔競娛樂合作報導，但本輪未找到公開 press kit 與可下載授權條款。拿到圖後 credit 應依書面要求，不自行寫 CC。
3. **有爭議、只限 inline：影片 thumbnail 或新聞截圖的狹義 fair use。**必須有相鄰文字直接評論畫面／事件，低解析且不替代原作市場。
4. **不建議：以口袋奇兵道歉截圖、Deepfake 新聞圖或小玉監所圖作人物 hero。**會把尊整體人物介紹綁在他人犯罪／單一爭議上，也最難滿足必要性與比例性。

## 七、逐項 negative findings（務必保留給主撰稿）

1. `@zun` 不是穩定的官方影片入口；正確主 handle 是 `@loserzun`。
2. 主頻道沒有找到明確題名為「2018 百萬達成」的現存官方長影片；不能憑媒體里程碑杜撰百萬紀念片。
3. 2023 口袋奇兵道歉沒有官方 YouTube 影片；原聲明為過期 IG Story。
4. 2021 小玉案爆發後道歉沒有官方 YouTube 影片；原聲明同為 IG Story／新聞翻攝。
5. `gurH6B41S5k` 的「道歉申明」只是 2019 第二頻道停更題材，不是任何上述爭議道歉。
6. `m5Za_ARPRx0` 標題的「直接跑去監獄問」不能當作監所內實拍證據；需人工看完整片確認問答機制與龍船時間點。
7. `twgMJSxS-H8` 確實存在、2025-12-13 上傳、目前可 embed；但標題／description 單獨只證「新家」，沒有明寫「買房」，購屋斷言須另外核對片中口述或可靠報導。
8. 現有文章註腳把蘿倫 Q&A 日期寫 2022-05-29；YouTube metadata 為 2022-05-28。若因台灣頁面顯示跨日，正文宜寫「2022 年 5 月下旬」或以 metadata 日期為準並註時區。
9. 沒有自由授權人物照片；Wikidata／Commons 均無本人圖。搜尋到的 `Zun` CC0 圖是青銅器，不是 YouTuber。
10. YouTube thumbnail 可讀取、可顯示不等於可下載再授權；所有候選 metadata `license=null`，不能標 CC。
11. Newtalk 的口袋奇兵圖片是二次翻攝 IG／Dcard；新聞社頁面也未授權再利用。不能把「圖：翻攝」誤寫成「Newtalk 授權」。
12. 鏡新聞／聯合影音有可靠新聞價值，但其圖片與影片均保留版權；適合作來源連結，不適合搬入 repo。

## 八、建議最終影音節奏

若文章只能放 3 支，優先順序：

1. `OUZB30lyGcc`：本人回看黑歷史，提供起點；
2. `m5Za_ARPRx0`：第二頻道百萬＋監獄問答，提供最有張力的中後段；
3. `twgMJSxS-H8`：新家，提供時間軸收束。

若可放第 4 支，再加 `BDxeiny76y4`，因為是蘿倫本人頻道的一手關係 Q&A；`wZCCV85V9dc` 則作二擇一的生活化替代。`Tkf8_8_nl68` 只在文章深寫小玉入監前心境時加入，否則會令兄長案件佔比過重。

## 九、來源與搜索軌跡

### 官方／平台一手

1. YouTube 主頻道：<https://www.youtube.com/@loserzun/videos>（rendered DOM 及 flat playlist）。
2. YouTube 第二頻道：<https://www.youtube.com/@nerdzun/videos>（rendered DOM 及 flat playlist）。
3. YouTube individual video metadata：上述 8 支 watch URL，以 `yt-dlp --skip-download --dump-single-json` 查 `id/title/upload_date/channel_id/uploader_id/availability/playable_in_embed/age_limit/license`。
4. YouTube rendered DOM：Chrome 實際載入兩頻道 `/videos`；主頻道抓到 verified heading、handle、訂閱數、影片數與 `twgMJSxS-H8`／`wZCCV85V9dc` 卡片；第二頻道抓到 handle、訂閱數、影片數、說明及回主頻道連結。
5. Wikidata API：`wbgetentities&sites=zhwiki&titles=人生肥宅x尊&props=claims|sitelinks` → `Q28410710` 無 P18/P373。
6. Commons API：`generator=search&gsrsearch=人生肥宅x尊 OR 朱玉恩&gsrnamespace=6` → 無本人圖，僅同名器物。

### 可靠媒體／交叉佐證

7. [聯合影音：全台最嫩百萬訂閱YouTuber 人生肥宅x尊來惹](https://video.udn.com/news/927944)，2018-08-23。
8. [好房網：人生肥宅x尊 登「全台最嫩百萬YT訂閱主」全靠這招](https://news.housefun.com.tw/news/article/amp/196239205065.html)，搜尋摘要顯示 2018-08-24；本輪頁面 403，故只作里程碑交叉佐證，不擷取圖片。
9. [台灣達人秀：自嘲從抄襲阿神起家](https://www.ttshow.tw/articles/48444)，2018-05-07；與官方 `OUZB30lyGcc` 互證黑歷史脈絡。
10. [Newtalk：百萬YTB「尊」遭爆手遊業配造假](https://newtalk.tw/news/view/2023-11-03/895065)，2023-11-03；頁面正文與圖說均可讀。
11. [鏡新聞：小玉服刑前畫面曝光](https://www.mnews.tw/story/20240623nm011)，2024-06-23；正文直接連 `Tkf8_8_nl68`，並引尊、小玉談話。
12. 中文維基「人生肥宅x尊」只用來發現官方 channel links 與 Wikidata entity；其人物里程碑敘述有「2017／2018」矛盾，不能當唯一日期來源。

### 實際查詢字串／命令摘要

- 搜尋：`site:youtube.com/watch 人生魯宅x尊 黑歷史`、`尊 第二頻道 百萬 小玉 探監 金紙龍船`、`尊 蘿倫 官方 YouTube 交往 Q&A`、`尊 100萬訂閱 2018 影片`。
- 頻道索引：`yt-dlp --flat-playlist --dump-single-json https://www.youtube.com/@loserzun/videos`；第二頻道同理。
- 關鍵詞掃描：`黑歷史|百萬|道歉|爭議|探監|監獄|小玉|新家|房子|蘿倫|女友|哥哥|龍船|金紙|黃毛豬|口袋奇兵|訂閱`。
- 單片狀態：`yt-dlp --skip-download --dump-single-json https://www.youtube.com/watch?v=VIDEO_ID`。
- 關鍵判定欄位：`availability=public`、`playable_in_embed=true`、`age_limit=0`；`license=null` 視為未授予 CC，不作自由授權聲明。

## 十、交付給主撰稿的最短可執行摘要

- Hero：不要用新聞／YouTube 人物截圖；做 Taiwan.md 自製抽象雙頻道視覺，或先取得 press portrait 書面授權。
- Inline embeds：`OUZB30lyGcc`、`m5Za_ARPRx0`、`twgMJSxS-H8`；蘿倫段視篇幅加 `BDxeiny76y4`。
- 爭議：口袋奇兵只連 Newtalk 並引述文字；明寫原聲明是 IG 限動，沒有官方影片。
- 小玉：需要前後對照時加 `Tkf8_8_nl68`；不要說 `m5Za_ARPRx0` 是監所內實拍。
- 日期校正：蘿倫 Q&A metadata 是 2022-05-28；新家是 2025-12-13；黑歷史是 2018-05-05。
- 所有影片在 2026-07-15 均仍 public 且可 embed，但上線前應再跑一次 oEmbed／`playable_in_embed` smoke check。
