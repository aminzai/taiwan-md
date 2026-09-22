---
title: "Tang Ping: Cada decisão notável dela rejeita o rótulo de 'gênio'"
description: "Aos 8 anos, foi nocauteada por colegas; aos 14, recusou a admissão na Jianzhong; aos 24, se assumiu como transexual mas recusou ser embaixadora; aos 35, o primeiro requisito para entrar no gabinete era 'não ter escritório'. Em 2 de dezembro de 2025, ela recebeu o Prêmio Right Livelihood em Estocolmo e falou não sobre 'eu', mas sobre 'nós'."
date: 2026-05-16
category: 'People'
tags:
  [
    'pessoa',
    'Tang Ping',
    'Departamento de Desenvolvimento Digital',
    'g0v',
    'transgênero',
    'programação',
    'governo aberto',
    'vTaiwan',
    'Plurality',
    'Prêmio Right Livelihood',
  ]
subcategory: '教育與社會'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-05-16
lastHumanReview: true
readingTime: 14
image: '/article-images/people/audrey-tang-portrait-2016.webp'
imageAlt: 'Retrato de Tang Ping tirado em Paris em março de 2016, vestindo roupas escuras sob luz natural suave.'
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
translatedAt: '2026-09-22T15:14:24.762164+00:00'
---

# Tang Feng: Cada decisão notável dela rejeita o rótulo de "gênio"

> **Resumo em 30 segundos:**
> Aos 8 anos, foi nocauteada por colegas e se afastou dos estudos; aos 14, recusou a admissão na Jianzhong; aos 24, fez _coming out_ como transgenérica mas rejeitou ser porta-voz; aos 35, a primeira condição para entrar no gabinete era "não ter escritório". Em 2020, de madrugada, ela e Jiang Mingzong codificaram um mapa de máscaras no Slack do g0v; em 2 de dezembro de 2025, recebeu o Prêmio Right Livelihood em Estocolmo. Enquanto todos esperavam sua história pessoal, ela enfatizou a palavra "nós" no palco. O mundo a trata como uma gênio; cada decisão notável dela rejeita esse lugar.

## Um Mapa de Máscaras que Queimou Vinte Mil Dólares

No final de janeiro de 2020, a COVID-19 começou a se espalhar em Taiwan. A escassez de máscaras em farmácias e o anúncio do governo sobre a compra com registro (em 2/6) geraram uma corrida por suprimentos. Em 2 de fevereiro, Howard Wu Chuan-wei, um engenheiro da Tainan Good Idea Studio, criou um mapa usando a API do Google Maps para rastrear os estoques de máscaras em lojas próximas. Ele o implementou e compartilhou nas redes sociais na madrugada[^1].

Ao almoçar, ele voltou ao computador e viu que a conta de _backend_ da API do Google havia atingido 20 mil dólares — queimados pelo volume de uso em 24 horas.

Naquele dia, Tang Fern apareceu no canal Slack do g0v. Ela não estava lá para dar ordens. Ela coordenou com a equipe de engenheiros do Google para conter a conta atual; ao mesmo tempo, junto com alguns amigos antigos do g0v — Jiang Ming-zong (secretário anterior do Escritório de Cidades Inteligentes de Tainan), e membros da equipe de TI da Agência Nacional de Seguro Saúde (Chang Ling-chi, Chen Tzu-yu) — eles pensaram: como fazer com que o estoque de máscaras das mais de 6.000 farmácias em todo Taiwan seja sincronizado a um mapa acessível por qualquer pessoa a cada 30 segundos[^2]?

Às 8h da manhã do dia 6 de fevereiro, o mapa de compra de máscaras das farmácias foi oficialmente lançado com os dados abertos da Agência Nacional de Seguro Saúde. Em 24 horas, mais de 1 milhão de acessos foram registrados. Até 15 de fevereiro, 101 aplicações relacionadas haviam sido acumuladas no HackMD, e a comunidade g0v havia criado mais de 140 ferramentas[^2][^3].

Jiang Ming-zong mencionou em sua transcrição de palestra:

> ✦ "A Secretária é muito habilidosa com arquitetura da informação; ela entende qualquer requisito que apresentamos. O mais importante é que Tang Fern tem poder de decisão e pode modificar o código sozinha, então não precisamos ir a Pequim para relatar a nenhum superior."[^4]

O protagonista desta história não foi apenas Tang Fern. Foram Jiang Ming-zong, Howard Wu Chuan-wei, os funcionários da equipe de TI da Agência Nacional de Seguro Saúde, os centenas de engenheiros da comunidade g0v e toda a noite em que o escritório de Tang Fern estava constantemente modificando o código.

Mas após 2020, todas as mídias estrangeiras focaram nela como a única protagonista. A BBC escreveu "Audrey Tang salvou Taiwan com código", a Wired escreveu "A Hacker que se Tornou Ministra Digital de Taiwan", e a TIME a listou entre os "líderes globais no combate à pandemia".

Em cada entrevista, ela devolvia o crédito. Mas a narrativa de "a ministra gênio salva Taiwan" estava grudada nela por mais de quarenta anos, e não foi tão fácil remover.

