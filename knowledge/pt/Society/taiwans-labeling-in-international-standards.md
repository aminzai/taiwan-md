---
title: 'O problema da sinalização de Taiwan nos padrões internacionais'
description: 'Dos códigos ISO ao software livre — como o nome de Taiwan é escrito, contestado e corrigido na infraestrutura digital global'
date: 2026-03-18
category: 'Society'
tags:
  [
    'ISO 3166',
    'padrões internacionais',
    'software livre',
    'g0v',
    'soberania digital',
    'sinalização de Taiwan',
  ]
subcategory: '國際關係'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-03-19
lastHumanReview: false
translatedFrom: 'Society/台灣在國際標準中的標示問題.md'
sourceCommitSha: '18157ab5d'
sourceContentHash: 'sha256:474db7988470495f'
sourceBodyHash: 'sha256:288ae1e41983889d'
translatedAt: '2026-07-26T17:01:26+08:00'
---

# O problema da sinalização de Taiwan nos padrões internacionais

> **Resumo em 30 segundos:** Na infraestrutura digital global, Taiwan costuma ser sinalizado como «Taiwan, Província da China». Esta sinalização tem origem no cenário político internacional posterior à Resolução 2758 da Assembleia Geral das Nações Unidas, de 1971, influenciou padrões internacionais como a ISO 3166 e estendeu-se a software livre e serviços de rede em todo o mundo. Comunidades de código aberto continuam a pressionar por sinalizações mais neutras através de relatórios de erro e _pull requests_.

Na infraestrutura digital global, a forma como Taiwan é sinalizado reflete uma divergência política internacional que dura mais de meio século. Da ISO 3166 à interface de escolha de espelhos do Ubuntu, por trás de um detalhe técnico está a disputa inacabada sobre a identidade de Taiwan no sistema internacional.

## Contexto histórico: da UN 2758 à ISO 3166

Em 1971, a Assembleia Geral das Nações Unidas aprovou a Resolução 2758, decidindo que «o assento da China nas Nações Unidas» seria representado pela República Popular da China, fazendo com que a República da China perdesse o seu assento na ONU. Esta resolução originalmente só envolvia o assento de representação na ONU, mas passou a ser amplamente invocada como base para a exclusão de Taiwan ou a sua sinalização de forma específica em vários tipos de organizações internacionais e organismos de normalização.[^1]

Em 1974, o nome do verbete de Taiwan no padrão internacional ISO 3166 foi alterado de «Taiwan» para «Taiwan, Província da China», formalizando a forma de sinalização que vigora até hoje. A ISO 3166-1 atribuiu simultaneamente a Taiwan o código de duas letras `TW`, mas a controvérsia sobre o nome oficial persiste sem solução.

A posição da ISO é seguir a base de dados de nomes geográficos da Divisão de Estatística das Nações Unidas (UNSD), cuja sinalização, por sua vez, remonta ao cenário político posterior à UN 2758. Formou-se assim um sistema de interdependência mútua: padrões internacionais citam dados da ONU, software livre cita padrões internacionais, e finalmente «Taiwan, Província da China» aparece nos menus suspensos de programadores em todo o mundo.[^2]

## Ações de correção da comunidade de software livre

O Bug #1138121 do Ubuntu (reportado em 2013) é um dos casos mais citados. Quando utilizadores de Taiwan escolhiam espelhos de fontes de software, viam «Taiwan, Província da China» na interface, o que causava desconforto a muitos. O relator sugeriu adotar o campo _common name_ da ISO 3166, ou seja, simplesmente «Taiwan», em vez do nome oficial completo.

Problemas semelhantes surgiram repetidamente noutros projetos de código aberto. A Issue #43 do ISO-3166-Countries-with-Regional-Codes, o PR 138672 do FreeBSD, a Issue #1938892 do Drupal registam todos a objeção da comunidade a esta sinalização. A solução costuma ser passar a usar dados do CLDR (Unicode Common Locale Data Repository), cuja sinalização para Taiwan é mais neutra.[^3]

