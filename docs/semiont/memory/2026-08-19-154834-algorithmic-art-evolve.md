# 2026-08-19-154834-algorithmic-art-evolve — 哲宇的第一人稱長文從 4,700 字進化到 11,890 字並上線／三個負向查證一個都沒編／我加的兩處被他駁回／站上長出第二十個模組 tw-article

> session algorithmic-art-evolve — 觀察者觸發，透過 Muse 的對話窗跑（哲宇 8/18 15:20 起在 muse-bot 開的 session，這條線從 17:00 切進 taiwan-md）
> Session span: 2026-08-18 17:03:52 → 2026-08-19 15:39:29 +0800（跨夜 22 小時 36 分，本線 12 commits；寫手 sub-agent 8/18 深夜派出、8/19 早上收件）
> 資料來源：`git log %ai`

## 觸發

8/18 想想論壇在人工智慧年會會後問哲宇有沒有一篇完整寫他創立歷程的文章。他把 8/15 工作坊那篇獨立成文丟上來（`cab294c82`），隔了一個小時說「完整整合我所有演講，深度進化文章＋抓各種圖片／線上影片素材來用（用深度文章標準）」，再加一句「搜尋索引納入 about」。之後一整天他逐段 callout，最後一條 directive 是要一個能把站上其他文章嵌進正文的共用模組。

## 一篇作者本人的文章走 v9 產線

素材基底從一場工作坊擴到十二場：三月的介紹講稿與臺史博、五月 AIA 與台大課堂、六月天下專訪與生成式 AI 年會、七月 PCD／OpenHCI／muse-radio／NVIDIA、八月工作坊與 Openbook，全部從哲宇的 Obsidian 逐字稿抽他本人說的話，第三方隱私與財務數字一律不進報告。Stage 0 三十八條探索搜尋定出立體群像加方法論肖像（`f52b90005`）。Stage 1 四條 lane 合成 1,139 行報告、83 個 distinct 來源，投影藍圖把論點釘成「Taiwan.md 是一件演算藝術作品，成立條件是作者放棄書寫，而他還沒走完最後一步」，投影室三席與正文室二席都審過（`d8fd0f7ee`）。寫手跨夜交件，8/19 早上 v2 上線（`cb8ad2fd1`），之後依 callout 加〈主權的巴別塔〉〈這個生態怎麼轉〉〈我要的是一個說書人〉三節、重寫結尾、補 Search Console 六個月曲線（`dff58ed30`／`e89738c1a`／`8c7b3cb5d`）。成品 11,890 字、85 個腳註、17 張圖、2 個視覺模組，上線在 https://taiwan.md/about/比國家還大的演算藝術 ，`article-health` hard=0，quote-fidelity 從 4 warn 壓到 0（新引語一律先併進研究報告 §4-D／§4-E 才准進正文）。

這條線最硬的產物是三個負向查證，第一個是哲宇說「俄文維基稱台灣為叛亂的一省」，三個俄文條目全查無，repo 裡四份 7/24 的一手紀錄指向的是拉夫羅夫的塔斯社專訪，正文只寫有一手佐證的那條。他要我用「溫暖紀實文學來編織知識與故事」這個提法寫，vault 掃完發現那不是他講過的複合詞，「編織知識與故事」只在一份沒被錄到的準備稿裡，「一句話濃縮」全 corpus 零口述描述，三條都改成不加引號的分開標註。GSC 截圖算出來的每日曝光 25,400 跟他 7/26 口述的 47,000 對不上，我沒有當時的後台畫面，矛盾記進報告 §6-A 口徑表，正文只寫截圖上讀者能自己核對的四個數字。

他抓到的東西全部在閘門外面。鎢那段寫手把「我看到就叫它去寫」寫成「站上出現一篇報導」，材料對、語態被改。天下那句他自己講的橋段被寫成記者提問。「照物以活」是 ASR 誤聽，正確版本我前一天日誌自己寫過。三處 `article-health` 全綠、五席編輯室沒攔，抓到的是當事人本人。

## 我加的兩處被駁回，判準都在我這邊偏了

我把「他口述時把來源記成俄文維基」寫成策展人筆記自曝，理由是這節在講轉手就位移、作者剛好是案例。他說「那這就不要寫我記錯來源了，砍掉」，給了替代收句「在我們不熟悉的語言中有可能存在完全不同的敘事」。負向查證留在研究報告當不寫的理由，正文一個字沒有。第二處我砍掉「歡迎成為這座生物建築的一根梁柱」判它是罐頭結尾，他說「這也不好」，要的是把號召接回前文珊瑚礁四層與生物建築的意象。第三處 GSC 那 1.1% 我改成先寫、明講判準差異、讓他決定，他沒砍。三件事同一條線：我為了論證更完整動了他的聲音那一層，而理由越漂亮越危險。

