---
title: 'A barra invertida dentro do caractere "gōng" (功): os dois impostos padrão que engenheiros de Taiwan pagam todo dia'
description: 'No Windows 11 com locale zh-TW, o script de status de tradução jogou todos os mais de quatro mil caminhos escaneados em "root", zerando Technology, enquanto na mesma semana o CI no Linux passava. O script usa barra normal para separar categorias, o disco usa barra invertida, e não consegue separar. Uma camada mais antiga está dentro do caractere: o segundo byte de "gōng" (功) em Big5 é a barra invertida ASCII, conhecida na comunidade de desenvolvimento como "xǔ gōng gài" (許功蓋). Como os caminhos são escritos, quais símbolos moram dentro dos caracteres — os valores padrão não contaram com esta máquina. O quotePath do Git é outra linha, com causa diferente.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'código aberto',
    'Windows',
    'Big5',
    'UTF-8',
    'codificação de caracteres',
    'chinês tradicional',
  ]
subcategory: '文字與工具'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-13
lastHumanReview: false
translatedFrom: 'Technology/功字裡的那根反斜線.md'
sourceCommitSha: '5dcaeea42'
sourceContentHash: 'sha256:57b41e308a296fb4'
sourceBodyHash: 'sha256:9af4500f829effce'
translatedAt: '2026-09-14T00:53:32+08:00'
---

