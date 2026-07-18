---
title: 'Laboratório de IA de Taiwan (Taiwan AI Labs)'
description: "Instituição de pesquisa em IA sem fins lucrativos fundada por Ethan Tu, o 'pai do PTT', em março de 2017. Modelos de código aberto: TAIDE (modelo de linguagem grande em chinês tradicional), TAME, FedGPT, com mais de 60 bilhões de tokens de corpus em chinês tradicional. Foco em saúde inteligente e prevenção de guerra cognitiva. Aplicativo de distância social COVID (Bluetooth descentralizado)."
date: 2026-03-19
category: 'pt'
tags:
  [
    'IA',
    'Saúde Inteligente',
    'Ethan Tu',
    'Inovação Tecnológica',
    'Prevenção de Guerra de Informação',
    'TAIDE',
    'PTT',
  ]
subcategory: '人工智慧'
author: 'idlccp02'
featured: true
lastVerified: 2026-05-07
lastHumanReview: true
readingTime: 8
translatedFrom: 'Technology/台灣人工智慧實驗室.md'
sourceCommitSha: 'c8e5ac9ea'
sourceContentHash: 'sha256:905a736099878754'
sourceBodyHash: 'sha256:f134440a7453a1a5'
translatedAt: '2026-07-18T18:57:48+08:00'
---

# Laboratório de IA de Taiwan (Taiwan AI Labs)

> **Resumo em 30 segundos:** O Laboratório de IA de Taiwan foi fundado por Ethan Tu, o "pai do PTT", em março de 2017, sendo a primeira instituição de pesquisa em IA sem fins lucrativos da Ásia. [^1] Perfil de Ethan Tu: em 1995, no segundo ano da faculdade, criou o PTT em seu dormitório usando um computador 486; em 2006, ingressou na Microsoft; em 2012, entrou no departamento de IA da Microsoft (a descrição exata do cargo na região da Ásia-Pacífico apresenta divergências, ver P0⚠️). [^2] Modelos de linguagem de código aberto: **TAIDE** (modelo de linguagem grande em chinês tradicional), **TAME**, e o **FedGPT** de nível federado, com um corpus de mais de 60 bilhões de tokens em chinês tradicional. [^3] Áreas centrais: saúde inteligente, prevenção de guerra cognitiva, aplicativo de distância social COVID (Bluetooth descentralizado). [^4]

---

## Contexto de fundação e princípios fundamentais

O Taiwan AI Labs foi fundado por Ethan Tu em março de 2017. [^1] Na época, o desenvolvimento global de IA era majoritariamente dominado por grandes gigantes da tecnologia multinacionais. Ethan Tu reconheceu as vantagens únicas de Taiwan em hardware de semicondutores, talentos em software e no banco de dados do Seguro Nacional de Saúde, decidindo retornar ao Taiwan para fundar o laboratório.

O cargo de Ethan Tu: em comunicados de imprensa da TSMC e em algumas mídias, é descrito como "ex-diretor de pesquisa da região Ásia-Pacífico da Microsoft em IA", mas a Wikipedia registra como "departamento de IA da Microsoft". A descrição exata do cargo apresenta divergências (P0⚠️), sendo recomendável consultar o LinkedIn oficial ou os comunicados do site do Taiwan AI Labs. [^2]

Princípios fundamentais: "Tecnologia para o Bem (Tech for Good)" e "Espírito de Código Aberto" — não tendo o lucro comercial como único objetivo, foca nas dores sociais e compartilha os resultados da pesquisa com o setor industrial, governo e academia por meio de código aberto ou cooperação.

---

## Três áreas centrais de pesquisa

### Saúde Inteligente (Smart Healthcare)

Utiliza os dados do Seguro Nacional de Saúde e dados clínicos de Taiwan para desenvolver aplicações de IA médica — como reconhecimento de imagens médicas (tumores cerebrais, lesões pulmonares) e análise de sequenciamento genético por IA.

Para resolver o problema da privacidade dos dados médicos, adota a "Aprendizado Federado (Federated Learning)": os modelos de IA são treinados localmente nos servidores de cada hospital, retornando apenas os parâmetros do modelo, enquanto os dados originais dos pacientes nunca saem do hospital, quebrando os silos de dados entre as instituições de saúde.

### Cidades Inteligentes e Interfaces Homem-Máquina

Inclui sistemas de inspeção por drones, análise de tráfego inteligente e a IA de voz e música "Yating" — capaz de realizar reconhecimento de voz chinês localizado preciso (incluindo mandarim taiwanês e mistura de chinês-inglês), bem como criação musical.

### Prevenção de Guerra de Informação e Cognitiva

O Taiwan é considerado uma das regiões mais afetadas por ataques de desinformação no mundo. O projeto "Infodemic" utiliza IA para analisar comportamentos coordenados inautênticos (Coordinated Inauthentic Behavior) nas redes sociais, publicando regularmente relatórios de observação do ambiente de informação.

---

## Modelos de linguagem de código aberto: TAIDE, TAME, FedGPT

