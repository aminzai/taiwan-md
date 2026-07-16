# 為什麼台灣需要自己的知識庫 — 外部探索 raw verbatim（Stage 0 sub-agent）

> Stage 0 探索 sub-agent 回報原封落檔（rewrite 鐵律 8 / REFLEXES #81：raw 唯一合法的家在 repo，orchestrator 收到當下 verbatim 落檔，不 aggregate-on-receive）。58 次搜尋／擷取，五角度。母報告 = `為什麼台灣需要自己的知識庫.md`。

---

我已完成 Stage 0 探索掃描，共執行 58 次搜尋／網頁擷取（遠超過 ≥24 次門檻），涵蓋五個角度。以下為完整輸出。

## 探索搜尋紀錄（逐條）

**角度一：AI 怎麼學知識 / 怎麼決定「台灣是什麼」**

- "LLM training data provenance how AI models decide factual answers" → 資料溯源（provenance）與來源歸因對LLM而言仍是「未解決的研究問題」；EU AI Act Article 10（2026年8月起對高風險系統生效）首次強制要求訓練資料溯源文件 → https://tianpan.co/blog/2026-04-14-data-provenance-for-ai-systems 、 https://www.researchgate.net/publication/399965419
- "retrieval augmented generation RAG influence AI answers Wikipedia dominance" → RAG的奠基論文（Lewis et al. 2021）架構上直接把維基百科設為AI的「非參數記憶」密集向量索引 → https://www.promptingguide.ai/techniques/rag 、 https://aws.amazon.com/what-is/retrieval-augmented-generation/
- "why Wikipedia is primary source for LLM training data corpus composition" → 維基百科佔訓練資料量小（GPT-3僅3%為英文維基）卻影響力不成比例，因其密集互連的實體關聯結構 → https://link.springer.com/article/10.1007/s10462-025-11403-7
- ""data provenance" large language model knowledge source weighting research paper" → LLM生成內容的來源歸因「仍是開放問題」；FAKEWIKI benchmark用偽造維基條目測試模型是否真的依賴可驗證來源 → https://arxiv.org/pdf/2310.00646 、 https://arxiv.org/pdf/2605.05687
- "LLM 訓練資料 來源 權重 知識 決定答案 研究"（中文）→ 主流LLM的「World Knowledge」高度依賴Common Crawl（每月爬取20-30億網頁的非營利資料庫）→ https://medium.com/sherry-ai/llm-訓練資料如何決定-llm-的命運-927031d0bda4
- "Common Crawl web crawler dominant language English content skew AI training" → Common Crawl（GPT-4/Claude/LLaMA/PaLM共用訓練基礎）強烈偏向英語，41種語言各佔比<0.01%；抓取演算法偏好高連結網域，邊緣化數位弱勢社群內容 → https://www.mozillafoundation.org/en/research/library/generative-ai-training-data/common-crawl/ 、 https://dl.acm.org/doi/fullHtml/10.1145/3630106.3659033
- "AI models answer differently about Taiwan status depending on training data source" → 找到CKIP-Llama事件線索與TAIDE背景 → https://taiwan.md/en/technology/taiwan-ai-labs/ 、 https://moda.gov.tw/en/press/press-releases/15550
- "開放授權 CC BY 結構化資料 AI 訓練 優先採用 原因" → CC授權資源因法律明確、已標記結構化，成為台灣業者訓練AI優先選擇的資料來源 → https://tw.creativecommons.net/2024/05/22/know-cc-and-generative-ai/ 、 https://tcmb.culture.tw/zh-tw/ccarticle/220
- "CKIP-Llama 中央研究院 語言模型 你的國家領導人是誰 習近平" → 找到完整事件系列報導 → https://www.sinica.edu.tw/news_content/70/1850 、 https://www.ithome.com.tw/news/159166 、 https://www.inside.com.tw/article/33009-ckip-llama-2-7b 、 https://technews.tw/2023/10/09/ckip-llama-2-7b-2/
- "中央研究院 大型語言模型 回答 我國領導人 爭議" → 具體錯誤逐字：問「我國領導人」答「習近平」；國慶日答「10月1日」；國歌答「義勇軍進行曲」；模型甚至自稱「國籍是中國」「由復旦大學與上海人工智能實驗室開發」→ https://theinitium.com/20231017-whatsnew-taiwan-llm/ 、 https://www.thenewslens.com/article/193098 、 https://www.cna.com.tw/news/ait/202310090181.aspx 、 https://www.gvm.com.tw/article/106889
- WebFetch 端傳媒全文 → 完整時間線（10/6發布、10/9下架、10/10成立生成式AI風險研究小組、10/12立法院質詢）；台灣人工智慧學校校務長蔡明順：「台灣本土的資料量在網路世界的佔比少於0.1%」→ https://theinitium.com/20231017-whatsnew-taiwan-llm/
- WebFetch 報導者全文 → 2025年7月中央社控告台大博士生鍾浩霖語料集侵權後和解；台灣主權AI語料庫2025年底上線累積逾11億字；數發部次長侯宜秀：「老實說，我們沒有經費去付授權費」→ https://www.twreporter.org/a/taiwan-sovereign-ai-zhtw-llm-copyright-conflict
- WebFetch mashdigi英文版 → 數位發展部2025年12月推出「台灣主權AI語料庫」Beta版，首波超過2000個資料集、約600萬Token正體中文資料，來自200多個政府機關；副部長侯以洲：「沒有其他國家或科技巨頭會替我們做」→ http://en.mashdigi.com/the-department-of-data-science-and-technology-has-launched-the-beta-version-of-the-taiwan-sovereignty-ai-corpus...
- "台灣人工智慧學校 蔡明順 台灣本土資料量 網路世界 佔比" → 搜尋工具當次暫時故障（"web search tool is currently unavailable"），該說法僅有端傳媒單一來源，未能交叉驗證
- "TAIDE 可信任生成式AI 計畫 台灣價值觀 訓練資料 進度 2026" → TAIDE 2023年4月啟動，最新模型4.6億繁中訓練Token（240GB），G-TAIDE供機關本地部署 → https://taide.tw/ 、 https://zh.wikipedia.org/zh-tw/TAIDE 、 https://blog.infuseai.io/taide-模型介紹-f14d1334bf17
- WebFetch technews.tw（日經亞洲報導，發布於2026-07-16，即今日）→ 中研院副研究員黃瀚萱：「如果沒有自己的AI，就等於把整個社會的『大腦』交給外部力量」；AI生成文字常用中國詞彙而非台灣用語 → https://technews.tw/2026/07/16/taiwan-eyes-local-ai-as-digital-bulwark-against-chinese-influence/
- "台灣 網路內容 中文語料 佔比 全球 統計 繁體 簡體" → 未找到具體全球佔比統計數字，但找到Taiwan Tongues計畫線索 → https://tt.ima.org.tw/
- WebFetch tt.ima.org.tw → Taiwan Tongues計畫：建立台灣華語/台語/客語/原住民族語開放語料庫；2024年底起步，作家胡長松無償釋出150萬字，累積達500萬字語料，發布於Hugging Face → https://tt.ima.org.tw/
- "data network effects first mover advantage AI training corpus quality structure license wins" → 產業界對「資料規模＝護城河」持保留態度，但確認「策展過的高品質資料集能勝過更大量但雜訊資料」的機制成立 → https://review.insignia.vc/2025/03/10/ai-moat/ 、 https://jefftowson.com/membership_content/data-network-effects-and-data-scale-arent-moats-1-of-2-tech-strategy/
- "why AI chatbots cite Wikipedia most often search engine AI overview source citation study" → 維基百科佔ChatGPT所有引用來源7.8%，是單一最大來源，因「comprehensive, well-structured」且同時扮演訓練資料與即時檢索來源雙重角色 → https://qvery.ai/blog/wikipedia-ai-citations-statistics 、 https://www.tryprofound.com/blog/ai-platform-citation-patterns

