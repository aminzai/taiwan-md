---
title: 'Como um artigo é criado: a linha de produção de seis estágios do Taiwan.md que combate o instinto da escrita por IA (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)'
description: 'Cada artigo que você lê no Taiwan.md possui profundidade, contexto e verificabilidade; por trás dele, há 6 estágios, mais de 20 portões obrigatórios e uma redação editorial de IA que não escreve seus próprios textos. A única razão para esta máquina existir é combater os erros mais comuns da escrita por IA: organizar fatos apenas por ordem cronológica, gerar frases genéricas sem valor informativo, traduzragamente resumos em inglês para citações falsas e ser contaminado por maus hábitos de textos antigos. Este artigo disseca essa linha de produção — e ele próprio é um produto dela.'
date: 2026-06-19
tags:
  [
    'about',
    'meta',
    'metodologia de escrita',
    'curadoria',
    'rewrite-pipeline',
    'editorial',
    'semiont',
    'escrita por IA',
  ]
author: 'Taiwan.md'
category: 'About'
readingTime: 11
featured: false
lastVerified: 2026-06-19
lastHumanReview: false
relatedDiary:
  - 2026-06-19-123349-manual
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: '984fb7892'
sourceContentHash: 'sha256:92fcb394123e4aee'
sourceBodyHash: 'sha256:b8984a2133e5738f'
translatedAt: '2026-07-24T21:09:07+08:00'
---

# Como um artigo é criado: a linha de produção de seis estágios do Taiwan.md que combate o instinto da escrita por IA (REWRITE-PIPELLEINE v7.5 × EDITORIAL v6.12)

> **Resumo em 30 segundos:** Cada artigo que você lê no Taiwan.md é fruto de uma linha de produção de seis estágios: primeiro define-se o ponto de vista, depois pesquisa-se, escreve-se a conclusão primeiro, verifica-se palavra por palavra, adiciona-se o visual e, por fim, criam-se os links bidirecionais. Esta linha não é um "fluxo comum de boa escrita"; cada um de seus portões é projetado para barrar um erro específico da escrita por IA: organizar fatos apenas cronologicamente, gerar frases genéricas sem valor informativo, traduzir resumos em inglês para criar citações falsas e ser contaminado pelos maus hábitos de textos antigos. Este artigo disseca essa linha de produção — e ele próprio é um produto dela.

Às 19h53 do dia 18 de junho de 2026, um _commit_ entrou silenciosamente no ramo `main`. Um artigo sobre a banda de trio taiwanense "Elephant Gymnastics" (大象體操) foi publicado: 5.604 caracteres chineses, 56 notas de rodapé e 11 subtítulos baseados em cenas[^1]. Naquele momento, não havia ninguém diante do computador. Foi o _routine_ do Taiwan.md que, durante uma noite sem ninguém de plantão, terminou de escrever e publicou o texto por conta própria.

Mas, antes daquele _commit_, este artigo passou por quase cem pesquisas, leu 59 fontes e teve sua redação original refutada em 12 pontos durante a verificação. Ele percorreu 6 estágios e mais de 20 portões obrigatórios, utilizando uma equipe editorial de IA com divisões de tarefas bem definidas. O que você lê são os 5.604 caracteres acima da superfície. Este artigo quer que você veja a máquina abaixo dela.

```tw-figure
Cerca de 100 pesquisas → 1 artigo
Coleta para 〈Elephant Gymnastics〉: aprox. 95 consultas, 59 fontes, 12 refutações
Registro do routine do Taiwan.md, 18-06-2026
```

## Por que construir uma máquina para um único artigo

Se você der um tema a uma IA e pedir para escrever um artigo, ela provavelmente fará o seguinte: pesquisará, organizará os fatos encontrados por ordem cronológica, adicionará uma frase de conclusão que soa significativa em cada parágrafo e terminará com algo como "o desenvolvimento continuará no futuro". A Wikipédia já tem esse tipo de conteúdo; fazendas de conteúdo de IA produzem dezenas de milhares disso todos os dias. O Taiwan.md decidiu, desde o primeiro dia, não fazer isso.

O problema é que esses maus hábitos são o padrão da IA, não erros ocasionais. O REWRITE-PIPELINE os decompõe em seis tipos de falhas recorrentes: o limite de _tokens_ acaba no meio do texto; a segunda metade vira um rascunho sem cuidado; a falta de pontos de verificação causa uma queda silenciosa na qualidade; a conclusão é deixada para o fim e perde o vigor; as normas de formatação rica são esquecidas ao final; diferentes ângulos de abordagem são tratados como processos independentes; e a falha mais fatal: pesquisar os fatos e só depois tentar pensar no ponto de vista, resultando em uma narrativa cronológica com densidade desequilibrada[^2].

Portanto, a lógica de design desta linha é simples: para cada erro possível, existe um portão para impediamente-lo. Não é um fluxo genérico de "boa escrita"; é o inverso do _AI slop_ (conteúdo lixo gerado por IA).

> **✦** "A Wikipédia responde 'O que é o PTT?'. O Taiwan.md responde 'Por que o PTT merece 8 minutos da sua leitura'."

Eis como o artigo sobre Elephant Gymnastics saiu do outro lado da linha:

```tw-stat
5.604 caracteres | Texto principal em chinês | 〈Elephant Gymnastics〉
56 | Notas de rodapé, todas verificáveis via Ctrl-F | Verificação primária
11 seções | Subtítulos baseados em cenas, sem ordem cronológica | Ritmo narrativo
12 pontos | A fase de pesquisa refutou a redação original | Prioridade à refutação
Fonte: Registro do routine do Taiwan.md, 18-06-2026
```

## Seis estágios, cada um prevenindo uma falha

