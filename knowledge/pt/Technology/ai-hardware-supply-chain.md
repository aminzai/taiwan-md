---
title: 'A cadeia de suprimentos de hardware de IA: o lugar onde Taiwan transforma a nuvem em máquinas'
description: 'A IA generativa parece um serviço em nuvem, mas na verdade exige uma via física completa: há quem projete chips, quem produza wafers, quem realize o encapsulamento, quem gerencie memória, energia, refrigeração, placas-mãe e racks. A importância de Taiwan não se resume à TSMC, mas à concentração de pontos críticos ao longo dessa via; esse interesse comum é real, mas vem acompanhado de pressões sobre energia, emissões de carbono, distribuição de renda, relocação de fábricas e riscos geopolíticos, transformando slogans abstratos em evidências verificáveis da cadeia de suprimentos.'
date: 2026-07-11
category: 'Technology'
tags:
  [
    'Hardware de IA',
    'Semicondutores',
    'Cadeia de suprimentos',
    'Servidores de IA',
    'Processos avançados',
    'Encapsulamento avançado',
    'Indústria tecnológica de Taiwan',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-07-11
lastHumanReview: false
researchReport: 'reports/research/2026-07/半導體供應鏈草稿地圖.md'
rationale: "{'why_this_hook': '從「兆元宴」座位表切入，讓讀者先看見 AI 硬體供應鏈不是單一公司，而是一整組台灣工程節點。', 'whats_excluded': '不做完整產業百科，也不逐一列出台灣所有半導體、伺服器與零組件公司。', 'where_it_hedges': '把台灣的供應鏈價值與水電、碳排、所得分配、海外設廠、地緣政治風險一起處理。', 'whos_pushing_back': '全球客戶與盟友一方面需要台灣，另一方面也透過海外設廠降低對台灣海峽周邊產能的單點依賴。'}"
image: '/article-images/technology/ai-hardware-supply-chain-flow.svg'
imageCredit: 'Taiwan.md Contributors'
imageLicense: 'CC BY-SA 4.0'
translatedFrom: 'Technology/AI硬體供應鏈.md'
sourceCommitSha: '8f5e81ee5'
sourceContentHash: 'sha256:96b285db19941653'
sourceBodyHash: 'sha256:96ecb5a6142f55f7'
translatedAt: '2026-07-26T08:13:12+08:00'
---

# A cadeia de suprimentos de hardware de IA: o lugar onde Taiwan transforma a nuvem em máquinas

> **Resumo em 30 segundos:** A IA parece responder perguntas na tela, mas por trás há um longo revezamento físico. Alguém formula a demanda, alguém projeta o chip, alguém fabrica o chip, alguém monta o chip, a memória, o sistema de refrigeração, a energia e a placa-mãe em máquinas, enviando-as finalmente para os data centers. A importância de Taiwan não pode ser resumida apenas com "a TSMC é forte"; nesse revezamento, há várias etapas críticas que estão em Taiwan. Esse interesse comum é real, mas não é uma garantia; ele traz simultaneamente pressões sobre energia, emissões de carbono, distribuição de renda, relocação de fábricas no exterior e geopolítica.

Em 28 de maio de 2026, Jensen Huang organizou um banquete em Taipei. A imprensa chamou de "Banquete de Triliões", porque a capitalização de mercado das empresas por trás dos convidados somava um valor impressionante. Mas o mais interessante naquela mesa não era quem estava na cadeira principal, nem quanto valiam essas empresas somadas.

O que realmente vale a pena observar é a lista de assentos.

Na área de _foundry_ de _wafers_, há o Wei Chieh-chia (魏哲家) da TSMC. Na montagem de servidores e racks de IA, há o Liu Yang-wei (劉揚偉) da Foxconn, o Lin Baili (林百里) da Quanta, o Lin Hsien-ming (林憲銘) da Wistron e o Hong Li-ning (洪麗寗) da Inventec. No design de circuitos integrados (IC), há o Tsai Li-hsing (蔡力行) da MediaTek. Na energia e refrigeração, há o Cheng Ping (鄭平) da Delta Electronics, o Chiu Sen-pin (邱森彬) da Lite-On e o Shen Ching-hsing (沈慶行) da Chicony. Na placa-mãe e marcas finais, há o Shih Chung-tang (施崇棠) da ASUS, o Yeh Pei-cheng (葉培城) da Gigabyte e o Chen Chun-sheng (陳俊聖) da Acer. As categorias da cadeia de suprimentos listadas pela Central News Agency (CNA) vão desde a _foundry_ de _wafers_, encapsulamento e teste, módulos de refrigeração, gerenciamento de energia, placas-mãe até a montagem por contrato e marcas, sendo quase um corte transversal de um servidor de IA desmontado. [^1]

![Jensen Huang segurando a GPU RTX Blackwell durante o discurso principal na CES 2025, com o fundo preto do palco mostrando o logotipo da NVIDIA e o novo módulo de chip de IA na mão](/article-images/technology/jensen-huang-ces-2025-blackwell.webp)

_Jensen Huang apresenta a GPU RTX Blackwell no discurso principal da CES 2025. Esta imagem traz o "IA" de volta da interface de software para o hardware nas mãos. Foto: Steve Jurvetson. CC BY 2.0 via Wikimedia Commons._

Não foi apenas um jantar corporativo comum. Foi como colocar uma pergunta na mesa: quando o mundo todo diz que a IA precisa de Taiwan, o que exatamente ela precisa?

A resposta não será apenas uma empresa, nem apenas um chip. É mais como uma estrada: começa com a frase "precisamos de mais capacidade de computação de IA", passa por chips, fábricas, encapsulamento, energia, refrigeração, placa-mãe, racks, e finalmente chega ao data center. Taiwan está em vários pontos críticos ao longo dessa estrada.

## Primeiro, pense na IA como um serviço que precisa de corpo

O contato geral com a IA geralmente ocorre em celulares, computadores ou páginas da web. Digita-se um texto e a resposta aparece. Parece mágica, também parece um serviço em nuvem sem peso.

![Salão da feira Computex no Centro de Exposições de Nangang, Taipei, corredores largos com barracas de empresas de TI dispostas em ambos os lados, multidões reunidas, mostrando a cena da cadeia de suprimentos de hardware de Taiwan sendo vista na feira](/article-images/technology/computex-nangang-floor-2015.webp)

_Salão da feira Computex no Centro de Exposições de Nangang, Taipei. A cadeia de suprimentos de hardware de IA não existe apenas nos demonstrativos financeiros, mas também é vista concretamente nos salões, protótipos, racks e reuniões de negócios. Foto: Solomon203. CC BY-SA 4.0 via Wikimedia Commons._

Mas para responder perguntas, a IA precisa de máquinas operando por trás. Essas máquinas ficam nos data centers, consomem eletricidade, geram calor, precisam de manutenção, e também precisam de alguém que as construa, monte e entregue às mãos dos clientes.

Pode-se pensar na IA como um grande restaurante. Você vê o garçom servindo o prato na mesa, mas não vê o design do cardápio, as compras, a cozinha, o gás, a água e eletricidade, a refrigeração, a logística de saída e a limpeza. A IA é assim. Você vê a resposta na tela, mas por trás há todo um conjunto de cozinha de hardware.

A posição de Taiwan está exatamente nessas bancadas de trabalho importantes dentro dessa cozinha.

## Como um pedido se torna um rack

Uma cadeia de suprimentos de hardware de IA frequentemente começa com uma demanda comum: empresas de nuvem, empresas de modelos ou grandes corporações precisam de mais capacidade de computação. Essa frase soa como comprar um serviço em nuvem, mas rapidamente se torna uma série de problemas físicos: que chip projetar? Onde fabricar? Como aproximar a memória? Como dissipar o calor? Como enviar a energia? Quem finalmente monta essas peças caras em máquinas que podem ser entregues, mantidas e colocadas em data centers?

![Diagrama de fluxo da cadeia de suprimentos de hardware de IA: a demanda de IA passa pelo design de chips, processos avançados, encapsulamento avançado, HBM e *substrates*, refrigeração e energia, placa-mãe, ODM/EMS, rack de IA, e finalmente entra no data center; o diagrama marca os pontos de engenharia altamente concentrados em Taiwan como processos, encapsulamento, energia e calor, placas e montagem/racks](/article-images/technology/ai-hardware-supply-chain-flow.svg)

_Diagrama ilustrativo criado pela Taiwan.md. Este diagrama não é um gráfico de participação de mercado, nem um mapa completo de empresas; ele serve para ilustrar uma via central: como a demanda de IA se materializa em máquinas que podem ser alimentadas, resfriadas e entregues._

O design de chips na ponta mais avançada é geralmente controlado por empresas como NVIDIA, AMD, Broadcom, Google, Amazon e Microsoft. Uma das posições importantes de Taiwan é quando o projeto precisa se tornar um chip. A rota técnica oficial da TSMC lista processos lógicos de 7 nm, 5 nm, 3 nm, 2 nm, A16, A14, com o N2 marcado para produção em massa no quarto trimestre de 2025. [^2] Para muitos chips de IA, este é o momento em que o design toca pela primeira vez a terra de Taiwan.

Mas fabricar o chip não significa que a IA esteja online. Os chips de IA precisam estar próximos à memória e também precisam conectar diferentes _dies_ em um sistema que funcione em alta velocidade. A TSMC descreve o 3DFabric como uma combinação de tecnologias de _stacking_ de silício 3D e encapsulamento avançado, incluindo SoIC, CoWoS, InFO, etc. A Associated Press (AP), ao reportar sobre a nova fábrica de Xinhua em Taichung, também a coloca no contexto do fortalecimento da produção de chips de IA. [^3][^4] Aqui, o papel de Taiwan começa a se estender de "fabricar o chip" para "conectar o chip em módulos funcionais".

Avançando mais, a cadeia de suprimentos se parece menos com uma linha reta. A memória HBM de alta largura de banda é principalmente dominada por empresas coreanas. Equipamentos, materiais e software de design envolvem fornecedores dos EUA, Holanda, Japão e Europa. Plataformas de nuvem e serviços de modelos ficam majoritariamente nas mãos dos EUA. Taiwan não monopoliza cada segmento, nem leva o maior lucro em cada segmento. Sua singularidade reside no fato de que os pontos críticos de _foundry_ de _wafers_, encapsulamento, encapsulamento e teste, _substrates_, energia, refrigeração, placa-mãe e montagem de整机 estão próximos, com um hábito de longo prazo de resolver problemas de engenharia juntos.

![Diagrama em camadas de servidores de IA: chips e aceleradores, placas e placas-mãe, energia e refrigeração, servidores e racks, data centers empilhados sequencialmente, explicando como a GPU se torna infraestrutura de IA online](/article-images/technology/ai-server-rack-stack.svg)

_Diagrama ilustrativo criado pela Taiwan.md. A GPU é apenas um dos núcleos dos servidores de IA; ela precisa ser conectada a placas, energia, refrigeração,整机, racks e data centers._

Na etapa de整机, a questão torna-se muito específica. Quanto mais forte o chip, maior a corrente, mais difícil dissipar o calor. Placa-mãe, energia, refrigeração, carcaça, sistema de gerenciamento e cronograma de entrega interagem juntos. Foxconn, Quanta, Wistron, Inventec, InnoVision, Compal e Pegatron recebem o trabalho de montar chips, placas, energia, refrigeração e design mecânico em servidores e racks de IA. A CNA, ao reportar sobre a entrega da nova plataforma da Foxconn, também a coloca no contexto da exibição de sistemas de servidores de IA. [^10]

Portanto, o diagrama de fluxo não serve para memorizar termos. Serve para fazer as pessoas verem: o valor de Taiwan não está apenas em uma empresa, nem apenas em um chip, mas na capacidade de, em uma curta distância e curto tempo, empurrar produtos complexos desde o _wafer_ e encapsulamento até o rack e o data center. Essa densidade é o que diferencia Taiwan de bases de manufatura de baixo custo comuns.

Para o leitor geral, esse trecho também oferece um método de leitura de notícias. Da próxima vez que vir uma empresa anunciar uma nova plataforma de IA, não pergunte apenas quem projetou o chip; também pergunte: onde é o encapsulamento? Quem faz o整机? Quem gerencia a energia e o calor? Quem assume o prazo de entrega e a manutenção? Ao fazer essas perguntas, o contorno de Taiwan na cadeia de suprimentos ficará mais claro, mais concreto e mais fácil de avaliar.

## Semicondutores são a entrada, não o destino

Escrever a indústria tecnológica de Taiwan como "apenas a TSMC" é conveniente, mas faz perder muitas coisas.

A fábrica de _wafers_ responde à pergunta "se o chip pode ser fabricado". A cadeia de suprimentos de hardware de IA ainda precisa responder a outras perguntas: o chip pode ser conectado à memória? Pode ser alimentado, resfriado, testado e mantido? Pode ser montado em um rack inteiro, uma fileira inteira, um data center inteiro dentro do tempo exigido pelo cliente?

O que realmente precisa ser questionado aqui é qual limite cada segmento está resolvendo. O processo lógico de ponta mais avançada resolve "se é possível encaixar mais transistores em um chip menor e mais eficiente". O encapsulamento avançado resolve "quando um único chip não é suficiente, se é possível conectar o chip de computação, a memória e diferentes _dies_ de forma próxima e rápida". O que os servidores de IA precisam perguntar é outra coisa: essas peças caras podem ser transformadas em uma máquina estável, mantida, produzida em massa e entregue?

Portanto, refrigeração e energia não são coadjuvantes. Quanto mais forte o chip, maior a corrente, mais difícil lidar com o calor. Se a energia for instável e o calor não for dissipado, os chips mais avançados só podem reduzir a velocidade ou até não entrar online. Processos maduros também não desaparecem, porque uma máquina de IA ainda precisa de muitos chips de controle, conexão, gerenciamento de energia e periféricos. O processo mais avançado é como o motor; processos maduros e componentes são como freios, sistema de combustível, painel e sistema de resfriamento. Sem qualquer um desses segmentos, o carro não pode correr de forma confiável.

Neste grande quadro, basta capturar uma coisa: semicondutores são a entrada, não o destino. Para a IA entrar realmente online, ainda precisa passar por toda uma via que transforma o chip em máquina.

É por isso que "Taiwan tem valor" não deve ser apenas um consolo abstrato. Deve poder ser desmontado em um diagrama: quem faz o _wafer_, quem faz o encapsulamento, quem faz a refrigeração, quem faz a energia, quem faz a placa-mãe, quem faz o整机, quem assume o prazo, quem assume a energia e água, quem é cortado primeiro na reversão do ciclo econômico.

Este diagrama também ajuda a identificar a linguagem das notícias. Quando um empresário diz "Taiwan é um parceiro", pode-se perguntar se ele depende do processo, encapsulamento, ODM, energia ou da velocidade de resposta do sistema inteiro. Quando um político diz "interesse comum", pode-se perguntar em quais empresas, quais cidades e quais trabalhadores esse interesse está concentrado. Quando um investidor diz "o futuro da IA é promissor", pode-se追问 se esse futuro está no design de chips, capacidade de encapsulamento, montagem de servidores ou componentes de refrigeração e energia. Quando slogans abstratos são desmontados em camadas, o leitor é menos propenso a ser levado apenas pelas emoções.

## Interesse comum é real, mas não é mágica

A posição de Taiwan na cadeia de suprimentos de hardware de IA realmente criou um interesse comum.

Para a NVIDIA, grandes empresas de nuvem e empresas globais de IA, Taiwan é o lugar onde elas transformam design em produto. Para os EUA, Japão, Europa e outros países, Taiwan é um nó de fornecimento indispensável para chips avançados e infraestrutura de IA. Para Taiwan, essa relação de ser necessária traz exportações, investimento, emprego, visibilidade na bolsa e cartas de jogo na política internacional.

A Associated Press (AP) em 2026, ao reportar sobre a economia de IA de Taiwan, colocou crescimento forte, aumento de exportações, expansão da presença da NVIDIA em Taiwan, bolha de IA, riscos geopolíticos e desigualdade de renda na mesma matéria. [^5] Essa coligação é importante porque lembra o leitor: interesse comum não é proteção unilateral, nem um amuleto que nunca falha.

Outros países estão tentando mover parte da cadeia de suprimentos para fora. A TSMC abre fábricas nos EUA, Japão e Alemanha; por um lado, prova que o mundo precisa da TSMC, por outro, também significa que clientes e governos não querem apostar todos os riscos em Taiwan. Fábricas no exterior não podem necessariamente replicar a densidade completa de Taiwan a curto prazo, mas mudarão a estrutura de negociação a longo prazo.

Além disso, interesses corporativos não são iguais a interesses nacionais. A NVIDIA quer fornecimento estável e alta margem de lucro. A TSMC quer liderança tecnológica e clientes globais. As fábricas de ODM querem pedidos e taxa de utilização de capacidade. A sociedade taiwanesa quer salários, habitação, segurança energética, capacidade ambiental e segurança. Esses interesses se sobrepõem, mas também entram em conflito.

Todos na mesa são importantes, mas o poder não é médio. A NVIDIA controla a arquitetura GPU, o ecossistema CUDA e o ritmo da plataforma. A TSMC controla processos avançados e capacidade de encapsulamento crítico. Grandes empresas de nuvem controlam a compra de data centers. Fábricas de ODM controlam design de整机, montagem de racks e entrega em massa, mas a margem de lucro é geralmente muito inferior às empresas de design de chips. Fábricas de componentes como energia, refrigeração, _substrates_ e interfaces de teste, algumas obtêm melhor lucro devido a barreiras tecnológicas altas, outras flutuam com os pedidos dos grandes clientes. É por isso que o "interesse comum" precisa ser observado desmontado: na mesma cadeia de suprimentos, cada segmento é necessário, mas nem todos dividem o mesmo poder.

A afirmação mais precisa deve ser mais cautelosa: o mundo precisa de Taiwan, dando a Taiwan um conjunto importante de cartas de jogo. Mas as cartas de jogo precisam ser mantidas com defesa nacional, diplomacia, energia, governança industrial e distribuição social.

## Relocar fábricas no exterior não é tão simples quanto mudar de casa

A TSMC abrindo fábricas nos EUA, Japão e Alemanha é frequentemente colocada na mesma ansiedade: se a manufatura avançada for removida, o "Escudo de Silício" de Taiwan se tornará mais fino?

Essa pergunta não pode ser respondida com um simples "sim" ou "não".

A relocação de fábricas no exterior é, por um lado, uma extensão da capacidade de Taiwan. Clientes e aliados estão dispostos a fornecer subsídios, terras e capital político exatamente porque a TSMC e a cadeia de suprimentos de Taiwan são muito importantes. Essas fábricas permitem que a TSMC fique mais próxima dos clientes, e também tornam a cadeia de suprimentos global politicamente mais aceitável.

Por outro lado, a relocação de fábricas no exterior também é um movimento de diversificação de riscos. EUA, Europa e Japão não querem que os chips mais críticos fiquem permanentemente concentrados perto do Estreito de Taiwan. Taiwan é necessária, portanto é investida. Taiwan é muito importante, portanto é dispersa. Essas duas frases são simultaneamente verdadeiras.

Mas uma fábrica não é igual a um ecossistema inteiro. Processos avançados precisam de equipamentos, materiais, produtos químicos, engenheiros, manutenção, experiência de rendimento, capacidade de encapsulamento, colaboração com clientes e velocidade de resposta dos fornecedores. Mover parte da capacidade para fora e mover toda a sociedade de engenharia para fora são duas dificuldades diferentes.

Portanto, a relocação de fábricas no exterior é mais como puxar a cadeia de suprimentos de Taiwan para fora em alguns nós, em vez de arrancar Taiwan da cadeia. Ela mudará lentamente a estrutura de negociação e testará como Taiwan mantém a P&D central, a produção em massa de ponta e a densidade da cadeia de suprimentos.

## Processos maduros também estão no mesmo mapa

A febre da IA容易 fazer as pessoas colocarem toda a atenção em 3 nm, 2 nm e CoWoS. Mas uma máquina de IA não opera apenas com o chip mais avançado.

IC de gerenciamento de energia, controladores, sensores, chips de comunicação de rede, chips periféricos, chips automotivos e industriais, muitos ainda usam processos maduros. Esses chips não vão às notícias como a GPU, mas suportam conversão de energia, controle de sinal, monitoramento de equipamentos e muitas funções insignificantes nos data centers.

Durante a escassez global de chips na pandemia, as linhas de produção automotiva, eletrodomésticos e industriais entenderam uma coisa: o mundo não só precisa de chips mais avançados, mas também pode faltar aqueles nós maduros que parecem comuns, mas sem os quais não se pode entregar. O mapa de semicondutores de Taiwan, portanto, não pode olhar apenas para o topo. TSMC, UMC, Vanguard, JSMC e uma série de empresas de processos especiais, encapsulamento/teste e materiais constituem uma base mais espessa.

Isso é importante para o leitor. O valor de Taiwan não deve ser entendido como uma corrida de números de nanômetros. Quanto mais complexo o hardware de IA, mais precisa de avançado e maduro trabalhando juntos. Mais precisa de整机 e componentes entregues juntos.

Portanto, os processos maduros devem ser colocados de volta no mesmo mapa. É a base sobre a qual o hardware de IA opera de forma estável. A GPU mais avançada precisa ficar sobre muitos chips comuns para se tornar uma máquina verdadeiramente utilizável, mantida e produzida em massa.

## A conta do grupo de "Montanhas Sagradas de Proteção da Nação"

Conectar toda a demanda de hardware de IA do mundo a Taiwan também deixa a conta em Taiwan.

A primeira conta vista é a eletricidade. Fábricas de _wafers_ avançadas, exposição EUV, linhas de encapsulamento, testes de servidores de IA e data centers precisam de eletricidade estável. A mídia tecnológica reportou alertas sobre a pressão da indústria de semicondutores de Taiwan sobre energia verde e fornecimento de eletricidade. A TSMC também continua publicando planos de economia de energia EUV e gerenciamento de recursos hídricos. [^6][^7] A melhoria da eficiência é importante, mas enquanto a demanda de IA continuar a se expandir, a pressão total ainda existe.

A segunda conta é a vulnerabilidade da água e do clima. A fabricação de _wafers_ requer muita água ultra pura. A reportagem da WIRED sobre o uso de água na fabricação de chips aponta que uma única fábrica de _wafers_ pode usar milhões de galões de água por dia; durante a seca em Taiwan, a tensão entre água agrícola e produção de chips também emergiu. A capacidade de processo não pode ser desvinculada de reservatórios, chuva, água reciclada e despacho regional. [^8]

A terceira conta é a emissão de carbono e o bloqueio de caminho industrial. O estudo de Roussilhe et al. usa fabricantes de componentes eletrônicos de Taiwan como amostra, discutindo o aumento de energia, água e emissões de gases de efeito estufa com o crescimento da produção, e o risco de _carbon lock-in_. [^9] O grupo de "Montanhas Sagradas de Proteção da Nação" traz cartas de jogo internacionais, mas também liga profundamente a energia nacional e o uso de terra à manufatura de alta intensidade energética.

A quarta conta é a distribuição. A IA faz a bolsa de Taiwan, exportações e salários da indústria tecnológica subirem, mas nem todos estão nessa cadeia principal de crescimento. Indústrias tradicionais, setor de serviços, inquilinos e jovens não tecnológicos podem não receber os dividendos simultaneamente. Quando preços de imóveis, tarifas de eletricidade, terra e investimento público são todos acionados pela indústria de alta tecnologia, "o futuro de Taiwan é promissor" não é igual a "a vida de cada taiwanês está melhorando".

Isso não é para negar a importância da indústria de semicondutores e da cadeia de suprimentos de IA. Pelo contrário, exatamente porque é importante, a conta precisa ser escrita claramente.

## Onde Taiwan se coloca

A cadeia de suprimentos de hardware de IA dá a Taiwan, além de divisas e pedidos, também uma maneira de se entender.

Taiwan não é uma pequena ilha protegida pelo mundo, nem um império tecnológico que pode controlar unilateralmente a IA do mundo. É mais como um hub de engenharia altamente especializado: necessário, portanto tem cartas de jogo. Dependente, portanto tem responsabilidade. Concentrado, portanto também assume riscos.

Quando o leitor ouvir "Taiwan é insubstituível" da próxima vez, pode não parar apenas no slogan. Pode fazer emergir mentalmente uma via física: a demanda da empresa de modelos entra no design de chips, o design de chips entra no processo da TSMC, o _wafer_ entra no encapsulamento avançado, o módulo de encapsulamento entra na refrigeração, energia, placa-mãe e rack, e finalmente é entregue ao data center pela ODM/EMS de Taiwan.

Essa via é a evidência concreta. Ela transforma o "interesse comum" de emoção em um fato que pode ser discutido, questionado e mantido.

Taiwan transforma a nuvem em máquinas. O verdadeiro significado dessa frase é: a IA mais abstrata, finalmente, ainda precisa passar pela ilha mais concreta.

Esta é uma das posições mais claras e que mais precisa ser vista de Taiwan neste momento.

## Leitura complementar

- [Comércio exterior de Taiwan e cadeia de suprimentos global](/economy/台灣外貿與全球供應鏈) — Contexto macro desde exportação orientada, comércio triangular até reorganização da cadeia de suprimentos EUA-China.
- [NVIDIA em Taiwan](/technology/NVIDIA在台灣) — Como a NVIDIA deposita profundamente a manufatura de chips, encapsulamento e montagem de servidores em Taiwan.
- [Indústria de semicondutores](/technology/半導體產業) — Contexto de longo prazo desde transferência de tecnologia RCA, _foundry_ da TSMC até campo de batalha de materiais e encapsulamento.
- [Computex](/technology/Computex) — Por que a Taipei Computer Expo se tornou o local de peregrinação da oferta de hardware global na era da IA.
- [Energia de Taiwan e semicondutores](/technology/台灣的電力與半導體) — A conta de energia por trás da cadeia de suprimentos de IA, pressão de energia verde e segurança energética.
- [Água de semicondutores e recursos hídricos de Taiwan](/technology/半導體用水與台灣水資源) — Como fábricas de _wafers_ se conectam a reservatórios, seca, água reciclada e governança local.
- [Relocação de fábricas no exterior da cadeia de suprimentos de IA](/technology/AI供應鏈海外設廠) — Desde TSMC, Foxconn, Wistron até Delta, como a cadeia de suprimentos de Taiwan é "pedida para fora" pelo mundo.

## Fontes de imagem

- **Diagrama de fluxo da cadeia de suprimentos de hardware de IA**: Diagrama ilustrativo SVG criado por Contribuidores da Taiwan.md, CC BY-SA 4.0, armazenado em `public/article-images/technology/ai-hardware-supply-chain-flow.svg`. Os nós do diagrama são organizados com base no texto principal e referências deste artigo, servindo para explicar como a demanda de IA entra no data center através de design de chips, processos avançados, encapsulamento avançado, HBM/_substrates_, refrigeração/energia, placa-mãe, ODM/EMS, rack de IA; não é um gráfico de participação de mercado, nem representa um mapa completo de empresas.
- **Diagrama em camadas de servidores de IA**: Diagrama ilustrativo SVG criado por Contribuidores da Taiwan.md, CC BY-SA 4.0, armazenado em `public/article-images/technology/ai-server-rack-stack.svg`. Serve para explicar a hierarquia de sistemas de servidores de IA desde chips até data centers, não representa um mapa completo de empresas ou participação de mercado.
- **Jensen Huang mostrando RTX Blackwell GPU**: [Jensen Huang holding RTX Blackwell at CES 2025](<https://commons.wikimedia.org/wiki/File:Jensen_Huang_-_RTX_Blackwell_-_Nvidia_Keynote_-_CES_2025_Las_Vegas_(3).jpg>) — Foto: Pronoia, Wikimedia Commons, CC0. A versão usada neste artigo está em cache em `public/article-images/technology/jensen-huang-ces-2025-blackwell.webp`.
- **Salão da feira Computex em Nangang**: [Computex Taipei at Taipei Nangang Exhibition Center](https://commons.wikimedia.org/wiki/File:Computex_Taipei_at_Taipei_Nangang_Exhibition_Center_20150602.jpg) — Foto: NVIDIA Taiwan, Wikimedia Commons, CC BY 2.0. A versão usada neste artigo está em cache em `public/article-images/technology/computex-nangang-floor-2015.webp`.

## Referências

[^1]: [CNA: Banquete de Triliões de Jensen Huang acontece; Wei Chieh-chia, Liu Yang-wei, Lin Baili e outros grandes nomes participam](https://www.cna.com.tw/news/afe/202605280300.aspx) — Reportagem da CNA em 28 de maio de 2026 sobre Jensen Huang convidando executivos de alta hierarquia de empresas da cadeia de suprimentos de IA de Taiwan para um jantar em Taipei, listando categorias da cadeia de suprimentos como _foundry_ de _wafers_, encapsulamento/teste, módulos de refrigeração, gerenciamento de energia, placas-mãe, montagem por contrato e marcas.

[^2]: [TSMC Logic Technology](https://www.tsmc.com/english/dedicatedFoundry/technology/logic) — Página de tecnologia de processos lógicos oficial da TSMC, listando processos lógicos avançados de 7 nm, 5 nm, 3 nm, 2 nm, A16, A14 e explicações de rota técnica.

[^3]: [TSMC Advanced Packaging Services](https://www.tsmc.com/english/dedicatedFoundry/services/advanced-packaging) — Página de serviços de encapsulamento avançado oficial da TSMC, explicando que o 3DFabric inclui tecnologias de integração front-end e back-end como SoIC, CoWoS, InFO, etc.

[^4]: [AP: Taiwan takes a further step in production of AI chips with advanced new plant](https://apnews.com/article/1e087e92592b0b9ab7fb20442a5b8dc7) — Reportagem da Associated Press sobre a nova fábrica de Xinhua em Taichung e a participação de Jensen Huang, fornecendo uma perspectiva internacional sobre o papel do encapsulamento avançado de Taiwan na cadeia de suprimentos de chips de IA.

[^5]: [AP: Taiwan's AI-powered economy soars in the shadow of bubble fears and China threats](https://apnews.com/article/7527bd4bf3089cbd2dab1c530ee61c3e) — Reportagem da Associated Press em 2026 sobre a demanda de IA de Taiwan impulsionando crescimento econômico e exportações, ao mesmo tempo organizando limitações como bolha de IA, riscos geopolíticos e desigualdade de renda, adequada como material equilibrado.

[^6]: [Tom's Hardware: TSMC-led semiconductor association warns of power supply pressure](https://www.tomshardware.com/tech-industry/tmsc-led-semiconductor-association-begs-taiwan-government-for-clean-green-energy-as-demand-skyrockets-fabs-are-struggling-to-keep-up-with-power-needs) — Mídia tecnológica reportando alertas da indústria de semicondutores de Taiwan sobre energia verde e fornecimento de eletricidade estável, podendo ser usada como fonte secundária para limitações energéticas e pressão RE100; citação formal ainda deve seguir TSIA ou fonte oficial original.

[^7]: [Tom's Hardware: TSMC reduces peak power consumption of EUV tools by 44%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-reduces-peak-power-consumption-of-euv-tools-by-44-percent-company-to-save-190-million-kilowatt-hours-of-electricity-by-2030) — Reportando o plano de economia de energia EUV da TSMC e a escala total de consumo de energia, adequado para explicar a tensão entre melhoria de eficiência e crescimento total; citação formal precisa对照 dados de sustentabilidade da TSMC.

[^8]: [WIRED: Want to Win a Chip War? You’re Gonna Need a Lot of Water](https://www.wired.com/story/want-to-win-a-chip-war-youre-gonna-need-a-lot-of-water/) — Reportagem da WIRED em 2023 sobre a necessidade de água ultra pura e instalações de tratamento de água para manufatura de semicondutores, mencionando a tensão entre TSMC e água agrícola durante a seca em Taiwan, podendo apoiar o segmento de recursos hídricos deste artigo.

[^9]: [Roussilhe et al.: From Silicon Shield to Carbon Lock-in?](https://arxiv.org/abs/2209.12523) — Estudo de 16 fabricantes de componentes eletrônicos de Taiwan de 2015-2020, propondo aumento de energia, água e emissões de carbono com o crescimento da produção e risco de _carbon lock-in_.

[^10]: [CNA: Liu Yang-wei: Otimista com entrega da plataforma Vera Rubin da NVIDIA no segundo semestre](https://www.cna.com.tw/news/afe/202605290100.aspx) — Reportagem da CNA em 29 de maio de 2026 sobre o presidente da Foxconn, Liu Yang-wei, falando sobre entrega da plataforma Vera Rubin, CPO/fotônica de silício e exibição de sistemas de servidores de IA.