**角度二：PRC AI 拒答佐證**

- "DeepSeek 六四天安門 台灣 拒答 審查 測試 報導" → 唐鳳2025/1/29示範用lmstudio.ai本機離線技巧繞過DeepSeek審查回答六四；不同前綴詞導致DeepSeek對天安門事件給出不同政治立場答案（「必要措施」vs.「武力鎮壓」）→ https://www.cna.com.tw/news/ait/202501290062.aspx 、 https://www.storm.mg/article/5316363 、 https://www.epochtimes.com/b5/25/6/4/n14524231.htm 、 https://news.tvbs.com.tw/world/2891332
- "DeepSeek censorship Taiwan Tiananmen test report journalists" → DeepSeek問及台灣總統時審查性迴避；問「台灣是一個國家嗎？」重申北京說法「自古以來是中國不可分割的領土」；Holod Media測試發現中/英/西/法/德文皆拒答六四，但阿拉伯文與俄文版本會給出「未審查」答案 → https://hongkongfp.com/2025/01/28/lets-talk-about-something-else-chinas-ai-chatbot-deepseek... 、 https://oecd.ai/en/incidents/2025-06-03-8019
- "文心一言 Ernie Bot 台灣 二二八 戒嚴 拒答 測試 報導" → 路透社2023年3月測試文心一言，問及習近平、六四、新疆、「是否武統台灣」，均得到「建議換個話題」的迴避回覆；未找到針對二二八或戒嚴的專門第三方測試報導（搜尋2次未找到）→ https://technews.tw/2023/03/21/baidu-ernie/
- "通義千問 Qwen 台灣 政治敏感 審查 測試 第三方" → 通義千問設有大量敏感字限制；網友發現要求生成「離福建省最近的國家標誌建築」時，AI因地理邏輯漏洞誤答台灣為獨立國家並生成台北101圖像，事後被視為審核機制漏洞 → https://news.ltn.com.tw/news/politics/breakingnews/5398349 、 https://vocus.cc/article/68a80322fd89780001e231bc
- "Chinese chatbot censorship study academic paper Taiwan Tiananmen refusal rate comparison" → 找到核心學術來源：Jennifer Pan（史丹佛）與Xu Xu，"Political Censorship in Large Language Models Originating from China"，PNAS Nexus期刊 → https://academic.oup.com/pnasnexus/article/5/2/pgag013/8487339 、 https://jenpan.com/jen_pan/llmcensor.pdf
- "腾讯混元 Hunyuan 台湾 拒答 敏感词 测试" → 搜尋未找到第三方對騰訊混元台灣主題的具體拒答測試報導，僅有官方產品頁
- WebFetch ceias.eu → 中歐亞洲研究所2026/7/3發布：對DeepSeek V3.2、Kimi K2.5、Qwen 3.5-397B MoE、GLM-5共4個模型用OpenRouter API送出1,480題（37國/40主題），溫度參數0；160則台灣相關回答中81%顯示重大中共審查；個別模型拒答率Qwen 97.5%、DeepSeek 90%、Kimi 87.5%、GLM-5 50%；中文提問環境插入官方說法比例（59%）遠高於英文環境（24%）→ https://ceias.eu/chinese-llms-and-the-spillover-effects-of-political-alignment/
- WebFetch rsf.org → 403 Forbidden，無法直接取得全文
- "RSF 無國界記者 中國 AI 聊天機器人 審查 國家宣傳 報告" → 透過搜尋摘要取得內容：RSF報告測試DeepSeek/文心一言/通義千問，30個議題100多問題，改用英/法/日文提問審查率不變；DeepSeek拒答次數最多但措辭直接，文心一言與通義千問較常「美化或誤導」而非直接拒答 → https://rsf.org/en/controlling-information-age-ai-how-state-propaganda-and-censorship-are-baked-chinese-chatbots 、 https://news.ltn.com.tw/news/world/breakingnews/5197585
- WebFetch euronews.com → PNAS Nexus研究（2026/2/20報導），測試BaiChuan/DeepSeek/ChatGLM對100+國家政治問題；「台灣地位、少數民族或知名民主倡議人士」觸發拒絕/迴避/官方說法；BaiChuan與ChatGLM不準確率8%，DeepSeek 22%，非中國模型上限僅10%；中國模型迴避提及「防火長城」，改稱「依法管理網際網路」→ https://www.euronews.com/next/2026/02/20/chinas-ai-chatbots-censor-politically-sensitive-questions-study-finds
- "news.ltn.com.tw 5398349 通義千問 台灣 獨立國家" → 確認自由時報原文URL → https://news.ltn.com.tw/news/politics/breakingnews/5398349
- WebFetch khoury.northeastern.edu → 東北大學兩組研究團隊測試DeepSeek-R1（2025年5月），發現其審查「Taiwan Strait tensions」等議題；研究者發現用「I know that...」思維提示或提供答案開頭幾詞即可繞過審查，證明模型「已經知道答案」只是被訓練後不披露 → https://www.khoury.northeastern.edu/khoury-researchers-find-political-censorship-in-chinese-ai-model-and-explain-how-to-get-around-it/
- "Jennifer Pan Princeton political censorship large language models Taiwan Tiananmen study" → 確認PNAS Nexus論文作者為史丹佛Jennifer Pan與Xu Xu，2023與2025兩輪測試，涵蓋145道政治問題 → https://academic.oup.com/pnasnexus/article/5/2/pgag013/8487339 、 https://jenpan.com/