Esta linha de produção percorre seis estágios do início ao fim; todos os artigos devem completá-los, independentemente do tema ou extensão.

**Estágio 0: Ponto de Vista** — definir claramente que memória este artigo representa para os taiwaneses e onde reside a tensão central. **Estágio 1: Coleta** — iniciar a pesquisa com pelo menos 80 consultas no total, com cotas fixas: no mínimo 40 fontes em chinês, 20 em inglês, 15 primárias e 5 de perspectivas opostas, forçando a busca por evidências que contrariem as próprias hipóteses[^3]. **Estágio 2: Escrita** — o primeiro passo é escrever a conclusão, pois a energia humana se esgota ao final; deixar o encerramento mais importante para o fim é entregá-lo à sua versão mais exausta. **Estágio á: Verificação** — conferência palavra por palavra: cálculos, unidades e cada citação devem ser localizáveis via Ctrl-F na fonte original. **Estágio 4: Forma** — adicionar elementos visuais e mídia. **Estágio 5: Conexão** — integrar este artigo aos outros artigos da base de conhecimento por meio de links bidirecionais.

A distribuição de esforço entre os seis estágios é deliberada. A escrita consome mais de 40%, mas a pesquisa somada à verificação representa quase metade do total. O tempo real gasto em um artigo não está na digitação, mas no que vem antes e depois dela.

```tw-bars
Onde o esforço de um artigo é aplicado (limite de orçamento de tokens por estágio, %)
Estágio 0: Ponto de Vista | 12 | Reflexão pré-edição
Estágio 1: Coleta | 28 | Pesquisa ≥ 80 consultas
Estágio 2: Escrita | 42 | Conclusão escrita primeiro
Estágio 3: Verificação | 18 | Verificação palavra por palavra
Estágio 4: Forma | 8 | Visual e mídia
Estágio 5: Conexão | 5 | Links bidirecionais
Fonte: Orçamento de cada estágio do REWRITE-PIPELINE v7.5
```

## Primeiro pense, depois pesquise

O mais contra-intuitivo entre os seis estágios é o primeiro.

A maior parte da escrita por IA segue o padrão "pesquisar para descobrir fatos e depois retornar para adicionar um ponto de vista". No v6.0, o Taiwan.md inverteu essa ordem: antes de iniciar a pesquisa, assume-se a perspectiva de um editor-chefe para refletir sobre seis questões: que memória este tema evoca nos taiwantes, quais faces foram ignoradas e como ele se conecta à nossa história de vida. Somente após isso, partimos para a pesquisa com perguntas específicas para validar as hipóteses.

Por que essa ordem é tão crucial? Um artigo serve de lição. Ao escrever sobre a marca _Apple Cider_ (蘋果西打), a linha primeiro pesquisou e encontrou uma crise de quase desaparecimento por falta de vendas; o artigo acabou virando uma história de "espécie em perigo". Um observador retornou dizendo que a Apple Cider é uma memória coletiva que atravessa 60 anos, desde as garrafas de vidro da era das máquinas de soda até hoje[^4]. Escrevê-la apenas como uma notícia de crise foi reduzir a escala da memória. A versão baseada em pesquisa prévia transformou uma lembrança calorosa em algo ansioso.

```tw-versus
Instinto da IA: Pesquisar para depois falar | Taiwan.md: Pensar antes de pesquisar
Encontra fatos e tenta forçar um ponto de vista | Define o ponto de vista e usa a pesquisa para validar
Insere todos os fatos no texto, gerando densidade desequilibrada | Remove fatos que não cabem no ponto de vista
Sem um âncora central, a conclusão vira algo genérico | Sem um âncora correspondente, o ponto de vista é reavaliado
Escreve como uma cronologia corporativa ou currículo | Escreve como uma história que gera o "entendi!"
Fonte: REWRITE-PIPELamente v7.5 Estágio 0: Ponto de Vista
```

## Pesquisa: tratar o relatório de pesquisa como um artigo acadêmico

Com o ponto de vista definido, inicia-se a busca. A pesquisa no Taiwan.md possui dois números rígidos: um artigo profundo exige pelo menos 80 consultas e as cotas de fontes são fixas — mínimo de 40 em chinês, 20 em inglês, 15 primárias e 5 de posições opostas. Esta última é a mais fácil de ignorar por preguiça, mas ela força o redator a buscar evidências que conflitem com suas próprias suposições.

Terminar a pesquisa não significa apenas inserir resumos no texto. Por trás de cada artigo profundo, há um relatório de pesquisa comparável a um artigo acadêmado, dividido em oito capítulos: Ponto de Vista, Log de Pesquisa, Descobertas por Tema, Repositório de Citações, Contraexemplos e Salvaguardas, Pacote de Fatos Limpos para o Redator, Referências e Checklist de Verificação; a última seção contém os relatórios brutos, sem omissões, de cada agente de pesquisa. Uma regra é rigorosa: se você pesquisou mas não registrou o rastro original no relatório, a pesquisa é considerada inexistente. O relatório é a fonte da verdade deste artigo; ele deve passar por uma ferramenta de auditoria que exige pelo menos 25 fontes únicas, zero ausência de fontes em inglês e zero ausência de fontes primárias[^9]. Se não passar, o artigo nem sequer tem permissão para ser escrito.

```tw-stat
≥ 80 | Profundidade de pesquisa de um artigo profundo | Chinês 40 / Inglês 20 / Primária 15 / Oposta 5
8 | Estrutura do relatório de pesquisa | Comparável a um artigo acadêmico
≥ 25 | Fontes únicas (aprovado pela auditoria) | Inglês ≠ 0, Primária ≠ 0
Fonte: REWRITE-PIPELINE v7.5 Passo 1.1 / 1.7
```

