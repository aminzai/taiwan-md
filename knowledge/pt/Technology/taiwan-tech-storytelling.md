---
title: 'Tecnologia de Taiwan conta histórias: chips de 100 pontos, microfones de 60 pontos'
description: 'Taiwan consegue produzir chips de 100 pontos, mas habituou-se a falar deles com o tom de um briefing de fornecedor. O mesmo chip: a Qualcomm transforma-o em mito, a MediaTek em tabela de especificações; a NVIDIA não fabrica nem uma única unidade, mas o seu lucro líquido é o dobro do da foundry. Esses 40 pontos de diferença, o mercado já fez as contas há muito tempo, e a fatura está impressa nas margens líquidas.'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'Tecnologia',
    'Storytelling',
    'Marca',
    'Semicondutores',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'Curva do Sorriso',
    'Subtexto',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-15
lastHumanReview: false
difficulty: 'beginner'
readingTime: 16
image: '/article-images/technology/tsmc-fab-14b-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg'
rationale: "{'why_this_hook': '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。', 'whats_excluded': '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。', 'where_it_hedges': '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。', 'whos_pushing_back': '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'}"
sporeLinks: []
curation: 'incubating'
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '6d762f5ac'
sourceContentHash: 'sha256:7e79f4d7834c55c1'
sourceBodyHash: 'sha256:e24305e511c42507'
translatedAt: '2026-09-12T19:57:16+08:00'
---

# Tecnologia de Taiwan conta histórias: chips de 100 pontos, microfones de 60 pontos

![Exterior da fábrica Fab 14B da TSMC no Parque Científico de Tainan, edifício industrial de vários andares estendendo-se sob céu azul, local físico da capacidade de fabrico avançado](/article-images/technology/tsmc-fab-14b-2025.webp)
_Fábrica Fab 14B da TSMC em Tainan, maio de 2025. Foto: 4300streetcar. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **Visão geral em 30 segundos:** Em junho de 2024, Jensen Huang no Ginásio da Universidade Nacional de Taiwan transformou o chip feito pela TSMC na narrativa de uma era; na mesma temporada, a apresentação da conferência de resultados da TSMC ainda era números financeiros, taxa de utilização de capacidade, perspectivas conservadoras. Ano fiscal 2026 da NVIDIA: receita de 215,9 mil milhões USD, lucro líquido de 120,1 mil milhões USD; a TSMC, que fabrica os seus chips, em 2025: receita de 122,4 mil milhões, lucro líquido de 55,1 mil milhões[^5][^6]. A empresa que desenha a história ganha o dobro de quem põe a mão na massa. Este artigo propõe-se a traduzir o que está por trás das falas.

2 de junho de 2024, Ginásio da Universidade Nacional de Taiwan. Jensen Huang sobe ao palco com aquela jaqueta de couro preta, fala por duas horas. A plateia parece um concerto: transmissão ao vivo, imprensa estrangeira, mar de gente com telemóveis no ar. Ele fala de Blackwell, fala de CUDA, transforma slide após slide na cerimónia de abertura de uma era[^19].

No mesmo ilha, a menos de cem quilómetros a sul, Hsinchu. A conferência de resultados da TSMC tem outra estética: números financeiros, taxa de utilização de capacidade, variação trimestral e anual, intervalo de perspectivas conservadoras. Os chips mais avançados do mundo saem daquela linha de produção, mas a apresentação inteira soa como aula de contabilidade.

O mesmo chip, duas formas de contar. A diferença de 40 pontos pelo meio, o mercado já fez as contas há muito.

A diferença entre estas duas cenas, os taiwaneses veem desde pequenos. Habituámo-nos: o produto é nosso, os aplausos são dos outros. Em feiras, o stand das empresas taiwanesas fala de custo, fala de yield, fala de prazo de entrega; o palco das marcas americanas fala de futuro, fala de missão, fala de mudar o mundo. O fosso entre os dois é exatamente esses quarenta pontos. Que cara têm esses quarenta pontos, este artigo traduz para você ver.

