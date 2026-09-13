---
title: 'Pagamento móvel em Taiwan: por que o telefone tem vários apps de pagamento e ainda assim se carrega dinheiro em espécie?'
description: 'No terceiro trimestre de 2024, 92% dos 5.000 entrevistados pela MIC já usaram pagamento móvel e 84% usam com frequência. Uma pesquisa nacional encomendada pelo Banco Central mostra, porém, que 73,8% ainda combinam espécie e não-espécie. Analisando consumidores, comerciantes e o QR comum do TWQR, este texto desmonta as diferentes ferramentas, contratos e fluxos de confirmação por trás do pagamento com o celular, responde por que a alta adesão ainda enfrenta dois obstáculos para viver sem dinheiro e explica o que o QR comum já resolveu — e o que ainda não.'
date: 2026-09-01
category: 'Technology'
tags:
  [
    'pagamento móvel',
    'pagamento eletrônico',
    'TWQR',
    'Taiwan Pay',
    'QR Code',
    'dinheiro em espécie',
    'fintech',
  ]
subcategory: '數位與網路'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-09-01
lastHumanReview: false
researchReport: 'reports/research/2026-09/台灣行動支付.md'
image: '/article-images/technology/taiwan-mobile-payments-merchant-2026.webp'
imageCredit: '財金資訊股份有限公司（TWQR 官方網站）'
imageLicense: 'Fair use editorial commentary'
imageSource: 'https://www.twqr.com.tw/'
translatedFrom: 'Technology/台灣行動支付.md'
sourceCommitSha: '574b1a339'
sourceContentHash: 'sha256:1e2fca6dab4c2f1c'
sourceBodyHash: 'sha256:62d9c6127e29bebe'
translatedAt: '2026-09-13T00:44:04+08:00'
---

# Pagamento móvel em Taiwan: por que o telefone tem vários apps de pagamento e ainda assim se carrega dinheiro em espécie?

![Miniatura da entrevista oficial de comerciantes do TWQR com lojistas e letreiro de pagamento móvel](/article-images/technology/taiwan-mobile-payments-merchant-2026.webp)
_Minaitura da entrevista oficial de comerciantes do TWQR, usada apenas para análise de material institucional. A imagem representa apenas a loja entrevistada e não pode ser considerada evidência de campo independente da adoção por lojas em toda Taiwan. Imagem: FinTech Info Corp. (site oficial do TWQR), uso justo em comentário editorial._

> **Resumo de 30 segundos:** Na amostra online da MIC no terceiro trimestre de 2024, 92% já usaram pagamento móvel. Uma pesquisa encomendada pelo Banco Central mostra que 73,8% dos adultos ainda usam espécie e não-espécie juntos. Apesar de diferentes populações e perguntas, ambos apontam para o mesmo fato: usar o celular para pagar, conseguir fazer isso em qualquer lugar e confiar em deixar a última cédula em casa são três barreiras distintas. Às vezes, ter vários apps ajuda a cobrir lacunas nas linhas de distribuição; outras, para recuperar cashback e funcionalidades de fidelidade. O TWQR está integrando o QR comum, mas ainda não unificou todas as fontes de fundos, contratos comerciais e cenários de falha em um único meio de pagamento.

Em setembro de 2025, o analista sênior da MIC, Wu Tzu-li, divulgou uma pesquisa sobre comportamento do consumidor em pagamentos móveis. Ele observou que os usuários ativos instalam mais de cinco ferramentas, "principalmente para poder usar pagamento móvel em diferentes canais".[^1] Essa frase soa familiar a muitos que já fizeram isso na frente do caixa: primeiro olham para os adesivos na porta de vidro ou no balcão, depois decidem qual app abrir. Se não reconhecem nenhum ícone conhecido, levantam e perguntam: "Aceita qual aqui?"

O celular tem opções cada vez mais numerosas, mas o bolso ainda carrega algumas cédulas. Essa coexistência costuma ser lida de duas formas: como um mercado de pagamentos fragmentado em Taiwan, ou como uma escolha simples de benefícios. Ambas capturam parte da realidade. A fricção entre aceitação e interoperabilidade realmente leva as pessoas a instalar mais ferramentas e manter espécie; mas fatores como cashback, fidelidade, transferências, hábitos, preferências pessoais e backup em caso de falha também entram em jogo. Para entender isso, é preciso separar três barreiras: adoção pelo usuário, validade entre diferentes cenários e capacidade de recuperação quando algo dá errado — até que o último usuário se sinta seguro para deixar a última cédula em casa.

