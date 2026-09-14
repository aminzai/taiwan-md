---
title: 'A Narrativa da Tecnologia de Taiwan: Chips de 100 Pontos, Microfones de 60'
description: 'Taiwan produz chips perfeitos (100 pontos), mas tende a apresentá-los com o tom de um relatório de fornecedor. A mesma peça é uma lenda para a Qualcomm e uma tabela de especificações para a MediaTek; a NVIDIA não fabrica nada, mas seu lucro líquido é o dobro do fabricante contratado. Essa diferença de 40 pontos já foi calculada pelo mercado, e a conta está impressa na margem de lucro.'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'tecnologia',
    'narrativa',
    'marca',
    'semicondutor',
    'tsmc',
    'nvidia',
    'mediatek',
    'qualcomm',
    'htc',
    'jensen huang',
    'morris chang',
    'curva do sorriso',
    'subtexto',
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
translatedAt: '2026-09-14T00:53:32+08:00'
---

# A Narrativa da Tecnologia de Taiwan: Chips de 100 Pontos, Microfones de 60

![Vista externa da fábrica TSMC Fab 14B no Parque Científico de Tainan, com múltiplos edifícios industriais se estendendo sob o céu azul, um local físico para a capacidade de processo avançado](/article-images/technology/tsmc-fab-14b-2025.webp)
_Fábrica TSMC em Tainan, Maio de 2025. Foto: 4300streetcar. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **Resumo em 30 segundos:** Em junho de 2024, Jensen Huang transformou os chips da TSMC em uma era no Ginásio Nacional de Taiwan; no mesmo trimestre, a apresentação de resultados da TSMC ainda apresentava números financeiros, taxa de utilização da capacidade e perspectivas conservadoras. A NVIDIA teve receita de US$ 215,9 bilhões e lucro líquido de US$ 120,1 bilhões em seu ano fiscal de 2026; a TSMC, que fabrica para ela, registrou uma receita de US$ 122,4 bilhões e um lucro líquido de US$ 55,1 bilhões em 2025[^5][^6]. A empresa que conta histórias ganha o dobro do valor daqueles que fazem. Este artigo tem como objetivo traduzir o subtexto por trás das palavras.

Em 2 de junho de 2024, no Ginásio Nacional de Taiwan. Jensen Huang subiu ao palco vestindo uma jaqueta de couro preta e falou por duas horas. A multidão abaixo era como em um show: transmissão ao vivo, mídia estrangeira, mar de pessoas segurando celulares. Ele falou sobre Blackwell, falou sobre CUDA, transformando slides em uma inauguração de era[^19].

Na mesma ilha, a menos de cem quilômetros ao sul, Hsinchu. A apresentação de resultados da TSMC tinha outra estética: números financeiros, taxa de utilização da capacidade, crescimento trimestral e um intervalo de perspectivas conservadoras. Os chips mais avançados do mundo estavam naquela linha de produção, mas toda a apresentação soava como uma aula de contabilidade.

O mesmo chip, duas formas de falar. A diferença de 40 pontos já foi calculada pelo mercado.

A distinção entre esses dois cenários é algo que os taiwaneses veem desde pequenos. Estamos acostumados: o produto é nosso, mas os aplausos são de outra pessoa. Em feiras, os estandes das empresas de Taiwan falam sobre custo, taxa de rendimento e prazo de entrega; os palcos das marcas americanas falam sobre futuro, missão e mudar o mundo. A lacuna entre eles é esses quarenta pontos. Este artigo vem para mostrar como são esses quarenta pontos.

## O Mesmo Chip, Duas Formas de Falar

Em outubro de 2024, dois eventos de lançamento ocorreram com menos de duas semanas de diferença. A MediaTek lançou o Dimensity 9400 em Shenzhen, e a Qualcomm realizou o Snapdragon Summit na ilha de Maui, Havaí[^9][^10].