## Aos 8 Anos Foi Trocada e Desmaiou por Colegas, aos 14 Recusou a Escola Jianzhong

Em 18 de abril de 1981, Tang Feng nasceu em Taipé. Seu nome original era Tang Zonghan. Seu pai, Tang Guanghua, foi vice-editor do _China Times_, e sua mãe, Li Yaqing, foi subdiretora da equipe de reportagem do mesmo jornal[^5].

Ela tinha uma cardiopatia congênita. A escola realizou três testes de QI, e todos indicaram "pelo menos 160" (o nível mais alto do instrumento de teste). Quando ela tinha 8 anos, sua família ainda não possuía um computador; ela leu um livro de programação Applesoft BASIC e desenhou um teclado e uma tela de computador em papel, escrevendo os botões e o conteúdo que o computador poderia exibir[^5].

Mas o rótulo de "criança gênio" pode ser o adjetivo mais comum associado ao seu nome em 2026; aos 8 anos, isso não era uma realidade. Naquele lugar havia agressão física, hematomas e a pergunta: "Por que você não morre?".

No sexto ano do ensino fundamental, ela trocou de três jardins de infância e seis escolas primárias. Em um dia no segundo ano, depois que a professora saiu da sala com as provas corrigidas, Tang Feng tinha terminado cedo. Vários colegas que não conseguiam terminar estenderam as mãos para pegar sua prova. Ela correu com a prova e caiu; um dos colegas usou toda a sua força para chutá-la, e ela bateu na parede e desmaiou[^6]. Mais tarde, aquele colega disse uma frase que foi registrada verbatim pela _Ima Weekly_:

> ✦ "Por que você não morre? Se você morresse, eu seria o melhor."[^6]

Ela não falou sobre isso ao chegar em casa. Um dia, sua mãe viu os hematomas em seu abdômen enquanto ela tomava banho e decidiu suspender seus estudos[^6].

A mãe, Li Yaqing, depois foi para a Alemanha estudar educação alternativa e fundou a Escola Experimental de Crianças Semente em Wulai em 1994, tornando-se sua primeira diretora[^7]. Em 1995, aos 14 anos, Tang Feng anunciou aos pais, após um período de reclusão na montanha de Wulai: ela não iria mais estudar e desistiu da admissão automática na Jianzhong[^8].

Isso não foi uma escolha do tipo "eu sou muito gênio e não preciso de escola". Foi a decisão, aos catorze anos, de uma criança que aprendeu a se esconder aos oito, de rejeitar a versão dela enquadrada como "superdotada".

Ela disse muitas vezes: "Eu não acho que exista mais o conceito de gênio no mundo moderno. Na era da internet, todo mundo é um QI 180."[^9]

## Aos 24 anos, ela mudou de nome, mas recusou ser uma embaixadora transgênero

Aos 12 anos, ela começou a aprender Perl[^10]. Aos 19 (em 2000), já era engenheira em uma empresa de software no Vale do Silício, na Califórnia[^11].

Em 1º de fevereiro de 2005, aos 24 anos, ela iniciou o projeto Pugs — um compilador e interpretador do Perl 6 implementado em Haskell[^12]. O Pugs foi um projeto _bootstrap_ na comunidade Perl: uma linguagem implementada por outra. Entre 2001 e 2006, ela lançou mais de 100 projetos no CPAN[^13]. A comunidade internacional de código aberto a chamava de Audrey ou au.

No final de 2005, ela se autodeclarou transgênero em seu blog, blog.elixus.org[^14]. Ela usava estrogênio, mas não fez cirurgia. Mudou seu nome chinês para "Tang Feng" e seu nome inglês, Autrijus, para Audrey.

Nessa postagem do blog, ela escreveu:

> ✦ «Não importa o passado, presente ou futuro, estou feliz que as pessoas me chamem com um substantivo feminino.»[^14]

A resposta de seu pai, Tang Guanghua, em uma entrevista, foi posteriormente transcrita verbatim por várias mídias:

> ✦ «Se ela sente que a mudança de gênero pode torná-la mais feliz e mais criativa, sem prejudicar ninguém, não há razão para rejeitar.»[^15]

Ela recusou o cargo de "embaixadora transgênero". Em 2020, ela marcou "nenhum" no campo de gênero em seu currículo governamental. Na época, ela explicou aos repórteres[^16]:

> ✦ «Eu sou 'pós-categoria'. Eu não escolho um lado na discussão de gênero. Não é que eu ache o tema sem importância, mas acho que a discussão não resolve nenhum problema.»[^16]

Em uma entrevista com a Marie Claire, ela deixou outra frase frequentemente citada:

> ✦ «Se você conseguir conviver com a confusão, aos poucos verá que nem é um problema seu, nem social, mas sim a lacuna no meio. Tudo tem uma lacuna, e a lacuna é a entrada da luz.»[^17]

De 2010 a 2016, ela atuou como consultora da Apple, participando do desenvolvimento do Siri, cujo valor por hora era supostamente equivalente a 1 Bitcoin[^18]. Aos 33 anos (em 2014), ela transferiu suas responsabilidades com o Socialtext e a Apple, declarando "aposentadoria"[^11].