## O celular pode pagar, mas isso não significa que levar só ele seja o suficiente hoje

Os 92% de "já usaram" e 84% de "usam com frequência" vêm de uma amostra online de 5.000 respostas, coletada no terceiro trimestre de 2024. Como a página pública não lista integralmente a moldura de amostragem, faixa etária e método de ponderação, essas porcentagens só descrevem a amostra online, não podendo ser estendidas diretamente à população total de Taiwan.[^2] Mesmo com essa ressalva, o dado mostra que, entre os respondentes, o pagamento com o celular já ultrapassou a fase de tecnologia desconhecida.

Outra pesquisa, encomendada pelo Banco Central e realizada pelo Instituto de Estudos Econômicos de Taiwan, perguntou como pessoas de 18 anos ou mais usam espécie e não-espécie no dia a dia. A coleta foi feita principalmente por telefone fixo e celular, com apoio online, abrangendo 22 cidades e regiões, ponderada segundo a estrutura populacional, com 4.234 respostas válidas. O resultado: 73,8% usam espécie e não-espécie ao mesmo tempo, 25% usam só espécie e apenas 1,2% usam só não-espécie.[^3] A categoria "não-espécie" inclui cartões de crédito, cartões financeiros e cartões recarregáveis, então não reflete diretamente a participação de mercado do pagamento móvel, mas é útil para desenhar o perfil atual do bolso.

```tw-waffle
Coexistência é a rotina da maioria (% )
Usa espécie e não-espécie | 73.8
Só usa espécie | 25
Só usa não-espécie | 1.2
Fonte: Pesquisa encomendada pelo Banco Central sobre instrumentos de pagamento, divulgada em 2024
```

Portanto, nada de estranho em alguém pagar com o celular no café da manhã, usar código QR para acumular pontos no almoço e, ao final do dia, pagar com espécie no mercado. Ele já passou da primeira barreira — "as pessoas usam" — mas ainda precisa trocar de ferramenta conforme o local, o comerciante e o equipamento. A frase do título "ainda carrega espécie" só pode ser lida como um backup em escala, não como uma necessidade diária de cada pessoa em Taiwan.

Os hábitos de pagamento já mudaram, mas exceções ainda existem por aí. Ter vários apps parece resolver essas exceções, mas para entender por que eles funcionam, primeiro precisamos reconhecer que não são todos iguais. Abrir o celular parece o mesmo, mas o caminho que a transação segue depois pode ser completamente diferente.

## Vários apps parecem pagar, mas cada um segue um caminho diferente

O material didático da CMTF classifica os meios de pagamento móvel por ferramenta vinculada, tecnologia e regulamentação aplicável: cartão de crédito móvel, cartão financeiro móvel, pagamento por código QR, instituições de pagamento eletrônico e bilhete eletrônico.[^4]

O que o consumidor faz na frente — passar, escanear, confirmar — pode ser executado por ferramentas, tecnologias, endpoints de cobrança e regras diferentes. Pagar com o celular pode usar um cartão vinculado ou uma conta digital. O endpoint de cobrança e a especificação adotados pelo comerciante determinam quais combinações são viáveis. LINE Pay, E.Sun, Apple Pay, AllPay e Taiwan Pay não podem ser apenas listados como cinco carteiras idênticas por causa do logotipo. Alguns competem entre si, outros colaboram na mesma transação, e alguns se substituem em canais diferentes.

Para entender como PChome, Shopee e Coolpad mudam o cenário das compras online, veja [Ecosistema de comércio eletrônico e pagamento digital de Taiwan](/pt/technology/e-commerce-and-digital-payment-ecosystem). Este texto se limita ao último quilômetro do caixa físico.

Assim, ter um app específico no celular responde apenas se o usuário tem a ferramenta. Não responde se o comerciante possui o endpoint compatível. Ver o mesmo código QR não significa que todos os apps, direções de escaneamento e fontes de fundo funcionam. Ir direto do ícone no celular para "disponível em toda Taiwan" pula pelo menos três etapas: ferramenta vinculada, contrato comercial e especificações de transação.

