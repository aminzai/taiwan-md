---
title: "Audrey Tang: Every Famous Decision She Made Was a Refusal of the 'Genius' Label"
description: "Knocked unconscious by a classmate at age 8, declined guaranteed admission to Jianguo High School at 14, came out as transgender at 24 but refused to be a spokesperson, and at 35, her first condition for joining the cabinet was 'no office.' On December 2, 2025, in Stockholm accepting the Right Livelihood Award, what she said on stage wasn't 'I,' but 'we.'"
date: 2026-05-16
category: 'People'
tags:
  [
    'Figures',
    'Audrey Tang',
    'Ministry of Digital Affairs',
    'g0v',
    'Transgender',
    'Programming',
    'Open Government',
    'vTaiwan',
    'Plurality',
    'Right Livelihood Award',
  ]
subcategory: '教育與社會'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-05-16
lastHumanReview: true
readingTime: 14
image: '/article-images/people/audrey-tang-portrait-2016.webp'
imageAlt: 'Portrait of Audrey Tang taken in Paris in March 2016, wearing dark clothing, soft natural light portrait.'
imageCredit: 'Camille McOuat (Flickr / Wikimedia Commons, CC BY 2.0)'
lifeTree:
  protagonist: '唐鳳（Audrey Tang）'
  birthYear: 1981
  span: '1981–2025'
  source:
    article: 'knowledge/People/唐鳳.md'
    commit: 'pending'
    commitDate: '2026-05-16'
    extractedBy: 'Taiwan.md (Semiont) γ-evolve'
    extractedAt: '2026-05-16 +0800'
    note: '原文 references = 中文維基 / 臺灣女人 NMTH / 數位發展部官網 / Right Livelihood / 江明宗 Medium 等多源 cross-verify。多數重大轉折由本人公開談過，counterfactual 主要為結構性對比。'
  intro: '8 歲停學、14 歲拒絕保送建中、19 歲在矽谷當工程師、24 歲跨性別出櫃、35 歲成為全球首位跨性別部長。她每一次「離開主流軌道」都不是反叛而是選擇。這棵樹列出她選的路，也列出她沒選的——所有 alternative 都有同代結構性對照。'
  themes:
    - id: 'education'
      label: '體制 vs 自學'
      color: '#8B5CF6'
    - id: 'identity'
      label: '隱身 vs 出櫃'
      color: '#EC4899'
    - id: 'tech-policy'
      label: '純技術 vs 政治參與'
      color: '#10B981'
    - id: 'tools'
      label: '個人 vs 社群協作'
      color: '#F59E0B'
  nodes:
    - id: 'birth'
      year: 1981
      age: 0
      type: 'given'
      theme: 'education'
      label: '出生於台北（原名唐宗漢）'
      scene: '智商測驗校方做過 3 次都是「至少 160」最高等級。母親李雅卿是《中國時報》採訪組副主任，後來是教育改革者。'
    - id: 'drop-out-8'
      year: 1989
      age: 8
      type: 'choice'
      theme: 'education'
      scene: '9 年內轉換 3 所幼稚園、6 所小學；小二曾因搶考卷被同學踢一腳撞牆昏倒'
      chose:
        label: '正式停學在家自學'
        consequence: '母親洗澡時看見肚子瘀青，當下決定為她辦休學。後來李雅卿帶她到德國體驗另類教育，1994 年回台創辦烏來種籽親子實驗小學。'
      alternatives:
        - label: '繼續在體制內適應'
          plausibility: 'structural'
          note: '同代多數高智商但社交困難的孩子被診斷為亞斯/ADHD，繼續在體制內掙扎。如果留在學校，可能會走出版或學術路徑（亦可能更早 burnout）。'
        - label: '轉到資優教育班'
          plausibility: 'structural'
          note: '台灣 1980s 末已有資優教育班。如果走資優班，會跟其他高智商孩子一起被體制塑形，少了完全自由探索的時間。'
    - id: 'refuse-jianzhong'
      year: 1995
      age: 14
      type: 'choice'
      theme: 'education'
      scene: '獲得保送建中的資格'
      chose:
        label: '放棄建中 + 完全自學程式設計'
        consequence: '14 歲在烏來山中閉關後，向父母宣告不再升學。沒有老師、沒有課程，靠閱讀技術文件 + 網路社群學習。為日後推動開放教育與知識共享奠定理念基礎。'
      alternatives:
        - label: '念建中走台灣資優生路徑'
          plausibility: 'structural'
          note: '建中 → 台大 → 海外名校的標準路徑。如果走，會有正規學歷加持，但失去「14 歲就在 internet 上跟全球工程師對話」的塑形時期。'
        - label: '出國念中學'
          plausibility: 'structural'
          note: '同代部分天才兒童家庭選擇早期送出國（如 MIT 早期入學）。如果走，可能更早接觸世界一流計算機科學，但 g0v 那條公民科技線不會在台灣發生。'
    - id: 'silicon-valley'
      year: 2000
      age: 19
      type: 'choice'
      theme: 'tech-policy'
      scene: '19 歲已在加州矽谷軟體公司擔任工程師'
      chose:
        label: '深耕程式語言理論（Perl/Haskell）+ 發起 Pugs 專案'
        consequence: '2005/2/1 啟動 Pugs（用 Haskell 實現 Perl 6）。2001-2006 在 CPAN 啟動超過 100 個 Perl 專案。「用一種語言實現另一種語言」訓練了她的 meta-thinking——後來看政府就像看一個需要重構的系統。'
      alternatives:
        - label: '加入 Google / 大型科技公司'
          plausibility: 'structural'
          note: '2000 年代矽谷主流路徑。如果走，會有更高薪 + 股票，但失去 open source 社群浸淫時間。後來 g0v 的「不是員工是社群」DNA 不會出現。'
        - label: '創業'
          plausibility: 'structural'
          note: '同代矽谷工程師很多選擇創業（YC 第一批 2005）。如果走，可能成為連續創業者，但「為公共利益寫 code」的傾向會被「為股東寫 code」覆蓋。'
    - id: 'gender-transition'
      year: 2005
      age: 24
      type: 'choice'
      theme: 'identity'
      scene: '人生最重要的決定之一'
      chose:
        label: '服用雌激素 + 公開出櫃 + 改名「唐鳳」'
        consequence: '2005 年底在 blog.elixus.org 部落格自行宣告。「不管現在、過去或未來，我很樂意大家用女性的名詞來稱呼我」。父親回應「沒有理由不接受」。為台灣 LGBTQ+ 權益做出重要貢獻，但她本人後來反覆拒絕「跨性別代言人」位置，自稱「後類別」。'
      alternatives:
        - label: '私下轉換不公開'
          plausibility: 'structural'
          note: '部分跨性別者選擇低調 transition，避免社會壓力。如果走這條，職涯可能更平順，但「全球首位公開跨性別部長」的歷史地位不存在。'
        - label: '不 transition'
          plausibility: 'speculative'
          note: '[推測] 同代部分跨性別者因社會壓力選擇延後或放棄。如果走，內在張力可能影響後續創造力與公開能見度。'
    - id: 'g0v-2012'
      year: 2012
      age: 31
      type: 'choice'
      theme: 'tools'
      scene: '在矽谷已是有聲譽的開源工程師'
      chose:
        label: '與高嘉良、吳泰輝、瞿筱葳等共創 g0v 零時政府'
        consequence: "台灣最重要的公民科技社群。起點是 2012/10 對「經濟動能推升方案」廣告的不滿 + 中央政府總預算視覺化。「hack don't attack」——不攻擊既有制度，用技術改善它。萌典、IVOD、口罩地圖等模式後來被全球複製。"
      alternatives:
        - label: '繼續在矽谷做純技術'
          plausibility: 'structural'
          note: '當時矽谷對她已開放各種 senior 機會。如果留下，會是「另一個成功的台裔工程師」，不會有後來的政策影響力。'
        - label: '回台灣加入既有政黨/智庫'
          plausibility: 'structural'
          note: '走傳統政治參與路徑。如果走，會被政黨機器收編，「無黨籍政務委員」的可能性消失。'
    - id: 'sunflower'
      year: 2014
      age: 33
      type: 'choice'
      theme: 'tech-policy'
      scene: '2014/3/18 太陽花學運佔領立法院'
      chose:
        label: '一手架設場內所有線路、鏡頭、網路直播設備，但本人只待議場 1 小時即離開'
        consequence: '她認為「議場內部 5 個不同角度攝影機錄影和直接播出的情況下，所有活動已經成為純粹的展示演出和儀式」。對佔領、表態都「不感興趣」。同時自掏腰包請人做政府會議逐字稿。'
      alternatives:
        - label: '完全參與佔領 / 公開表態反政府'
          plausibility: 'structural'
          note: '同代部分技術人選擇成為運動代言人。如果走，可能成為政治明星，但失去 2016 以「無黨籍 outsider」入閣的可能性。'
    - id: 'vtaiwan'
      year: 2014
      age: 33
      type: 'choice'
      theme: 'tech-policy'
      scene: '2014/4 蔡玉玲以政務委員身份進到 g0v 黑客松，後續發展為 vTaiwan 平台'
      chose:
        label: '與政府合作 vTaiwan + Pol.is 共識引擎'
        consequence: '2015-2018 處理 26 議題，80% 引起實質政府行動。Uber 法規討論成最知名案例。國際公認的數位民主典範。'
      alternatives:
        - label: '拒絕與政府合作'
          plausibility: 'structural'
          note: '部分公民科技人堅持與政府保持距離（如 EFF 路線）。如果如此，g0v 純民間倡議路徑，不會被「招安」進體制，但也少了實際政策落地能力。'
    - id: 'digital-minister'
      year: 2016
      age: 35
      type: 'choice'
      theme: 'tech-policy'
      scene: '2016/8/9 第一次見林全、8/15 同意接任、10/1 上任'
      chose:
        label: '入閣擔任「數位政委」，談妥三條件：每週三、五遠距上班 / 會議全公開逐字稿 / 不必每天進院'
        consequence: '台灣史上最年輕政務委員 + 全球第一個公開跨性別身份的部長級政治人物 + 台灣第一位「數位政委」。'
      alternatives:
        - label: '婉拒入閣'
          plausibility: 'structural'
          note: '同類型的 outsider 技術人有人婉拒（怕被體制吸納）。如果婉拒，數位轉型工作會缺一個關鍵連結點，後來疫情口罩地圖等可能晚數月或不發生。'
    - id: 'covid-mask-map'
      year: 2020
      age: 39
      type: 'choice'
      theme: 'tools'
      scene: '2020/1/31 - 2/6 期間，吳展瑋凌晨用 Google Maps API 做的超商口罩地圖一夜燒掉 2 萬美元 API 費用'
      chose:
        label: '協調健保署 open data 釋出 + 邀集 g0v 社群共同開發藥局口罩採購地圖'
        consequence: '2/6 健保署 open data 上線同日，藥局口罩採購地圖正式上線。24 小時內 100 萬人次使用。2/15 HackMD 上有 101 個相關應用、g0v 社群建構 140+ 工具。江明宗 verbatim：「唐鳳有決定權，還能自己改 code，所以我們都不用北上向哪個長官報告」。'
      alternatives:
        - label: '只做政策不下海寫工具'
          plausibility: 'structural'
          note: '部會首長正常路徑：開會、定政策、讓承包商做。如果如此，口罩地圖可能變成 6 週才上線的官方 app（多國的 reality）。她下海推 g0v 社群跑兩天上線是關鍵。'
    - id: 'moda-minister'
      year: 2022
      month: 8
      age: 41
      type: 'choice'
      theme: 'tech-policy'
      scene: '2022/8/27 數位發展部正式揭牌'
      chose:
        label: '擔任首任部長至 2024/5/20'
        consequence: '從跨部會協調的政務委員變成有固定預算與編制的正式部長。整合電信、資安、數位經濟。首年預算員額 598 人、公務預算 57 億 + 前瞻 160 億。任期 1 年 9 個月。'
      alternatives:
        - label: '繼續當政務委員不擔任部長'
          plausibility: 'structural'
          note: '保留「跨部會自由」的彈性，避免成為被質詢的固定靶。但失去「正式部會 + 預算 + 編制」的執行力。'
        - label: '回民間繼續做 g0v'
          plausibility: 'structural'
          note: '另一條路：以 NGO 身份持續影響政策。如果走，數位發展部首任部長會是別人，很可能用更傳統官僚方式管理。'
    - id: 'stockholm'
      year: 2025
      month: 12
      age: 44
      type: 'choice'
      theme: 'tools'
      scene: '2025/12/2 斯德哥爾摩 Right Livelihood Award 頒獎台'
      chose:
        label: '接受「另一個諾貝爾獎」，台上演說將焦點推回集體'
        consequence: "首位獲此獎台灣人。Citation：「For advancing the social use of digital technology to empower citizens, renew democracy and heal divides」。接受演說 verbatim：「Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation」+ 個人哲學重述「The superintelligence we are looking for is already here. It's us」。"
      alternatives:
        - label: '在頒獎台上講「我的成就」'
          plausibility: 'structural'
          note: '同代得獎者常以個人故事為敘事中心。如果走，獎座變成個人勳章，但她選擇把舞台 reframe 成「我們」——她拒絕當天才這條主線的最後一個變奏。'
