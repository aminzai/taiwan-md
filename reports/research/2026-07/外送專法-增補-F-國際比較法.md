# 外送專法 — 增補研究 F：國際比較法對照組

執行摘要：搜尋／查證 37 次（WebSearch 12＋WebFetch 21＋Bash curl 2＋PDF read 2），最大 falsify：（1）歐盟指令走的是「雇用推定＋舉證責任倒置」，跟台灣「不定性、直接給付權益」是**方向相反**的兩種哲學，且轉換期限到 2026-12-02、目前全歐盟無一國完成轉換，不能拿「歐盟模式」當作已驗證的對照組；（2）日本《フリーランス法》官方逐字條文證實它**完全不處理雇用身份認定**，是純交易公平化立法，跟台灣「以身份為對象、逐項給付權益」的專法邏輯本質不同，此前報告把兩者並列可能誤導；（3）「第三類身份」在國際學術界正反意見都極端明確——美國 EPI（2026）稱其為「合法化剝削的財富移轉」，英國政府本身正在檢討廢除已運作 20+ 年的「worker」中間類別，但也有學者（Peetz 2023）主張這是比全面僱傭化更政治永續的路線。

---

## §1 搜尋軌跡（逐條，不可省、不可事後重組）

1. 「Directive (EU) 2024/2831 platform work eur-lex」→ 找到官方 CELEX 頁面與 Wikipedia 條目入口 → https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024L2831-20241111 [英/一手]
2. 「EU Platform Work Directive presumption of employment algorithmic management transposition deadline」→ 確認轉換期限 2026-12-02、目前轉換進度 → https://employsome.com/blog/platform-work-directive/ [英/二手]
3. WebFetch eur-lex HTML 直連 → 空白回應（WAF/JS challenge，非拒絕存取），改用 Bash curl 驗證
4. WebFetch https://www.chusho.meti.go.jp/keiei/torihiki/law_freelance.html → HTTP 403（bot 防護）
5. Bash curl -sIL eur-lex → 確認為 AWS WAF `x-amzn-waf-action: challenge`，非內容問題，改走 r.jina.ai 讀取代理
6. WebFetch https://r.jina.ai/https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024L2831-20241111 → **成功取得 Article 5、Article 10(5)、Article 11(1)、Article 29(1) 逐字英文條文** [英/一手]
7. 「フリーランス法 特定受託事業者に係る取引の適正化等に関する法律 厚生労働省 施行 2024年11月」→ 確認正式名稱與施行日 → https://www.chusho.meti.go.jp/keiei/torihiki/law_freelance.html [日/一手線索]
8. WebFetch https://r.jina.ai/https://en.wikipedia.org/wiki/Platform_Work_Directive_2024 → 取得 Chapter III（Article 6-10）演算法管理章節架構 [英/二手索引]
9. 「EU Platform Work Directive criticism debate presumption employment vs Taiwan third category worker status」→ 找到歐洲議會新聞稿與批評文獻 → https://www.europarl.europa.eu/news/en/press-room/20240318IPR19420/platform-work-first-green-light-to-new-eu-rules-on-employment-status [英/一手（歐洲議會官方）]
10. WebFetch https://www.etui.org/publications/eu-platform-work-directive → HTTP 403（付費牆/bot 防護）
11. 「ILO World Employment Social Outlook digital labour platforms classification typology employment status third category」→ 找到 ICSE-18 分類與中國案例文章 → https://www.ilo.org/resource/article/beyond-employees-and-contractors-mapping-china%E2%80%99s-platform-based-gig-workers [英/一手（ILO 官方）]
12. WebFetch https://www.ilo.org/media/407896/download（G20 2019 政策報告 PDF）→ **成功取得逐頁原文**（Read PDF pages 1-10）[英/一手（ILO 官方，惟為 2019 年 web-based crowdwork 報告，非 location-based 外送對照）]
13. WebFetch https://www.ilo.org/resource/article/beyond-employees-and-contractors-mapping-china%E2%80%99s-platform-based-gig-workers → 取得 Xueyu Wang 研究摘要 [英/一手（ILO 官方轉引學者研究）]
14. 「Italy etero-organizzato riders Jobs Act 2019 article 2 co.co.co third category gig economy」→ 確認義大利路線非創設新類別而是「規則延伸」 → https://www.lavorodirittieuropa.it/dottrina/lavori-atipici/1793-il-lavoro-eterorganizzato-e-la-disciplina-per-i-riders [義/學術二手]
15. 「Spain TRADE trabajador autónomo económicamente dependiente gig platform workers third category」→ 確認 TRADE 定義（≥75% 收入依賴單一客戶） → https://cllpj.law.illinois.edu/content/dispatches/2021/Dispatch-No.-36.pdf [英/學術（伊利諾大學勞動法期刊 Dispatch）]
16. 「Canada dependent contractor gig economy Ontario intermediate employment category academic」→ 確認 Foodora 案判例 → https://onlabor.org/the-classification-of-gig-workers-in-canadian-work-law/ [英/學術二手]
17. 「UK "worker" status Uber Aslam gig economy third category academic evaluation pros cons」→ 確認 UK 政府擬廢除 worker 中間類別 → https://connaughtlaw.com/gig-economy-worker-rights-uk-guide/ [英/二手（法律事務所）]
18. WebFetch https://connaughtlaw.com/gig-economy-worker-rights-uk-guide/ → **逐字確認**「政府擬諮詢簡化雇用身份、朝二分制方向」原句 [英/二手]
19. WebFetch https://www.bristol.ac.uk/media-library/sites/business-school/documents/Gig%20Rights%20&%20Gig%20Wrongs%20Report.pdf → PDF 內容無法解析為可讀文字，未能取得逐字
20. 「노무제공자 고용추정제 2026년 5월 시행 서울고등법원 2026년 7월 배달기사 근로자 판결」→ 找到法律事務所 newsletter 與多家韓媒報導 → https://www.bkl.co.kr/law/insight/newsletter/6647 [韓/權威二手（律師事務所）]
21. WebFetch https://www.bkl.co.kr/law/insight/newsletter/6647 → 確認為二手解讀非判決原文，未取得案號
22. 「노무제공자 근로자 추정 특고 플랫폼종사자 2026년 5월 1일 시행 고용노동부 보도자료」→ 找到勞動部官方業務報告連結 → https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18725 [韓/一手（政府官方）]
23. WebFetch https://www.dailypop.kr/news/articleView.html?idxno=95614 → **取得業界反對「노동자 추정제」逐字引語** [韓/權威二手（產業媒體）]
24. WebFetch https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18725 → **取得勞動部官方逐字定義句**，惟未見民事/刑事適用範圍區分的官方原文 [韓/一手]
25. WebFetch https://r.jina.ai/https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/bunya/freelance_00006.html → 確認頁面提及施行一年統計但未取得具體數字 [日/一手]
26. 「フリーランス法 就業環境整備 育児介護 ハラスメント 中途解除予告 30日前 逐条解説 厚生労働省」→ 定位官方 PDF 小冊子 → https://www.jftc.go.jp/file/flpamph.pdf [日/一手（公正取引委員會＋厚生勞働省＋中小企業廳聯合官方文件）]
27. WebFetch https://r.jina.ai/https://www.chusho.meti.go.jp/keiei/torihiki/law_freelance.html → 確認法律番号「令和5年法律第25号」、施行日「令和6年11月1日」 [日/一手]
28. WebFetch https://www.jftc.go.jp/file/flpamph.pdf（2MB PDF）→ **成功 Read PDF pages 1-8**，取得法目的（第1條）、對象定義（第2條）、與勞基法關係的官方明文說明 [日/一手]
29. Read 同一 PDF pages 20-25 → **取得第13條（育兒介護配慮）、第14條（騷擾防治）、第16條（中途解除30日前預告）逐字條文說明與案例** [日/一手]
30. 「third category gig economy workers loophole platforms avoid employment obligations academic critique intermediate status」→ 找到 EPI 與 Cambridge 期刊兩篇對立觀點 → https://www.epi.org/publication/state-misclassification-of-workers/ [英/學術（智庫）]
31. 「ILO World Employment Social Outlook 2021 digital labour platforms report Taiwan intermediate status classification」→ **查無 ILO WESO 2021 報告中提及台灣**（negative finding）
32. WebFetch https://www.epi.org/publication/state-misclassification-of-workers/ → HTTP 403
33. WebFetch https://www.cambridge.org/core/journals/the-economic-and-labour-relations-review/article/can-and-how-should-the-gig-worker-loophole-be-closed/C267DB9F253A374379D186F1A9573484 → **取得 David Peetz（2023, The Economic and Labour Relations Review）逐字論點**，主張契約規範路線優於員工再分類 [英/學術]
34. WebFetch https://r.jina.ai/https://www.epi.org/publication/state-misclassification-of-workers/ → **取得 EPI（2026-07-14）逐字批評「第三類立法讓平台合法化剝削」原句** [英/智庫（勞方立場，需標注立場）]
35. 「서울고등법원 2026 라이더유니온 근로자성 판결 사건번호 2025나」→ **取得案號「서울고등법원 2026. 7. 3. 선고 2024나2037832 판결」** → https://www.pressian.com/pages/articles/2026070717595884718 [韓/權威二手]
36. WebFetch https://www.khan.co.kr/article/202607071745001 → **取得法院判決理由逐字韓文原文** [韓/權威二手（京鄉新聞）]
37. （交叉核對）Bash curl -s eur-lex（無 header）→ HTTP 202 空內容，確認第 3 條 WAF 判斷正確，非內容不存在