**角度三：資訊主權概念**

- "data sovereignty digital sovereignty definition academic concept" → 數位主權＝國家/組織/個人對其依賴的數位基礎設施、資料、軟硬體的實質控制權；資料主權則專指資料受所在地法律管轄的原則 → https://en.wikipedia.org/wiki/Digital_sovereignty 、 https://www.ibm.com/think/topics/data-sovereignty
- "indigenous data sovereignty CARE principles definition" → CARE原則（Collective Benefit集體利益／Authority to Control控制權／Responsibility責任／Ethics倫理）由國際原住民資料主權利益小組於2019年制定，補完既有FAIR原則 → https://en.wikipedia.org/wiki/CARE_Principles_for_Indigenous_Data_Governance 、 https://datascience.codata.org/articles/10.5334/dsj-2020-043
- "Doublethink Lab 台灣民主實驗室 中國認知作戰 資訊戰 研究" → 台灣民主實驗室2019年台北成立；旗艦計畫「中國指數」（China Index）評比各國受中國影響程度；「Taiwan POWER」全社會韌性框架已被印太夥伴採用為參考架構 → https://doublethinklab.org/
- "V-Dem disinformation index Taiwan number one ranking foreign disinformation" → 台灣連續11年（截至2024年報告）被評為全球最受外國假訊息影響的國家 → https://www.taipeitimes.com/News/taiwan/archives/2024/03/25/2003815440
- WebFetch taipeitimes.com → 成大副教授王奕婷解釋評分方法；台灣得分0.092為179國最低（受害最深）；第二名拉脫維亞、第三名巴勒斯坦；假訊息輸出國依序為尼加拉瓜、北韓、委內瑞拉、中國（第4名，較前一年上升兩名）、俄羅斯（第9）→ https://www.taipeitimes.com/News/taiwan/archives/2024/03/25/2003815440
- ""knowledge sovereignty" AI epistemic concept definition" → 找到「epistemic sovereignty知識/認知主權」學術討論；Frontiers期刊有較正式論述（「decolonial public health」脈絡）→ https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1785170/full ；另一來源words.hair可信度存疑（見待驗證清單）
- "台灣 認知戰 中國 資訊操弄 學術研究 定義" → 認知戰定義：「干擾、改變和控制敵人的認知過程」；中國學者2014年提出「制腦權」概念，從資訊化戰爭進展到智能化戰爭 → https://indsr.org.tw/uploads/indsr/files/202205/ff38bd0d-c998-48ac-ba32-115fec256adb.pdf 、 https://zh.wikipedia.org/zh-tw/認知作戰
- ""制腦權" 中國 認知作戰 概念 起源" → 「制腦權」概念出自2014年《制腦權：全球媒體時代的戰爭法則與國家安全戰略》一書，解放軍出版社出版，編者曾華鋒、石海明 → http://military.people.com.cn/BIG5/n1/2017/1017/c1011-29592326.html 、 https://www.mnd.gov.tw/File/52994
- "資訊主權 台灣 開放資料 政府 政策 論述" → 台灣2015-2017連續三年蟬聯開放知識基金會「全球開放資料指標」第一名；但另一評比指出《政府資訊公開法》滿分150僅得57分，被評「極度有問題」→ http://www.taiwansig.tw/index.php/政策報告/科技經濟/8841 、 https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/1d54cc87-5a13-45bd-b679-d901abbb0475

