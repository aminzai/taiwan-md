---
title: 'Comunidade de código aberto e g0v'
description: 'Em fevereiro de 2020, quando o mundo ainda disputava máscaras, programadores taiwaneses criaram em 72 horas um sistema para consultar o estoque de máscaras em 13.000 farmácias. Sem ordens governamentais nem verbas, apenas a convicção de que o código muda a sociedade. Este é o governo zero (g0v), um experimento fascinante de "fork do governo".'
date: 2026-03-23
category: 'Technology'
tags: ['Tecnologia', 'Comunidade de código aberto', 'g0v', 'Tecnologia cívica']
subcategory: '開源社群'
author: 'Taiwan.md'
featured: false
lastVerified: 2026-03-23
lastHumanReview: true
readingTime: 8
translatedFrom: 'Technology/開源社群與g0v.md'
sourceCommitSha: '6eeee35c8'
sourceContentHash: 'sha256:ccabd00d4cba7d6b'
sourceBodyHash: 'sha256:c135fc23da71593b'
translatedAt: '2026-07-26T21:33:24+08:00'
---

# Comunidade de código aberto e g0v

> **Resumo em 30 segundos:** Em 2012, após o governo gastar uma fortuna em um anúncio vazio, um grupo de engenheiros decidiu "forkar o governo" — alterando gov.tw para g0v.tw e redesenhando como o governo deveria ser. 8 anos depois, com o surto da COVID-19, esses programadores "amadores" construíram o mapa de máscaras em 72 horas, permitindo que todos os taiwaneses consultassem em tempo real o estoque de máscaras em 13.000 farmácias. Este não é um feito do governo, é uma vitória da sociedade civil.

Na noite de outubro de 2012, Gao Jialiang (高嘉良) sentava-se diante do computador, assistindo ao anúncio do "Plano de Impulso da Dinâmica Econômica" do governo, cada vez mais indignado. O governo gastou mais de 40 milhões de novos dólares taiwaneses produzindo um vídeo promocional, mas o conteúdo era tão vazio que se fazia necessário questionar: seria mais significativo jogar esse dinheiro diretamente na bacia sanitária?

Naquela noite, ele tomou uma decisão que mudaria Taiwan: **se o governo não faz bem, nós faremos.**

Ele alterou a letra "o" do domínio gov.tw para o número "0", criando g0v.tw. Este simples jogo de palavras simbolizava um conceito totalmente novo: **fork the government** (fork do governo). Assim como no software de código aberto, se a versão original tem problemas, faz-se um fork (ramificação) e reescreve-se uma versão melhor.

## Fork do governo: um experimento cívico na era digital

O g0v não busca derrubar o governo, mas sim "paralelizar" o governo — usando a colaboração de código aberto para reimaginar como os serviços governamentais deveriam ser.

**Em dezembro de 2012**, ocorreu o zero-hackathon (hackathon) do g0v no Instituto de Matemática da Academia Sinica, com a participação de mais de 40 pessoas. O primeiro projeto foi resgatar o "Orçamento Geral do Governo Central" do "inferno em PDF", transformando-o em um site de visualização interativa.

Originalmente, o livro de orçamento do governo era um PDF de mais de 500 páginas, repleto de números e tabelas densas, incompreensíveis para o público geral. Os voluntários do g0v reorganizaram esses dados, criando gráficos interativos — **com um clique, você pode ver para onde o governo gastou seus impostos.**

> **📝 Nota da curadoria**
> A escolha do primeiro projeto do g0v para a visualização do orçamento governamental não foi por acaso. O orçamento é o núcleo da política democrática — o povo tem o direito de saber o que o governo faz com o dinheiro dos cidadãos. Mas os livros de orçamento tradicionais foram feitos para serem incompreensíveis. O g0v usou a tecnologia para decifrar essa "opacidade intencional".

Este pequeno experimento provou uma coisa: **o fato de o governo não fazer algo não significa que seja impossível. Significa apenas que ninguém o fez.**

## O Movimento 318: a demonstração de fogo da tecnologia cívica

Na noite de 18 de março de 2014, estudantes ocuparam o Legislativo Yuan (Parlamento). Na manhã seguinte, voluntários do g0v apareceram no local, não para protestar, mas para "construir a infraestrutura".

**Ninguém organizou, ninguém comandou.** Os participantes da comunidade g0v assumiram espontaneamente estas ações:

- **Transmissão ao vivo:** Construíram um sistema de transmissão multi-câmera, permitindo que o mundo inteiro visse o que ocorria dentro do recinto legislativo.
- **Integração de informações:** Criaram pastas no Hackfoldr para coletar, organizar e verificar em tempo real as diversas informações da internet.
- **Colaboração de massa:** Estabeleceram um sistema de notas compartilhadas, permitindo que o público fora do local participasse da coleta de dados e da verificação de fatos.
- **Conexão externa:** Forneceram tradução simultânea em múltiplos idiomas, permitindo que a mídia internacional compreendesse as demandas do protesto em tempo real.

**Durante os 24 dias de ocupação, a transmissão ao vivo foi de alta qualidade e nunca caiu.** Isso era uma conquista técnica inacreditável em 2014. Na época, o Facebook Live ainda não existia e a transmissão ao vivo do YouTube não era comum, mas os voluntários do g0v construíram, usando ferramentas de código aberto, um sistema de transmissão mais estável do que o da mídia profissional.

Mais importante ainda, provaram o poder da "transparência". Graças à transmissão ao vivo, todos podiam ver o que acontecia no recinto legislativo, tornando impossível para o governo distorcer os fatos. Este modelo de "usar a tecnologia para supervisionar o governo" foi posteriormente aprendido e imitado por movimentos cívicos em todo o mundo.

## Mapa de máscaras: um milagre em 72 horas

No início de fevereiro de 2020, a COVID-19 começou a se espalhar em Taiwan. O governo anunciou a política de registro de compra de máscaras, permitindo a compra de 2 máscaras por pessoa por semana. A questão era: onde comprar? Quais farmácias ainda tinham estoque?

**Em 6 de fevereiro**, a Ministra de Política Digital, Audrey Tang (que é também membro fundador do g0v), anunciou que o governo abriria os dados de estoque de máscaras de 13.000 farmácias conveniadas em todo Taiwan, atualizados a cada 30 minutos.

**Em 8 de fevereiro**, o primeiro mapa de máscaras foi lançado.
**Em 9 de fevereiro**, mais de 100 versões diferentes do mapa de máscaras já existiam.

Este não foi um projeto contratado por uma empresa de TI do governo, mas sim o resultado do "trabalho extra voluntário" de programadores de todo Taiwan. **Todos queriam contribuir para o combate à epidemia, e o que os programadores podiam fazer era escrever código.**

As versões mais populares incluem:

- **Mapa de máscaras de Taiwan** por Howard Wu: interface de mapa simples e clara
- **Há máscaras?** por kiang: integração de comentários sobre farmácias e informações de funcionamento
- **Onde comprar máscaras** por Finjon Kiang: suporte à função de consulta por voz

Em 72 horas, Taiwan já possuía o sistema de consulta de estoque de máscaras mais completo do mundo. **Enquanto os cidadãos de outros países ainda faziam filas para comprar, os taiwaneses já podiam consultar em seus celulares quantas máscaras restavam na farmácia mais próxima.**

> **⚠️ Perspectiva controversa**
> Alguns criticam o governo por "ter terceirizado a responsabilidade para os voluntários", fazendo com que a sociedade civil construísse sistemas gratuitamente para o governo. A resposta da comunidade g0v é direta: não estamos sendo usados pelo governo, escolhemos ativamente usar nossa expertise para retribuir à sociedade. Além disso, o mapa de máscaras de código aberto é mais fácil de usar, mais inovador e mais alinhado às necessidades do usuário do que os sistemas que o próprio governo teria feito.

## A magia da colaboração de código aberto

O modelo de funcionamento do g0v é simples: **sem chefe, sem funcionários, sem orçamento, sem escritório.** Apenas um grupo de pessoas dispostas a resolver problemas sociais com tecnologia e uma cultura de colaboração de código aberto.

### Cultura do Hackathon

Realiza-se um grande hackathon a cada dois meses, onde os participantes apresentam ideias, formam equipes e desenvolvem no local. O fluxo é:

1. **Apresentação em três minutos:** Qualquer pessoa pode subir ao palco para propor uma ideia
2. **Formação livre de equipes:** Pessoas interessadas podem se juntar ao projeto
3. **Desenvolvimento no local:** Começa-se a trabalhar no dia
4. **Apresentação de resultados:** À tarde, compartilham-se os progressos do dia

**Ninguém é rejeitado, nenhuma ideia é negada.** O único requisito é que o projeto seja de código aberto, permitindo que outros continuem a melhorá-lo.

### Ferramentas de colaboração