A quantidade de apps também exagera no "cinco em média". A amostra online da MIC de 2024 mostra que 86% usam cinco ou menos, sendo 61% usando menos de três e 14% usando seis ou mais. Os dados públicos não trazem média nem mediana, nem distribuição completa de um a cinco.[^5] O dado confirma que é possível usar vários, mas não define um "usuário típico" com exatamente cinco.

O balanço mensal da CMTF de junho de 2026 soma 41.128,87 milhões de contas de pagamento eletrônico registradas. Mas isso é o total por instituição, não o número único de pessoas. Reflete um instantâneo de contratos, não o número de apps que um usuário típico tem.[^6]

> **📝 Nota do editor**
> Os logotipos no balcão são marcas, os ícones no celular são interfaces, e o que a CMTF acumula são contratos de contas ainda não encerrados. Chamar tudo isso de "usuários" achata o nível mais interessante do mercado de pagamentos.

Apesar de parecerem iguais à primeira vista, as diferenças aparecem quando a transação chega ao outro lado. Baixar quantos apps o usuário quiser não completa o processo de inscrição, verificação e reconciliação para o comerciante. A segunda barreira está atrás do balcão.

## O que o consumidor vê é um escaneio; o comerciante precisa conectar toda a cadeia

Para aceitar Taiwan Pay, um comerciante precisa solicitar ao emissor um contrato de adquirente, obter código de adquirente, código de comerciante e código de terminal, e concluir o registro do serviço.[^7] Depois de começar a receber pagamentos, o equipamento e a rede precisam funcionar, os funcionários precisam saber como confirmar notificações e tratar devoluções, e o sistema interno precisa fazer a conciliação e o repasse. Para lojas pequenas, colocar o código de pagamento é só o começo: depois vem uma cadeia operacional que precisa ser fechada todos os dias.

A FAQ oficial de Taiwan Pay descreve com precisão o momento mais fácil de esconder atrás de um código QR: quando o dispositivo está offline, o comerciante ainda pode gerar um código QR sem valor na tela de login, mas o celular dele não recebe a notificação da transação.[^8] A tela do cliente mostra pagamento concluído, mas o endpoint fica sem confirmação imediata, e o balcão precisa decidir se libera o produto, onde consultar a transação. Escanear é só o início; a confirmação no momento e a reconciliação depois são o que tornam a transação real.

A taxa de Taiwan Pay depende do contrato entre o comerciante e o emissor. A explicação oficial diz: "A taxa de processamento de transações é definida pelo contrato entre o comerciante (recebedor) e o emissor (banco)". Outras plataformas têm condições públicas, negociação para redes chainadas e fontes de pagamento distintas.[^9] A taxa entra na decisão do comerciante, assim como prazo de repasse, devolução, conectividade, equipamento, perfil de clientes, aprendizado e conciliação.

Pesquisa acadêmica com lojas comerciais em Tainan chegou à conclusão de que a percepção de utilidade, facilidade de uso, adoção pelo consumidor e compatibilidade estão positivamente correlacionadas com a intenção de adoção, enquanto a percepção de custo não mostrou relação significativa na amostra.[^10] Isso indica que o comerciante não apenas avalia custos: também considera se a ferramenta é prática e se os clientes já a usam. Essa pesquisa local não pode ser generalizada para todo Taiwan, mas impede a explicação simplista de que "o comerciante não aceita só por causa da taxa".

A pesquisa encomendada pelo Banco Central dá escala a essa diferença de aceitação. De 611 vendedores ambulantes, 76,1% aceitam só espécie. Entre 1.436 lojas, a proporção cai para 46,8%. O relatório atribui a maior proporção entre vendedores ambulantes ao local, equipamento e escala.[^11] Aqui, "aceitar só espécie" é em contraste com todas as ferramentas não-espécie, então não pode ser interpretado como taxa de adoção de pagamento móvel, nem usado para criticar a falta de iniciativa dos vendedores.

```tw-bars
Vendedores ambulantes e lojas têm critérios de aceitação diferentes (% que aceitam só espécie)
Vendedores ambulantes | 76.1 | 611 unidades
Lojas | 46.8 | 1.436 unidades
Fonte: Pesquisa encomendada pelo Banco Central sobre instrumentos de pagamento, divulgada em 2024
```