## g0v e o Palácio de Legisladores do Flores de Girassol: Dar Crédito aos Invisíveis

Em outubro de 2012, ela cofundou o g0v Zero Hour Government com Kaohsiung (clkao), Kirby e ipa. O ponto de partida foi a insatisfação com um anúncio da "Proposta de Impulso Econômico" do Conselho Executivo — um comercial governamental com orçamento de 33 milhões, que não deixava claro o que o governo pretendia fazer[^19].

O primeiro projeto do g0v foi a visualização orçamentária do governo central: transformar os pesados relatórios orçamentários em páginas clicáveis[^19]. Mais tarde vieram o MoeDict, o IVOD (Cinema Legislativo) e a transmissão ao vivo do Palácio de Legisladores durante o Movimento Flores de Girassol.

Na madrugada de 18 de março de 2014, estudantes ocuparam o Palácio de Legisladores. Todos os circuitos, câmeras e equipamentos de transmissão online no local foram montados por Tang Feng[^20].

Mas ela saiu do palácio em apenas uma hora. Mais tarde, a PNN (China Central Television) a entrevistou, e ela disse:

> ✦ "Com cinco câmeras filmando e transmitindo ao vivo de diferentes ângulos dentro do palácio, todas as atividades se tornaram um mero espetáculo e ritual."[^20]

Ela não tinha interesse na ocupação nem na declaração política. O que importava era a tecnologia das ferramentas. Ao mesmo tempo, ela pagou para transcrever reuniões governamentais — permitindo que pessoas que não estavam presentes lessem o diálogo completo[^20].

Após o Flores de Girassol, em abril de 2014, Tsai Ing-wen (a então comissária) participou do hackathon do g0v. A partir desse momento, os termos "governo" e "g0v", que eram originalmente antagônicos, começaram a desenvolver um meio-termo[^21].

O nome desse meio-termo é vTaiwan. Entre 2015 e 2018, a plataforma processou 26 tópicos, dos quais 80% resultaram em ações governamentais concretas[^22]. O exemplo mais conhecido foi o debate sobre regulamentação do Uber: taxistas e defensores do Uber estagnaram por seis anos, e finalmente legalizaram o Uber sob sete condições[^22].

O núcleo da plataforma é o motor de consenso Pol.is — onde grandes quantidades de opiniões são organizadas em alguns _clusters_ (aglomerados), permitindo que cada participante veja "com quem ele pensa parecido, com quem ele pensa diferente e quais reivindicações são aceitas por todos". Ele não vota nem se opõe; apenas desenha o formato da divergência.

## Sem escritório, transcrições totalmente públicas e três dias de trabalho remoto por semana

Em 9 de agosto de 2016, Tang Feng, aos 35 anos, conheceu Lin Quan, o chefe do Conselho Executivo. Em 15 de agosto, ela aceitou o cargo de Comissária Política. No final de setembro, ela retornou a Taiwan vinda do Vale do Silício. Em 1º de outubro, ela assumiu no Conselho Executivo[^23].

Os três termos que ela negociou previamente se tornaram uma ruptura inédita no sistema burocrático taiwanês: trabalho remoto às quartas e sextas-feiras; transcrições públicas de todas as reuniões; e não ser obrigada a ir ao escritório todos os dias[^23].

Lin Quan explicou aos repórteres na época:

> ✦ "O Conselho Executivo atualmente não tem regulamentação para trabalho remoto, mas seu modo de trabalho anterior foi sempre remoto. Eu acredito que, sem afetar o trabalho, é viável transmitir ideias ou instruções políticas remotamente através do computador."[^24]

Ela se tornou três coisas: a Comissária Política mais jovem da história de Taiwan, a primeira figura ministerial com identidade transgênero divulgada globalmente e a primeira "Comissária Digital" de Taiwan[^25].

Ela não tinha um escritório fixo no Conselho Executivo. Ela dizia que todo o complexo era seu espaço de trabalho. Após as reuniões, as transcrições eram publicadas em sayit.pdis.nat.gov.tw, e qualquer pessoa podia pesquisar[^26].

Ela formou um pequeno grupo de 20 pessoas chamado PDIS (Public Digital Innovation Space, Espaço Público de Inovação Digital). Metade era composta por profissionais do setor privado e a outra metade por voluntários de diferentes ministérios. No verão, foram adicionados mais 30 estagiários[^26]. Não era uma organização hierárquica — era um espaço de trabalho.

Em 2019, ela foi selecionada como uma das cem pensadoras globais da _Foreign Policy_ (categoria votação do leitor)[^27]. A mídia a descreveu como "a única ministra transgênero global" e "estrela da programação". Em todas as entrevistas, ela devolvia o crédito — mas a história da "ministra gênio" era mais facilmente recontada do que o que ela dizia.

![Tang Feng em 8 de maio de 2019 no evento Digital Social da re:publica em Berlim](/article-images/people/audrey-tang-re-publica-2019.webp)
_Cena do diálogo "Digital Social Innovation" na re:publica em Berlim, 8 de maio de 2019, com Tang Feng e Julia Kloiber. Foto: Jan Michalko. [CC BY-SA 2.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg).\_