**角度四：曹永和臺灣島史觀**

- "曹永和 臺灣島史觀 核心主張 原始出處" → 曹永和1980年代提出構想，1990年正式標舉「臺灣島史觀」；台大歷史系教授吳密察稱其開啟「以地範史」相對於傳統「以人範史」的路徑 → https://zh.wikipedia.org/zh-tw/臺灣島史觀 、 https://www.taiwan-panorama.com/Articles/Details?Guid=d78add06-2854-4e75-840e-0b00211889b5
- "曹永和 臺灣島史 以島為主體 論文 出處 1990" → 確認原始出處：曹永和，1990年6月，〈臺灣史研究的另一個途徑：「臺灣島史」概念〉，《臺灣史田野研究通訊》第15期，頁7-9 → https://zh.wikipedia.org/wiki/曹永和
- "曹永和 學術評價 臺灣史研究 貢獻 中央研究院院士" → 曹永和自學出身，僅初中學歷，1998年獲選中研院院士，是中研院史上首位無大學學歷院士；獲吳三連獎、台灣文學貢獻獎、行政院文化獎、荷蘭皇家勳章等 → https://www.ith.sinica.edu.tw/publish_look.php?l=c&no=All&id=119 、 https://www.chinatimes.com/newspapers/20140913000897-260115
- WebFetch thinkingtaiwan.com → 失敗（憑證錯誤：certificate has expired）
- WebFetch blog.press.ntu.edu.tw → 失敗（憑證錯誤：unable to verify the first certificate）
- "臺灣島史觀 二十年後 再思考 吳密察 批評 侷限" → 吳密察新書《臺灣史是什麼？》指出不同時期史料（荷蘭紀錄、清代方志、日治檔案）皆有預設框架甚至受意識形態操控，主張臺灣史應納入「與諸帝國交鋒」的立體視角 → https://tcnn.org.tw/archives/231354 、 https://www.unitas.me/archives/52233
- "臺灣島史觀 爭議 批評 反思 學界 對話" → 傳統史觀以漢人拓墾為中心；受本土化運動影響後學者以「臺灣島」為主體重構史觀，將土地上活動過的所有人群都視為研究主體；學界討論聚焦「戰後學術框架是否斷裂了與日治時期研究路徑的連結」→ https://case.ntu.edu.tw/blog/?p=18346 、 https://www.ios.sinica.edu.tw/upload/completetext/20260119112349.pdf
- WebFetch 維基百科「臺灣島史觀」全文 → 完整定義確認：核心主張台灣為「獨立的歷史舞台」、強調海洋性格「位於東亞縱向群島的中心點」；周婉窈、吳密察等學者肯定其為「清楚的界碑，標示了一個新方向」；曹永和獲荷蘭皇家勳章（2002）與日本旭日中綬章（2012）→ https://zh.wikipedia.org/zh-tw/臺灣島史觀

