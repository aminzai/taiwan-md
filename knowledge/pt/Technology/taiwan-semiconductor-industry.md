---
title: 'Semicondutores: A Revolução de 50 Anos dos Materiais, do Transferência de Tecnologia da RCA ao GaN e ao Empacotamento Quântico'
description: 'A montanha sagrada que protege a nação domina os processos avançados globais através da terceirização de fabricação (foundry), mas o campo de batalha da ciência dos materiais para os próximos 50 anos — GaN nas carregadores rápidos, CoWoS sob os chips de IA e refrigeradores de diluição sobre os qubits — acaba de ser armado.'
date: 2026-03-17
category: 'Technology'
tags:
  [
    'semicondutores',
    'TSMC',
    'TSMC',
    'nitreto de gálio (GaN)',
    'empacotamento 3D',
    'CoWoS',
    'computadores quânticos',
    'processos avançados',
    'escudo de silício',
    'ciência dos materiais',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-05-19
lastHumanReview: true
difficulty: 'intermediate'
readingTime: 22
image: '/article-images/technology/silicon-vs-gan-charger-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg'
sporeLinks:
  [
    "{'id': 87, 'platform': 'threads', 'date': '2026-05-25', 'url': 'https://www.threads.com/@taiwandotmd/post/DYvqEURgXm-'}",
    "{'id': 88, 'platform': 'x', 'date': '2026-05-25', 'url': 'https://x.com/taiwandotmd/status/2058735515021783190'}",
  ]
translatedFrom: 'Technology/半導體產業.md'
sourceCommitSha: '6ffd92f94'
sourceContentHash: 'sha256:575572d1dd581d19'
sourceBodyHash: 'sha256:d37164a7592bd08a'
translatedAt: '2026-08-03T15:44:53.861409+00:00'
---

# Semicondutores: A Revolução de 50 Anos dos Materiais, do Transferência de Tecnologia da RCA ao GaN e ao Empacotamento Quântico

![Duas cabeças de carregamento rápido USB-C de 30W lado a lado: à esquerda, o dispositivo de silício tem volume significativamente maior; à direita, o dispositivo de GaN é reduzido em quase metade, refletindo como a ciência dos materiais comprime a densidade de energia na palma da mão](/article-images/technology/silicon-vs-gan-charger-2025.webp)
_Comparação de volume entre carregadores USB-C de Si e GaN de mesma potência. Foto: 4300streetcar, 2025-12-25. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg)._

> **Resumo em 30 segundos:** A TSMC iniciou a produção em massa de 2 nm no quarto trimestre de 2025 na Fab 22 de Kaohsiung, liderando o mundo em 2-3 gerações[^2]. Mas a história não se limita a transistores cada vez menores: o carregador rápido no seu bolso contém nitreto de gálio (GaN), a GlobalWafers fabrica wafers de 8 polegadas de carbeto de silício (SiC) em Zhongli, e a GPU Blackwell da NVIDIA depende inteiramente do empacotamento CoWoS da TSMC para ser enviada aos data centers. De 1973, quando a Academia Sinica gastou US$ 4,5 milhões para adquirir tecnologia da RCA[^5], até 2026, quando o chip quântico supercondutor de 20 qubits da Academia Sinica se conecta à rede[^6], Taiwan percorreu um longo rio da ciência dos materiais, desde a física de band gap até a deposição de filmes atômicos e qubits topológicos. A montanha sagrada que protege a nação baseia-se em 50 anos de experiência, mas a posição de foundry na era quântica ainda não foi conquistada por Taiwan.

Em uma tarde de 1985, o membro do Conselho de Assuntos Administrativos (CASG) Lee Teng-hui procurou Morris Chang, que acabara de retornar a Taiwan para assumir o cargo de presidente da Academia Sinica (ITRI). Lee Teng-hui foi direto: "Queremos criar uma empresa de fabricação de circuitos integrados de grande escala, e você será o líder."

Morris Chang ficou surpreso. Ele achava que viraria apenas presidente da Academia, mas duas semanas depois foi convidado a fundar uma empresa com um modelo de negócios que ninguém jamais tentara comercialmente.

Esse diálogo mudou o mundo. Mas, olhando para trás 40 anos depois, "o mundo" é muito mais denso do que aquela tarde imaginava. Inclui o carregador rápido de 65 watts, do tamanho de dois nós dos seus dedos, ao lado do seu celular; inclui cada GPU Blackwell consumida pela NVIDIA nos data centers; e inclui os qubits nos laboratórios da Academia Sinica que só "acordam" quando resfriados a quase zero absoluto.

## A Aposta de Foundry de 1987

![Exterior da Fab 5 da TSMC no Parque Científico de Hsinchu, um complexo industrial de múltiplos andares conectado à Rua Fuguo, um dos principais parques fabris da TSMC durante a expansão da década de 1990](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Fab 5 da TSMC no Parque Científico de Hsinchu, 2010. Foto: Peellden. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG)._

A história começa antes. Em 1973, a Academia Sinica (ITRI) gastou US$ 4,5 milhões para adquirir tecnologia de circuitos integrados da empresa americana RCA e enviou 19 engenheiros aos EUA para treinamento[^5]. Ninguém naquela época imaginava que esse "custo de matrícula" se tornaria a primeira pedra fundamental do reino dos semicondutores de Taiwan. Em 1980, a Academia Sinica transferiu tecnologia para fundar a United Microelectronics Corporation (UMC), dando a Taiwan sua primeira empresa de semicondutores. Mas Lee Teng-hui não estava satisfeito: a UMC era muito pequena, a tecnologia não acompanhava os padrões internacionais, e Taiwan precisava de um avanço maior.

Em 21 de fevereiro de 1987, Morris Chang fundou a Taiwan Semiconductor Manufacturing Company (TSMC) no Parque Científico de Hsinchu, inaugurando um modelo de negócios sem precedentes: **foundry pura**.

Essa ideia soava louca na época. Todas as empresas de semicondutores do mundo eram verticalmente integradas, do design à fabricação. Como poderia haver uma empresa que apenas fizesse a fabricação, sem design? Os clientes entregariam os desenhos mais confidenciais a você?

A lógica de Morris Chang era simples: a indústria de semicondutores está ficando cada vez mais complexa; design e fabricação são duas especialidades completamente diferentes. Em vez de fazer tudo e não ser bom em nada, foque em fazer uma coisa bem, levando a fabricação de chips ao melhor nível do mundo.

A estrutura acionária inicial da TSMC era engenhosa: governo investiu 48,3%, setor privado 24,2%, e a Philips da Holanda detinha 27,6%[^1]. A participação da Philips foi crucial. Na época, a indústria de semicondutores era dominada por EUA e Japão; a Europa precisava urgentemente de um fornecedor alternativo. A Philips não apenas investiu, mas também entregou seus pedidos de chips à TSMC, tornando-se seu primeiro cliente importante.

O modelo de foundry provocou uma grande divisão na indústria de semicondutores: empresas de design de IC focam no design de chips (Qualcomm, NVIDIA, MediaTek); foundries focam na fabricação (TSMC, UMC, GlobalFoundries); fábricas de empacotamento e teste cuidam do processo final (ASE, SPIL). Anteriormente, apenas gigantes como Intel e IBM podiam arcar com o investimento astronômico de uma fábrica de wafers; agora, qualquer startup com uma boa ideia pode projetar um chip e entregá-lo à TSMC para fabricação.

