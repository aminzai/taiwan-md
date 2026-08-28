---
title: 'Audrey Tang: Every Famous Decision She Made Was a Refusal of the “Genius” Label'
description: 'Kicked unconscious by classmates at eight, turning down a guaranteed place at Taipei Municipal Jianguo High School at fourteen, coming out as transgender at twenty-four while refusing to become its spokesperson, and making “no office” the first condition of joining the cabinet at thirty-five. In 2020, in the small hours, she was patching code in the g0v Slack to build the mask map; on December 2, 2025, she accepted the Right Livelihood Award in Stockholm — and the word she stressed on stage was not “I,” but “we.”'
date: 2026-05-16
category: 'People'
tags:
  [
    'People',
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
author: 'Taiwan.md Contributors'
featured: true
lastVerified: 2026-08-28
lastHumanReview: false
readingTime: 22
image: '/article-images/people/audrey-tang-portrait-2016.webp'
imageAlt: 'Portrait of Audrey Tang, photographed in Paris in March 2016; dark clothing, a soft natural-light portrait.'
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
    - id: education
      label: '體制 vs 自學'
      color: '#8B5CF6'
    - id: identity
      label: '隱身 vs 出櫃'
      color: '#EC4899'
    - id: tech-policy
      label: '純技術 vs 政治參與'
      color: '#10B981'
    - id: tools
      label: '個人 vs 社群協作'
      color: '#F59E0B'
  nodes:
    - id: birth
      year: 1981
      age: 0
      type: given
      theme: education
      label: '出生於台北（原名唐宗漢）'
      scene: '智商測驗校方做過 3 次都是「至少 160」最高等級。母親李雅卿是《中國時報》採訪組副主任，後來是教育改革者。'
    - id: drop-out-8
      year: 1989
      age: 8
      type: choice
      theme: education
      scene: '9 年內轉換 3 所幼稚園、6 所小學；小二曾因搶考卷被同學踢一腳撞牆昏倒'
      chose:
        label: '正式停學在家自學'
        consequence: '母親洗澡時看見肚子瘀青，當下決定為她辦休學。後來李雅卿帶她到德國體驗另類教育，1994 年回台創辦烏來種籽親子實驗小學。'
      alternatives:
        - label: '繼續在體制內適應'
          plausibility: structural
          note: '同代多數高智商但社交困難的孩子被診斷為亞斯/ADHD，繼續在體制內掙扎。如果留在學校，可能會走出版或學術路徑（亦可能更早 burnout）。'
        - label: '轉到資優教育班'
          plausibility: structural
          note: '台灣 1980s 末已有資優教育班。如果走資優班，會跟其他高智商孩子一起被體制塑形，少了完全自由探索的時間。'
    - id: refuse-jianzhong
      year: 1995
      age: 14
      type: choice
      theme: education
      scene: '獲得保送建中的資格'
      chose:
        label: '放棄建中 + 完全自學程式設計'
        consequence: '14 歲在烏來山中閉關後，向父母宣告不再升學。沒有老師、沒有課程，靠閱讀技術文件 + 網路社群學習。為日後推動開放教育與知識共享奠定理念基礎。'
      alternatives:
        - label: '念建中走台灣資優生路徑'
          plausibility: structural
          note: '建中 → 台大 → 海外名校的標準路徑。如果走，會有正規學歷加持，但失去「14 歲就在 internet 上跟全球工程師對話」的塑形時期。'
        - label: '出國念中學'
          plausibility: structural
          note: '同代部分天才兒童家庭選擇早期送出國（如 MIT 早期入學）。如果走，可能更早接觸世界一流計算機科學，但 g0v 那條公民科技線不會在台灣發生。'
    - id: silicon-valley
      year: 2000
      age: 19
      type: choice
      theme: tech-policy
      scene: '19 歲已在加州矽谷軟體公司擔任工程師'
      chose:
        label: '深耕程式語言理論（Perl/Haskell）+ 發起 Pugs 專案'
        consequence: '2005/2/1 啟動 Pugs（用 Haskell 實現 Perl 6）。2001-2006 在 CPAN 啟動超過 100 個 Perl 專案。「用一種語言實現另一種語言」訓練了她的 meta-thinking——後來看政府就像看一個需要重構的系統。'
      alternatives:
        - label: '加入 Google / 大型科技公司'
          plausibility: structural
          note: '2000 年代矽谷主流路徑。如果走，會有更高薪 + 股票，但失去 open source 社群浸淫時間。後來 g0v 的「不是員工是社群」DNA 不會出現。'
        - label: '創業'
          plausibility: structural
          note: '同代矽谷工程師很多選擇創業（YC 第一批 2005）。如果走，可能成為連續創業者，但「為公共利益寫 code」的傾向會被「為股東寫 code」覆蓋。'
    - id: gender-transition
      year: 2005
      age: 24
      type: choice
      theme: identity
      scene: '人生最重要的決定之一'
      chose:
        label: '服用雌激素 + 公開出櫃 + 改名「唐鳳」'
        consequence: '2005 年底在 blog.elixus.org 部落格自行宣告。「不管現在、過去或未來，我很樂意大家用女性的名詞來稱呼我」。父親回應「沒有理由不接受」。為台灣 LGBTQ+ 權益做出重要貢獻，但她本人後來反覆拒絕「跨性別代言人」位置，自稱「後類別」。'
      alternatives:
        - label: '私下轉換不公開'
          plausibility: structural
          note: '部分跨性別者選擇低調 transition，避免社會壓力。如果走這條，職涯可能更平順，但「全球首位公開跨性別部長」的歷史地位不存在。'
        - label: '不 transition'
          plausibility: speculative
          note: '[推測] 同代部分跨性別者因社會壓力選擇延後或放棄。如果走，內在張力可能影響後續創造力與公開能見度。'
    - id: g0v-2012
      year: 2012
      age: 31
      type: choice
      theme: tools
      scene: '在矽谷已是有聲譽的開源工程師'
      chose:
        label: '與高嘉良、吳泰輝、瞿筱葳等共創 g0v 零時政府'
        consequence: "台灣最重要的公民科技社群。起點是 2012/10 對「經濟動能推升方案」廣告的不滿 + 中央政府總預算視覺化。「hack don't attack」——不攻擊既有制度，用技術改善它。萌典、IVOD、口罩地圖等模式後來被全球複製。"
      alternatives:
        - label: '繼續在矽谷做純技術'
          plausibility: structural
          note: '當時矽谷對她已開放各種 senior 機會。如果留下，會是「另一個成功的台裔工程師」，不會有後來的政策影響力。'
        - label: '回台灣加入既有政黨/智庫'
          plausibility: structural
          note: '走傳統政治參與路徑。如果走，會被政黨機器收編，「無黨籍政務委員」的可能性消失。'
    - id: sunflower
      year: 2014
      age: 33
      type: choice
      theme: tech-policy
      scene: '2014/3/18 太陽花學運佔領立法院'
      chose:
        label: '一手架設場內所有線路、鏡頭、網路直播設備，但本人只待議場 1 小時即離開'
        consequence: '她認為「議場內部 5 個不同角度攝影機錄影和直接播出的情況下，所有活動已經成為純粹的展示演出和儀式」。對佔領、表態都「不感興趣」。同時自掏腰包請人做政府會議逐字稿。'
      alternatives:
        - label: '完全參與佔領 / 公開表態反政府'
          plausibility: structural
          note: '同代部分技術人選擇成為運動代言人。如果走，可能成為政治明星，但失去 2016 以「無黨籍 outsider」入閣的可能性。'
    - id: vtaiwan
      year: 2014
      age: 33
      type: choice
      theme: tech-policy
      scene: '2014/4 蔡玉玲以政務委員身份進到 g0v 黑客松，後續發展為 vTaiwan 平台'
      chose:
        label: '與政府合作 vTaiwan + Pol.is 共識引擎'
        consequence: '2015-2018 處理 26 議題，80% 引起實質政府行動。Uber 法規討論成最知名案例。國際公認的數位民主典範。'
      alternatives:
        - label: '拒絕與政府合作'
          plausibility: structural
          note: '部分公民科技人堅持與政府保持距離（如 EFF 路線）。如果如此，g0v 純民間倡議路徑，不會被「招安」進體制，但也少了實際政策落地能力。'
    - id: digital-minister
      year: 2016
      age: 35
      type: choice
      theme: tech-policy
      scene: '2016/8/9 第一次見林全、8/15 同意接任、10/1 上任'
      chose:
        label: '入閣擔任「數位政委」，談妥三條件：每週三、五遠距上班 / 會議全公開逐字稿 / 不必每天進院'
        consequence: '台灣史上最年輕政務委員 + 全球第一個公開跨性別身份的部長級政治人物 + 台灣第一位「數位政委」。'
      alternatives:
        - label: '婉拒入閣'
          plausibility: structural
          note: '同類型的 outsider 技術人有人婉拒（怕被體制吸納）。如果婉拒，數位轉型工作會缺一個關鍵連結點，後來疫情口罩地圖等可能晚數月或不發生。'
    - id: covid-mask-map
      year: 2020
      age: 39
      type: choice
      theme: tools
      scene: '2020/1/31 - 2/6 期間，吳展瑋凌晨用 Google Maps API 做的超商口罩地圖一夜燒掉 2 萬美元 API 費用'
      chose:
        label: '協調健保署 open data 釋出 + 邀集 g0v 社群共同開發藥局口罩採購地圖'
        consequence: '2/6 健保署 open data 上線同日，藥局口罩採購地圖正式上線。24 小時內 100 萬人次使用。2/15 HackMD 上有 101 個相關應用、g0v 社群建構 140+ 工具。江明宗 verbatim：「唐鳳有決定權，還能自己改 code，所以我們都不用北上向哪個長官報告」。'
      alternatives:
        - label: '只做政策不下海寫工具'
          plausibility: structural
          note: '部會首長正常路徑：開會、定政策、讓承包商做。如果如此，口罩地圖可能變成 6 週才上線的官方 app（多國的 reality）。她下海推 g0v 社群跑兩天上線是關鍵。'
    - id: moda-minister
      year: 2022
      month: 8
      age: 41
      type: choice
      theme: tech-policy
      scene: '2022/8/27 數位發展部正式揭牌'
      chose:
        label: '擔任首任部長至 2024/5/20'
        consequence: '從跨部會協調的政務委員變成有固定預算與編制的正式部長。整合電信、資安、數位經濟。首年預算員額 598 人、公務預算 57 億 + 前瞻 160 億。任期 1 年 9 個月。'
      alternatives:
        - label: '繼續當政務委員不擔任部長'
          plausibility: structural
          note: '保留「跨部會自由」的彈性，避免成為被質詢的固定靶。但失去「正式部會 + 預算 + 編制」的執行力。'
        - label: '回民間繼續做 g0v'
          plausibility: structural
          note: '另一條路：以 NGO 身份持續影響政策。如果走，數位發展部首任部長會是別人，很可能用更傳統官僚方式管理。'
    - id: stockholm
      year: 2025
      month: 12
      age: 44
      type: choice
      theme: tools
      scene: '2025/12/2 斯德哥爾摩 Right Livelihood Award 頒獎台'
      chose:
        label: '接受「另一個諾貝爾獎」，台上演說將焦點推回集體'
        consequence: "首位獲此獎台灣人。Citation：「For advancing the social use of digital technology to empower citizens, renew democracy and heal divides」。接受演說 verbatim：「Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation」+ 個人哲學重述「The superintelligence we are looking for is already here. It's us」。"
      alternatives:
        - label: '在頒獎台上講「我的成就」'
          plausibility: structural
          note: '同代得獎者常以個人故事為敘事中心。如果走，獎座變成個人勳章，但她選擇把舞台 reframe 成「我們」——她拒絕當天才這條主線的最後一個變奏。'
curation: incubating
translatedFrom: 'People/唐鳳.md'
sourceCommitSha: '29ff6f481'
sourceContentHash: 'sha256:97c9b6fe6c788bcc'
sourceBodyHash: 'sha256:223451ab2ee89544'
translatedAt: '2026-08-28T18:30:00+08:00'
---

# Audrey Tang: Every Famous Decision She Made Was a Refusal of the “Genius” Label

> **30-Second Overview:** Kicked unconscious by classmates and pulled out of school at eight, refusing a guaranteed place at Taipei Municipal Jianguo High School at fourteen, coming out as transgender at twenty-four while refusing to become its spokesperson, and making “no office” the first condition of joining the cabinet at thirty-five. In 2020, in the middle of the night, she was patching code with Finjon Kiang in the g0v Slack to build the mask map; on December 2, 2025, she accepted the Right Livelihood Award in Stockholm, where the hall had come for her personal story — and the word she stressed on stage was “we.” The world treats her as a genius; every famous decision she has made was a refusal of that position.

## A Mask Map That Burned Twenty Thousand US Dollars

In late January 2020, COVID-19 was beginning to spread in Taiwan. Mask supplies at pharmacies were running short, and the government announced that mask purchases would move to a name-based rationing system starting February 6. In Tainan, an engineer at Goodideas Studio, Wu Chan-wei (Howard), sat down alone in the small hours of February 2 and wired the Google Maps API into a map that could show the mask stock of nearby convenience stores. He deployed it before dawn and shared it with the community.[^1]

When he returned to his computer after lunch, the Google API billing dashboard had already run up US$20,000 — burned through within twenty-four hours by the users flooding in.

That same day, Audrey Tang appeared in the g0v Slack channel. She had not come to give orders. She coordinated with Google’s engineering team to hold down the bill, and at the same time she pulled in several old g0v friends — Finjon Kiang (kiang, former executive secretary of the Tainan Smart City Office) and the NHI Administration’s information team (Chang Ling-chih and Chen Tzu-yu among them) — to work on one question: how to sync the mask stock of Taiwan’s 6,000-plus pharmacies, every thirty seconds, onto a map that anyone could open.[^2]

At 8 a.m. on February 6, the moment the NHI Administration’s open data was officially released, the pharmacy mask procurement map went live. Within twenty-four hours it had more than a million users. By February 15, 101 related applications had piled up on HackMD, and the g0v community had turned out more than 140 tools.[^2] [^3]

Finjon Kiang later left this passage in the transcript of one of his own talks:

> ✦ “The minister is supremely fluent in information architecture; she understood every requirement we raised. Most important of all, Audrey Tang had the authority to decide, and she could write code herself — so none of us ever had to travel north and brief some official.”[^4]

The protagonist of this story was never Audrey Tang alone. It was Finjon Kiang, it was Wu Chan-wei, it was the civil servants of the NHI Administration’s information team, it was the hundreds of engineers of the g0v community, and it was one whole night of people taking turns writing code around Tang’s office.

But after 2020, every version written by foreign media had a single protagonist: her. The BBC wrote that “Audrey Tang saved Taiwan with code.” Wired wrote “The Hacker Who Became Taiwan’s Digital Minister.” TIME put her on its list of the world’s leaders in the fight against the pandemic.

In every interview she pushed the credit back out. But the narrative of the “genius minister who saved Taiwan” has clung to her for over forty years, and it does not come off that easily.

## Kicked Unconscious at Eight, Turning Down Jianguo High School at Fourteen

Audrey Tang was born in Taipei on April 18, 1981, under the name Tang Tsung-han. Her father, Tang Kuang-hua, was a former deputy editor-in-chief of the _China Times_; her mother, Li Ya-ching, was deputy director of the same paper’s reporting division.[^5]

She had congenital heart disease. The school administered IQ tests three times, and each one came back “at least 160” — the top grade the instrument could record. The year she turned eight, her family did not yet own a computer; she read a book on Applesoft BASIC programming, drew a keyboard and a screen on paper by hand, and wrote down what each button would do and what the computer might output in response.[^5]

But if “gifted child” is set to be the adjective that appears most often next to her name in 2026, that position did not exist on the eight-year-old of 1989. What filled that position was a beating, bruises, and the words “why don’t you die.”

Across her six years of elementary school she went through three kindergartens and six elementary schools. One day in her second year, the teacher handed out the test papers and left the room. Audrey Tang had finished early; several classmates who could not solve the test reached over to snatch her paper. She grabbed it and ran, fell, and one of them kicked her with full force; she hit the wall and lost consciousness.[^6] That classmate later said something that _Business Today_ preserved verbatim:

> ✦ “Why don’t you just die? If you die, then I’ll be the best.”[^6]

She said nothing about it at home. One day her mother saw the bruises across her stomach while bathing her, and decided on the spot to take her out of school.[^6]

Her mother, Li Ya-ching, later went to Germany to study alternative education, and in 1994 founded the Seedling Parent-Child Experimental Elementary School in Wulai, serving as its first principal.[^7] In 1995, fourteen-year-old Audrey Tang, after a retreat in the mountains of Wulai, announced to her parents: she was done with formal schooling, and she was giving up the guaranteed place at Jianguo High School.[^8]

That was not a choice of “I am too gifted to need school.” It was a child who had learned, from the age of eight, to hide herself making a decision at fourteen: being boxed into the position of “gifted student” was the version of life she did not want.

She has said it many times since: “I don’t think the modern world still has a category called genius. In the internet era, everyone is IQ 180.”[^9]

## At Twenty-Four She Changed Her Name but Refused to Be a Transgender Spokesperson

At twelve she began learning Perl.[^10] At nineteen — in 2000 — she was already working as a software engineer in California’s Silicon Valley.[^11]

On February 1, 2005, at twenty-four, she started the Pugs project — a compiler and interpreter implementing Perl 6, written in Haskell.[^12] Within the Perl community, Pugs was a bootstrap undertaking: one language realizing itself through another language. Between 2001 and 2006 she started more than 100 Perl projects on CPAN.[^13] The international open source community knew her as Audrey, or au.

At the end of 2005, she announced on her own blog, blog.elixus.org, that she was a transgender person.[^14] She began taking estrogen but did not have surgery. She changed her Chinese name to 「唐鳳」, and her English name from Autrijus to Audrey.

In that blog post she wrote:

> ✦ “No matter whether it is now, the past, or the future, I am happy for people to address me with feminine words.”[^14]

Her father, Tang Kuang-hua, was asked for his response in an interview, and the answer was later carried verbatim by several media outlets:

> ✦ “If she feels that this change of gender can make her happier and let her creativity flow more freely, and it hurts no one, there is no reason not to accept it.”[^15]

She refused the position of “transgender spokesperson.” In 2020, on the personnel form for the Executive Yuan cabinet, she wrote “none” in the gender field. Her explanation to reporters at the time:[^16]

> ✦ “I am ‘post-category.’ I don’t take a side in the argument over gender. It is not that I think the issue is unimportant; it is that I don’t think arguing solves anything.”[^16]

In her interview with Marie Claire, she left behind another line that has been quoted again and again:

> ✦ “If you can make peace with confusion, you gradually begin to see that it is neither your problem nor society’s problem, but the gap in between. Everything has a gap, and the gap is where the light gets in.”[^17]

From 2010 to 2016 she concurrently advised Apple, took part in the development of Siri, and was said to be paid at an hourly rate equivalent to one bitcoin.[^18] At thirty-three — in 2014 — she finished handing over her work at Socialtext and Apple and declared herself “retired.”[^11]

## g0v and the Sunflower Chamber: Sharing the Credit with the Invisible

In October 2012, together with Chia-liang Kao (clkao), Kirby Wu (吳泰輝), and ipa (瞿筱葳), she co-founded g0v, the “gov zero” civic hacking community. The starting point was frustration with the Executive Yuan’s “Economic Power-Up” advertising campaign — a NT$33 million government promotional video that left viewers unable to say what the government actually intended to do.[^19]

g0v’s first project was a visualization of the central government budget: spreading the dense budget volumes into page after page of clickable charts.[^19] Later came MoeDict (萌典), the Legislative Yuan’s IVOD video archive, and the live streams from the Sunflower Movement’s occupied chamber.

Late in the night of March 18, 2014, students seized the Legislative Yuan chamber. All the cabling, cameras, and livestreaming equipment inside were set up by Audrey Tang herself.[^20]

But she stayed in the chamber for only an hour before leaving. Interviewed later by PTS’s PNN news program, she said:

> ✦ “With five cameras filming and broadcasting the chamber from different angles, everything happening inside has already become pure spectacle and ritual.”[^20]

She was “not interested” in the occupation, or in declaring a side. What she cared about was tooling. At the same time, she paid out of her own pocket to have people transcribe government meetings — so that people who were not in the room could still read the full conversation.[^20]

After the Sunflower Movement ended, in April 2014, Tsai Yu-ling, then a minister without portfolio, walked into a g0v hackathon. From that moment, “government” and “g0v” — two words that had faced each other as opponents — began to grow a strip of middle ground between them.[^21]

That middle ground was called vTaiwan. Between 2015 and 2018, the platform took up 26 issues, and 80 percent of them led to substantive government action.[^22] Its best-known case was the Uber consultation: taxi operators and Uber supporters were deadlocked for six years, and Uber was ultimately legalized under seven conditions.[^22]

At the platform’s core was the Pol.is consensus engine — large volumes of opinion machine-sorted into clusters, letting every participant see “who I think like, who I think nothing like, and which claims everyone agrees on.” It held no votes and took no sides; it only drew the shape of the disagreement.

## No Office, Fully Public Transcripts, Remote Work Two Days a Week

On August 9, 2016, thirty-five-year-old Audrey Tang met Premier Lin Chuan for the first time. On August 15 she agreed to join the cabinet as a minister without portfolio. At the end of September she flew back to Taiwan from Silicon Valley, and on October 1 she walked into the Executive Yuan.[^23]

The three conditions she had negotiated in advance became the first breach in Taiwan’s civil-service system: remote work on Wednesdays and Fridays; verbatim transcripts published for all meetings; and no requirement to enter the building every day.[^23]

Lin Chuan explained to reporters at the time:

> ✦ “The Executive Yuan currently has no rules on remote work, but her working pattern has long been remote. I think that as long as the work is not affected, passing along ideas or policy directions through a computer from a distance is workable.”[^24]

She became three things at once: the youngest minister without portfolio in Taiwan’s history, the world’s first openly transgender minister-level politician, and Taiwan’s first “digital minister.”[^25]

She had no fixed office in the Executive Yuan. She said the whole compound was her office. After every meeting, the transcript went up on sayit.pdis.nat.gov.tw, searchable by anyone.[^26]

She assembled a twenty-person team called PDIS (Public Digital Innovation Space): half practitioners from civil society, half volunteers drawn from the ministries, with thirty more interns added over the summer.[^26] It was not a bureaucracy — it was a workspace.

In 2019, _Foreign Policy_ named her to its list of the world’s Top 100 Global Thinkers (readers’ choice category).[^27] The media called her “the world’s only openly transgender minister” and a “coding star.” In every interview she pushed the credit back out — but the story of the “genius minister” travels more easily than anything she actually says.

![Audrey Tang speaking at the re:publica conference in Berlin, May 2019](/article-images/people/audrey-tang-re-publica-2019.webp)
_Audrey Tang on stage with Julia Kloiber in the “Digital Social Innovation” conversation at the re:publica conference in Berlin, May 8, 2019. Photo: Jan Michalko. [CC BY-SA 2.0 via Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>).\_

## Conservative Anarchism: Refusing to Command, Refusing to Be Commanded

Audrey Tang calls herself a “conservative anarchist.” On its face, a contradiction in terms.

“Conservative” means keeping the things in existing institutions that already work; “anarchist” means opposing the concentration of power and rejecting top-down coercion. People who weld the two words together usually mean this: I believe some things inside existing institutions are worth keeping, but I do not believe anyone is entitled to force other people to accept them in the name of authority.

Her interview with _Rest of World_ left behind a line that reads almost like a declaration:

> ✦ “Any top-down, coercion, whether it’s from the capitalists or from the state, is equally bad.”[^28]

In her conversation with the economist Tyler Cowen, asked “what is your role,” she said:

> ✦ “I’m working _with_ the government; I’m not working _for_ the government.”[^29]

At the Q&A of ICFP 2020, the International Conference on Functional Programming, she also dropped this:

> ✦ “In Taiwan we have this strange idea that broadband internet access is a human right. Everyone has broadband. And if you don’t, it’s my fault, personally.”[^30]

She used the word “human right” heavily, and “my fault, personally” lightly. The attitude she wanted to bring to a government job could be put as: if something is missing somewhere, I will go fill it.

One item in her working philosophy is called humor over rumor. Once the CoFacts system detected viral disinformation, her team would put out, within two hours, a two-minute video or a two-panel graphic (under 200 characters), answering the fake news with humor. In shorthand, the 2-2-2 rule.[^31]

The “toilet paper panic” of February 2020 is the case most cited by international media in that period: a rumor spread that masks and toilet paper were made from the same pulp, and people panic-bought; within hours the Executive Yuan pushed out a meme card — the shoulder-pat image of then-Premier Su Tseng-chang captioned with the Hokkien line 「咱只有一粒卡臣」 — together with an explainer that the two products drew on different supply chains, and the rumor cooled off the same day.[^31] In her TED talk and repeated international interviews she holds this up as the showcase case of humor over rumor: the rumor was not suppressed by law; it was crowded out by an image that was funnier than the rumor and slipped the facts in at the same time.

On August 27, 2022, the Ministry of Digital Affairs was formally inaugurated, and she took office as its first minister.[^32] The first-year staffing plan was 598 people, with a regular budget of NT$5.7 billion plus NT$16 billion from the Forward-looking Infrastructure program — NT$21.7 billion in all.[^33]

In office she pushed through digital resilience (persuading the UK’s OneWeb and Luxembourg’s SES to deploy low- and medium-orbit satellite terminals in Taiwan), amended the Electronic Signatures Act — a law that had gone twenty years untouched — launched the 111 government-exclusive short-code SMS platform against fraud, and required 47 Grade-A agencies to adopt the unified T-Road transmission standard within two years.[^34] [^35]

But she also took plenty of direct criticism. Ko Wen-je of the Taiwan People’s Party asked: “NT$30 million per head on average — what kind of job is this?” DPP legislator Liu Shih-fang said the ministry “still hasn’t found its own direction.” KMT legislator Wu Yi-ting said that on the online fraud the public cares about most, “there has been no substantive action.”[^36] [^37]

Even the POs (public participation officers) that PDIS planted inside the ministries were confused. The Reporter interviewed one PO, verbatim:

> ✦ “I’ve been a PO for two months now, and it feels like one more job on top of everything else. I still can’t tell how far we’re actually allowed to step in, or how much authorization we actually have... I don’t know, with these platforms, what our role is going to be in the future.”[^38]

She could not answer that question. Or rather, her answer was: that is yours to decide.

The price of “demonstrating rather than commanding” is slowness, unflattering KPIs, and two years gone without anyone able to say clearly what the Ministry of Digital Affairs has actually done. The bet she placed was on cultural change, and cultural change either lands or it does not.

But PDIS’s SayIt public transcript system had accumulated full-text records of more than 7,000 meetings by the day she left office.[^26] Anyone typing the keywords “Uber,” “masks,” or “LINE Pay” can read every word she said at the time to industry, to civil servants, and to legislators. The system did not exist before she entered government, and no one removed it after she left. She could never compress it into a single talking point, but she did leave behind seven years of searchable government conversation — a first in Taiwan’s political history.

## On the Stockholm Stage, She Said “We”

On the evening of May 20, 2024, as President Lai Ching-te’s inauguration ceremony ended, Audrey Tang headed straight for Taoyuan Airport. Over the following three months she set foot in twenty countries.[^39]

That April, together with the economist Glen Weyl and the Plurality community scattered across the world, she had published _Plurality: The Future of Collaborative Technology and Democracy_. The book was released under CC0 — meaning anyone may take the full text and do anything with it: no attribution required, no payment, no permission to ask.[^40]

For the title concept they took a single character-like symbol: ⿻ (related to the Chinese 「衆」, roughly pronounced zhòng). In Unicode it is one of the Ideographic Description Characters, used to describe the structure of “two things interwoven.” Explaining it to international media, she said ⿻ emphasizes interweaving — the differences of many individuals are not erased, but form the texture of a single whole. The concept is the exact opposite of “genius”: a genius is one bright point set off against the gray around it; ⿻ is every thread wound around every other thread, none of them dispensable.

The vTaiwan Uber case is the example she reaches for most often to explain ⿻: taxi operators and Uber supporters deadlocked for six years, and Uber was finally legalized under seven added conditions.[^22] No side entirely “won” that consensus, and no side entirely “lost.” She said that is what democracy actually looks like — the work of weaving everyone’s texture into the same cloth.

On October 7, the Ministry of Foreign Affairs appointed her Taiwan’s Cyber Ambassador-at-Large (無任所大使).[^41] On her personal site, audreyt.org, and on cyberambassador.tw, the same opening line sits unchanged:

> ✦ “I want to be a good enough ancestor for future generations.”[^42]

On December 2, 2025, in Stockholm, in the award hall of the Right Livelihood Foundation. The Right Livelihood Award is known as the “Alternative Nobel Prize,” founded in 1980 by the Swedish-German philanthropist Jakob von Uexküll to cover the ground the Nobel Prizes leave untouched.

Tang was the first person from Taiwan to receive the award.[^43] The citation reads:

> ✦ “For advancing the social use of digital technology to empower citizens, renew democracy and heal divides.”[^43]

The first thing she said in her acceptance speech was not about what she had done. It was about what cyberspace is:

> ✦ “Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation. It is time we work on peace in this zone.”[^43]

Then she returned to the line from the front matter of _Plurality_:

> ✦ “The superintelligence we are looking for is already here. It’s us.”[^44]

She accepted the trophy known as “the Alternative Nobel,” and then, standing on the award stage, turned the spotlight toward “we” — the woman the world insists on treating as Taiwan’s genius had once again refused the position of “genius.”

From the eight-year-old kicked across a gifted classroom in 1989 to the forty-four-year-old on the Stockholm stage in 2025, the road between is long, and it is paved with refusals, one after another. Each refusal, taken alone, looks like rebellion; laid side by side, they turn out to be variations on a single gesture: refusing to be defined by the position of “outstanding individual,” and putting herself back in the role of node, bridge, and builder of spaces.

She refuses to be a genius. The world insists on making her one. But she has never let the world win the argument — it has only taken the world a very long time to hear what she is actually saying.

![Audrey Tang’s personal signature, released as an SVG in 2021](/article-images/people/audrey-tang-signature.svg)
_Audrey Tang’s personal signature, released publicly in August 2021, originally provided for Japan’s \_Bungeishunju_. Author: Audrey Tang herself. [CC0 public domain](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>).\_

---

## Further Reading

- [Sodagreen: From a Small Gongliao Stage to the “Fish-Berry” Fight, a Twenty-Year War to Reclaim Musical Sovereignty](/en/music/sodagreen) — Another Taiwanese outlier that rose in the 2000s, another long campaign of “refusing to be boxed in by an assigned identity”; only the arena was the music industry rather than the government
- [Tony Hsiao (蕭上農)](/en/people/tony-hsiao-inside-founder) — Co-founder of INSIDE and iCook, who likewise defines his place in Taiwan’s tech scene by “crossing many fields”
- [Tai-yu Wu (吳大猷)](/en/people/tai-yu-wu) — The transmission of Taiwan’s intellectual elite from science to technology; as president of Academia Sinica, Wu laid the foundations of Taiwan’s research establishment
- [Open Culture Foundation](/en/technology/open-culture-foundation) — The foundation that grew out of g0v’s back office into a bridge for Taiwan’s digital rights; it has crossed paths with the Ministry of Digital Affairs under Audrey Tang time and again, in cooperation and in watchfulness
- Taiwan’s COVID-19 Pandemic and Vaccines (台灣新冠疫情與疫苗) — The epidemic within which the mask map’s chain of coordination grew, and the eighteen months Taiwan bought with its borders and its masks

---

## Image Sources

This article uses 3 images, all cached in `public/article-images/people/` to avoid hotlinking the origin servers. All three are Wikimedia Commons CC / CC0 licensed:

- **hero**: [Portrait Audrey Tang (cropped)](<https://commons.wikimedia.org/wiki/File:Portrait_Audrey_Tang_(25915794061,_cropped).jpg>) — Photo: Camille McOuat, 2016-03-09 Paris, CC BY 2.0
- **scene-mid**: [Re:publica 19 - Day 3](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>) — Photo: Jan Michalko, 2019-05-08, the “Digital Social Innovation” conversation at re:publica in Berlin, CC BY-SA 2.0
- **signature**: [Audrey Tang signature](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>) — Author: Audrey Tang herself, 2021-08-18, CC0 public domain

---

[^1]: [TechNews: Building the mask map by hand — the team behind “saving the nation by keyboard” (2020-02-23)](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Details how Howard Wu deployed in the small hours and ran up a US$20,000 API bill, plus the timeline of Audrey Tang coordinating Google and g0v

[^2]: [Finjon Kiang, Medium: The pharmacy mask procurement map is live (2020-02)](https://medium.com/%E6%B1%9F%E6%98%8E%E5%AE%97-kiang/%E8%97%A5%E5%B1%80%E5%8F%A3%E7%BD%A9%E6%8E%A1%E8%B3%BC%E5%9C%B0%E5%9C%96%E4%B8%8A%E7%B7%9A-54e11bd63e84) — A first-person account by the engineer himself, with the verbatim line “the official data is expected to go live at 8 a.m. on 2/6,” plus Audrey Tang coordinating community participation in development

[^3]: [Ministry of Health and Welfare, COVID-19 key decisions website](https://covid19.mohw.gov.tw/ch/cp-4822-53563-205.html) — The government’s official account, verbatim: “Audrey Tang, minister without portfolio of the Executive Yuan, convened civil communities to build the ‘mask map’ application platform from NHI Administration open data”

[^4]: [TechNews: Building the mask map by hand (same as [^1])](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — See the original link for supplementary detail

[^5]: [Chinese Wikipedia, entry “唐鳳 (Audrey Tang)”](https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3) — Birth, family background, the childhood self-study with a paper keyboard, and other basic biographical material

[^6]: [Business Today: Bullied unconscious by classmates... the child genius Audrey Tang thought of suicide many times (2020-11)](https://www.businesstoday.com.tw/article/category/183035/post/202011090020/) — The second-grade classroom beating scene, the classmate’s verbatim “why don’t you die,” and the mother’s discovery of the bruises while bathing her that led to the decision to withdraw her from school

[^7]: [China Times: Audrey Tang becomes youngest minister without portfolio; Li Ya-ching a model of self-study education reform (2016-08-25)](https://www.chinatimes.com/realtimenews/20160825005980-260405) — Li Ya-ching’s return to Taiwan in 1992 and her founding of the Seedling Parent-Child Experimental Elementary School in Wulai in 1994, serving as its first principal

[^8]: [Taipei Sounds: Escaping “school bullying” into self-study — Audrey Tang’s “major discovery” at fourteen](https://www.taisounds.com/specialtopic/content/46/23226) — After retreating to the Wulai mountains at fourteen, she refused the guaranteed admission to Jianguo High School

[^9]: Cited across multiple media outlets, restated by Audrey Tang herself in different interviews: “I don’t think the modern world still has a category called genius” and “In the internet era, everyone is IQ 180”

[^10]: [Wikipedia: Audrey Tang](https://en.wikipedia.org/wiki/Audrey_Tang) — “Tang started programming at the age of eight and began learning Perl at the age of 12”

[^11]: Chinese Wikipedia, entry “唐鳳” (same as [^5]) — By 2000, at nineteen, already working as an engineer in Silicon Valley; in 2014, at thirty-three, handing over her Socialtext and Apple work to announce her “retirement”

[^12]: [Wikipedia: Pugs (compiler)](<https://en.wikipedia.org/wiki/Pugs_(compiler)>) — Wikipedia entry

[^13]: [Wikipedia: Audrey Tang (English)](https://en.wikipedia.org/wiki/Audrey_Tang) — “Tang initiated over 100 Perl projects between June 2001 and July 2006, including the popular PAR archiver”

[^14]: Chinese Wikipedia, entry “唐鳳” (same as [^5]) + consistent verbatim quotes across media: “No matter whether it is now, the past or the future, I am happy for people to address me with feminine words.” Original source: the 2005 blog blog.elixus.org

[^15]: [Business Today: Interview with Audrey Tang’s father (2016-09)](https://www.businesstoday.com.tw/article/category/80407/post/201609010032/) — Her father Tang Kuang-hua, verbatim: “There is no reason not to accept it”

[^16]: [Taiwan Women, NMTH: Taiwan’s first transgender cabinet member and first digital minister — Audrey Tang](https://women.nmth.gov.tw/?p=20105) — Tang’s verbatim “I am ‘post-gender,’” and the background of writing “none” in the gender field of the 2020 cabinet personnel form

[^17]: [Marie Claire Taiwan: Through childhood bullying, Audrey Tang says: “Make good company of your confusion”](https://www.marieclaire.com.tw/entertainment/story/52923/audrey-tang) — Verbatim: “Everything has a gap, and the gap is where the light gets in”

[^18]: Chinese Wikipedia, entry “唐鳳” (same as [^5]) + [Encyclopaedia Britannica: Audrey Tang](https://www.britannica.com/biography/Audrey-Tang) — See the original links for supplementary detail

[^19]: [Taiwan Panorama: The civic hacker power of g0v, “government zero”](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — The October 2012 starting point, the central government budget visualization, and the co-founder list

[^20]: [PTS News PNN: Report on the Sunflower Student Movement (2014)](https://news.pts.org.tw/article/327548) — Verbatim: “Every cable, camera, and livestreaming device inside the chamber was set up single-handedly by the civic hacker ‘Audrey Tang,’” plus Tang’s comment that the chamber had become “pure spectacle and ritual,” and her paying out of pocket for the meeting transcripts

[^21]: [The Reporter: Creating a space for dialogue — the fantastic voyage of Audrey Tang](https://www.twreporter.org/a/g0v-audrey-tang) — The verbatim account of Tsai Yu-ling entering a g0v hackathon in April 2014, and the origin of vTaiwan

[^22]: [Democracy Technologies: Consensus Building in Taiwan](https://democracy-technologies.org/participation/consensus-building-in-taiwan/) — vTaiwan 2015-2018: 26 issues handled / 80% led to substantive government action / Uber legalized under seven conditions

[^23]: [Liberty Times: Breaking with tradition — Audrey Tang works remotely on Wednesdays and Fridays (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859132) — First meeting with Lin Chuan on 8/9 / agreement on 8/15 / taking office on 10/1 / the three conditions for joining the cabinet

[^24]: [Liberty Times: Audrey Tang’s remote work — Lin Chuan: this is workable (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859246) — Lin Chuan, verbatim: “The Executive Yuan currently has no rules on remote work... this is workable”

[^25]: Chinese Wikipedia, entry “唐鳳” (same as [^5]) — At thirty-five, the youngest minister without portfolio in Taiwan’s history and the world’s first openly transgender minister-level politician

[^26]: [pdis.nat.gov.tw work logs and the SayIt public transcript system](https://sayit.pdis.nat.gov.tw/) — The 20-person PDIS structure: half civil-society professionals, half volunteers from the ministries, plus 30 interns

[^27]: [Taipei Times: Audrey Tang named in “Top 100 Global Thinkers” (2019-01-25)](https://www.taipeitimes.com/News/front/archives/2019/01/25/2003708586) — Selected for Foreign Policy’s global thinkers list (readers’ choice category)

[^28]: [Rest of World: Audrey Tang on her “conservative-anarchist” vision for Taiwan’s future (2020)](https://restofworld.org/2020/audrey-tang-the-conservative-anarchist/) — Verbatim: “Any top-down, coercion, whether it’s from the capitalists or from the state, is equally bad”

[^29]: [Conversations with Tyler Ep.106: Audrey Tang](https://conversationswithtyler.com/episodes/audrey-tang/) — Verbatim: “I’m working with the government; I’m not working for the government”

[^30]: [Lindsey on X: live quote from the ICFP 2020 Q&A](https://x.com/lindsey/status/1297886318114963456) — Verbatim: “In Taiwan we have this strange idea that broadband internet access is a human right”

[^31]: [SwissInfo: Freedom of expression: humour over rumour](https://www.swissinfo.ch/eng/politics/freedom-of-expression-humour-over-rumour-lessons-from-taiwan-in-digital-democracy/46592080) — See the original link for supplementary detail

[^32]: [Ministry of Digital Affairs official site: past ministers](https://moda.gov.tw/aboutus/ministers-since-2022/1527) — Verbatim tenure: “August 27, 2022 – May 20, 2024,” the term of Audrey Tang

[^33]: [Liberty Times: Audrey Tang to head the digital ministry — budget and headcount of 598](https://news.ltn.com.tw/news/politics/breakingnews/4021987) — Liberty Times report

[^34]: [Liberty Times (Economy): From genius IT minister to freelance lecturer — reviewing the three achievements and controversies of Tang’s tenure](https://ec.ltn.com.tw/article/breakingnews/4677986) — Digital resilience / OneWeb / SES satellites / the Electronic Signatures Act amendment / the 111 short-code SMS platform

[^35]: [INSIDE: The Ministry of Digital Affairs turns one — two achievements and three controversies of the Tang era](https://www.inside.com.tw/article/32615-Taiwan-moda-anniversary) — The T-Road unified transmission standard adopted by 47 Grade-A agencies, plus a staff member’s verbatim line: “Compared with previous agencies, Audrey Tang was far more willing to delegate power”

[^36]: [Global Views Monthly: One year in, criticism that the Ministry of Digital Affairs has no achievements](https://www.gvm.com.tw/article/105627) — Verbatim criticism from Liu Shih-fang / Wu Yi-ting

[^37]: [ETtoday: The digital ministry budgets NT$21.1 billion — Ko Wen-je: NT$30 million per person on average, “what kind of job is this?” (2022-08-30)](https://www.ettoday.net/news/20220830/2327863.htm) — Ko Wen-je’s verbatim question

[^38]: [The Reporter: Open government — how Audrey Tang got past the civil servants](https://www.twreporter.org/a/open-government-audrey-political-commissar-challenges) — A PO’s verbatim words: “I’ve been a PO for two months now... I still can’t tell how far we’re allowed to step in”

[^39]: [Liberty Times (Economy): From genius IT minister to freelance lecturer (same as [^34])](https://ec.ltn.com.tw/article/breakingnews/4677986) — Liberty Times report

[^40]: [Plurality Institute: Book Launch of Plurality](https://www.plurality.institute/blog-posts/book-launch-plurality-the-future-of-collaborative-technology-and-democracy-by-e-glen-weyl-audrey-tang-and-the-plurality-community) — Co-authored with Glen Weyl and the Plurality community / published April 16, 2024 / released under CC0

[^41]: Chinese Wikipedia, entry “唐鳳” (same as [^5]) + [cyberambassador.tw](https://cyberambassador.tw/) — See the original links for supplementary detail

[^42]: [audreyt.org](https://audreyt.org/) — See the original link for supplementary detail

[^43]: [Right Livelihood: Taiwan’s Audrey Tang honoured with Right Livelihood Award (2025)](https://rightlivelihood.org/news/taiwans-audrey-tang-honoured-with-right-livelihood-award-for-advancing-digital-democracy-and-social-trust/) — Citation verbatim + the verbatim passage of Tang’s acceptance speech beginning “Cyberspace is a conflict region” + [Focus Taiwan (CNA English) report](https://focustaiwan.tw/society/202512030022)

[^44]: cyberambassador.tw verbatim + a philosophical restatement from the _Plurality_ book jacket — “The superintelligence we are looking for is already here. It’s us”