## Anarcocapitalismo: Recusar Ordens e Recusar Ser Ordenado

Tang Feng se autodenomina uma "anarcocapitalista". À primeira vista, é um termo contraditório.

"Conservador" significa manter os sistemas existentes que funcionam bem; "anarquista" significa ser contra a concentração de poder e recusar coerção de cima para baixo. Quem junta essas duas palavras geralmente quer dizer: eu acredito que há algo de valor nos sistemas atuais, mas não acredito que ninguém tenha o direito de forçar os outros a aceitá-lo por autoridade.

Em uma entrevista com Rest of World, ela deixou uma declaração quase um manifesto:

> ✦ "Any top-down, coercion, whether it's from the capitalists or from the state, is equally bad." (Qualquer coerção de cima para baixo, seja dos capitalistas ou do estado, é igualmente ruim.)[^28]

Em sua entrevista com o economista Tyler Cowen, quando lhe perguntaram "qual é o seu papel", ela disse:

> ✦ "I'm working _with_ the government; I'm not working _for_ the government." (Eu trabalho _com_ o governo; eu não trabalho _para_ o governo.)[^29]

No Q&A da Conferência Internacional de Ciência da Computação (ICFP) em 2020, ela também lançou uma frase como esta:

> ✦ "In Taiwan we have this strange idea that broadband internet access is a human right. Everyone has broadband. And if you don't, it's my fault, personally." (Em Taiwan temos essa ideia estranha de que o acesso à internet banda larga é um direito humano. Todo mundo tem banda larga. E se você não tiver, é minha culpa, pessoalmente.)[^30]

Ela usa a palavra "direito humano" com muito peso, mas usa "responsabilidade pessoal" com pouca. A atitude que ela quer ter no serviço governamental é: "se algo estiver faltando, eu vou complementar".

Sua filosofia de trabalho inclui o lema _humor over rumor_ (humor em vez de boato). Quando o sistema CoFacts detectava desinformação viral, sua equipe lançava um vídeo de dois minutos ou duas imagens (com menos de 200 caracteres) em duas horas para responder ao falso boato com humor. Isso é conhecido como a regra 2-2-2[^31].

O "Incidente do Papel Higiênico" em fevereiro de 2020 foi o caso mais citado pela mídia internacional na época: boatos circulavam de que máscaras e papel higiênico usavam o mesmo tipo de polpa, causando pânico e acúmulo por parte do público; o Conselho Executivo lançou uma imagem com explicação da cadeia de suprimentos, mostrando diferentes fontes de matéria-prima (a foto "Nós só temos um [tipo de] cartão" do então chefe executivo Su Tsz-chang), e os boatos esfriaram no mesmo dia[^31]. Ela usou isso como exemplo de _humor over rumor_ em TED e em várias entrevistas internacionais: o boato não era reprimido por lei, mas sim coberto por uma imagem mais engraçada que inseria a verdade.

Em 27 de agosto de 2022, o Departamento de Desenvolvimento Digital foi oficialmente inaugurado, e ela assumiu como primeira diretora[^32]. No primeiro ano, havia 598 funcionários orçamentários, um orçamento público de NT$ 5,7 bilhões mais NT$ 16 bilhões de "visão futura", totalizando NT$ 21,7 bilhões[^33].

Durante seu mandato, ela promoveu a resiliência digital (convencendo OneWeb do Reino Unido e SES da Luxemburgo a implantar terminais em Taiwan), revisou o 《Lei de Assinatura Eletrônica》 que não era atualizada há 20 anos, lançou uma plataforma de SMS dedicada ao governo para prevenção de fraudes, e exigiu que 47 agências de Nível A adotassem o padrão de transmissão unificado T-Road em dois anos[^34][^35].

Mas ela também recebeu muitas críticas positivas. Ko Wen-jei do Partido Popular questionou: "média de 30 milhões por pessoa, que tipo de trabalho é este?"; Liu Shih-fang, deputada do DPP, disse: "o Departamento Digital ainda não encontrou seu rumo"; e Wu Yi-ling, deputada do KMT, afirmou: "não há ações concretas sobre o golpe de internet, que mais preocupa o povo"[^36][^37].

Até os funcionários públicos PO (Ponto de Contato Público) nomeados para cada ministério pelo PDIS ficaram confusos. Um repórter entrevistou um PO em _verbatim_:

> ✦ "Faz dois meses que sou PO, sinto que é mais uma tarefa, ainda não entendi bem o quanto podemos intervir ou qual autorização podemos obter... eu não sei qual será nosso papel nesses plataformas no futuro?"[^38]

Ela não conseguiu responder a essa pergunta. Ou melhor, sua resposta foi: você decide.

O preço de "demonstrar em vez de ordenar" é lentidão, KPIs pouco bonitos e dois anos sem que ninguém consiga dizer claramente "o que o Departamento Digital fez". Sua aposta era na mudança cultural, e a mudança cultural ou acontece ou não acontece.