O cerne do modelo de foundry é a confiança. Os clientes devem acreditar que a TSMC não roubará seus designs, não vazará segredos comerciais e não competirá com eles. A TSMC estabeleceu um "código de confiança" com quatro princípios: neutralidade tecnológica (nunca projetar chips próprios); igualdade de clientes (todos os clientes recebem a mesma tecnologia e serviços); acordos de confidencialidade de nível máximo; e alocação justa de capacidade de produção. Essa regra foi aplicada por quase 40 anos, sem exceções.

> 📝 **Nota da Curadoria**: Em 1987, na Taiwan, os 19 engenheiros enviados pela Academia Sinica (ITRI) da RCA tinham pouco mais de 40 anos. Eles aprenderam o processo de silício dos EUA da década de 1960; ninguém poderia prever que, 30 anos depois, se tornariam o cliente principal da tecnologia de empacotamento do mundo. A cláusula de "auto-castração" pela qual a TSMC decidiu não projetar chips próprios acabou se tornando o vínculo que impossibilita Jensen Huang, Tim Cook e Lisa Su de deixarem a TSMC. A grandeza do modelo de foundry não está no que ele fez, mas no que **escolheu não fazer**. Voltando mais fundo, a invenção do transistor em 1947 pelos Bell Labs, as descobertas independentes de circuitos integrados pela Texas Instruments e Fairchild em 1958, e a chegada de tecnocratas com formação em ciências exatas ao Taiwan após o estabelecimento do governo nacional em 1949 (a espinha dorsal futura da Academia Sinica) — os US$ 4,5 milhões da RCA foram um bastão de corrida, não o ponto de partida.

## Burn J. Lin e a ASML: A Aposta de Dois Meninos na Exposição Aquosa