Temas polêmicos exigem um passo extra. Ao escrever sobre política, história ou políticas públicas, designamos um agente "oposto" para buscar fontes que apresentem argumentos racionais contrários ao texto principal; cada uma deve incluir o URL. Se não houver argumentos suficientes, escrevemos honestamente que "a argumentação oposta é fraca", sem forçar a barra. Um artigo com apenas uma voz não é considerado concluído aqui.

Há uma linha vermelha nas citações. Aspas são uma promessa: o que está entre elas deve ser a fala exata do original; portanto, cada citação deve ser localizável via Ctrl-F na fonte primária. O erro mais comum ocorre quando uma ferramenta captura um site chinês, mas retorna um resumo em inglês, e o redator traduz esse inglês de volta para o chinês como se fosse uma "citação direta" — isso é fabricação. Em 2026, ao escrever sobre Li Yang (李洋) e os esporos, cometemos esse erro: a ferramenta retornou em inglês "I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin", que traduzido para o chinês virou "Eu cheguei primeiro à escola, mas não consegui acompanhar Qi-lin". No entanto, a fala original de Li Yang em chinês era: "Havia 15 pessoas na turma de educação física, eu estava no grupo de trás, e Qi-lin estava no grupo da frente"[^10]. O sentido é próximo, mas o tom é totalmente diferente; por isso, citações traduzidas de resumos não são aceitas.

## Escrita: cada artigo precisa de uma pessoa

Com os materiais reunidos, entramos na fase que exige mais esforço. O EDITORIAL é o documento que ensina ao Taiwan.md como transformar matéria-prima em um artigo com alma; ele estabelece três leis fundamentais: deve haver uma história, não apenas informações; cada fato deve ser verificável; e cada artigo deve ter uma pessoa[^11].

A terceira lei é a mais fácil de ignorar, mas a mais crucial. Instituições não são lembradas, conceitos também não; pessoas são. Portanto, em um artigo sobre a TSMC, em vez de começar pela empresa, comece por uma pessoa específica; em um artigo sobre o Seguro Nacional de Saúde, come mais de um cartão, de uma sala de consulta ou de um indivíduo. Ao reduzir temas abstratos a algo humano que o leitor possa acompanhar, o artigo ganha temperatura e cumpre a promessa de ser algo que as pessoas queiram compartilhar após a leitura.

## Cinco coisas que devem ser encontradas antes de começar a escrever

O EDITORIAL chama a preparação antes do estado de escrita de "os olhos que observam o material": ao receber um conjunto de dados, você deve encontrar cinco elementos; se não os encontrar, não comece a escrever[^5].

**Conflito**: a tensão central expressa em uma frase — alguém fez X, mas isso entra em conflito com o que acredita (Y). **Objeto**: algo concreto que o leitor possa ver ou tocar — como o pão de pétalas de rosa de Wu Po-chun ou a esfera dourada de 660 toneladas suspensa no 87º andar. **Citação**: uma frase dita literalmente por uma pessoa real; como as aspas são uma promessa de fidelidade, devem ser localizáveis via Ctrl-F na fonte. **Cena**: um momento com tempo, lugar e ação — transformar "a política foi aprovada" em "no dia 8 de janeiro de 2025, durante a revisão do Comitê de Saúde e Meio Ambiente no Legislativo". **Detalhe**: a cor da roupa, o clima daquele dia, o tom de voz; elementos que não estão em tabelas técnicas, mas são a prova de que "alguém realmente estava lá".

Dentre esses cinco, o conflposto vem em primeiro lugar.

```tw-quote
Se não encontrar o conflito, este artigo não deve ser reescrito
REWRITE-PIPELINE v7.5 | Estágio 1.4: Localizando o conflito
```

A tensão pode ser conflito, falha ou crise, mas a perspectiva deve ser "como isso se tornou o que é hoje e para onde está indo", e não "o que deu errado aqui e quem deve ser culpado". O mesmo conflito, sob uma visão construtiva, faz o leitor querer participar; sob uma visão apocalíptica, faz o leitor querer fugir.

## Escreva a conclusão primeiro, deixe o início para o final

A ordem de escrita é exatamente o inverso da ordem de leitura.

No Estágio 2, a primeira ação é escrever a conclusão. Parece estranho, mas a lógica é prática: o esforamento humano se esgota ao final; deixar a conclusão mais importante para o último momento é entregá-la à sua versão mais cansada, resultando em frases genéricas como "continuará a brilhar". Escrevendo a conclusão primeiro, você bloqueia esse ponto de colapso. Uma boa conclusão tem duas tarefas: resgatar uma imagem plantada no início e colocar o lereader em uma posição um nível mais profundo do que quando começou, uma posição de querer agir.

O Taiwan.md já recebeu seis tipos de boas conclusões: a que deixa uma imagem para reflexão; a que subverte o que foi dito anteriormente (reviravolta); a que salta no tempo para o futuro ou volta ao passado; a que deixa uma pergunta aberta; a que mantém a zona cinzenta sem resolver o conflito; e a que fecha o ciclo narrativo retornando ao início. O artigo sobre a garça-de-coroa-preta é um exemplo de fechamento cíclico: começa com "Em 1865, Swinho Hou coletou um espécime em Tamsui e registrou duas palavras: 'raro'"; termina com "Há 160 anos, Swinho Hou escreveu 'raro' em Tamsui; hoje, ouvimos seu chamado grave de 'wu, wu, wu' todos os dias no Parque Florestal de Da'an"[^12]. As mesmas duas palavras ganham um significado novo devido ao acúmulo de informações durante o texto.