A universalidade do pagamento só existe quando os dois lados completam: o consumidor tem a ferramenta e o comerciante tem um fluxo contínuo de recebimento, confirmação, devolução e reconciliação. A fricção institucional já tem forma definida, mas só explica parte da coexistência entre apps e espécie. Às vezes, o próximo app é um backup; outras, parece uma extensão de fidelidade.

## Instalar mais um app, às vezes para funcionar, às vezes só para melhorar

Quando o Banco Central perguntou sobre dificuldades no uso de pagamento móvel, 18,9% apontaram "o comerciante não aceita", 12,0% "o comerciante não aceita o app que uso", e apenas 7,6% "tem muitos tipos no mercado". Sinal de rede fraco representa 6,5%, bateria do celular 3,4%.[^12] Como são respostas múltiplas, não podem ser lidas como proporções causais de por que o espécie ainda é usado, mas mostram claramente a lacuna entre "ter um app" e "o app que tenho funcionar".

O "diferentes canais" mencionado por Wu Tzu-li corresponde exatamente a essa motivação de substituição. Se uma loja não aceita o app que o usuário usa, ele pode instalar outro. Se precisar dividir contas em um jantar com amigos ou transferir pontos para familiares, pode manter outro app. Uma série de pesquisas da MIC mostra que 57% dos usuários usaram serviços financeiros além de pagar, sendo os mais comuns transferir e enviar pontos, com 38%.[^13] Essas funções levam o app de pagamento para a vida social e de fidelidade: a razão para ter o app já vai além de "o caixa escaneia".

Um estudo comissionado pela Visa em 2022 entrevistou 1.000 pessoas em Taiwan, com idades entre 18 e 55 anos, e encontrou que 40% acompanham regularmente os pontos de consumo e 22% planejam cuidadosamente para maximizar o retorno.[^14] Esses dados não permitem estimar quantas pessoas instalam apps por causa do cashback, mas mostram que parte dos entrevistados acompanha pontos e busca promoções. Ecossistemas de fidelidade de varejo também criam seus próprios apps de pagamento. Para ver como RT-Mart evoluiu de lojas físicas e online para uma plataforma de vida com alta frequência, veja [RT-Mart](/pt/economy/pxmart-supermarket) — sem reescrever a história corporativa e controvérsias aqui.

O ministério da Economia oferece uma visão de longo prazo. Calculando pela proporção do valor pago, a participação de pagamento móvel subiu de 0,6% em 2017 para 11,2% em 2023, enquanto o espécie caiu de 41,1% para 23,0%. A explicação oficial atribui parte dessa mudança ao crescimento de ecossistemas de fidelidade e ferramentas de pagamento desenvolvidas internamente pelos varejistas.[^15] A participação de pagamento móvel cresceu enquanto o espécie caiu. A competição entre marcas também criou escolhas reais. Se considerarmos que ter vários apps é apenas um sintoma de falha institucional, perderíamos essa trajetória de crescimento e a preferência ativa do usuário.

```tw-slope
Participação do valor pago no varejo: pagamento móvel sobe, espécie cai (% )
2017 | 2023
*Pagamento móvel | 0.6 | 11.2
Espécie | 41.1 | 23.0
Fonte: Departamento de Estatística do Ministério da Economia, Pesquisa de Condições de Negócios no Varejo, Restaurantes e Serviços de Alimentação
```

Os apps múltiplos desempenham dois papéis: um complementa lacunas de aceitação e fontes de fundos; o outro carrega descontos, pontos, fidelidade e transferências. A quantidade de apps não mede adoção, universalidade ou distância de viver sem espécie. Com a competição e substituição entrelaçadas, a pergunta passa a ser: até onde a integração chegou?

## TWQR integra o QR comum, mas não transforma todos os pagamentos em um só

O TWQR é uma resposta prática à pergunta: "pagamento móvel com regras e letreiros de comerciantes demais". O padrão de QR comum conecta instituições financeiras e empresas de pagamento eletrônico. Até o final de 2025, dados do Banco Central listam 44 instituições financeiras, 10 empresas de pagamento eletrônico e 678.000 lojas parceiras. Em 2025, foram 146,734 milhões de transações, totalizando 713,6 bilhões de dólares.[^16] "Pagamento por QR em Taiwan realmente não interoperável" já não é verdade.