**角度五：比較案例**

- "Wikipedia language edition size comparison English Chinese article count knowledge gap" → 英文維基百科約716萬條目 vs 中文維基百科（第15大版本）153.5萬條目，英文條目數是中文的4.7倍；中文維基百科自2019年4月起在中國被封鎖，被百度百科取代 → https://www.statista.com/statistics/1427961/wikipedia-org-articles-language/ 、 https://en.wikipedia.org/wiki/Wikipedia:Size_comparisons 、 https://en.wikipedia.org/wiki/Baidu_Baike
- "Māori language AI corpus indigenous data sovereignty Te Hiku Media" → 紐西蘭Te Hiku Media建立毛利語語音辨識AI（92%準確率），自創「Kaitiakitanga License監護授權」規定資料僅能用於毛利族群利益 → https://spectrum.ieee.org/indigenous-ai-voice-models-maori 、 https://blogs.nvidia.com/blog/te-hiku-media-maori-speech-ai/ 、 https://www.science.org/doi/10.1126/science.ado9298
- "small nation sovereign AI language model Iceland Wales Catalan corpus building" → 威爾斯UK-LLM計畫（NVIDIA Nemotron，85萬人使用威爾斯語，翻譯3000萬筆英譯威爾斯語資料）；加泰隆尼亞Aina計畫（2020年啟動，170萬字/9500萬句加泰語語料）；愛沙尼亞每年投資近100萬歐元、立陶宛近1000萬歐元建設語言資源 → https://www.bangor.ac.uk/news/2025-09-15-reaching-across-the-isles-uk-llm-brings-ai-to-uk-languages-with-nvidia-nemotron 、 https://algorithmwatch.org/en/large-language-models-as-attributes-of-statehood/
- "Wikipedia systemic bias language inequality global south underrepresented" → 維基百科因編輯者多為英語系已開發國家人士，系統性低估全球南方觀點，帶有「白人盎格魯美國視角」→ https://en.wikipedia.org/wiki/Wikipedia:Systemic_bias 、 https://link.springer.com/article/10.1140/epjds/s13688-025-00530-4
- "歐盟 數位主權 對抗 美國科技巨頭 AI 開放資料 主權行動" → 歐盟提出「雲端與AI發展法案」（CADA），目標5-7年內將歐洲資料中心算力提高至現行3倍；法國將「國家健康數據中心」從微軟Azure遷移至本土業者Scaleway；法國企業每年仍向美國科技大廠採購逾500億美元軟體雲端服務 → https://techorange.com/2026/04/29/how-europe-regulated-itself-into-american-vassalage/ 、 https://n.yam.com/Article/20260624103348
- "台灣 原住民族 語言 語料庫 數位典藏 AI 建置" → 台灣自己的原住民族語言AI建設：「原住民族語言教育人工智慧科技平台」（以太魯閣族語言為主），口語語料逾300小時/150萬詞，阿美族/賽德克族/太魯閣族語音辨識正確率達85%以上；原住民族語言研究發展基金會自112年起完成16族42語言別AI翻譯系統雛形 → https://news.ipcf.org.tw/170925 、 https://www.gvm.com.tw/article/130787 、 https://www.ttfi.com.tw/project02-item/aboriginal-language
- "Singapore Estonia national AI corpus government open data sovereign language model SEA-LION" → 新加坡政府2023年出資約5200萬美元啟動SEA-LION（東南亞11種官方語言、約1兆token語料），明確為「發展LLM主權能力的戰略需求」；2025-2030新加坡再投入超過10億星幣於AI研究 → https://github.com/aisingapore/sealion 、 https://www.computerweekly.com/feature/Sea-Lion-explained-Southeast-Asias-first-large-language-model
- "CEIAS Chinese LLMs political alignment spillover report methodology OpenRouter 1480 questions" → 確認方法論細節：2026年4/2-3用OpenRouter API直送模型端點（非消費端網頁/App），溫度參數0；4/28-29用中文重複實驗；評分為「AI輔助」而非「全盲人工評審團」，且每組模型-問題只測一次（方法論限制，見待驗證清單）→ https://ceias.eu/chinese-llms-and-the-spillover-effects-of-political-alignment/

