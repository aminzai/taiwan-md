---
title: 'O espírito open source de Taiwan — engenheiros movidos a paixão'
description: 'O projeto open source mais influente de Taiwan não é um software, é um grupo de engenheiros que em um hackathon disseram ao governo: "Vocês não fazem bem, nós fazemos".'
date: 2026-03-29
category: 'Technology'
tags:
  [
    'Código aberto',
    'g0v',
    'COSCUP',
    'GitHub',
    'Tecnologia cívica',
    'Software livre',
  ]
subcategory: 'Comunidade e Cultura Digital'
author: 'p3nchan'
featured: false
lastVerified: 2026-03-29
lastHumanReview: false
readingTime: 8
translatedFrom: 'Technology/台灣開源精神.md'
sourceCommitSha: '4b6d28c54'
sourceContentHash: 'sha256:d044abffde5fb58e'
translatedAt: '2026-07-25T06:57:15.502613+00:00'
---

> A indústria de software de Taiwan não está na primeira linha global, mas o GitHub conta com mais de 44.000 usuários marcados como Taiwan, hackathons comunitários acumulam mais de 70 edições e milhares de contribuidores — quase todos desenvolvedores individuais que participam depois do expediente por conta própria. Este artigo não fala apenas do g0v, mas monta o mapa completo da cultura open source de Taiwan a partir de quatro ângulos: pessoas, comunidade, educação e indústria.

## Um anúncio que desencadeou um hackathon

Outubro de 2012, o Yuan Executivo transmitiu na televisão um anúncio de 40 segundos a promover o «Plano de Impulso do Dinamismo Económico». O conteúdo do anúncio era apenas uma frase: «Este plano é realmente muito complexo, não pode ser explicado claramente em poucas palavras simples.»

Kao Chia-liang (clkao), graduado em Ciência da Computação pela NTU, viu o anúncio e ligou o computador. Ele e alguns amigos participaram no Yahoo! Open Hack Day, alteraram o tema de última hora e, em três dias, criaram o projeto «Visualização do Orçamento do Governo Central», ganhando um prémio de menção honrosa. Dois meses depois, Kao Chia-liang registrou o g0v.tw e usou o dinheiro do prémio para organizar o «Hackathon de Mobilização Antichaos Número Zero».

O nome g0v vem de substituir o «o» de gov (governo) por 0. O significado é direto: vocês fazem mal, nós fazemos.

Isto não é uma organização. O g0v não tem escritório, nem conselho de administração, nem funcionários a tempo inteiro. É uma comunidade descentralizada, mantida por hackathons bimestrais. Até ao final de 2025, já se realizaram mais de 70 edições, o Slack tem mais de 8.000 membros e o HackMD acumulou mais de 4.500 notas colaborativas.

---

## 72 horas, 100 apps

O momento em que o g0v foi mais visto internacionalmente foi 2020.

No início da pandemia de COVID-19, Taiwan implementou o racionamento de máscaras com nome real. O Ministério da Saúde e Bem-Estar disponibilizou uma API aberta com o estoque de máscaras das farmácias, e a então Ministra Digital Audrey Tang anunciou a novidade no canal de chat do g0v. Nas 72 horas seguintes, a comunidade de desenvolvedores de Taiwan explodiu com uma energia colaborativa sem precedentes: Kiang (Jiang Ming-zong) criou o mapa de máscaras das farmácias, Jarvis Lin fez o app para Android, e um chatbot do LINE também entrou no ar no mesmo dia.

Em uma semana, surgiram mais de 100 aplicativos relacionados à consulta de máscaras. Estima-se que cerca de mil engenheiros participaram do desenvolvimento.

A _Foreign Affairs_ publicou um artigo especial, _Civic Technology Can Help Stop a Pandemic_, afirmando que Taiwan demonstrou um terceiro caminho, diferente da vigilância no estilo chinês e também diferente dos gigantes tecnológicos ocidentais: a inovação democrática impulsionada pela tecnologia cívica (civic tech). Um relatório da Faculdade de Medicina de Stanford registrou 124 intervenções independentes implementadas por Taiwan durante a pandemia. NPR, _MIT Technology Review_ e _Harvard Business Review_ também fizeram reportagens especiais.