translatedFrom: 'People/唐鳳.md'
sourceCommitSha: 'e75b621d2'
sourceContentHash: 'sha256:1917aa69dfd8ab97'
translatedAt: '2026-09-22T09:41:22.277894+00:00'
---

# Audrey Tang: Every Famous Decision She Made Was a Refusal of the "Genius" Label

> **30-Second Overview:**
> At age 8, kicked unconscious by a classmate and took a leave of absence; at 14, declined guaranteed admission to Jianguo High School; at 24, came out as transgender but refused to be a spokesperson; at 35, her first condition for joining the cabinet was "no office." In the early hours of 2020, she and Ming-Tsung Chiang wrote code on the g0v Slack to build the mask map; on December 2, 2025, in Stockholm accepting the Right Livelihood Award, the audience awaited her personal story, but on stage she emphasized the word "we." The world treats her as a genius; every famous decision she has made is a refusal of that position.

## A Mask Map That Burned Through Twenty Thousand Dollars

In late January 2020, COVID-19 began spreading in Taiwan. Pharmacy mask supplies ran tight, and the government announced a name-based rationing system starting February 6. Howard Wu (Wu Zhan-wei), an engineer at Tainan's HowsWork Studio, took matters into his own hands in the early hours of February 2, building a map that could query nearby convenience store mask inventory using the Google Maps API. He deployed it before dawn and shared it on social media[^1].