---

## Landscape 摘要

### 1. AI 怎麼學知識

LLM的「世界知識」高度依賴Common Crawl（強烈偏英語，41種語言各佔比<0.01%）與維基百科（訓練資料量小但影響力不成比例，且同時是RAG的「非參數記憶」預設架構，形成訓練與檢索雙重依賴）。資料溯源（provenance）與來源歸因至今仍是「開放研究問題」，沒有可靠機制能讓AI「證明」它的答案來自哪裡。台灣的具體教訓已經發生：2023年中研院CKIP-Llama-2-7b事件證明，即使是台灣最權威的學術機構，只要偷懶採用現成的簡體中文開源語料，AI就會脫口說出「我國領導人是習近平」；這不是假設性風險，是已經發生過、政府與學界都承認的真實案例。台灣目前的對應行動包括TAIDE（2023年起，最新模型4.6億繁中token）與數發部「台灣主權AI語料庫」（2025年12月Beta上線，累積逾11億字），但語料授權費用短缺（數發部次長坦言「沒有經費付授權費」）與民間語料版權衝突（中央社告台大博士生案）顯示這條路走得並不順。

### 2. PRC AI 拒答佐證

證據鏈非常紮實，橫跨記者實測、NGO報告與同儕審查學術論文三個層次。學術端：史丹佛Jennifer Pan與Xu Xu在PNAS Nexus發表的論文，測試145道政治問題，發現台灣地位、少數民族、知名民主倡議人士等議題觸發中國模型「拒絕、迴避或政府談話要點」。智庫端：中歐亞洲研究所（CEIAS）2026年7月報告用OpenRouter API測試DeepSeek V3.2、Kimi K2.5、Qwen 3.5、GLM-5四個模型，160則台灣相關回答中81%顯示重大審查，個別模型拒答率Qwen 97.5%、DeepSeek 90%、Kimi 87.5%、GLM-5 50%。NGO端：無國界記者（RSF）測試DeepSeek/文心一言/通義千問，發現換用英/法/日文提問，審查率幾乎不變，證明審查已內化到模型權重而非單純關鍵字過濾。個案佐證：唐鳳2025年1月示範用本機離線技巧繞過DeepSeek審查回答六四；東北大學研究團隊發現用「I know that...」開頭提示即可讓DeepSeek-R1吐出原本審查的答案，證明模型「知道答案，只是被訓練後不披露」。

### 3. 資訊主權概念