- **Canais no Slack:** Discussões diárias e compartilhamento de informações
- **GitHub:** Gerenciamento de código e controle de versão
- **HackMD:** Documentos de notas compartilhadas e atas de reuniões
- **Trello:** Gerenciamento de projetos e acompanhamento de progresso

### Três espíritos centrais

1. **Código aberto:** O código, os dados e a documentação de todos os projetos são públicos
2. **Descentralização:** Não há hierarquia de liderança; qualquer pessoa pode iniciar um projeto
3. **Prática acima de tudo:** "Talk is cheap, show me the code" (Falar é barato, mostre-me o código)

> **💡 Você sabia?**
> A comunidade g0v tem uma tradição: em cada hackathon, são preparados adesivos de "pequeno esquilo". Se você participa pela primeira vez, recebe um adesivo de esquilo. Este design sugere: mesmo que você seja um novato, você é bem-vindo a contribuir com um pouco de força; assim como o esquilo coleta bolotas, cada pequena contribuição é importante.

## Projetos importantes e impacto social

Em 8 anos, a comunidade g0v produziu centenas de projetos, muitos dos quais influenciaram diretamente as políticas governamentais e o funcionamento da sociedade.

### Transparência nos trabalhos do Legislativo Yuan

Os **Registros de Atividades do Legislativo Yuan** eram anteriormente apenas em texto, dificultando ao público geral compreender o que os legisladores realmente faziam no parlamento. Voluntários do g0v criaram a plataforma "Transparência nos Trabalhos do Legislativo Yuan", oferecendo:

- **Transmissão ao vivo:** Transmissão ao vivo das sessões do Legislativo Yuan
- **Registros de fala:** Estatísticas e busca de conteúdo das falas de cada legislador
- **Registros de votação:** Resultados de votação de leis importantes
- **Acompanhamento de propostas:** O processo completo da proposta à aprovação em terceira leitura

O resultado foi: **os legisladores passaram a se importar com seus "dados".** A taxa de presença, o número de perguntas e o número de propostas — números que antes ninguém se importava — agora têm sites que os calculam automaticamente. Os representantes eleitos descobriram que cada um de seus movimentos era supervisionado, e seu comportamento começou a mudar.

### vTaiwan: um experimento de democracia digital

Em 2014, o g0v e o governo lançaram juntos a plataforma vTaiwan, permitindo que o público participasse do processo de formulação de políticas. O caso mais famoso foi a controvérsia sobre o Uber:

**Em 2015**, a operação do Uber em Taiwan gerou protestos por parte dos taxistas. O tratamento tradicional seria uma decisão unilateral do governo, mas o vTaiwan ofereceu um terceiro caminho: permitir que todas as partes interessadas conversassem na plataforma online e encontrassem uma solução ganha-ganha.

Após meses de discussões online e oficinas presenciais, formou-se a política de "táxis diversificados", protegendo os direitos dos taxistas tradicionais enquanto permitia a existência de modelos de serviço inovadores.

**Esta foi a primeira vez que Taiwan resolveu uma controvérsia de política usando "democracia digital".**

### Impulsionadores do governo aberto

As reivindicações do g0v influenciaram diretamente as políticas governamentais:

- **2012:** O projeto de visualização do orçamento governamental impulsionou o governo a abrir os dados do orçamento
- **2013:** O projeto de transparência do Legislativo Yuan levou à transmissão ao vivo dos trabalhos do Legislativo Yuan
- **2014:** Após o Movimento dos Lírios das Estrelas (318), o governo prometeu promover a revisão da "Lei de Acesso à Informação Governamental"
- **2015:** A plataforma vTaiwan tornou-se um canal oficial de participação política do governo
- **2016:** Audrey Tang assumiu o cargo de Ministra de Política Digital, trazendo a experiência do g0v para o governo

## Influência internacional e conexões

A experiência do g0v não apenas influenciou Taiwan, mas também inspirou movimentos de tecnologia cívica em todo o mundo.

### Rede Code for All

O g0v é membro fundador da rede internacional **Code for All**, cooperando estreitamente com organizações como Code for Japan (Japão), Code for Korea (Coreia do Sul) e Code for America (EUA).

**Em 2019**, o g0v summit foi realizado em Taipei, reunindo comunidades de tecnologia cívica de mais de 30 países para compartilhar experiências e tecnologias.

### Cooperação internacional durante a epidemia

Durante a epidemia de 2020, a experiência do mapa de máscaras do g0v foi aprendida por outros países:

- **Itália:** Versão Roma do mapa de máscaras
- **Alemanha:** Versão Berlim do mapa de máscaras
- **EUA:** Mapa de EPI (Equipamentos de Proteção Individual)
- **Coreia do Sul:** 마스크맵 (mask map)

Voluntários do g0v também ajudaram ativamente outros países a construir sistemas semelhantes, compartilhando a experiência de tecnologia de combate à epidemia de Taiwan com o mundo.

## Desafios e futuro

Como uma "organização sem chefe", o g0v enfrenta os desafios que todas as comunidades de código aberto encontram.

### Sustentabilidade dos projetos

Muitos projetos do g0v são produtos de "impulso momentâneo", carecendo de manutenção a longo prazo. O mapa de máscaras foi muito ativo durante a epidemia, mas após o fim da epidemia, gradualmente ninguém mais o manteve. **Como fazer com que bons projetos continuem operando é o maior desafio do g0v.**

### Fadiga dos participantes

A participação voluntária de alta intensidade por 8 anos fez com que alguns dos primeiros contribuidores começassem a sentir fadiga. Como atrair novos talentos e tornar a participação mais sustentável são questões que a comunidade precisa enfrentar.

### Relação com o governo

A relação entre o g0v e o governo é sutil: cooperação e supervisão simultâneas. Quando o governo abraça ativamente o código aberto e a democracia digital, o papel de "oposição" do g0v torna-se difuso. Manter a independência e o espírito crítico durante a cooperação é um desafio contínuo.

### Desinformação e guerra de informações

Na era da guerra de informações, o princípio da abertura e transparência também pode ser abusado. Como manter a abertura ao mesmo tempo em que se evita tornar-se um canal de propagação de desinformação é um novo desafio.

## Um experimento que continua

Em 2012, quando Gao Jialiang alterou gov.tw para g0v.tw, ele apenas queria expressar sua insatisfação com o governo. 12 anos depois, o g0v já se tornou parte da democracia de Taiwan e uma força importante no movimento de tecnologia cívica mundial.

Este experimento provou algumas coisas:

1. **A tecnologia pode ser uma ferramenta de participação cívica**, não apenas um meio de lucro comercial
2. **A abertura e transparência são mais importantes do que a eficiência do governo**, pois a transparência traz eficiência
3. **Pequenas raivas podem mudar o mundo**, desde que você esteja disposto a colocar a mão na massa
4. **Forkar o governo não é derrubar o governo**, mas sim provar que existem possibilidades melhores

Nesta era de retrocesso democrático, o g0v nos lembra: **os cidadãos não são usuários do governo, são co-criadores.** Coisas que o governo não faz bem, nós podemos fazer. Coisas que o governo faz bem, podemos ajudá-lo a fazer ainda melhor.

Esta não é uma revolução que termina, mas um experimento contínuo. Cada hackathon, cada novo projeto, cada linha de código, responde à mesma pergunta: na era digital, como a democracia pode ser?

A resposta ainda está sendo escrita, e cada pessoa disposta a contribuir é autora desta resposta.

## Referências

- [Site oficial do governo zero g0v](https://g0v.tw/)
- [Organização GitHub do g0v](https://github.com/g0v)
- [Pastas de notas compartilhadas do g0v no Hackfoldr](https://beta.hackfoldr.org/)
- [Rede internacional Code for All](https://codeforall.org/)
- [Plataforma de democracia digital vTaiwan](https://vtaiwan.tw/)
- [Participação democrática na era digital: dos Lírios das Estrelas ao g0v](https://www.books.com.tw/products/0010867342)
- [Palestra TED: Como corrigir o governo sem permissão](https://www.ted.com/talks/audrey_tang_how_digital_innovation_can_fight_pandemics_and_strengthen_democracy)
- [Entrevista com os desenvolvedores do mapa de máscaras](https://www.ithome.com.tw/news/136038)

## Tópicos relacionados

- [Fundação da Cultura Aberta](/technology/開放文化基金會): A fundação por trás do g0v que paga contas, emite notas fiscais e suporta a administração da comunidade, e a história de como ela cresceu a partir dos bastidores para se tornar um guardião dos direitos digitais
- [Indústria de semicondutores](/technology/半導體產業): A base da força tecnológica de Taiwan
- [Mini Taiwan Pulse](/technology/mini-taiwan-pulse): Uma implementação de código aberto de tecnologia cívica em 2026 — usando dados abertos do TDX + Three.js para desenhar Taiwan em faixas de luz 3D