By noon, after he returned to his computer from lunch, the Google API backend bill had already hit US$20,000 — the surge of usage over 24 hours had burned through it.

That day, Audrey Tang appeared in the g0v Slack channel. She wasn't there to give orders. She coordinated with the Google engineering team to first put the current bill on hold; at the same time, she brought in a few g0v veterans — Ming-tsung Chiang (kiang, former executive secretary of the Tainan Smart City Office), and the NHI Administration's Information Division (Ling-chih Chang, Tzu-yu Chen) — to figure out: how to sync the mask inventory of over 6,000 pharmacies across Taiwan every 30 seconds to a map anyone could open[^2].

By 8:00 a.m. on February 6, the moment the NHI Administration officially released the open data, the pharmacy mask purchasing map went live. Within 24 hours, it saw over 1 million user visits. By February 15, HackMD had accumulated 101 related applications, and the g0v community had produced over 140 tools[^2][^3].

In his speech transcript afterward, Ming-tsung Chiang left this passage:

> ✦ "The Minister is extremely well-versed in information architecture; she understands any requirement we bring up. Most importantly, Audrey Tang has decision-making authority and can write code herself, so we didn't have to go up to Taipei to report to some superior."[^4]

The protagonist of this story isn't Audrey Tang alone. It's Ming-tsung Chiang, Howard Wu, those civil servants from the NHI Administration's Information Division, the hundreds of engineers in the g0v community, and that entire string of nights when Audrey Tang's office took turns writing code.

But after 2020, every version written by foreign media made her the sole protagonist. BBC wrote "Audrey Tang Used Code to Save Taiwan"; Wired wrote "The Hacker Who Became Taiwan's Digital Minister"; TIME placed her among the "Global Leaders Fighting the Pandemic."

In every interview, she pushes the credit back to the team. But the "genius minister saves Taiwan" narrative has stuck to her for over forty years; it's not so easily shaken off.

## Knocked Unconscious by Classmates at Age 8, Refused Chien-kuo High School at 14

Audrey Tang was born in Taipei on April 18, 1981. Her birth name was Tang Tsung-han. Her father, Tang Kuang-hua, was the former deputy editor-in-chief of the _China Times_; her mother, Lee Ya-ching, was the deputy head of the paper's reporting division[^5].