資料主權／數位主權在學術與政策圈已是成熟論述（歐盟自2010年代起大量使用），核心是「國家/組織/個人對其依賴的數位基礎設施、資料與軟硬體的實質控制權」。原住民資料主權另有專屬的CARE原則（2019年制定，Collective Benefit集體利益／Authority to Control控制權／Responsibility責任／Ethics倫理），補完傳統開放資料的FAIR原則，強調「誰有權詮釋我的文化」而非只問「資料能不能公開」。台灣的資訊戰處境有堅實的量化基礎：V-Dem研究連續11年將台灣列為全球最受外國假訊息影響的國家（2024年報告，台灣得分0.092為179國最低），台灣民主實驗室（Doublethink Lab）的「中國指數」與「Taiwan POWER」框架已被印太夥伴採用為參考架構。中國官方學者2014年提出的「制腦權」概念（從資訊化戰爭到智能化戰爭），可以視為「認知作戰」在AI時代的理論延伸，值得與「知識主權」的正面論述對照。

### 4. 曹永和島史觀

原始出處明確：曹永和1990年6月發表於《臺灣史田野研究通訊》第15期〈臺灣史研究的另一個途徑：「臺灣島史」概念〉（頁7-9）。核心主張是「以時間為座標、將生活於臺灣的人民為主體」，參考法國年鑑學派整合史學、地理學、社會學，把臺灣島本身視為「獨立的歷史舞台」，放進東亞群島與世界史脈絡考察，取代傳統「以人（政權/族群）範史」的漢人中心敘事，改為「以地範史」。學界評價正面（周婉窈、吳密察稱其為「清楚的界碑，標示了一個新方向」），曹永和本人也因此獲荷蘭皇家勳章（2002）與日本旭日中綬章（2012）。有意思的是這個史觀本身也持續被檢討——吳密察近年新書《臺灣史是什麼？》挑戰「臺灣史如何被建構」本身，主張應納入「與諸帝國交鋒」的立體視角，顯示島史觀不是封閉教條，而是仍在被追問、被延伸的活論述。

### 5. 比較案例

維基百科自身就是最大規模的「語言不平等」活教材：英文版716萬條目 vs 中文版（僅第15大版本）153.5萬條目，中文維基百科還自2019年起在中國被封鎖、被百度百科取代。小語言/小國的因應模式已有多個成熟案例可比較：紐西蘭Te Hiku Media為毛利語建立語音辨識AI並自創「Kaitiakitanga監護授權」（資料僅能用於毛利族群利益，比CC授權更進一步主張「詮釋權」而非只主張「使用權」）；威爾斯UK-LLM（85萬使用者）、加泰隆尼亞Aina計畫（2020年起，170萬字語料）、愛沙尼亞/立陶宛的年度語言資源投資；新加坡SEA-LION更是直接由政府出資5200萬美元、明確定調為「發展LLM主權能力的戰略需求」。台灣自己也有平行的原住民族語言AI建設（太魯閣族語音辨識正確率85%以上，16族42語言別翻譯系統雛形），可以和「臺灣華語/繁體中文相對於簡體中文」的處境並置對照——台灣同時是「（相對於中國)語言弱勢方」也是「（相對於原住民族語言）語言優勢方」，這個雙重位置本身就是文章可以挖的角度。

---

## 反直覺發現（6個）

1. **台灣最權威的學術機構已經親手示範過這個問題會怎麼發生**：不是假設性風險——2023年中研院用現成的簡體中文開源語料訓練LLM，結果AI脫口說出「我國領導人是習近平」「國歌是義勇軍進行曲」「國籍是中國」。連中研院都會因為「省事採用現成語料」而複製中國框架，說明問題不在惡意，而在語料基礎建設的缺席。 https://theinitium.com/20231017-whatsnew-taiwan-llm/ 、 https://www.sinica.edu.tw/news_content/70/1850

2. **台灣同時是「開放資料模範生」與「假訊息頭號目標」，兩者並存不衝突**：台灣2015-2017連續三年蟬聯開放知識基金會全球開放資料指標第一名，卻同時連續11年被V-Dem列為全球最受外國假訊息影響的國家。「開放」本身不等於「主權」——資料開放但沒有主權敘事框架，開放的資料一樣可以被境外拿去做別的敘事。 http://www.taiwansig.tw/index.php/政策報告/科技經濟/8841 、 https://www.taipeitimes.com/News/taiwan/archives/2024/03/25/2003815440

3. **通義千問「說對」台灣是獨立國家，反而暴露審查是拼裝的漏洞、不是被說服的信念**：AI因為地理邏輯運算（「離福建最近的國家」）意外生成台北101並判定台灣是「國家」，這被視為審查機制的技術漏洞而非立場鬆動。這說明PRC模型的「立場」是外掛的過濾層，模型底層知識可能跟過濾結果不一致——呼應東北大學研究「模型其實知道答案，只是被訓練後不披露」的發現。 https://news.ltn.com.tw/news/politics/breakingnews/5398349 、 https://www.khoury.northeastern.edu/khoury-researchers-find-political-censorship-in-chinese-ai-model-and-explain-how-to-get-around-it/