> **Resumo em 30 segundos:** Rodei o script de status de tradução, a tela mostrou 4546, todos em `root`. No GitHub, o CI no Linux estava verde. Só depois percebi duas coisas. A barra invertida dos caminhos do Windows, o script usa barra normal e não consegue separar. A segunda metade do código Big5 de "gōng" (功) é ela mesma a barra invertida ASCII `\`. Dois mecanismos diferentes, mas que costumam aparecer juntos na mesma máquina Windows em chinês tradicional.

Mantenho o script de status de tradução do Taiwan.md em um Windows 11 com locale zh-TW. Naquela noite, rodei `i18n-status.py` como de costume, esperando o terminal imprimir os números. O console era cp950. A saída não tinha vermelho.

A tela parou em 4546. Todos em uma categoria chamada `root`. Technology era 0.

Na mesma semana, subindo para o GitHub, o CI no Linux estava verde.

A variável do script chama-se `zh_articles`, ela varre os caminhos sob `knowledge` exceto os diretórios em inglês, about e os que começam com underline; japonês, coreano e árabe também entram. Naquela noite, nem o nome da categoria conseguia extrair, mais de quatro mil caminhos enfiados no mesmo balde. Nenhuma exceção, nenhum aviso. A estatística parecia que o site inteiro tinha quebrado, mas nenhum arquivo a menos. [^8]

O caminho no disco é `knowledge\Technology\certo-artigo.md`, as pastas separadas por barra invertida. O script usa `split('/')` para pegar o nome da categoria. No Linux funciona, porque o caminho já usa barra. No Windows, não corta a barra invertida, o caminho inteiro volta como está, o artigo vai para o `root` padrão. [^1]

Mudando para deixar o `pathlib` cuidar dos diretórios, Technology passou a ter 59 artigos, batendo com o que está na pasta. No meio só havia um palpite: qual linha sua máquina usa para separar pastas.

> **📝 Nota do curador:** A sintaxe do script não estava errada, o CI de fato rodou os testes. A racha fica entre "a máquina onde o autor realmente senta" e "a máquina que a ferramenta acha que você senta". Essa fresta não pertence a nenhuma etapa, então ninguém fica responsável por vigiar.

## A linha dentro do "gōng" (功)

O caminho é a primeira camada. A segunda é muito mais velha, está enterrada no caractere.

O Big5 foi padronizado em 1984, um caractere chinês em dois bytes. Se o segundo byte cai entre `0x40` e `0x7E`, sobrepõe-se a símbolos ASCII comuns: `[`, `]`, `{`, `}`, `\`, `|`. O então professor associado do Departamento de Gestão da Informação da Universidade de Tecnologia Chaoyang, Hong Chao-kuei (洪朝貴, aposentado em agosto de 2023), escreveu em sua página de ensino: "Como 40-7E é o intervalo de códigos ASCII de caracteres comuns, às vezes traz alguns incômodos para programadores." [^2]

O código de "gōng" (功) é `A5 5C`. Esse `0x5C` final, em ASCII, é a barra invertida `\`. Um programa que varre byte a byte e trata `\` como escape ou separador, ao escanear a segunda metade de "gōng", acha que encontrou um caminho. Se o nome do arquivo tem "gōng", se o caminho tem "gōng", ambos podem tropeçar aqui.

A comunidade de desenvolvimento de Taiwan e Hong Kong chama isso de "xǔ gōng gài" (許功蓋): "xǔ" (許) é `B3 5C`, "gōng" (功) é `A5 5C`, "gài" (蓋) é `BB 5C`, três caracteres comuns que juntos parecem um nome de pessoa. [^5] Hong Chao-kuei também listou "jiā yě chéng zhèn gōng" (加也程陣功), cujos segundos bytes batem respectivamente em `[`, `]`, `{`, `}`, `\`, e criou a ferramenta de varredura `b5tm`. [^2] Quando um bug ganha nome de gente, costuma ser porque aparece com frequência suficiente para que uma geração precise de um jeito de apontar para ele e falar.

Em 2015, o autor do blog "Dark Thread" (黑暗執行緒) migrou para o Visual Studio 2015. Os velhos arquivos `.cs` ainda eram salvos em BIG5. Quando o compilador passou a usar o Roslyn, os "xǔ gōng gài" dentro dos arquivos viraram erros de compilação.

Dois dias depois, um colega disse que eles também travaram por muito tempo na migração, e acabaram caindo no artigo dele. Um internauta tinha dezenas de milhares de arquivos, converteu um e ainda sobrou um monte, "só restou dizer adeus ao VS2015". Ele depois escreveu uma ferramenta de conversão em lote para UTF-8, porque salvar à mão não acabava mais. [^7]

Isso não é a mesma coisa do `split('/')` anterior. Um é ferramenta moderna assumindo como o caminho deve ser. O outro é quarenta anos atrás, ao escolher dois bytes, o corpo do caractere acabou abrigando um símbolo. Mecanismos diferentes, mas a fatura costuma chegar junto na mesma máquina cp950. Sobre como o lado da entrada enfia o caractere no computador, veja [métodos de entrada de texto do Leste Asiático](/pt/technology/east-asian-input-methods/). Aqui a questão é: depois que o caractere já está no disco, a cadeia de ferramentas ainda o reconhece.

## Os valores padrão não abriram branch para esta máquina

O Git vem com `core.quotePath` ligado. Nomes de arquivo com bytes maiores que `0x80`, o `git status` imprime como `\344\270\255` esse tipo de octal. O nome chinês ainda está lá, você só não entende mais o que seu repositório está dizendo. [^3] Ele escapa os bytes altos do UTF-8. O `0x5C` do Big5 é outra linha. Parecem ambas barra invertida, mas a causa é diferente.

No Python 3 no Windows, se `open()` não tiver `encoding='utf-8'`, pode acabar usando o locale do sistema. O mesmo arquivo UTF-8, o Linux lê, esta máquina usa cp950 para decodificar, a pontuação ou o bopomofo quebram. [^4] Eu mesmo paguei essa: usei `Get-Content | Set-Content` do PowerShell 5.1 para converter arquivo UTF-8, o travessão longo virou `??` no diff. Isso também é imposto padrão, não é o segundo tema.

Quando a mensagem de status traz emoji, este console cp950 cai direto. O charset não tem aqueles símbolos, o Python não consegue imprimir, a exceção estoura até o topo. O CI no Linux não pega isso, porque não roda nesta máquina.

O `$HOME/project/src` dos exemplos de caminho do Git, Python, CI, não abriu uma ramificação para o Windows zh-TW.

Hong Chao-kuei, em entrevista ao iThome em 2015, falou sobre em que formato o governo deve abrir arquivos e por quanto tempo eles sobrevivem. A reportagem parafraseia: se o governo só usa produtos Microsoft para abrir dados de arquivos, equivale a acreditar que a Microsoft viverá mais que a República da China. [^6] Aquela frase trata de formato de arquivo e prazo de preservação. Dados amarrados a qual conjunto de ferramentas padrão, ao esticar o tempo, vira a pergunta de quem ainda consegue ler. A colaboração de código aberto amarra-se ao ambiente padrão de um certo tipo de máquina. O cabo de guerra entre tecnologia cívica e formatos de arquivo do governo, veja [comunidade open source e g0v](/pt/technology/open-source-and-g0v/). A cultura de desenvolvedores de Taiwan absorvendo essa defasagem há longo prazo, veja [espírito open source de Taiwan](/pt/technology/taiwan-open-source-spirit/).

Separador de caminho, codificação do terminal, `$HOME` dos exemplos de CI, nenhuma ramificação aberta para esta máquina. No dia em que 4546 caminhos foram classificados errado, nenhuma linha de código reportou erro. A estatística parecia normal, até você sentar na frente desta máquina.

## Leitura complementar

- [espírito open source de Taiwan](/pt/technology/taiwan-open-source-spirit): a cultura e o contexto da participação de desenvolvedores de Taiwan no código aberto.
- [métodos de entrada de texto do Leste Asiático](/pt/technology/east-asian-input-methods): como os caracteres entram no computador, da tabela de códigos ao teclado.
- [comunidade open source e g0v](/pt/technology/open-source-and-g0v): a colaboração entre dados abertos e formatos de governo.

## Referências

[^1]: [Microsoft Learn: Formatos de caminho de arquivo no Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — A documentação .NET explica que caminhos DOS tradicionais usam barra invertida como separador de diretório, e a barra normal é convertida em barra invertida.

[^2]: [Hong Chao-kuei: Problemas de código Big-5 que podem aparecer ao programar](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Página de ensino lista caracteres comuns cujo segundo byte cai no intervalo perigoso do ASCII (jiā yě chéng zhèn gōng / 加也程陣功), e apresenta a ferramenta de varredura b5tm. A página não informa o cargo. O iThome de 2015 chama de professor associado. A página pessoal dele registra atuação na Gestão da Informação da Chaoyang de 1997 a 2023, aposentadoria em agosto de 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — A documentação oficial explica que, por padrão, caminhos com bytes maiores que 0x80 são exibidos como sequências de escape octal.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — A documentação da função indica que, quando encoding não é especificado, pode-se usar o locale do sistema como codificação padrão.

[^5]: [Wikipédia: Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Registra "gōng" (功) 0xA55C, "xǔ" (許) 0xB35C, "gài" (蓋) 0xBB5C, e explica que este problema é jocosamente chamado de xǔ gōng gài (許功蓋).

[^6]: [iThome: Entrevista com Hong Chao-kuei](https://www.ithome.com.tw/news/93606) — Entrevista de 2015, o texto chama de professor associado do Departamento de Gestão da Informação da Universidade de Tecnologia Chaoyang. A página original costuma retornar 403; a frase sobre a vida da Microsoft usa apenas a paráfrase visível nos resultados de busca, não como citação literal.

[^7]: [Dark Thread: Máquina de escudo potencial — Resolvendo problema de compatibilidade BIG5 em arquivos do VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Registro de 2015 sobre compilação de código-fonte BIG5 no Visual Studio 2015, onde xǔ gōng gài (許功蓋) causava erros de compilação. O texto traz "só restou dizer adeus ao VS2015".

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Mesclado em 2026-07-26. Antes da correção, no Windows categories só sobrava root: 4546; depois, Technology zh: 59. Também removeu os emojis que derrubavam o console cp950.