Mas o sistema SayIt de transcrição pública do PDIS acumulou mais de 7000 registros completos de reuniões até o dia em que ela renunciou[^26]. Qualquer pessoa poderia digitar palavras-chave como "Uber", "máscara" ou "LINE Pay" e ler cada palavra que ela disse com fornecedores, funcionários públicos e deputados. Este sistema não existia antes dela entrar no governo, nem foi removido depois que ela saiu. Ela não conseguia resumir tudo em uma frase de conquista política, mas ela realmente deixou um registro de diálogo governamental pesquisável por sete anos — algo inédito na história política de Taiwan.

## O Pódio de Estocolmo, Ela Disse "Nós"

Em 20 de maio de 2024, na noite seguinte à cerimônia de posse do presidente Lai Ching-te, Tang Fern se dirigiu diretamente ao Aeroporto de Taoyuan. Nos três meses seguintes, ela visitou 20 países[^39].

Em abril do mesmo ano, ela publicou, junto com o economista Glen Weyl e a comunidade Plurality distribuída globalmente, o livro 《Plurality: The Future of Collaborative Technology and Democracy》. Este livro foi lançado sob licença CC0 — ou seja, qualquer pessoa pode fazer qualquer coisa com o texto completo sem precisar de atribuição, pagamento ou consentimento[^40].

Para o título "Plurality", elas usaram um caractere Han: ⿻ (escrito em chinês como 衆, pronunciado de forma semelhante a _zhòng_). Este caractere é um dos "caracteres descritivos semânticos" no Unicode e é usado para descrever uma estrutura onde "duas coisas se entrelaçam". Ela explicou à mídia internacional que ⿻ enfatiza o "entrelaçamento" (_interweaving_) — as diferenças de muitos indivíduos não são eliminadas, mas formam uma textura coesa. Este conceito é exatamente o oposto de "gênio": um gênio é um ponto brilhante realçado pelo cinza ao redor; ⿻ é cada linha sendo envolvida pelas outras e essencial para o todo.

O caso do vTaiwan lidando com as regulamentações da Uber é frequentemente usado por ela como exemplo de ⿻: taxistas e defensores da Uber estagnaram por seis anos, chegando a uma legalização da Uber sob sete condições adicionais[^22]. Esse consenso não fez com que nenhuma das partes "vencesse" completamente, mas também não fez com que nenhuma delas "perdesse" completamente. Ela disse que essa é a verdadeira forma da democracia — o trabalho de tecer a textura de todos em um mesmo tecido.

Em 7 de outubro, o Ministério das Relações Exteriores a nomeou Embaixadora _ad hoc_ (Cyber Ambassador-at-Large) da República da China (Taiwan)[^41]. Na sua página pessoal audreyt.org e em cyberambassador.tw, a frase inicial permanece:

> ✦ "I want to be a good enough ancestor for future generations." (Eu quero ser um ancestral bom o suficiente para as gerações futuras.)[^42]

Em 2 de dezembro de 2025, no salão de premiação da Right Livelihood Foundation em Estocolmo. O Prêmio Right Livelihood é chamado de "Prêmio Nobel Alternativo", criado em 1980 pelo filantropo alemão de origem sueca Jakob von Uexküll, para preencher áreas não cobertas pelo Prêmio Nobel.

Tang Fern foi a primeira pessoa de Taiwan a receber este prêmio[^43]. A citação é:

> ✦ "For advancing the social use of digital technology to empower citizens, renew democracy and heal divides." (Por promover o uso social da tecnologia digital para empoderar cidadãos, renovar a democracia e curar divisões.)[^43]

Na sua palestra, a primeira coisa que ela disse não foi o que ela fez. Ela falou sobre o que é o ciberespaço:

> ✦ "Cyberspace is a conflict region, and my work turns that conflict into an energy source for co-creation. It is time we work on peace in this zone." (O ciberespaço é uma região de conflito, e meu trabalho transforma esse conflito em uma fonte de energia para cocriação. É hora de trabalharmos pela paz nesta zona.)[^43]

Em seguida, ela reiterou a frase da capa do livro Plurality:

> ✦ "The superintelligence we are looking for is already here. It's us." (A superinteligência que procuramos já está aqui. Somos nós.)[^44]

Ela aceitou o prêmio chamado de "Prêmio Nobel Alternativo" e, no pódio, mudou o foco para "nós" — ela, que é vista como um gênio por todo o mundo, recusou mais uma vez a posição de "gênio".

Da criança de 8 anos, chutada em sala de aula avançada em 1989, à mulher de 44 anos no pódio de Estocolmo em 2025, há um longo caminho pavimentado por inúmeras recusas. Cada recusa parece ser uma rebeldia, mas vistas juntas, elas revelam variações do mesmo movimento: a recusa em ser definida como um "indivíduo excepcional", reposicionando-se como construtora de nós, pontes e espaços.

Ela recusou ser um gênio. O mundo insiste em vê-la como tal. Mas ela nunca permitiu que o mundo vencesse essa discussão — apenas levou muito tempo para o mundo entender o que ela realmente estava dizendo.