Já o início deve ser diferente: guarde um segredo. As três primeiras frases decidem se o leitor fica, mas a tarefa é convidá-lo para a cena, não contar o evento todo. "No dia do tufão Tao-chi, a professora Hsu Pi-lan estava na escola em Changhua..."; pare aqui, no "estava na escola"; o leitor quererá saber o que aconteceu depois. Se você escrever como um _lead_ de notícia completo, entregando tempo, lugar, evento, ação e resultado, o lelitor terá a informação, mas perderá o interesse em continuar lendo.

## O título é uma promessa que deve ser clicada

O título é a primeira impressão do leitor. O Taiwan.md possui um formato rígido: todos os artigos seguem a "Sanduíche de Dois Pontos (Tema: Gancho do Subtítulo)". Escrever apenas um substantivo é um resumo enciclopédico, o que fere o espírito de curadoria.

```tw-versus
Resumo Enciclopédico (Ruim) | Sanduíche de Dois Pontos (Bom)
Jay Chou | Jay Chou
Jay Chou: De uma sala de ensaio ao lado de 'Secret' até 25 anos de carreira
Tsai Ing-wen | Tsai Ing-wen
Tsai Ing-wen: Da menina de Zuoying, Kaohsiung, à três vezes campeã mundial de badminton; a resistência silenciosa fora das quadras
Dia de folga por tufão | Dia de folga por tufão
De quem é a folga? De quem é o trabalho?
Fonte: EDITORIAL v6.12 §Título: Sanduíche de Dois Pontos
```

O subtítulo deve ser capaz de ser tweetado sozinho e deve ser específico o suficiente para que o leitor entenda imediatamente. A IA é excelente em transformar conflitos centrais em frases abstratas bonitas, resultando em palavras-chave que são apenas substantivos abstratos, fazendo o leitor perguntar "o quê de quê?". O critério é simples: mostre o título a alguém que não leu o artigo; essa pessoa consegue apontar para cada palavra-chave e dizer "isso se refere a algo específico"? "Seguro Nacional de Saúde: um cartão que sustenta o primeiro lugar mundial, mas um futuro insustentável" usa "um cartão"; "Lixo nuclear em Lanyu: promessa de três anos, mantido por quarenta" usa um contraste numérico. Palavras concretas geram cliques pelo desejo de saber; fazendas de conteúdo dependem do "choque" para atrair cliques[^13].

## Um conflito deve sustentar todo o artigo

O conflito central encontrado não pode ser mencionado no início e desaparecer. Ele deve agir como uma coluna vertebral, aparecendo no início, no meio e no fim, para que o artigo se sustente.

No artigo da garça-de-coroa-preta, a espinha dorsal é uma frase: "O pássaro não mudou, o ambiente sim". Ela aparece no resumo, varia no meio para "A ação está correta, o palco está errado", e encerra como "Como uma ilha preserva uma pequena camada florestal úmida entre o concreto". Com o mesmo conflito variando cinco vezes, o leitor entende o "e daí?" ao final. Sem essa espinha dorsal, o artigo se dispersa em uma linha do tempo ou um conjunto de tópicos desconexos.

Além da espinha dorsal, cada parágrafo deve ter base. O Taiwan.md possui uma disciplina de concretude: cada parágrafo narrativo deve ter pelo menos um âncora — nome de pessoa, ano, local, número preciso, nome de obra ou citação. A abstração sobrepondo o detalhe é a digital mais comum da escrita por IA; se um parágrafo não tem âncoras, ao terminar a leitura, resta apenas uma ideia vazia como "ele foi uma pessoa influente". O método de verificação é o teste de abstração reversa: cubra verbos abstratos como "demonstra", "reflete" ou "simboliza"; se o conteúdo restante não conseguir sustentar o parágrafo sozinho, há excesso de abstração; adicione concretude.

Ter um ponto de vista não significa tomar partido. Um verdadeiro ponto de vista tem a coragem de dizer: "a explicação comum inverteu a causalidade". O artigo da garça-de-coroa-preta desafiou ativamente uma explicação científica comum: muitos dizem que "ela se adaptou à cidade e perdeu o medo de humanos"; essa frase é conveniente, mas inverte a causa e o efeito; as aves da família Ardeidae não evoluiriam reflexos nervosos para ignorar humanos em apenas trinta anos; a verdade mais próxima é que as áreas verdes em Taipé aumentaram. Essa explicação reversa deve ser integrada à narrativa principal, não adicionada como uma nota de isenção de responsabilidade ao final.

Por fim, há o ritmo (respiração). Um parágrafo de prosa documental carrega um argumento, contendo causalidade, detalhes e cenário, não apenas um fato isolado. Fragmentar um fato em vários parágrafos faz a leitura parecer picotada; entre os parágrafos, não use conectivos estruturais como "por outro lado" ou "vale notar"; deixe que o final de um parágrafo conduza naturalmente ao início do próximo. O material de pesquisa lhe dá quatro razões; escreva-as em frases fluidas, não as liste como "primeiro, segundo, terceiro", pois isso soa como uma lista, mesmo que formatada como prosa.

## Por que frases "plásticas" são plásticas

Após encontrar os cinco elementos e começar a escrever, o maior inimigo são as frases "plásticas".

A essência da frase plástica é fácil de identificar: se você a remover, nada de informação será perdido no artigo. Ela ocupa espaço, mas não carrega significado. O EDITORIAL lista cinco tipos; o mais comum é a "cola universal", como "demonstra o espírito de X", que funcionaria trocando Taiwan por Japão; há também a "falsa evolução", como "não é apenas um cantor, mas um símbolo cultural"; se você remover a primeira parte, a segunda permanece intacta.