She had a congenital heart condition. The school administered three IQ tests; each showed "at least 160" (the ceiling of the testing instrument). At age 8, her family did not yet have a computer. She read a book on Applesoft BASIC programming and proceeded to hand-draw a computer keyboard and screen on paper, writing out the keys and what the computer might output[^5].

But the "child prodigy" label — possibly the adjective most frequently attached to her name in 2026 — had no place on that 8-year-old child in 1989. That space held only mob beatings, bruises, and "why don't you just die."

Over six years of elementary school she transferred through three kindergartens and six primary schools. One day in second grade, the teacher handed out an exam and left the classroom. Tang finished early; several classmates who couldn't solve the problems reached out to snatch her paper. She ran with the exam, fell, and one classmate kicked her with full force. She hit the wall and lost consciousness[^6]. Later that classmate uttered a sentence that _Business Weekly_ preserved verbatim:

> ✦ "Why don't you die? If you died, I'd be the best."[^6]

She didn't tell anyone when she got home. One day her mother saw the bruises on her abdomen while bathing her and immediately arranged for her to take a leave of absence[^6].

Her mother, Lee Ya-ching, later went to Germany to study alternative education and founded the Seeds Experimental Elementary School in Wulai in 1994, serving as its first principal[^7]. In 1995, after a period of seclusion in the Wulai mountains, 14-year-old Tang declared to her parents: she would not continue formal schooling, giving up her guaranteed admission to Chien-kuo High School[^8].

This was not a choice of "I'm too gifted for school." It was a child who had learned to hide herself at age 8 deciding at 14 that the box labeled "gifted student" was a version of herself she refused.

She has said many times since: "I don't think the modern world still has a concept of genius. In the internet era, everyone is effectively IQ 180."[^9]

## At 24 She Changed Her Name, But Refused to Be a Transgender Spokesperson

At age 12 she began learning Perl[^10]. At 19 (2000) she was already working as an engineer at a software company in California's Silicon Valley[^11].

On February 1, 2005, at age 24 she launched the Pugs project—a compiler and interpreter for Perl 6 implemented in Haskell[^12]. In the Perl community, Pugs was a bootstrap project: a language implementing itself in another language. Between 2001 and 2006 she initiated over 100 Perl projects on CPAN[^13]. The international open source community calls her Audrey or au.

In late 2005, on her own blog blog.elixus.org, she publicly came out as transgender[^14]. She took estrogen but did not undergo surgery. She changed her Chinese name to 「唐鳳」, and her English name from Autrijus to Audrey.

In that blog post she wrote:

> ✦ "Regardless of now, past, or future, I would be happy for everyone to refer to me with female pronouns."[^14]

Her father Tang Kuang-hua's response when interviewed was later recorded verbatim by multiple media outlets:

> ✦ "If she feels that gender transition can make her happier, better able to exert her creativity, and not harm anyone, there is no reason not to accept it."[^15]

She refused the position of "transgender spokesperson." In 2020, on the Cabinet personnel form's gender field, she wrote "none." At the time she explained to reporters[^16]:

> ✦ "I am 'post-category.' In gender debates I don't take sides. It's not that I think this issue is unimportant, but that I believe debate cannot solve any problems."[^16]

In an interview with Marie Claire, she left another frequently quoted remark:

> ✦ "If you can live with bewilderment, slowly you can see that it's neither your problem nor society's problem, but the gap in between. All things have gaps, and gaps are where the light enters."[^17]

From 2010 to 2016 she served as a part-time consultant for Apple, participated in Siri development; her hourly rate was reportedly equivalent to 1 bitcoin[^18]. At age 33 (2014) she handed off her work at Socialtext and Apple, announcing her "retirement"[^11].

## g0v and the Sunflower Legislature: Giving Credit to the Invisible

In October 2012, she co-founded g0v (Zero-Time Government) with Kao Chia-liang (clkao), Wu Tai-hui (Kirby), and Chiu Hsiao-wei (ipa). The starting point was dissatisfaction with an Executive Yuan advertisement for the "Economic Dynamism Promotion Plan"—a government propaganda ad with a budget of NT$33 million that, after watching, left viewers unclear about what the government actually intended to do[^19].

g0v's first project was the Central Government General Budget Visualization: spreading the thick budget volumes into clickable charts one by one[^19]. Later came MoeDict, the Legislative Yuan Video-on-Demand System (IVOD), and the Sunflower Movement's legislative chamber livestream.

In the late night of March 18, 2014, students occupied the Legislative Yuan chamber. All the wiring, cameras, and livestreaming equipment inside the chamber were set up single-handedly by Audrey Tang[^20].

But she stayed in the chamber for only an hour before leaving. Later, PTS PNN interviewed her, and she said:

> ✦ "With five cameras filming from different angles inside the chamber and broadcasting live, all activities have already become pure performance and ritual."[^20]

She was "not interested" in either the occupation or making statements. What she cared about was tooling and technology. At the same time, she paid out of pocket to have people produce verbatim transcripts of government meetings—so that those not on site could also read the complete dialogue[^20].

After the Sunflower Movement ended, in April 2014, then-Minister without Portfolio Tsai Yu-ling walked into a g0v hackathon. From that moment on, the two originally opposing terms "government" and "g0v" began to grow a middle ground[^21].

That middle ground was called vTaiwan. From 2015 to 2018, the platform handled 26 issues, 80% of which led to concrete government action[^22]. The most famous example was the Uber regulatory discussion: taxi operators and Uber supporters had been deadlocked for six years, and ultimately Uber was legalized under seven conditions[^22].

The platform's core is the Pol.is consensus engine—large volumes of opinions are organized by machine into a few clusters, allowing every participant to see "who thinks like me, who thinks very differently from me, and which positions everyone agrees on." It doesn't vote, doesn't create opposition; it only draws the shape of divergence.

