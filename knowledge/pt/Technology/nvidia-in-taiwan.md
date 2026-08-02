---
title: 'NVIDIA em Taiwan: a empresa mais valiosa do mundo, sem fabricar um único chip'
description: 'Na Computex de maio de 2025, Jensen Huang vestia sua jaqueta de couro e o telão de fundo acendeu os logotipos de 55 empresas taiwanesas — uma companhia americana apontando publicamente a indústria de uma ilha inteira como seu próprio corpo. Da carta de 1996 a Morris Chang até a capitalização de mercado ultrapassar cinco trilhões de dólares e a prefeitura de Taipé desembolsar 44,34 bilhões para lhe liberar um terreno, a NVIDIA depositou todo o seu corpo físico em Taiwan. Taiwan, assim, segura o interruptor que o mundo não pode desligar, mas fica com margem de 5%, vê água e eletricidade serem drenadas e aposta o risco de guerra na ilha: não conseguir se desvencilhar não significa que Taiwan dê as cartas.'
date: 2026-06-22
category: 'Technology'
tags:
  [
    'NVIDIA',
    'Huang',
    'Jensen Huang',
    'IA',
    'semicondutores',
    'TSMC',
    'cadeia de suprimentos',
    'escudo de silício',
    'inteligência artificial',
    'Computex',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-06-22
lastHumanReview: false
researchReport: 'reports/research/2026-06/NVIDIA在台灣.md'
relatedDiary: ['2026-06-22-143854-nvidia-taiwan']
image: '/article-images/technology/computex-jensen-huang-2016.webp'
translatedFrom: 'Technology/NVIDIA在台灣.md'
sourceCommitSha: '67e5b3684'
sourceContentHash: 'sha256:b56a9c2f52721e09'
sourceBodyHash: 'sha256:4f355b3d3c9b0f43'
translatedAt: '2026-08-02T13:22:33+08:00'
---

# NVIDIA em Taiwan: a empresa mais valiosa do mundo, sem fabricar um único chip

> **Resumo em 30 segundos:** A NVIDIA é a empresa mais valiosa do planeta, com capitalização de mercado superando cinco trilhões de dólares em 29 de outubro de 2025[^1], mas não possui uma única fábrica de wafers; cada chip de IA é fabricado pela TSMC, cada servidor de IA é montado pela Foxconn, Quanta e Wistron, e Taiwan responde por nove em cada dez servidores de IA fabricados por encomenda no mundo[^2]. Essa dependência é tão profunda que a NVIDIA já é o maior cliente da TSMC (19% da receita)[^3], a ponto de sua arquitetura de chips ser ditada pela taxa de sucesso das embalagens avançadas de Taiwan[^4]. O problema é que deter a jugular de outrem e repartir os ganhos são coisas diferentes: a NVIDIA tem margem bruta de 75%, enquanto os fabricantes taiwaneses (ODM) ficam com 5% a 8%[^5]. Este artigo explica como essa relação assimétrica chegou ao ponto atual.

![Jensen Huang no palco da Computex Taipei, vestindo sua jaqueta escura característica, com uma grande tela de projeção ao fundo e a plateia lotada](/article-images/technology/computex-jensen-huang-2016.webp)
_Jensen Huang na Computex Taipei 2016. A partir de 2023, ele retorna quase todo ano a esta feira para anunciar os novos chips de IA da NVIDIA, diante da cadeia de suprimentos taiwanesa inteira que os produz. Foto: NVIDIA Taiwan, 2016._

Em 19 de maio de 2025, no Centro de Exposições de Nangang, em Taipé. Jensen Huang subiu ao palco principal da Computex com sua jaqueta de couro característica; ao fundo, o enorme painel traseiro acendeu uma parede de logotipos: Etron, Systex, Delta, Gigabyte, Quanta, Wistron, Wiwynn, Foxconn, MediaTek, TSMC, UMC… um após outro, até fixar-se em 55 empresas taiwanesas[^6]. Somando o vídeo de agradecimento do evento, o total de empresas taiwanesas citadas chegou a 122[^6].

Foi a primeira vez que os taiwaneses "viraram" sua indústria inteira sendo nomeada, de uma só vez, por uma única empresa americana.

O orgulho é real. Mas aquela parede guarda uma pergunta não dita: cada logotipo ali trabalha para esta empresa americana, enquanto o verdadeiro poder está nas mãos de quem ergueu a parede, não nos nomes nela estampados.

<div
  class="video-embed"
  style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;"
>
  <iframe
    src="https://www.youtube.com/embed/TLzna9__DnI"
    title="Keynote de Jensen Huang, CEO da NVIDIA, na COMPUTEX 2025 (vídeo oficial completo)"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    loading="lazy"
    allowfullscreen
  ></iframe>
</div>

_Keynote completo de Jensen Huang na COMPUTEX de 19 de maio de 2025 (canal oficial da NVIDIA). Foi nesta apresentação que a parede de 55 logotipos taiwaneses foi revelada e que a NVIDIA anunciou a instalação de sua sede internacional em Taipé._

## Uma empresa que não fabrica nada, tornada a mais valiosa do mundo

A NVIDIA é o modelo "fabless" (sem fábricas) levado ao extremo. Ela projeta chips, mas não constrói fábricas, não compra máquinas de litografia, não produz um único wafer. Um império de cinco trilhões de dólares sem uma única fábrica de semicondutores em seu nome.

Ela terceirizou inteiramente a manufatura para uma ilha do outro lado do Pacífico.

![Microfotografia do die do GPU NVIDIA Ampere GA102, mostrando a densa estrutura de circuitos](/article-images/technology/nvidia-ampere-ga102-die.webp)
_Micrografia do die do chip NVIDIA Ampere GA102, produzido no processo de 8 nm da TSMC. A NVIDIA o projetou, mas cada uma das linhas densamente compactadas foi gravada nas fábricas de Taiwan. Foto: Fritzchens Fritz, CC0._

Os chips mais lucrativos (H200, Blackwell, o futuro Rubin) dependem todos dos processos de 3 nm e 4 nm da TSMC[^7]. No próprio relatório anual enviado à SEC (Comissão de Valores Mobiliários dos EUA), a NVIDIA admite por escrito essa concentração: sua cadeia de suprimentos está concentrada na Ásia-Pacífico, utilizando foundries como a TSMC para produzir seus wafers[^8]. Esse trecho está num documento legal da empresa para a SEC. Em outras palavras, é a própria NVIDIA que lista Taiwan como sua maior fonte de risco geopolítico.

O chip pronto ainda não basta. Para virar algo que computasse, ele precisa passar por embalagem avançada e ser instalado em servidores. O CoWoS da TSMC é hoje o gargalo global de embalagem avançada, e a NVIDIA sozinha consome cerca de 60% dessa capacidade (estimativas da mídia taiwanesa chegam a 70%)[^9]. Após a embalagem, os chips vão para montagem nas empresas taiwanesas: a Ingrasys da Foxconn monta os sistemas de rack GB200 NVL72, e a Yuanta Investment Consulting estima sua fatia de mercado em montagem de racks de IA acima de 40%[^10]; a Quanta monta servidores em nuvem, com mais de 50% de participação nos 50 maiores data centers[^11]; a nova fábrica de IA da Wistron em Zhubei foi inteiramente absorvida pelos pedidos da NVIDIA[^12].

```tw-stat
75,0% | Margem bruta anual da NVIDIA FY2025 | Relatório anual SEC
19% | Participação da NVIDIA na receita da TSMC 2025 | Superou a Apple como maior cliente
~90% | Participação de Taiwan na fabricação por encomenda global de servidores de IA | Incluindo fornecedores de marcas americanas chega a 100%
~60% | Participação da NVIDIA na capacidade CoWoS da TSMC | Mídia taiwanesa estima 70%
Fonte: NVIDIA SEC 10-K, TrendForce, MIC do III, Ministério da Economia
```

Taiwan responde por 90% da fabricação por encomenda global de servidores de IA; se contarmos também os fornecedores de marcas americanas, chega a 100%[^2]. Isso significa que praticamente cada máquina física que roda IA no planeta passou pelas mãos de trabalhadores taiwaneses.

Empilhando esses números, a contradição central emerge: **a empresa mais valiosa não fabrica nada, porque seu corpo inteiro está depositado em Taiwan**. Taiwan é o interruptor que ela não pode desligar.

Mas segurar a jugular de alguém e tirar proveito disso são duas coisas distintas. A próxima parede está escondida atrás daqueles 55 logotipos.

## O verso da parede de logotipos: o fundo da curva do sorriso

A manufatura tem uma velha "curva do sorriso": as duas pontas são altas, o meio é baixo. Quem controla marca, design e tecnologia nas pontas tem lucros gordos; quem fica no meio com a "montagem e fabricação" tem as margens mais finas. Taiwan ocupa justamente o meio.

A margem bruta anual da NVIDIA no FY2025 foi de 75,0%, segundo seu próprio relatório à SEC[^5]. No mesmo período, as margens das empresas taiwanesas que montam seus servidores eram: Foxconn 6,18%, Quanta 4,78% (mínima de 15 trimestres), Wistron 5,21%, Wiwynn 7,2%[^13]. A margem da NVIDIA é cerca de doze vezes a da Foxconn, dezesseis vezes a da Quanta.

```tw-bars
Quem fica com o lucro: margens brutas da cadeia de IA (%)
*NVIDIA | 75,0 | Design, marca, ecossistema CUDA
Delta | 37,0 | Fontes, refrigeração (ponta tecnológica)
Tripod | 21,3 | Substratos ABF (ponta tecnológica)
Wiwynn | 7,2 | Montagem de servidores
Foxconn | 6,18 | Montagem de sistemas de rack
Wistron | 5,21 | Montagem de servidores
Quanta | 4,78 | Montagem de servidores em nuvem
Fonte: NVIDIA SEC 10-K, conferências de resultados das empresas (FY2025–FY2026)
```

Este gráfico esconde uma contradição intuitiva. Entre as empresas taiwanesas, quanto mais próximo da pura "montagem", menor a margem; quanto mais próximo da "tecnologia", maior a margem. A Delta, que faz fontes e refrigeração, tem 37%; a Tripod, que faz substratos ABF, estima-se 21,3%[^14]. A diferença não está em "ser empresa taiwanesa", mas em "em qual ponto da curva você está". Na montagem, quem quer que faça, a margem é igualmente fina.

> 📝 **Nota do curador**: O Morgan Stanley fez em maio de 2026 uma conta ainda mais cortante — a margem bruta de valor agregado na montagem de sistemas completos pelos ODMs caiu de 2,7% no rack GB300 (geração anterior) para 1,9% no VR200 (próxima geração)[^15]. Ou seja, a cada novo chip mais potente da NVIDIA, as empresas taiwanesas precisam aportar mais capital e veem sua margem encolher. Quanto mais a cadeia avança, mais o fundo da curva é achatado. Os logotipos brilham na parede, as margens murcham no fundo da curva — ambas as coisas são verdadeiras ao mesmo tempo.

Orgulho e custo se puxam na mesma corrente. A bolsa de Taiwan disparou com a IA, e o crescimento econômico de 2025 foi de cerca de 7,37%, o mais rápido em quinze anos, colocando o país entre os líderes globais[^16]. Mas a pesquisadora da economia taiwanesa Chiang Min-hua aponta um número frio: a maioria dos taiwaneses não sentiu os benefícios dessa prosperidade[^16]. Os 10% mais ricos ficam com 48% da renda total, enquanto os 50% mais pobres dividem apenas 12%[^16]. Na prática, a renda per capita do topo 10% é vinte vezes a da base 50%.

Um artigo de opinião no The Reporter de junho de 2026 tornou essa dicotomia em K mais concreta: "a população diretamente empregada na cadeia principal de crescimento de IA, semicondutores e eletrônicos representa menos de 10% do total de ocupados"[^17]. Um trabalhador de alimentação ganha 38.484 novos dólares taiwaneses por mês, apenas 34,6% do que ganha quem trabalha na fabricação de componentes eletrônicos[^17]. O dividendo da IA é real, mas concentra-se no capital e em poucos engenheiros; a maioria assiste à onda do lado de fora.

Este é o primeiro sentido de "não conseguir se desvencilhar não significa dar as cartas": Taiwan segura o interruptor, mas fica com os 5%.

## Taiwan já a segurou, mas também quase a derrubou

Para entender como essa relação assimétrica começou, é preciso voltar aos anos 1990, quando a NVIDIA ainda corria contra a falência.

Fundada em 1993, a NVIDIA esteve à beira do abismo várias vezes nos primeiros anos. Em agosto de 1997, ao lançar o chip gráfico RIVA 128, a empresa tinha "caixa para apenas mais um mês de folha de pagamento"[^18]. Naqueles dias, Huang abria cada reunião mensal com o mesmo lema em inglês: "Nossa empresa está a trinta dias da falência"[^18]. A frase virou crença interna da NVIDIA, mas nunca foi dita em chinês.

Quem realmente puxou a NVIDIA daquela crise foi a Sega, com 5 milhões de dólares — não Taiwan[^19]. Isso precisa ser dito claramente, porque a ideia de que "Taiwan salvou a NVIDIA" costuma ser contada de forma romantizada.

O papel de Taiwan foi outro: o da veia da manufatura. Por volta de 1996, aos 32 anos, Huang escreveu uma carta ao fundador da TSMC, Morris Chang, perguntando se a TSMC poderia fabricar chips para a NVIDIA[^20]. C. Y. Miao (米玉傑), da TSMC, lembrou em 2025 que essa "parceria profunda começou no momento crucial, justamente em 1997", quando "o fundador da TSMC, Morris Chang, contatou pessoalmente o fundador da NVIDIA, Jensen Huang, em resposta ao pedido de serviços de foundry da NVIDIA"[^21]. Em 1998, as duas assinaram o contrato, e a TSMC tornou-se a principal foundry da NVIDIA[^20]. A divisão "design no Vale do Silício, fabricação na TSMC" passou, desde então, a ancorar o corpo da NVIDIA nesta ilha.

> 💡 **Você sabia**: A versão corrente diz que, ao atender o telefonema de Morris Chang, Huang empolgou-se e gritou para os colegas fazerem silêncio, porque era Morris Chang na linha[^22]. A cena é relato de segunda mão, o tom pode não ser exato, mas captura um fato real: aquela pequena empresa à beira do colapso tratou um telefonema da TSMC como uma corda de salvação.

Acontece que essa corda quase virou laço. Em 1998, um processo químico da TSMC deu errado, inutilizando grandes lotes de chips da NVIDIA e quase derrubando a empresa de novo[^23]. Por isso, a descrição mais honesta é: Taiwan não foi o "anjo da falência" da NVIDIA; Taiwan é sua "veia da manufatura" — uma veia de mão dupla, que a segurou e que também quase a estrangulou. Simbiose nunca é gratidão unidirecional.

O resto da história é mais conhecido. Em 2006, a NVIDIA lançou o CUDA; na época, quase todos acharam loucura. Em 2012, o pesquisador Alex Krizhevsky usou duas placas NVIDIA GTX 580 no quarto dos pais para treinar a AlexNet, derrubando a taxa de erro do ImageNet de 26% para 15,3%[^24]. Naquele momento provou-se que GPU é o motor do aprendizado profundo. Em 2022, o ChatGPT explodiu a demanda global por poder de computação, e o valor de mercado da NVIDIA decolou como foguete.

```tw-timeline
1993 | NVIDIA fundada no Vale do Silício | Huang e mais dois, faziam chips gráficos
1996 | Huang escreve a Morris Chang | Pede foundry à TSMC, 1998 assina contrato, corpo ancorado em Taiwan
2006 | Lançamento do CUDA | Transforma GPU em plataforma de computação universal, tido como loucura na época
2012 | AlexNet treinada com duas GTX 580 | Prova GPU = motor do deep learning
2022 | ChatGPT lançado | Demanda global por computação explode, valor da NVIDIA decola
2025 | Valor de mercado passa 5 trilhões | Primeira empresa na história, no mesmo ano anuncia sede internacional em Taiwan
Fonte: The Nvidia Way, podcast Acquired, Wikipédia, CNBC
```

De uma empresa a trinta dias da falência à primeira empresa de cinco trilhões da história — e cada chip do caminho foi feito em Taiwan.

![Jensen Huang no keynote da CES 2025 segurando GPU RTX Blackwell](/article-images/technology/jensen-huang-ces-2025-blackwell.webp)
_Jensen Huang na CES 2025 erguendo a nova GPU Blackwell. Do fundador que todo mês dizia "estamos a trinta dias da falência" até este chip que o mundo disputa — e que ainda só sai de Taiwan. Foto: Pronoia, CC0._

## A indispensabilidade tem prazo de validade?

Chega-se assim a uma pergunta que precisa ser encarada com honestidade: a "indispensabilidade" de Taiwan é permanente ou tem fronteira temporal?

No curto prazo, a fronteira é dura, quase sem frestas. Entre 2025 e 2027, as GPUs de IA mais avançadas da NVIDIA, da fabricação à embalagem final, dependem 100% das linhas CoWoS-L da TSMC dentro de Taiwan[^25]. A TSMC detém cerca de 90% a 92% da capacidade global de processos avançados (5 nm e abaixo), e sua capacidade de embalagem avançada supera a soma de todos os concorrentes[^26]. A pesquisa do professor Chou Yün-tsai (周雲蔡) da Universidade de Ciência e Tecnologia de Taiwan (台科大) é direta: no curto prazo, não é viável diversificar a foundry da TSMC; construir uma nova fábrica de ponta leva três a quatro anos e custa mais de 10 bilhões de dólares[^27].

A evidência de engenharia mais forte não está em relatório algum, mas no próprio design dos produtos da NVIDIA. O Rubin Ultra da próxima geração originalmente previa embalagem de "quatro dies", mas a TrendForce apontou em abril de 2026 que quatro dies fariam a área da embalagem inchar para 7,5 a 8 vezes o limite do retículo, "prejudicando severamente taxa de sucesso e custo", por isso "o design agora migra para arquitetura de dois dies"[^4]. Leia devagar: é o limite físico da taxa de sucesso de embalagem em Taiwan que dita, retroativamente, como o chip da NVIDIA deve ser. Até a maior empresa de design de chips do mundo precisa redesenhar em torno da taxa de sucesso de Taiwan — isso já é um gargalo no nível da física, sem espaço para negociação.

Mas "fronteira dura no curto prazo" não significa "para sempre". Taiwan tem um precedente doloroso.

Em 2002, Taiwan lançou a política industrial "Dois Trilhões, Estrelas Gêmeas", e painéis e DRAM (memória) também foram tratados como veias indispensáveis de proteção nacional. Resultado? Por falta de tecnologia nuclear, o investimento em P&D ficou em 6%, bem abaixo dos 10% a 21% de Coreia, Japão, EUA e Europa; as duas indústrias foram esvaziadas pela Coreia e pela China. O United Daily News resumiu depois com dureza: "As fábricas de painéis e de memória que brilharam por um tempo, poucos anos depois, com excesso de oferta global, levaram as empresas a prejuízos massivos, sendo ironizadas pelos internautas como 'feiticeiros de Maoshan' (margem de três a quatro), ou seja, margem bruta de apenas 3% a 4%; a 'indústria Dois Trilhões, Estrelas Gêmeas' virou 'indústria Dois Trilhões, Coração Partido'."[^28]

> ⚠️ **O que difere desta vez de painéis e DRAM**: Painéis e DRAM foram esvaziados porque Taiwan não detinha a tecnologia nuclear; qualquer um podia alcançar. Desta vez, o fosso da IA parece bem mais fundo — a TSMC de fato detém a propriedade intelectual do processo, a taxa de sucesso do CoWoS e a viscosidade de todo o ecossistema não se replicam com dinheiro em três a cinco anos. Mas isso não é motivo para Taiwan dormir tranquila. A SMIC já anunciou produção em 5 nm, embora com taxa de sucesso apenas um terço da TSMC, custo 50% maior e defasagem de cerca de cinco anos[^29]. Cinco anos, na tecnologia, não é eternidade. Tratar "ser profundamente dependido" como "segurança eterna" foi exatamente o erro da turma de 2002.

A partir de 2028, rachaduras começam a aparecer. Em dezembro de 2025, a NVIDIA investiu cerca de 5 bilhões de dólares na Intel; o verdadeiro objetivo é "garantir acesso prioritário à capacidade de embalagem avançada da Intel nos EUA", prevendo uso na arquitetura Feynman de 2028[^30]. A fábrica de embalagem AP1 da TSMC no Arizona prevê produção em 2028[^31]. A Powertech (力成) de Taiwan desenvolveu o PiFO, embalagem equivalente ao CoWoS-L, com custo de produção cerca de 30% menor, e já tem "várias empresas americanas de chips de IA" batendo à porta[^32]. São movimentos reais de afrouxamento, apenas ainda não entraram na cadeia principal das GPUs mais avançadas da NVIDIA.

Um número ilustra bem a delicadeza atual: a TrendForce estima que o déficit de oferta do CoWoS encolherá dos atuais ~20% para ~10% no fim de 2026[^33]. Mas o déficit encolhe porque a própria TSMC expande capacidade, não porque fornecedores alternativos a preencham[^33]. Ou seja, até hoje, esse gargalo só Taiwan consegue resolver.

A indispensabilidade é fato de engenharia, mas tem uma fronteira dura escrita por volta de 2028. As fichas de Taiwan têm data de validade.

## 44,34 bilhões: uma cidade limpando o terreno para uma empresa de trilhões

Se a margem bruta é a balança abstrata do poder, o que aconteceu no segundo semestre de 2025 no Parque Tecnológico Shilin-Beitou (北士科), em Taipé, é a fatia mais afiada dessa balança.

Tudo começou em 2021. A prefeitura de Taipé colocou em licitação os terrenos T17 e T18 do parque (3,89 hectares no total) com direito de superfície por 50 anos; a Shin Kong Life (新光人壽) arrematou como única licitante por 44 bilhões[^34]. Por três anos, o terreno ficou ocioso, coberto de mato.

Em maio de 2025, Huang anunciou na Computex que a sede internacional "Constellation" da NVIDIA tinha preferência pelo parque[^35]. Mas havia um problema: o direito de superfície ainda estava com a Shin Kong Life, e direitos de superfície públicos não podem ser transferidos diretamente. NVIDIA, Shin Kong Life e prefeitura travaram por cinco meses por causa desse terreno[^36].

A solução final foi a prefeitura pagar para a Shin Kong Life sair. Em 12 de novembro de 2025, o conselho municipal de Taipé aprovou por unanimidade 44,34 bilhões de novos dólares taiwaneses de indenização, pagos pela prefeitura à Shin Kong Life, para retomar o terreno[^37]. O número lido em voz alta: 4.434.064.085 novos dólares taiwaneses[^37].

```tw-figure
NT$4.434.064.085
Indenização paga pela prefeitura de Taipé à Shin Kong Life para retomar o terreno do parque e entregá-lo à NVIDIA (aprovado pelo conselho em 12/11/2025)
Conselho Municipal de Taipé, CNA, Apple Daily
```

A conta de rescisão enviada pela Shin Kong Life incendiou o conselho. A vereadora do KMT, You Shu-hui (游淑慧), ao receber a fatura, escreveu: "Ao ver na fatura de 8 páginas da Shin Kong Life que até corte de grama, manutenção ambiental, ajuste de logotipo, honorários de escriturário etc. são cobrados da prefeitura, só dá para rir amargo. Manutenção ambiental não é dever do inquilino? Até taxa de ajuste de logotipo da fusão Taishin-Shin Kong a prefeitura tem que pagar? É de desmaiar… suspiro triplo de impotência."[^38] Mas ela acabou votando a favor, acrescentando uma frase que resume o clima: "A fatura da Shin Kong Life é inconcebível, mas o grande quadro pesa mais."[^38]

Naquele dia, o conselho viu uma cena rara: azul, verde e branco (KMT, DPP, TPP) em rara harmonia; a bancada do DPP até gritou "Apoie a NVIDIA, assine logo o contrato"[^39]. Um terreno, uma empresa estrangeira, fizeram partidos que vivem se mordendo falar a mesma língua.

> 📝 **Nota do curador**: Vale parar para olhar a estrutura de poder. Para acomodar uma empresa de trilhões de dólares, a prefeitura e o conselho de uma cidade mobilizam dinheiro público, cruzam linhas partidárias, removem todos os obstáculos, e limpam o terreno que um inquilino anterior ocupava. A NVIDIA não pagou esses 44,34 bilhões; o dinheiro saiu dos contribuintes de Taipé antecipadamente (dos quais os custos próprios da Shin Kong Life e impostos já pagos somam 14,41 bilhões, que a NVIDIA se compromete a reembolsar)[^40]. "Não conseguir se desvencilhar não significa dar as cartas" ganha aqui sua forma mais concreta: quando você precisa demais que alguém fique, você acaba pagando contas que não eram suas.

## Sede: vitrine ou raiz fincada?

O que a NVIDIA deu a Taiwan em troca? Precisa separar duas coisas, senão a conta sai errada.

Uma é a "vitrine": a sede Constellation, inspirada na "nave estelar" da sede americana, para cerca de 4.000 pessoas, início das obras em 2026, inauguração só em 2030 — até hoje, nem a terraplanagem começou[^41]. Olhando só isso, duvidar se "a sede não passa de jogada de RP" não é infundado.

A outra é a "raiz fincada há tempos". A NVIDIA não chegou a Taiwan em 2025. Já tem escritório em Neihu, Taipé, com cerca de 1.800 funcionários (estimativa da mídia, não oficial)[^42]. Em 2021, obteve do Ministério da Economia a aprovação do "Plano de Centro de P&D de Inovação em IA", investimento total de 243 bilhões, subsídio governamental de 67 bilhões, meta de contratar 1.000 pesquisadores entre 2022 e 2027[^43]. Em novembro de 2025, constituiu a "NVIDIA Taiwan Classic Co.", capital de 10 bilhões elevado para 33 bilhões — uma pessoa jurídica independente, que pode pagar impostos e deter ativos por conta própria[^44].

Portanto, a verdade da "sede em Taiwan" está no meio: a raiz real de P&D existe, a subsidiária tributável também; mas a nave estelar mais visível continua no papel. As duas metades não podem ser contadas pela metade.

## A ilha sugada por esta cadeia

Além do brilho e das contas, há uma fatura paga por cada morador desta ilha: água, eletricidade, ar, casas inalcançáveis.

![Fachada da fábrica da TSMC em Taichung, prédio cinza com logotipo TSMC](/article-images/technology/tsmc-taichung-factory.webp)
_Fábrica da TSMC em Taichung. O corpo de cada geração de GPU da NVIDIA toma forma em fábricais assim, e a água e a eletricidade que elas sugam são a outra fatura que esta ilha está pagando. Foto: Briáxis F. Mendes, CC BY-SA 4.0._

Olhe a eletricidade. A TSMC consumiu 24,775 bilhões de kWh em 2023, 8,96% de todo o consumo de Taiwan[^45]. A Standard & Poor's projeta que, em 2030, o consumo da TSMC pode chegar a 23,7% do total da ilha[^45]. Ou seja, daqui a poucos anos, a cada quatro kWh gerados em Taiwan, quase um será consumido por esta única empresa.

```tw-line
Participação da TSMC no consumo total de eletricidade de Taiwan: uma empresa, sugando quase 1/4 da energia de uma ilha (%)
Ano | Participação
2023 | 8,96
2030 | 23,7
Fonte: Standard & Poor's, Relatório CSR da TSMC
```

Emissões de carbono acompanham. O Greenpeace, em relatório de abril de 2025 "A Sombra por Trás do Brilho dos Chips", calculou que o consumo global de eletricidade na fabricação de chips de IA saltou de 218 GWh para 984 GWh, alta anual superior a 3,5 vezes; só Taiwan saltou para 375,8 GWh, "respondendo por 38% do total global"[^46]. Como a TSMC depende fortemente de fósseis, sua emissão na fabricação de chips de IA atingiu 185.700 toneladas de CO₂ equivalente, e o Greenpeace a nomeia diretamente "campeã de emissões na fabricação de chips de IA"[^46].

E a NVIDIA? Nota F do Greenpeace. O relatório diz que "as emissões da cadeia de suprimentos da NVIDIA quase triplicaram em três anos, de 3,51 milhões de toneladas em 2022 para 6,91 milhões em 2024", e que ela apenas "transfere as emissões e a poluição da cadeia para outras partes do mundo"[^46]. Em suma: valorização e aura ficam no nome da NVIDIA; carbono e poluição ficam no céu de Taiwan.

Água também. A TSMC usa mais de 200.000 toneladas por dia; as quatro estações de água regenerada de Tainan fornecem 81.000 toneladas/dia, "quase todas para a TSMC"[^47]. O custo recai nos campos: as áreas de Chianan (嘉南) tiveram irrigação suspensa em 2021 e 2023, cedendo água à indústria de semicondutores[^48]. Uma única wafer de 12 polegadas consome 8.327 litros[^49]; nesta ilha, já houve lavouras paradas para que chips tivessem água.

Depois, as casas. Após o anúncio da NVIDIA no parque Shilin-Beitou, os preços imobiliários da região se mexeram. O Departamento de Desenvolvimento Econômico de Taipé projeta 60.000 trabalhadores fixos no parque no futuro, mas o levantamento 591 mostra apenas cerca de 1.476 unidades residenciais à venda (terreno residencial é só 13,8% da área)[^50]. 60.000 pessoas disputando 1.476 unidades — o rumo dos preços é óbvio: reportagens já falam de novos empreendimentos no miolo do parque acima de 1,5 milhão por ping (3,3 m²)[^51].

Aqui convém separar duas coisas, para não contabilizar a ansiedade errada. No registro real de transações, o maior preço de 2025 em Shilin foi 570.400 por m² (≈ 1,88 milhão por ping, base: No. 39, Hehuan Rd., total 447 milhões)[^52]. Mas esses recordes caem em mansões de Tianmu e do centro de Shilin, não no parque em si; o "novo empreendimento no parque acima de 1,5 milhão por ping" é outro número, da mídia. Não se deve misturar. Mas ambos apontam a mesma sensação: o crescimento acontece na minha rua, eu é que não compro.

> ⚠️ **"A empresa nem começou a obra, por que sobe?"**: A reação dos moradores é concreta. Um empresário disse em off que, por falta de infraestrutura de vida no parque, "muitos funcionários não querem se mudar… até dos que vêm, um terço pede demissão, por causa do transporte"[^53]. No PTT, o sentimento anônimo é mais direto: "Antes usaram o tema TSMC até cansar, agora só trocaram pelo tema NVIDIA"[^54]. Uma sede que nem começou a obra já empurra o preço da casa dos locais — esta é a versão mais na mesa de jantar da dicotomia em K. Honestidade exige: a IA pôs Taiwan no mapa mundial é verdade; água e eletricidade sugadas, casas inalcançáveis, também são verdade; as duas precisam ser escritas.

## Quem não consegue se desvencilhar não é só Taiwan

Afaste a câmera, e aparece algo maior: nessa relação NVIDIA-Taiwan, "não conseguir se desvencilhar" é bilateral, até multilateral. Até do outro lado do estreito, todos estão presos nessa estrutura.

![Centro de Exposições de Nangang, Computex, corredores largos com estandes de empresas de TI e multidão](/article-images/technology/computex-nangang-floor-2015.webp)
_Centro de Exposições de Nangang na Computex. Todo junho, compradores do mundo inteiro invadem este pavilhão pelo que esta cadeia de Taiwan produz — quem não consegue se desvencilhar nunca foi só Taiwan. Foto: NVIDIA Taiwan, CC BY 2.0._

É o conceito do "escudo de silício": Taiwan controla os chips de que o mundo precisa, e essa indispensabilidade vira uma camada de proteção. Mas o escudo sempre tem dois lados. É ao mesmo tempo amuleto e paiol de pólvora amarrado à ilha. A academia chama as duas faces de "Silicon Shield" (escudo de silício) e "Silicon Trap" (armadilha de silício): a mesma concentração pode dissuadir a invasão, mas também pode virar incentivo à invasão ou ponto único de falha[^55].

Um debate mais agudo surgiu em 2021 num artigo do U.S. Army War College, defendendo a estratégia extrema de "terra arrasada / ninho quebrado": se a China invadir, destruir a própria indústria de semicondutores para que o invasor não leve nada. Mas as contra-argumentações têm igual força: mesmo que a autodestruição econômica dissuada a China no curto prazo, pode apenas adiar a invasão até o dia em que a China consiga produzir seus próprios chips; e o povo taiwanês dificilmente veria essa autossabotagem como seu interesse[^56]. Não é a Taiwan que cabe julgar, mas essa tensão paira de verdade por trás de toda discussão sobre "Taiwan tem ou não fichas".

O próprio escudo está sendo diluído pela TSMC. Para dispersar risco geopolítico, a TSMC investe 165 bilhões de dólares em expansão nos EUA[^57]. O MIT Technology Review de agosto de 2025 titula "O escudo de silício de Taiwan pode estar enfraquecendo"[^58]. O temor: a migração de capacidade dilui as fichas de Taiwan em solo próprio, fazendo EUA e outros acharem que Taiwan já não vale tanto defender[^58]. Mas Bonnie Glaser (葛來儀), do German Marshall Fund, lembra que esse ecossistema não se copia fácil: "O ecossistema que eles criaram é verdadeiramente único. É função do pipeline de talentos, da cultura e das leis de Taiwan; não dá para replicar facilmente em nenhum lugar."[^59]. Paul Triolo, especialista em tecnologia chinesa, é mais direto — sobre fabricação de ponta, "o Arizona ainda está longe, e nunca vai chegar lá"[^60].

O que melhor ilustra a assimetria dessa dependência é um momento político.

Em 29 de maio de 2024, Huang disse publicamente em Taiwan: "Taiwan is one of the most important countries in the world." (Taiwan é um dos países mais importantes do mundo.)[^61] Dias depois, em 2 de junho, na NTU (Universidade Nacional de Taiwan), descreveu "Taiwan é o herói anônimo, mas o pilar do mundo"[^62].

```tw-quote
Taiwan é o herói anônimo, mas o pilar do mundo
Jensen Huang | CEO da NVIDIA, palestra na NTU na Computex, 2024
```

Dezoito dias depois, o porta-voz do Gabinete de Assuntos de Taiwan da China, Chen Binhua (陳斌華), respondeu: "Quanto a essa observação extremamente errada, o povo e os internautas do continente já expressaram forte insatisfação. Taiwan nunca foi um país… Espero que ele estude mais."[^63]

Mas o revelador é outra coisa. A CNA (Agência Central de Notícias) notou que a mídia financeira chinesa fez ampla cobertura da visita de Huang, mas "não se viu menção à afirmação de Huang de que 'Taiwan é um país importante', como se tivessem omitido o que costuma ser tratado como 'prioridade máxima' em matéria sensível"[^64]. Ou seja: a boca oficial protesta duramente, a mídia financeira escolhe o silêncio.

> 📝 **Nota do curador**: Esse silêncio vaza onde o poder realmente está. A China precisa dos chips da NVIDIA; por isso, mesmo quando Huang diz o que Pequim menos tolera, a mídia de lá opta por não noticiar, não amplificar, com medo de estragar a relação com este "papa da IA". Circula uma frase: a China precisa da NVIDIA, mas a NVIDIA não precisa da China[^65]. Nessa relação, até o vasto mercado do outro lado do estreito está, em certa medida, com o pescoço preso na cadeia de suprimentos de uma única empresa americana. É exatamente a posição estranha desta ilha: o mundo inteiro, inclusive quem mais quer mudar seu status, não consegue viver sem os chips feitos aqui. Só que "o mundo não vive sem você" e "por isso você está seguro, por isso você manda" continuam sendo duas coisas diferentes. O autor não tira conclusão política por Taiwan, mas essa tensão em si vale que cada leitor pese por conta própria.

## Não conseguir se desvencilhar não significa dar as cartas

Volte àquela parede de 55 logotipos.

Cada nome ali é real. Eles são o corpo da revolução de IA no planeta; sem eles, a NVIDIA de cinco trilhões não entrega um único chip. Essa indispensabilidade é fato de engenharia, não retórica. Taiwan tem razão de se orgulhar.

Mas, vistos assim, o brilho, a valorização, o poder de decisão, ficam nas mãos de quem ergueu a parede; os 5% de margem, a água e a eletricidade sugadas, os preços empurrados ao inalcançável, o risco de guerra apostado na ilha, caem nos nomes da parede. Taiwan segura o interruptor que o mundo não pode desligar, mas não por isso dá as cartas. E essa ficha ainda tem validade por volta de 2028.

Taiwan não está parada. Lai Ching-te (賴清德) propôs em 2025 tornar Taiwan "um dos cinco maiores centros de computação do mundo" e desenvolver "IA soberana"[^66]; a Foxconn constrói em Kaohsiung um supercomputador nacional com 10.000 chips Blackwell[^67]; os "Dez Novos Grandes Projetos de IA" do Executivo preveem investir mais de 100 bilhões, visando 15 trilhões de valor de produção[^68]. É a tentativa de, dentro do "fabricar para outros", fazer nascer o "computar para si": subir um degrau na curva do sorriso.

Só que o caminho ainda é longo. O modelo de linguagem próprio de Taiwan, o TAIDE, é descrito como "nível ensino médio", enquanto os gigantes internacionais já estão no "nível pós-graduação"[^69]. A Coreia do Sul comprou de uma vez 260.000 GPUs; Taiwan ainda negocia um terreno, uma indenização[^70]. De receber um telefonema de Morris Chang a receber o poder de computação do mundo, Taiwan levou quase trinta anos para chegar à parede. Mas estar na parede e segurar a caneta são duas coisas.

A parede vai continuar acesa. Na próxima Computex, o painel traseiro de Huang terá ainda mais logotipos. Em 2026, ele revelou que o gasto anual da NVIDIA em Taiwan já beira 150 bilhões de dólares, cinco anos atrás eram apenas 10 a 15 bilhões[^71]. "Taiwan é importante ou não" já tem resposta. A pergunta mais difícil que Taiwan precisa responder é: quando o mundo todo não vive sem o que você faz, como você faz "não viver sem" virar, devagar, "quem manda sou eu".

Os nomes na parede só aumentam. Quem segura a caneta vai trocar para si mesmo — esta caneta, Taiwan só agora começa a buscar.

---

**Leitura complementar**:

- [Jensen Huang: do menino que limpava banheiros ao papa da jaqueta de couro de cinco trilhões](/pt/people/jensen-huang) — História de vida do fundador da NVIDIA, este artigo só toca de leve; sua família em Tainan e trajetória estão aqui
- [Indústria de semicondutores](/pt/technology/taiwan-semiconductor-industry) — Por que Taiwan virou o centro global de fabricação de chips, a cadeia de suprimentos deste artigo tem aqui o fio condutor completo
- [Empresa de Taiwan: TSMC](/pt/economy/tsmc) — Aquela que fabrica cada chip da NVIDIA, a "montanha sagrada de proteção nacional", e seu outro lado sugado
- [Morris Chang: o destinatário daquela carta, e o império de foundry que ergueu](/pt/people/tsmc-morris-chang) — Quem recebeu a carta de Huang em 1996, o fundador da TSMC
- [Computex: como a feira de computadores de Taipé virou a cerimônia de abertura global da IA](/technology/Computex) — O palco onde a parede de logotipos acendeu, o campo principal anual da tecnologia de Taiwan
- [Indústria de IA](/pt/technology/artificial-intelligence-industry) — De fabricar chips da NVIDIA a construir ecossistema de IA, a posição de Taiwan na onda
- [Desenvolvimento de IA em Taiwan e estratégia futura](/technology/台灣人工智慧發展與未來策略) — IA soberana, TAIDE e a ambição nacional de Taiwan de subir da fabricação por encomenda
- [Empresa de Taiwan: Foxconn](/pt/economy/foxconn-precision-industry) — O gigante que monta 40% dos racks de IA do mundo, aquelas mãos maiores no fundo da curva do sorriso

## Créditos das imagens

- [Jensen Huang na Computex Taipei](https://commons.wikimedia.org/wiki/File:Jensen_Huang_at_Computex_Taipei_20160531c.jpg) — Foto: NVIDIA Taiwan, 2016, CC BY 2.0 (imagem principal, Huang no palco da Computex)
- [Die do GPU NVIDIA Ampere GA102](<https://commons.wikimedia.org/wiki/File:Nvidia@8nm@Ampere@GA102@GeForce_RTX_3090@S_TW_2032A1_SNNB9W.000_GA102-300-A1_DSC06025-DSC06107_(50740715646).jpg>) — Foto: Fritzchens Fritz, CC0 (micrografia do die)
- [Jensen Huang segurando RTX Blackwell na CES 2025](<https://commons.wikimedia.org/wiki/File:Jensen_Huang_-_RTX_Blackwell_-_Nvidia_Keynote_-_CES_2025_Las_Vegas_(3).jpg>) — Foto: Pronoia, CC0
- [Fábrica da TSMC em Taichung](https://commons.wikimedia.org/wiki/File:TSMC_logo_on_Taichung_factory_building.jpg) — Foto: Briáxis F. Mendes, CC BY-SA 4.0
- [Computex Taipei no Centro de Exposições de Nangang](https://commons.wikimedia.org/wiki/File:Computex_Taipei_at_Taipei_Nangang_Exhibition_Center_20150602.jpg) — Foto: NVIDIA Taiwan, 2015, CC BY 2.0
- Vídeo: [Keynote de Jensen Huang, CEO da NVIDIA, na COMPUTEX 2025](https://www.youtube.com/watch?v=TLzna9__DnI) — Canal oficial da NVIDIA no YouTube

## Referências

[^1]: [NVIDIA becomes first company to hit $5 trillion market cap](https://www.cnbc.com/2025/10/29/nvidia-5-trillion-market-cap.html) — CNBC, 29 de outubro de 2025, a NVIDIA torna-se a primeira empresa na história a ultrapassar cinco trilhões de dólares de capitalização, impulsionada pela demanda por computação de IA.

[^2]: [Taiwan responde por 90% do mercado global de servidores de IA](https://technews.tw/) — Dados do Ministério da Economia e do MIC do III, a indústria de servidores de Taiwan já respondia por mais de 80% das remessas globais, e a fabricação por encomenda de servidores de IA já atinge 90%; incluindo fornecedores de marcas americanas, chega a 100%; fator determinante: clientes americanos exigem produção fora da China.

[^3]: [TrendForce: NVIDIA vira maior cliente da TSMC](https://www.trendforce.com/) — TrendForce, 1º de junho de 2026, "Cliente A" (NVIDIA) sobe de 12% em 2024 para 19% em 2025 na receita da TSMC, superando Apple (22%→17%) como maior cliente. Fonte primária: relatório anual da TSMC 2025 (investor.tsmc.com).

[^4]: [TrendForce: Rubin Ultra adota arquitetura de dois dies](https://www.trendforce.com/news/) — TrendForce, 1º de abril de 2026, embalagem de quatro dies faria área inchar para 7,5–8 vezes o limite do retículo, "prejudicando severamente taxa de sucesso e custo", por isso design migra para dois dies; IA ocupará 36% da capacidade de 3 nm em 2026, contra 5% em 2025. Limite físico da taxa de sucesso de embalagem dita diretamente a arquitetura do chip.

[^5]: [NVIDIA FY2025 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581025000023/nvda-20250126.htm) — Relatório anual da NVIDIA à SEC, margem bruta GAAP FY2025 de 75,0% (FY2024 foi 72,7%).

[^6]: [Resumo da palestra de Huang na Computex 2025: parede de 55 logotipos taiwaneses](https://money.udn.com/money/story/5612/8750451) — Compilação do Economic Daily News, lista textual das 55 empresas taiwanesas no painel traseiro (Etron, Systex, Delta… TSMC, UMC, Tripod, Wistron, Wiwynn, Auras), outra reportagem diz que painel mais vídeo de agradecimento somam 122.

[^7]: [Dependência da NVIDIA dos 3/4 nm da TSMC](https://www.ainvest.com/news/) — Análise de indústria, H200, Blackwell, Rubin da NVIDIA dependem todos dos processos de 3 nm e 4 nm da TSMC, criando duplo gargalo de fabricação e embalagem.

[^8]: [Divulgação de concentração da cadeia de suprimentos no NVIDIA FY2025 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581025000023/nvda-20250126.htm) — Texto original do relatório: "Our supply chain is mainly concentrated in the Asia-Pacific region. We utilize foundries, such as Taiwan Semiconductor Manufacturing Company Limited, or TSMC... to produce our semiconductor wafers." Risk Factors lista concentração geográfica de fornecedores, foundries, embalagem/teste como risco geopolítico.

[^9]: [Capacidade CoWoS da TSMC e participação da NVIDIA](https://www.financialcontent.com/article/tokenring-2025-12-26-tsmc-boosts-cowos-capacity) — Dados FinancialContent e SiliconAnalysts, NVIDIA responde por ~60% da capacidade CoWoS da TSMC (SiliconAnalysts cita ~595.000 wafers), mídia taiwanesa diz 70% em 2025; top 3 clientes (NVIDIA, Broadcom, AMD) somam >85%.

[^10]: [Participação da Foxconn em montagem de racks de IA >40%](https://vocus.cc/) — Yuanta Investment Consulting estima que Foxconn (Ingrasys) responde por módulos GPU, switch board, compute board e sistemas de rack do GB200 NVL72, fatia >40%; fábrica de Nanqing certificada pelo Fórum Econômico Mundial como primeira lighthouse factory global de servidores de IA (dez/2023).

[^11]: [Quanta tem >50% nos 50 maiores data centers](https://www.artificialintelligence-news.com/news/ai-servers-transform-taiwan-manufacturing-giants/) — AI News, Quanta (QCT) responde por integração L10 e L11, fatia >50% nos 50 maiores data centers em nuvem, segundo maior montador de servidores do mundo.

[^12]: [Nova fábrica de IA da Wistron em Zhubei totalmente absorvida por pedidos da NVIDIA](https://vocus.cc/) — Reportagem de indústria, Wistron responde por HGX/DGX, seu novo parque de IA em Zhubei "totalmente absorvido pelos fortes pedidos da NVIDIA".

[^13]: [Margens brutas de servidores de IA das empresas taiwanesas em conferências de resultados](https://www.cnyes.com/) — Conferências FY2025–FY2026: Foxconn Q1 FY2026 margem 6,18% (servidores de IA passam de 50% da receita de nuvem/rede), Quanta 4,78% (queda trimestral de 1,54 p.p., mínima de 15 trimestres), Wistron 5,21%, Wiwynn 7,2% (ano anterior 9,4%).

[^14]: [Margens das empresas taiwanesas de segundo nível (Yuanta)](https://vocus.cc/) — Quanto mais na ponta tecnológica, maior a margem: Delta (fontes/refrigeração) fatia >60% em fontes para servidores de IA, Q1 FY2026 margem 37%; Tripod (substratos ABF) fatia >70% em substratos ASIC para IA, único fornecedor atual de placas CoWoP da NVIDIA, margem estimada 21,3%.

[^15]: [Morgan Stanley: margem de valor agregado de montagem dos ODM cai](https://newtalk.tw/) — Newtalk cita Morgan Stanley 22/05/2026, margem bruta de valor agregado na montagem de sistemas completos cai de 2,7% no GB300 para ~1,9% no VR200; valor agregado por rack sobe de ~108 mil USD no GB300 para 149,6 mil USD no VR200. Nota: esta é margem de valor agregado de montagem de sistema completo, dimensão diferente da margem bruta geral da empresa (5–7%).

[^16]: [Taiwan Insight: economia próspera, maioria não sente benefícios](https://taiwaninsight.org/) — Chiang Min-hua (江岷樺), Universidade de Nottingham, 12/01/2026: "most people in Taiwan did not feel the benefits of the thriving economy." "The top 10% earners in Taiwan received 48% of total income, whereas the bottom 50% only received 12%." Crescimento 2025 estimado em 7,37%, entre os líderes globais.

[^17]: [The Reporter: dicotomia em K sob o brilho da IA](https://www.twreporter.org/) — The Reporter, 11/06/2026, artigo de Wang Ying-da (王穎達): "população diretamente empregada na cadeia principal de crescimento de IA, semicondutores e eletrônicos representa menos de 10% do total de ocupados." "Alimentação: 38.484 NTD/mês por pessoa, comparado à fabricação de componentes eletrônicos, apenas 34,6%." Participação de eletrônicos na receita da manufatura sobe de 58,0% para 64,7%.

[^18]: [The Nvidia Way: a trinta dias da falência](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) — Livro de Tae Kim 2024 e podcast Acquired/Sequoia, lema interno "Our company is thirty days from going out of business." (abertura de cada reunião mensal), agosto de 1997, lançamento do RIVA 128, caixa para ~um mês de folha. Lema em inglês, sem versão chinesa textual.

[^19]: [Sega salvou a NVIDIA com 5 milhões de dólares](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) — Podcast Acquired e fontes da história inicial da NVIDIA, quem realmente puxou a empresa da crise financeira no fim dos anos 90 foi a Sega (SEGA) com 5 milhões de dólares, não Taiwan; esclarece a narrativa romantizada de "Taiwan salvou a NVIDIA".

[^20]: [Huang escreve a Morris Chang pedindo foundry](https://www.ettoday.net/) — ETtoday cita que Huang, por volta de 1996, escreveu a Morris Chang perguntando "se a TSMC podia fabricar o primeiro chip da NVIDIA", 1998 assinam contrato de cooperação, TSMC vira foundry principal.

[^21]: [C. Y. Miao da TSMC: parceria profunda começou em 1997](https://technews.tw/) — TechNews, 19/05/2025, Miao recorda: "A parceria profunda começou no momento crucial, justamente em 1997. O fundador da TSMC, Morris Chang, contatou pessoalmente o fundador da NVIDIA, Jensen Huang, em resposta ao pedido de serviços de foundry da NVIDIA."

[^22]: [Cena de Huang atendendo telefonema de Morris Chang (relato de segunda mão)](https://www.businessweekly.com.tw/) — Business Weekly, versão em quadrinhos do livro, Huang atende Chang e grita "Pessoal! Silêncio! É o Morris Chang ligando!" Relato de segunda mão, tom pode não ser exato.

[^23]: [1998: erro de processo da TSMC quase derruba NVIDIA](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) — Podcast Acquired e fontes da história inicial, 1998, um processo químico da TSMC falha, inutiliza grandes lotes de chips da NVIDIA, quase derruba a empresa de novo — confirma o enquadramento de "veia da manufatura, não anjo da falência", simbiose bilateral.

[^24]: [AlexNet treinada com duas GTX 580](https://en.wikipedia.org/wiki/AlexNet) — Wikipédia e Tom's Hardware, 2012, Alex Krizhevsky no quarto dos pais usa duas GTX 580 da NVIDIA para treinar AlexNet, erro ImageNet cai de 26% para 15,3%, vantagem de 10,8 p.p. sobre o 2º lugar, prova GPU = motor do deep learning. CUDA lançado em 2006.

[^25]: [Blackwell/Rubin 100% dependentes do CoWoS-L em Taiwan](https://finance.biggo.com/news/) — Análise de indústria (citando Financial Times), 2025–2027, GPUs de IA mais avançadas da NVIDIA, da fabricação à embalagem final, 100% travadas nas linhas CoWoS-L da TSMC dentro de Taiwan.

[^26]: [TSMC detém ~90–92% da capacidade global avançada](https://www.csis.org/analysis/countering-chinas-challenge-american-ai-leadership) — Análise CSIS, TSMC produz ~92% dos semicondutores mais avançados (≤5 nm) do mundo, capacidade de embalagem avançada supera soma de todos os concorrentes; quase 90% dos clientes dependentes de Taiwan incluem Apple, Amazon, Google, NVIDIA, Qualcomm.

[^27]: [Prof. Chou Yün-tsai da NTUST: curto prazo não dá para diversificar foundry da TSMC](https://www.sciencedirect.com/) — ScienceDirect 2025, Chou Yün-tsai (周雲蔡, 台科大): "Taiwan's supply chain would be particularly vulnerable to a quarantine initiated before 2027" "Diversifying TSMC foundries is not feasible in the short term. Building a new leading-edge fab takes 3–4 years and costs $10B+." Meta de 2 nm no Arizona para 2030.

[^28]: [United Daily News: Dois Trilhões, Estrelas Gêmeas viram Dois Trilhões, Coração Partido](https://udn.com/) — United Daily News retrospectiva: "As fábricas de painéis e de memória que brilharam por um tempo, poucos anos depois, com excesso de oferta global, levaram as empresas a prejuízos massivos, sendo ironizadas pelos internautas como 'feiticeiros de Maoshan' (margem de três a quatro), ou seja, margem bruta de apenas 3% a 4%, a 'indústria Dois Trilhões, Estrelas Gêmeas' virou 'indústria Dois Trilhões, Coração Partido'." Painéis e DRAM com P&D de só 6% (muito abaixo de 10–21% de Coreia, Japão, EUA, Europa) foram esvaziados.

[^29]: [SMIC 5 nm taxa de sucesso só um terço da TSMC](https://technews.tw/2025/03/28/) — TechNews, 28/03/2025: "Wafers de 5 nm da SMIC com mesmo fluxo, preço 50% acima da TSMC, taxa de sucesso só 33% da TSMC por só ter equipamentos DUV"; dez/2025 já anuncia produção, defasagem ~cinco anos.

[^30]: [NVIDIA investe 5 bi USD na Intel para garantir capacidade de embalagem](https://www.intel.com/) — Dez/2025, NVIDIA adquire ~5% da Intel, objetivo real "garantir acesso prioritário à capacidade de embalagem avançada da Intel nos EUA", avaliado para arquitetura Feynman de 2028, resposta ao gargalo CoWoS da TSMC. Cobertura de longo prazo, não substituição imediata.

[^31]: [Fábrica de embalagem AP1 da TSMC no Arizona prevê 2028](https://www.tomshardware.com/) — Reportagem de indústria, AP1/AP2 da TSMC no Arizona iniciam obras inícios 2026, AP1 prevê produção 2028; hoje 100% dos chips (incluindo os feitos em Phoenix) ainda voltam a Taiwan para embalagem. Fábrica da Amkor no Arizona prevê início 2028.

[^32]: [PiFO da Powertech equivalente ao CoWoS-L](https://www.trendforce.com/news/) — TrendForce, 10/11/2025: "PiFO advanced packaging technology—benchmarked against TSMC's CoWoS-L—has emerged as the industry's top alternative", substrato de vidro dissipa melhor, custo ~30% menor, várias empresas americanas de chips de IA disputando, pedidos agendados até 2027. Mas clientes são "outras empresas americanas de chips de IA", não explicitamente GPUs principais da NVIDIA.

[^33]: [TrendForce: déficit CoWoS encolhe por expansão própria da TSMC](https://www.trendforce.com/news/) — TrendForce, 15/06/2026: "the CoWoS supply-demand gap is expected to narrow significantly from around 20% currently to about 10% by the end of 2026", capacidade mensal 2026 pode chegar a 120k–140k wafers, recorde; encolhimento do déficit vem da própria expansão da TSMC, não de fornecedores alternativos.

[^34]: [Shin Kong Life arremata direito de superfície T17/T18 do parque em 2021](https://www.cna.com.tw/news/afe/202510035002.aspx) — CNA, 2021, prefeitura de Taipé licita T17, T18 (3,89 ha total) com direito de superfície 50 anos (sem exigência de plano de investimento), Shin Kong Life leva T17 28 bi, T18 16 bi (total 44 bi), única licitante, três anos ocioso.

[^35]: [Huang anuncia sede Constellation no parque na Computex 2025](https://focustaiwan.tw/business/202505190009) — Focus Taiwan, Huang na Computex 2025 anuncia sede internacional "Constellation" da NVIDIA de olho no parque Shilin-Beitou, investimento >400 bi NTD, obras 2026, inauguração 2030, >10 mil vagas.

[^36]: [NVIDIA, Shin Kong Life, prefeitura travados cinco meses](https://news.pts.org.tw/article/777650) — PTS, porque direito de superfície T17/T18 está com Shin Kong Life, direito público não transferível diretamente, três partes travam ~cinco meses na aquisição do terreno.

[^37]: [Conselho municipal aprova 44,34 bi de indenização](https://www.cna.com.tw/news/afe/202510035002.aspx) — CNA, 12/11/2025, conselho de Taipé aprova por unanimidade 4.434.064.085 NTD de indenização, prefeitura paga à Shin Kong Life, retoma terreno, baixa do registro em 28/12.

[^38]: [You Shu-hui critica fatura de rescisão da Shin Kong Life](https://www.nextapple.com/) — Apple Daily (verificado via WebFetch), You Shu-hui textual: "Ao ver na fatura de 8 páginas da Shin Kong Life que até corte de grama, manutenção ambiental, ajuste de logotipo, honorários de escriturário etc. são cobrados da prefeitura, só dá para rir amargo… Até taxa de ajuste de logotipo da fusão Taishin-Shin Kong a prefeitura tem que pagar? É de desmaiar… suspiro triplo de impotência." Seguido: "A fatura da Shin Kong Life é inconcebível, mas o grande quadro pesa mais."

[^39]: [Legal Plain Language: conselho aprova harmoniosamente](https://plainlaw.me/) — Movimento Legal Plain Language, "12/11, conselho de Taipé aprova caso de 44,34 bi, processo harmonioso entre partidos, bancada do DPP até grita 'Apoie a NVIDIA, assine logo o contrato'"; presidente Dai Xi-qin (戴錫欽) "sem opinião, manda arquivar", palmas no plenário.

[^40]: [Análise da composição dos 44,34 bi](https://www.nextapple.com/) — Apple Daily e contadores contratados pela prefeitura, Shin Kong Life pagou ~33 bi originalmente (3 anos sem obra), apresentou fatura de 44,7 bi (inclui corte de grama, ajuste de logotipo, cercamento), contadores cortaram ~400 mi, fixaram 44,34 bi, dos quais custos próprios da Shin Kong Life + impostos já pagos = 14,41 bi, cobertos pela NVIDIA.

[^41]: [Comissão de planejamento aprova design da sede Constellation](https://www.cna.com.tw/news/) — CNA, 26/01/2026, T17 (2,29 ha) + T18 (1,6 ha) unificados, taxa de ocupação 50%→70%, índice de aproveitamento 300%, altura 119,5 m, inspirado na "nave estelar" da sede EUA, cobertura verde 80%, ~4.000 pessoas, obras fim 2026, inauguração 2030.

[^42]: [NVIDIA Taiwan tem ~1.800 funcionários](https://www.digitimes.com/news/a20250519PD231/) — Digitimes e outros estimam, escritório em Neihu, Taipé (No. 8, Jihu Rd.) com ~1.800 pessoas, três subsidiárias; estimativa da mídia, não oficial.

[^43]: [Plano de Centro de P&D de Inovação em IA da NVIDIA](https://focustaiwan.tw/business/202505190009) — Focus Taiwan e Ministério da Economia, NVIDIA 2021 obtém aprovação do "Plano de Centro de P&D de Inovação em IA", investimento total 243 bi, subsídio 67 bi, 2022–2027 contratar 1.000 pesquisadores.

[^44]: [NVIDIA Taiwan Classic Co. constituída](https://www.cna.com.tw/news/afe/202510035002.aspx) — CNA, NVIDIA em 11/2025 constitui "NVIDIA Taiwan Classic Co.", capital de 10 bi para 33 bi, pessoa jurídica independente, pode pagar impostos e deter ativos.

[^45]: [S&P: TSMC pode chegar a 23,7% do consumo de Taiwan em 2030](https://theinitium.com/20250912-international-tsmc-energy-explainer/) — The Reporter e Standard & Poor's, TSMC 2023 consumiu 24,775 bi kWh, 8,96% do total (16,2% do setor industrial), 2024 consumiu 27,456 bi kWh, renováveis só 14,1%; S&P projeta 2030 em 23,7%.

[^46]: [Greenpeace "A Sombra por Trás do Brilho dos Chips"](https://www.greenpeace.org/taiwan/press/44037/) — Greenpeace, 10/04/2025 (textual): consumo global fabricação chips IA de 218 GWh para 984 GWh (alta >3,5×), Taiwan salta para 375,8 GWh "respondendo por 38% do total global"; emissões TSMC chips IA 185.700 t CO₂eq vira "campeã de emissões"; NVIDIA nota F, emissões cadeia triplicam em 3 anos de 3,51 mi t para 6,91 mi t, "apenas transfere emissões e poluição da cadeia para outras partes do mundo".

[^47]: [Água regenerada de Tainan quase toda para TSMC](https://theinitium.com/20250912-international-tsmc-energy-explainer/) — The Reporter, TSMC usa >200 mil t/dia (Hsinchu 5,6, Taichung 5,3, Tainan 9,9 mil t); quatro estações de Tainan fornecem 81 mil t/dia "quase todas para TSMC".

[^48]: [Chianan suspende irrigação 2021 e 2023 cedendo água a semicondutores](https://theinitium.com/) — The Reporter e outros, áreas agrícolas de Chianan em 2021 e 2023 duas vezes suspendem irrigação, desviam água agrícola para indústria de semicondutores.

[^49]: [Uma wafer de 12 polegadas precisa 8.327 litros](https://www.greenpeace.org/taiwan/) — Greenpeace e dados de indústria, fabricação de uma wafer de 12 polegadas consome ~8.327 litros.

[^50]: [Parque projeta 60 mil trabalhadores para 1.476 unidades](https://house.udn.com/house/story/123590/8769929) — Economic Daily News imóveis, Dept. Desenvolvimento Econômico de Taipé projeta 60 mil trabalhadores fixos no parque, levantamento 591 mostra ~1.476 unidades à venda, terreno residencial só 13,8% da área.

[^51]: [Novo empreendimento no miolo do parque acima de 1,5 mi por ping](https://www.ctee.com.tw/news/20260603701575-430601) — Commercial Times, 06/2026, novo empreendimento no miolo do parque fecha acima de 1,5 milhão por ping, "60 mil pessoas por 1.500 unidades", moradores temem congestionamento estilo Neihu, questionam "empresa nem começou obra, por que sobe?"

[^52]: [Registro real: Shilin maior transação 1,88 mi por ping](https://lvr.land.moi.gov.tw/) — Portal de Consulta de Preços Reais de Imóveis do Ministério do Interior, 2025 Shilin maior transação residencial 570.400 por m² (≈ 1,88 mi por ping, No. 39, Hehuan Rd., total 447 mi), várias acima de 1,5 mi/ping. Nota: são mansões de Tianmu e centro de Shilin, não o parque em si.

[^53]: [Empresário: infraestrutura fraca, 1/3 dos funcionários pede demissão](https://house.udn.com/house/story/123590/8769929) — United Daily News imóveis cita empresário (anonimo): "Por infraestrutura fraca, muitos funcionários não querem vir para o parque… até dos que vêm, um terço pede demissão, por causa do transporte"; diretor de transporte Xie Ming-hong (謝銘鴻) diz que parque avalia adicionar 3 linhas de ônibus.

[^54]: [PTT anônimo: só trocaram tema TSMC por tema NVIDIA](https://www.ptt.cc/) — Discussão anônima PTT (não rastreável individual, como sentimento anônimo): "Antes usaram o tema TSMC até cansar, agora só trocaram pelo tema NVIDIA" "Neihu cheio de engenheiros morando fora, NVIDIA vem pro parque e todo mundo vai se mudar? Lógica não fecha?"

[^55]: [Debate escudo de silício vs armadilha de silício](https://www.researchgate.net/) — ResearchGate 2025 "Silicon Shield or Silicon Trap?", explora a dupla face da concentração de chips de Taiwan: proteção dissuasória (escudo) e incentivo à invasão / ponto único de falha (armadilha).

[^56]: [Contra-argumentos à estratégia ninho quebrado / terra arrasada](https://thenewslens.com/) — The News Lens e U.S. Army War College Parameters (McKinney & Harris, 2021) "Broken Nest" e contra-argumentos: "Autolesão econômica, mesmo se dissuadir China no curto prazo, pode só adiar agressão até China atingir metas domésticas de semicondutores" "é improvável que o público taiwanês veja tal sabotagem como seu interesse".

[^57]: [TSMC expansão EUA 165 bi USD](https://www.foreignaffairs.com/) — TSMC anuncia investimento total 165 bi USD no Arizona (65 bi + 100 bi) para dispersar risco geopolítico.

[^58]: [MIT Tech Review: escudo de silício de Taiwan pode estar enfraquecendo](https://www.technologyreview.com/) — MIT Technology Review, 15/08/2025 "Taiwan's silicon shield could be weakening": "Now some Taiwan specialists and some of the island's citizens are worried that this 'silicon shield,' if it ever existed, is cracking." Teme que migração de capacidade dilua fichas de Taiwan em solo próprio.

[^59]: [Glaser: ecossistema de Taiwan difícil de copiar](https://www.technologyreview.com/) — MIT Tech Review cita Bonnie Glaser (葛來儀), German Marshall Fund: "The ecosystem they created is truly unique. It's a function of the talent pipeline, the culture, and laws in Taiwan; you can't easily replicate it anywhere."

[^60]: [Triolo: Arizona nunca chega lá](https://www.technologyreview.com/) — MIT Tech Review cita Paul Triolo sobre fábrica da TSMC no Arizona: "Arizona ain't that yet, and never will be."

[^61]: [Huang: Taiwan é um dos países mais importantes do mundo](https://www.cna.com.tw/) — CNA múltiplas fontes, Huang 29/05/2024 em Taiwan diz publicamente: "Taiwan is one of the most important countries in the world." (original em inglês).

[^62]: [Palestra na NTU Computex 2024: Taiwan herói anônimo, pilar do mundo](https://www.tbotaiwan.com/) — Transcrição completa da palestra de Huang na NTU na Computex 2024, final do vídeo textual: "Taiwan é o herói anônimo, mas o pilar do mundo." "Obrigado, Taiwan!" "Taiwan é a concentração de nossos parceiros mais preciosos, tudo da NVIDIA começa aqui."

[^63]: [Gabinete de Assuntos de Taiwan Chen Binhua responde a Huang](https://zh.wikinews.org/) — Wikinews, porta-voz Chen Binhua (18 dias depois): "Quanto a essa observação extremamente errada, o povo e os internautas do continente já expressaram forte insatisfação. Taiwan nunca foi um país… Espero que ele estude mais."

[^64]: [CNA: mídia chinesa silencia "Taiwan é país importante" de Huang](https://www.cna.com.tw/) — CNA, 03/06/2024: "A mídia financeira daqui fez ampla cobertura, mas não se viu menção à afirmação de Huang de que 'Taiwan é um país importante', como se tivessem omitido o que costuma ser 'prioridade máxima' em matéria sensível."

[^65]: [Especialista: China precisa da NVIDIA, mas NVIDIA não precisa da China](https://www.voacantonese.com/a/china-s-media-turned-a-blind-eye-to-jensen-huang-s-statement-20240607/7646642.html) — VOA Cantonês cita especialista, analisa que silêncio da mídia financeira chinesa sobre fala de Huang reflete "China precisa da NVIDIA, mas NVIDIA não precisa da China", relação assimétrica.

[^66]: [Lai Ching-te: top 5 centros de computação globais e IA soberana](https://www.bnext.com.tw/article/79391/sovereign-ai) — Digital Era, Lai Ching-te 10/2025 propõe Taiwan como "um dos cinco maiores centros de computação do mundo", desenvolver "IA soberana".

[^67]: [Foxconn constrói supercomputador nacional com 10 mil Blackwell](https://blogs.nvidia.com.tw/blog/foxconn-ai-factory-tsmc-taiwan-nvidia/) — Blog NVIDIA Taiwan, Foxconn (Big Innovation Company) em Kaohsiung constrói supercomputador nacional com 10.000 chips Blackwell, >90 exaflops, com TSMC e Conselho Nacional de Ciência e Tecnologia, criando primeira fábrica de IA de Taiwan.

[^68]: [Dez Novos Grandes Projetos de IA do Executivo](https://iknow.stpi.niar.org.tw/post/Read.aspx?PostID=21832) — STPI iKnow, Executivo "Dez Novos Grandes Projetos de IA" planeja investir >100 bi NTD até 2040, meta 15 trilhões de valor de produção.

[^69]: [TAIDE nível ensino médio, gigantes nível pós-graduação](https://www.cw.com.tw/article/5137534) — Commonwealth Magazine, modelo de linguagem próprio TAIDE descrito "como ensino médio, gigantes já pós-graduação", orçamento anual do TAIDE nem chega ao custo de um único treino de modelo internacional; TAIDE parte com 9 nós (72 H100).

[^70]: [Coreia do Sul compra 260 mil GPUs](https://www.cw.com.tw/) — Commonwealth Magazine e reportagens, governo coreano compra direto 260.000 GPUs, contrastando com hesitação relativa de Taiwan na decisão política.

[^71]: [Huang Computex 2026: gasto anual em Taiwan ~150 bi USD](https://cryptobriefing.com/nvidia-150b-taiwan-silicon-shield-ai/) — Cryptobriefing e Reuters, Huang na Computex 2026 revela gasto anual da NVIDIA em Taiwan ~150 bilhões USD (cinco anos atrás 10–15 bi), parceiros da cadeia Vera Rubin dobram, incluem 150 empresas taiwanesas; TSMC produz ~90% da capacidade avançada global.