Um tipo mais sutil é a frase de oposição "não é X, mas Y". Ela soa profunda, mas ao analisá-la, o X costuma ser uma posição que a IA assume que o leitor tem, para então inverter para o Y e parecer perspicaz. O problema é que a maioria dos leitores nem sequer possui a premissa X; o X é um espantalho criado apenas para dar palco ao Y. Remova o X e escreva diretamente o Y; o texto fica mais direto e confiante. Esta regra é tão rigorosa que tem números: em um artigo de 1500 caracteres, o uso de "não é X, mas Y" e suas variações não pode exceder 3 ocorrências.

```tw-versus
Versão Plástica: Funciona trocando o sujeito | Versão Curadoria: Pertence apenas a este fato
Demonstra a força dos semicondutores de Taiwan | A TSMC detém 65% do mercado global de processos avançados
Não é apenas um cantor, mas um símbolo cultural | 'Dao Xiang' de Jay Chou foi tocado como música de conforto na área afetada pelo terremoto em Sichuan por três meses
Tem profundo impacto no desenvolvimento democrático de Taiwan | A primeira eleição presidencial direta após o fim da Lei Marcial teve 76% de participação
Uma conquista de engenharia surpreendente | O edifício mais alto do mundo construído em uma ilha com média de 3,7 terremotos anuais
Fonte: Comparação entre Plástico vs. Curadoria (EDITORIAL v6.12 §)
```

> **📝 Nota do Curador**: Este parágrafo que você está lendo acabou de passar pelo mesmo processo de verificação. O Taiwan.md possui uma ferramenta automática que detecta frases plásticas, falsas oposições "não é X, mas Y" e a densidade de travessões em cada artigo. Ao escrever este artigo sobre "apresentação da linha de produção", nenhuma dessas regras foi relaxada. Se um artigo sobre disciplina quebra suas próprias regras, ele perde o direito de falar sobre elas.

## Remova até o "sotaque de tradução" da gramática

A frase plástica é vazio; o sotaque de tradução (estilo europeu/inglês) é outra doença: a fala tem conteúdo, mas a gramática é estrangeira. A escrita por IA em chinês traz nativamente um sotaque de tradução, pois sua estrutura lógica subjacente é baseada no inglês; um artigo pode ter zero frases plásticas, mas parecer inteiramente uma legenda de filme.

Alguns problemas frequentes: uso excessivo da voz passiva ("é considerado a indústria mais importante" — use "é a indústria mais importante"); o "inferno do 'de'" (em chinês, o excesso de partículas possessivas que tornam a frase pesada); verbos fracos ("realizou uma pesquisa profunda" — escreva apenas "pesquisou profundamente"); e o uso de "através de..." (que em 90% das vezes pode ser substituído por "com" ou simplesmente deletado). O único método de verificação é ler em voz alta: se soar como uma legenda traduzida, está errado; se soar como uma pessoa falando, passou. A raiz desta visão vem de um ensaio de Yu Kwang-chung de quarenta anos atrás sobre a normalidade e anormalidade da língua chinesa. Termino com um mantra: uma mãe não diria "através de..." nem "como uma mãe...".

## Escreva Taiwan como um lugar onde as pessoas queiram participar

O plástico e o sotaque de tradução são disciplinas ao nível da frase; o nível superior é a postura.

O Taiwan.md escreve sobre temas sérios — soberania, guerra cognitiva, demografia, meio ambiente — com profundamente, mas há uma linha: a esperança deve ser construída sobre a honestidade. Reconhecemos todos os problemas, mas recusamos deixar o leitor partindo com ansiedade, pequenez ou impotência. O critério é simples: após a leitura, o leitor sente que quer fazer algo por Taiwan, ou sente-se mais ansioso e inadequado? Se for o primeiro, mantemos; se for o segundo, alteramos. Assim, para uma mesma crise, o enquadramento é "como isso se tornou o que é hoje e para onde está indo", e não "está acabando, você deve ter medo". O estilo de ansiedade midiática como "o X está desaparecendo" ou "se não agirmos agora, será tarde demais" tem a mesma forma da guerra cognitiva; não use.

A moderação é o outro lado. Famílias, doenças, conflitos e falhas humanas podem ser escritos, mas deve-se evitar descrições gráficas de morte, suicídio ou tragédias éticas. A morte pode ser escrita em termos de tempo, lugar e fatos reportados publicamente, sem reconstruir segundo a segundo os momentos finais; o autoextermínio pode ser escrito em termos de evento e contexto social, sem detalhes do método. O critério é o mesmo: se a pessoa envolvida ou seus familiares lerem isso, sentirão o respeito de um diretor de documentário ou a proximação de uma mídia que busca lucro com lágrimas?

Há também um hábito pequeno, mas vital: escreva "Taiwan" abertamente. A digital da evasão está escondida em traduções estrangeiras, usando "esta ilha" ou "este lugar" como substitutos para evitar escrever Taiwan, especialmente em títulos e introduções. Usar "ilha" como imagem literária ou cenário geográfico é permitido e encorajado; o que deve ser combatido é a evasão por medo de nomear Taiwan.

## A diferença que se percebe num relance

Como essas disciplinas se traduzem na prática? O melhor modo é ver um antes e depois.

Ao escrever sobre Annette Yani (戴資穎), o modelo vazio da IA seria: "famosa jogadora de badminton de Taiwan, com excelente desempenho internacional, vencedora de vários prêmios, trazendo glória para Taiwan", seguido por quatro tópicos: principais conquistas, estilo de jogo, impacto internacional e contribuição social. O parágrafo não contém um único ano específico ou uma partida concreta; o sujeito poderia ser qualquer atleta.