![Ilustração oficial do sistema TWQR mostrando "um contrato, múltiplos pagamentos"](/article-images/technology/taiwan-mobile-payments-single-contract-2026.webp)
_Ilustração oficial do sistema TWQR "um contrato, múltiplos pagamentos", apresentando o modelo de adesão proposto pela FinTech Info Corp. Trata-se de material institucional, não podendo provar sozinho que todas as lojas parceiras estão ativas, todas as transações são bem-sucedidas ou todas as fontes de pagamento são interoperáveis. Imagem: FinTech Info Corp. (site oficial do TWQR), uso justo em comentário editorial._

O QR comum resolve uma camada importante, mas a página de adquirente publicada pelo banco cooperativo também mostra que limites ainda existem. A lista de "pagamento iniciado pelo usuário" inclui Taiwan Pay, E.Sun, AllPay, iPASS, iPASS Pay e outras 11 ferramentas. A lista de "pagamento iniciado pelo comerciante" é mais curta e limitada à especificação QR Auth. AllPay, EasyCard e iPASS aparecem na lista de pagamento iniciado pelo usuário, mas não na de pagamento iniciado pelo comerciante.[^17] Direção do escaneamento, especificação e participação da instituição mudam as combinações disponíveis, e o comerciante ainda precisa solicitar TWQR ao emissor.

678.000 é o número de lojas parceiras do TWQR, mas os dados públicos do Banco Central não dizem quantas estão ativamente operando, nem a participação de mercado ou a taxa de sucesso no local. O QR comum também não unifica automaticamente fontes de fundos como cartões de crédito ou contas, pontos de fidelidade, cashback, contratos comerciais, taxas ou fluxos de devolução. Ele avança o letreiro e a especificação de transação para um nível comum, mas não elimina as diferenças entre os mundos comerciais de cada app.

> **📝 Nota do editor**
> O maior reconhecimento do TWQR está escondido na palavra "comum": QR comum e mensagens entre instituições já formam uma base em larga escala, mas a ativação diária das lojas, cada fonte de fundos e cada regra de fidelidade ainda dependem de outras camadas. A universalidade está sendo construída camada por camada.

A barreira de interoperabilidade avançou, mas o número de lojas parceiras não significa que todos podem usar em qualquer momento, com qualquer fonte de fundos. Enquanto a integração continua em andamento, o espécie permanece como uma alternativa — e ganha outra justificativa.

## O espécie não prova que o pagamento móvel falhou; normalmente, não precisa nem perguntar se funciona

Para que uma ferramenta seja universal, o usuário precisa ter acesso, o comerciante precisa reconhecer e confirmar, a transação precisa ser concluída, e precisa haver um mecanismo de recuperação previsível quando o celular fica sem bateria, a rede falha ou a notificação não chega. Isso significa que ambas as partes sabem onde procurar, quando tentar novamente e quais caminhos alternativos seguir após uma falha. Também importa se, após a transação, ambas as partes podem acessar o mesmo registro.

Com essa métrica, o pagamento móvel já encurta o processo de fechamento em muitas transações cotidianas, mas ainda não oferece o mesmo caminho para todos os cenários. Na maioria das transações presenciais de baixo valor, o espécie não exige cadastro nem dispositivo, e a entrega e confirmação acontecem ao mesmo tempo. Continua sendo a interface mínima comum. Claro, o espécie também tem custos de troco, segurança e reconciliação — aqui a comparação é sobre aceitação e tolerância a falhas, não sobre custo operacional total.

A pesquisa encomendada pelo Banco Central traz diferenças individuais no papel do espécie: pessoas com 40 anos ou mais e moradoras em áreas remotas tendem a usar mais espécie.[^18] Esses dados mostram uma tendência, não podem ser estendidos a todos os idosos ou moradores de áreas rurais. A pesquisa também não tem dados suficientes para estimar proporções ou representar vozes de menores, pessoas com deficiência, trabalhadores migrantes ou turistas de curta duração. Ferramentas populares podem ser convenientes para alguns, mas não garantem que todos tenham acesso ao mesmo tipo de conta, cartão, celular ou rede.