Isso não é mérito do governo, nem apenas de Audrey Tang. É obra de um grupo de engenheiros sem salário, que no fim de semana abriram seus laptops e fizeram acontecer.

---

## Antes de Tang Feng: as raízes do open source em Taiwan

O g0v pôde formar-se rapidamente em 2012 porque Taiwan já contava com vinte anos de solo open source.

**Audrey Tang** aprendeu Perl aos 12 anos, abandonou a escola aos 14 para empreender. Antes de entrar para o governo, lançou mais de 100 projetos no CPAN (repositório de módulos Perl), liderou o **Pugs** — a primeira implementação executável do Perl 6 em Haskell — e co-desenvolveu o **EtherCalc** com Dan Bricklin, pai da planilha eletrônica. É figura de liderança reconhecida nas comunidades Perl e Haskell, com influência no open source internacional muito anterior à sua carreira política.

**Hong Jen-yu (PCMan)** é outro nome representativo. Médico internista, aprendeu programação sozinho no ensino médio e escreveu o software de conexão BBS **PCMan**. Em 2006, iniciou o projeto **LXDE** — um ambiente de desktop Linux leve. O LXDE chegou a ser o ambiente de desktop mainstream com menor consumo de memória no mundo, adotado por distribuições como **Knoppix** e **Lubuntu**. Um ambiente de desktop escrito por um médico taiwanês, rodando em máquinas Linux pelo mundo afora. Hong juntou-se depois ao Google, mas a história do LXDE ilustra uma característica típica dos contribuidores taiwaneses de open source: a profissão principal não é software, mas usam o tempo livre para criar projetos de nível internacional.

**Huang Ching-chun (jserv)** trilhou outro caminho. Participou de desenvolvimento de software de sistema na **MediaTek** e na **Andes Technology**, depois passou a lecionar no Departamento de Ciência da Computação da **Universidade Nacional Cheng Kung**, onde criou a disciplina "Design do Núcleo Linux" — o único curso universitário em Taiwan que disseca sistematicamente o kernel Linux mais recente. Seus alunos submetem patches diretamente para Linux, glibc, GCC, LLVM. Apresentou-se diversas vezes no **COSCUP** e no **FOSDEM** europeu. O jserv não representa o contribuidor "gênio", mas a tentativa de embutir a prática open source no sistema educacional.

---

## Ecossistema comunitário: não apenas o COSCUP

A densidade das comunidades de código aberto de Taiwan na Ásia é anómala.

O **COSCUP** (Conference for Open Source Coders, Users and Promoters), desde 2006, é a maior conferência anual de código aberto de Taiwan. Em 2024, o número de participantes ultrapassou 2.800, com mais de 40 trilhas comunitárias (community rooms), abrangendo temas como Kubernetes, PostgreSQL, Ruby, Python, Blockchain, entre outros. Cada trilha comunitária dispõe de cerca de 6 horas de programação, planeada autonomamente por cada comunidade. O COSCUP não cobra ingressos. São mais de cem voluntários, todos não remunerados. 2025 marca a 20.ª edição do COSCUP.