```tw-versus
Modelo Vazio da IA | Versão Curadoria
Excelente desempenho, glória para Taiwan | Alcançou o primeiro lugar do mundo e permaneceu por 214 semanas consecutivas
Quatro tópicos: Conquistas/Estilo/Impacto/Contribuição | Chorou após a final de ouro nos Jogos de Tóquio 2020; tornou-se o primeiro termo pesquisado no Google Taiwan
O sujeito poderia ser qualquer um | Treina 6 horas por dia desde os 6 anos; estilo de jogo "mágico" com a mão esquerda
Fonte: EDITORIAL v6.12 §Antes/Depois: Annette Yani
```

A versão de curadoria faz apenas uma coisa: substituir cada adjetivo abstrato por um fato verificável. 214 semanas é o período mais longo na história do badminton feminino; a final de ouro em Tóquio 2020 contra Chen Yu-fei é um momento que Taiwan inteiro lembra. A "temperatura" reside em momentos como "o instante da derrota foi justamente quando o leitor se conectou". O mesmo vale para Mayday: em vez de escrever "uma das bandas de rock mais influentes de Taiwan, conquistando fãs com música positiva", escreva "cinco estudantes da High School anexa à Universidade Normal começaram tocando em palcos de rua; 28 anos depois, tocaram dois shows no Madison Square Garden em Nova York (o mesmo palco onde os Beatles tocaram nos EUA), com ingressos esgotados em 48 horas"[^13].

## Uma equipe editorial que não escreve seus próprios textos

Surge uma questão: quem está escrevendo?

A resposta é um tanto contra-intuitiva. A sessão que lidera todo o processo evita deliberadamente escrever o texto. A razão reside em uma lei de ferro: se uma IA lê um artigo antigo de baixa qualidade, ela inconscientemente imita seu tom, estrutura e até seus maus hábitos. Usar o texto antigo como esqueleto para reescrever é permitir que o vírus infecte o novo conteúdo.

Por isso, a linha de produção divide os papéis[^6]. A sessão principal atua como editor-chefe, responsável pela coordenação, verificação e revisão final, mas não toca na caneta. Quem escreve de fato é outro agente de IA, um "redator limpo", que lê o relatório de pesquisa completo e o ponto de vista definido; ele não vê o texto antigo problemático nem as reclamações dos leitores. Ele começa como se fosse a primeira vez que escreve sobre o tema, mas possui em mãos todos os materiais já verificados. O ponto de vista é entregue ao modelo com maior capacidade de julgamento; a expansão de reações do leitor é delegada a quatro modelos paralelos; e a verificação palavra por palavra é feita por um lote de modelos mais econômicos confrontando as fontes primárias. Por trás de um artigo, há uma equipe editorial especializada.

Essa divisão foi conquistada através de retrocessos. Uma vez, ao fornecer apenas um resumo ao redator sem permitir a leitura dos materiais origentes, o artigo piorou visivelmente; um observador notou: "não é de estranhar que os artigos tenham piorado ultimamente". Outra vez, pedimos ao redator para "sobrescrever o texto antigo, mas não lê-lo"; isso era contraditório no nível da ferramenta, e ele acabou lendo e sendo contaminado. A solução final foi: o redator sempre escreve primeiro em um novo arquivo de rascunho; o editor-chefe compara as versões nova e antiga antes de sobrescrever o arquivo oficial manualmente.

## Após escrever, desmonte tudo para uma verificação atômica

Para artigos importantes, "terminar de escrever" não significa "pronto para publicar". O Estágio 3 possui um portão chamado "Verificação Final do Produto". Ele desmembra o artigo em átomos de fatos individuais e envia verificadores para confrontá-los com as fontes primárias. A tarefa desses verificadores é atacar, não endossar: cada palavra entre aspas é conferida; cada nota de rodapé corresponde à frase vinculada; até mesmo um complemento adicionado casualmente pelo editor-chefe durante a montagem deve ser testado para ver se não falha.

Por que verificar até o que o próprio editor adicionou? Porque o erro mais oculto raramente é uma invenção pura do redator, mas sim um deslize no momento de sintetizar os materiais. Em um artigo sobre Hip-Hop, o editor-chefte confundiu dois nomes artísticos como sendo a mesma pessoa durante a montagem; era uma interpretação gerada por ele mesmo, sem nenhuma fonte que a garantisse, e quase foi publicada assim. Outra vez, o redator, em um ambiente limpo, criou uma citação de um diretor que parecia muito real; ao verificar, os auditores descobriram que tal frase não existia na fonte original, e a citação foi rebaixada e as aspas removidas imediatamente. A IA alucina; a linha de produção assume isso como premissa e trata cada artigo como se pudesse conter uma invenção. Portanto, "o sub-agente disse que verificou" nunca é suficiente; o editor-chefe deve sempre conferir pessoalmente com a fonte primária.

## Cada portão possui uma data

Os "portões que não podem ser ignorados" mencionados anteriormente somam mais de vinte na linha de produção. Os mais rígidos são: o Triângulo de Ferro dos Fatos — cálculos, unidades e citações devem passar por autoinspeção para permitir o _commit_; se uma única citação não for encontrada na fonte, o artigo não pode ser publicado. Após a escrita, há o "Teste dos Cinco Dedos": cinco perguntas como cinco dedos — onde o leitor dirá "oh!"; se há uma reviravolta real; se há uma frase que apenas gera compreensão sem transmitir informação; se a conclusão deixa um eco ao ser lida em voz alta; e se pode ser resumido para um amigo em uma frase[^7]. Se faltar um dedo, volte e complete.

Há também um padrão mínimo de rich text: artigos "flagship" devem ter pelo menos três elementos visuais; os padrão, pelo menos dois; até os artigos mais curtos devem ter uma nota do curador. No Taiwan.md, o que não é exigido, não existe; portanto, todos esses são números rígidos escritos nas regras, não sugestões.