O Taiwan AI Labs lançou três modelos relacionados ao chinês tradicional de código aberto [^3]: **TAIDE** (Trustworthy AI Dialogue Engine) é um modelo de linguagem grande em chinês tradicional, com mais de 60 bilhões de tokens de corpus em chinês tradicional treinados; **TAME** é outro modelo de código aberto, cujos usos detalhados podem ser vistos na documentação oficial; **FedGPT** é um modelo de linguagem de nível de aprendizado federado, enfatizando a arquitetura de privacidade de dados. As três modelos respondem conjuntamente à questão estrutural de que o corpus em chinês tradicional representa uma proporção extremamente baixa nos dados de treinamento de IA global, dificultando a evitação da premissa de visão de chinês simplificado.

---

## Prática de prevenção de pandemias COVID-19

Durante a pandemia a partir de 2020, o Taiwan AI Labs colaborou com o governo para lançar o "Aplicativo de Distância Social de Taiwan": utiliza tecnologia Bluetooth descentralizada, não coleta localização GPS pessoal, auxiliando na investigação epidemiológica sob a garantia da privacidade, tornando-se um modelo internacional de prevenção de pandemias por tecnologia [^4]. Este produto também é um caso concreto da rota de pesquisa "aprendizado federado" e "privacidade em primeiro lugar", transformando a ideia em uma implementação pública em larga escala.

---

## Leituras adicionais

- [Miin: Ethan Tu ensina IA a identificar contas que puxam o vento, mas ele próprio é processado por roubo de notícias](/technology/迷音Miin) — O produto principal do laboratório voltado ao público geral, que usa IA para identificar contas de operações coordenadas, entrou em processo judicial por direitos autorais devido a notícias agregadas no final de 2025.
- [Desenvolvimento e Estratégia Futura da IA em Taiwan: de 2024 com dois Prêmios Nobel ao Mercado Noturno de Ningxia](/technology/台灣人工智慧發展與未來策略) — Coloca o Taiwan AI Labs de volta ao tabuleiro geral de hegemonia de hardware + dois Prêmios Nobel de 2024, observando a distância entre o TAIDE e a pesquisa básica global de IA.
- [Por que Taiwan precisa de seu próprio banco de conhecimento](/about/為什麼台灣需要自己的知識庫) — A outra face da construção de capacidades de IA pela sociedade civil: a lacuna de corpus para alimentar os modelos, e como a recusa de resposta da IA sobre temas de Taiwan pode ser quantificada.
- [Site oficial do Taiwan AI Labs](https://ailabs.tw/)
- [Ethan Tu — Wikipedia](https://zh.wikipedia.org/zh-tw/杜奕瑾)
- [BNext: Ethan Tu retorna ao Taiwan para fundar o Laboratório de IA](https://www.bnext.com.tw/article/44267/founder-of-ptt-ethan-tu-back-to-taiwan-to-establish-an-ai-lab)
- [Centro de Pesquisa do Ambiente de Informação de Taiwan do IORG](https://iorg.tw/)

---

## Referências

[^1]: [Taiwan AI Labs: Sobre nós](https://ailabs.tw/zh/關於我們/) — Confirma a fundação por Ethan Tu em março de 2017 e a posição de primeira instituição de pesquisa em IA sem fins lucrativos da Ásia.

[^2]: [Wikipedia: Ethan Tu](https://zh.wikipedia.org/zh-tw/杜奕瑾) — Confirma que em 1995, no segundo ano da faculdade, criou o PTT em seu dormitório usando um computador 486; ingressou na Microsoft em 2006; entrou no departamento de IA da Microsoft em 2012 (a descrição exata do cargo "diretor de pesquisa da região Ásia-Pacífico" apresenta divergências P0⚠️).

[^3]: [Verse: Entrevista com Ethan Tu (TAIDE/TAME/FedGPT)](https://www.verse.com.tw/article/my-way-ethan-tu) — Confirma os nomes dos modelos de código aberto TAIDE/TAME/FedGPT; o corpus do TAIDE tem mais de 60 bilhões de tokens em chinês tradicional.

[^4]: [Ministério da Saúde e Bem-Estar, CDC: Descrição do Aplicativo de Distância Social de Taiwan](https://www.cdc.gov.tw/) — Confirma que o aplicativo de distância social COVID utiliza tecnologia Bluetooth descentralizada e não coleta localização GPS.

[^5]: [BNext: Ethan Tu retorna ao Taiwan para fundar o Laboratório de IA](https://www.bnext.com.tw/article/44267/founder-of-ptt-ethan-tu-back-to-taiwan-to-establish-an-ai-lab) — Reportagem sobre o contexto e motivação de Ethan Tu retornar ao Taiwan para fundar o Taiwan AI Labs.

---

_Este artigo foi escrito pelo contribuidor da comunidade @idlccp02, atualizado em 2026-05-07 para incluir os resultados da verificação de fatos P0 (TAIDE/TAME/FedGPT/60 bilhões de tokens; hedge sobre o cargo de Ethan Tu na Microsoft)._
