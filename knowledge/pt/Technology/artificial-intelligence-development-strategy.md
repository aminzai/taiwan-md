---
title: 'Desenvolvimento de Inteligência Artificial em Taiwan e Estratégias Futuras: O ingresso no hardware foi conquistado, qual é a próxima batalha'
description: 'Em 8 de outubro de 2024, o Nobel de Física foi concedido a Hopfield e Hinton; no dia seguinte, o de Química foi dado aos três responsáveis pelo AlphaFold. Em 29 de maio do mesmo ano, Jensen Huang comeu omelete de ostras com Morris Chang na feira noturna de Ningxia em Taipei. Taiwan fabrica 90% dos servidores de IA globais e 72% das wafers avançadas, mas esteve ausente nas soluções para o problema da rede neural de 42 anos e do dobramento de proteínas de 50 anos. De Taiwan AI Labs, fundada por Du Yijin do PTT, ao modelo LLM em chinês tradicional TAIDE apoiado pelo Conselho Nacional de Ciência e Tecnologia, esta ilha é apenas uma fábrica de fabricação?'
date: 2026-03-19
category: 'Technology'
tags:
  [
    'inteligência artificial',
    'IA',
    'semicondutores',
    'política tecnológica',
    'transformação digital',
    'Prêmio Nobel',
    'AlphaFold',
  ]
subcategory: '人工智慧'
author: 'Taiwan.md'
difficulty: 'advanced'
readingTime: 18
featured: true
lastVerified: 2026-05-19
lastHumanReview: true
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
translatedFrom: 'Technology/台灣人工智慧發展與未來策略.md'
sourceCommitSha: 'b70d6d8c4'
sourceContentHash: 'sha256:36a555145d356c00'
sourceBodyHash: 'sha256:9929570d1f524d80'
translatedAt: '2026-10-03T20:15:37.337958+00:00'
---

# Desenvolvimento de Inteligência Artificial em Taiwan e Estratégia Futura: O Passe de Entrada do Hardware Foi Conquistado, Qual é a Próxima Batalha?

> **Resumo de 30 segundos:** Em 8 de outubro de 2024, o Prêmio Nobel de Física foi concedido aos físicos que escreveram a Rede Hopfield e aos cientistas cognitivos que desenvolveram o _backpropagation_ [^N1]. No dia seguinte, 9 de outubro, o Prêmio Nobel de Química foi dado a três pesquisadores que resolveram o enigma do dobramento proteico por meio da IA [^N2]. Em 29 de maio do mesmo ano, Jensen Huang, CEO da NVIDIA, apareceu no mercado noturno Ningxia em Taipé jantando _o-a-jie_ com Morris Chang, Lin Po-li e Tsai Li-hing. A TSMC conquistou 72% da receita global do mercado de fundição de wafers, e a Foxconn, Quanta e Wistron produziram coletivamente noventa por cento dos servidores de IA globais. No entanto, neste ritual científico que ocorreu em dois dias e validou 42 anos de história das redes neurais, nenhum nome era de Taiwan. Desde o Laboratório de Inteligência Artificial de Taiwan, fundado por Du Yijin da PTT, até o modelo de linguagem grande TAIDE, apoiado pelo governo em mandarim tradicional, uma aposta está em andamento: passar de "fabricar IA" para "ser IA".

## A Confirmação de 42 Anos: Os Dois Prêmios Nobel em Dias Consecutivos em 2024

Em 8 de outubro de 2024, Estocolmo. A Academia Real da Ciência Sueca anunciou que o Prêmio Nobel de Física de 2024 seria concedido a dois cientistas de IA: John J. Hopfield, professor honorário de Princeton, de 91 anos, e Geoffrey Hinton, de 76 anos, que havia deixado o Google cinco meses antes. O prêmio, no valor de 11 milhões de coroas suecas, foi dividido igualmente entre os dois[^N1].

O comitê avaliador deu como motivo "descobertas e invenções fundamentais que possibilitam o aprendizado de máquina com redes neurais artificiais"[^N1]. Esta é a primeira vez na história do Prêmio Nobel de Física em que o prêmio foi diretamente concedido ao campo das redes neurais.

No dia seguinte, 9 de outubro, veio o prêmio de Química. Os três laureados foram David Baker da Universidade de Washington, juntamente com Demis Hassabis e John Jumper do DeepMind. Baker recebeu metade do prêmio, enquanto Hassabis e Jumper dividiram a outra metade[^N2]. O motivo do prêmio foi dividido em duas partes: "design computacional de proteínas" para Baker, e "previsão da estrutura proteica" para Hassabis e Jumper.

Dois dias, dois Nobéis, ambos relacionados à IA. Isso não tem precedentes na história dos prêmios Nobel.

Ao compararmos a linha do tempo: quando Hopfield publicou o artigo intitulado _Neural networks and physical systems with emergent collective computational abilities_ em 1982 no _Proceedings of the National Academy of Sciences (PNAS)_, ele acabara de transicionar da física do estado sólido para as neurociências[^N3]. De 1982 a 2024, foram 42 anos. O artigo de Hinton e Rumelhart em 1986, que tornou o algoritmo _backpropagation_ uma ferramenta utilizável[^N4], levou 38 anos do seu lançamento até a premiação. Já o AlphaFold, desde sua primeira aparição no CASP13 em 2018 até receber o Nobel em 2024, demorou apenas 6 anos.

No fim das contas, os laureados destes dois dias não são o ChatGPT, mas sim artigos de trinta ou quarenta anos atrás que ninguém entendia. A diferença temporal entre a pesquisa fundamental e a aplicação industrial é sempre essa.