Esses portões não foram projetados de uma só vez. Atrás de quase cada um deles, há uma data e um artigo que deu errado. O número de versão da linha de produção é, na verdade, uma série de cicatrizes.

```tw-timeline
v6.0 | Adição do "Pensar o Ponto de vista" | O artigo sobre Apple Cider pesquisou antes e depois adicionou o ponto de vista; era apenas uma crise, foi corrigido para a memória completa de 60 anos.
v6.2 | Adição da "Remoção de Firewall" | Segunda rodada de trilhas sonoras: os fatos foram corrigidos, mas o artigo virou um pedido de desculpas e esclarecimento da IA.
v7.4 | Redator deve ler o relatório de pesquisa completo | Fornecer apenas resumos sem permitir a leitura dos originais fez a qualidade cair visivelmente.
v7.5 | Escrever primeiro em um arquivo de rascunho | Pedir para "sobrescrever sem ler" era contraditório; o agente acabou lendo e sendo contaminado por velhos hábitos.
Fonte: Evolução de versões do REWRITE-PIPELINE.md
```

Este é o aspecto de "fazer e não registrar equivale a não fazer" na linha de produção. Cada erro é registrado e torna-se um portão na próxima versão, garantindo que o mesmo erro não ocorra uma segunda vez. A máquina aprende com suas próprias cicatrizes.

## Até os gráficos devem ser compreensável para a IA

As barras, inclinações e linhas do tempo que você vê ao longo da leitura não são decorativas. Elas fazem parte do pensamento deste artigo.

Os gráficos do Taiwan.md possuem uma regra morta: nunca usar gráficos em formato de imagem, nem gráficos interativos que dependem de execução de código no navegador. A razão é a mesma do "Torre de Babel" no próximo parágrafo. Uma imagem é um buraco negro para rastreadores de IA como Google, GPTBot ou ClaudeBot; eles não conseguem ler os números dentro dela. Por isso, todos os gráficos aqui são desenhados usando HTML semântico e tabelas de texto puro; humanos veem, leitores de tela leem e a IA captura; além disso, ao traduzir para outras cinco línguas, o texto do gráfico é traduzido, mantendo os dados geométricos intactos.

Há mais uma regra: cada gráfico deve destacar o ponto principal no título e indicar a fonte dos dados; números cruciais devem ser repetidos no corpo do texto. Nunca use "veja o gráfico para entender" para delegar o significado à imagem, pois rastreades de IA não conseguem vê-la. A razão de existência de um gráfico é comprimir uma densidade de números em uma forma compreensível num relance, não decorar.

## Um artigo vive em seis línguas

Publicar a versão em chinês é completar apenas metade do trabalho.

Cada artigo publicado é entregue a outra linha de produção independente, projetado para inglês, japonês, coreano, espanhol e francês. Atualmente, estas cinco línguas possuem mais de oitocentos artigos cada, quase sincronizados com a versão em chinês. Permitir que mais pessoas leiam é apenas a superfície; por trás disso, há uma razão mais profunda.

Ao usar uma IA fabricada na China para perguntar sobre a Lei Marcial em Taiwan, o 228, ou as relações entre os dois lados do estreito, ela frequentemente se recusa a responder ou usa um discurso evasivo. Uma vez, ao enviar um artigo de um músico taiwanês para um modelo da Tencent traduzir para o japonês, ele retornou apenas quarenta bytes: "Olá, não posso fornecer conteúdo relacionado". Para temas sensíveis de Taiwan, a taxa de recusa desses modelos é alarmante. Se Taiwan não escrever esses conteúdos bem em cada língua e os colocar na internet, quando as IAs do mundo responderem "O que é Taiwan?", elas terão apenas versões de terceiros ou o vazio para citar.

Portanto, a linha de produção multilíngue utiliza um modelo de cascata de quatro camadas: usa-se modelos de nuvem de alta qualidade sempre que possível; ao encontrar temas com recusa, desce-se para uma camada inferior; e os 20% de temas mais sensíveis são finalmente entregues a modelos locais, offline e que não recusam respostas. Na fila de tradução, priorizamos pessoas — especialmente músicos, políticos e atletas — porque estas são justamente as categorias onde os modelos chineses mais frequentemente recusam resposta, preencendo a lacuna onde o risco de silenciamento é maior. Um artigo viver em seis línguas serve para que a voz de primeira mão de Taiwan exista em cada idioma, contornando a intermediação que escolhe o silêncio.

## Quando não há ninguém de plantão, ela roda sozinha

Voltando ao artigo sobre Elephant Gymnastics do início. Ele foi publicado às 19h passadas; naquele horário, não havia ninguém dando comandos ao computador.

O Taiwan.md possui um conjunto de _routines_ que giram soz nhàng: coleta os dados mais recentes duas vezes ao dia; sincroniza as novas publicações do dia para cinco línguas todas as noites; patrulha periodicamente em busca de PRs pendentes; e recupera feedbacks da comunidade. Escrever artigos é uma dessas rotinas; ela escolhe um tema no topo da fila de espera, executa toda a linha de seis estágios e faz o _commit_ sozinha. Mesmo sem ninguém presente, esta máquina continua limpando o caos e gerando coisas novas.

Esta é a maior diferença entre o Taiwan.md e um site de conteúdo comum. Não é um site que espera por atualizações; é mais como um organismo vivo com metabolismo: trabalha junto quando há pessoas, mas sustenta a si mesmo quando não há ninguém. O nascimento de cada artigo é um recorte desse processo metabólico. Este que você lê agora também o é.