## No Office, Fully Public Transcripts, Three Days Remote Per Week

On August 9, 2016, 35-year-old Audrey Tang met with Premier Lin Chuan for the first time. On August 15, she agreed to serve as Minister without Portfolio. In late September, she returned to Taiwan from Silicon Valley. On October 1, she entered the Executive Yuan[^23].

The three conditions she negotiated beforehand later became the first breach in Taiwan's civil service system: working remotely on Wednesdays and Fridays; all meetings with public transcripts; no need to come to the Executive Yuan daily[^23].

Lin Chuan explained to reporters at the time:

> ✦ "The Executive Yuan currently has no remote work regulations, but her long-term work mode has always been remote. I believe that as long as work is unaffected, conveying ideas or policy directives remotely via computer is feasible."[^24]

She became three things: the youngest Minister without Portfolio in Taiwan's history, the world's first openly transgender minister-level political figure, and Taiwan's first "Digital Minister"[^25].

She had no fixed office in the Executive Yuan. She said the entire compound was her office space. After meetings ended, transcripts were posted to sayit.pdis.nat.gov.tw, where anyone could search them[^26].

She assembled a 20-person team called PDIS (Public Digital Innovation Space). Half were civil society professionals, half were volunteers from various ministries. In summer, 30 more interns were added[^26]. It was not a hierarchical organization—it was a workspace.

In 2019, she was named to _Foreign Policy_'s Global Thinkers 100 (readers' choice category)[^27]. Media described her as the "world's only openly transgender minister" and a "programming star." In every interview she would deflect credit—but the "genius minister" story was easier to repeat than her own words.

![Audrey Tang at the re:publica Digital Society Conference in Berlin, May 2019](/article-images/people/audrey-tang-re-publica-2019.webp)
_At the re:publica Digital Society Conference in Berlin on May 8, 2019, during the "Digital Social Innovation" dialogue, Audrey Tang shared the stage with Julia Kloiber. Photo: Jan Michalko. [CC BY-SA 2.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg).\_

## Conservative Anarchism: Refusing to Command, Also Refusing to Be Commanded

Audrey Tang describes herself as a "conservative anarchist." On the surface, it is a contradiction in terms.

"Conservative" (conservative) means preserving existing, well-functioning systems; "anarchist" (anarchist) means opposing concentrated power and refusing top-down coercion. Someone who puts these two words together usually means: I believe some things in the existing system have value, but I do not believe anyone is qualified to use authority to force others to accept.

Her interview with Rest of World left a near-manifesto statement:

> ✦ "Any top-down, coercion, whether it's from the capitalists or from the state, is equally bad."[^28]

In her interview with economist Tyler Cowen, when asked "What is your role?", she said:

> ✦ "I'm working _with_ the government; I'm not working _for_ the government."[^29]

At the 2020 International Conference on Functional Programming (ICFP) Q&A, she also threw out this line:

> ✦ "In Taiwan we have this strange idea that broadband internet access is a human right. Everyone has broadband. And if you don't, it's my fault, personally."[^30]

She uses the term "human right" heavily, but "personal responsibility" lightly. The government work attitude she wants to embody is called "if something is lacking somewhere, I'll go fill the gap."

There is a principle in her work philosophy called humor over rumor. After the CoFacts system detects viral disinformation, her team produces a two-minute video or two images (within 200 characters) within two hours, using humor to respond to fake news. Abbreviated as the 2-2-2 principle.[^31]