Usuários intensivos em lojas e redes conhecidas podem, de fato, passar muito tempo sem tocar um papel. Outra pessoa pode manter espécie por hábito, privacidade ou controle de gastos — não necessariamente por ter tido uma transação falhar. A fricção institucional, aceitação comercial, cashback, fidelidade, hábitos, preferências e resiliência a falhas atuam juntas, e os estudos disponíveis não conseguem rankeá-las em uma causa única.

A barreira de adoção pergunta quantas pessoas usam. A barreira de universalidade pergunta se diferentes pessoas e lojas conseguem transacionar em cenários distintos. A barreira de "sem espécie" pergunta se, após uma falha, dá para recuperar. À medida que as duas primeiras barreiras avançam, menos pessoas carregam espécie — mas quando a última cédula sai do bolso depende de até que ponto as exceções já não valem a pena serem cobertas.

A seguir, um cenário hipotético baseado nas limitações de funcionamento offline descritas na FAQ oficial — não um caso real: o celular do comerciante fica offline, e a tela de login ainda mostra um código QR sem valor. O cliente escaneia, mas o comerciante não recebe a notificação. Ambos olham para suas telas, presos entre "pagamento concluído" e "confirmação no local". O cliente guarda o celular e pega uma cédula. A cédula não vence a tecnologia: ela apenas, nesse cenário, ainda não precisa perguntar "aceita qual aqui?".

## Leituras recomendadas

- [Ecosistema de comércio eletrônico e pagamento digital de Taiwan](/pt/technology/e-commerce-and-digital-payment-ecosystem) — Uma retrospectiva sobre as batalhas entre plataformas e logísticas dos últimos vinte anos do e-commerce em Taiwan.
- [Desenvolvimento da fintech em Taiwan](/pt/economy/taiwan-fintech-development) — Colocar os casos de pagamento de volta no contexto de uma década de fintech em Taiwan entre abertura e gestão de riscos.
- [RT-Mart](/pt/economy/pxmart-supermarket) — Ver como RT-Mart evoluiu de lojas físicas e online para uma plataforma de vida com alta frequência.

## Créditos das imagens