## O mesmo chip, duas narrativas

Outubro de 2024, dois lançamentos com menos de duas semanas de intervalo. A MediaTek em Shenzhen lança o Dimensity 9400, a Qualcomm no Maui, Havai, abre o Snapdragon Summit[^9][^10].

A [MediaTek](/pt/economy/mediatek/) é, por volume de expedição, um dos maiores fornecedores mundiais de chips para telemóveis, _market share_ de sete em cada dez chips para televisão[^4b]. O volume da Qualcomm perde para ela, mas receita e _brand premium_ ganham. Onde está a diferença? A Qualcomm vende o nome "Snapdragon": desde a nomeação em 2006 já lá vão quase vinte anos[^8], tem mascote próprio, festival tecnológico anual próprio. Nos lançamentos globais de _flagships_ aquela frase "Powered by Snapdragon" salta mais aos olhos que a própria marca do fabricante do telemóvel.

A MediaTek vende a tabela de especificações. O conteúdo do lançamento do Dimensity 9400 é processo, IPC, curva de eficiência energética, números todos sustentáveis, a imprensa de _reviews_ dá-lhe o título de "rei da eficiência"[^9]. Mas o consumidor só conhece o Snapdragon.

O trono do volume de expedição, a MediaTek na verdade já sentou nele. Terceiro trimestre de 2020, volume de chips para telemóvel da MediaTek ultrapassa a Qualcomm pela primeira vez, _market share_ cerca de 31%[^7]. Mas nos anos em que foi número um em volume, a maior fatia da receita da MediaTek vinha de telemóveis de gama média-baixa, o topo de gama continuava a ser da Qualcomm. Só no final de 2021, com o Dimensity 9000, a MediaTek conseguiu pela primeira vez colocar um chip _flagship_ nas tabelas comparativas dos _flagships_ Android das várias marcas. As especificações alcançaram, o lançamento continua a parecer briefing de fornecedor para cliente.

A MediaTek sabe deste problema. Estes anos começou a aprender: chip _flagship_ tem nome próprio, lançamento tem _opening show_, fabricantes parceiros também aceitam pôr "Dimensity" no _slogan_ publicitário. A direção está certa, só começou tarde uns dez anos. Construção de marca é maratona, quem começou cedo cada volta acumula juros compostos.

> 💡 **Sabia que**
> Snapdragon é _snapdragon flower_ (boca-de-leão), nome de uma flor; Dimensity (天璣) é a terceira estrela do Grande Carro[^8]. Uma vai buscar nome ao jardim, outra ao mapa estelar, ambas bonitas. A diferença: a Qualcomm cultivou esta flor até virar marca que desfila na _red carpet_, a luz da estrela Dimensity na maior parte do tempo ainda fica na tabela de especificações.

> 📝 **Nota do curador**
> A guerra de marcas na indústria de chips é cruelmente concreta: na hora de pagar, o consumidor reconhece Snapdragon ou Dimensity, ninguém pergunta qual chip a TSMC fabricou. A Qualcomm começou a cultivar a marca em 2006, a MediaTek só no final de 2019 pôs a série "Dimensity" no _flagship_. Vinte anos de juros compostos de narrativa, nenhuma tabela de especificações alcança.

## Como morreu o "Quietly Brilliant"

Recuemos mais um caso doloroso. 7 de abril de 2011, valor de mercado da HTC ultrapassa a Nokia, cerca de 33,8 mil milhões USD[^1]. Na altura a HTC detinha cerca de 20% do mercado de telemóveis, lado a lado com Samsung e Apple como três gigantes[^2].