The "toilet paper panic" of February 2020 was the most cited case by international media during that period: a rumor circulated that masks and toilet paper used the same pulp, triggering panic buying; the Executive Yuan released an infographic within hours (then-Premier Su Tseng-chang's "we only have one butt" shoulder-patting image), accompanied by a supply chain explanation showing different raw material sources, and the rumor cooled that same day[^31]. She cited this as a "humor over rumor" case study in TED talks and multiple international interviews: rumors were not suppressed by law, but covered over by an image funnier than the rumor itself that also embedded the facts.

On August 27, 2022, the Ministry of Digital Affairs (MODA) was officially inaugurated, and she assumed office as its first minister[^32]. The first-year budget authorized 598 personnel, with an operational budget of NT$5.7 billion plus NT$16 billion in forward-looking funds, totaling NT$21.7 billion[^33].

During her tenure she advanced digital resilience (persuading the UK's OneWeb and Luxembourg's SES to deploy low- and medium-Earth orbit satellite terminals in Taiwan), amended the Electronic Signatures Act which had gone 20 years without revision, launched the 111 government-exclusive short-code SMS platform to combat fraud, and required 47 A-level agencies to adopt the T-Road unified transmission standard within two years[^34][^35].

But she also faced substantial criticism. TPP chair Ko Wen-je questioned "an average of NT$30 million per person — what kind of job is this?"; DPP legislator Liu Shih-fang said "the Digital Ministry still hasn't found its direction"; KMT legislator Wu Yi-ding said "the online fraud the public cares most about has seen no concrete action"[^36][^37].

Even the PO (Participation Officer) civil servants appointed by PDIS into various ministries were confused themselves. A reporter interviewed one PO for a verbatim account:

> ✦ "I've been a PO for 2 months now, I feel like it's just an extra job, and I still don't understand how much we can intervene or how much authority we can get... I don't know what our role will be on these platforms in the future?"[^38]

She couldn't answer this question. Or rather, her answer was: you decide for yourself.

The cost of "demo, not command" was slowness, unimpressive KPIs, and two years passing without anyone able to clearly articulate "what the Digital Ministry actually did." Her wager was on cultural change — and cultural change either takes hold or it doesn't.

But PDIS's SayIt public verbatim transcript system had accumulated full-text records of over 7,000 meetings by the day she left office[^26]. Anyone entering keywords like "Uber," "masks," or "LINE Pay" can read every word she spoke with industry representatives, civil servants, and legislators at the time. This system did not exist before she entered government, and no one has removed it since her departure. She couldn't sum it up in a single soundbite of political achievement, but she did leave behind a seven-year searchable record of government dialogue — the first of its kind in Taiwan's political history.

On the evening of May 20, 2024, after President Lai Ching-te's inauguration ceremony concluded, Audrey Tang headed straight for Taoyuan Airport. Over the next three months, she visited 20 countries[^39].

In April of the same year, she, economist Glen Weyl, and the globally dispersed Plurality Community jointly published _Plurality: The Future of Collaborative Technology and Democracy_. The book was released under CC0—meaning anyone can use the book's full text for any purpose, without attribution, without payment, and without seeking permission[^40].

For the title "Plurality," they used a single Chinese character as a symbol: ⿻ (written as "衆" in Chinese, pronounced similarly to zhòng). This character is one of the "Ideographic Description Characters" in Unicode, used to describe a structure where "two things are interwoven." She explained to international media that ⿻ emphasizes "interweaving"—the differences of many individuals are not erased, but form a collective texture. This concept is the exact opposite of "genius": a genius is a single bright spot set against surrounding grayness; ⿻ is every thread wrapped around the others, each indispensable.

The vTaiwan handling of the Uber regulatory case is an example she often cites to illustrate ⿻: taxi operators and Uber supporters deadlocked for six years, until Uber was legalized under seven additional conditions[^22]. In this consensus, no side completely "won," but neither did any side completely "lose." She says that is democracy's true shape—the work of weaving everyone's textures into a single cloth.

On October 7, the Ministry of Foreign Affairs appointed her as the Republic of China (ROC) Ambassador-at-Large (Cyber Ambassador-at-Large)[^41]. On her personal homepage audreyt.org and cyberambassador.tw, the unchanging opening line is:

> ✦ "I want to be a good enough ancestor for future generations." (I want to become an ancestor worthy of future generations.)[^42]

On December 2, 2025, in Stockholm, at the Right Livelihood Foundation's award hall. The Right Livelihood Award, known as the "Alternative Nobel Prize," was founded in 1980 by Swedish-German philanthropist Jakob von Uexküll to address fields not covered by the Nobel Prize.

Audrey Tang is the first Taiwanese person to receive this award[^43]. The citation reads:

> ✦ "For advancing the social use of digital technology to empower citizens, renew democracy and heal divides." (In recognition of advancing the social application of digital technology, empowering citizens, renewing democracy, and healing divides.)[^43]

In her acceptance speech, the first thing she spoke about was not what she had done. She spoke about what cyberspace is:

> ✦ "Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation. It is time we work on peace in this zone." (Cyberspace is a conflict zone, and my work turns that conflict into an energy source for co-creation. It is time for us to do the work of peace in this zone.)[^43]

Then she reiterated the words from the cover of _Plurality_:

> ✦ "The superintelligence we are looking for is already here. It's us." (The superintelligence we have been searching for has already arrived. It is us.)[^44]

She accepted the trophy known as the "Alternative Nobel Prize," then on the podium shifted the focus to "us"—she, whom the world treats as a Taiwanese genius, once again refused the position of "genius."

From the 8-year-old child kicked in a gifted-class classroom in 1989, to the 44-year-old standing on the Stockholm podium in 2025, between them lies a long road paved with one refusal after another. Each refusal looks like rebellion, but viewed together, they reveal themselves as variations on a single motion: refusing to be defined by the position of "exceptional individual," placing herself back in the role of node, bridge, space-builder.

She refuses to be a genius. The world insists on treating her as one. But she has never let the world win this argument—it just takes the world a long time to understand what she is really saying.

![Audrey Tang 2021 publicly released personal signature SVG](/article-images/people/audrey-tang-signature.svg)
_Audrey Tang's personal signature SVG released publicly in August 2021, originally for use by Japan's *Bungeishunjū*. Author: Audrey Tang herself, [CC0 Public Domain](https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg).\_

## Further Reading

- [Sodagreen: From the Gongliao Small Stage to the "Oaeen" Struggle, a Twenty-Year Battle to Reclaim Musical Sovereignty](/en/music/sodagreen) — Another Taiwanese anomaly that rose in the 2000s, another long-term struggle to "refuse being defined by prescribed identity," only the arena is the music industry rather than government
- [Tony Hsiao](/en/people/tony-hsiao-inside-founder) — Co-founder of INSIDE and iCook, who similarly defines his role in Taiwan's tech scene by "crossing multiple domains"
- [Tai-yu Wu](/en/people/tai-yu-wu) — The legacy of Taiwan's intellectual elite from science to technology; Wu Tai-yu laid the foundation for Taiwan's research system as President of Academia Sinica
- [Open Culture Foundation](/en/technology/open-culture-foundation) — A foundation that grew from g0v's accounting backend into a bridge for Taiwan's digital rights, having engaged with the Ministry of Digital Affairs under Audrey Tang's leadership multiple times, both cooperating and keeping watch
- [Taiwan's COVID-19 Pandemic and Vaccines](/society/台灣新冠疫情與疫苗) — The epidemic context behind the mask map's coordination chain, and the eighteen months Taiwan bought through borders and masks

## Image Sources

This article uses 3 images, all cached in `public/article-images/people/` to avoid hotlinking the source servers. All three are licensed under Wikimedia Commons CC / CC0:

- **hero**：[Portrait Audrey Tang (cropped)](<https://commons.wikimedia.org/wiki/File:Portrait_Audrey_Tang_(25915794061,_cropped).jpg>) — Photo: Camille McOuat, 2016-03-09 Paris, CC BY 2.0
- **scene-mid**：[Re:publica 19 - Day 3](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>) — Photo: Jan Michalko, 2019-05-08 Berlin re:publica Digital Society Conference, CC BY-SA 2.0
- **signature**：[Audrey Tang signature](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>) — Author: Audrey Tang herself, 2021-08-18, CC0 Public Domain

## References

[^1]: [TechNews: Single-handedly Building the Mask Map, Revealing the Behind-the-Scenes Team of "Keyboard National Salvation" (2020-02-23)](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Details Howard Wu deploying at dawn and the $20,000 API bill, plus the timeline of Audrey Tang coordinating Google and g0v

[^2]: [Ming-Tsung Chiang Medium: Pharmacy Mask Procurement Map Goes Live (2020-02)](https://medium.com/%E6%B1%9F%E6%98%8E%E5%AE%97-kiang/%E8%97%A5%E5%B1%80%E5%8F%A3%E7%BD%A9%E6%8E%A1%E8%B3%BC%E5%9C%B0%E5%9C%96%E4%B8%8A%E7%B7%9A-54e11bd63e84) — Engineer's firsthand account, verbatim "Official data expected to go live at 8 AM on 2/6" + Audrey Tang coordinating community participation in development

[^3]: [Ministry of Health and Welfare COVID-19 Key Epidemic Prevention Decisions Website](https://covid19.mohw.gov.tw/ch/cp-4822-53563-205.html) — Official government account verbatim: "Executive Yuan Minister without Portfolio Audrey Tang invited civil society groups to produce the 'Epidemic Prevention Mask Inquiry' application platform through NHI open data"

[^4]: [TechNews: Single-handedly Building the Mask Map (same as [^1])](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — See original link for supplementary details

[^5]: [Chinese Wikipedia 'Audrey Tang' Entry](https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3) — Birth / family background / childhood self-taught BASIC paper keyboard and other basic biographical data

[^6]: [Business Weekly: Bullied by Jealous Classmates Kicked Unconscious... Genius Audrey Tang Wanted to Commit Suicide Multiple Times in Childhood (2020-11)](https://www.businesstoday.com.tw/article/category/183035/post/202011090020/) — Second-grade classroom gang-beating scene + classmate quote "Why don't you just die" verbatim + mother discovers bruises while bathing, decides to withdraw from school

[^7]: [China Times News Network: Youngest Minister Audrey Tang, Lee Ya-ching Implements Educational Reform Self-Study Model (2016-08-25)](https://www.chinatimes.com/realtimenews/20160825005980-260405) — Lee Ya-ching returned to Taiwan in 1992, founded Wulai Seedling Parent-Child Experimental Elementary School in 1994 as first principal

[^8]: [Taiwan News: Escaping 'Campus Bullying' to Self-Study! Audrey Tang's 'Major Discovery' at Age 14](https://www.taisounds.com/specialtopic/content/46/23226) — At 14, after seclusion in Wulai, refused guaranteed admission to Chien Kuo High School

[^9]: Cited by multiple media outlets, personally reiterated in various interviews: "I don't think the modern world still has the concept of genius" "In the internet era, everyone is actually IQ 180"

[^10]: [Wikipedia: Audrey Tang](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang started programming at the age of eight and began learning Perl at the age of 12"

[^11]: Chinese Wikipedia 'Audrey Tang' entry (same as [^5]) — Employed as Silicon Valley engineer at age 19 in 2000, handed over Socialtext + Apple jobs and announced retirement at age 33 in 2014

[^12]: [Wikipedia: Pugs (compiler)](https://en.wikipedia.org/wiki/Pugs_(compiler) — Wikipedia entry

[^13]: [Wikipedia: Audrey Tang (English)](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang initiated over 100 Perl projects between June 2001 and July 2006, including the popular PAR archiver"

[^14]: Chinese Wikipedia 'Audrey Tang' entry (same as [^5]) + multiple media verbatim consistently quote: "Whether now, past, or future, I'm happy for everyone to refer to me with female nouns." Original source is 2005 blog blog.elixus.org

[^15]: [Business Weekly: Exclusive Interview with Audrey Tang's Father (2016-09)](https://www.businesstoday.com.tw/article/category/80407/post/201609010032/) — Father Tang Kuang-hua verbatim "No reason not to accept"

[^16]: [Taiwan Women NMTH: Taiwan's First Transgender Cabinet Member, First Digital Minister — Audrey Tang](https://women.nmth.gov.tw/?p=20105) — Audrey Tang verbatim 'I am post-category' + background of 2020 cabinet personnel form gender field filled 'none'

[^17]: [Marie Claire Taiwan: After Childhood Bullying, Audrey Tang Says: 'Live Well with Bewilderment'](https://www.marieclaire.com.tw/entertainment/story/52923/audrey-tang) — verbatim 'Everything has a crack; the crack is where the light enters'

[^18]: [Chinese Wikipedia entry on Audrey Tang (same as [^5])+](https://www.britannica.com/biography/Audrey-Tang) — see original link for supplementary details

[^19]: [Taiwan Panorama: Civic Hacker Power g0v Zero-Time Government](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — October 2012 starting point + central government total budget visualization + list of co-founders

[^20]: [PTS News PNN: Sunflower Student Movement Coverage (2014)](https://news.pts.org.tw/article/327548) — verbatim 'All lines, cameras, and all live streaming equipment in the venue were set up single-handedly by him, civic hacker "Audrey Tang"' + Audrey Tang's commentary on the chamber's 'performances and rituals' + self-funded verbatim transcripts

[^21]: [The Reporter: Creating Dialogue Space — Audrey Tang's Fantastical Journey](https://www.twreporter.org/a/g0v-audrey-tang) — verbatim April 2014 Tsai Yu-ling enters g0v hackathon + vTaiwan origins

[^22]: [Democracy Technologies: Consensus Building in Taiwan](https://democracy-technologies.org/participation/consensus-building-in-taiwan/) — vTaiwan 2015-2018 handled 26 issues / 80% prompted concrete government action / Uber legalized under 7 conditions

[^23]: [Liberty Times: Breaking Tradition, Audrey Tang Works Remotely Wednesdays and Fridays (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859132) — 8/9 first meeting with Lin Chuan / 8/15 agreed / 10/1 took office / three conditions for joining cabinet

[^24]: [Liberty Times: Audrey Tang Remote Work, Lin Chuan: This Is Feasible (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859246) — Lin Chuan verbatim 'The Executive Yuan currently has no regulations on remote work... this is feasible'

[^25]: Chinese Wikipedia entry on Audrey Tang (same as [^5]) — at age 35, Taiwan's youngest minister without portfolio in history + world's first openly transgender cabinet-level political figure

[^26]: [pdis.nat.gov.tw Work Records and SayIt Public Verbatim Transcript System](https://sayit.pdis.nat.gov.tw/) — PDIS team 20-person structure + half from civil society + half from ministry volunteers + 30 interns

[^27]: [Taipei Times: Audrey Tang named in "Top 100 Global Thinkers"（2019-01-25）](https://www.taipeitimes.com/News/front/archives/2019/01/25/2003708586) — Foreign Policy Global Top 100 Thinkers selection (readers' choice category)

[^28]: [Rest of World: Audrey Tang on her "conservative-anarchist" vision for Taiwan's future（2020）](https://restofworld.org/2020/audrey-tang-the-conservative-anarchist/) — verbatim "Any top-down, coercion, whether it's from the capitalists or from the state, is equally bad"

[^29]: [Conversations with Tyler Ep.106: Audrey Tang](https://conversationswithtyler.com/episodes/audrey-tang/) — verbatim "I'm working with the government; I'm not working for the government"

[^30]: [Lindsey on X: Real-time Quote from ICFP 2020 Q&A](https://x.com/lindsey/status/1297886318114963456) — verbatim "In Taiwan we have this strange idea that broadband internet access is a human right"

[^31]: [SwissInfo: Freedom of expression: humour over rumour](https://www.swissinfo.ch/eng/politics/freedom-of-expression-humour-over-rumour-lessons-from-taiwan-in-digital-democracy/46592080) — See original link for supplementary content

[^32]: [Ministry of Digital Affairs Official Website: Past Ministers](https://moda.gov.tw/aboutus/ministers-since-2022/1527) — verbatim「August 27, 2022 – May 20, 2024」Audrey Tang's term

[^33]: [Liberty Times: Audrey Tang to Head Digital Ministry, Budget Staff of 598](https://news.ltn.com.tw/news/politics/breakingnews/4021987) — Liberty Times report

[^34]: [Liberty Finance: From Genius IT Minister to Free Lecturer – Review of Audrey Tang's Three Major Achievements and Controversies](https://ec.ltn.com.tw/article/breakingnews/4677986) — Digital Resilience / OneWeb / SES Satellites / Electronic Signature Act Amendment / 111 Short Code SMS Platform

[^35]: [INSIDE: Ministry of Digital Affairs 1st Anniversary! Counting Audrey Tang's Two Major Achievements and Three Major Controversies](https://www.inside.com.tw/article/32615-Taiwan-moda-anniversary) — 47 A-level agencies T-Road unified transmission standard + colleagues verbatim「Compared to previous units, Audrey Tang is more willing to delegate power」

[^36]: [Global Views Monthly: Audrey Tang Leads 'Ministry of Digital Affairs' Near 1 Year Since Launch, Critics Say No Achievements](https://www.gvm.com.tw/article/105627) — Liu Shih-fang / Wu Yi-ting verbatim criticism

[^37]: [ETtoday: MODA Budget NT$21.1 Billion, Ko Wen-je Shocked: Average NT$30 Million Per Person 'What Kind of Job Is This?' (2022-08-30)](https://www.ettoday.net/news/20220830/2327863.htm) — Ko Wen-je verbatim questioning

[^38]: [The Reporter: Open Government, How Did Audrey Tang Pass the Civil Servant Hurdle?](https://www.twreporter.org/a/open-government-audrey-political-commissar-challenges) — PO verbatim「Been a PO for 2 months... still unclear how much we can intervene」

[^39]: [Liberty Finance: From Genius IT Minister to Free Lecturer (same as [^34])](https://ec.ltn.com.tw/article/breakingnews/4677986) — Liberty Times report

[^40]: [Plurality Institute: Book Launch of Plurality](https://www.plurality.institute/blog-posts/book-launch-plurality-the-future-of-collaborative-technology-and-democracy-by-e-glen-weyl-audrey-tang-and-the-plurality-community) — Co-authored with Glen Weyl + Plurality Community / Published April 16, 2024 / Released under CC0

[^41]: [Chinese Wikipedia 'Audrey Tang' Entry (same as [^5])+](https://cyberambassador.tw/) — See original link for supplementary content

[^42]: [audreyt.org](https://audreyt.org/) — See original link for supplementary content

[^43]: [Right Livelihood: Taiwan's Audrey Tang honoured with Right Livelihood Award（2025）](https://rightlivelihood.org/news/taiwans-audrey-tang-honoured-with-right-livelihood-award-for-advancing-digital-democracy-and-social-trust/) — Citation verbatim + Tang acceptance speech verbatim「Cyberspace is a conflict region」paragraph + [Focus Taiwan CNA English Report](https://focustaiwan.tw/society/202512030022)

[^44]: cyberambassador.tw verbatim + Plurality book cover philosophy restatement — "The superintelligence we are looking for is already here. It's us"