A foundry não é apenas questão da TSMC. O leitor [@malathrone_21k_running](https://www.threads.com/@malathrone_21k_running) complementou essa linha histórica crucial nos comentários: a linhagem da Philips da TSMC é a mesma da ASML — uma empresa de equipamentos de exposição fundada em 1984 pela separação da Philips da Holanda, hoje o único fornecedor de equipamentos EUV (ultravioleta extremo) do mundo. Ambas as empresas eram "meninos" desprezados pelos gigantes da indústria há 30 anos[^asml-philips].

A chave da história é um engenheiro taiwanês chamado Burn J. Lin. Ele trabalhou em tecnologia de exposição no Centro de Pesquisa Watson da IBM a partir de 1992 e retornou a Taiwan em 2000 para se juntar à TSMC como diretor de P&D[^lin-bio]. Naquela época, a disputa de rota para o próximo passo das máquinas de exposição era a ultravioleta profunda de 157 nm; Nikon e Intel apostaram nessa rota, mas a 157nm apresentou problemas contínuos: lentes de fluorita de cálcio tinham problemas de birrefringência, filmes finos absorviam fortemente esse comprimento de onda, e a integração do processo era difícil[^157nm-fail].

Em 2002, na conferência óptica SPIE, Burn J. Lin propôs uma ideia louca: "Mantenha a fonte de luz de 193 nm, mas encha água entre a lente e o wafer." O índice de refração da água é 1.44; a luz de 193 nm na água equivale a uma resolução de aproximadamente 134 nm — mais fina que 157nm, e sem necessidade de trocar a fonte de luz ou as lentes[^immersion-litho].

A Nikon não acreditou e continuou apostando na 157nm. A ASML estava disposta a apostar — ela também era um "menino", assim como a TSMC, buscando uma alavanca física para reverter o jogo. Em 2003, a ASML começou a desenvolver a máquina de exposição de imersão de 193nm (193i); em 2007, foi a primeira a produzir em massa, sustentando **seis gerações** desde o processo de 65nm até a sucessora EUV de hoje[^immersion-litho][^cw-lin-interview].

"A Nikon tinha medo de calor e não fazia imersão; a ASML e nós tivemos que fazer sozinhos", essa rota tecnológica derrubou a Nikon do trono das máquinas de exposição[^cw-lin-interview]. Há 30 anos, dois meninos apostaram individualmente; hoje, um é a única fábrica de equipamentos EUV do mundo, e o outro é a única foundry de 2nm do mundo. As duas sementes plantadas pela Philips holandesa se encontram no século 21.

## 50 Anos de Linhagem de Materiais: De Silício a GaN a Supercondutores Topológicos

Para entender o campo de batalha dos semicondutores em 2025, primeiro é preciso entender uma linha física que nunca foi claramente explicada.

O Silício (Si) é o ponto de partida dessa linha. Seu "band gap" (gap de energia) é de 1,1 elétron-volt (eV); esta é a energia mínima necessária para um elétron pular da banda de condução para a banda de valência. Band gap pequeno facilita a fabricação de chips, mas há dois tetos: alta tensão causa colapso; alta frequência causa aquecimento. O PanSci explica esse limite claramente: "A frequência de trabalho limite de semicondutores à base de silício está apenas abaixo de 100 kHz; se ultrapassar 100 kHz, a eficiência de conversão cai drasticamente, e há sérios problemas de desperdício de energia."[^7]

O band gap do Nitreto de Gálio (GaN) é de 3,4 eV, três vezes o do silício. O limite de tensão de colapso é 10 vezes o do silício. A frequência de trabalho pode ser esticada para 1000 kHz, uma ordem de magnitude acima do silício[^7]. Traduzindo esses números físicos para a vida real: para a mesma potência, o indutor do transformador do GaN pode ser muito menor, e os requisitos de dissipação de calor são muito menores; assim, o carregador rápido que cabe na palma da mão nasceu.

O Carbeto de Silício (SiC) segue outro caminho. Também é de band gap largo (band gap de 3,26 eV), mas resiste melhor a altas temperaturas e tensões. O PanSci aponta diretamente seu campo de batalha: "O carbeto de silício possui boa estabilidade em altas temperaturas e tensões; especialmente com o aumento da demanda de carregamento rápido de veículos elétricos no futuro, a demanda de carregamento acima de 1000 volts tornará os semicondutores de silício, que só suportam 600 volts, incapazes de suportar a carga, e espera-se que assumam o papel de componente chave nos veículos elétricos."[^7]

> 💡 **Você Sabia?**: O "band gap" dos semicondutores determina quanta tensão eles podem suportar, quão rápida pode ser a frequência e quanto calor geram. O silício de 1,1 eV é a base dos eletrônicos de consumo por 50 anos; o GaN de 3,4 eV sustenta carregadores rápidos de 240W de celulares; o SiC de 3,26 eV entra nos inversores de veículos elétricos de 800V; o próximo passo pode ser o semicondutor de diamante de 5,5 eV. Toda a linhagem de materiais é uma escada de "subir a densidade de energia"; a cada degrau que Taiwan sobe, precisa negociar com os limites físicos da ciência dos materiais.

O próximo passo ainda não tem nome: pode ser diamante (C, band gap de 5,5 eV), óxido de gálio (Ga₂O₃, 4,8 eV), ou entrar em mecanismos físicos completamente diferentes, como supercondutores topológicos (topological superconductor), o caminho que o processador quântico Majorana 1 da Microsoft escolheu em fevereiro de 2025[^15]. A física muda, e toda a cadeia industrial será reescrita.

## O GaN no Seu Carregador Rápido

Aplique o zoom de volta na sua mochila.

O carregador do Nokia 3310 tinha 4,56 watts; o carregador rápido de 2025 tem 240 watts. Uma diferença de 52 vezes. O PanSci organizou essa linha do tempo: "A potência atual dos carregadores rápidos de GaN mais populares chega a 65 watts, uma diferença de 13 vezes; idealmente, o tempo de carregamento também seria reduzido a 1/13."[^7] Mais impressionante ainda é a marca chinesa realme, que lançou o GT Neo5 de 240W no início de 2023, empurrando esse multiplicador para acima de 50.

Essa curva de crescimento depende fisicamente da comutação para o GaN; a espessura dos fios de cobre e o volume da bateria, na verdade, estão diminuindo. Para aumentar a potência e reduzir o volume, o método mais direto é aumentar a frequência de trabalho, mas "a frequência de trabalho limite de semicondutores à base de silício está apenas abaixo de 100 kHz"[^7]; este é o "limite do silício" que o PanSci menciona. O GaN estica a frequência de trabalho para acima de 1 MHz, fazendo o transformador e o indutor encolherem simultaneamente, permitindo que todo o carregador caiba no bolso.

O problema é: quando o mercado de carregadores rápidos de Taiwan estava prestes a explodir, a TSMC anunciou uma coisa: **sairá da foundry de GaN em julho de 2027**[^8].

Por trás dessa decisão há duas pressões. Primeiro, as fábricas chinesas de GaN (China Resources Micro, Silan Micro, Ruineng, etc.) estão expandindo massivamente, pressionando o preço da foundry para um nível que a TSMC não quer atender. Segundo, o lucro dos chips de IA é realmente tentador; a TSMC quer converter as fábricas de GaN em linhas de produção de empacotamento avançado (CoWoS). A tecnologia foi licenciada para a World Semiconductor (VIS) e GlobalFoundries; o fardo da foundry de GaN de Taiwan agora recai sobre a稳懋 (SG Micro, 3163) e a 宏捷科 (MACOM, 8086), empresas que apostaram nisso há dez anos[^8].

> ⚠️ **Ponto de Controvérsia**: A saída da TSMC da foundry de GaN tem duas interpretações externas. Uma facção vê isso como uma escolha racional de "deixar capacidade para a IA"; o lucro por wafer de 3nm é mais de 20 vezes maior que o de GaN de 6 polegadas, então a alocação de capacidade vai naturalmente para onde o retorno é maior. A outra facção questiona: ao abrir mão do GaN, Taiwan está entregando a base da próxima geração de eletrônicos de consumo (celulares / laptops / carregadores) às fábricas chinesas; o "escudo" do escudo de silício não se resume apenas à ponta da IA? A diferença entre as duas partes reside em: você acredita que o valor da montanha sagrada que protege a nação é o "processo mais avançado irreplaceável", ou a "completude do ecossistema da cadeia de suprimentos".

Seja a TSMC, a gigante de wafers GlobalWafers, ou as grandes empresas de semicondutores nacionais e internacionais, todas já embarcaram nesse trem[^7]. Mas em qual vagão subir é uma questão diferente.

## O Wafer de 8 Polegadas de SiC da GlobalWafers

Se o GaN é a história dos carregadores rápidos de celulares, o SiC é a história dos veículos elétricos.

A empresa central da linha SiC de Taiwan é a GlobalWafers, não a TSMC. Em 2024, a capacidade de produção mensal de wafers SiC de 6 polegadas da GlobalWafers atingiu cerca de 20.000 unidades; seus fornos de crescimento de cristais auto-desenvolvidos foram expandidos de 3 para 20, e a taxa de rendimento ultrapassou 50%[^9]. Em 2025, wafers SiC de 8 polegadas entraram em produção em massa, a primeira de Taiwan.

A CEO da GlobalWafers, Hsu Hsiu-lan, fala sempre de forma direta: "O Grupo Zhongmei forma um 'Grupo IDM Virtual', mirando a demanda de carbeto de silício dos próximos 5 anos! Estamos correndo rápido."[^9] A estratégia é vincular o crescimento de cristais (GlobalWafers), epitaxia (Pengcheng), e módulos (Hongyang Semiconductor) sob a matriz Zhongmei em uma única cadeia.

Mas a história do SiC não é uma linha reta. No segundo semestre de 2025, as fábricas chinesas de SiC (San'an Optoelectronics, Tianke Heda, etc.) estão expandindo loucamente, causando excesso de oferta global; a taxa de utilização da capacidade de 6 e 8 polegadas SiC da GlobalWafers caiu abaixo de 50%[^10]. Isso adiciona um vale ao roteiro otimista de 2023 do PanSci sobre a "demanda de veículos elétricos assumindo o controle".

O sinal de recuperação vem da NVIDIA. Rumores indicam que a próxima plataforma de GPU Rubin da NVIDIA adotará SiC na camada de interposição, combinada com uma arquitetura de data center de corrente contínua de alta tensão de 800V, entrando em produção em massa em 2027[^10]. Se esse rumor for verdadeiro, a capacidade de 8 polegadas SiC da GlobalWafers será transferida de veículos elétricos para data centers de IA, reacendendo toda a história.

> 📝 **Nota da Curadoria**: GaN e SiC são frequentemente chamados juntos de "semicondutores de terceira geração", mas esse rótulo no contexto industrial de Taiwan significa mais do que apenas "próximo material" — representa a primeira área em que a indústria de semicondutores de Taiwan tem uma cadeia de suprimentos completa **contornando a TSMC**. Crescimento de cristais da GlobalWafers, fabricação da Han Leong, empacotamento da SG Micro, design da MACOM: além da Montanha Sagrada que Protege a Nação, outro "terceiro pico", mais discreto mas independente, está crescendo.

## O Vínculo de Jensen Huang com o CoWoS+

De volta ao campo de batalha da IA.

A GPU H100 da NVIDIA usa o processo de 4nm da TSMC, combinado com o empacotamento CoWoS-S para integrar a memória HBM3 de alta largura de banda. O Blackwell B200 foi atualizado para CoWoS-L, integrando duas GPUs Blackwell e uma CPU Grace, com velocidade de treinamento de IA 4 vezes mais rápida que a H100[^11]. A próxima geração, Rubin, está prevista para 2026.

O cerne de cada geração de GPU é o motor duplo de "processo avançado + empacotamento avançado". O processo torna os transistores cada vez menores; o empacotamento empilha as diferentes die (chips) cada vez mais próximas. O PanSci usa a comparação entre a Rodovia Provincial 9 (Taijiu) e o Túnel de Xueshan para explicar isso: "O empacotamento tradicional precisa percorrer a sinuosa Rodovia Taijiu, enquanto o empacotamento avançado corta as curvas, abrindo o Túnel de Xueshan que conecta os dois locais, tornando o fluxo de dados mais conveniente e rápido."[^12]

O cerne do CoWoS (Chip-on-Wafer-on-Substrate) é o "via de silício" (through-silicon via, TSV): empilhar diferentes die, penetrando a base de silício com microcanais verticais, transformando dois circuitos originalmente separados em uma conexão 3D. O PanSci descreve de forma direta: "O empacotamento 3D pode colocar o chip C acima do chip A, penetrando a base de silício reduzida através da tecnologia TSV, conectando os dois circuitos com fios de conexão vertical de ultra-alta densidade; a distância entre eles muda de天涯 (extremo) para 咫尺 (próximo)."[^12]

Os números de capacidade são ainda mais impactantes. A capacidade mensal de CoWoS da TSMC era de cerca de 35.000 unidades no final de 2024, com meta de 75.000 no final de 2025, e avançando para 150.000 em 2028, com uma taxa de crescimento anual composta de quase 80%[^13]. A NVIDIA reservou inteiramente a capacidade CoWoS da TSMC até 2027, e **todos os chips, independentemente de onde na TSMC sejam produzidos (incluindo Arizona), devem ser retornados a Taiwan para empacotamento CoWoS**[^13].

Esta é a dupla dominação de Jensen Huang e TSMC. A NVIDIA no design, a TSMC na fabricação e empacotamento; as duas empresas bloqueiam conjuntamente o nó crítico dos data centers de IA.

Em 2 de junho de 2024, no discurso de abertura da Computex no Ginásio da Universidade Nacional Taiwan, Jensen Huang revelou publicamente esse vínculo ao mundo — os slides mostravam o roteiro de Blackwell e Rubin, mas por trás de cada um estavam as linhas de produção CoWoS da TSMC.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
   <iframe src="https://www.youtube.com/embed/pKXDVsWZmUU" title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Canal oficial da NVIDIA: Discurso de abertura de Jensen Huang na Computex em 2 de junho de 2024, "The Era of AI". Toda a palestra de duas horas, ele expôs um a um as GPUs Blackwell, NVLink e Spectrum-X — mas o local físico de cada slide está em Baoshan, Hsinchu. "Sem a TSMC, não há NVIDIA"; ele não disse isso em voz alta, mas cada gráfico de capacidade diz isso._

O custo físico do empacotamento 3D também não é pequeno. O PanSci aponta o problema: "O empacotamento avançado exige alta planicidade de die e alto alinhamento de chips; se houver pontos de conexão mal conectados durante o empilhamento, causará perda de rendimento. Além disso, os circuitos integrados geram perda de energia durante o cálculo, causando aumento de temperatura; o empacotamento avançado aproxima os dies, a transferência de calor interage, todos se aquecem mutuamente, tornando a dissipação de calor ainda mais difícil."[^12]

A próxima etapa é SoIC (System on Integrated Chips) e SoW-X (System on Wafer). O SoIC é o "verdadeiro 3D", empilhamento wafer-on-wafer direto, sem bumps (bumping-free). O SoW-X está previsto para produção em massa em 2027, com tamanho de máscara 9,5 vezes maior que o CoWoS atual, integrando mais de 16 grandes chips de computação, com capacidade de computação 40 vezes superior ao CoWoS atual[^13]. Quanto maiores e mais longos os chips de IA ficam, mais as linhas de empacotamento da TSMC se assemelham a pequenas fábricas.

## ALD: Crescendo Átomo por Átomo

![Vitrine de museu exibindo várias amostras de wafers de silício de tamanhos diferentes lado a lado; o maior tem diâmetro de cerca de 12 polegadas, com brilho reflexivo como espelho, mostrando a matéria-prima central da fabricação de semicondutores](/article-images/technology/silicon-wafers-museum-2017.webp)
_Exibição de amostras de wafers de silício, 2017. Foto: ArticCynda. [Licença via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg)._

4nm, 2nm, 1,6nm. Por trás desses números há uma tecnologia de fabricação discreta, mas crucial: Deposição de Camada Atômica (Atomic Layer Deposition, ALD).

O ALD foi inventado por finlandeses, mas tornou-se uma etapa central que nenhum wafer de processo avançado de Taiwan pode contornar.

A história começa na Finlândia. Em 1974, o cientista de materiais Tuomo Suntola começou a desenvolver o ALD na empresa finlandesa Instrumentarium Oy. Em 1977, a tecnologia estava madura e fez sua estreia em uma exposição industrial[^14]. Naquela época, a tecnologia era apenas para displays eletroluminescentes; Suntola não poderia prever que, 30 anos depois, se tornaria a veia de vida dos processos nanométricos. Em 1999, ele vendeu a tecnologia ALD para a empresa holandesa de equipamentos semicondutores ASM. Hoje, a ASM detém mais de 55% de participação de mercado no mercado de ALD[^14].

O PanSci explica o princípio do ALD de forma limpa: "A deposição de camada atômica é uma técnica melhorada de deposição química em fase gasosa, dividindo o processo de deposição em duas etapas. Primeiro, injeta-se o primeiro precursor, reagindo com a superfície do substrato... Quando a superfície está saturada, injeta-se o segundo precursor, reagindo com o precursor já aderido, formando o material alvo e completando o processo de filme fino."[^14] Os dois precursores são injetados um por um; cada ciclo cresce apenas uma camada de filme com espessura atômica.

Por que isso é importante? Porque a espessura do gate (porta) dos transistores do processo de 2nm é de apenas alguns átomos, e a camada isolante do gate deve atingir planicidade e controle de espessura em nível atômico. A deposição química em fase gasosa tradicional (CVD) não consegue; a deposição física em fase gasosa (PVD) não consegue; apenas o ALD pode "crescer camada por camada". Cada fábrica de processo avançado da TSMC está equipada com equipamentos ALD da ASM; essa cadeia, composta por equipamentos holandeses, tecnologia finlandesa e processo taiwanês, é a base física pela qual o 2nm pode ser produzido em massa.

> 💡 **Você Sabia?**: A menor dimensão característica do processo de 2nm é aproximadamente a largura de 20 átomos de silício lado a lado. Se você ampliar os átomos de silício para o tamanho de uma bola de ping-pong, o transistor de 2nm terá aproximadamente o comprimento de uma mesa de ping-pong. O trabalho do ALD é "cobrir a mesa bola por bola" com material isolante.

A ASM não é listada em Taiwan, mas quase todos os seus maiores clientes de equipamentos ALD de 12 polegadas estão em Taiwan. **Esta cadeia de suprimentos é invisível, mas irreplaceável**; se a produção em massa do 2nm da TSMC for atrasada, não há segunda fábrica de ALD no mundo que possa preencher a lacuna.

## Após 2nm, Vem o Quântico

Depois do nível de angstrom (1 nm = 10 angstroms), a história que a TSMC ainda não terminou de escrever.

No quarto trimestre de 2025, a TSMC iniciou a produção em massa de 2nm na Fab 22 de Kaohsiung, seguida pela Fab 20 em Baoshan, Hsinchu[^2]. O 2nm adota pela primeira vez a arquitetura de transistor de folha nanométrica GAA (Gate-All-Around), abandonando o transistor FinFET usado desde 22nm até 3nm[^16]. 2nm equivale a 20 átomos de silício de largura, já próximo do limite teórico da física. Os primeiros clientes incluem os chips da série A da Apple e os chips de IA da NVIDIA; a capacidade de produção do processo de 2nm será expandida trimestralmente[^3].

O próximo passo é 1,6nm (A16), previsto para produção em massa no quarto trimestre de 2026, introduzindo pela primeira vez a "Rede de Entrega de Energia Traseira" (Backside Power Delivery Network), nomeada pela própria TSMC como Super Power Rail[^16]. Mesma potência, 10% mais rápido que N2P; mesma eficiência, 15-20% menos energia.

Mas e depois de 1,6nm? O nó de processo fica cada vez mais caro à medida que avança. O custo de P&D do processo de 28nm é de cerca de US$ 1 bilhão; salta para US$ 3 bilhões no 7nm; dispara para US$ 10 bilhões no 3nm; e estima-se que ultrapasse US$ 20 bilhões no 2nm[^4]. A curva exponencial da Lei de Moore transforma o custo de P&D da fase final em números astronômicos; este é o "aumento exponencial da complexidade e do capital investido no desenvolvimento de processos avançados, onde investimento e retorno muitas vezes não são proporcionais" que o PanSci menciona[^12].

Assim, a indústria de semicondutores muda de estratégia: expansão horizontal torna-se empacotamento vertical (3D), silício torna-se novo material (GaN/SiC), e finalmente pode mudar para física de computação completamente diferente, como computação quântica.

A linha do tempo da Academia Sinica segue assim. Em outubro de 2023, o computador quântico supercondutor de 5 qubits foi concluído. Em 29 de janeiro de 2024, a presidente Tsai Ing-wen inspecionou; o computador quântico foi oficialmente conectado à rede[^6]. O PanSci registrou: "Em janeiro de 2024, o primeiro computador quântico auto-desenvolvido de Taiwan nasceu oficialmente na Academia Sinica; embora tenha apenas 5 qubits, abriu o prelúdio para Taiwan ocupar um lugar na arena global de computadores quânticos."[^17]

Em dezembro de 2025, o chip quântico supercondutor de 20 qubits foi concluído. Em janeiro de 2026, foi anunciado para uso online[^6]. O tempo de coerência (coherence time T1) saltou de 15-30 microssegundos na era de 5 qubits para 530 microssegundos em 20 qubits. Tempo de coerência é a duração em que um qubit pode manter o estado de superposição; quanto maior, menos "ruído" e mais complexas as operações possíveis.

A equipe nacional quântica interministerial foi oficialmente formada em março de 2022, com orçamento de 8 bilhões de NT$ em 5 anos e 17 equipes de pesquisa[^18]. O Ministério da Economia estabeleceu o "Escritório de Impulso de Tecnologia da Indústria Quântica" em abril de 2026, conectando P&D acadêmico à indústria.

O que a Academia Sinica (ITRI) faz é particularmente interessante: usa o processo de 28nm da TSMC para fazer "chips de controle de qubits". A Central News Agency (CNA) citou a Academia Sinica em março de 2024: "Utilizando o design de IC de micro-ondas do qual Taiwan é especialista e o processo de 28nm da TSMC, criamos chips e módulos de controle de baixa temperatura (4K, ou -269°C)... Reduzindo o tamanho dos instrumentos de controle, colocando-os em geladeiras de diluição de baixa temperatura, reduzindo o volume total do equipamento em 40%, simplificando a fiação, possuindo vantagens comerciais... O consumo de energia deste módulo é mais de 50% menor que os dados publicados por grandes fabricantes internacionais."[^19]

> 📝 **Nota da Curadoria**: A estratégia quântica de Taiwan não reside em fabricar qubits por conta própria (esse é o território de IBM, Google e Academia Sinica), mas em miniaturizar os circuitos de controle para caber no refrigerador de diluição. De 5 qubits para 20 qubits, o chip de controle da Academia Sinica passou de suportar 1 qubit, 2 qubits, 8 qubits, e espera-se atingir 20 qubits em 2026-2027. **A próxima parada da Montanha Sagrada que Protege a Nação é ser a foundry da era quântica, não disputar diretamente o hegemonismo quântico**. Mas essa posição de foundry ainda não tem ninguém cravando o prego de "deixe com Taiwan".

## Três Rotas Quânticas: Supercondutor, Armadilha de Íons, Topológico

Computadores quânticos não têm apenas um caminho.

**Qubits supercondutores** (superconducting qubits) é a rota escolhida por IBM, Google e Academia Sinica. Vantagem: processo compatível com fábricas de semicondutores existentes (onde Taiwan tem chance); velocidade de controle rápida. Desvantagem: requer refrigerador de diluição próximo a zero absoluto (15 mK, aprox. -273°C); alto ruído. A Google usou o "Salice" (Sycamore) de 53 qubits em 2019 para declarar hegemon quântica; em 200 segundos, completou uma tarefa que um supercomputador tradicional levaria 10.000 anos[^20].

**Qubits de armadilha de íons** (trapped ion qubits) segue a rota de controle de laser de átomos individuais. O PanSci organizou as diferenças dessa rota: "A tecnologia de armadilha de íons utiliza laser para controlar átomos individuais para computação; essa tecnologia tem alta precisão e estabilidade, mas enfrenta problemas de complexidade técnica e custo."[^17] Fabricantes representativos são IonQ e Quantinuum. Vantagem: alta precisão, boa estabilidade, não requer ultra-baixa temperatura. Desvantagem: velocidade de controle lenta, difícil de escalar para muitos qubits.

**Qubits topológicos** (topological qubits) é a próxima geração na qual a Microsoft apostou. Em fevereiro de 2025, a Microsoft apresentou o processador quântico topológico Majorana 1, alegando poder escalar para um milhão de qubits[^15]. Teoricamente, qubits topológicos são extremamente resistentes a interferências; mas essa rota é a menos madura, e a própria existência das partículas Majorana ainda está na fase de verificação na física.

Essas três rotas têm riscos diferentes. A estratégia de Taiwan é "garantir que, independentemente de qual rota vença, Taiwan tenha um nó na cadeia de suprimentos", sem apostar que uma única rota vencerá. A rota supercondutora depende do chip de controle de 28nm da TSMC. A rota de armadilha de íons requer óptica de precisão, compatível com a indústria optoeletrônica de Taiwan; se a rota topológica tiver sucesso, ainda exigirá filmes de pureza extrema, retornando ao território do ALD.

## Fab Overseas: Expansão ou Exportação?

A globalização da TSMC acelerou a partir da década de 2020.

**Fab 21 de Arizona, EUA**: Fase 1 de 4nm em produção em massa no primeiro semestre de 2025; Fase 2 de 3nm/2nm no segundo semestre de 2027; Fase 3 de 2nm/A16 prevista antes de 2030. Investimento total de capital de cerca de US$ 165 bilhões[^21]. Mas há um "porém" importante: o empacotamento CoWoS de todos os chips de IA ainda ocorre apenas em Taiwan; os wafers produzidos na fábrica de Arizona são retornados a Taiwan para empacotamento[^13].

**Fab 1 de Kumamoto, Japão**: Processos de 22-28nm, produção em massa em 2024, em parceria com Sony e Toyota. O planejamento original da Fab 2 (12-16nm) tem progresso incerto; parte dos recursos foi realocada para Arizona.

**ESMC de Dresden, Alemanha** (TSMC detém 40%): Chips de carro de 28/22/16/12nm, equipamentos de mudança no segundo semestre de 2025, produção em massa em 2027, capacidade mensal de cerca de 40.000 unidades[^22].

Essas fábricas overseas têm um "Princípio N-2" comum: **sempre ficam duas gerações atrás da Taiwan本土**. Quando a Taiwan本土 faz 2nm, o mais avançado overseas é 4nm; quando Taiwan lança 1,6nm, o overseas chega apenas a 3nm. Essa linha vermelha está escrita na ética de engenharia geopolítica, não nas cláusulas do contrato.

> ⚠️ **Ponto de Controvérsia**: Fab overseas expande ou dilui o Escudo de Silício? Suportadores dizem: tecnologia fica em Taiwan, capacidade se expande overseas, transformando o Escudo de Silício de "uma ilha" em "uma cadeia", tornando a des-risco mais completa. Opositores dizem: cada fábrica overseas enviada leva engenheiros treinados, um SOP de produção em massa e relacionamentos com clientes. Quando Arizona ou Kumamoto acumularem na fronteira N-2 daqui a 30 anos, essa "duas gerações mais avançadas" pode ser lentamente comprimida. O Princípio N-2 é atualmente uma promessa da TSMC, não uma lei física.

Junto com as fab overseas, há também a "migração de talentos de design". O design de chips de IA não requer apenas Taiwan; Silicon Valley, Tel Aviv e Nova Déli têm seus próprios centros de design. O ecossistema de foundry da TSMC está se tornando uma mistura de "engenheiros globais + fabricação insular".

## O Preço Ambiental: O Outro Lado da Montanha Sagrada

A Montanha Sagrada que Protege a Nação tem peso.

Recursos hídricos são os mais intuitivos. Os três parques científicos da TSMC consomem mais de 208.000 toneladas de água por dia; grupos ambientalistas estimam que, após 2025, com a entrada em operação de novas fábricas, o consumo de água pode aumentar 4 vezes para 770.000 toneladas/dia[^23]. A resposta da TSMC é: cada gota de água é usada em média 3,5 vezes; taxa de reciclagem atinge 87%; meta de novas fábricas é 90%; 5,54 milhões de metros cúbicos de economia de água adicionados em 2024.

Energia elétrica é a segunda questão. Uma fábrica de 3nm consome cerca de 2,1 bilhões de kWh por ano, equivalente ao consumo anual de 20.000 famílias em Taiwan. O consumo de 2nm e 1,6nm continuará subindo. A TSMC promete alcançar RE100 (100% energia renovável) até 2050, mas a oferta de energia verde de Taiwan não acompanha a velocidade da expansão de semicondutores; essa linha do tempo está sendo constantemente testada sob pressão.

Horas de trabalho é a terceira questão. As horas de trabalho, preços de imóveis e taxa de natalidade dos engenheiros do Parque Científico de Hsinchu são o tema de outro artigo. Mas, assim como a ciência dos materiais, é uma questão física: o tempo e a energia humana também têm um "band gap"; ultrapassado o limiar, ocorre colapso.

A existência da Montanha Sagrada que Protege a Nação depende, além da tecnologia da TSMC, das políticas governamentais e das oportunidades geopolíticas, também do preço compartilhado por 170.000 engenheiros do parque científico, toda a cadeia de suprimentos e cada residente taiwanês que usa água e eletricidade.

## Ecossistema Completo: Taiwan Não é Apenas TSMC

A competitividade da indústria de semicondutores de Taiwan deriva de todo o aglomerado, não apenas da TSMC. No design de IC, há MediaTek (top 3 global), Novatek, Realtek, Himax; além da TSMC na foundry de wafers, há UMC, World Semiconductor, JSMC; empacotamento e teste são feitos por ASE (top 1 global), SPIL, Kinsus. Semicondutores de terceira geração dependem de GlobalWafers (crescimento de SiC), Han Leong, SG Micro (GaN), MACOM; memória é suportada por Nanya Technology e Winbond; equipamentos e materiais são preenchidos por empresas invisíveis como Jade Mountain Precision, Sin-Eun, e Chao Yue.

Um chip, do design à conclusão, pode fazer um circuito completo em Taiwan, sem transporte transnacional. Essa "vantagem de cadeia curta" foi vista pelo mundo durante a COVID; desde então, está escrita nos whitepapers de cadeia de suprimentos de cada gigante tecnológico.

O Parque Científico de Hsinchu foi estabelecido em 1980; em mais de 40 anos, acumulou mais de 500 empresas e 170.000 profissionais. Um engenheiro pode ficar 5 anos na TSMC, pular para MediaTek para design de chips, depois mudar para ASE para empacotamento; esse ciclo de talentos entre empresas dissemina efetivamente o nível tecnológico de toda a indústria.

E os concorrentes? A estratégia de integração vertical da Samsung da Coreia do Sul investiu US$ 230 bilhões entre 2022-2026, mas a taxa de rendimento de processo avançado ainda está atrás da TSMC[^4]. A Intel travou no 10nm por anos; em 2021, propôs IDM 2.0 para combinar design e foundry, mas até 2025 ainda não conquistou clientes importantes na foundry — o mais irônico é que alguns chips de alto nível da própria Intel agora são fabricados pela TSMC.

## A posição quântica continua vaga

O carregador do Nokia 3310 tinha 4,56 watts; o carregador rápido de 2025 tem 240 watts. Uma diferença de 52 vezes. O silício levou 30 anos para percorrer esse caminho; o nitreto de gálio completou em 5.

No laboratório quântico da Academia Sinica, os chips quânticos supercondutores precisam operar a 15 milieletrons-volt (cerca de -273 °C). O ITRI, usando o processo de 28 nanômetros da TSMC, produziu um chip de controle que comprimiu o "volume do instrumento de controle" necessário para essa temperatura extrema de um prédio inteiro para uma pequena caixa. A capacidade de semicondutores de Taiwan está, pouco a pouco, deslocando as fronteiras do computador quântico.

Mas ninguém sabe dizer onde fica essa fronteira. O tempo de coerência dos qubits varia de 15 microssegundos a 530 microssegundos — isso é apenas o começo. Os 19 engenheiros que a RCA enviou há 50 anos provavelmente não imaginavam que seu trabalho de 1973 se cristalizaria no processo de 2 nanômetros de 2025.

A montanha sagrada que protege o país dominou o presente graças à experiência industrial dos anos 1950. Nos próximos 50 anos, a posição de foundry na era quântica ainda não foi conquistada por Taiwan.

> ✦ O Blackwell de Jensen Huang roda inferência na nuvem acima da sua cabeça; os wafers de SiC da GlobalWafers aquecem no posto de recarga de veículos elétricos na sua esquina; a primeira película fina de ALD que Tuomo Suntola fez na Finlândia em 1974 sela a camada de isolamento do gate no chip do seu celular — os semicondutores sempre foram um espectro inteiro de materiais subindo degrau a degrau pela física da banda proibida ao longo de 50 anos, e não pertencem apenas à TSMC. Onde fica o próximo degrau, a física nos dirá; mas se vamos subi-lo ou não, é escolha de Taiwan.

---

**Leitura complementar**:

- [Empresa de Taiwan: TSMC](/pt/economy/tsmc) — Governança corporativa, estrutura financeira, escala de capex da montanha sagrada
- [Empresa de Taiwan: MediaTek](/pt/economy/mediatek) — Como o líder em design de IC se posiciona em chips para celular e computação de borda com IA
- [Empresa de Taiwan: ASE Semiconductor](/pt/economy/taiwan-enterprise-ase-semiconductor) — Indústria de embalagem e teste global nº 1, ecossistema de back-end além do CoWoS
- [Os Construtores da Montanha: A Aposta do Século](/pt/art/mountain-makers-tsmc-documentary) — Documentário de 2025 de Hsiao Ju-chen, cinco anos de entrevistas com 80+ veteranos de semicondutores; em 2026 chega a Purdue, Wisconsin e Michigan, três polos de investimento do CHIPS Act
- [Wu Ta-you](/pt/people/tai-yu-wu) — Enquanto Taiwan apostava nos semicondutores nos anos 1980, como presidente da Academia Sinica insistiu na importância da ciência básica, lançando as bases do sistema de pesquisa de Taiwan
- [Huang Chung-jen](/people/黃崇仁) — Fundador da Powerchip / PSMC, a rota de Taiwan no DRAM construindo fábricas próprias sobre licenciamento alheio: market share caiu de 23,2% para 6,3%, o capítulo menos contado desta indústria
- [Indústria de robótica de Taiwan](/pt/technology/taiwan-robotics-industry) — A ilha nº 1 em semicondutores, por que na era da robótica é aluna de recuperação? Olhando a fratura industrial a partir da inauguração do NCAIR
- [Bolsa e mercado de capitais de Taiwan](/pt/economy/taiwan-stock-market) — Como todo o ecossistema da cadeia de suprimentos que sustenta o 6º maior mercado global em 2026 se reflete no mercado de capitais
- [Cadeia de suprimentos de tungstênio de Taiwan](/pt/technology/taiwan-tungsten-supply-chain) — O hexafluoreto de tungstênio preenche contatos e word lines de 3D NAND; Taiwan não tem minas de tungstênio, mas subiu ao midstream desta matéria-prima via reciclagem e refino
- [Escola de IA de Taiwan](/pt/technology/taiwan-ai-academy) — Como os 10 mil engenheiros de IA treinados em 8 anos pela AIA retornam à cadeia ICT existente de semicondutores, reforçando o lado de software de Taiwan
- [Computex: três grandes feiras internacionais de computação, duas acabaram, a que sobrou cresce em Taipé](/technology/Computex) — O CoWoS e os processos avançados da TSMC todo fim de maio apertam a mão dos gigantes globais de IA nesta feira de 45 anos em Taipé
- [Parques científicos de Taiwan](/pt/technology/science-park-development) — Hsinchu, Sul e Centro, três parques que são o suporte físico do cluster de semicondutores e também o centro geográfico do escudo de silício

## Fontes de Imagem

Este artigo usa 3 imagens sob licença CC/PD, cacheadas em `public/article-images/technology/` para evitar servidores de origem de links quentes:

- [Silicon vs GaN 30W USB-C chargers](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg) — Foto: 4300streetcar, 2025-12-25, CC BY 4.0, Wikimedia Commons file Silicon_vs_GaN_30W_USB-C_chargers.jpg
- [TSMC Fab 5 Hsinchu](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG) — Foto: Peellden, 2010-09-05, CC BY-SA 3.0, Wikimedia Commons file TSMC_Fab5.JPG
- [Silicon wafers museum display](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg) — Foto: ArticCynda, 2017-10-23, CC0 public domain, Wikimedia Commons file Silicon_wafers.jpg

## Referências

[^1]: [Semiwiki — How Philips Saved TSMC](https://semiwiki.com/semiconductor-history/307560-how-philips-saved-tsmc/) — A participação acionária da Philips, conforme investigado pelo Semiwiki, deve ser 27,6%; acionista chave para tecnologia e clientes nos estágios iniciais da TSMC

[^2]: [Focus Taiwan 2025/12/30 — TSMC 2nm production](https://focustaiwan.tw/business/202512300012) — Produção em massa de 2nm da TSMC tem a Fab 22 de Kaohsiung como prioridade; Fab 20 em Baoshan, Hsinchu segue em seguida

[^3]: [数位时代 — TSMC 2nm正式量產](https://www.bnext.com.tw/article/89663/tsmc-2nm-volume-production) — TSMC inicia produção em massa de 2nm no Q4 de 2025; números específicos de capacidade mensal são estimativas externas da indústria, não divulgadas oficialmente

[^4]: [科技新報 — TSMC 3nm utilization reaches 100%](https://technews.tw/2025/05/26/tsmcs-2nm-process-is-expected-to-reach-full-capacity-in-four-seasons/) — Estimativas da indústria indicam que a taxa de rendimento de processos avançados da TSMC é superior à dos concorrentes; números específicos de rendimento são estimativas de terceiros, não divulgadas oficialmente

[^5]: [天下雜誌 — Lee Teng-hui e o Nascimento da TSMC](https://www.cw.com.tw/article/5095492) — Morris Chang funda a TSMC em 1987, estabelecendo o modelo de "foundry pura", baseando a divisão industrial global de semicondutores; contexto de transferência de tecnologia de US$ 4,5 milhões da RCA em 1973

[^6]: [Academia Sinica — 20 Qubit Superconducting Quantum Chip Announcement](https://www.sinica.edu.tw/News_Content/56/2375) — Academia Sinica conclui chip quântico supercondutor de 20 qubits em dezembro de 2025; conectado em 29 de janeiro de 2026; tempo de coerência T1 atinge 530 microssegundos

[^7]: [PanSci — GaN: Get Same Power in 1/3 Time](https://pansci.asia/archives/362660) — Autor: Equipe Editorial PanSci. Band gap de GaN 3,4 eV, tensão de colapso 10x, frequência de trabalho 1 MHz vs silício 100 kHz; aplicação de carregamento rápido de veículos elétricos de 1000V de SiC. Parceiro de Curadoria de Conteúdo por MOU 2026-05-05

[^8]: [TrendForce — TSMC exits GaN foundry by July 2027](https://www.trendforce.com/news/2025/08/22/news-tsmc-reportedly-exits-gan-foundry-business-by-2027/) — TSMC sai de foundry de GaN em julho de 2027; tecnologia licenciada para World Semiconductor (VIS) e GlobalFoundries; SG Micro (3163) tem exportação mensal de cerca de 500 unidades de GaN de 6 polegadas

[^9]: [富果直送 — GlobalWafers SiC 8-inch wafer 2025 mass production](https://www.fugle.tw/news/article/1234567) — Capacidade mensal de 6 polegadas SiC da GlobalWafers atinge 20.000 unidades no final de 2024; fornos de crescimento auto-desenvolvidos de 3 → 20 unidades; rendimento > 50%; estratégia de "Grupo IDM Virtual" de Hsu Hsiu-lan

[^10]: [科技新報 — SiC Supply Chain Under Pressure](https://technews.tw/2025/11/sic-market-oversupply) — Expansão massiva de fábricas de SiC chinesas em 2025 leva taxa de utilização de capacidade de 6/8 polegadas SiC da GlobalWafers a abaixo de 50%; rumor de GPU Rubin da NVIDIA adota camada de interposição SiC + data center de corrente contínua de alta tensão de 800V para produção em massa em 2027

[^11]: [SemiAnalysis — NVIDIA Blackwell CoWoS-L Analysis](https://www.semianalysis.com/p/nvidia-blackwell-b200-cowos-l) — Blackwell B200 da NVIDIA usa CoWoS-L para integrar 2 GPUs Blackwell + 1 CPU Grace; velocidade de treinamento de IA 4x mais rápida que H100; NVIDIA reserva capacidade CoWoS da TSMC até 2027

[^12]: [PanSci — 3D Stacking: How Advanced Packaging Lets Chips Enter Xueshan Tunnel](https://pansci.asia/archives/367588) — Autor: Equipe Editorial PanSci. Princípios de CoWoS/SoIC/TSV; metáfora de Rodovia Taijiu vs Túnel de Xueshan; desafios de rendimento e dissipação de calor de empacotamento 3D. Parceiro de Curadoria de Conteúdo por MOU 2026-05-05

[^13]: [Digitimes — TSMC CoWoS Capacity Expansion Plan](https://www.digitimes.com.tw/iot/article.asp?cat=158&id=0000696823_X1D7L8XB6JNL2Y8XLPZJK) — Capacidade mensal CoWoS da TSMC: 35.000 unidades no final de 2024, 75.000 no final de 2025, meta de 150.000 em 2028; NVIDIA reserva capacidade até 2027; wafers de Arizona retornados a Taiwan para empacotamento

[^14]: [PanSci — ALD Atomic Layer Deposition: 50 Years of Thin Film Revolution](https://pansci.asia/archives/377669) — Autor: Equipe Editorial PanSci. ALD desenvolvido por Suntola em Instrumentarium Oy em 1974; tecnologia madura em 1977; vendida para ASM em 1999; 55% de participação de mercado da ASM; princípio de dois precursores de deposição química em fase gasosa. Parceiro de Curadoria de Conteúdo por MOU 2026-05-05

[^15]: [科技新報 — Microsoft Majorana 1 Topological Quantum Processor Released](https://technews.tw/2025/02/20/microsoft-majorana-1-topological-qubit/) — Microsoft apresenta em fevereiro de 2025 o primeiro processador quântico topológico Majorana 1 do mundo, alegando escalabilidade para um milhão de qubits

[^16]: [Site Oficial da TSMC — A16 (1.6nm) Process Announcement](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) — 2nm adota pela primeira vez transistor de folha nanométrica GAA (abandonando FinFET); A16 introduz pela primeira vez rede de entrega de energia traseira (Super Power Rail); produção em massa Q4 2026; 10% mais rápido que N2P na mesma potência; 15-20% menos energia na mesma eficiência

[^17]: [PanSci — Taiwan Quantum Tech: From 5 Qubits to Mass Production Era](https://pansci.asia/archives/377923) — Autor: Equipe Editorial PanSci. Computador quântico de 5 qubits da Academia Sinica nasce em janeiro de 2024; três rotas: supercondutor vs armadilha de íons vs topológico; Salice de 53 qubits da Google resolve problema de 10.000 anos em 200 segundos. Parceiro de Curadoria de Conteúdo por MOU 2026-05-05

[^18]: [iThome — Quantum National Team 5 Years 8 Billion Budget](https://www.ithome.com.tw/news/151234) — Equipe nacional quântica interministerial formada em março de 2022; 8 bilhões de NT$ em 5 anos; 17 equipes de pesquisa; Escritório de Impulso de Tecnologia da Indústria Quântica do Ministério da Economia estabelecido em abril de 2026

[^19]: [Central News Agency 2024/03/06 — ITRI Quantum Control Chip](https://www.cna.com.tw/news/ait/202403060123.aspx) — ITRI utiliza processo de 28nm da TSMC para criar chip de controle quântico de baixa temperatura (4K, -269°C); volume reduzido em 40%; consumo de energia 50% menor que grandes fabricantes internacionais; roteiro 1 qubit em 2024 → 20 qubits em 2026-2027

[^20]: [TechNews — Google Sycamore Quantum Supremacy](https://technews.tw/2019/10/24/google-sycamore-quantum-supremacy/) — Computador quântico Salice de 53 qubits da Google atinge hegemon quântica em 2019; 200 segundos para completar tarefa de cálculo que supercomputador tradicional levaria 10.000 anos

[^21]: [SemiAnalysis — TSMC Arizona Fab 21 Investment Plan](https://www.semianalysis.com/p/tsmc-arizona-1650b-capex) — Investimento de 3 fases da Fab 21 da TSMC em Arizona: US$ 165 bilhões; Fase 1 (4nm) produção em massa 2025; Fase 2 (3nm/2nm) 2027; Fase 3 (2nm/A16) antes de 2030; Princípio N-2: overseas sempre fica duas gerações atrás da Taiwan本土

[^22]: [Digitimes — ESMC Dresden 2027 Mass Production](https://www.digitimes.com.tw/news/esmc-dresden-2027) — TSMC detém 40% da ESMC; fábrica de chips de carro de 28/22/16/12nm em Dresden, Alemanha; equipamentos de mudança no segundo semestre de 2025; produção em massa em 2027; capacidade mensal de cerca de 40.000 unidades

[^23]: [天下雜誌 — TSMC Water Consumption](https://www.cw.com.tw/article/5128456) — Consumo diário de água dos três parques científicos da TSMC ultrapassa 208.000 toneladas; grupos ambientalistas estimam que, após 2025, com entrada em operação de novas fábricas, consumo de água aumenta para 770.000 toneladas/dia; resposta da TSMC: cada gota usada 3,5 vezes, taxa de reciclagem 87% (novas fábricas 90%); 5,54 milhões de metros cúbicos de economia de água adicionados em 2024

[^asml-philips]: [Wikipedia — ASML Holding](https://en.wikipedia.org/wiki/ASML_Holding) — ASML fundada em 1º de abril de 1984 pela joint venture 50/50 da Philips holandesa (Philips) e ASM International (ASMI) para criar ASM Lithography; após listagem de ações em 1995, ASMI sai; hoje ASML é o único fornecedor de equipamentos de exposição EUV do mundo

[^lin-bio]: [Wikipedia — Burn-Jeng Lin](https://en.wikipedia.org/wiki/Burn-Jeng_Lin) — Lin Benjian (Burn J. Lin) nasceu em 1942 no Vietnã; trabalhou em tecnologia de exposição no Centro de Pesquisa Watson da IBM a partir da década de 1970; retornou a Taiwan em 2000 para se juntar à TSMC como diretor de P&D; recebeu o Prêmio Frits Zernike da SPIE em 2008; elogiado como "Pai da Litografia de Imersão"

[^157nm-fail]: [Electronics Weekly — Immersion litho sidelines 157nm](https://www.electronicsweekly.com/news/research-news/process-rd/immersion-litho-sidelines-157nm-2005-05/) — Rota de 157nm é substituída por 193nm immersion após 2002-2003 devido a problemas de birrefringência de lentes de fluorita de cálcio (CaF₂), forte absorção de filmes finos para 157nm, e dificuldades de integração de processo; aposta de Intel + Nikon falha

[^immersion-litho]: [Wikipedia — Immersion lithography](https://en.wikipedia.org/wiki/Immersion_lithography) — Lin Benjian propõe litografia de imersão de 193nm na SPIE em 2002; índice de refração da água de 1,44 torna 193nm equivalente a resolução de aprox. 134nm; ASML produz em massa em 2007, sustentando de 65nm a 7nm, estendendo a Lei de Moore por seis gerações

[^cw-lin-interview]: [天下雜誌 CommonWealth — Interview with the Father of Immersion Lithography Who Put TSMC on the Map](https://english.cw.com.tw/article/article.action?id=3720) — Entrevista com Lin Benjian em 2024-06-18 — Contexto histórico de "Nikon não ousa fazer immersion"; Lin Benjian retorna à TSMC em 2000 para promover adoção de litografia de imersão; vínculo de cooperação tecnológica de 30 anos entre TSMC e ASML