A [MediaTek](/pt/economy/mediatek/) é um dos maiores fornecedores globais de chips para celulares medidos por volume de envio, com cerca de 70% do mercado de chips de TV[^4b]. A Qualcomm a supera em volume de envio, receita e prêmio de marca. Qual é a diferença? A Qualcomm vende o nome "Snapdragon": há quase vinte anos desde que foi nomeado em 2006[^8], com seu próprio mascote e sua própria feira tecnológica anual. O slogan "Powered by Snapdragon" nos lançamentos globais de smartphones é mais chamativo do que a marca do próprio celular.

A MediaTek vende a tabela de especificações. A apresentação do Dimensity 9400 abordou processo, IPC e curvas de eficiência energética; os números eram sólidos, e o setor de testes lhe deu o título de "Rei da Eficiência Energética"[^9]. Mas o consumidor só conhece Snapdragon.

A MediaTek já ocupou o trono do volume de envio. No terceiro trimestre de 2020, a MediaTek ultrapassou pela primeira vez a Qualcomm em volume de chips para celular, com cerca de 31% de participação[^7]. Mas nos anos em que liderou em volume, a maior parte da receita da MediaTek vinha de celulares de médio e baixo custo; o topo dos modelos _flagship_ era sempre da Qualcomm. Só no final de 2021, com o lançamento do Dimensity 9000, a MediaTek colocou pela primeira vez um chip _flagship_ em comparação com os principais aparelhos Android. As especificações estavam alinhadas, mas a apresentação ainda parecia um relatório de fornecedor para cliente.

A MediaTek sabe disso. Nos últimos anos, começou a aprender: o chip _flagship_ precisa ter seu próprio nome, e a apresentação precisa ter seu próprio show de abertura; os fabricantes parceiros também estão dispostos a colocar "Dimensity" em seus slogans publicitários. A direção está correta, mas o início foi mais de uma década atrasado. A construção de marca é uma maratona, e quem começa cedo ganha juros compostos a cada volta.

> 💡 **Você sabia?**
> Snapdragon é o nome em inglês para _snapdragon flower_, uma flor; Dimensity é a terceira estrela da Ursa Major[^8]. Uma empresa que escolhe um nome de jardim e outra que escolhe um nome de constelação são boas opções. A diferença é: a Qualcomm transformou essa flor em uma marca que anda no tapete vermelho, enquanto o brilho de Dimensity permanece, na maior parte do tempo, na tabela de especificações.

> 📝 **Nota do Curador**
> A guerra de marcas na indústria de chips é cruel e específica: quando o consumidor paga, ele reconhece Snapdragon ou Dimensity; ninguém pergunta qual chip a TSMC fabricou. A Qualcomm construiu sua marca em 2006, enquanto a MediaTek só colocou a série "Dimensity" nos _flagships_ no final de 2019. Vinte anos de juros compostos narrativos não podem ser alcançados por nenhuma tabela de especificações.

## Como Morreu o Brilhante Silencioso

Vamos voltar um caso mais doloroso. Em 7 de abril de 2011, a HTC ultrapassou a Nokia em valor de mercado, cerca de US$ 33,8 bilhões[^1]. Na época, a HTC detinha cerca de 20% do mercado de celulares, sendo uma das três gigantes ao lado da Samsung e Apple[^2].

Em termos de escolha tecnológica, a HTC estava quase correta: lançou o primeiro celular Android G1 em 2008[^3]. O One de 2013, com corpo unificado de liga de alumínio, câmera de grande pixel e dupla lente, também foi pioneiro. Mas você se lembra do seu slogan global?