![Tang Fern SVG assinado publicamente em 2021](/article-images/people/audrey-tang-signature.svg)
_Assinatura pessoal de Tang Fern, divulgada publicamente em agosto de 2021, originalmente destinada à revista japonesa *Bungei Shunju*. Autor: Tang Fern, [Domínio Público CC0](https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg).\_

---

## Leitura Complementar

- [Soda Green: Da pequena cena de Gongliao à luta "Fish and Thread", uma batalha por soberania musical que durou vinte anos](/pt/music/sodagreen) — Assim como um grupo marginalizado que surgiu na década de 2000, e assim como a longa luta para "recusar ser enquadrado em uma identidade predefinida", mas o cenário é a indústria musical, não o governo.
- [Tony Hsiao](/pt/people/tony-hsiao-inside-founder) — Cofundador da INSIDE e Ai Liao Ri, ele também define seu papel no círculo tecnológico de Taiwan como alguém que "atravessa múltiplos campos".
- [Tai Yu Wu](/pt/people/tai-yu-wu) — A transmissão do conhecimento de elite científica em Taiwan, de ciência a tecnologia; Tai Yu Wu estabeleceu o sistema científico de Taiwan como diretor do Academia Sinica.
- [Open Culture Foundation](/pt/technology/open-culture-foundation) — Uma fundação que se transformou na ponte de direitos digitais de Taiwan após reportar g0v, e que interagiu repetidamente com o Departamento de Desenvolvimento Digital liderado por Tang Feng, tanto cooperando quanto observando.
- [Pandemia e Vacinas em Taiwan](/society/台灣新冠疫情與疫苗) — Em que tipo de pandemia estava a cadeia de coordenação do mapa de máscaras, e os dezoito meses que Taiwan conseguiu com base nas fronteiras e na compra de máscaras.

## Fontes das Imagens

Este artigo utiliza 3 imagens, todas cacheadas em `public/article-images/people/` para evitar fontes de servidor com problemas de link. As três são licenciadas sob CC / CC0 do Wikimedia Commons:

- **hero**: [Retrato de Audrey Tang (cortado)](<https://commons.wikimedia.org/wiki/File:Portrait_Audrey_Tang_(25915794061,_cropped).jpg>) — Foto: Camille McOuat, 09-03-2016 Paris, CC BY 2.0
- **scene-mid**: [Re:publica 19 - Dia 3](<https://commons.wikimedia.org/wiki/File:Re_publica_19_-_Day_3_(32860400897).jpg>) — Foto: Jan Michalko, 08-05-2019 Berlim Re:publica Conferência Digital Social, CC BY-SA 2.0
- **signature**: [Assinatura de Audrey Tang](<https://commons.wikimedia.org/wiki/File:Audrey_Tang_signature_(51385705516).svg>) — Autor: Tang Feng, 18-08-2021, Domínio Público CC0

## Referências

[^1]: [TechNews: Mapeamento de Máscaras Criado por um Grupo, Revelando a Equipe Por Trás do 'Resgate Nacional com Teclado' (23/02/2020)](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Detalha o cronograma da API cobrando US$ 20.000 após o deploy de Wu Zhanwei Howard e a coordenação de Tang Feng com Google e g0v.

[^2]: [Medium por Jiang Mingzong: Mapa de Compra de Máscaras em Farmácias Lançado (Fev/2020)](https://medium.com/%E6%B1%9F%E6%98%8E%E5%AE%97-kiang/%E8%97%A5%E5%B1%80%E5%8F%A3%E7%BD%A9%E6%8E%A1%E8%B3%BC%E5%9C%B0%E5%9C%96%E4%B8%8A%E7%B7%9A-54e11bd63e84) — O próprio engenheiro descreve, verbatim, 'Os dados oficiais serão lançados apenas às 8h do dia 6/2' + Tang Feng coordenando o desenvolvimento com a comunidade.

[^3]: [Mapa de Decisões Críticas de Prevenção da COVID-19 do Ministério da Saúde](https://covid19.mohw.gov.tw/ch/cp-4822-53563-205.html) — Descrição oficial do governo, verbatim: 'A Comissária Tang Feng do Executivo convidou comunidades privadas para produzir uma plataforma de consulta de máscaras de prevenção usando dados abertos da NHI'.

[^4]: [TechNews: Mapeamento de Máscaras Criado por um Grupo (o mesmo que [^1])](https://technews.tw/2020/02/23/expose-the-team-behind-mask-map/) — Consulte os dados suplementares no link original.

[^5]: [Wikipédia em Chinês: Tang Feng](https://zh.wikipedia.org/zh-tw/%E5%94%90%E9%B3%B3) — Dados biográficos básicos sobre nascimento / histórico familiar / autoaprendizagem na infância, como teclado de papel.

[^6]: [Ima Weekly: Colega Inveja a Nocautea... Gênio Tang Feng Quase Tenta Suicídio Várias Vezes na Infância (Nov/2020)](https://www.businesstoday.com.tw/article/category/183035/post/202011090020/) — Cena de briga em sala de ensino fundamental + citação do colega 'Por que você não morre?' verbatim + decisão de suspensão após a mãe encontrar hematomas durante o banho.

[^7]: [China Times: Li Yaqing, A Comissária Mais Jovem de Tang Feng, Pratica o Paradigma da Autoaprendizagem na Reforma Educacional (25/08/2016)](https://www.chinatimes.com/realtimenews/20160825005980-260405) — Li Yaqing retornou a Taiwan em 1992 e fundou a Escola Experimental Ulai Seedling como diretora em 1994.

[^8]: [Tai Bo: Fugindo do 'Bullying Escolar' para a Autoaprendizagem! A 'Grande Descoberta' de Tang Feng aos 14 Anos](https://www.taisounds.com/specialtopic/content/46/23226) — Recusa de ser recomendada para Jianzhong após o isolamento em Ulai aos 14 anos.

[^9]: Citado por várias mídias, a pessoa repete em diferentes entrevistas: 'Não acho que exista mais o termo gênio no mundo moderno', 'Na era da internet, todos são QI 180'.

[^10]: [Wikipedia: Audrey Tang](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang começou a programar aos oito anos e aprendeu Perl aos 12 anos"

[^11]: Wikipédia em Chinês: Tang Feng (o mesmo que [^5]) — Trabalhou como engenheira no Vale do Silício aos 19 anos em 2000, e anunciou a aposentadoria ao deixar o Socialtext + Apple aos 33 anos em 2014.

[^12]: [Wikipedia: Pugs (compilador)](https://en.wikipedia.org/wiki/Pugs_(compiler) — Entrada da Wikipédia.

[^13]: [Wikipedia: Audrey Tang (Inglês)](https://en.wikipedia.org/wiki/Audrey_Tang) — "Tang iniciou mais de 100 projetos Perl entre junho de 2001 e julho de 2006, incluindo o popular arquivador PAR"

[^14]: Wikipédia em Chinês: Tang Feng (o mesmo que [^5]) + Múltiplas mídias citam verbatim consistentemente: 'Não importa se é agora, passado ou futuro, estou feliz que todos me chamem com um substantivo feminino'. A fonte original é o blog.elixus.org de 2005.

[^15]: [Ima Weekly: Entrevista com o Pai de Tang Feng (Set/2016)](https://www.businesstoday.com.tw/article/category/80407/post/201609010032/) — O pai, Tang Guanghua, diz verbatim 'Não há razão para não aceitar'.

[^16]: [Taiwan Woman NMTH: Tang Fern, a trans-gender cabinet member and the first digital commissioner in Taiwan](https://women.nmth.gov.tw/?p=20105) — Tang Fern verbatim "I am 'post-category'" + gender field on 2020 Cabinet Personnel Data filled as "None"

[^17]: [Marie Claire Taiwan: Audrey Tang, who was bullied in childhood, says: "Coping well with uncertainty"](https://www.marieclaire.com.tw/entertainment/story/52923/audrey-tang) — verbatim "Everything has flaws; the flaw is the entrance for light"

[^18]: [Artigo da Wikipédia em Chinês sobre Tang Fern (o mesmo que [^5])+](https://www.britannica.com/biography/Audrey-Tang) — Consulte os dados complementares no link original

[^19]: [Taiwan Guanghua Magazine: Citizen Hacker g0v, Zero Hour Government](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — Ponto de partida em 2012/10 + visualização do orçamento geral do governo central + lista de cofundadores

[^20]: [CCTV News PNN: Sunflower Student Movement Report (2014)](https://news.pts.org.tw/article/327548) — verbatim "All lines, cameras, and network live broadcasting equipment in the venue were set up by her, the citizen hacker 'Tang Fern'" + comentários de Tang Fern sobre a 'apresentação e cerimônia' no parlamento + transcrição feita por conta própria

[^21]: [Reporter: Creating a Space for Dialogue—Audrey Tang's Fantastic Journey](https://www.twreporter.org/a/g0v-audrey-tang) — verbatim April 2014, Cai Yuling joins g0v Hackathon + origin of vTaiwan

[^22]: [Democracy Technologies: Consensus Building in Taiwan](https://democracy-technologies.org/participation/consensus-building-in-taiwan/) — vTaiwan processou 26 tópicos entre 2015 e 2018 / 80% resultaram em ações governamentais substanciais / legalização de 7 condições do Uber

[^23]: [Liberty Times: Breaking Tradition, Tang Fern's 'Remote Work' on Wednesdays and Fridays (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859132) — Primeiro encontro com Lin Quan em 9/8 / Concordância em 15/8 / Nomeação em 1/10 / Três condições para o cargo ministerial

[^24]: [Liberty Times: Tang Fern's Remote Work, Lin Quan: This is Feasible (2016)](https://news.ltn.com.tw/news/politics/breakingnews/1859246) — Lin Quan verbatim "The Executive Yuan currently has no regulations for remote work... this is feasible"

[^25]: Artigo da Wikipédia em Chinês sobre Tang Fern (o mesmo que [^5]) — A jovem política mais jovem da história de Taiwan com 35 anos + a primeira figura política trans-gênero pública do mundo

[^26]: [pdis.nat.gov.tw Work Records and SayIt Public Transcript System](https://sayit.pdis.nat.gov.tw/) — Estrutura do grupo PDIS com 20 pessoas + metade civil e metade voluntário ministerial + 30 estagiários

[^27]: [Taipei Times: Audrey Tang named in "Top 100 Global Thinkers" (Jan 25, 2019)](https://www.taipeitimes.com/News/front/archives/2019/01/25/2003708586) — Inclusão no Top 100 Pensadores Globais da Foreign Policy (categoria de votação do leitor)

[^28]: [Rest of World: Audrey Tang on her "conservative-anarchist" vision for Taiwan's future (2020)](https://restofworld.org/2020/audrey-tang-the-conservative-anarchist/) — verbatim "Any top-down coercion, whether from capitalists or the state, is equally bad"

[^29]: [Conversations with Tyler Ep.106: Audrey Tang](https://conversationswithtyler.com/episodes/audrey-tang/) — verbatim "I'm working with the government; I'm not working for the government"

[^30]: [Lindsey on X: Real-time citation of ICFP 2020 Q&A](https://x.com/lindsey/status/1297886318114963456) — verbatim "In Taiwan we have this strange idea that broadband internet access is a human right"

[^31]: [SwissInfo: Liberdade de expressão: humor sobre rumores](https://www.swissinfo.ch/eng/politics/freedom-of-expression-humour-over-rumour-lessons-from-taiwan-in-digital-democracy/46592080) — Consulte o material suplementar no link original.

[^32]: [Site Oficial do Departamento de Desenvolvimento Digital: Ministros em exercício](https://moda.gov.tw/aboutus/ministers-since-2022/1527) — Período de mandato de Tang Feng, '27 de agosto de 2022 a 20 de maio de 2024', transcrito.

[^33]: [Liberty Times: Tang Feng liderará o Departamento Digital com 598 funcionários orçamentários](https://news.ltn.com.tw/news/politics/breakingnews/4021987) — Reportagem do Liberty Times.

[^34]: [Liberty Finance: De ministra de TI genial a palestrante independente, revisando as 3 principais realizações e controvérsias durante o mandato de Tang Feng](https://ec.ltn.com.tw/article/breakingnews/4677986) — Resiliência digital / OneWeb / Satélite SES / Revisão da Lei de Assinatura Eletrônica / Plataforma SMS de código curto 111

[^35]: [INSIDE: Um ano do Departamento de Desenvolvimento Digital! Detalhando as duas principais realizações e três controvérsias de Tang Feng](https://www.inside.com.tw/article/32615-Taiwan-moda-anniversary) — Padrão de transmissão unificado T-Road para 47 agências de Nível A + Colegas 'Em comparação com unidades anteriores, Tang Feng está mais disposta a delegar poder'.

[^36]: [Revista Yuanjian: O 'Departamento de Desenvolvimento Digital' liderado por Tang Feng completará 1 ano, mas críticos dizem que não há realizações](https://www.gvm.com.tw/article/105627) — Críticas de Liu Shih-fang / Wu Yi-ching.

[^37]: [ETtoday: Orçamento do Departamento de Desenvolvimento Digital é de 21,1 bilhões; Ko Wen-jei se surpreende: 'Em média, cada pessoa gasta 30 milhões. Que tipo de trabalho é este?' (30/08/2022)](https://www.ettoday.net/news/20220830/2327863.htm) — Questionamento de Ko Wen-jei.

[^38]: [Repórter: Governo aberto, como Tang Feng passou no teste de funcionário público?](https://www.twreporter.org/a/open-government-audrey-political-commissar-challenges) — PO 'Estou fazendo PO há 2 meses... não tenho certeza do quanto podemos intervir'.

[^39]: [Liberty Finance: De ministra de TI genial a palestrante independente (o mesmo que [^34])](https://ec.ltn.com.tw/article/breakingnews/4677986) — Reportagem do Liberty Times.

[^40]: [Plurality Institute: Lançamento do Livro Plurality](https://www.plurality.institute/blog-posts/book-launch-plurality-the-future-of-collaborative-technology-and-democracy-by-e-glen-weyl-audrey-tang-and-the-plurality-community) — Coescrito com Glen Weyl + Comunidade Plurality / Publicado em 16 de abril de 2024 / Liberado sob CC0.

[^41]: [Artigo da Wikipédia em Chinês sobre Tang Feng (o mesmo que [^5])+](https://cyberambassador.tw/) — Consulte o material suplementar no link original.

[^42]: [audreyt.org](https://audreyt.org/) — Consulte o material suplementar no link original.

[^43]: [Right Livelihood: Audrey Tang homenageada com o Prêmio Right Livelihood (2025)](https://rightlivelihood.org/news/taiwans-audrey-tang-honoured-with-right-livelihood-award-for-advancing-digital-democracy-and-social-trust/) — Citação transcrita + Trecho de Tang aceitando o discurso 'O ciberespaço é uma região de conflito' + [Reportagem da Focus Taiwan em inglês](https://focustaiwan.tw/society/202512030022)}

[^44]: cyberambassador.tw transcrito + Reafirmação filosófica do livro Plurality — "A superinteligência que procuramos já está aqui. Somos nós"