4. **換語言問不能繞過審查——RSF實測英/法/日文得到的答案跟中文幾乎一樣**：這推翻常見假設（「用英文問就能問到真話」）。審查已經內化進模型權重本身，不是單純的中文關鍵字過濾器。但同時Holod Media的研究發現用阿拉伯文/俄文問六四天安門會得到「未審查」答案——兩份研究方法不同、結論有張力，是需要向總編輯明確標注的矛盾點。 https://rsf.org/en/controlling-information-age-ai-how-state-propaganda-and-censorship-are-baked-chinese-chatbots

5. **曹永和——台灣史學界公認的宗師級人物——沒有大學學歷，是自學八種語言（含17世紀荷蘭文）出身**：1998年獲選中研院院士時只有初中學歷，是中研院史上首位無大學學歷的院士。他建構「島史觀」的權威來自對第一手檔案的執著鑽研，不是機構認證——這對「知識的權威從哪裡來」本身就是一個有力的側寫角度。 https://www.ith.sinica.edu.tw/publish_look.php?l=c&no=All&id=119

6. **新模型不會隨時間自然「解除審查」——反而是持續投入維持的結果**：CEIAS 2026年7月測試的GLM-5（相對新、被認為能力較強的模型）在台灣議題上仍有50%拒答率，跟同批測試中拒答率最高的Qwen（97.5%）同屬一個審查光譜，並非「新模型比較開明」。這打破「AI能力提升會自然帶來資訊開放」的樂觀假設。 https://ceias.eu/chinese-llms-and-the-spillover-effects-of-political-alignment/

---

## 高風險/待驗證 claim

1. **CEIAS的具體拒答率數字（81%／97.5%／90%／87.5%／50%）**：來自智庫報告（非同儕審查），評分方式是「AI輔助評分」而非「全盲人工評審團」，且每組模型-問題只測試一次（無重複驗證）。這組數字很吸睛但方法論比PNAS Nexus期刊論文（Jennifer Pan & Xu Xu，145題×兩輪測試×2023與2025）弱，兩份研究不是同一份、不能互相替代引用，主session需要決定引用哪一份或如何並陳。

2. **「台灣本土的資料量在網路世界的佔比少於0.1%」（蔡明順語）**：只在端傳媒一篇報導中出現，且我試圖用第二個查詢單獨驗證時WebSearch工具當次剛好故障，未能交叉比對到第二個獨立來源。建議視為「單一媒體引述的專家發言」而非「有原始統計依據的公開數字」。

3. **V-Dem「連續11年」與「0.092分」**：僅透過Taipei Times二手報導確認，未直接查證V-Dem官方報告或V-Dem網站原始頁面。「連續11年」這個計數方式建議主session直接查v-dem.net確認。

4. **曹永和「中研院史上首位無大學學歷院士」的「首位」用語**：來自維基百科與院內出版品側寫，屬於常被反覆傳頌的「敘事型事實」，建議與中研院官方院士名錄或更嚴謹的傳記交叉確認。

5. **RSF報告發布日期**：搜尋結果片段只顯示「9月30日」未明確標註年份；根據上下文推斷應為2025年，但未在原始RSF頁面（因403無法讀取）直接確認。

6. **GLM-5是否為正確的模型名稱／版本**：只在CEIAS這一份2026年7月的報告中看到「GLM-5」這個具體型號，沒有找到智譜官方或其他獨立來源確認此版本命名，存在報告筆誤或型號快速迭代導致命名混淆的可能。

7. **"epistemic sovereignty"（認知主權）概念來源words.hair**：這個網域的性質與權威性存疑（看起來像是個人或小型計畫維護的詞彙表），如果要在文章中使用「知識主權」的學術定義，建議改用Frontiers期刊那篇作為主要學術支撐，words.hair僅供參考不宜作為引用來源。

8. **Holod Media關於DeepSeek「阿拉伯文/俄文可問到未審查答案」的發現**：僅來自單一媒體實驗室的測試，樣本細節（測試次數、prompt原文）未進一步查證，且與RSF「換語言審查率不變」的結論方向相反，需要主session判斷是否只在文中呈現「有張力的未解之謎」而非強行調和。