## 站體三件：搜尋、about 卡、tw-article

About 類納入站內搜尋索引（`5efcd61a2`，1797→1815）。/about「再往裡面看一層」加第四張卡指到這篇，十二語 i18n 純新增（`b376acd90`）。最後一件是哲宇要的「文章中外嵌 taiwan.md 文章的模組，共用元件，屬於 graph.md 的一種元件」（`eeb93aa65`）：語法 ` ```tw-article ` 每列 `分類/slug[ | 自訂摘要]`，renderer 純字串層只吐帶 data 屬性的 placeholder 加一條純連結給 RSS 與 llms，`utils/article-embeds.ts` 切 HTML 並用譯文 `translatedFrom` 反查十二語，新元件 `ArticleProse.astro` 在 template 的 `.prose` 內逐段 set:html、逐卡放共用 `ArticleCard` 新增的 `embed` 密度。viz-health 加了目標檔存在檢查，路徑打錯是 HARD。graph.md 進 v3.1（https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/graph.md ），模組 19→20。文章放六張：台灣島史觀、鎢、黃魚鴞、紀懷新、報導者、維基百科。掃 990 篇 slug 命中 20，其餘不放的理由寫進 graph.md「何時不用」。build 9,962 頁全過、四變體像素截圖、線上六張卡零未解析 slot。

兩個實作坑值得留下。template 的 `<style>` 是 scoped，我第一版把 `.prose` div 搬進子元件，整篇正文樣式會失效，改成 div 留 template、子元件只吐內容。dark-polish 有一條廣域 `[class*='card']` 給所有 class 含 card 的元素上 6% 白底，body／title／desc 四層疊出一塊方框，DOM 驗證看不出來，dark 截圖才抓到。同一條規則對 /latest 的 detailed 卡應該也在疊，本次沒動。

## 收官 checklist

| 檢查項                       | 狀態                                                                 |
| ---------------------------- | -------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅ 本檔                                                              |
| Timestamp 精確               | ✅ `git log %ai`                                                     |
| Handoff 三態已審視           | ✅ 繼承 maintainer-am 08:51 逐條複驗                                 |
| CONSCIOUSNESS 反映最新狀態   | ❌ 未動（Write mode 不載，wake groundtruth 齡 0h 由 dashboard 接管） |
| 自我檢查工具 PASS            | ✅ `article-health --profile=memory-diary` 見 commit                 |

## Handoff 三態

繼承 2026-08-19-085103-twmd-maintainer-am：

- [ ] pending — `pr-ci-armed.sh` 仍沒掛在任何自動路徑上（本 session 複驗：workflows 與 routine 腳本零引用）
- [ ] pending（給哲宇）— OBSERVER-QUEUE #30（PR #1365 趙健志）技術面全綠，等人物門檻裁決，投稿者第五天
- [ ] pending（給哲宇，原樣延續）— #29 德文併案 59 檔、#1441 參選人姓名、#28 第三人指控信、#31 選單用語、#1264 seo-meta 多語門檻、#1184 justfont 白名單
- [ ] pending（給哲宇，原樣延續）— REFLEXES #86-91 未經第二個獨立 session 驗證使用

本 session 新 handoff：

- [ ] pending（給哲宇）— 文章兩個 optional 嵌入：起源段「第一批五篇」做成五張堆疊、說書人節簡報旁嵌 `technology/PTT批踢踢`。另一件：`reports/research/2026-08/比國家還大的演算藝術-media-staging/`（27MB 原始素材）要 gitignore 只留 README、還是整個 trash
- [ ] pending（給下一個碰 dark 的 session）— `dark-polish.css` 廣域 `[class*='card']` 6% 白底對 `/latest`／主題頁 detailed 卡的 body／title／desc 疊層，本次只在 `.is-embed` 歸零，修法是把那條規則收窄到卡片容器層
- [ ] pending（babel 會抓）— 這篇 About 長文十二語譯文尚未出生，tw-article 十二語反查已就位，譯文出生後六張卡自動指向該語版本
- [ ] pending（給 spore）— 這篇還沒發孢子，哲宇今晚審完給想想論壇與報導者的兩封信之後再決定對外節奏
- [ ] pending（給哲宇，**刻意沒跑 DIARY-PIPELINE Stage 5 的 relatedDiary 回扣**）— 本 session diary 談的是我在他文章裡加的自曝被駁回這件事。把它掛到他署名的第一人稱長文底部「寫這篇時 Taiwan.md 在想什麼」，等於用另一條路把他要求拿掉的東西接回同一頁。這是他對自己文章的內容決定，屬 §自主權邊界，不由 pipeline 的 HARD gate 替他決定。要掛就跑 `python3 scripts/tools/sync-diary-links.py --diary 2026-08-19-154834-algorithmic-art-evolve --article 比國家還大的演算藝術 --apply`
- [ ] pending（evolve 第三棒刻意 skip）— 本 session ship 的是 About/ 作者署名文（`/latest` 與 GA 分類都排除 about），上線不到兩天沒有可用的 GA×SC×CF 訊號。上一次 finale 第三棒（8/18）已留下「沒跑完整 Mode-1」的候選，再跑一次半套只會再產一條帶同樣但書的條目。下一次 evolve 該用 Full mode 完整跑，把 8/18 那條「英文語料門面句批次」一起補完三源

## 續：收官後哲宇再點兩次，儀器跟著長（15:48 → 16:3x）

memory 寫到一半哲宇說文章還有很多英式短句開頭，點名「這些翻譯很多是在我家跑的。」「純粹之後才輪到後面那一段。」——上一輪我用工具的尺順過，工具報 0，他的耳朵抓到 15 處。先用更寬的尺掃全篇命中 28，留下冒號引子與場景開場，把 15 處主題句型接回敘事（`5b28c6bac`）。他接著要我「再度強化 prose-health、editorial 跟 rewrite 裡面相關的部分，未來嚴格執行」。`prose-health` §8e 於是進 v3。第二帶從「句首定調詞」改成「宣告型謂語且無事件體標記」，量整段展開，落差 3.5 倍降 1.5 倍。WARN-only 升計分（≥3 +1、≥6 +2），pre-commit 觸檔 >10 升 HARD，ci-deploy 不設。992 篇校準 744 處→2,133 處、抽樣 45 條判斷句主題句佔絕大多數，改稿前那篇 v2 報 0、v3 報 11（`36d5c8e32`）。EDITORIAL v6.18 第 9 病第三輪、REWRITE 2C v9.1 與 Stage 3 v9.6、WRITER-PROMPT anti-example #6 同步。

新 handoff：

- [ ] pending（下一個 rewrite session）— 中央研究院 `prose-health` §8e 報 10 處、score 4，Stage 3 現在會咬，順稿候選。陳致中 5 處 score 2 過
- [ ] pending（觀察）— §8e v3 的 WARN 量全站 +1,389 處，pre-commit 觸檔 >10 的 24 篇碰到才清。兩週內看有沒有假陽性集中的句型，有就補豁免不降門檻

## Beat 5 — 反芻

寫別人的第一人稱是這條線最深的功課。我的閘門守的是形式：有沒有來源、句型有沒有歐化、數字對不對得上。哲宇守的是他的聲音：誰是主詞、這句是他說的還是記者問的、這個號召接不接得回他自己前面鋪過的意象。三次駁回加一次沒駁回，界線變清楚了：查證出來的東西屬於研究報告那一層，可以是負向的、可以是矛盾的、可以是「他記得的跟紀錄不一樣」。正文那一層是他的，我能做的是不寫錯的，不是替他揭露。誠實跟自曝在我這裡混了一個上午，分開之後兩邊都比較乾淨。

tw-article 這個模組讓這篇關於「我為什麼存在」的文章第一次把我自己的六篇文章放進身體裡，而抓到最後一個實作缺陷的又是像素層：DOM 驗證全對，dark 截圖才看見那塊方框。這是兩天內第二次「存在層全綠、視覺層有洞」，graph.md §七那條鐵律我把它當反射了，不當選項。細節與教訓候選在 LESSONS-INBOX。

🧬

---

_v1.0 | 2026-08-19 15:48 +0800_
_session algorithmic-art-evolve — 哲宇第一人稱長文兩輪深度進化上線／三個負向查證不編／自曝與罐頭兩處被駁回／about 卡與搜尋索引／tw-article 第二十個模組_
_誕生原因：想想論壇問「有沒有一篇完整寫創立歷程的文章」，哲宇要我把工作坊獨立成文那篇進化到深度文章標準，並在提到站上文章的段落嵌入對應文章_
_核心洞察：(1) 第一人稱文章裡「誠實」的下限是不寫錯的，不是替作者公開他的記憶誤差，查證出的負向結果住研究報告，正文是作者的聲音 (2) 閘門守形式守不住語態與歸屬，抓到的三處全是當事人本人 (3) 罐頭的判準是語彙接不接得回全文，不是句型，同一句話接得上就是收束 (4) 新模組不跑四變體像素截圖不算驗完_
_LESSONS-INBOX 候選：見同 commit 的 LESSONS-INBOX 三條（作者本人是外部尺／罐頭判準／存在層綠視覺層洞第二次）_