---

## §2 Findings（依 6 項任務分節）

### 2-1 EU 平台工作指令 Directive (EU) 2024/2831（最高優先）

【來源】https://r.jina.ai/https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024L2831-20241111 — EUR-Lex 官方統整條文（透過 Jina Reader 代理讀取，因 eur-lex.europa.eu 對直接 fetch 有 AWS WAF challenge）
【來源】https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024L2831 — 同一指令官方 PDF（供 Ctrl-F 核對用連結，本次工具未能直接解析內容，逐字取自上一條 Jina 代理）
【逐字】Article 5(1)：「The contractual relationship between a digital labour platform and a person performing platform work through that platform shall be legally presumed to be an employment relationship where facts indicating direction and control, in accordance with national law, collective agreements or practice in force in the Member States and with consideration to the case-law of the Court of Justice, are found.」
【逐字】Article 5(1) 舉證責任倒置：「Where the digital labour platform seeks to rebut the legal presumption, it shall be for the digital labour platform to prove that the contractual relationship in question is not an employment relationship.」
【逐字】Article 29(1) 轉換期限：「Member States shall bring into force the laws, regulations and administrative provisions necessary to comply with this Directive by 2 December 2026.」
【逐字】Article 10(5) 人工決策要求：「Any decision to restrict, suspend or terminate the contractual relationship or the account of a person performing platform work or any other decision of equivalent detriment shall be taken by a human being.」
【逐字】Article 11(1) 人工複審權：「Member States shall ensure that persons performing platform work have the right to obtain an oral or written explanation from the digital labour platform for any decision taken or supported by an automated decision-making system without undue delay.」
【信度】一手（歐盟官方法律文本，惟透過第三方讀取代理取得，建議正文引用前另行以 Ctrl-F 在 eur-lex.europa.eu 官方頁面核對，因原始頁面本次工具連線受 WAF 阻擋無法直接驗證）
【falsify 註記】**指令採「雇用推定 + 舉證責任倒置」路線，與台灣「不定性、直接給付特定權益」是方向相反的兩種立法哲學——歐盟先假定「是僱傭」，平台要自己舉證推翻；台灣則刻意不做身份判定，直接列舉外送員該拿到的具體保障項目。這個對比成立，且是本次研究最關鍵的確認**。惟指令 2026-12-02 才是轉換期限，據 2026-07-01 時點的產業報導，全歐盟 27 國尚無一國完成國內法轉換，僅義大利、西班牙、比利時、葡萄牙 4 國「本來就有」平台工作僱傭推定的既存國內法（非因本指令新訂），不能用「歐盟已經這樣做」的現在式描述，須標注「規則已生效但尚未落地」。