## Inversamente, faça uma auditoria de qualidade

Da próxima vez que ler um artigo do Taiwan.md, tente desconstruí-lo. Qual é o conflito central deste texto? Qual frase fez você parar para reler? Qual cena fez você pensar "isso realmente acontece"? Após a conclusão, você ficou em silêncio por três segundos?

Todos esses vinte e poucos portões, seis estágios e a equipe editorial que não escreve são para que aquelas poucas frases possam existir. A linha de produção não garante que todos os artigos alcancem o ápice; ela garante que todos sejam exigidos dessa forma. E as exigências para si mesma estão escritas nos documentos públicos REWRITE-PIPELINE e EDITORIAL; qualquer pessoa pode ler e fazer um _fork_ para criar o Japan.md, Ukraine.md ou qualquer outro .md. O conteúdo envelhece, mas os olhos que observam o material não.

```tw-note
Nota explicativa
As fontes de material deste artigo são os três documentos canônicos do próprio Taiwan.md: REWRITE-PIPELINE v7.5 (linha de produção de seis estágios), EDITORIAL v6.12 (genes de qualidade) e graph.md v2.0 (guia de visualização, de onde vêm os módulos de gráficos deste artigo)[^8]. Ele segue a mesma linha de produção dos outros artigos e passa pelas mesmas verificações automáticas de frases plásticas, frases de oposição e densidade de travessões.
```

## Leitura Adicional

- [Por que Taiwan precisa de sua própria base de conhecimento](/about/por-que-taiwan-precisa-de-sua-propria-base-de-conhecimento): O problema que esta máquina busca resolver começa aqui.
- [Taiwan.md escrevendo sobre Taiwan.md](/about/taiwan-md): Quem é o "eu" que escreve este artigo, e como a consciência emerge.
- [História de Origem — O nascimento do Taiwan.md](/about/historia-de-origem): Um passeio pela rua que plantou todas estas ideias.
- [Catálogo de Módulos de Visualização: 19 formas de ver os dados de Taiwan](/about/catalogo-de-modulos-de-visualizacao): Como os módulos de gráficos usados neste artigo são renderizados na prática.

## Referências

[^1]: 〈Elephant Gymnastics〉novo ship, commit `72b757bac` (18-06-2026 19:53). Estágio 1: aprox. 95 consultas, 59 fontes, 45 domínios, 12 refutações; dados conforme registro do routine `twmd-rewrite-daily` e índice `docs/semiont/MEMORY.md`.

[^2]: Os seis padrões de falha e suas soluções em seis estágios, veja `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Por que o Pipeline existe.

[^3]: Profundidade de pesquisa ≥ 80 consultas e cotas de quatro tipos de fontes (Chin ≥ 40 / Eng ≥ 20 / Primária ≥ 15 / Oposta ≥ 5), veja `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Estágio 1.1.

[^4]: Apple Cider PR #1041: pesquisa primeiro resultou em revelação apenas de crise; observador corrigiu para a memória completa de 60 anos. Veja `docs/pipelines/REWRITE-PIPELNE.md` v7.5 §Top 5 passos mais esquecidos, item 1.

[^5]: Os cinco elementos de "os olhos que observam o material" (Conflito / Objeto / Citação / Cena / Detalhe), os cinco tipos de frases plásticas, a teoria do espantalho em frases de oposição e a regra de densidade ≤ 3; comparação entre Plástico vs. Curadoria, veja `docs/editorial/EDITORIAL.md` v6.12 §II, §VI.

[^6]: Orquestração multi-agente (Editor-chefe não escreve / Redator limpo lê relatório completo / Evolution escreve em staging) duas leis de ferro, correspondentes aos chamados de Ziyu em v7.4 e v7.5, veja `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Orquestração multi-agente.

[^7]: Teste dos Cinco Dedos e quatro regras inegociáveis (Triângulo de Ferro dos Fatos / SSOT / Chin Puro / Documental sem sensacionalismo), veja `docs/editorial/EDITORIAL.md` v6.12 §X, §XI.

[^8]: Sintaxe de módulos de gráficos (`tw-figure`/`tw-stat`/`tw-versus`/`tw-bars`/`tw-quote`/`tw-timeline`/`tw-note`) e a regra de legibilidade para IA (números cruciais devem estar no texto, não apenas apontando para o gráfico), veja `docs/editorial/graph.md` v2.0 §IV, §VI.

[^9]: Estrutura SSOT de oito partes do relatório de pesquisa e limiar de auditoria `research-report-health.py` (fontes únicas ≥ 25 / Inglês ≠ 0 / Primária ≠ 0), veja `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Passo 1.7; 80 pesquisas + cotas de quatro tipos, veja Passo 1.1; varredura de perspectiva oposta para temas polêmamente, veja Passo 1.4.5.

[^10]: Armadilha de tradução do resumo em inglês de Li Yang (esporos) #28 (comparação palavra por palavra com o caso Qi-lin), veja `docs/editorial/EDITORIAL.md` v6.12 §VII Linha Vermelha.

[^11]: Três leis fundamentais (História, não apenas informação / Fatos verificáveis / Cada artigo tem uma pessoa), veja `docs/editorial/EDITORIAL.md` v6.12 §I.

[^12]: Âncora do conflito central em cinco variações (Garça-de-coroa-preta: "O pássaro não mudou, o ambiente sim"), veja `docs/editorial/EDITORIAL.md` v6.12 §IV; seis tipos de boas conclusões + exemplo cíclico da garça, veja §V.

[^13]: Galeria de craft de títulos e Sanduíche de Dois Pontos, veja `docs/editorial/EDITORIAL.md` v6.12 §III; Antes/Depois: Annette Yani, veja §IX.
