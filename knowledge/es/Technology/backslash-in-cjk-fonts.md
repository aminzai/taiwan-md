---
title: 'La barra invertida dentro del carácter «gong»: el doble impuesto por defecto que pagan los ingenieros de Taiwán'
description: 'En Windows 11 en la configuración de idioma zh-TW, el script de estado de traducción arroja todas las más de cuatro mil rutas al directorio raíz, haciendo que la categoría Tecnología sea cero, mientras que la CI de Linux es verde en la misma semana. El script usa barras diagonales para dividir los nombres de categoría, pero el sistema de archivos usa barras invertidas, por lo que no puede dividirlos correctamente. Una capa aún más antigua está oculta en los caracteres: el segundo byte de «gong» en Big5 es exactamente una barra invertida ASCII, conocida en la comunidad de desarrollo como «Xu Gonggai». La forma de escribir las rutas y los símbolos alojados en los caracteres muestran que los valores por defecto no han calculado esta máquina. La opción quotePath de Git es otra línea, con causas diferentes.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'código abierto',
    'Windows',
    'Big5',
    'UTF-8',
    'codificación de caracteres',
    'chino tradicional',
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
translatedAt: '2026-09-11T18:15:11+08:00'
---

> **Resumen en 30 segundos:** Ejecuto el script de estado de traducción y la pantalla muestra 4546, todo en `root`. En GitHub, la CI de Linux es verde. Después logro entender claramente dos cosas. La barra invertida de las rutas de Windows no puede ser dividida por el script usando la barra diagonal. La segunda mitad del código Big5 de «gong» es en sí misma una barra invertida ASCII `\`. Los mecanismos de ambos casos son diferentes, pero suelen aparecer juntos en la misma máquina de chino tradicional de Windows.

Mantengo el script de estado de traducción de Taiwan.md en Windows 11 con la configuración de idioma zh-TW. Esa noche, como era habitual, ejecuté `i18n-status.py` y esperé a que la terminal imprimiera los números. La consola usa cp950. No hubo texto en rojo en la salida.

La pantalla se detuvo en 4546. Todo estaba en una categoría llamada `root`. Tecnología era 0.

En la misma semana, al hacer push a GitHub, la CI en Linux mostraba luz verde.

La variable del script se llama `zh_articles` y escanea las rutas debajo de `knowledge`, excluyendo inglés, about y directorios con guion bajo; también se incluyen japonés, coreano y árabe. Esa noche ni siquiera pudo dividir los nombres de categoría, y las más de cuatro mil rutas fueron vertidas en una sola casilla. Sin excepciones, sin advertencias. Las estadísticas parecían indicar que todo el sitio estaba roto, sin que faltara ni un solo archivo. [^8]

Las rutas en el disco son `knowledge\Technology\AlgunArtículo.md`, con las carpetas separadas por barras invertidas. El script usa `split('/')` para obtener el nombre de la categoría. En Linux esta línea funciona porque las rutas son barras diagonales por defecto. En Windows no puede cortar la barra invertida, por lo que la ruta completa regresa intacta y el artículo es enviado a la categoría por defecto `root`. [^1]

Después de cambiar para que `pathlib` gestione los directorios, debajo de Tecnología hay 59 artículos, consistente con lo que hay en las carpetas. Solo hay una suposición de por medio: qué tipo de línea usa tu máquina para separar las carpetas.

> **📝 Nota del curador:** La sintaxis del script no está mal escrita, y la CI efectivamente ejecutó las pruebas. La ruptura ocurre entre «la máquina en la que el autor está realmente sentado» y «la máquina que la herramienta asume que estás usando». Esta grieta no pertenece a ningún componente específico, por lo que nadie es responsable de vigilarla.

## La línea dentro de «gong»

Las rutas son la primera capa. La segunda es mucho más antigua y está oculta en los caracteres.

Big5 fue definido en 1984, con dos bytes por carácter chino. Si el segundo byte cae entre `0x40` y `0x7E`, se superpone con los símbolos ASCII comunes: `[`, `]`, `{`, `}`, `\`, `|`. El entonces profesor adjunto del departamento de Gestión de Información de la Universidad Tecnológica Chaoyang, Hong Zhao-gui (jubilado en agosto de 2023), escribió en su página de enseñanza: «Dado que 40-7E es el rango de códigos ASCII de caracteres de uso común, a veces esto puede causar algunas molestias a los programadores». [^2]

El código de «gong» es `A5 5C`. Ese `0x5C` posterior, en ASCII, es una barra invertida `\`. Un programa que escanea una cadena byte por byte y trata `\` como un carácter de escape o separador, al llegar a la segunda mitad de «gong», pensará que se encuentra con una ruta. Si el nombre del archivo tiene «gong», o si la ruta tiene «gong», ambos pueden tropezar aquí.

En las comunidades de desarrollo de Taiwán y Hong Kong lo llaman «Xu Gonggai»: «Xu» es `B3 5C`, «gong» es `A5 5C`, «gai» es `BB 5C`; tres caracteres comunes escritos juntos parecen un nombre de persona. [^5] Hong Zhao-gui también listó «jia, ye, cheng, zhen, gong», cuyos segundos bytes chocan respectivamente con `[`, `]`, `{`, `}`, `\`, y creó una herramienta de escaneo llamada `b5tm`. [^2] Un error de programación recibe un nombre de persona generalmente porque aparece con frecuencia suficiente para que una generación pueda señalarlo y hablar de él.

En 2015, el autor del blog «Dark Thread» cambió a Visual Studio 2015. Los antiguos archivos `.cs` aún se guardaban en BIG5. Después de que el compilador cambiara a Roslyn, las «Xu Gonggai» dentro de los archivos se convertirían en errores de compilación.

Dos días después, un colega le dijo que ellos también se habían quedado atascados por mucho tiempo después del cambio, y finalmente, tras buscar en foros, volvieron a su artículo. Un usuario tenía miles de archivos, convirtió uno y aún quedaban muchos, «así que tuvo que decirle adiós a VS2015». Más tarde escribió una herramienta por lotes para convertir a UTF-8, porque guardar manualmente como nuevo no era viable. [^7]

Esto no es lo mismo que el `split('/')` anterior. Uno es una herramienta moderna que asume cómo se ven las rutas. El otro es un símbolo que entró en el cuerpo del carácter después de elegir un sistema de dos bytes hace cuarenta años. Los mecanismos son diferentes, pero las facturas a menudo llegan juntas en la misma máquina cp950. Cómo se envían los caracteres a la computadora desde el lado de la entrada se ve en [Métodos de entrada de caracteres de Asia Oriental](/es/technology/east-asian-input-methods/). Aquí se trata de lo que la cadena de herramientas reconoce después de que el carácter ya está en el disco.

## Los valores por defecto no crearon una rama para esta máquina

Git tiene `core.quotePath` activado por defecto. Los nombres de archivo con bytes mayores a `0x80` se imprimirán en `git status` como secuencias octales `\344\270\255`. Los nombres de archivo en chino siguen ahí, solo que no entiendes qué dice tu repositorio cada día. [^3] Esto escapa los bytes altos de UTF-8. El `0x5C` de Big5 es otra línea. Parecen ser barras invertidas, pero las causas son diferentes.

Si Python 3 en Windows no especifica `encoding='utf-8'` en `open()`, puede heredar el idioma del sistema. Un mismo archivo UTF-8 se lee bien en Linux, pero esta máquina lo decodifica con cp950, corrompiendo los signos de puntuación o el bopomofo. [^4] Yo mismo pagué este impuesto una vez: al usar `Get-Content | Set-Content` de PowerShell 5.1 para modificar un archivo UTF-8, el guion largo se convirtió en `??` en el diff. Ese también es un impuesto por defecto, no el segundo tema.

Cuando los mensajes de estado llevan emojis, esta consola cp950 se bloquea directamente. El conjunto de caracteres no tiene esos símbolos, Python no puede imprimirlos y la excepción estalla hasta la capa superior. La CI de Linux no puede detectar esto porque no se ejecuta en esta máquina.

Git, Python, los ejemplos de rutas en la CI como `$HOME/project/src` no crearon una rama separada para Windows en zh-TW.

En 2015, Hong Zhao-gui fue entrevistado por iThome, hablando sobre en qué formato deberían abrirse los archivos gubernamentales y cuánto tiempo podrían sobrevivir. El informe resume su idea: si el gobierno solo usa productos de Microsoft para abrir archivos, es como creer que la vida de Microsoft será más larga que la de la República de China. [^6] Esta frase trata sobre formatos de archivo y años de conservación. Cuando los datos están atados a un conjunto de herramientas por defecto, al extender el tiempo, se convierte en quién puede leerlos. La colaboración de código abierto está atada al entorno por defecto de un tipo de máquina. La tensión entre la tecnología cívica y los formatos de archivo gubernamentales se ve en [Comunidad de código abierto y g0v](/es/technology/open-source-and-g0v/). Los desarrolladores de Taiwán han absorbido durante mucho tiempo la cultura de esta brecha, como se ve en [Espíritu de código abierto de Taiwán](/es/technology/taiwan-open-source-spirit/).

Los separadores de rutas, la codificación de la terminal, `$HOME` en los ejemplos de la CI, no crearon una rama para esta máquina. El día que 4546 rutas fueron clasificadas incorrectamente, ninguna línea de código generó un error. Las estadísticas parecían normales, hasta que te sientas frente a esta máquina.

## Lecturas adicionales

- [Espíritu de código abierto de Taiwán](/es/technology/taiwan-open-source-spirit): La cultura y el contexto de la participación de los desarrolladores de Taiwán en el código abierto.
- [Métodos de entrada de caracteres de Asia Oriental](/es/technology/east-asian-input-methods): Cómo se escriben los caracteres en la computadora, desde las tablas de códigos hasta los teclados.
- [Comunidad de código abierto y g0v](/es/technology/open-source-and-g0v): Colaboración entre datos abiertos y formatos gubernamentales.

## Referencias

[^1]: [Microsoft Learn: Formato de rutas de archivo en sistemas Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — La documentación de .NET explica que las rutas DOS tradicionales usan la barra invertida como separador de directorios, y las barras diagonales se convierten en barras invertidas.

[^2]: [Hong Zhao-gui: Problemas de código big-5 que pueden ocurrir al programar](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — La página de enseñanza lista los caracteres comunes cuyo segundo byte cae en el intervalo peligroso de ASCII (jia, ye, cheng, zhen, gong) e introduce la herramienta de escaneo b5tm. No se especifica el rango jerárquico al final de la página. En 2015, iThome lo llamó profesor adjunto. La página principal de la persona indica que estuvo en el departamento de Gestión de Información de la Universidad Tecnológica Chaoyang de 1997 a 2023, jubilándose en agosto de 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — La documentación oficial explica que por defecto se mostrarán las rutas con bytes mayores a 0x80 como secuencias de escape octales.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — La descripción de la función indica que si no se especifica encoding, puede heredar el idioma del sistema como codificación por defecto.

[^5]: [Wikipedia: Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Indica que «gong» es 0xA55C, «Xu» es 0xB35C, «gai» es 0xBB5C, y explica que este problema se bromea llamándolo «Xu Gonggai».

[^6]: [iThome: Entrevista a Hong Zhao-gui](https://www.ithome.com.tw/news/93606) — Entrevista de 2015, donde se le llama profesor adjunto del departamento de Gestión de Información de la Universidad Tecnológica Chaoyang. La página original a menudo devuelve 403; la frase sobre la vida de Microsoft solo se adopta de la descripción del informe visible en los resultados de búsqueda, no se considera una cita textual exacta.

[^7]: [Dark Thread: Stealth Fighter - Solución del problema de compatibilidad BIG5 de archivos de programa VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Registro de 2015 sobre cómo las «Xu Gonggai» causan errores de compilación al compilar código fuente BIG5 con Visual Studio 2015. El texto contiene «tuvo que decirle adiós a VS2015».

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Fusionado el 2026-07-26. Antes de la corrección, en Windows las categorías solo tenían root: 4546; después de arreglarlo, Technology zh: 59. Se eliminaron también los emojis que hacían que la consola cp950 se bloqueara.