![Foto oficial do Geoffrey E. Hinton durante a Semana Nobel em Estocolmo em 8 de dezembro de 2024, vestindo um terno escuro, com cabelos brancos, olhando para a câmera com expressão calma](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton, laureado do Prêmio Nobel de Física de 2024, Semana Nobel em Estocolmo. Foto: Arthur Petron, 8 de dezembro de 2024. [CC BY-SA 4.0 via Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Geoffrey%5FE.%5FHinton,%5F2024%5FNobel%5FPrize%5FLaureate%5Fin%5FPhysics%5F(3x4%5Fcropped).jpg>)._

## O Jantar de Bilhões no Mercado Noturno de Ningxia

Na noite do dia 29 de maio de 2024, antes da realização da Computex, um grupo incomum de clientes apareceu no mercado noturno de Ningxia em Taipé. Jensen Huang, CEO da NVIDIA, estava com Morris Chang, cofundador da TSMC, Lin Byu-li, presidente da Quanta Computer, e Eric Tsai, CEO da MediaTek, apertados em frente a uma barraca para comer _oaijian_ (panqueca de ostras) [^1]. Os transeuntes reconheceram Jensen Huang e ele foi instantaneamente cercado por fãs e repórteres, o cenário era digno de um evento de celebridade.

O valor de mercado deste jantar somava mais de bilhões de dólares. Mas a verdadeira história não estava à mesa, mas sim na cadeia industrial por trás dela: as empresas representadas por essas pessoas sustentam a base física do processamento global de IA. Durante sua viagem a Taiwan, Jensen Huang afirmou publicamente: "Taiwan é um dos países mais importantes do mundo" [^2]. Isso não era uma formalidade. Sem Taiwan, o alicerce de hardware da revolução da IA não existiria.

Jensen Huang nasceu em Taipé em 1963 e passou a infância em Tainan, emigrando para os Estados Unidos aos nove anos [^3]. A NVIDIA, que ele cofundou em 1993, é hoje um sinônimo de chips de IA. Cada GPU avançada projetada pela NVIDIA, desde as A100 e H100 usadas para treinar o ChatGPT até a mais recente série Blackwell, é fabricada pela TSMC [^4].

Os dois prêmios Nobel anunciados em Estocolmo quatro meses depois não tinham nenhum nome relacionado a este jantar. Essa disparidade não foi um acaso; é um fato estrutural.

## Hardware: Uma Ilha Sustentando Toda a Revolução da IA

A posição de Taiwan na cadeia de suprimentos de hardware de IA é um eufemismo, para dizer o mínimo.

No setor de fabricação de chips, em 2025, a TSMC detinha uma fatia de mercado global de fundição de wafers de 72%[^5]. Em processos avançados abaixo de 7 nanômetros, a participação da TSMC ultrapassava noventa por cento. A NVIDIA tem cerca de 86% do mercado de GPUs para IA, e quase todas essas GPUs são fabricadas pela TSMC[^6]. A vasta maioria da capacidade computacional usada no mundo para treinar e executar modelos de IA nasceu em salas limpas de Taiwan.

Após a fabricação dos chips, eles precisam ser montados em servidores para entrar nos data centers. Este setor também é dominado por Taiwan. Os três grandes fabricantes ODM — Foxconn, Quanta e Wistron — produziram cerca de 90% dos servidores de IA do mundo[^7]. Em 2025, a receita anual dessas três empresas ultrapassou individualmente NT$1 trilhão (cerca de US$32 bilhões), sendo que a receita de servidores de IA superou pela primeira vez os produtos de eletrônicos de consumo no segundo trimestre[^8].

O desempenho dos chips de IA não depende apenas da miniaturização do processo, mas também da tecnologia de empacotamento. A tecnologia avançada CoWoS (Chip on Wafer on Substrate) da TSMC é crucial para que as GPUs de ponta da NVIDIA atinjam seus objetivos de desempenho. Em 2026, a demanda estimada apenas pela NVIDIA por wafers CoWoS atingiu 595 mil unidades, representando 60% da demanda global[^9].

A Foxconn também colaborou com a NVIDIA e o governo taiwanês para construir um supercomputador de nível de 100 megawatts (MW) em Kaohsiung, utilizando a arquitetura mais recente Blackwell da NVIDIA[^10]. Taiwan está evoluindo de "o local onde os chips de IA são fabricados" para "o local onde a IA é executada".

![Vista da fábrica Fab 5 do Parque Científico de Hsinchu (TSMC), cena dos anos 2010, o local físico da fabricação de wafers semicondutores](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Fábrica Fab 5 da TSMC em Hsinchu, um local físico para a fabricação de chips de IA. Foto: Wikimedia Commons via [arquivo Fab 5 da TSMC](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

A questão é: o hardware ganhou o ingresso; onde será a próxima batalha?

> 📝 **Nota do Curador**
>
> A narrativa comum diz que "a montanha sagrada de Taiwan sustenta a revolução da IA". Embora essa afirmação seja conveniente narrativamente, ela inverte metade da causalidade. Não é a TSMC que cresceu por causa da revolução da IA; é a revolução da IA que precisava das GPUs e, portanto, escolheu a TSMC. A verdadeira tensão reside em: quando as GPUs se tornam mercadorias, para onde migra o valor na próxima fase? As respostas dadas pelos dois prêmios Nobel de 2024 são os próprios modelos — o papel de 12 páginas escrito por Hopfield, aquela noite em que Hinton e seu aluno Krizhevsky reduziram a taxa de erro de reconhecimento de imagens do ImageNet de 26,2% para 15,3% com AlexNet em 2012[^N5], e aquela tarde em que o grupo de Hassabis fez o AlphaFold atingir um GDT médio de 92,4 no CASP14.

## Hopfield em 1982: Um modelo de memória criado por um físico

Em 1982, John Hopfield, um físico do estado sólido de Princeton, publicou um artigo de apenas 12 páginas intitulado 《Neural networks and physical systems with emergent collective computational abilities》[^N3], publicado na _Proceedings of the National Academy of Sciences_ (Anais da Academia Nacional das Ciências dos EUA) [^N3].

O que ele fez foi essencialmente traduzir a "memória" para a física.

Na física, existe algo chamado vidro de spin (_spin glass_): um conjunto de átomos magnéticos, cada um com sua própria direção de spin, interagindo entre si, e o sistema inteiro tende a encontrar um ponto de energia mínima por conta própria. Hopfield aplicou esse conceito aos neurônios: ele imaginou os neurônios como spins e as forças de conexão como interações; assim, toda a rede converge espontaneamente para um estado estável de "mínimo de energia" (_energy minimum_) [^N3]. Cada mínimo de energia é uma memória armazenada.

A elegância deste modelo reside no fato de que ele transforma a memória em algo descritível pela linguagem da física. Dado um rastro incompleto, a rede encontra por conta própria o ponto de mínimo de energia mais próximo e completa toda a memória. Este é o ancestral matemático do que a IA generativa faz hoje.

Em 1982, Taiwan estava apenas começando sua indústria eletrônica, antes mesmo da fundação da TSMC. Tsung-mo Chiang só fundaria a empresa que se tornaria um "pilar nacional" 42 anos depois em 1987. O artigo de Hopfield acumulou mais de vinte e sete mil citações no Google Scholar até 2026 [^N6].

O mais interessante é o que Hopfield disse posteriormente. Ele dedicou sua vida à física do estado sólido em Princeton, sendo visto por seus colegas da época como um "passatempo" ao migrar para a neurociência. Quando foi anunciado o prêmio Nobel em 2024, aos 91 anos, ele relatou em uma entrevista telefônica com a Academia Real da Suécia que estava preocupado com "a direção em que ninguém entende ou controla a IA" [^N7].

O homem que escreveu os fundamentos matemáticos de toda a IA moderna alertou para o perigo no dia em que recebeu o prêmio.

![Retrato de John J. Hopfield durante a entrevista do Nobel em Estocolmo, 8 de dezembro de 2024, vestindo um terno escuro e com cabelos brancos, expressão séria](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield, laureado com o Prêmio Nobel de Física em 2024, Semana do Nobel em Estocolmo. Foto: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

---

## Hinton: O artigo de 1986 e o aviso após deixar o Google em 2023

Geoffrey Hinton, nascido em Wimbledon, Londres, em 1947, é outra pessoa que demorou 38 anos para ser reconhecida pela história[^N8].

Em 1986, Hinton publicou um artigo sobre _backpropagation_ na revista _Nature_, juntamente com David Rumelhart e Ronald Williams[^N4]. Este algoritmo significa que, quando uma rede neural comete um erro, o sinal de erro pode ser retropropagado para cada camada, ajustando os pesos das conexões camada por camada. É assim que todos os modelos de aprendizado profundo são treinados hoje.

Embora este algoritmo tenha sido concebido em 1986, ele só explodiu quando três coisas estavam prontas: poder computacional acessível, uma quantidade suficiente de dados e pessoas dispostas a acreditar nesse caminho. As duas primeiras coisas ficaram prontas no início da década de 2010; os representantes da terceira coisa são Hinton e seus dois alunos, Alex Krizhevsky e Ilya Sutskever. Em 2012, o AlexNet, uma rede neural convolucional treinada com GPU, conquistou a taxa de erro top-5 em 15,3% na competição ImageNet, superando amplamente o segundo lugar com 26,2%[^N5]. Foi nesse momento que toda a indústria passou a acreditar que _backpropagation_ realmente funcionava.

Em março de 2013, o Google adquiriu a pequena empresa de Hinton, DNNresearch, por US$ 44 milhões, integrando-o à sua equipe aos 65 anos[^N8]. Durante a década seguinte, ele foi um dos acadêmicos de IA mais proeminentes do Vale do Silício.

Então, em 1º de maio de 2023, o _The New York Times_ publicou uma entrevista: Hinton havia deixado o Google.

O motivo de sua saída não era a aposentadoria. Na entrevista, ele disse que queria "poder discutir os riscos da IA livremente, sem ter que se preocupar com como isso afetaria o Google"[^N9]. Os avisos que ele deu incluíam: sistemas de IA podem se tornar muito mais inteligentes do que os humanos rapidamente, podendo ser usados por pessoas mal-intencionadas para fins nocivos, e "é difícil saber o que pode ser feito para impedir isso"[^N9]. Ele até disse ter "algum arrependimento" sobre sua vida profissional[^N9].

Quando recebeu o Prêmio Nobel de Física em 2024, ele reiterou um aviso durante uma entrevista telefônica: cuidado com a possibilidade de a IA sair do controle[^N10].

Os criadores dos algoritmos de treinamento de aprendizado profundo e os criadores dos modelos de memória se apresentaram simultaneamente no palco da Academia Sueca das Ciências em 10 de outubro de 2024, alertando a todos sobre o perigo que essa tecnologia poderia representar. A cena lembrava a expressão de Oppenheimer ao ver as nuvens de cogumelo surgirem no deserto do Novo México em 1945.

Dois meses depois, em 8 de dezembro de 2024, Hinton proferiu seu discurso do Prêmio Nobel na Aula Magna da Universidade de Estocolmo. O tema foi 〈Máquinas de Boltzmann〉—seu trabalho inicial que integrava a distribuição probabilística termodinâmica em redes neurais, seguindo a linhagem de Hopfield. Ao ouvir, ficou claro que o artigo de _backpropagation_ de 1986 não era uma ideia isolada, mas sim um conjunto completo de ideias geradas na intersecção entre a física e as ciências cognitivas dos anos 80:

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Canal oficial da Royal Swedish Academy of Sciences: O discurso do Prêmio Nobel de Física de Geoffrey Hinton em 8 de dezembro de 2024, "Máquinas de Boltzmann". De quando ele e Sejnowski escreveram as Máquinas de Boltzmann nos anos 1980, passando por *backpropagation* até os LLMs atuais—quatro décadas. Nos últimos 5 minutos, ele reiterou sua preocupação com os riscos da IA, desta vez no palco do Nobel._

## De PTT a Laboratório de IA: As Duas Jornadas Empreendedoras de Du Yijin

Voltando à ilha Taiwan. Na mesma época em que Hopfield escreveu o modelo de memória, Taiwan estava apenas começando a ter cursos de ciência da computação.

Em 1995, Du Yijin, um estudante do segundo ano do Departamento de Ciência da Computação da Universidade Nacional de Taiwan (NTU), montou o [PTT](/pt/technology/ptt-bulletin-board-system/) em seu dormitório usando um computador 486 e software de código aberto, que mais tarde se tornou o maior quadro de avisos eletrônicos de Taiwan. Trinta anos depois, o PTT ainda tem centenas de milhares de usuários online diariamente, sendo uma relíquia da cultura de internet de Taiwan.

Du Yijin trabalhou na Microsoft, participando do desenvolvimento do assistente de voz Cortana. Em abril de 2017, ele abandonou os altos salários do Vale do Silício para retornar a Taiwan e fundar o "Taiwan AI Labs" (Laboratório de Inteligência Artificial de Taiwan), que foi a primeira organização de pesquisa de IA aberta e sem fins lucrativos da Ásia[^11].

Sua motivação era direta: Taiwan possuía talentos de software de classe mundial, mas esses talentos iam para o Vale do Silício. Ele queria criar uma plataforma onde as pessoas que quisessem voltar ou permanecer pudessem fazer pesquisa em IA.

O produto mais conhecido do Taiwan AI Labs é o "Transcrição Yating", um sistema de reconhecimento de voz otimizado para mandarim tradicional e sotaque taiwanês. Durante a pandemia de COVID-19, o laboratório também desenvolveu ferramentas de detecção de desinformação e IA médica federada[^12]. O ponto comum desses projetos era: eles resolviam problemas locais de Taiwan, utilizando dados locais, em vez de traduzir modelos americanos para uso.

A história de Du Yijin, de PTT aos Labs de IA, é, em certa medida, um microcosmo do desenvolvimento de software de Taiwan: não faltava capacidade técnica, mas sim o ecossistema necessário para reter os talentos.

> 💡 **Você sabia?**
>
> No ano em que Hinton publicou a retropropagação (backpropagation) em 1986, o PIB de Taiwan era de cerca de US$ 77,9 bilhões e o PIB per capita era de cerca de US$ 4.007; o Parque Científico de Hsinchu tinha acabado de operar por seis anos[^N11]. Três eventos ocorreram no mesmo planeta ao mesmo tempo, mas essa linha histórica só se cruzaria com o conjunto de dados ImageNet 26 anos depois. A escala de tempo da pesquisa básica é sempre maior do que a narrativa industrial percebe.

## AlphaFold: A Outra Metade do Enigma de Dobramento Proteico de 50 Anos Premiada com o Nobel

A história do Prêmio Nobel de Química de 2024 começa com um problema surgido em 1972.

Naquele ano, quando o bioquímico americano Christian Anfinsen recebeu o Prêmio Nobel de Química, ele propôs uma hipótese: a estrutura tridimensional das proteínas é determinada inteiramente pela sua sequência de aminoácidos[^N12]. Se essa hipótese fosse verdadeira, teoricamente, bastaria observar uma sequência de aminoácidos para calcular a estrutura 3D correspondente. No entanto, esse "deveria" persistiu por meio século sem ser alcançado. O dobramento proteico é conhecido como um grande desafio. A comunidade científica realiza o concurso CASP a cada dois anos, onde os resultados preditos são comparados com as estruturas experimentais; desde 1994, foram realizadas 13 edições, e ninguém conseguiu romper essa barreira[^N13].

Até o CASP13 em 2018, quando o AlphaFold da DeepMind participou e venceu com a primeira geração, mas cuja precisão ainda não era considerada prática. O verdadeiro ponto de virada foi o CASP14, realizado em 30 de novembro de 2020: o AlphaFold 2 obteve uma pontuação média GDT de 92.4[^N13]. Um GDT de 92.4 significa que mais da metade das previsões tinham um desvio na posição atômica menor que um Ångstrom em relação aos valores experimentais, atingindo o nível de resolução experimental. John Moult, organizador do CASP, declarou no dia: "Em grande parte, este problema foi resolvido"[^N13].

O problema não solucionado por 50 anos foi resolvido por uma equipe de pesquisa em Londres em seis anos.

Os acontecimentos se aceleraram ainda mais. Em julho de 2021, o código-fonte do AlphaFold 2 foi liberado; no mesmo ano, a DeepMind colaborou com o European Molecular Biology Laboratory (EMBL-EBI) para criar um banco de dados público das estruturas proteicas preditas pelo AlphaFold. Em julho de 2022, este banco de dados cobriu 1 milhão de espécies e cerca de 200 milhões de estruturas proteicas, liberando gratuitamente os modelos 3D da quase totalidade das proteínas conhecidas na Terra[^N14].

Em 8 de maio de 2024, a DeepMind publicou o AlphaFold 3 em _Nature_, expandindo sua capacidade preditiva de uma única proteína para as interações entre proteínas e DNA, RNA, ligantes e íons[^N15]. De desde o desenvolvimento de novos medicamentos ao design de vacinas e engenharia enzimática, todos os campos que dependem do conhecimento de como as moléculas se encaixam foram reescritos por esta ferramenta.

Demis Hassabis, criador do AlphaFold, não é um bioquímico tradicional. Ele começou a jogar xadrez aos quatro anos e ganhou o título de mestre aos 13; aos 17 anos, ele co-desenvolveu o jogo de simulação _Theme Park_ com Peter Molyneux, vendendo milhões de cópias[^N16]. Em 2010, ele fundou a DeepMind em Londres com Shane Legg e Mustafa Suleyman, sendo adquirido pelo Google por 400 milhões de libras esterlinas em 2014[^N16]. O AlphaGo da DeepMind venceu Lee Sedol em 2016; o AlphaFold 2 veio em 2020; o Nobel em 2024. Três eventos com menos de dez anos de intervalo.

A linha que os conecta é uma aposta comum: usar redes neurais para resolver problemas humanos que não podiam ser resolvidos pelo cérebro humano no passado. O Go (Xiangqi) é um campo fechado por regras, enquanto o dobramento proteico é um campo aberto por regras, mas com fortes restrições físicas. Hassabis escolheu bem os campos de batalha em ambas as áreas.

Em Taiwan, a pesquisa de moléculas de carboidratos estabelecida pela diretora do Academia Sinica, Oung-Hui Tseng (2006-2016), é o investimento acadêmico mais próximo desta fronteira[^N17]. Grupos no Instituto de Biomedicina e no Instituto de Bioquímica da Academia Sinica também estão realizando pesquisas downstream usando os pesos abertos do AlphaFold. No entanto, Taiwan atualmente não possui uma estrutura institucional para desenvolver modelos centrais no nível do AlphaFold.

> ⚠️ **Ponto de Vista Controverso**
>
> O Nobel de Química concedido ao AlphaFold gerou debate na comunidade acadêmica: alguns biólogos estruturais argumentam que o prêmio deveria ter sido dado aos cientistas de difração de raios X ou ressonância magnética nuclear que fizeram as descobertas experimentais mais cruciais, e não à ferramenta computacional elevada ao panteão da química[^N18]. Outros acreditam que este debate está ultrapassado — quando um algoritmo consegue completar a estrutura 3D de quase todas as proteínas do planeta em cinco anos, isso é química. O debate entre essas duas posições gradualmente migrou para a segunda após outubro de 2024, mas a tensão não desapareceu: o que acontece com os limites das disciplinas tradicionais à medida que o que a IA pode fazer se expande?

## TAIDE: Por que Taiwan precisa de seu próprio modelo de linguagem

Em abril de 2023, seis meses após o ChatGPT tomar conta do mundo, a Comissão Científica e Tecnológica Nacional (NSTC) de Taiwan lançou o projeto "TAIDE", cujo nome completo é Trustworthy AI Dialogue Engine (Motor de Diálogo de IA Confiável) [^13].

Por que uma ilha com 23 milhões de habitantes precisaria desenvolver seu próprio modelo de linguagem grande?

A razão não é apenas a soberania tecnológica. A proporção do chinês tradicional nos dados de treinamento global de IA é extremamente baixa, e a maior parte dos dados em chinês vem de sites simplificados. Quando os taiuaneses usam o ChatGPT ou outros modelos, as respostas frequentemente carregam hábitos linguísticos e pressupostos conceituais da China continental. Diferenças aparentemente sutis, como "視頻" (shìpín) em vez de "影片" (yǐngpiàn), ou "質量" (zhìliàng) em vez de "品質" (pǐnzhí), estão ligadas a questões de subjetividade cultural. A revista _Asia Economic Journal_ reportou o TAIDE com o título "Prevenindo a invasão cultural da IA chinesa" [^14].

Em abril de 2024, a equipe do TAIDE lançou os modelos comerciais TAIDE-LX-7B e acadêmicos TAIDE-LX-13B, que apresentaram bom desempenho em tarefas como escrita, tradução e sumarização [^15]. Em 2026, o TAIDE 2.0 foi lançado, juntamente com o modelo Breeze-8B suportado pela MediaTek, fazendo com que o ecossistema de LLMs de Taiwan passasse da fase de "perseguição" para a fase de "utilidade" [^16].

Mais interessante ainda é o florescimento das aplicações. A Universidade Nacional de Chung-Hsing usou o TAIDE para criar o sistema de recuperação de conhecimento agrícola "Shennong TAIDE"; a Universidade de Tainan desenvolveu um robô conversacional taiwanês-inglês para o ensino do dialeto taiwanês; e a Academia de Ciência, Tecnologia e Engenharia de Yangmingshan treinou modelos TAIDE em dialetos taiwanês e Hakka [^17]. Essas aplicações comprovam uma coisa: os modelos de linguagem são simultaneamente produtos tecnológicos e veículos culturais. Uma IA que não entende "Tianchuanri" (o dia em que o céu atravessa) ou "Mazu Raoting" (processão da Mazu) não pode servir verdadeiramente o povo de Taiwan.

No entanto, o escopo do TAIDE ainda é pequeno: os modelos comerciais 8B e acadêmicos 13B estão a mais de duas ordens de magnitude de distância dos níveis do GPT-4 da OpenAI (estimado em mais de um trilhão de parâmetros). Essa lacuna não é um problema de capacidade, mas sim um problema orçamentário de GPU. O poder computacional necessário para treinar um LLM de ponta está na ordem de centenas de milhões de dólares, o mesmo nível do orçamento anual de uma instituição científica nacional.

## Cibersegurança de IA "Hackeada"

Taiwan é um dos países mais frequentemente atacados por cibercrimes no mundo. Essa triste realidade acabou gerando uma indústria robusta de cibersegurança baseada em Inteligência Artificial (IA).

A CyCraft, fundada no final de 2017, é a primeira empresa de segurança em Taiwan a combinar IA com monitoramento de endpoints. Sua tecnologia foi listada sete vezes em relatórios da organização global de pesquisa Gartner e é a única empresa taiwanesa a ser avaliada três vezes pela autoridade MITRE ATT&CK dos EUA[^18]. Em fevereiro de 2026, a CyCraft foi listada na Bolsa de Valores de Taiwan (TWSE) no mercado inovador, tornando-se o primeiro fabricante de software de cibersegurança com capacidade de P&D autônomo de nível internacional no mercado de capitais taiwanês[^19].

Os clientes da CyCraft incluem agências governamentais taiwanesas, unidades de defesa nacional, bancos e empresas de semicondutores — que são justamente os alvos mais frequentemente visados por hackers de nível estatal. A empresa possui subsidiárias no Japão e em Singapura e está exportando sua "experiência prática adquirida através de ataques" para toda a região do Pacífico Asiático.

Este caso demonstra uma coisa: a vantagem da IA de Taiwan não provém apenas dos semicondutores, mas também da capacidade prática forjada por seu contexto geopolítico singular.

## Política: Da "Era da IA" ao Ministério de Transformação Digital

O desenvolvimento da política de IA em Taiwan pode ser compreendido através de três marcos.

De 2017 a 2018 foi o estágio inicial. O ministro da Ciência e Tecnologia, Chen Liang-chi, declarou que 2017 era um "Ano da IA", propondo a "Estratégia Nacional de Pequeno País, Grande Potência em IA" [^21], reconhecendo o pequeno mercado taiwanês, mas enfatizando três cartas: fabricação de semicondutores, cadeia de suprimentos de TIC e talentos em ciências exatas. Em 2018, foi iniciado o primeiro "Plano de Ação de IA de Taiwan", investindo mais de NT$40 bilhões ao longo de quatro anos, com foco na construção da infraestrutura de computação de IA, a "Taiwan AI Cloud" (TWCC) [^20].

Em 2022, houve uma institucionalização. O Ministério de Transformação Digital foi estabelecido, integrando as tarefas digitais que antes estavam dispersas entre o Ministério da Ciência e Tecnologia, o Ministério da Economia e o Ministério do Transporte. A importância deste passo reside no fato de que a política de IA passou de um "projeto do Ministério da Ciência e Tecnologia" para uma "estratégia nacional interministerial". No mesmo ano, o governo publicou as "Diretrizes de Pesquisa em Inteligência Artificial", enfatizando princípios como centrado no ser humano, transparência, explicabilidade e não discriminação.

A partir de 2023, a tendência foi para a IA generativa. O impacto do ChatGPT forçou uma mudança de rumo na política. O projeto TAIDE foi lançado, o rascunho da Lei Básica de IA foi promovido e a adoção de IA pelo setor público foi acelerada. A estratégia de Taiwan é muito pragmática: em vez de competir com EUA e China no número de artigos de pesquisa básica, ela conecta a IA às vantagens industriais existentes. Manufatura inteligente, imagem médica e previsão de rendimento de semicondutores são áreas onde Taiwan possui dados, cenários e competitividade.

O problema é que os dois prêmios Nobel concedidos em outubro de 2024 não vieram da rota da "manufatura inteligente".

## Ansiedade: A Lacuna de Software no Império do Hardware

Por trás dos números brilhantes, o desenvolvimento de IA em Taiwan possui um problema estrutural: um grave desequilíbrio entre hardware e software.

Taiwan produz nove décimos da IA servidores globais e a maior parte dos chips de IA, mas tem pouca presença nas áreas de "soft" como o desenvolvimento de modelos de IA, ecossistema de dados e software de plataforma. Nenhum dos vinte principais modelos de IA globais, incluindo GPT, Claude, Gemini e LLaMA, é originário de Taiwan. Ao comparar os trabalhos premiados com o Prêmio Nobel duplo em 2024 — da Rede Hopfield ao _backpropagation_ até AlphaFold —, essas três linhas estão distantes do setor taiwanês.

A razão é uma nova versão de um problema antigo. Quando engenheiros da TSMC podem ganhar mais de NT$ 2 milhões por ano, as startups de software têm dificuldade em atrair talentos de ponta. O Google, Microsoft e NVIDIA estabeleceram centros de P&D em Taiwan, criando um forte efeito de sucção com salários e benefícios. A primeira escolha de um graduado do Departamento de Ciência da Computação da National Taiwan University (NTU) é frequentemente uma empresa estrangeira ou a TI da TSMC, e não ingressar em uma startup local de IA.

O desafio mais fundamental é o dado. O valor dos modelos de IA vem dos dados de treinamento, e a quantidade de dados de alta qualidade em chinês tradicional é insignificante em comparação com inglês ou chinês simplificado. A quantidade de texto gerada pela população de 23 milhões de Taiwan naturalmente não se compara ao mundo anglófono ou à China continental. O projeto TAIDE tenta resolver esse problema, mas a desvantagem de escala dos dados é estrutural.

A verdadeira aposta da IA em Taiwan está nas aplicações verticais, e não nos modelos básicos: em vez de competir diretamente com OpenAI ou Google em modelos genéricos, Taiwan escolhe encontrar um lugar insubstituível na IA de processos de semicondutores, IA de imagens médicas, IA de segurança cibernética e PNL em chinês tradicional. Nestas áreas, Taiwan possui vantagens únicas em dados e cenários que são difíceis para os outros replicarem.

## A Escolha de IA de uma Ilha

Em 2026, Taiwan ocupa uma posição única: é indispensável na cadeia de suprimentos de hardware de IA, mas permanece marginal no ecossistema de software de IA.

Isso não é totalmente negativo. Historicamente, o modelo de sucesso de Taiwan tem sido o de "não ser a marca, mas sim a marca por trás da marca". O modelo puramente de fabricação por contrato (foundry), inventado por Tseng Shih-mao em 1987, tornou a TSMC uma das dez maiores empresas do mundo em valor de mercado. Hoje, a mesma lógica está se repetindo na indústria de servidores de IA: a Foxconn não desenvolve modelos de IA, mas todos os modelos de IA do mundo rodam em servidores montados pela Foxconn.

No entanto, as regras do jogo na era da IA podem ser diferentes. Quando o foco do valor migra do hardware para o software e dados, o espaço de lucro apenas com fabricação por contrato é comprimido. Os prêmios Nobel concedidos nos dois dias de 2024 foram todos focados na camada de software. Hopfield escreveu um modelo matemático, Hinton escreveu um algoritmo de treinamento, e Hassabis escreveu uma metodologia de solução biológica. Todo esse trabalho roda em hardware fabricado em Taiwan, mas o prêmio não é dado ao hardware.

Taiwan precisa desenvolver capacidade em software e dados sobre a base da hegemonia do hardware: o hardware ainda é a fundação, e novas camadas de valor são construídas sobre ela. TAIDE é uma tentativa, CyCraft é uma tentativa, Taiwan AI Labs é uma tentativa. O que os une é que eles não buscam ser "a IA mais grande do mundo", mas sim "a IA que melhor entende Taiwan".

Há 42 anos, quando Hopfield escreveu aquelas 12 páginas em Princeton, ninguém sabia que isso se tornaria a base matemática dos modelos de memória humana atuais. Há 50 anos, quando Anfinsen propôs a hipótese do dobramento proteico no discurso do Nobel, ninguém previu que seria desvendada por um grupo de londrinos apenas na tarde de 2020. A escala de tempo da pesquisa básica é maior do que qualquer Computex.

A refeição em um mercado noturno de Ningxia representa a posição acumulada por Taiwan ao longo destes 42 anos. Qual será o próximo campo de batalha? Não está na barraca de _oaijian_, mas se Taiwan tem coragem para fazer com que um estudante programando no dormitório da Universidade Nacional de Taichung receba um Nobel pertencente a esta ilha daqui a vinte ou trinta anos.

---

**Leitura Complementar**:

- [Ascensão do País Insular de IA: Desenvolvimento e Estratégia de Inteligência Artificial em Taiwan](/pt/technology/ai-development-in-taiwan) — Narrativa de estrutura de políticas da fase inicial, o Plano de Ação de IA, os cinco domínios estratégicos e a visão geral de como a montanha sagrada dos semicondutores se conecta à revolução da IA.
- [Laboratório de Inteligência Artificial de Taiwan](/pt/technology/taiwan-ai-labs) — A jornada completa de Du Yijin do PTT aos AI Labs, o ecossistema de modelos de linguagem abertos TAIDE / TAME / FedGPT.
- [Escola de Inteligência Artificial de Taiwan](/pt/technology/taiwan-ai-academy) — O exército de IA construído com a arrecadação privada de 180 milhões (NT$) que não terminou a ligação, e a história da formação de talentos por mais de dez mil ex-alunos.
- [Vida Diária da IA em Taiwan](/pt/technology/taiwan-ai-in-daily-life) — Observações em nível de cena sobre a chegada da IA generativa à vida cotidiana em Taiwan, desde pedidos em lojas de conveniência até auditorias em lote pela Agência Nacional de Seguro Saúde.
- [Empresas de Taiwan: TSMC](/pt/economy/tsmc) — Líder global em fundição de wafers, o núcleo da fabricação de chips de IA, da lógica de fabricação por contrato de Tseng Shih-mao ao conto do _packaging_ avançado.
- [Indústria Semicondutora](/pt/technology/taiwan-semiconductor-industry) — Panorama completo do ecossistema de semicondutores de Taiwan, do design de IC ao teste e embalagem.
- [Desenvolvimento da Indústria de Cibersegurança em Taiwan](/pt/technology/taiwan-cybersecurity-industry-development) — Como a pressão geopolítica deu origem à indústria de cibersegurança de nível Ásia-Pacífico.

## Fonte das Imagens

Este artigo utiliza 4 imagens de domínio público/licença CC, todas cacheadas em `public/article-images/technology/` para evitar links diretos a servidores:

- [Estrutura tridimensional da proteína CBLN1 pelo AlphaFold com codificação rainbow](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — herói, Estrutura predita do proteína CBLN1 pelo AlphaFold, codificação de extremidade N→C em cores arco-íris. Foto: BQUB25-UPoch (obra própria, AlphaFold + PyMOL), 15/11/2025, CC BY 4.0.
- [Geoffrey E. Hinton, Prêmio Nobel de Física de 2024 (3x4 cortado)](<https://commons.wikimedia.org/wiki/File:Geoffrey%5FE.%5FHinton,%5F2024%5FNobel%5FPrize%5FLaureate%5Fin%5FPhysics%5F(3x4%5Fcropped).jpg>) — em linha, Retrato oficial de Hinton na semana do Nobel de 2024. Foto: Arthur Petron, 08/12/2024, CC BY-SA 4.0.
- [John J. Hopfield, Prêmio Nobel de Física de 2024 1 (cortado)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — em linha, Retrato oficial de Hopfield na semana do Nobel de 2024. Foto: Arthur Petron, 08/12/2024, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — em linha, Fábrica TSMC Hsinchu Fab 5, cena física da fabricação de chips de IA. Foto: Wikimedia Commons (cache existente).

---

## Referências

[^1]: [Tom's Hardware: Lendas de semicondutores passeiam em um mercado noturno taiwanês](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — Reportagem do Mercado Noturno de Ningxia, 29 de maio de 2024, registrando Huang Renxun, TSMC (C.C. Lin), Lin Bairi e Cai Lixing jantando juntos.

[^2]: [Taiwan News: CEO da Nvidia chama Taiwan de 'um dos países mais importantes do mundo'](https://www.taiwannews.com.tw/news/5880054) — Declaração pública de Jensen Huang durante sua visita a Taiwan em 30/05/2024.

[^3]: [Wikipedia: Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — Biografia de Jensen Huang, nascido em Taipei em 1963, infância em Tainan e imigração para os EUA aos nove anos.

[^4]: [Klover.ai: Domínio de Fabricação de IA da TSMC](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) — Todos os GPUs avançados da NVIDIA (A100, H100, série Blackwell) são fabricados por contrato pela TSMC. Veja

[^5]: [SQ Magazine: Estatísticas de Chips de IA 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — Dados de participação de mercado de fôlderias da TSMC em 72% em 2025; veja também a cobertura simultânea do Motley Fool.

[^6]: [PatentPC: A Explosão do Mercado de Chips de IA](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — Fonte dos dados de que a NVIDIA detém 86% da fatia de mercado de GPUs de IA.

[^7]: [Tech-Now: Taiwan lidera a mudança global de servidores de IA, superando iPhones em 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — Dados de exportação globais de servidores de IA da Foxconn, Wistron e Quanta, atingindo 90%.

[^8]: [DigiTimes: Foxconn, Wistron e Quanta sustentarão receita de trilhões em servidores de IA em 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — Relato de que as receitas anuais das três ODMs ultrapassarão um trilhão, com servidores de IA superando eletrodomésticos.

[^9]: [36Kr: Quem dividirá a capacidade de produção CoWoS em 2026?](https://eu.36kr.com/en/p/3580962946874242) — Dados de que a NVIDIA precisa de 595 mil fôlderes de wafers CoWoS, representando 60% do global.

[^10]: [NVIDIA Newsroom: Foxconn constrói fábrica de IA em parceria com Taiwan e NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — Projeto da fábrica de IA de 100MW em Kaohsiung; veja também a cobertura da CNBC sobre a capacidade de energia de 100MW.

[^11]: [Site Oficial do Laboratório de Inteligência Artificial de Taiwan - Sobre Nós](https://ailabs.tw/zh/關於我們/) — Apresentação oficial de Du Yijin, que fundou o PTT em 1995 na Universidade Nacional de Taiwan e fundou a Taiwan AI Labs em abril de 2017.

[^12]: [TechNews: O Novo Jornal da Tecnologia: Talentos de IA estão em Taiwan, devem ficar ou ir embora? Entrevista com o fundador do Laboratório de Inteligência Artificial de Taiwan, Du Yijin](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — Transcrição de Ya Ting e introdução de projetos centrais como a medicina de aprendizado federado.

[^13]: [Executivo do Conselho: Aperfeiçoando a infraestrutura de IA de Taiwan — Criando o motor de diálogo confiável TAIDE](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — Declaração oficial sobre o projeto TAIDE, iniciado em abril de 2023.

[^14]: [Taiwan Literature Magazine: 'Prevenindo a Agressão Cultural da IA Chinesa' - O que pode fazer o primeiro grande modelo de linguagem chinês tradicional TAIDE?](https://www.cw.com.tw/article/5129076) — Relato temático sobre TAIDE, e discussão sobre a subjetividade cultural do LLM em chinês tradicional.

[^15]: [Comunicado de Imprensa da Academia Nacional de Ciências: O TAIDE foi um sucesso em um ano; cooperação público-privada promove modelos de linguagem grandes com características taiwanesas](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — Lançamento das versões comerciais TAIDE-LX-7B e acadêmicas 13B em abril de 2024.

[^16]: [CloudInsight: Status de Desenvolvimento de LLMs em Taiwan 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — Inventário completo do ecossistema de LLM taiwanês, incluindo TAIDE 2.0 e Breeze-8B.

[^17]: Relatório CloudInsight mencionado acima. Detalhes dos casos de uso como o 'Shennong TAIDE' da Universidade Chung-Hsing, o robô de conversação Taiwanês da Universidade de Tainan e o modelo TAIDE em dialeto taiwanês da Universidade de Educação Internacional de Yangming.

[^18]: [CIO Taiwan: Visita às Empresas de Cibersegurança de Taiwan - Ogy Wisdom Technology](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — Detalhes sobre a Ogy Wisdom, que foi listada sete vezes pelo Gartner e passou três vezes na avaliação MITRE ATT&CK.

[^19]: [Site Oficial da Ogy Wisdom: Rei da Cibersegurança IA Lançado! Ogy Cyber Lista Hoje](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — Comunicado de imprensa sobre o lançamento na Innovation Board em 5 de fevereiro de 2026.

[^20]: [NSTC: Estratégia de Pesquisa em IA](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — Estrutura de políticas, como o Plano de Ação de IA de Taiwan com orçamento de 40 bilhões e a construção do TWCC.

[^21]: [Semiconductors Shooting Star, Tech Arena Chen Liang-chi: 16 Bilhões para a IA de Taiwan — Revista Vision, 2017](https://www.gvm.com.tw/article/39819) — O Ministro da Tecnologia, Chen Liang-chi, declarou que 2017 era o ano da IA e apresentou a Grande Estratégia Nacional de IA em meados de agosto.

[^N1]: [Comunicado de Imprensa do Prêmio Nobel de Física 2024](https://www.nobelprize.org/prizes/physics/2024/press-release/) — Anúncio oficial da Royal Swedish Academy of Sciences em 8 de outubro de 2024. O texto original é: 'A Royal Swedish Academy of Sciences decidiu conceder o Prêmio Nobel de Física de 2024 a John J. Hopfield e Geoffrey Hinton por descobertas e invenções fundamentais que permitem o aprendizado de máquina com redes neurais artificiais.' A recompensa é de 11 milhões de coroas suecas, dividida igualmente entre os dois.

[^N2]: [Comunicado de Imprensa do Prêmio Nobel de Química 2024](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — Anúncio em 9 de outubro de 2024. A recompensa é de 11 milhões de coroas suecas, com David Baker recebendo metade 'por design computacional de proteínas', e Demis Hassabis e John Jumper compartilhando a outra metade 'por predição da estrutura de proteínas'.

[^N3]: [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities."

[^N4]: [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors."

[^N5]: [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks."

[^N6]: [PanSci Ciência Geral: Prêmio Nobel de Física 2024 — Hopfield e Hinton Iniciam a Era do Aprendizado de Máquina com Redes Neurais Artificiais](https://pansci.asia/archives/378242) — Parceiro de Curadoria de Conteúdo conforme MOU 2026-05-05. Abrange o contexto da Rede de Hopfield, a analogia com vidro de spin, o acúmulo de citações do artigo e a conexão matemática com o aprendizado profundo contemporâneo.

[^N7]: [The Guardian: Vencedor do Prêmio Nobel de Física 2024 John Hopfield alerta sobre perigos da IA](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — Relato de entrevista telefônica do Prêmio Nobel de Física em 8 de outubro de 2024, onde Hopfield e Hinton emitiram um aviso sobre os riscos da IA no mesmo dia.

[^N8]: [Wikipedia: Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton nasceu em Wombwell, Londres, em 6 de dezembro de 1947, e juntou-se ao Google após a aquisição da DNNresearch por US$ 44 milhões em março de 2013.

[^N9]: [BBC News: 'Padrinho' da IA Geoffrey Hinton alerta sobre perigos ao deixar o Google](https://www.bbc.com/news/world-us-canada-65452940) — Em 1º de maio de 2023, após deixar o Google, Hinton expressou preocupações com os riscos da IA à BBC. O original diz: "Eu saí para poder falar sobre os perigos da IA sem considerar como isso afeta o Google", e "parte de mim agora lamenta o trabalho da minha vida". Os detalhes da entrevista do NYT na época também são referenciados neste relatório.

[^N10]: [Nature: Cientista de IA Geoffrey Hinton ganha Prêmio Nobel de Física](https://www.nature.com/articles/d41586-024-03213-8) — Detalhes da Nature sobre a ligação telefônica com Hinton no local da premiação do Prêmio Nobel de Física em 2024.

[^N11]: [Wikipedia: História econômica de Taiwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — Dados do PIB de Taiwan em 1986; o Parque Científico de Hsinchu foi estabelecido em dezembro de 1980.

[^N12]: [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — Anfinsen, C. B. (1973). "Princípios que governam a dobra das cadeias proteicas."

[^N13]: [Nature: 'Isso mudará tudo': IA do DeepMind faz salto gigantesco na resolução de estruturas proteicas](https://www.nature.com/articles/d41586-020-03348-4) — Relato da publicação dos resultados do CASP14 em 30 de novembro de 2020, onde a GDT mediana do AlphaFold 2 foi de 92.4, e John Moult, organizador do CASP, comentou: "em algum sentido o problema está resolvido".

[^N14]: [DeepMind: AlphaFold revela a estrutura do universo proteico](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — Anúncio em 28 de julho de 2022 sobre o Banco de Dados de Estrutura Proteica AlphaFold cobrindo 1 milhão de espécies e cerca de 200 milhões de estruturas proteicas.

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Previsão precisa de interações biomoleculares com AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — O AlphaFold 3 foi publicado em 8 de maio de 2024, expandindo a previsão para complexos de proteína/DNA/RNA/ligante/íon.

[^N16]: [Wikipedia: Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis começou a jogar xadrez aos 4 anos; em 17 anos (1994), co-desenvolveu Theme Park com Peter Molyneux; fundou o DeepMind em Londres em 2010; foi adquirido pelo Google por cerca de £ 400 milhões em 2014.

[^N17]: [Centro de Pesquisa Genômica da Academia Sinica](https://www.genomics.sinica.edu.tw/) — Centro de Pesquisa de Estrutura Molecular de Glicanos estabelecido durante o mandato do diretor Cheng-Hui Weng (2006-2016).

[^N18]: [PanSci Ciência Abrangente: Prêmio Nobel de Química 2024 — David Baker, Demis Hassabis e John Jumper resolvem o enigma da dobra proteica](https://pansci.asia/archives/378388) — Parceiro de Curadoria de Conteúdo conforme MOU 2026-05-05. Cobre a controvérsia do AlphaFold no Prêmio Nobel de Química e o debate sobre as fronteiras disciplinares entre biologia estrutural e química computacional.

[^N19]: [PanSci Ciência Abrangente: AlphaFold 3 prevê interações de proteínas com outros moléculas, elevando o desenvolvimento de medicamentos](https://pansci.asia/archives/377917) — Parceiro de Curadoria de Conteúdo conforme MOU 2026-05-05. Análise do impacto downstream do AlphaFold 3 no desenvolvimento de medicamentos e engenharia enzimática.

[^N20]: [PanSci Ciência Abrangente: OI 'Cérebro Artificial' desafia a IA — o tecido cerebral em placa pode substituir os chips de silício?](https://pansci.asia/archives/366027) — Parceiro de Curadoria de Conteúdo conforme MOU 2026-05-05. Pesquisa de cérebro artificial da equipe de Thomas Hartung, Johns Hopkins, como uma direção computacional alternativa à IA.
