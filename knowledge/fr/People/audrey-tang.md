---
title: "Tang Ping : Chaque décision célèbre est un rejet de l'étiquette de « génie »"
description: "Aînée par ses camarades à l'âge de 8 ans, elle a refusé d'être admise sans examen au Jianzhong à 14 ans, s'est outée en tant que personne transgenre à 24 ans mais a refusé d'être une ambassadrice, et la première condition pour son entrée au conseil à 35 ans était « pas de bureau ». Le 2 décembre 2025, elle a reçu le Prix Right Livelihood à Stockholm, parlant non pas d'elle-même, mais de « nous »."
date: 2026-05-16
category: 'People'
tags:
  [
    'personnage',
    'Tang Ping',
    'ministère du développement numérique',
    'g0v',
    'transgenre',
    'programmation',
    'gouvernement ouvert',
    'vTaiwan',
    'Plurality',
    'Prix Right Livelihood',
  ]
subcategory: '教育與社會'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-05-16
lastHumanReview: true
readingTime: 14
image: '/article-images/people/audrey-tang-portrait-2016.webp'
imageAlt: 'Portrait de Tang Ping pris en mars 2016 à Paris, vêtue de sombre avec une lumière naturelle douce.'
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
translatedAt: '2026-09-22T05:46:32.362764+00:00'
---

# Tang Feng : Chaque décision célèbre est un rejet de l'étiquette « génie »

> **Aperçu en 30 secondes :**
> Battue inconsciente par des camarades à l'âge de 8 ans, elle a dû s'absenter ; à 14 ans, elle a refusé d'intégrer Jianzhong (une école prestigieuse) ; à 24 ans, elle est devenue transgenre et a refusé d'être une ambassadrice ; à 35 ans, la première condition qu'elle a posée pour rejoindre le gouvernement était « ne pas avoir de bureau ». En 2020, au milieu de la nuit, elle a codé avec Jiang Mingzong sur Slack g0v pour créer une carte des masques ; en décembre 2025, à Stockholm, elle a reçu le Prix Right Livelihood. Alors que tout le monde attendait son histoire personnelle, ce qu'elle a souligné sur scène fut le mot « nous ». Le monde la considère comme un génie ; chaque décision célèbre est une négation de cette position.

## Une carte de masques qui a coûté vingt mille dollars

Fin janvier 2020, la pandémie de COVID-19 commençait à se propager à Taïwan. L'approvisionnement en masques dans les pharmacies était tendu et le gouvernement avait annoncé un achat nominatif à partir du 6 février. Wu Zhanwei (Howard), ingénieur chez Tainan Haoxiang Studio, a créé une carte consultable des stocks de masques dans les supérettes environnantes avec l'API de Google Maps dès la nuit du 2 février. Il l'a déployée et partagée sur les réseaux sociaux au petit matin [^1].

À midi, après avoir mangé, il est revenu devant son ordinateur et a constaté que le compte en arrière-plan de l'API de Google avait atteint 20 000 dollars — une consommation engloutie en 24 heures.

Ce jour-là, Tang Feng est apparue sur le canal Slack de g0v. Elle n'était pas là pour donner des ordres. Elle a coordonné avec l'équipe d'ingénieurs de Google pour maîtriser la facture du moment ; elle s'est également associée à quelques amis de longue date de g0v — Jiang Mingzong (secrétaire adjoint du bureau de la ville intelligente de Tainan), Zhang Lingzhi et Chen Ziyu du groupe informatique de la NHI — pour réfléchir : comment synchroniser le stock de masques des plus de 6 000 pharmacies de tout Taïwan sur une carte accessible à tous, toutes les 30 secondes [^2] ?

À 8 heures du matin le 6 février, la carte d'achat de masques des pharmacies a été officiellement publiée par l'open data de la NHI. Plus d'un million d'utilisations ont été enregistrées en 24 heures. Au 15 février, HackMD comptait 101 applications connexes et la communauté g0v avait lancé plus de 140 outils [^2][^3].

Jiang Mingzong a mentionné ceci dans son discours post-événement :

> ✦ « La secrétaire est très compétente en matière d'architecture de l'information, elle comprend toutes nos demandes. Le plus important, c'est que Tang Feng a le pouvoir de décision et peut modifier le code elle-même, donc nous n'avons pas besoin de faire un rapport à un haut fonctionnaire à Taipei. » [^4]

Le personnage principal de cette histoire n'était pas seulement Tang Feng. C'étaient Jiang Mingzong, Wu Zhanwei, les fonctionnaires du groupe informatique de la NHI, les centaines d'ingénieurs de la communauté g0v, et toutes ces nuits où l'équipe de bureau de Tang Feng modifiait le code.

Mais après 2020, tous les médias étrangers ont fait d'elle le seul personnage principal. Le BBC a écrit « Audrey Tang sauve Taïwan avec du code », Wired a écrit « La hackeuse devenue ministre numérique de Taïwan », et TIME l'a classée parmi les « leaders mondiaux dans la lutte contre la pandémie ».

Elle renvoyait toujours le mérite lors de chaque entretien. Mais le récit selon lequel « la ministre géniale sauve Taïwan » était si ancré en elle depuis plus de quarante ans, qu'il n'était pas si facile à décoller.