- Imagem principal: FinTech Info Corp. (site oficial do TWQR), [fonte original](https://www.twqr.com.tw/), uso justo em comentário editorial. A imagem original é um captura de tela do vídeo oficial "Dizendo o que o dono pensa | Formosa Meats", usada aqui apenas para comentar o material institucional do TWQR.
- Imagens dentro do texto: FinTech Info Corp. (site oficial do TWQR), [fonte original](https://www.twqr.com.tw/), uso justo em comentário editorial. A imagem original é uma ilustração institucional oficial de "um contrato, múltiplos pagamentos".

## Referências

[^1]: [MIC: Pesquisa de consumo de pagamento móvel 2025](https://mic.iii.org.tw/research.aspx?id=730) — Wu Tzu-li explica que usuários ativos instalam mais ferramentas para diferentes canais, e divulga método, taxa de adoção e faixas de quantidade.

[^2]: [MIC: Pesquisa de consumo de pagamento móvel 2025](https://mic.iii.org.tw/research.aspx?id=730) — Dados coletados no terceiro trimestre de 2024, por pesquisa online, com 5.000 respostas válidas. Os 92% de "já usaram" e 84% de "usam com frequência" se aplicam apenas a essa amostra.

[^3]: [Banco Central: Resultados da pesquisa encomendada sobre CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Método, amostra e ponderação da pesquisa, além dos resultados de 73,8% usando espécie e não-espécie, 25% só espécie e 1,2% só não-espécie.

[^4]: [CMTF Inteligência Financeira: Material didático de pagamento móvel](https://moneywise.fsc.gov.tw/uploaddowndoc?file=financeroom%2F202001131202240.pdf&filedisplay=%E6%96%B0%E5%A2%9E%E6%95%99%E6%9D%90PPT-+%E8%A1%8C%E5%8B%95%E6%94%AF%E4%BB%98-%E5%AE%9A%E7%A8%BF.pdf&flag=doc) — Classifica pagamento móvel por ferramenta vinculada, tecnologia e regulamentação: cartão de crédito móvel, cartão financeiro móvel, pagamento por QR, instituições de pagamento eletrônico e bilhete eletrônico.

[^5]: [MIC: Pesquisa de consumo de pagamento móvel 2025](https://mic.iii.org.tw/research.aspx?id=730) — Publica distribuição de 2024 entre cinco ou menos, menos de três e seis ou mais, sem divulgar média ou mediana.

[^6]: [CMTF Banco Central: Informações importantes de contas de pagamento eletrônico de junho de 2026](https://www.fsc.gov.tw/userfiles/file/BB-1156_%E9%9B%BB%E5%AD%90%E6%94%AF%E4%BB%98%E5%B8%B3%E6%88%B6%E9%87%8D%E8%A6%81%E8%B3%87%E8%A8%8A%E6%8F%AD%E9%9C%B2.pdf) — Total acumulado em 41.128.870, definido como número de usuários registrados e com contrato ainda não rescindido por instituição.

[^7]: [Taiwan Mobile Payment: FAQ de operação para comerciantes](https://www.twmp.com.tw/Faq?n=95c7608a1dfc4fa1834f4467d41a32d1) — Explica que o comerciante precisa assinar contrato com o emissor e obter códigos de adquirente, comerciante e terminal.

[^8]: [Taiwan Mobile Payment: FAQ de recebimento para comerciantes](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Explica que, mesmo offline, é possível gerar um código QR sem valor, mas não é possível fazer login ou receber notificações de transação.

[^9]: [Taiwan Mobile Payment: FAQ de recebimento para comerciantes](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — A oficialização afirma que a taxa de processamento é definida pelo contrato entre o comerciante e o banco emissor, não podendo ser generalizada como uma taxa única de mercado.

[^10]: [Universidade Nacional de Ciência e Tecnologia: Estudo sobre adoção de pagamento móvel por lojas comerciais em Tainan](https://researchoutput.ncku.edu.tw/en/studentTheses/what-factors-affect-stores-willingness-to-adopt-mobile-payment-de/) — Resumo de tese de doutorado lista fatores significativos e não significativos na intenção de adoção, limitando a pesquisa ao contexto de lojas em Tainan.

[^11]: [Banco Central: Resultados da pesquisa encomendada sobre CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Amostras de 611 vendedores ambulantes e 1.436 lojas, relacionando a proporção que aceita só espécie com local, equipamento e escala.

[^12]: [Banco Central: Pesquisa sobre instrumentos de pagamento no Relatório de Estabilidade Financeira](https://www.cbc.gov.tw/tw/dl-207586-2f35d674d8a34ee09d1d1c0fd68a6fea.html) — Gráfico mostra opções múltiplas de dificuldades: comerciante não aceita, não aceita o app usado, muitas opções, sinal de rede e bateria do celular.

[^13]: [MIC: Pesquisa de consumo de pagamento móvel 2025](https://mic.iii.org.tw/research.aspx?id=730) — A pesquisa lista serviços financeiros além de pagar, sendo transferir e enviar pontos os tipos mais comuns.

[^14]: [Visa Taiwan: Pesquisa de consumo de carteiras móveis e pagamento eletrônico 2022](https://www.visa.com.tw/about-visa/newsroom/press-releases/nr-tw-230310.html) — Revela 1.000 entrevistados em Taiwan, com idades entre 18 e 55 anos, e proporções que acompanham retorno e planejam promoções.

[^15]: [Departamento de Estatística do Ministério da Economia: Comunicado sobre nova pesquisa de participação de pagamento móvel no varejo (PDF)](https://www.moea.gov.tw/Mns/populace/news/wHandNews_File.ashx?file_id=116845) — Proporções de valor pago em 2017 e 2023, com explicação sobre ecossistemas de fidelidade no varejo, restaurantes e serviços de alimentação.

[^16]: [Banco Central: Relatório anual de 2025](https://www.cbc.gov.tw/tw/dl-225165-b56d9b5e547843a4822acd679cb4868e.html) — Lista instituições participantes, lojas parceiras e volume total de transações e valor de TWQR em 2025.

[^17]: [Banco Cooperativo: Serviços de adquirente TWQR entre instituições](https://www.tcb-bank.com.tw/company-banking/credit-card/special-store/twqr) — Lista instituições disponíveis para pagamento iniciado pelo usuário e pelo comerciante, especificações QR Auth e formas de inscrição para comerciantes, mostrando como a interoperabilidade varia por direção e especificação.

[^18]: [Banco Central: Resultados da pesquisa encomendada sobre CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — O relatório mostra diferenças direcionais por idade e região; este texto não inventa proporções ou vozes específicas para grupos não representados.