【來源】https://www.europarl.europa.eu/news/en/press-room/20240318IPR19420/platform-work-first-green-light-to-new-eu-rules-on-employment-status — 歐洲議會官方新聞稿
【逐字】（新聞稿確認）指令目標是「correct the imbalance of power between the platform and the person performing platform work」
【信度】一手（歐洲議會官方）
【falsify 註記】無

【來源】https://employsome.com/blog/platform-work-directive/ — 產業合規服務商部落格，二手轉引
【逐字】（轉引整理）「As of 1 July 2026 no EU member state has fully transposed the Platform Work Directive; Italy is the furthest ahead, with an in-force rider presumption from May 2026; 4 states in total (Italy, Spain, Belgium and Portugal) already have a platform-work presumption of employment in national law; 5 are drafting; and 18 have not started.」
【信度】權威二手（惟為商業合規顧問網站，非學術或官方統計，具體轉換進度數字建議另行以歐盟執委會官方轉換追蹤頁核對）
【falsify 註記】**「歐盟已用雇用推定解決問題」是簡化敘事——27 國中 18 國「尚未開始」轉換，這個指令目前更接近「規範方向已定、執行進度極慢」，跟台灣專法 7/21 已零時施行、立即生效的執行力道完全不在同一個時間刻度上，行文比較時必須標注此落差。**

【來源】https://www.lexisnexis.com/en-gb/legal/guidance/the-eu-platform-work-directive — LexisNexis 英國法律指引（二手，經 WebSearch 摘要，未逐字 WebFetch 核對）
【信度】【存疑：僅搜尋摘要層級，未經 WebFetch 逐字核對，正文引用前建議另行查證】
【falsify 註記】無

---

### 2-2 日本《フリーランス法》逐字補強

【來源】https://www.jftc.go.jp/file/flpamph.pdf — 公正取引委員會・厚生労働省・中小企業庁聯合官方小冊子（2MB PDF，成功以 Read 工具解析頁面 1-8、20-25，非二手轉引）
【逐字】封面：「特定受託事業者に係る取引の適正化等に関する法律（フリーランス・事業者間取引適正化等法）パンフレット」「令和6年11月1日施行」
【逐字】第1條目的（本法概要頁）：「取引の適正化・就業環境の整備」
【逐字】對象定義（第2條）：フリーランス＝「特定受託事業者」（個人であって従業員を使用しないもの、または法人であって一の代表者以外に他の役員がなく、かつ従業員を使用しないもの）
【逐字】**本法與勞基法關係的官方明文（\ここがPoint\ 標注）**：「形式的には業務委託契約を締結している者であっても、実質的に労働基準法上の労働者と判断される場合には、労働基準関係法令が適用され、本法は適用されません。」
【逐字】義務清單：①取引条件の明示義務（第3條）②期日における報酬支払義務（第4條）③発注事業者の禁止行為（第5條）④募集情報の的確表示義務（第12條）⑤育児介護等と業務の両立に対する配慮義務（第13條）⑥ハラスメント対策に係る体制整備義務（第14條）⑦中途解除等の事前予告・理由開示義務（第16條）
【逐字】第13條育兒照護配慮：「発注事業者は、フリーランスからの申出に応じて、6か月以上の期間で行う業務委託について、フリーランスが妊娠、出産若しくは育児又は介護（育児介護等）と業務を両立できるよう、必要な配慮をしなければなりません。」（6個月未滿的委託則為努力義務，非強制）
【逐字】第14條騷擾防治：發注事業者「ハラスメントによりフリーランスの就業環境を害することのないよう相談対応のための体制整備その他の必要な措置を講じなければなりません」，並列出パワハラ／セクハラ／マタハラ三類型逐一定義與例示
【逐字】第16條中途解除30日前預告：「発注事業者は、①6か月以上の期間で行う業務委託について、②契約の解除または不更新をしようとする場合、③例外事由に該当する場合を除いて、解除日または契約満了日から30日前までにその旨を予告しなければなりません。」
【信度】一手（日本公正取引委員會・厚生勞働省・中小企業廳聯合官方文件，非搜尋摘要，逐字取自官方 PDF）
【falsify 註記】**這是本次研究對前次報告【存疑】標記最關鍵的修正**：前次報告只有搜尋摘要層級資訊；本次逐字核對官方 PDF 後確認——**日本フリーランス法完全不處理「雇用身份認定」問題，是純粹的「B2B交易公平化」立法，且官方文件明文寫死「若實質上是勞基法勞工，本法就不適用、改用勞動關係法令」**。這代表日本走的既不是「雇用推定」也不是「創設第三類身份」，而是**第三種立法哲學：不碰身份認定，只規範交易行為本身（報酬支付期限、契約明示、解約預告、育兒照護配慮、騷擾防治）**。跟台灣「明確以『外送員』這個職業身份為對象、逐項給付具體保障」的路線也不同——台灣專法鎖定特定職業群體立法，日本フリーランス法適用對象是「所有個人接案自營工作者」（不限外送、不限特定產業），涵蓋範圍更廣但保障內容更薄（沒有最低報酬、沒有保險強制、沒有演算法透明專章）。**任務假設中「日本模式也走不定性但給權益路線，所以台灣不是孤例」需要修正**：日本模式的「不定性」跟台灣的「不定性」性質不同——日本是「不碰、留給既有二元認定」，台灣是「創設新的、專屬外送員的權益清單」。