## Aînée battue par des camarades à 8 ans, elle refuse Jianzhong à 14 ans

Tang Feng est née à Taipei le 18 avril 1981. Son nom de naissance était Tang Zonghan. Son père, Tang Guanghua, fut un rédacteur adjoint du _China Times_, et sa mère, Li Yaqing, était une vice-directrice de la section reportage du même journal [^5].

Elle souffrait d'une cardiopathie congénitale. L'école avait effectué trois tests de QI, tous indiquant « au moins 160 » (le niveau le plus élevé possible pour l'outil de test). À l'âge de huit ans, elle n'avait pas d'ordinateur chez elle ; elle avait lu un livre de programmation Applesoft BASIC et avait dessiné sur papier un clavier et un écran d'ordinateur, en écrivant les boutons et ce que l'ordinateur pourrait afficher [^5].

Mais le label de « enfant prodige » est peut-être l'adjectif qui sera le plus souvent associé à son nom en 2026 ; il n'était pas présent sur l'enfant de huit ans en 1989. À cette place, il y avait des coups, des ecchymoses et « pourquoi tu ne meurs pas ».

Au sixième année d'école primaire, elle a changé de trois jardins d'enfants et de six écoles primaires. Un jour au deuxième cycle du primaire, l'enseignante est sortie de la classe après avoir distribué les examens. Tang Feng avait fini tôt ; plusieurs camarades qui n'avaient pas réussi à écrire ont tendu la main pour lui arracher ses copies. Elle a couru avec les copies et est tombée ; un des camarades l'a frappée de plein fouet, et elle est tombée inconsciente contre le mur [^6]. Plus tard, ce camarade avait dit une phrase qui a été conservée mot pour mot par _Jin Zhoukan_ :

> ✦ « Pourquoi tu ne meurs pas ? Si tu étais morte, j'aurais été la meilleure. » [^6]

Elle n'en a rien dit en rentrant chez elle. Un jour, sa mère l'a vue avec des ecchymoses sur le ventre pendant qu'elle se baignait, et elle a décidé de lui accorder un congé scolaire [^6].

La mère, Li Yaqing, est ensuite allée étudier dans l'éducation alternative en Allemagne, où elle a fondé l'école expérimentale Seed Family à Wulai en 1994, en tant que première directrice [^7]. En 1995, Tang Feng, âgée de 14 ans, après s'être isolée au milieu des montagnes de Wulai, a annoncé à ses parents : elle ne poursuivrait pas les études et renoncerait à l'admission précoce à Jianzhong [^8].

Ce n'était pas un choix du type « je suis trop géniale pour avoir besoin d'école ». C'était la décision, prise à quatorze ans par une enfant qui avait appris à se cacher dès huit ans : ne pas vouloir de cette version où elle était encadrée en tant que « jeune surdouée ».

Elle a dit maintes fois : « Je ne pense pas qu'il existe encore le concept de génie dans le monde moderne. À l'ère d'Internet, tout le monde est en fait à un QI de 180. » [^9]

## À l'âge de 24 ans, elle a changé de nom mais a refusé d'être une ambassadrice transgenre

Elle a commencé à apprendre Perl à l'âge de 12 ans [^10]. À 19 ans (en 2000), elle était déjà ingénieure dans une entreprise de logiciels de la Silicon Valley en Californie [^11].

Le 1er février 2005, à 24 ans, elle a lancé le projet Pugs — un compilateur et interpréteur de Perl 6 implémenté en Haskell [^12]. Pugs est une entreprise de _bootstrap_ au sein de la communauté Perl : un langage qui se réalise avec un autre langage. Entre 2001 et 2006, elle a lancé plus de 100 projets Perl sur CPAN [^13]. La communauté open source internationale l'appelle Audrey ou au.

Fin 2005, elle s'est déclarée transgenre sur son blog blog.elixus.org [^14]. Elle prenait des œstrogènes mais n'avait pas subi d'opération. Elle a changé son nom chinois en « Tang Feng » et son nom anglais Autrijus en Audrey.

Dans cet article de blog, elle écrivait :

> ✦ « Que ce soit maintenant, dans le passé ou dans le futur, je suis heureuse que les gens m'appellent avec un nom féminin. » [^14]

La réponse de son père, Tang Guanghua, lors d'un entretien, a été citée verbatim par plusieurs médias :

> ✦ « Si elle pense que le changement de genre la rend plus heureuse et plus créative, sans nuire à qui que ce soit, il n'y a pas de raison de ne pas l'accepter. » [^15]

Elle a refusé le poste d'« ambassadrice transgenre ». En 2020, elle a indiqué « Aucun » dans la case genre du dossier du personnel ministériel. Elle a expliqué aux journalistes à l'époque :

> ✦ « Je suis 'post-catégorielle'. Je ne prends pas parti dans le débat sur le genre. Ce n'est pas parce que je pense que ce sujet n'est pas important, mais parce que je pense que le débat ne résout aucun problème. » [^16]

Dans une interview avec Marie Claire, elle a laissé une autre phrase qui a été souvent citée :

> ✦ « Si vous pouvez vivre avec l'incertitude, vous commencez à voir que ce n'est ni votre problème ni un problème social, mais le vide entre les deux. Tout a des vides, et le vide est l'entrée de la lumière. » [^17]

De 2010 à 2016, elle a été consultante pour Apple, participant au développement de Siri, avec un taux horaire réputé équivalent à 1 Bitcoin [^18]. À 33 ans (en 2014), elle a transmis ses travaux sur Socialtext et Apple, annonçant sa « retraite » [^11].

## g0v et le parlement des fleurs : attribuer le mérite aux invisibles

En octobre 2012, elle a cofondé la "g0v" (gouvernement zéro heure) avec clkao, Kirby, ipa, entre autres. Le point de départ était l'insatisfaction face à la publicité pour le « Plan de stimulation économique » du Conseil exécutif — une campagne publicitaire financée à hauteur de 33 millions, dont on ne comprenait pas ce que le gouvernement voulait faire [^19].

Le premier projet de g0v fut la visualisation budgétaire du gouvernement central : transformer les lourds documents budgétaires en des graphiques cliquables [^19]. Ensuite, il y a eu MoeDict (dictionnaire mignon), IVOD (cinéma parlementaire) et le streaming en direct des débats lors du mouvement étudiant des fleurs.

Tard dans la nuit du 18 mars 2014, les étudiants ont occupé le parlement. Tous les circuits, caméras et équipements de diffusion en ligne présents sur place avaient été installés par Tang Feng [^20].

Mais elle n'est restée au parlement qu'une heure avant de partir. Plus tard, lors d'un entretien avec PNN (Public Broadcasting Service), elle a déclaré :

> ✦ « Dans le cas où cinq caméras enregistreraient et diffuseraient en direct depuis différents angles à l'intérieur du parlement, toutes les activités deviennent une pure performance et un rituel. » [^20]

Elle n'était pas intéressée par l'occupation ni par la prise de position. Ce qui l'intéressait, c'était la technologie des outils. Elle a également payé quelqu'un pour transcrire les réunions gouvernementales — permettant à ceux qui n'étaient pas sur place de lire l'intégralité du dialogue [^20].

Après la fin du mouvement des fleurs, en avril 2014, Tsai Ing-wen, alors commissaire politique, a participé au hackathon de g0v. À partir de ce moment, les deux termes initialement opposés, « gouvernement » et « g0v », ont commencé à développer un terrain d'entente [^21].

Ce terrain d'entente s'appelle vTaiwan. De 2015 à 2018, la plateforme a traité 26 sujets, dont 80 % ont conduit à des actions gouvernementales concrètes [^22]. L'exemple le plus connu est le débat sur la réglementation d'Uber : après six ans de blocage entre les taxis et les partisans d'Uber, Uber a finalement été légalisé sous sept conditions [^22].

Le cœur de la plateforme est le moteur de consensus Pol.is — un grand nombre d'opinions est organisé en plusieurs clusters par des machines, permettant à chaque participant de voir « avec qui je pense de manière similaire, avec qui je pense différemment, et quels arguments sont acceptés par tous ». Il ne vote pas, il n'est pas conflictuel ; il dessine simplement la forme des divergences.

## Pas de bureau, transcriptions publiques complètes, trois jours de télétravail par semaine

Le 9 août 2016, à l'âge de 35 ans, Tang Feng a rencontré pour la première fois le Premier ministre Lin Quan. Le 15 août, elle a accepté le poste de commissaire politique. Fin septembre, elle est revenue à Taïwan depuis la Silicon Valley. Le 1er octobre, elle a rejoint le gouvernement [^23].

Les trois conditions qu'elle avait préalablement négociées sont devenues une brèche inédite dans le système bureaucratique taïwanais : du télétravail les mercredis et vendredis ; la publication des transcriptions complètes de toutes les réunions ; l'absence d'obligation de se présenter au bureau tous les jours [^23].

Lin Quan a expliqué aux journalistes à l'époque :

> ✦ « Le gouvernement n'a pas de réglementation sur le télétravail pour le moment, mais son mode de travail antérieur était toujours en télétravail. Je pense que c'est faisable si les idées ou les directives politiques sont transmises à distance par ordinateur sans affecter le travail » [^24].

Elle est devenue trois choses : la plus jeune commissaire politique de l'histoire de Taïwan, la première personnalité ministérielle au monde à avoir une identité transgenre publique, et la première « commissaire numérique » de Taïwan [^25].

Elle n'avait pas de bureau fixe au gouvernement. Elle disait que tout le complexe administratif était son espace de travail. Après les réunions, les transcriptions étaient publiées sur sayit.pdis.nat.gov.tw, et n'importe qui pouvait effectuer une recherche [^26].

Elle a formé un petit groupe de 20 personnes, appelé PDIS (Public Digital Innovation Space, Espace d'innovation numérique publique). La moitié était composée de professionnels du secteur privé, l'autre moitié de volontaires issus de divers ministères. Pendant les vacances d'été, 30 stagiaires ont été ajoutés [^26]. Ce n'était pas une structure hiérarchique — c'était un espace de travail.

En 2019, elle a été sélectionnée parmi les cent grands penseurs mondiaux par _Foreign Policy_ (catégorie vote des lecteurs) [^27]. Les médias la décrivaient comme « le seul ministre transgenre au monde » ou une « star du code ». Lors de chaque entretien, elle renvoyait le mérite — mais l'histoire de la « ministre géniale » était plus facile à raconter que ce qu'elle disait.

![Tang Feng lors de sa conférence à re:publica à Berlin en mai 2019](/article-images/people/audrey-tang-re-publica-2019.webp)
_Scène du dialogue « Digital Social Innovation » au re:publica à Berlin le 8 mai 2019, Tang Feng et Julia Kloiber sur scène. Photo : Jan Michalko. [CC BY-SA 2.0 via Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>).\_

## L'anarchisme conservateur : refuser d'ordonner, mais aussi refuser d'être ordonné

Tang Feng se décrit comme une « anarchiste conservatrice ». C'est un oxymore apparent.

Le terme « conservateur » signifie préserver les systèmes existants et fonctionnels ; « anarchiste » signifie s'opposer à la concentration du pouvoir et au contrôle descendant. Ceux qui combinent ces deux mots veulent dire : je crois qu'il y a de la valeur dans le système actuel, mais je ne crois que personne n'est habilité à forcer les autres à l'accepter par autorité.

Dans son entretien avec Rest of World, elle laisse une déclaration presque manifeste :

> ✦ « Any top-down, coercion, whether it's from the capitalists or from the state, is equally bad. » (Toute coercition descendante, que ce soit celle des capitalistes ou de l'État, est également mauvaise.)[^28]

Lors d'un entretien avec l'économiste Tyler Cowen, lorsqu'on lui a demandé « Quel est votre rôle ? », elle a répondu :

> ✦ « I'm working _with_ the government; I'm not working _for_ the government. » (Je travaille _avec_ le gouvernement ; je ne travaille pas _pour_ le gouvernement.)[^29]

Elle a également fait cette déclaration lors d'une session de questions-réponses à la Conférence internationale sur l'informatique (ICFP) en 2020 :

> ✦ « In Taiwan we have this strange idea that broadband internet access is a human right. Everyone has broadband. And if you don't, it's my fault, personally. » (À Taïwan, nous avons cette idée étrange que l'accès à Internet haut débit est un droit humain. Tout le monde devrait avoir du haut débit. Si ce n'est pas le cas, c'est ma faute, personnellement.)[^30]

Elle utilise le mot « droits humains » avec beaucoup de poids, mais elle utilise « responsabilité personnelle » avec peu d'emphase. L'attitude qu'elle adopte vis-à-vis du poste gouvernemental est : « Si quelque chose manque, je vais combler le vide ».

Sa philosophie de travail contient un principe appelé _humor over rumor_ (l'humour plutôt que la rumeur). Après que le système CoFacts ait détecté une désinformation virale, son équipe a publié en deux heures une vidéo ou deux images (moins de 200 mots) pour répondre à la fausse nouvelle avec humour. C'est ce qu'on appelle la règle du 2-2-2[^31].

Le « scandale des mouchoirs » en février 2020 est l'exemple le plus cité par les médias internationaux de cette période : une rumeur circulait selon laquelle les masques et les mouchoirs utilisaient la même pulpe, provoquant une panique d'achat ; le gouvernement a réagi en quelques heures avec une image (la photo « Nous n'avons qu'une seule carte Chen » du chef de l'exécutif à l'époque, Su Tseng-chang), accompagnée d'une explication des chaînes d'approvisionnement différentes pour les matières premières, faisant retomber la rumeur le jour même[^31]. Elle présente cela comme un exemple de _humor over rumor_ lors de conférences TED et dans de nombreux entretiens internationaux : la rumeur n'est pas réprimée par la loi, mais est recouverte par une image plus drôle qui y intègre les faits.

Le Ministère du développement numérique a été officiellement inauguré le 27 août 2022, où elle a pris ses fonctions en tant que première ministre[^32]. Le budget de la première année comptait 598 employés, un budget public de 5,7 milliards de dollars new taïwanais plus 16 milliards supplémentaires pour l'avenir, soit un total de 21,7 milliards[^33].

Au cours de son mandat, elle a promu la résilience numérique (en persuadant OneWeb britannique et SES de Luxembourg à déployer des terminaux à Taïwan), révisé la loi sur la signature électronique qui n'avait pas été modifiée depuis 20 ans, mis en ligne une plateforme SMS dédiée au gouvernement pour prévenir les fraudes, et exigé que 47 agences de niveau A adoptent le standard de transmission unifié T-Road en deux ans[^34][^35].

Mais elle a également reçu beaucoup de critiques positives. Ko Wen-je du Parti populaire a remis en question : « Avec une moyenne de 30 millions par personne, quel travail est-ce ? » ; Liu Shih-fang, députée du DPP, a déclaré que le ministère n'avait pas encore trouvé sa voie ; et Wu Yi-ling, députée du KMT, a dit : « Il n'y a aucune action concrète concernant la fraude en ligne qui préoccupe le plus les gens »[^36][^37].

Même les fonctionnaires PO (Responsables de l'engagement public) nommés par PDIS dans divers ministères étaient perplexes. Un rapport cite verbatim un PO :

> ✦ « J'ai fait du PO depuis deux mois, je pense que c'est une tâche supplémentaire, et je ne suis toujours pas clair sur le degré d'intervention ou de délégation que nous pouvons obtenir... Je ne sais pas quel sera notre rôle dans ces plateformes à l'avenir ? »[^38]

Elle n'a pas pu répondre à cette question. Ou plutôt, sa réponse est : décidez par vous-mêmes.

Le prix du « montrer au lieu d'ordonner » est la lenteur, des indicateurs de performance (KPI) peu flatteurs, et le fait qu'après deux ans, personne ne puisse clairement dire « Qu'a fait le Ministère du développement numérique ? ». Son pari était sur un changement culturel, et un changement culturel soit réussit, soit échoue.

Mais le système de transcriptions publiques SayIt de PDIS a accumulé plus de 7000 enregistrements de réunions jusqu'à son départ[^26]. N'importe qui peut saisir les mots-clés « Uber », « masque », « LINE Pay » et lire tout ce qu'elle a dit aux entreprises, aux fonctionnaires et aux députés à l'époque. Ce système n'existait pas avant qu'elle ne rejoigne le gouvernement, et personne ne l'a supprimé après son départ. Elle ne peut pas résumer cela en une phrase de bilan politique, mais elle a effectivement laissé un enregistrement de dialogue gouvernemental consultable sur sept ans — c'est la première fois dans l'histoire politique de Taïwan.

## La scène de remise des prix à Stockholm : elle dit « nous »

Le soir du 20 mai 2024, après la cérémonie d'investiture du président Lai Ching-te, Tang Fern s'est rendue directement à l'aéroport de Taoyuan. Durant les trois mois suivants, elle a visité 20 pays [^39].

En avril de cette année, elle a publié avec l'économiste Glen Weyl et la communauté Plurality dispersée dans le monde, le livre _Plurality: The Future of Collaborative Technology and Democracy_. Ce livre est distribué en CC0 — ce qui signifie que n'importe qui peut faire quoi avec le texte intégral sans attribution, sans frais ni demande de consentement [^40].

Pour le titre « Plurality », elles ont utilisé un caractère Han : ⿻ (écrit en chinois « 衆 », prononcé de manière similaire à _zhòng_). Ce caractère est l'un des « caractères descriptifs sémantiques » dans Unicode, utilisé pour décrire une structure où « deux choses sont entrelacées ». Elle a expliqué aux médias internationaux que ⿻ souligne l'« entrelacement » (_interweaving_) — les différences de nombreux individus ne sont pas effacées, mais forment une texture globale. Ce concept est précisément l'opposé du « génie » : un génie est un point lumineux rehaussé par le gris environnant ; ⿻ représente chaque ligne enroulée par les autres et indispensable.

L'affaire vTaiwan concernant la réglementation d'Uber est souvent citée comme un exemple de ⿻ : après six ans de blocage entre les taxis et les partisans d'Uber, Uber a finalement été légalisé sous sept conditions supplémentaires [^22]. Ce consensus n'a permis à aucune partie de « gagner » complètement, mais non plus à aucune partie de « perdre » complètement. Elle a dit que c'était là la véritable forme de la démocratie : le travail d'entrelacer la texture de tous dans un même tissu.

Le 7 octobre, le ministère des Affaires étrangères l'a nommée ambassadrice _ad hoc_ de la République de Chine (Cyber Ambassador-at-Large) [^41]. Sur son site personnel audreyt.org et sur cyberambassador.tw, la phrase d'introduction reste invariable :

> ✦ « I want to be a good enough ancestor for future generations. » (Je veux être un ancêtre assez bon pour les générations futures.) [^42]

Le 2 décembre 2025, à Stockholm, dans la salle de remise des prix de la Right Livelihood Foundation. Le Prix Right Livelihood est surnommé le « Nobel alternatif » ; il a été fondé en 1980 par le philanthrope d'origine allemande et suédoise Jakob von Uexküll pour combler les domaines non couverts par le prix Nobel.

Tang Fern est la première personne de Taïwan à recevoir cette distinction [^43]. La citation est la suivante :

> ✦ « For advancing the social use of digital technology to empower citizens, renew democracy and heal divides. » (Pour avoir promu l'utilisation sociale de la technologie numérique afin de donner du pouvoir aux citoyens, de renouveler la démocratie et de guérir les divisions.) [^43]

Dans son discours, elle n'a pas commencé par ce qu'elle a fait. Elle a parlé de ce qu'est le cyberespace :

> ✦ « Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation. It is time we work on peace in this zone. » (Le cyberespace est une région de conflit, et mon travail transforme ce conflit en une source d'énergie pour la co-création. Il est temps que nous travaillions à la paix dans cette zone.) [^43]

Elle a ensuite répété la phrase de la couverture du livre _Plurality_ :

> ✦ « The superintelligence we are looking for is already here. It's us. » (La superintelligence que nous recherchons est déjà là. C'est nous.) [^44]

Elle a reçu le prix surnommé le « Nobel alternatif », puis, sur la scène de remise des prix, elle a recentré l'attention sur le « nous » — celle qui était considérée par le monde comme un génie taïwanais, refusant une fois de plus cette position de « génie ».

De l'enfant de 8 ans bousculé dans sa classe pour enfants doués en 1989 à la femme de 44 ans sur la scène de remise des prix à Stockholm en 2025, il y a un long chemin pavé par une série de refus. Chaque refus semble être une rébellion, mais pris ensemble, ils révèlent une variation du même geste : le refus d'être défini comme un « individu exceptionnel », se replaçant dans le rôle de nœud, de pont, de constructeur d'espace.

Elle refuse d'être un génie. Le monde insiste pour qu'elle en soit un. Mais elle n'a jamais permis au monde de gagner ce débat — c'est juste que le monde met du temps à comprendre ce qu'elle dit réellement.

![Signature personnelle d'Audrey Tang en 2021](/article-images/people/audrey-tang-signature.svg)
_Signature personnelle d'Audrey Tang publiée en août 2021, initialement destinée au magazine japonais *Bungei Shunju*. Auteur : Audrey Tang elle-même, [domaine public CC0](https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg).\_

## Lectures complémentaires

- [Soda Green : de la petite scène de Gongliao à la lutte « fils et aiguilles », une bataille pour la souveraineté musicale de vingt ans](/fr/music/sodagreen) — Tout comme des figures marginales nées au cours du millénaire, il s'agit d'une longue lutte contre le « refus d'être confiné dans une identité prédéfinie », mais le théâtre est l'industrie musicale plutôt que le gouvernement.
- [Tony Hsiao](/fr/people/tony-hsiao-inside-founder) — Co-fondateur de INSIDE et Ai Liao Li, il définit également son rôle dans la sphère technologique taïwanaise en « traversant plusieurs domaines ».
- [Tai Yu Wu](/fr/people/tai-yu-wu) — La transmission des élites du savoir taïwanaises, de la science à la technologie : Tai Yu Wu a jeté les bases du système de recherche scientifique taïwanais en tant que directeur de l'Academia Sinica.
- [Fondation pour la culture ouverte](/fr/technology/open-culture-foundation) — Une fondation qui est passée d'un tableau de bord de comptabilité g0v à un pont des droits numériques taïwanais, interagissant à plusieurs reprises avec le ministère du développement dirigé par Tang Feng, tant en collaboration qu'en surveillance.
- [La pandémie de COVID à Taïwan et les vaccins](/society/台灣新冠疫情與疫苗) — Dans quel type d'épidémie se trouvait la chaîne de coordination de la carte des masques, ainsi que ces dix-huit mois où Taïwan a obtenu ses masques grâce aux frontières.

## Sources des images

Cet article utilise 3 images, toutes mises en cache dans `public/article-images/people/` pour éviter de dépendre d'un serveur externe. Les trois sont sous licence CC / CC0 de Wikimedia Commons :

- **hero** : [Portrait d'Audrey Tang (recadré)](<https://commons.wikimedia.org/wiki/File:Portrait_Audrey_Tang_(25915794061,_cropped).jpg>) — Photo : Camille McOuat, 09 mars 2016 à Paris, CC BY 2.0
- **scene-mid** : [Re:publica 19 - Jour 3](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>) — Photo : Jan Michalko, 08 mai 2019 à Berlin re:publica Conférence sur la société numérique, CC BY-SA 2.0
- **signature** : [Signature d'Audrey Tang](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>) — Auteur : Tang Feng elle-même, 18 août 2021, Domaine public CC0

## Références

[^1]: [TechNews : Création de la carte des masques, révélation de l'équipe derrière le « sauvetage par clavier » (2020-02-23)](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Détaille la chronologie où Wu Zhanwei Howard a déployé une API pour 20 000 dollars et Tang Feng coordonnait Google et g0v

[^2]: [Medium de Jiang Mingzong : Mise en ligne de la carte d'achat de masques des pharmacies (février 2020)](https://medium.com/%E6%B1%9F%E6%98%8E%E5%AE%97-kiang/%E8%97%A5%E5%B1%80%E5%8F%A3%E7%BD%A9%E6%8E%A1%E8%B3%BC%E5%9C%B0%E5%9C%96%E4%B8%8A%E7%B7%9A-54e11bd63e84) — L'ingénieur lui-même décrit, verbatim : « Les données officielles ne seront disponibles que le 6/2 à 8 heures du matin » + Tang Feng coordonne le développement avec les réseaux sociaux

[^3]: [Carte de décision clé pour la prévention du COVID-19 du Ministère de la Santé](https://covid19.mohw.gov.tw/ch/cp-4822-53563-205.html) — Description officielle du gouvernement, verbatim : « La commissaire Tang Feng a invité des communautés privées à produire une application de 'recherche de masques préventifs' en utilisant les données Open Data de la NHIA »

[^4]: [TechNews : Création de la carte des masques (voir [^1])](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Voir les informations supplémentaires dans le lien original

[^5]: [Wikipédia en chinois : Tang Feng](https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3) — Données biographiques de naissance / contexte familial / auto-apprentissage d'enfance, comme le clavier papier BASIC

[^6]: [Jin Zhoukan : La camarade jalouse l'a mise KO... L'enfant prodige Tang Feng a eu plusieurs idées suicidaires (2020-11)](https://www.businesstoday.com.tw/article/category/183035/post/202011090020/) — Scène de bagarre dans une salle d'école primaire + citation d'un camarade « Pourquoi ne meurs-tu pas » verbatim + décision de suspension après que sa mère ait trouvé des ecchymoses en prenant un bain

[^7]: [CNA : Li Yaqing, la plus jeune commissaire Tang Feng, met en œuvre le modèle d'auto-apprentissage pour la réforme éducative (2016-08-25)](https://www.chinatimes.com/realtimenews/20160825005980-260405) — Li Yaqing est revenue à Taïwan en 1992 et a fondé l'école expérimentale de Wulai Seed Family en tant que directrice en 1994

[^8]: [Taibo : Échapper au « harcèlement scolaire » pour se lancer dans l'auto-apprentissage ! La « grande découverte » de Tang Feng à 14 ans](https://www.taisounds.com/specialtopic/content/46/23226) — Après son isolement à Wulai à l'âge de 14 ans, elle a refusé d'être admise à Jianzhong

[^9]: Cité par plusieurs médias, elle répète dans différentes interviews : « Je ne pense pas qu'il y ait encore le terme 'génie' dans le monde moderne » et « À l'ère d'Internet, tout le monde est un QI de 180 »

[^10]: [Wikipedia: Audrey Tang](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang a commencé à programmer à l'âge de huit ans et a commencé à apprendre Perl à l'âge de 12 ans"

[^11]: Wikipédia en chinois : Tang Feng (voir [^5]) — A travaillé comme ingénieure dans la Silicon Valley à l'âge de 19 ans en 2000, et a annoncé sa retraite après avoir cédé Socialtext + Apple à l'âge de 33 ans en 2014

[^12]: [Wikipedia: Pugs (compilateur)](https://en.wikipedia.org/wiki/Pugs_(compiler) — Article Wikipédia

[^13]: [Wikipedia: Audrey Tang (English)](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang a initié plus de 100 projets Perl entre juin 2001 et juillet 2006, y compris l'archive populaire PAR"

[^14]: Wikipédia en chinois : Tang Feng (voir [^5]) + plusieurs médias citent uniformément verbatim : « Que ce soit maintenant, dans le passé ou dans le futur, je suis heureuse que les gens m'appellent par un nom féminin ». La source originale est un blog datant de 2005 sur blog.elixus.org

[^15]: [Jin Zhoukan : Interview du père de Tang Feng (septembre 2016)](https://www.businesstoday.com.tw/article/category/80407/post/201609010032/) — Le père, Tang Guanghua, dit verbatim : « Il n'y a aucune raison de ne pas accepter »

[^16]: [Taiwan Woman NMTH : Tang Fern, la première femme transgenre et la première conseillère numérique de Taïwan](https://women.nmth.gov.tw/?p=20105) — Tang Fern verbatim « Je suis une 'catégorie post-moderne' » + le champ du genre dans les données ministérielles de 2020 est marqué comme 'Aucun'

[^17]: [Marie Claire Taiwan : Après avoir été victime d'intimidation dans son enfance, Tang Fern dit : « Apprendre à vivre avec l'incertitude »](https://www.marieclaire.com.tw/entertainment/story/52923/audrey-tang) — verbatim « Tout a des lacunes, et les lacunes sont les portes de la lumière »

[^18]: [Article Wikipédia en chinois sur Tang Fern (voir [^5]) +](https://www.britannica.com/biography/Audrey-Tang) — Voir les informations supplémentaires dans le lien original

[^19]: [Taiwan Guanghua Magazine : Les hackers citoyens, g0v, un gouvernement sans temps](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — Point de départ en 2012/10 + visualisation du budget général du gouvernement central + liste des cofondateurs

[^20]: [CNA News PNN : Couverture du mouvement étudiant des fleurs de Taïwan (2014)](https://news.pts.org.tw/article/327548) — verbatim « Tous les circuits, caméras et équipements de diffusion en ligne dans le lieu étaient gérés par elle, la hackeuse citoyenne 'Tang Fern' » + commentaires de Tang Fern sur l'« spectacle et le rituel » du parlement + transcription faite à ses frais

[^21]: [Reporter : Créer un espace de dialogue — Le voyage fantastique de Tang Fern](https://www.twreporter.org/a/g0v-audrey-tang) — verbatim Cai Yuling rejoignant g0v hackathon en avril 2014 + origine de vTaiwan

[^22]: [Democracy Technologies: Consensus Building in Taiwan](https://democracy-technologies.org/participation/consensus-building-in-taiwan/) — vTaiwan a traité 26 sujets entre 2015 et 2018 / 80 % ont entraîné des actions gouvernementales concrètes / légalisation de 7 conditions d'Uber

[^23]: [Liberty Times : Briser les traditions, Tang Fern travaille à distance tous les mercredis et vendredis (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859132) — Première rencontre avec Lin Quan le 9/8 / Accord le 15/8 / Prise de fonction le 1/10 / Trois conditions pour l'entrée au gouvernement

[^24]: [Liberty Times : Tang Fern travaille à distance, Lin Quan : C'est faisable (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859246) — Lin Quan verbatim « Le Bureau exécutif n'a actuellement aucune réglementation sur le travail à distance... c'est faisable »

[^25]: Article Wikipédia en chinois sur Tang Fern (voir [^5]) — La plus jeune commissaire au gouvernement de l'histoire de Taïwan avec 35 ans + la première personnalité politique transgenre au niveau ministériel au monde

[^26]: [pdis.nat.gov.tw Registre de travail et système de transcription publique SayIt](https://sayit.pdis.nat.gov.tw/) — Structure du groupe PDIS composé de 20 personnes + la moitié est composée de civils / l'autre moitié est composée de volontaires ministériels + 30 stagiaires

[^27]: [Taipei Times : Audrey Tang nommée parmi les « 100 penseurs mondiaux » (25/01/2019)](https://www.taipeitimes.com/News/front/archives/2019/01/25/2003708586) — Inclusion dans le Top 100 des penseurs mondiaux de Foreign Policy (catégorie vote des lecteurs)

[^28]: [Rest of World : La vision 'conservateur-anarchiste' d'Audrey Tang pour l'avenir de Taïwan (2020)](https://restofworld.org/2020/audrey-tang-the-conservative-anarchist/) — verbatim « Toute forme de coercition descendante, qu'elle vienne des capitalistes ou de l'État, est également mauvaise »

[^29]: [Conversations with Tyler Ép.106 : Audrey Tang](https://conversationswithtyler.com/episodes/audrey-tang/) — verbatim « Je travaille avec le gouvernement ; je ne travaille pas pour le gouvernement »

[^30]: [Lindsey sur X : Citation en direct de la FAQ ICFP 2020](https://x.com/lindsey/status/1297886318114963456) — verbatim « À Taïwan, nous avons cette idée étrange que l'accès à Internet haut débit est un droit humain »

[^31]: [SwissInfo : Liberté d'expression : humour plutôt que rumeur](https://www.swissinfo.ch/eng/politics/freedom-of-expression-humour-over-rumour-lessons-from-taiwan-in-digital-democracy/46592080) — Voir les informations supplémentaires dans le texte du lien original

[^32]: [Site officiel du Ministère du développement numérique : Anciens ministres](https://moda.gov.tw/aboutus/ministers-since-2022/1527) — Période de mandat de Tang Feng, du 27 août 2022 au 20 mai 2024 (mot pour mot)

[^33]: [Liberty Times : Tang Feng dirigera le ministère du numérique avec 598 employés prévus](https://news.ltn.com.tw/news/politics/breakingnews/4021987) — Reportage de Liberty Times

[^34]: [Liberty Finance : De ministre informatique génial à conférencière indépendante, bilan des 3 réalisations et controverses durant le mandat de Tang Feng](https://ec.ltn.com.tw/article/breakingnews/4677986) — Résilience numérique / OneWeb / Satellite SES / Réforme de la loi sur la signature électronique / Plateforme SMS à code court 111

[^35]: [INSIDE : Un an du ministère du développement numérique ! Détail des deux réalisations et trois controverses de Tang Feng](https://www.inside.com.tw/article/32615-Taiwan-moda-anniversary) — Norme de transmission unifiée T-Road pour 47 agences de niveau A + Collègue 'Par rapport aux unités précédentes, Tang Feng est plus disposée à déléguer le pouvoir'

[^36]: [Far Eastern Magazine : Le 'ministère du développement numérique' dirigé par Tang Feng approche d'un an, les critiques disent qu'il n'y a pas de réalisations](https://www.gvm.com.tw/article/105627) — Critiques de Liu Shih-fang / Wu Yi-ching (mot pour mot)

[^37]: [ETtoday : Le budget du ministère du développement numérique est de 21,1 milliards ; Ko Wen-je s'étonne : en moyenne, 30 millions par personne 'Quel travail est-ce ?' (30/08/2022)](https://www.ettoday.net/news/20220830/2327863.htm) — Questionnement de Ko Wen-je (mot pour mot)

[^38]: [Reporter : Gouvernement ouvert, comment Tang Feng a-t-elle réussi le passage au statut de fonctionnaire ?](https://www.twreporter.org/a/open-government-audrey-political-commissar-challenges) — PO 'J'ai été PO pendant 2 mois... Je ne suis pas sûr de savoir dans quelle mesure nous pouvons intervenir'

[^39]: [Liberty Finance : De ministre informatique génial à conférencière indépendante (même que [^34])](https://ec.ltn.com.tw/article/breakingnews/4677986) — Reportage de Liberty Times

[^40]: [Plurality Institute : Lancement du livre Plurality](https://www.plurality.institute/blog-posts/book-launch-plurality-the-future-of-collaborative-technology-and-democracy-by-e-glen-weyl-audrey-tang-and-the-plurality-community) — Co-écrit avec Glen Weyl + Communauté Plurality / Publié le 16 avril 2024 / Libéré sous CC0

[^41]: [Article de Wikipédia en chinois sur Tang Feng (même que [^5])+](https://cyberambassador.tw/) — Voir les informations supplémentaires dans le texte du lien original

[^42]: [audreyt.org](https://audreyt.org/) — Voir les informations supplémentaires dans le texte du lien original

[^43]: [Right Livelihood : Audrey Tang honorée par le Prix Right Livelihood (2025)](https://rightlivelihood.org/news/taiwans-audrey-tang-honoured-with-right-livelihood-award-for-advancing-digital-democracy-and-social-trust/) — Citation mot pour mot + Passage de Tang recevant un discours 'Le cyberespace est une région de conflit' + [Reportage en anglais du Focus Taiwan, agence Xinhua](https://focustaiwan.tw/society/202512030022)

[^44]: cyberambassador.tw (mot pour mot) + Réinterprétation philosophique de Plurality — "La superintelligence que nous recherchons est déjà là. C'est nous"