As ações de correção da comunidade de código aberto refletem o encontro entre técnica e política: programadores geralmente preferem sinalizações mais neutras, mas limitados pela consideração de «seguir padrões internacionais», as alterações costumam exigir longas discussões comunitárias, e parte dos mantenedores opta por evitar o tema. Membros da comunidade g0v, como chewei, compilam há muito tempo os casos relacionados, documentando a amplitude do problema da sinalização de Taiwan no ecossistema global de software.

## Impacto mais amplo da nomeação

Em ocasiões formais de organizações internacionais, o problema da nomeação de Taiwan tem alcance mais vasto. Na Assembleia Mundial da Saúde (WHA), Taiwan participou como observador sob a designação «Taipé Chinesa» entre 2009 e 2016 (oito sessões); a partir de 2017, a China opôs-se à continuação da participação de Taiwan, os convites cessaram e Taiwan nunca mais recebeu convite formal.[^6] Na Organização da Aviação Civil Internacional (ICAO), Taiwan também não consegue participar na tomada de decisões como membro efetivo, dependendo há muito de canais informais para obter informações sobre normas técnicas de aviação, criando uma lacuna potencial na circulação de informação de segurança aérea. Nos Jogos Olímpicos, Taiwan participa desde 1981 sob o nome «Taipé Chinesa» — este nome provém do Acordo de Lausana assinado em 1981 entre o COI e o Comité Olímpico Chinês. Esta solução de compromisso também é adotada por muitas organizações internacionais não governamentais e estendida a ocasiões como a APEC.

O problema da nomeação ganhou novas extensões na era digital. Além da ISO 3166, códigos bancários SWIFT, códigos de aeroportos da ICAO, bases de dados geográficas de vários governos, todos têm formas diferentes de sinalizar Taiwan, sem padrão unificado.

Desde 2023, algumas empresas tecnológicas internacionais (como Apple, Google Maps), após relatos de utilizadores, ajustaram sucessivamente o nome de exibição de Taiwan, mas a sinalização oficial da ISO 3166-1 em si não mudou, mostrando que o descolamento entre a implementação empresarial e o padrão internacional continua a alargar-se.

## Alteração da capa do passaporte em 2020

**Em 2 de setembro de 2020**, o Ministério dos Negócios Estrangeiros da República da China divulgou o novo desenho do passaporte: a inscrição «REPUBLIC OF CHINA» na capa foi visivelmente reduzida (mantendo-se o brasão nacional), enquanto «TAIWAN» foi amplamente aumentado, ficando lado a lado com «REPUBLIC OF CHINA». Esta alteração respondeu a incidentes durante a pandemia de COVID-19 em que viajantes de Taiwan foram confundidos com cidadãos chineses e impedidos de entrar em vários países, sendo a primeira vez que o governo de Taiwan usa o desenho do passaporte para responder concretamente ao problema da «confusão na sinalização de soberania». O novo passaporte começou a ser emitido em **janeiro de 2021**.[^4]

## Controvérsia sobre Taipé Chinesa nos Jogos Olímpicos de Paris 2024

**Durante os Jogos Olímpicos de Paris, em julho-agosto de 2024**, Taiwan participou sob o nome «Taipé Chinesa», mas setores da sociedade chinesa traduziram esse nome como «China Taipei» (中國台北) em várias plataformas sociais, divergindo claramente da tradução chinesa oficial do COI, «Taipé Chinesa» (中華台北). Incidentes como a apreensão de bandeiras de atletas de Taiwan por espectadores chineses e a interferência de chefes de delegação chineses em grupos de apoio da diáspora taiwanesa reacenderam em Taiwan a reflexão sobre o Acordo de Lausana de 1981.[^5]

## Casos de pressão de empresas multinacionais