【來源】https://r.jina.ai/https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/bunya/freelance_00006.html — 厚生労働省官方頁面（施行一年紀念頁）
【逐字】頁面確認提及「都道府県労働局における令和６年度の法施行状況をみると」，惟本次工具讀取未取得具體相談件數／勧告件數數字
【信度】一手，但**具體統計數字未能取得，標【存疑：需另行查證厚勞省令和6年度施行狀況統計原文】**
【falsify 註記】無

---

### 2-3 南韓最新狀態

【來源】https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18725 — 韓國雇傭勞動部（고용노동부）2026年官方業務報告新聞稿
【逐字】「'노동자 추정제'를 도입하여 사용자가 노동자가 아님을 입증하지 못하면 노동자로 추정하고 노동법으로 보호하여 개인이 노동자임을 증명하지 못해 보호에서 배제되는 문제를 해소한다('26.상~)。」（中譯：導入「勞動者推定制」，雇主若無法證明對方不是勞動者，即推定為勞動者並受勞動法保護，藉此解決個人因無法自證勞動者身份而被排除於保障之外的問題，自 2026 年上半年起）
【信度】一手（韓國政府官方業務報告）
【falsify 註記】此為官方逐字定義，確認制度機制與前次報告（2026-05-01 上路、舉證責任轉移雇主）一致；惟本頁**未見「僅限民事爭議、不適用刑事案件」的官方原文限定**，此限定僅見於前次報告引用的 Korea Times 二手轉引，本次未能在官方新聞稿逐字核對，**維持【存疑】標記，建議標注來源為媒體轉引非官方原文**。

【來源】https://www.dailypop.kr/news/articleView.html?idxno=95614 — 데일리팝（韓國產業媒體），批評視角
【逐字】業界反對意見：「프리랜서 개념도 모르나…혁신 산업 위축 불가피」（不懂自由工作者概念嗎……創新產業萎縮不可避免）
【逐字】對政府政策的批評：「정부가 긱워커의 본질을 이해하지 못한 채 60년 전 산업시대 잣대로 21세기 플랫폼 경제를 재단하려 한다」（政府不理解零工經濟的本質，卻用 60 年前工業時代的尺度裁剪 21 世紀平台經濟）
【逐字】「노동계가 주장하는 '실질적 종속성' 해소를 위해 근로기준법이라는 낡은 틀을 억지로 씌우는 것은 오히려 일자리 축소를 초래할 수 있다」（為解決勞方主張的「實質從屬性」，硬套上勞基法這個陳舊框架，反而可能導致工作機會縮減）
【逐字】870萬零工工作者數字來源：「2026년 1월 현재 약 870만명으로 추산되는 프리랜서·플랫폼·특수고용 종사자들」，惟該文**未明確標注此數字的原始統計出處**
【信度】權威二手（韓國產業媒體，明確站在反對立法的業界／自由市場立場，需標注立場後引用）
【falsify 註記】**這是南韓對照組必要的反方證據**：南韓「勞動者推定制」雖方向上比台灣更激進（推定雇傭），但同樣面臨本土產業界「用工業時代框架硬套 21 世紀零工經濟」的批評——這跟台灣本土反對專法者（律師林智群，見主報告 §2 子題 7）的論述邏輯高度相似，說明「創設保障性立法引發業界『扼殺創新／彈性』反彈」是跨國通例，不是台灣或南韓獨有。

【來源】https://www.pressian.com/pages/articles/2026070717595884718 — 프레시안（Pressian，韓國調查媒體）
【逐字】確認案號：「서울고등법원 2026. 7. 3. 선고 2024나2037832 판결」
【信度】權威二手
【falsify 註記】無

【來源】https://www.khan.co.kr/article/202607071745001 — 경향신문（京鄉新聞，韓國主流媒體）
【逐字】法院判決理由：「배달 라이더가 독립적인 사업자로 고객을 직접 확보하는 것이 아니라 플랫폼사의 앱을 통해서만 주문과 배달을 수행할 수 있는 구조인 점, 보수의 산정 기준과 지급 방식 모두 회사가 사전에 정한 기준에 따라 결정된다는 점, 배차 등에서 라이더가 온전한 결정권이 있다고 보기 어려운 점 등이 노동자성 인정의 근거가 됐다.」（外送員無法獨立招攬客戶、只能透過平台App接單配送的結構、報酬計算基準與給付方式皆由公司事先訂定、派單上騎士難認有完整決定權，是法院認定勞動者性的依據）
【逐字】「배달 라이더가 플랫폼 애플리케이션(앱)에 접속해 일하는 동안 회사의 지휘·명령을 받아 종속적인 관계에서 노무를 제공했다면 근로기준법상 근로자로 봐야 한다」
【信度】權威二手（京鄉新聞為韓國主流全國性報紙）
【falsify 註記】此判決是**首爾高等法院第38-1民事部**（非本次任務假設籠統提及的「首爾高等法院」，具體到部別），適用法理與台灣勞動部 2019 年對外送員做「假承攬真雇傭」認定的判斷邏輯（從屬性、指揮監督）高度相似——說明台韓兩地在「事後司法／行政個案認定」層面早已走過類似路徑，差別在於台灣選擇不繼續走個案認定累積路線，改為專法直接立法給權益；南韓則是司法個案認定＋制度性推定雙軌並行。

---

### 2-4 制度分類框架

【來源】https://www.ilo.org/resource/article/beyond-employees-and-contractors-mapping-china%E2%80%99s-platform-based-gig-workers — ILO 官方文章，轉引學者 Xueyu Wang 研究
【逐字】（轉引整理）Wang 指出「traditional binary legal paradigms may not fully capture the diverse realities of these new digital arrangements」，並發現「Social insurance coverage is particularly inadequate among subtypes with higher levels of subordination——precisely the workers who face tighter control」
【信度】一手（ILO 官方發布，轉引已發表學術研究，作者具名可查）
【falsify 註記】此文聚焦中國「類雇員」中間地帶的實證資料，未提供跨國分類框架本身，但提供了「中間類別下、從屬性愈高的工作者社會保險覆蓋反而愈差」的實證發現——**是支持「第三類可能讓最需要保障的人反而落在保障縫隙」假設的證據**。

【來源】https://www.ilo.org/media/407896/download — ILO《Policy responses to new forms of work: International governance of digital labour platforms》，2019 年 G20 日本峰會勞動就業工作組報告（本次成功 Read PDF 全文頁 1-10）
【逐字】摘要：「National level responses can address many of the issues arising from new forms of work. With respect to cross-border, web-based digital labour platforms, however, national responses, built for an earlier era, may confront challenges.」
【逐字】報告呼籲「the development of an international governance system for digital labour platforms that sets and requires platforms (and their clients) to respect certain minimum rights and protections」，並以 2006 年《海事勞工公約》（MLC）跨國治理架構為類比範本
【信度】一手（ILO 官方報告）
【falsify 註記】**此報告聚焦「web-based 跨境群眾外包」（如 Upwork、Mechanical Turk），不是「location-based 外送」類別**——外送員在地理上固定於單一國家勞動市場，不面臨 ILO 此報告關切的「跨境法律衝突」問題，本篇不能直接套用於台灣外送專法的國際比較，**列為 negative finding**：本次搜尋未找到 ILO 針對「location-based delivery platform」的專門分類框架報告（ILO WESO 2021 涵蓋兩類但本次未能逐字取得其分類方法論章節，見 §4）。

**本報告依據上述多方來源（ILO、EPI、Peetz 2023、義大利/西班牙/英國/加拿大既有制度）綜合建構之四分類框架**（非引自單一具名機構的既定分類，而是本報告交叉多來源後的研究綜合，正文引用時須誠實標注此為研究者歸納非официal既定分類）：

1. **雇用推定型**（presumption of employment）：先假定僱傭關係成立，平台自證推翻，舉證責任在平台。代表：歐盟指令、南韓勞動者推定制、西班牙 Riders Law（僅限外送業）。
2. **第三類身份型**（third/intermediate category）：創設介於雇員與自營者之間的正式法律身份，享有部分但非全部雇員保障。代表：英國 worker、西班牙 TRADE（一般自營工作者）、加拿大 dependent contractor（判例法）。
3. **權益脫鉤型**（rights decoupled from status / 交易公平化）：不處理身份認定，直接規範特定交易行為（付款期限、契約明示、解約預告）。代表：日本フリーランス法。
4. **規則延伸型**（extension of existing rule）：不創設新身份、不做推定，而是把既有勞基法的「從屬性」認定標準直接延伸適用於符合特定客觀條件（如「他組織性」）的自營工作者。代表：義大利立法令81/2015第2條（"etero-organizzazione"）。

**台灣外送專法落點**：混合第 2 類與第 3 類之間——它像第三類身份型一樣「不判定雇傭關係、給付部分保障」，但不像英國 worker／西班牙 TRADE 是「泛用於所有自營工作者的通用身份」，而是像日本フリーランス法一樣「鎖定特定職業群體」；但又不像日本一樣迴避身份問題留給既有二元框架，而是**直接在專法內逐條列舉外送員專屬的保障項目（最低報酬、保險、演算法透明、申訴權）**，本質上更接近「不創設身份標籤、但創設身份專屬法規」的獨特混合——本次搜尋未找到與此完全對應的既有國際案例，這本身是一個值得寫入正文的發現。

---

### 2-5 「第三類身份」的國際前例與評價

【來源】https://www.lavorodirittieuropa.it/dottrina/lavori-atipici/1793-il-lavoro-eterorganizzato-e-la-disciplina-per-i-riders — 義大利勞動法學術網站
【逐字】（轉引整理）義大利立法令81/2015第2條「does not introduce a new intermediate contractual category, but rather a 'rule of discipline' aimed at applying subordinate employment protections to formally autonomous relationships characterized by a high degree of etero-organizzazione」
【信度】學術（義大利勞動法專業網站，經 WebSearch 摘要，未逐字 WebFetch 義大利文原文核對）
【falsify 註記】義大利明確**不是**創設第三類，這點值得注意——常見媒體報導籠統稱義大利「有第三類外送員身份」是不準確的簡化，正確理解是「規則延伸」而非「新身份標籤」。

【來源】https://cllpj.law.illinois.edu/content/dispatches/2021/Dispatch-No.-36.pdf — 伊利諾大學《Comparative Labor Law & Policy Journal》Dispatch 系列（學術期刊快訊）
【逐字】（經 WebSearch 摘要轉引，未逐字 WebFetch 核對）TRADE 定義：對單一客戶經濟依賴度達 75% 以上者，可申請 TRADE（Trabajador Autónomo Económicamente Dependiente）身份，享有書面契約強制、18 天有薪休假、資遣通知期等保障
【信度】學術（伊利諾大學勞動法期刊），惟**未逐字 WebFetch 原始 PDF 核對，標【存疑：僅搜尋摘要層級】**
【falsify 註記】TRADE 是西班牙**既存於 2007 年《自營工作者身份法》的一般性第三類制度**，早於 2021 年 Riders Law；西班牙對外送業另外疊加了 Riders Law 的雇用推定機制——這代表西班牙同時運作「第三類身份（TRADE，泛用）」與「雇用推定（Riders Law，僅限外送）」兩套制度，不是單一路線。

【來源】https://onlabor.org/the-classification-of-gig-workers-in-canadian-work-law/ — OnLabor（美國勞動法學術部落格，哈佛法學院背景學者參與）
【逐字】（轉引整理）「Canada has a long-standing recognition in both common law and some employment-related statutes of an intermediate category known as a 'dependent contractor'」
【逐字】Foodora 案：安大略勞動關係委員會認定「restrictions on subcontracting, Foodora's ownership and control over the Foodora App, and the system of incentives and restrictions controlling courier behaviour, strongly resembled a part-time employment relationship」，因此 Foodora 快遞員屬於安大略《勞資關係法》定義下的「員工」（透過 dependent contractor 這個中間認定路徑）
【信度】學術二手（法學院背景部落格，經 WebSearch 摘要，未逐字 WebFetch 核對原文）
【falsify 註記】加拿大 dependent contractor 是**判例法長期存在的既有概念**（非因應零工經濟新創），Foodora 案是把既有概念套用到平台工作，這跟台灣「為外送員量身訂做全新專法」的立法路徑不同——加拿大是「舊瓶裝新酒」，台灣是「新瓶新酒」。

【來源】https://connaughtlaw.com/gig-economy-worker-rights-uk-guide/ — 英國律師事務所法律指引
【逐字】「The government has committed to consulting on 'single worker status' reform by late 2025, potentially collapsing the current three-tier classification system (employee/worker/self-employed) into two categories: worker (with comprehensive employment rights) and genuinely self-employed (providing services to clients). This reform would eliminate the intermediate 'worker' category that platforms have exploited——where individuals receive some protections but lack full employee rights including unfair dismissal protection.」
【信度】權威二手（英國執業律師事務所公開指引，非官方一手，惟具體到政府諮詢時程，建議正文引用前另以英國政府官方公告核對）
【falsify 註記】**這是本次研究對「第三類身份」評價最關鍵的反面證據**：英國「worker」中間類別自 1996 年《雇用權利法》第230條存在至今已 30 年，Uber v Aslam (2021) 最高法院判決確認外送/叫車平台工作者適用——但**英國政府自己正打算廢除這個運作最久的第三類身份**，理由正是「平台一直在利用這個類別」（規避完整員工身份義務，同時只給付分次於員工的部分保障）。這直接支持「第三類身份長期而言可能變成平台的規避工具，而非保護升級」的假設。

【來源】https://www.cambridge.org/core/journals/the-economic-and-labour-relations-review/article/can-and-how-should-the-gig-worker-loophole-be-closed/C267DB9F253A374379D186F1A9573484 — David Peetz，《The Economic and Labour Relations Review》第34卷第4期，2023年12月
【逐字】（經 WebFetch 摘要轉引）「Regulating gig work as a form of contracting is a viable alternative」to employee reclassification
【逐字】「It is time to envisage labour law as something that extends not just to employees but to many contractors as well.」
【信度】學術（同儕審查期刊論文，惟本次為摘要層級轉引，未逐字取得全文 PDF）
【falsify 註記】**這是支持第三類/契約規範路線的正面學術意見**：Peetz 以澳洲新南威爾斯州（NSW）「Chapter 6 owner-drivers」制度（已運作 40+ 年）為例，主張契約規範型的中間路線比「一次性把所有零工工作者重新分類為員工」更**政治永續**——因為員工再分類容易在政黨輪替後被撤銷，且部分零工工作者本身傾向保留承攬人身份帶來的彈性。這與台灣專法「不做身份重分類、改用逐項立法給付」的政治考量邏輯相通。

【來源】https://r.jina.ai/https://www.epi.org/publication/state-misclassification-of-workers/ — Economic Policy Institute（美國智庫，勞方/進步派立場明確），2026-07-14 發布
【逐字】「When challenged by active enforcement of existing laws or new initiatives to extend minimum pay or employment protections to their workers, companies like Uber and Lyft have resorted to proposing a new 'third category' of worker——neither employee nor independent contractor.」
【逐字】此類立法「codif[y] their second-class status as nonemployees and their exclusion from a host of state and federal legal protections and benefits」
【逐字】「Because Black, brown, and immigrant workers are disproportionately represented in platform-based work, company campaigns to strip legal protections from drivers and delivery service workers help maintain deep racial inequalities and occupational segregation in U.S. labor markets.」
【信度】權威二手（智庫，勞方立場明確，非中立學術機構，數字與論點需標注立場後引用）
【falsify 註記】**這是對「第三類身份」最嚴厲的負面學術/智庫評價**，直指美國 Prop 22 模式的第三類立法本質是「企業主導遊說（花費數億美元）換來的規避工具」，不是保護升級。但須注意：EPI 討論的是**美國各州平台企業主動遊說推動的第三類立法（如 Prop 22）**，這與台灣**由六年多外送員死傷事故推動、工會與立委主導的專法立法過程**（見主報告 §A 立法歷程）在**立法發起方與政治過程**上完全相反——EPI 的批評對象是「企業要求的第三類」，不能直接套用於「工會推動的專法」，行文若引用需明確區分立法發起方向。

---

### 2-6 falsify：第三類身份是否讓平台更容易規避完整僱傭

**正面證據（支持第三類=規避工具的擔憂）**：

1. EPI（2026）：美國 Prop 22 式第三類立法由平台企業主動遊說推動，目的是規避既有法律的僱傭認定與最低薪資、僱員保障延伸。
2. 英國政府自身（經 connaughtlaw.com 轉引）正計畫廢除運作 30 年的「worker」中間類別，理由是「平台一直在利用這個類別」。
3. ILO 轉引 Xueyu Wang 研究（中國案例）：中間類別下「從屬性愈高的工作者，社會保險覆蓋反而愈不足」——保障沒有真正流向最需要的人。

**反面證據（支持第三類/契約規範=務實中間路線）**：

1. Peetz（2023，學術期刊）：契約規範型中間路線（NSW owner-drivers）已穩定運作 40+ 年，比一次性員工再分類更政治永續，且部分零工工作者本身偏好保留彈性。
2. 加拿大 dependent contractor（判例法）：Foodora 案顯示既有中間類別法理仍可被法院靈活套用保護零工工作者，未必淪為規避工具。
3. 義大利「規則延伸型」（非創設新類別）：把勞基法保障直接延伸適用於高度受組織支配的形式自營者——證明「不創設新標籤」也能達到保障目的，某種程度是對「創設新類別必然稀釋權益」擔憂的反例。

**本題結論（不做單向斷言）**：國際證據呈現**條件依賴**而非單一方向：第三類身份是否淪為規避工具，關鍵變數包括（a）**立法發起方**（企業主導遊說 vs 工會/事故驅動）、（b）**是否搭配具體、可執行、有罰則的保障條款**（而非僅停留在身份標籤）、（c）**執法資源是否到位**（有身份標籤但無執法 = 空洞保障）。台灣外送專法的立法發起方是工會與國會（非平台遊說），且逐條列舉具體保障項目與罰則（第8-11條），在既有國際案例的光譜上，**結構上更接近「規則延伸型」（義大利）與「契約規範型」（澳洲 Peetz 案例）的組合，而非「美國 Prop 22 式企業主導的第三類規避立法」**——但這是結構上的相似性判斷，不是對執行效果的預測，執行成效需待後續追蹤（見主報告 §2 子題 7 專法上路初期爭議）。

---

## §3 引語庫逐字（能當文章聲音的 verbatim）

- 「The contractual relationship between a digital labour platform and a person performing platform work through that platform shall be legally presumed to be an employment relationship where facts indicating direction and control...are found.」— EU Directive 2024/2831 Article 5(1)，https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024L2831，Ctrl-F 可驗 ✓（經 Jina Reader 代理逐字核對，官方頁面本次因 WAF 未能直連驗證）
- 「Member States shall bring into force the laws, regulations and administrative provisions necessary to comply with this Directive by 2 December 2026.」— EU Directive 2024/2831 Article 29(1)，同上 URL，Ctrl-F 可驗 ✓
- 「形式的には業務委託契約を締結している者であっても、実質的に労働基準法上の労働者と判断される場合には、労働基準関係法令が適用され、本法は適用されません。」— 公正取引委員會・厚生労働省・中小企業庁官方小冊子，https://www.jftc.go.jp/file/flpamph.pdf，Ctrl-F 可驗 ✓
- 「'노동자 추정제'를 도입하여 사용자가 노동자가 아님을 입증하지 못하면 노동자로 추정하고 노동법으로 보호하여...」— 韓國雇傭勞動部 2026年業務報告，https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18725，Ctrl-F 可驗 ✓
- 「배달 라이더가 독립적인 사업자로 고객을 직접 확보하는 것이 아니라 플랫폼사의 앱을 통해서만 주문과 배달을 수행할 수 있는 구조인 점...노동자성 인정의 근거가 됐다.」— 首爾高等法院 2026-07-03 判決（2024나2037832），經京鄉新聞轉引，https://www.khan.co.kr/article/202607071745001，Ctrl-F 可驗 ✓（記者轉述判決理由，非判決書逐字全文，建議正文引用標注「經媒體轉引之判決理由」）
- 「This reform would eliminate the intermediate 'worker' category that platforms have exploited——where individuals receive some protections but lack full employee rights including unfair dismissal protection.」— connaughtlaw.com 英國律師事務所指引，https://connaughtlaw.com/gig-economy-worker-rights-uk-guide/，Ctrl-F 可驗 ✓
- 「When challenged by active enforcement of existing laws or new initiatives to extend minimum pay or employment protections to their workers, companies like Uber and Lyft have resorted to proposing a new 'third category' of worker——neither employee nor independent contractor.」— Economic Policy Institute，2026-07-14，https://www.epi.org/publication/state-misclassification-of-workers/，Ctrl-F 可驗 ✓（經 Jina Reader 代理讀取，原站直連 403）
- 「It is time to envisage labour law as something that extends not just to employees but to many contractors as well.」— David Peetz，The Economic and Labour Relations Review 34(4)，2023，https://www.cambridge.org/core/journals/the-economic-and-labour-relations-review/article/can-and-how-should-the-gig-worker-loophole-be-closed/C267DB9F253A374379D186F1A9573484，非直接可 Ctrl-F（付費牆，本次僅取得摘要層級轉引，需標注）
- 「프리랜서 개념도 모르나…혁신 산업 위축 불가피」— 韓國業界對「노동자 추정제」反對意見，데일리팝轉引，https://www.dailypop.kr/news/articleView.html?idxno=95614，Ctrl-F 可驗 ✓

---

## §4 Negative findings（搜了沒找到什麼）

- **查無 ETUI（歐洲工會研究所）對指令的完整逐字評述**——https://www.etui.org/publications/eu-platform-work-directive 兩次嘗試（直連＋WebSearch 摘要）均 HTTP 403，僅取得 WebSearch 摘要層級的批評方向（「incomplete coverage」「zero procedural facilitations」），未能逐字核對，建議需要時另尋 ETUI PDF 報告全文或改用付費資料庫。
- **查無歐盟執委會官方逐國轉換進度追蹤頁的一手數字**——「僅 4 國已有既存推定法、18 國尚未開始」的具體統計僅見於 employsome.com 商業合規部落格轉引，未能在歐盟執委會官方頁面（如 ec.europa.eu 轉換追蹤儀表板）逐字核對，若正文要引用「18 國尚未開始」等具體數字，建議另行查證官方轉換追蹤頁。
- **查無日本厚生勞働省令和6年度施行狀況的具體統計數字**（相談件數、勧告件數、命令件數）——已 WebFetch 官方週年紀念頁確認頁面提及「令和６年度の法施行状況」但本次工具讀取未能取得表格內具體數字，需另行查證。
- **查無 ILO WESO 2021《The role of digital labour platforms in transforming the world of work》報告中提及台灣的段落**——試過 query「ILO WESO 2021 Taiwan intermediate status classification」，搜尋結果未指向報告內台灣專章或案例，該報告涵蓋範圍似以美歐拉美為主，本次未直接 WebFetch 報告全文（600+頁）逐章核對，不排除報告內有簡短提及但本次搜尋策略未命中，若後續需要應直接下載報告全文用關鍵字搜尋。
- **查無首爾高等法院 2024나2037832 判決書官方原文**（僅取得法律事務所與媒體轉引的判決理由摘錄，非대법원 종합법률정보 或법원도서관判決書全文），建議正文若需逐字引用判決理由，標注來源為「經媒體/律師事務所轉引之判決理由摘錄，非判決書全文」。
- **查無 Bristol「Gig Rights & Gig Wrongs」報告（Wood, Martindale, Burchell）逐字內容**——PDF 內容經 WebFetch 判讀為二進位/掃描格式無法解析純文字，本次未能取得具體引語，僅有先前搜尋摘要提及「classification status 對剝削與依賴的影響可能是不對稱的」（未逐字核對，不採信為引語，僅供後續線索）。
- **查無西班牙 TRADE 制度 2007 年立法官方逐字條文**（僅取得伊利諾大學期刊 Dispatch 與商業法律網站的摘要層級轉引），若正文需要 TRADE 精確定義（如 75% 收入依賴門檻的官方條文出處），建議另行查證西班牙《自營工作者身份法》（Ley 20/2007）官方文本。
- **查無「四分類框架（雇用推定型/第三類身份型/權益脫鉤型/規則延伸型）」出自單一具名學術機構或既定文獻**——這是本報告交叉多來源後的研究綜合分類，非引自 ILO/OECD/ETUI 既定的官方分類系統，正文引用時必須誠實標注為「本報告綜合國際案例後歸納」而非「某機構已建立的標準分類」，避免虛構權威來源。

---

## §5 質地素材（給 writer：場景／意象／數字對比／結尾畫面候選）

- **時間刻度的反差**：歐盟指令 2024-11 生效、轉換期限 2026-12-02，但截至 2026-07-01 全歐盟 27 國仍有 18 國「尚未開始」轉換國內法；台灣專法從 2019 年兩起死亡車禍到 2026-07-21 零時正式施行，六年半內從立法倡議走到全面上路——**「歐洲人還在討論怎麼寫法條的同時，台灣的外送員已經在用這部法律」**，這個時間刻度反差本身是個好素材，但要小心不要暗示台灣「贏了」歐盟，因為指令的推定機制一旦全面落地，對外送員的保障力度理論上比台灣更強（僱傭關係直接推定成立），只是時間上還沒到。
- **日本官方文件裡藏著的一句話**：厚生勞働省自己在官方 PDF 小冊子裡明白寫「如果你實質上是勞基法勞工，這部法律就不管你」——這句話本身透露出日本立法者的謹慎：他們寧可把「這個人到底算不算員工」的燙手山芋丟回既有的二元框架，也不願意在フリーランス法裡碰。這跟台灣立法者的選擇（不判定僱傭關係，但直接給付具體保障項目）形成有意思的對照：日本選擇「迴避+沿用舊框架」，台灣選擇「迴避+創設新框架」。
- **英國「worker」身份走到第 30 年，卻可能被自己的發明者廢除**：1996 年英國創造出「worker」這個介於員工與自營者之間的身份，2021 年最高法院用它保護了 Uber 司機，但 2025 年英國政府自己說要考慮把它廢掉——理由是平台學會了怎麼利用這個灰色地帶。**一個原本用來保護零工工作者的身份分類，用了 30 年後被政府自己判定「可能反而變成平台的工具」**，這個轉折很適合當作「第三類身份不是保障的終點，而是需要持續調校的過渡工具」這個論點的畫面。
- **南韓法院判決理由裡的三個「不能」**：外送員「不能」自己直接找客戶（只能透過平台App）、「不能」自己決定報酬怎麼算（公司事先訂好標準）、「不能」對派單有完整決定權——這三個「不能」組成南韓法院認定「勞動者性」的核心依據，跟台灣勞動部 2019 年對 foodpanda／Uber Eats「假承攬真雇傭」的認定邏輯幾乎一模一樣，只是台灣走向「創設新法給付權益」、南韓走向「回到既有勞基法框架下判定」，兩條路殊途但起點相同。
- **870萬 vs 全國外送員**：南韓「勞動者推定制」號稱涵蓋 870 萬名特殊雇傭/自由工作者/平台從業者，這個數字是台灣外送員規模（媒體估計約 15-20 萬人量級，需另查證確切數字）的數十倍——顯示南韓選擇了一條「一次性、大範圍」的制度設計，台灣選擇了「窄範圍、深規範」的專法設計，兩種規模選擇背後隱含不同的政治可行性計算：範圍越大，遭遇的產業反彈也越大（南韓業界「60年前工業時代尺度」的批評即為例證）。