![Close-up da lateral do HTC One M7, design monolítico de liga de alumínio, um padrão industrial no lançamento em 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Foto: Asmoth, CC BY-SA 4.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant." Brilhante em silêncio.

Na mesma época, o anúncio da Samsung, "The Next Big Thing is already here", mostrava diretamente fãs da Apple fazendo fila na loja, transformando-os em tolos[^18]. A HTC usou a humildade como afirmação de marca; a Samsung usou a Apple como vilã. Mais de dois anos depois, o preço das ações da HTC caiu de milhares para centenas[^2].

A HTC teve uma chance de se reerguer. O One (M7) de 2013 tinha muitas vantagens: corpo unificado de liga de alumínio, câmera UltraPixel de grande pixel e alto-falantes duplos BoomSound. Naquele ano, ela ganhou prêmios "Celular do Ano" de grandes mídias, mas vendeu muito menos que o Samsung S4 da época. A apresentação do M7 falava sobre especificações; a Samsung falava sobre estilo de vida; a Apple transformou o desbloqueio biométrico em uma mudança mundial. O mesmo modelo de celular, três formas de falar, três destinos.

Olhando para a derrota da HTC, é claro que não foi apenas um slogan. Mas a perda narrativa foi o primeiro dominó a cair: quando o mercado começou a escolher tendências com base em histórias, aqueles que não sabiam contar uma história foram colocados na cesta do "obsoleto". Os engenheiros não acreditavam nisso, achando que o produto falaria por si mesmo. O produto realmente fala, mas a maioria dos consumidores não entende e não quer ouvir.

![HTC Dream com teclado deslizante aberto, o primeiro celular Android do mundo em 2008](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Foto: Marcus Sümnick, CC BY 3.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Nota do Curador**
> "Quietly Brilliant" é uma tradução de subtexto: ao escolher a "modéstia" como afirmação global, a empresa entregou ativamente sua soberania narrativa. A tabela de especificações será esquecida; a história será lembrada. A HTC acertou em cada escolha técnica e perdeu em cada escolha narrativa.

## Curva do Sorriso: O Mapa da Situação dos Taiwaneses Há 30 Anos

A tragédia da HTC não é um caso isolado, ela tem um mapa para provar.

Em 1992, Eric Tung desenhou a "Curva do Sorriso" em _Reinventing Acer_: P&D e marca estão nas extremidades, com maior valor; manufatura está no meio, com menor valor[^4]. Os taiwaneses desenharam este mapa, e durante as trinta décadas seguintes, o grande corpo tecnológico de Taiwan ficou preso no ponto mais baixo da curva: Foxconn montando iPhones para a Apple, com margens anuais geralmente em um dígito. A pesquisa de mercado estima que a Apple leva a maior parte do lucro da indústria de celulares, superior a 80%[^11].

A [TSMC](/pt/economy/tsmc/) é a exceção. Ela transformou o _foundry_ (fabricação por terceiros) em um negócio que segura as duas extremidades, através do "não projetar seus próprios produtos": os clientes não podem dispensá-la, e ela não precisa competir com os clientes pelo culto do consumidor. Mas este negócio é construído na confiança B2B, sem necessidade de contar histórias ao público. A modéstia da TSMC é uma estratégia comercial; o efeito colateral é: o lugar onde Taiwan faz melhor semicondutores é precisamente o lugar que menos precisa praticar a arte de contar histórias.

Não há quem tenha chegado à extremidade direita. A Asus criou a submarca ROG (Republic of Gamers) em 2006, criando uma comunidade de _gamers_ reconhecida por sua marca; o olho do desperdício é um dos indicadores mais reconhecidos globalmente no hardware _gamer_[^15]. Mas o ROG é uma minoria: a maioria das marcas taiwanesas não se atreve a aumentar muito seu logotipo mesmo na frente do produto.

Taiwan também chegou à extremidade direita. A Acer já foi uma das três principais marcas de PC globais, e os cinco caracteres "Acer" estiveram em portões de embarque em aeroportos ao redor do mundo. Mas o lucro dos PCs era muito baixo, tão baixo que o prêmio da marca não conseguia suportar o peso da extremidade direita. O ROG provou que a extremidade direita pode ser alcançada, mas é preciso escolher o campo de batalha certo.

O mais cruel na Curva do Sorriso é que ela é uma questão de múltipla escolha que ninguém reavaliou em trinta anos. Trinta anos atrás, Taiwan escolheu ficar no meio porque era a resposta mais razoável da época: sem capital, sem marca, sem mercado; o _foundry_ era o único caminho para sobreviver. O perigo real é continuar tratando a resposta razoável de trinta anos atrás como a resposta de hoje.

## Economia do Exagero (Bluff)

Os números são os mais honestos. A NVIDIA teve uma receita de US$ 215,9 bilhões e um lucro líquido de US$ 120,1 bilhões em seu ano fiscal de 2026 (fevereiro de 2025 a janeiro de 2026)[^5]. A TSMC teve uma receita anual de US$ 122,4 bilhões e um lucro líquido de US$ 55,1 bilhões em 2025[^6]. Quase todos os chips da NVIDIA são fabricados pela TSMC; ela vende o ecossistema CUDA e a história do "Era da IA". Resultado: a empresa que conta histórias tem uma receita 1,8 vezes maior e um lucro líquido 2,2 vezes maior do que a empresa que faz.

Na mesma cadeia de suprimentos, subindo até o consumidor, o gradiente é mais íngreme:

| Posição na Cadeia            | Receita em 2025     | Lucro Líquido        | Margem Líquida |
| :--------------------------- | :------------------ | :------------------- | :------------- |
| Foxconn (montagem de iPhone) | 8,1 trilhões de NTD | 189,4 bilhões de NTD | 2.3%           |
| Apple (venda de iPhone)      | US$ 416,2 bilhões   | US$ 112 bilhões      | 26.9%          |
| TSMC (fabricação de chips)   | US$ 122,4 bilhões   | US$ 55,1 bilhões     | 45.0%          |
| NVIDIA (contar histórias)    | US$ 215,9 bilhões   | US$ 120,1 bilhões    | 55.6%          |

_Dados: Foxconn e Apple para o ano fiscal de 2025; NVIDIA para FY2026 (até janeiro de 2026); TSMC para 2025, baseados em relatórios financeiros das respectivas empresas (verificação cruzada com a coluna de finanças da Wikipédia)[^5][^6][^11]._

A montagem ganha 2.3%, quem vende a marca ganha 26.9%, quem faz o processo avançado ganha 45%, e quem transforma chips em uma era ganha 55.6%. A avaliação é um desconto do fluxo de caixa futuro. Metade do futuro é feito pela engenharia, metade é contado. A cultura implícita do Vale do Silício é _fake it till you make it_ (fingir até conseguir). A cultura implícita de Taiwan é "não ousar falar antes de fazer". A diferença entre as duas culturas não é uma diferença moral, mas uma diferença na taxa de desconto: o mercado dá menos desconto para a "história contada" e mais desconto para a "habilidade que não pode ser contada".

O mecanismo do prêmio da marca também é direto: o dinheiro extra que os fabricantes de celulares estão dispostos a pagar por um chip fabricado pela TSMC, se ele tiver o logotipo Snapdragon, é o prêmio. De onde vem esse prêmio? Do espetáculo dos lançamentos, do Summit anual fixo e da expectativa habitual dos desenvolvedores de que "o próximo Snapdragon será mais rápido". Essas coisas não entram na tabela de especificações, mas entram no relatório financeiro.

Alguns dirão que isso é um erro do mercado, uma especulação de Wall Street. Mas o mesmo mercado não dá desconto para a TSMC: sua margem líquida é de 45%, um degrau acima da Apple. O mercado está realmente disposto a pagar pela capacidade de Taiwan, contanto que essa capacidade possa ser contada. Os clientes da TSMC falam por ela: cada evento de lançamento da Apple, cada GTC da NVIDIA, é um anúncio gratuito para a TSMC.

Alguns perguntam se contar histórias em grande escala pode se tornar engano? A resposta de Jensen Huang está no relatório financeiro: cada palavra que ele diz é sustentada pela capacidade produtiva, taxa de rendimento e volume de envio. A fronteira entre contar histórias e exagerar é o que acontece depois que a história termina. Taiwan tem algo, mas frequentemente esquece de contá-lo.

> ⚠️ **Ponto de Vista Controverso**
> Um lado diz que a narrativa de 60 pontos de Taiwan é uma virtude: a vida do _foundry_ depende da confiança, e a modéstia é um ativo; se a TSMC fizesse apresentações o tempo todo, os clientes não dormiriam. O outro lado diz que o desconto narrativo se propaga sistemicamente: o valor das empresas taiwanesas é subestimado, os salários são subestimados, e o talento migra para as empresas que sabem contar histórias, fazendo com que a próxima geração de produtos seja ainda menos capaz de contar uma história. Você acredita em qual lado? E viverá em qual ciclo. Ambos os argumentos estão vivos e nenhum venceu.

## Taiwan Não Sabe Contar Histórias

Há quem conte bem as histórias em Taiwan.

Em 2021, Morris Chang chamou a TSMC de "Montanha Sagrada da Nação"[^12]. Quatro palavras que fizeram todo o povo de Taiwan ceder água, eletricidade e terra para a indústria de semicondutores. Este é um nome de nível máximo na história do marketing: desde então, cada notícia sobre escassez de água ou eletricidade se tornou automaticamente um anúncio beneficente de "a Montanha Sagrada precisa de você". No final de 2024, o empresário de mais de noventa anos publicou o segundo volume de suas memórias, que se tornou um _best-seller_[^13b].

O fato de as memórias terem sido um _best-seller_ diz tudo: um empresário de mais de noventa anos escreve sua vida em dois livros, e os taiwaneses fazem fila para comprar. Os taiwaneses adoram ouvir histórias e gostam de comprá-las, mas quando é a hora deles subirem ao palco, as palavras ficam curtas.

Este grupo de pessoas que sabem contar histórias tem um ponto em comum no currículo: Morris Chang trabalhou na Texas Instruments por vinte e cinco anos; Jensen Huang empreendeu no Vale do Silício por trinta anos; Su Zifeng fez seu doutorado no MIT. Ninguém desenvolveu essas habilidades em Taiwan. O solo de Taiwan pode produzir tais pessoas, mas o ambiente de trabalho taiwanês não ensina isso. A escola ensina a desenhar um circuito corretamente, mas não ensina a transformar um circuito em uma era.

Portanto, o problema nunca foi o talento. O problema é que a estrutura industrial de Taiwan enviou aqueles que sabem contar histórias para o exterior ou os colocou nas salas de reunião do _foundry_. Para desatar este nó, não basta depender apenas dos departamentos de marketing de algumas empresas; é preciso mudar desde a governança corporativa e a estrutura salarial até a educação escolar.

![Imagem de Jensen Huang participando da Cúpula Econômica APEC em 2021 como representante líder, foto oficial da presidência](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang na Cúpula Econômica APEC de 2021. Foto: Wang Yu Ching / Presidência, CC BY 2.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Eric Tung desenhou a Curva do Sorriso também para vender um conceito: um conceito que fez sua filosofia de gestão empresarial ser citada por escolas de negócios em todo o mundo.

Jensen Huang nasceu em Tainan e foi aos EUA aos nove anos[^13]. Su Zifeng nasceu em Tainan e foi aos EUA aos três anos[^14]. As duas pessoas mais habilidosas para contar histórias sobre semicondutores no mundo são do berço taiwanês, mas com terra americana.

![Jensen Huang dando uma palestra na aula CS 153 da Universidade de Stanford, vestindo sua jaqueta preta característica e gesticulando](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang palestrando em CS 153 da Universidade de Stanford, abril de 2026. Foto: Anderseidesvik, CC BY-SA 4.0. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Há quem conte bem nas _startups_ de Taiwan. A Gogoro foi fundada em 2011 e, em 2015, transformou as estações de troca de baterias no CES em uma "rede energética", dizendo ser uma empresa de energia e vendendo motos por acaso. A história levou à sua listagem na Nasdaq via SPAC em 2022, e a Castrol do BP investiu até US$ 50 milhões em 2024[^16]. A Gogoro ainda está procurando um ciclo comercial, mas seu exemplo mostra: quem sabe contar histórias pelo menos consegue um ingresso para ser testado pelo mercado. Quem não sabe, nem entra no portão.

A regra é clara: Taiwan não carece de talento para contar histórias; o que falta é o ambiente que permite amplificar a história. O DNA do _foundry_ ensina "o cliente é o protagonista"; o ambiente narrativo ensina "eu posso ser o protagonista".

> 📝 **Nota do Curador**
> O ponto mais interessante das quatro palavras "Montanha Sagrada da Nação" é: quando Morris Chang as disse, ele estava contando uma história para a sociedade taiwanesa que precisava de apoio: precisa de eletricidade, água, terra e talento. Saber contar histórias não é vaidade; é infraestrutura de política industrial. Os taiwaneses entendem essas quatro palavras, o que significa que sua capacidade narrativa não está ruim, apenas raramente usada externamente.

## Tabela de Tradução de Subtexto

A mesma informação técnica, duas formas de falar. Revele a história por trás das palavras e julgue a diferença.

| Quem Fala                                         | O Que É Dito Superficialmente                                                                            | Tradução do Subtexto                                                                                                                                                                                           |
| :------------------------------------------------ | :------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Apresentação da TSMC                              | "A taxa de utilização da capacidade está em ascensão, mantemos confiança no crescimento de longo prazo." | Só eu consigo fazer os chips mais avançados do mundo, mas falar isso não parece engenheiro.                                                                                                                    |
| Apresentação de Engenheiros Taiwaneses            | "Este projeto ainda tem espaço para otimização."                                                         | Já chegamos ao número um mundial, vamos dar um desconto antes que nos humilhem.                                                                                                                                |
| Primeira página do pitch de uma startup americana | "We are building the world's first AI-native platform to reinvent a $5 trillion industry."               | A empresa só tem três engenheiros e um PPT, mas o sonho é inestimável; por favor, dê dinheiro primeiro.                                                                                                        |
| Primeira página do pitch de uma startup taiwanesa | "A equipe se formou em Taiwan/Tsinghua, trabalhou na MediaTek por oito anos e possui 12 patentes."       | Não sabemos como falar sobre a visão, então usamos diplomas e currículos como armadura à prova de balas.                                                                                                       |
| Jensen Huang                                      | "The more you buy, the more you save."                                                                   | Este cartão é caro, mas se você não comprar, o consumo de eletricidade e poder computacional vão comer mais.                                                                                                   |
| Snapdragon Summit da Qualcomm                     | "The era of on-device AI begins now."                                                                    | Espere até lançar um iPhone para fazer _benchmarks_; primeiro, deixe parecer que você está testemunhando uma era.                                                                                              |
| Anúncio HTC 2010                                  | "Quietly Brilliant"                                                                                      | Somos brilhantes, mas desculpem, não podemos gritar.                                                                                                                                                           |
| Anúncio Samsung 2011                              | "The Next Big Thing is already here."                                                                    | Os fãs da Apple fazendo fila na loja parecem idiotas; venha comprar o meu.                                                                                                                                     |
| Elon Musk                                         | "We will make life multiplanetary."                                                                      | O foguete às vezes explode, mas a narrativa precisa decolar primeiro.                                                                                                                                          |
| Morris Chang 2021                                 | "O semicondutor é a Montanha Sagrada da Nação."                                                          | Quatro palavras que fizeram todo o povo de Taiwan ceder água, eletricidade e terra para os semicondutores. Uma frase de quem sabe contar histórias vale mais do que toda uma apresentação de resultados anual. |

_As citações em aspas nas colunas TSMC, Engenheiros Taiwaneses, Startups e Qualcomm são resumos típicos; as colunas Jensen Huang, HTC, Samsung e Musk são slogans ou falas públicas reais[^17][^18][^12]._

Ao traduzir, você perceberá que a diferença entre contar histórias bem e contar histórias mal é frequentemente apenas uma ordem de palavras da mesma verdade.

Esta tabela não serve para ridicularizar ninguém. A modéstia é muito útil na engenharia: ela permite que a cooperação continue e impede que o controle de qualidade seja frouxo. Mas, ao sair da sala de reuniões, a modéstia se torna um desconto. O que Taiwan precisa aprender é a manter a modéstia no laboratório e levar a confiança ao palco.

## De Volta ao Ginásio Nacional de Taiwan

Cada slide apresentado por Jensen Huang naquela noite estava fisicamente localizado em salas limpas em Hsinchu, Taichung e Tainan. A história foi contada; o mundo pagou a conta. Os ocupantes das salas limpas continuam em turno, os relatórios financeiros permanecem conservadores.

A tecnologia de 100 pontos não se transforma automaticamente em uma narrativa de 100 pontos. Esses 40 pontos precisam de alguém para subir ao palco, vestir a jaqueta como um uniforme de batalha e transformar o chip em uma era.

O próximo "Montanha Sagrada da Nação" de Taiwan pode não ser um novo chip, mas sim uma nova história.

> ✦ A Qualcomm transformou um SoC em uma marca que anda no tapete vermelho; Jensen Huang transformou os chips da TSMC em uma era; Morris Chang fez todo o povo de Taiwan ceder para os semicondutores com quatro palavras. A tecnologia de Taiwan tem coisas de 100 pontos, mas falta quem esteja disposto a subir ao palco e contá-las como 100 pontos.

---

**Leitura Complementar**:

- [Indústria de Semicondutores: Revolução de Materiais de 50 Anos da RCA para Nitreto de Gálio e Encapsulamento Quântico](/technology/半導體產業) — A narrativa técnica completa da Montanha Sagrada, e o vínculo com "NVIDIA monopoliza a capacidade CoWoS"
- [Empresa Taiwan: TSMC](/economy/台灣企業：台積電) — Governança e estrutura financeira desta empresa que escreveu a modéstia em seu modelo de negócios
- [Empresa Taiwan: MediaTek](/economy/台灣企業：聯發科技) — A fábrica de chips para celular com maior volume global, por que sua narrativa ainda está correndo atrás
- [Empresa Taiwan: Hon Hai](/economy/台灣企業：宏達電) — A história corporativa completa da morte do Brilhante Silencioso
- [Jensen Huang](/people/黃仁勳) — Nascido em Tainan, criado nos EUA, a pessoa que melhor conta histórias sobre chips no mundo
- [NVIDIA em Taiwan](/technology/NVIDIA在台灣) — O relacionamento entre aquela jaqueta de couro e a cadeia de suprimentos de Taiwan
- [Computex: Três Grandes Feiras de Computação Ganham Dois, A Terceira Fica em Taipé](/technology/Computex) — Em maio de cada ano, os gigantes da IA globais se revezam em Taipé contando histórias com o mesmo repertório.

## Fontes das Imagens

Este artigo utiliza 5 imagens licenciadas sob CC e armazenadas em `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Foto: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Foto: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Foto: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Foto: Wang Yu Ching / Presidência, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Foto: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Referências

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — Em 7 de abril de 2011, o valor de mercado da HTC era de cerca de US$ 33,8 bilhões, superando a Nokia.

[^2]: [Wikipédia — Hon Hai International](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — Em 2011, a participação de mercado em celulares era de cerca de 20%, com valor de mercado ultrapassando um trilhão de NTD e o preço das ações chegando a milhares.

[^3]: [Wikipédia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — O primeiro celular Android do mundo em 2008.

[^4]: [Wikipédia — Curva do Sorriso](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Proposta por Eric Tung em 1992 no livro _Reinventing Acer_.

[^4b]: [Wikipédia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — Um dos maiores fornecedores globais de SoC para celular medido por volume de envio; cerca de 70% do mercado de chips de TV.

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Comunicado oficial da NVIDIA; Receita de US$ 215,9 bilhões e lucro líquido de US$ 120,1 bilhões (verificação cruzada com a coluna de finanças da Wikipédia: https://en.wikipedia.org/wiki/Nvidia).

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Página oficial de investidores da TSMC; Receita anual de US$ 122,4 bilhões e lucro líquido de US$ 55,1 bilhões (verificação cruzada com a coluna de finanças da Wikipédia: https://en.wikipedia.org/wiki/TSMC).

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — No terceiro trimestre de 2020, a MediaTek ultrapassou pela primeira vez a Qualcomm em volume de chips para celular, com cerca de 31% de participação.

[^8]: [Wikipédia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — A plataforma SoC Snapdragon foi lançada em novembro de 2006; o nome da marca vem do nome da flor _snapdragon_ e a terceira estrela da Ursa Major (as duas formas de nomenclatura são dados públicos da marca, aguardando links oficiais).

[^9]: [MediaTek — Dimensity 9400 Press Release](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — O Dimensity 9400 foi lançado em outubro de 2024; o setor de testes geralmente destaca a eficiência energética (descrição conclusiva). Os modelos iniciais podem ser vistos em [Wikipédia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200).

[^10]: [Wikipédia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — O Snapdragon Summit 2024 ocorreu na ilha de Maui, Havaí, lançando o Snapdragon 8 Elite (o URL do comunicado oficial expirou, baseado em fontes secundárias da Wikipédia).

[^11]: [Wikipédia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — / [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Receita de 8,103 trilhões de NTD e lucro líquido de 189,35 bilhões de NTD da Foxconn no ano fiscal de 2025 (margem líquida de cerca de 2.3%); Receita de US$ 416,2 bilhões e lucro líquido de US$ 112 bilhões da Apple em FY2025 (margem líquida de cerca de 26.9%). O pico do lucro dos celulares da Apple foi superior a 80%: estimativas históricas da Counterpoint (aguardando links)

[^12]: [Wikipédia — Montanha Sagrada da Nação](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Apelido da TSMC (Escudo de Silício); "O semicondutor é a Montanha Sagrada da Nação" foi dito publicamente por Morris Chang em 2021 (aguardando link de notícia).

[^13]: [Wikipédia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Nascido em Tainan em 1963, imigrou para os EUA aos nove anos em 1972.

[^13b]: O segundo volume das memórias de Morris Chang foi publicado em novembro de 2024 e se tornou um _best-seller_ (aguardando link).

[^14]: [Wikipédia — Su Zifeng](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Nascida em Tainan em 1969, imigrou para os EUA aos três anos com a família.

[^15]: [Wikipédia — Asus](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Criou a submarca "Republic of Gamers" (ROG) em 2006.

[^16]: [Wikipédia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Fundada em 2011; lançou o Gogoro Smartscooter e a rede energética no CES em 2015; listada na Nasdaq com Poema Global SPAC em 2022; Castrol do BP anunciou um investimento de até US$ 50 milhões em 2024.

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — "The more you buy, the more you save" é da palestra oficial.

[^18]: "Quietly Brilliant" foi o slogan global da HTC a partir de 2009; "The Next Big Thing is Already Here" foi o slogan do Galaxy da Samsung em 2011; "We will make life multiplanetary" é uma declaração de missão da SpaceX (todos são textos comerciais públicos).

[^19]: [NVIDIA at Computex 2024 — Vídeo da palestra temática oficial](https://www.youtube.com/watch?v=pKXDVsWZmUU) — A palestra temática de Jensen Huang no Ginásio Nacional de Taiwan em 2 de junho de 2024.