A extensão da pressão chinesa baseada no «princípio de uma só China» expandiu-se fortemente para o domínio das empresas multinacionais a partir do final da década de 2010. A **China Airlines** (華航) usa há muito o nome «China Airlines» em rotas internacionais, gerando controvérsia interna sobre a identidade nacional de Taiwan (petição «Renomear a China Airlines» em 2018). **Delta Air Lines**, **Marriott Hotels**, **United Airlines**, **Zara**, **Starbucks**, **Marriott** e outras empresas foram pressionadas pela Administração de Aviação Civil da China ou pelo Gabinete de Informação da Internet da China por listarem «Taiwan» como país nos seus sites, sendo forçadas a alterar para «Taiwan da China» ou «Região de Taiwan da China». Estes casos mostram que o «efeito político dos padrões ISO» se expandiu do domínio técnico para ferramenta de pressão geopolítica.

## Perspetiva: a posição da China

Do ponto de vista oficial da República Popular da China, o «princípio de uma só China» é a base política das relações entre os dois lados do estreito, defendendo que a República Popular da China é o único governo legítimo que representa a China inteira e que Taiwan é uma província da República Popular da China (nível administrativo de «província de Taiwan»). Esta posição influenciou diretamente a sinalização «Taiwan, Província da China» na ISO 3166 a partir de 1974. Compreender o problema de Taiwan nos padrões internacionais exige ver simultaneamente a posição de oposição do governo da República da China, a reivindicação da República Popular da China e o espetro plural de identificações da sociedade taiwanesa — estes três elementos não coincidem, nem são redutíveis uns aos outros.

## A torre de Babel da soberania: _sovereignty preservation_

O problema da sinalização de Taiwan nos padrões internacionais é, em essência, um problema de **infraestrutura de preservação da soberania** (_sovereignty preservation infrastructure_). Fazer com que a _first-person voice_ de Taiwan exista em cada língua, em cada sistema, em cada base de dados, é a forma de manter Taiwan, como sujeito político independente, continuando a ser visto na era da informação. Cada relatório de erro, cada _pull request_, cada atualização do desenho do passaporte, são um tijolo desta infraestrutura.

## Referências

[^1]: [Resolução 2758 da Assembleia Geral das Nações Unidas (1971)](<https://undocs.org/zh/A/RES/2758(XXVI)>) — Texto integral da resolução que decide que o assento de representação da China na ONU é exercido pela República Popular da China.

[^2]: [ISO 3166 Maintenance Agency — Online Browsing Platform](https://www.iso.org/obp/ui/#iso:code:3166:TW) — Verbete de Taiwan na ISO 3166-1, contendo o código TW e o nome oficial.

[^3]: [Ubuntu Launchpad — Bug #1138121](https://bugs.launchpad.net/ubuntu/+source/software-properties/+bug/1138121) — Relatório original do problema de sinalização de Taiwan na interface de fontes de software do Ubuntu, 2013.

[^4]: [Ministério dos Negócios Estrangeiros da República da China — Explicação do novo passaporte](https://www.mofa.gov.tw/) — Divulgação do novo desenho do passaporte em 2 de setembro de 2020, ampliação da inscrição TAIWAN, emissão a partir de janeiro de 2021.

[^5]: [Comité Olímpico Internacional — Acordo do Comité Olímpico de Taipé Chinesa](https://www.olympic.org/) — Acordo de Lausana de 1981 estabelece o nome «Taipé Chinesa»; controvérsia nos Jogos de Paris 2024 pela tradução chinesa «China Taipei».

[^6]: [Ministério da Saúde e Bem-Estar da República da China — Explicação sobre a participação de Taiwan na OMS](https://www.mohw.gov.tw/) — Taiwan participou na WHA como observador de 2009 a 2016, sem convites desde 2017; contexto da exclusão da ICAO ver explicações do Ministério dos Negócios Estrangeiros.

## Leitura complementar

- [Comunidade g0v — Compilação do problema da sinalização de Taiwan](https://g0v.hackmd.io/5YRoMhveTt-aXwH60T2NZg) — Base de dados de casos de sinalização de Taiwan em software livre compilada por chewei
- [Plataforma de consulta online da ISO 3166](https://www.iso.org/obp/ui/#iso:code:3166:TW) — Consulta da sinalização atual de Taiwan na ISO 3166-1