O **SITCON** (Students' Information Technology Conference), desde 2013, é inteiramente idealizado e organizado por estudantes. O seu propósito é mostrar a estudantes do ensino médio de 18 anos que não precisam esperar a formatura para participar do código aberto. O SITCON realiza a sua conferência anual em março, além de promover o HackGen durante o semestre, acampamentos de verão e encontros quinzenais.

O **PyCon TW** é a conferência anual da comunidade Python, reunindo utilizadores de Python de diversas áreas. O **MozTW** é a comunidade de voluntários da Mozilla em Taiwan, mantendo a versão em chinês tradicional do Firefox desde 2004, gerindo o programa de embaixadores campus e o grupo de tradução de legendas. O espaço comunitário 「摩茲工寮」 em Taipé funcionou de 2014 a 2023; após o fim do patrocínio da Mozilla, passou a ser mantido por doações locais.

Há grande participação cruzada entre estas comunidades. A mesma pessoa pode ser simultaneamente palestrante no COSCUP, contribuidor do g0v e voluntário no PyCon TW. O círculo de código aberto de Taiwan não é grande, mas tem alta densidade.

## O legado institucional e a ruptura

Taiwan já teve uma tentativa governamental de promover o código aberto.

Em 2003, o Instituto de Ciência da Informação da Academia Sinica, com subsídio do Bureau Industrial do Ministério de Assuntos Econômicos, fundou a "Fundição de Software Livre" (OSSF, Open Source Software Foundry). A OSSF oferecia hospedagem de projetos, consultoria jurídica, promoção via boletim eletrônico e nutriu a comunidade local de código aberto por mais de uma década. Em 2015, o Ministério da Ciência e Tecnologia decidiu não mais subsidiar, a OSSF encerrou suas operações e o site foi mantido até o final de 2021, quando foi fechado.

O desaparecimento da OSSF não causou declínio nas atividades de código aberto de Taiwan — isso justamente mostra que a energia do código aberto de Taiwan nunca dependeu do governo. Quem realmente sustentou o ecossistema foi a "Fundação Cultura Aberta" (OCF, Open Culture Foundation), fundada em 2014. A OCF foi cofundada por várias comunidades de código aberto, é uma fundação sem fins lucrativos e atua como gestora financeira das comunidades: emite notas fiscais para a COSCUP, ajuda projetos a processar doações e oferece consultoria jurídica sobre licenciamento de código aberto. A OCF também colabora com instituições internacionais como o AIT, o Escritório Britânico em Taiwan e o Banco Mundial, exportando a experiência de tecnologia cívica de Taiwan para o exterior.

Essa estrutura é interessante: o plano governamental terminou, a fundação civil assumiu. A instituição nasceu de baixo para cima.

---

## As razões estruturais do "movido a amor"

Os contribuidores de código aberto de Taiwan são, em sua grande maioria, indivíduos. Não há empresas de código aberto no nível da Red Hat, nem programas de patrocínio empresarial na escala do Google Summer of Code; o investimento das empresas de tecnologia em código aberto se resume, na maior parte, a "permitir que os funcionários façam isso no tempo livre" em vez de "incluir código aberto nos KPIs".

Por quê?

A indústria tecnológica de Taiwan tem como núcleo a manufatura por encomenda de hardware e o design de CI. Os modelos de negócio da TSMC, MediaTek e Foxconn baseiam-se em capacidade de manufatura e barreiras de patentes, não em código aberto. Nesse ecossistema, o software costuma ser um "acessório que acompanha o hardware", e não uma fonte de receita independente. Entre as milhares de empresas de serviços de software, nove em cada dez fazem integração de sistemas, atendendo ao mercado interno.

O resultado: há muita gente que programa, mas quase ninguém "vive de código aberto". Código aberto é coisa de depois do expediente, de encontros de comunidade, de hackathons de sábado. Na lista de patrocinadores da COSCUP, você verá mais empresas estrangeiras (Google, LINE, Trend Micro) do que empresas locais.

Isso não é inteiramente ruim. Justamente porque código aberto não é KPI, a motivação dos participantes é mais pura. O mapa de máscaras do g0v só pôde surgir em 72 horas não porque alguém abriu uma issue, mas porque mil engenheiros sentiram que "isso tinha que ser feito".

Mas esse modelo tem teto. Sem investimento contínuo em nível empresarial, os projetos tendem a estagnar quando os mantenedores centrais se esgotam. Taiwan não falta hackers de fim de semana; faltam cargos que permitam dedicação integral ao código aberto.

Há 44.408 usuários no GitHub que indicam Taiwan (estatísticas de março de 2026). São necessários pelo menos 67 seguidores para entrar no ranking de Taiwan do committers.top. Considerando os 23 milhões de habitantes de Taiwan, esse número significa que há uma conta ativa no GitHub para cada 500 taiwaneses. Comparado com Japão, Singapura e Hong Kong, a atividade per capita de desenvolvedores taiwaneses no GitHub está entre as mais altas da Ásia.

O que merece mais atenção não são os números, mas o tipo de contribuição. O papel dos desenvolvedores de Taiwan em projetos internacionais costuma ser a "infraestrutura invisível": patches de kernel, otimizações de compilador, traduções de localização, escrita de documentação. Estudantes da Universidade Nacional Cheng Kung submetem código diretamente para o kernel do Linux. O MozTW mantém a versão em chinês do Firefox há vinte anos. Essas contribuições não fazem manchetes, mas sem elas o software não funcionaria.

A comunidade de código aberto de Taiwan tem ainda uma característica rara na Ásia: a g0v aplica a metodologia de código aberto à política pública. A plataforma vTaiwan usa a tecnologia Polis para deliberação online, tendo tratado mais de 30 temas, como a regulação da Uber e regulações de fintech. A _MIT Technology Review_ a chamou de "o sistema simples, mas engenhoso, que Taiwan usa para terceirizar leis para a multidão". Isso já não é mais uma questão de escrever código; é aplicar a lógica de colaboração do código aberto à governança democrática.

O código aberto em Taiwan nunca foi apenas assunto da comunidade técnica. É uma atitude: ver um problema, abrir o editor, começar a escrever.

## Referências

1. [g0v Manual de Projetos e Comunidade de Tecnologia Cívica](https://g0v.hackmd.io/@jothon/ctpbook) (fonte primária)
2. [2020, um ano turbulento: a contribuição do g0v não se limitou ao "mapa de máscaras"](https://www.gvm.com.tw/article/76428) — Global Views Monthly
3. [A tecnologia cívica pode ajudar a deter uma pandemia](https://www.foreignaffairs.com/articles/asia/2020-03-20/how-civic-technology-can-help-stop-pandemic) — Foreign Affairs (fonte em inglês)
4. [O poder dos hackers cívicos: g0v, o governo de hora zero](https://www.taiwan-panorama.com/Articles/Details?Guid=61281c3d-f79c-4db7-93d9-d18b29f90ba0) — Taiwan Panorama
5. [Audrey Tang, líder da comunidade open source internacional: open source é o novo paradigma de intercâmbio](https://www.ithome.com.tw/news/93603) — iThome
6. [Hong Jen-yu — Wikipédia](https://zh.wikipedia.org/zh-tw/%E6%B4%AA%E4%BB%BB%E8%AB%AD)
7. [Huang Ching-chun — Wikipédia](https://zh.wikipedia.org/zh-tw/%E9%BB%83%E6%95%AC%E7%BE%A4)
8. [Free Software Foundry — Wikipédia](https://zh.wikipedia.org/zh-tw/%E8%87%AA%E7%94%B1%E8%BB%9F%E9%AB%94%E9%91%84%E9%80%A0%E5%A0%B4)
9. [Sobre a OCF — Open Culture Foundation](https://ocf.tw/en/p/what_is_ocf_en.html)
10. [committers.top — Usuários mais ativos do GitHub em Taiwan](https://committers.top/taiwan.html)
11. [COSCUP — Wikipédia](https://en.wikipedia.org/wiki/COSCUP)
12. [O sistema simples mas engenhoso que Taiwan usa para obter leis via crowdsourcing](https://www.technologyreview.com/2018/08/21/240284/the-simple-but-ingenious-system-taiwan-uses-to-crowdsource-its-laws/) — MIT Technology Review

## Leitura adicional

- [Comunidade open source e g0v](/technology/開源社群與g0v) — fork da narrativa coletiva do governo
- [História da migração das comunidades online de Taiwan](/technology/台灣網路社群遷徙史) — História geracional do BBS ao Discord
- [Mini Taiwan Pulse](/technology/mini-taiwan-pulse) — A abordagem open source pessoal da tecnologia cívica, seis semanas e 193 commits transformando dados abertos em trilhas de luz 3D
- [As Espadas Gêmeas da Softstar](/technology/大宇雙劍) — Outra "história de Taiwan sobre fazer coisas que superam a escala com paixão" (RPG nascido no Guanghua Market)
- [Como se pode dormir sem entrar no porão?](/technology/不入地窖焉能睡覺) — Comunidade de jogadores de 6 milhões de membros nascida nos dormitórios da Universidade Central