Em escolhas tecnológicas, a HTC acertou quase tudo: 2008 lança o primeiro telemóvel Android do mundo, o G1[^3]. 2013 o One usa chassis unibody em liga de alumínio, câmara de _ultrapixel_ grande, câmara dupla, tudo pioneiro. Mas lembra-se do _slogan_ global da marca?

![Detalhe lateral do chassis do HTC One M7, design unibody em liga de alumínio, referência de artesanato da indústria em 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Foto: Asmoth, CC BY-SA 4.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant." Brilhante na discrição.

Na mesma época, o anúncio da Samsung "The Next Big Thing is already here" filmava diretamente fãs da Apple na fila à porta da loja, transformando quem fazia fila em parvos[^18]. A HTC punha a humildade como reivindicação de marca, a Samsung punha a Apple como antagonista principal. Dois anos e meio depois, a ação da HTC desabava de milhares para centenas[^2].

A HTC teve de facto uma hipótese de virar o jogo. O One (M7) de 2013 liderava a indústria em vários aspetos: chassis unibody em alumínio, câmara UltraPixel de píxeis grandes, altifalantes frontais duplos BoomSound. Esse ano levou "telemóvel do ano" em quase todos os _media_ principais, mas as vendas perderam por larga margem para o Samsung S4 contemporâneo. O lançamento do M7 falava de especificações, a Samsung falava de _lifestyle_, a Apple transformava o desbloqueio por impressão digital em mudança do mundo. Mesmo telemóvel da mesma geração, três narrativas, três destinos.

Olhando para trás as causas da derrota da HTC, claro que não é só um _slogan_. Mas a perda da narrativa foi o primeiro dominó a cair: quando o mercado começou a escolher lado pela história, quem não sabia contar história era o primeiro a ir para o cesto "prestes a ficar obsoleto". Engenheiros não acreditam nisto, acham que o produto fala por si. O produto de facto fala, só que a maioria dos consumidores não entende, nem quer ouvir.

![HTC Dream com teclado deslizante aberto, primeiro telemóvel Android do mundo G1 em 2008](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Foto: Marcus Sümnick, CC BY 3.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Nota do curador**
> "Quietly Brilliant" é em si uma tradução de subtexto: uma empresa escolher "discrição" como reivindicação global de marca equivale a entregar voluntariamente a soberania narrativa. Tabelas de especificações são esquecidas, histórias são lembradas. A HTC acertou em cada escolha técnica, perdeu em cada escolha narrativa.

## Curva do Sorriso: os taiwaneses desenharam o seu próprio mapa de posição há 30 anos

A tragédia da HTC não é caso isolado, tem gráfico por testemunha.

1992, Stan Shih em "Reconstruir a Acer" desenha a "Curva do Sorriso": I&D e marca nas duas pontas, valor mais alto, fabrico no meio, valor mais baixo[^4]. Os taiwaneses desenharam eles próprios este gráfico, e nos trinta anos seguintes a grande maioria da tecnologia de Taiwan ficou presa no ponto mais baixo da curva: a Foxconn a montar iPhone para a Apple, margem bruta crónica de dígitos únicos. A Apple leva a esmagadora maioria do lucro de toda a indústria de telemóveis, estimativas de pico acima de 80%[^11].

A [TSMC](/pt/economy/tsmc/) é a exceção. Apoiada na regra de "não desenhar os próprios produtos", transformou a própria _foundry_ no negócio que aperta as duas pontas: clientes não conseguem prescindir dela, ela não precisa de disputar a adoração do consumidor. Mas este negócio assenta na confiança B2B, não precisa de contar histórias ao grande público. A discrição da TSMC é estratégia comercial, efeito colateral: o sítio onde Taiwan melhor sabe fazer chips é precisamente o que menos precisa de treinar a contar histórias.

Também não é ninguém que virou para a ponta direita. A ASUS em 2006 cria a sub-marca ROG (Republic of Gamers), cultiva jogadores de _esports_ numa comunidade que reconhece a marca, o "olho da perdição" é uma das marcas mais reconhecidas globalmente em _hardware_ gaming[^15]. Mas ROG é minoria: a maioria das empresas taiwanesas nem na frente do produto ousa ampliar a própria marca.

A ponta direita da curva, Taiwan de facto já lá esteve. A Acer já foi top 3 global de marcas PC, as cinco letras Acer colaram-se nas portas de embarque de aeroportos pelo mundo inteiro. Mas a margem do PC era demasiado fina, fina a ponto de o _brand premium_ não aguentar o peso da ponta direita. A ROG prova que a ponta direita se alcança, basta escolher o campo de batalha certo.

O mais cruel da Curva do Sorriso é ser uma questão de escolha que ninguém refez há trinta anos. Trinta anos atrás Taiwan escolheu ficar no meio, porque era a resposta mais razoável na altura: sem capital, sem marca, sem mercado, _foundry_ era a única saída. O verdadeiramente perigoso é continuar a tratar a resposta razoável de trinta anos atrás como a resposta de hoje.

## A economia do _bluff_

Números são os mais honestos. Ano fiscal 2026 da NVIDIA (fevereiro 2025 a janeiro 2026) receita 215,9 mil milhões USD, lucro líquido 120,1 mil milhões USD[^5]. TSMC 2025 ano completo receita 122,4 mil milhões USD, lucro líquido 55,1 mil milhões USD[^6]. Os chips da NVIDIA quase todos entregues à TSMC para fabricar, ela vende ecossistema CUDA, vende a história "era da IA". Resultado: quem desenha a história fatura 1,8x quem põe a mão na massa, lucro líquido 2,2x.

Na mesma cadeia de abastecimento, subindo até ao consumidor, o gradiente é mais íngreme:

| Posição na cadeia         | Receita 2025          | Lucro líquido         | Margem líquida |
| ------------------------- | --------------------- | --------------------- | -------------- |
| Foxconn (monta iPhone)    | 8,1 biliões TWD       | 189,4 mil milhões TWD | 2,3%           |
| Apple (vende iPhone)      | 416,2 mil milhões USD | 112,0 mil milhões USD | 26,9%          |
| TSMC (faz chips)          | 122,4 mil milhões USD | 55,1 mil milhões USD  | 45,0%          |
| NVIDIA (conta a história) | 215,9 mil milhões USD | 120,1 mil milhões USD | 55,6%          |

_Dados: Foxconn e Apple ano fiscal 2025, NVIDIA FY2026 (até janeiro 2026), TSMC 2025, extraídos dos relatórios de cada empresa (verificados cruzadamente com secção financeira da Wikipédia)[^5][^6][^11]._

Quem monta ganha 2,3%, quem vende marca ganha 26,9%, quem faz fabrico avançado ganha 45%, quem transforma o chip em era ganha 55,6%. Valoração é desconto de fluxo de caixa futuro. Metade do futuro é engenharia a fazer, metade é narrativa a contar. A cultura padrão do Vale do Silício é _fake it till you make it_ (primeiro anuncia, depois arranja maneira de fazer). A cultura padrão de Taiwan é "ainda não fiz, não me atrevo a dizer". A distância entre as duas culturas não é moral, é de taxa de desconto: o mercado desconta pouco "história que se consegue contar", desconta muito "capacidade que não se consegue contar".

O mecanismo do _brand premium_ também é direto: o mesmo chip fabricado pela TSMC, cola-se a marca Snapdragon, o fabricante do telemóvel está disposto a pagar mais — esse extra é o _premium_. De onde vem o _premium_? Do aparato do lançamento, do Summit anual fixo, da expectativa habitual dos programadores de "o próximo Snapdragon certamente mais rápido". Estas coisas não entram na tabela de especificações, mas entram no relatório financeiro.

Há quem diga, é culpa do mercado, é Wall Street a fazer _hype_. Mas o mesmo mercado, para a TSMC não desconta: margem líquida de 45%, mais alta que a Apple. O mercado de facto está disposto a pagar pela capacidade de Taiwan, condição é que essa capacidade se consiga contar. Os clientes da TSMC contam-na por ela: cada lançamento da Apple, cada GTC da NVIDIA, são anúncios grátis da TSMC.

Perguntam, contar a história grande não vira mentira? A resposta de Jensen Huang está no relatório financeiro: cada frase que ele diz, por trás tem capacidade, yield e volume de expedição a segurar. A fronteira entre saber contar história e saber fazer _bluff_ está em: depois de contar, há ou não algo a receber. Taiwan tem o "algo", só costuma esquecer-se de contar.

> ⚠️ **Ponto de vista controverso**
> Uma corrente diz: os 60 pontos de narrativa de Taiwan são virtude: o negócio de _foundry_ vive de confiança, discrição é ativo; se a TSMC andasse sempre a fazer lançamentos, os clientes perdiam o sono. Outra corrente diz: o desconto narrativo transmite-se sistematicamente: valoração das empresas taiwanesas subestimada, salários a acompanhar subestimados, talento flui para empresas que sabem contar história, a próxima geração de produtos ainda menos sabe contar história. Em qual você acredita, nesse loop você habita. As duas teses estão ambas vivas, e nenhuma ainda ganhou.

## Taiwan não é que não saiba contar história

Quem conta bem, Taiwan tem de sobra.

Morris Chang em 2021 chamou à TSMC "Montanha Sagrada da Pátria" (護國神山)[^12]. Quatro caracteres, fazem Taiwan inteira ceder estrada, ceder água, ceder eletricidade à indústria de chips. É nomeação de topo na história do _marketing_: desde então cada notícia de seca ou racionamento de energia vira automaticamente anúncio de serviço público "a Montanha Sagrada precisa de você". Final de 2024, Morris Chang com noventa e poucos anos publica segundo volume da autobiografia, volta a _bestseller_[^13b].

A autobiografia virar _bestseller_ já explica o problema: um empresário de noventa e poucos anos escreve a própria vida em dois volumes, taiwaneses fazem fila para comprar. Taiwan gosta de ouvir histórias, gosta de comprar histórias, só que quando chega a sua vez de subir ao palco, as palavras encurtam.

Este lote de taiwaneses que sabem contar história, currículos têm ponto comum: Morris Chang 25 anos na Texas Instruments, Jensen Huang 30 anos a empreender no Vale do Silício, Lisa Su doutoramento no MIT. Nenhum treinou esta capacidade em Taiwan. O solo de Taiwan produz este tipo de gente, mas o local de trabalho de Taiwan não ensina isto. Escola ensina a desenhar o circuito certo, não ensina a contar o circuito como era.

Por isso o problema nunca foi talento. O problema é a estrutura industrial de Taiwan mandar quem sabe contar história para o estrangeiro, ou para a sala de reuniões da _foundry_. Para desatar este nó, não bastam uns departamentos de marketing de umas empresas, tem de se mudar da governação corporativa, estrutura salarial até à educação escolar.

![Morris Chang como representante líder na reunião de líderes económicos APEC 2021, foto oficial da Presidência](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang na reunião de líderes económicos APEC 2021. Foto: Wang Yu Ching / Presidência, CC BY 2.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Stan Shih ao desenhar a Curva do Sorriso também estava a vender conceito: um conceito fez a sua filosofia de gestão ser citada em escolas de negócios pelo mundo inteiro.

Jensen Huang nascido em Tainan, aos nove anos vai para os EUA[^13]. Lisa Su nascida em Tainan, aos três anos vai para os EUA[^14]. As duas pessoas que melhor sabem contar histórias de semicondutores no mundo, são semente de Taiwan, solo da América.

![Jensen Huang a palestrar no curso CS 153 de Stanford, com a icónica jaqueta de couro preta, gesticulando](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang no curso CS 153 de Stanford, abril de 2026. Foto: Anderseidesvik, CC BY-SA 4.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Nas _startups_ de Taiwan também há quem saiba contar. Gogoro fundada em 2011, 2015 na CES transforma estação de troca de baterias em "rede de energia", diz que é empresa de energia, de caminho vende motas. História tão bem contada que em 2022 consegue via SPAC entrar na Nasdaq, 2024 até a Castrol da BP investe 50 milhões USD[^16]. A Gogoro até hoje ainda procura fecho de ciclo comercial, mas o seu exemplo prova: saber contar história, pelo menos arranja bilhete para ser testada pelo mercado. Quem não sabe, nem porta entra.

A regra é clara: Taiwan não falta talento para contar histórias, falta ambiente que permita contar a história em grande. Gene de _foundry_ ensina "o cliente é protagonista", ambiente de contar história ensina "eu posso ser protagonista".

> 📝 **Nota do curador**
> O mais saboroso em "Montanha Sagrada da Pátria" quatro caracteres: quando Morris Chang os disse, estava a contar à sociedade taiwanesa uma história que precisava de apoio: precisa de eletricidade, precisa de água, precisa de terreno, precisa de talento. Saber contar história não é vaidade, é infraestrutura de política industrial. Taiwaneses perceberem estes quatro caracteres prova que a força narrativa dos taiwaneses não estragou, só não costuma virar para fora.

## Tabela de tradução de subtextos

Mesmo facto técnico, duas formas de dizer. Traduz as falas por trás das falas, a diferença vê-se sozinha.

| Quem fala                       | Fala de superfície                                                                                         | Tradução do subtexto                                                                                                                                                 |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conferência de resultados TSMC  | "Taxa de utilização de capacidade continua a recuperar, mantemos confiança no crescimento de longo prazo." | Só nós sabemos fazer os chips mais avançados do mundo, mas dizer isso não soa a engenheiro.                                                                          |
| Engenheiro taiwanês em briefing | "Esta tecnologia ainda tem algum espaço para otimização."                                                  | Já fizemos número um mundial, dou 20% de desconto primeiro, para não levar na cara.                                                                                  |
| _Pitch_ _startup_ EUA pág. 1    | "We are building the world's first AI-native platform to reinvent a $5 trillion industry."                 | Por enquanto a empresa tem três engenheiros e um PPT, mas o sonho não tem preço, dê o dinheiro primeiro.                                                             |
| _Pitch_ _startup_ Taiwan pág. 1 | "Membros da equipa formados em NTU/NTHU/NCTU, ex-MediaTek 8 anos, 12 patentes."                            | Não sabemos como contar visão, mostramos credenciais e currículo como colete à prova de bala.                                                                        |
| Jensen Huang                    | "The more you buy, the more you save."                                                                     | Esta placa é cara, mas se não compra, a conta da luz e a fila de capacidade de computação comem mais.                                                                |
| Qualcomm Snapdragon Summit      | "The era of on-device AI begins now."                                                                      | _Benchmarks_ esperam iPhone sair, primeiro faça você sentir que está a testemunhar a era.                                                                            |
| HTC anúncio 2010                | "Quietly Brilliant"                                                                                        | Somos _brilliant_, mas envergonhados de dizer alto.                                                                                                                  |
| Samsung anúncio 2011            | "The Next Big Thing is already here."                                                                      | Quem faz fila na loja da Apple parece parvo, venha comprar o meu.                                                                                                    |
| Elon Musk                       | "We will make life multiplanetary."                                                                        | Foguete ainda explode às vezes, mas a narrativa tem de descolar primeiro.                                                                                            |
| Morris Chang 2021               | "Semicondutores são a Montanha Sagrada da Pátria de Taiwan."                                               | Quatro caracteres, fazem Taiwan inteira ceder por chips. Um taiwanês que sabe contar história, uma frase vale um ano inteiro de slides de conferência de resultados. |

_Na tabela, as frases entre aspas da TSMC, engenheiro taiwanês, duas colunas de *startups* e Qualcomm são síntese indicativa de falas típicas, não citações textuais; as cinco colunas de Jensen Huang, HTC, Samsung, Musk, Morris Chang são *slogans* ou declarações públicas reais[^17][^18][^12]._

Traduzido até aqui você descobre: a diferença entre saber contar história e não saber, muitas vezes é só a ordem das palavras do mesmo facto.

Esta tabela não é para ridicularizar ninguém. Humildade na engenharia é muito útil: faz a colaboração andar, faz o controlo de qualidade não ousar facilitar. Mas humildade uma vez fora da sala de reuniões, vira cupão de desconto. O que Taiwan tem de aprender é deixar a humildade no laboratório, levar a confiança ao palco.

## De volta ao Ginásio da Universidade Nacional de Taiwan

Cada slide que Jensen Huang mostrou aquela noite, o local físico está nos _cleanrooms_ de Hsinchu, Taichung, Tainan. História contada, mundo inteiro paga. Gente do _cleanroom_ continua turnos, conferência de resultados continua conservadora.

Tecnologia de 100 pontos não vira automaticamente narrativa de 100 pontos. Esses 40 pontos precisam de alguém que suba ao palco, vista a jaqueta de couro como farda de guerra, conte o chip como era.

A próxima Montanha Sagrada da Pátria de Taiwan, talvez não seja um novo chip, seja uma nova história.

> ✦ A Qualcomm transformou um SoC numa marca que desfila na _red carpet_, Jensen Huang transformou o chip feito pela TSMC em era, Morris Chang com quatro caracteres fez Taiwan inteira ceder pela indústria de semicondutores. A tecnologia de Taiwan tem coisas de 100 pontos, falta quem esteja disposto a subir ao palco e contá-las como 100 pontos.

---

**Leitura complementar**:

- [Indústria de semicondutores: 50 anos de revolução de materiais da transferência tecnológica da RCA ao nitreto de gálio e encapsulamento quântico](/pt/technology/taiwan-semiconductor-industry) — Narrativa técnica completa da Montanha Sagrada, e aquela ligação "NVIDIA reserva capacidade CoWoS"
- [Empresa de Taiwan: TSMC](/pt/economy/tsmc) — Governança e estrutura financeira da empresa que pôs a discrição no modelo de negócio
- [Empresa de Taiwan: MediaTek](/pt/economy/mediatek) — Maior fabricante mundial de chips para telemóvel por volume, por que a narrativa ainda está a recuperar
- [Empresa de Taiwan: HTC](/pt/economy/htc-android-pioneer-vr-transformation) — História empresarial completa da morte do Quietly Brilliant
- [Jensen Huang](/pt/people/jensen-huang) — Nascido em Tainan, crescido na América, a pessoa que melhor sabe contar histórias de chips no mundo
- [NVIDIA em Taiwan](/pt/technology/nvidia-in-taiwan) — Aquela jaqueta de couro e a relação com a cadeia de abastecimento de Taiwan
- [Computex: três grandes feiras internacionais de computadores, duas acabaram, a que sobrou cresceu em Taipé](/pt/technology/computex) — Todos os anos em maio, gigantes globais de IA rodam por Taipé a usar a mesma retórica para contar histórias

## Fontes das imagens

Este artigo usa 5 imagens com licença CC, em _cache_ em `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Foto: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Foto: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Foto: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Foto: Wang Yu Ching / Presidência, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Foto: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Referências

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — 7 de abril de 2011 valor de mercado da HTC cerca de 33,8 mil milhões USD, ultrapassa Nokia

[^2]: [Wikipédia — HTC Corporation](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — 2011 _market share_ telemóvel cerca de 20%, valor de mercado rompe bilião, ação já esteve acima de mil TWD

[^3]: [Wikipédia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — 2008 primeiro telemóvel Android do mundo

[^4]: [Wikipédia — Curva do Sorriso](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Stan Shih 1992 em "Reconstruir a Acer" propõe

[^4b]: [Wikipédia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — Por volume de expedição um dos maiores fornecedores mundiais de SoC para telemóvel; _market share_ chip televisão cerca de sete em dez

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Comunicado oficial NVIDIA; FY2026 receita 215,9 mil milhões USD, lucro líquido 120,1 mil milhões USD (verificação cruzada secção financeira Wikipédia: https://en.wikipedia.org/wiki/Nvidia）

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Página oficial investidores TSMC; 2025 ano completo receita 122,42 mil milhões USD, lucro líquido 55,13 mil milhões USD (verificação cruzada secção financeira Wikipédia: https://en.wikipedia.org/wiki/TSMC）

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — Terceiro trimestre 2020 volume chips telemóvel MediaTek ultrapassa Qualcomm pela primeira vez, _market share_ cerca de 31%

[^8]: [Wikipédia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Plataforma SoC Snapdragon lançada novembro 2006; nome da marca vem de _snapdragon flower_, Dimensity vem da terceira estrela do Grande Carro (ambas segundo dados públicos da marca, aguarda ligação oficial)

[^9]: [MediaTek — Comunicado Dimensity 9400](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 lançado outubro 2024; imprensa de _reviews_ geralmente destaca desempenho de eficiência (descrição indutiva). Modelo de estreia ver [Wikipédia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200)

[^10]: [Wikipédia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 em Maui, Havai, lança Snapdragon 8 Elite (URL comunicado oficial expirado, baseia-se em Wikipédia como fonte secundária)

[^11]: [Wikipédia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — / [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Foxconn ano fiscal 2025 receita 8,103 biliões TWD, lucro líquido 189,35 mil milhões TWD (margem líquida cerca de 2,3%); Apple FY2025 receita 416,2 mil milhões USD, lucro líquido 112,0 mil milhões USD (margem líquida cerca de 26,9%). _Market share_ lucro iPhone pico acima de oito em dez: estimativas históricas Counterpoint (aguarda ligação fonte)

[^12]: [Wikipédia — Montanha Sagrada da Pátria](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Alcunha da TSMC (Escudo de Silício); "Semicondutores são a Montanha Sagrada da Pátria de Taiwan" é declaração pública de Morris Chang 2021 (fonte noticiosa aguarda ligação)

[^13]: [Wikipédia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — 1963 nascido em Tainan, 1972 (nove anos) emigra para EUA

[^13b]: Segundo volume autobiografia Morris Chang publicado novembro 2024, vendas nível _bestseller_ do ano (aguarda ligação fonte)

[^14]: [Wikipédia — Lisa Su](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — 1969 nascida em Tainan, três anos emigra para EUA com família

[^15]: [Wikipédia — ASUS](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — 2006 cria sub-marca "Republic of Gamers" (ROG)

[^16]: [Wikipédia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — 2011 fundada; 2015 CES lança Gogoro Smartscooter e rede de energia; 2022 fusão com Poema Global SPAC entra na Nasdaq; 2024 BP via Castrol anuncia investimento até 50 milhões USD

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — "The more you buy, the more you save" de Jensen Huang vem deste vídeo oficial

[^18]: "Quietly Brilliant" é _slogan_ global HTC desde 2009, "The Next Big Thing is Already Here" é _slogan_ anúncio Galaxy Samsung 2011, "We will make life multiplanetary" é declaração de missão SpaceX (três são textos comerciais públicos)

[^19]: [NVIDIA at Computex 2024 — Vídeo oficial keynote](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Keynote Computex de Jensen Huang a 2 de junho de 2024 no Ginásio da Universidade Nacional de Taiwan
