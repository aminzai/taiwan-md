---
title: 'La barra invertida en el carácter "gong": los dos impuestos predeterminados que pagan los ingenieros de Taiwán cada día'
description: 'En Windows 11 con la localización zh-TW, el script de estado de traducción mete más de cuatro mil rutas detectadas en `root`, haciendo que Technology sea cero; mientras que en una semana Linux CI es verde. El script usa barra diagonal para clasificar nombres y barra invertida para discos, sin poder separarlos. Una capa más antigua está incrustada en el carácter: el segundo byte del "gong" de Big5 es la barra invertida ASCII, y la comunidad de desarrollo lo llama *Xu Gong Gai*. La forma en que se escribe una ruta o qué símbolo contiene un carácter no incluye este hardware predeterminado. Git''s `quotePath` es otra línea con causas diferentes.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'Open Source',
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
translatedAt: '2026-09-14T00:53:28+08:00'
---

> **Resumen de 30 segundos:** Ejecuté el script de estado de traducción y la pantalla mostró 4546, todo en `root`. El CI de Linux en GitHub era verde. Luego entendí dos cosas. La barra invertida de las rutas de Windows no podía ser separada por el script con diagonal. La segunda mitad del código Big5 de "gong" es la propia barra invertida ASCII. Dos mecanismos diferentes aparecen a menudo juntos en una máquina Windows china tradicional.

Estaba manteniendo el script de estado de traducción de Taiwan.md en Windows 11 con la localización zh-TW. Esa noche, ejecuté `i18n-status.py` como era habitual, esperando que la terminal imprimiera un número. La consola principal era cp950. No había texto rojo en la salida.

La pantalla se detuvo en 4546. Todo estaba en una categoría llamada `root`. Technology era 0.

En la misma semana, al subir a GitHub, el CI de Linux fue verde.

El script tenía como nombre de variable `zh_articles`, y escaneaba las rutas bajo `knowledge` excepto los directorios en inglés, about y línea base; también se contaban japonés, coreano y árabe. Esa noche, ni siquiera podía separar los nombres de categoría, y más de cuatro mil rutas fueron metidas en una sola celda. Sin excepciones, sin advertencias. El conteo parecía que todo el sitio estaba roto, pero no faltaba ningún archivo.[^8]

La ruta del disco era `knowledge\Technology\un_articulo.md`, separando directorios con barra invertida. El script usaba `split('/')` para obtener el nombre de la categoría. Esto funcionaba en Linux porque la ruta ya era con diagonal. En Windows, no podía separar la barra invertida, y toda la ruta volvía tal cual, y el artículo se metía en la predeterminada `root`.[^1]

Después de cambiar para que `pathlib` manejara los directorios, Technology tenía 59 artículos debajo, lo que coincidía con el contenido del directorio. Solo había una suposición intermedia: qué tipo de línea usaba tu máquina para separar directorios.

> **📝 Nota del curador:** La sintaxis del script no estaba mal escrita y el CI sí ejecutó las pruebas. El punto de quiebre está entre "la máquina donde trabaja el autor" y "la máquina que la herramienta cree que estás usando". Esta costura no pertenece a ningún proceso, por lo que nadie está encargado de vigilarla.

## La línea dentro de "gong"

La ruta es la primera capa. La segunda capa es mucho más antigua y está incrustada en el carácter.

Big5 se estandarizó en 1984; un carácter chino son dos bytes. Si el segundo byte cae entre `0x40` y `0x7E`, colisiona con símbolos comunes de ASCII: `[` , `]` , `{` , `}` , `\` , `|`. El profesor adjunto del Departamento de Administración de Sistemas de la Universidad Tecnológica de Chaoyang (jubilado en agosto de 2023) escribió en su página de enseñanza: "Debido a que el rango ASCII 40-7E es un rango de caracteres comunes, a veces causa problemas a los programadores".[^2]

El código para "gong" es `A5 5C`. El `0x5C` posterior es la barra invertida `\` en ASCII. Un programa que escanea una cadena byte por byte y trata a `\` como un escape o separador, al encontrar la segunda mitad de "gong", puede pensar que ha encontrado una ruta. Si el nombre del archivo contiene "gong" o la ruta contiene "gong", ambos pueden tropezar aquí.

La comunidad de desarrollo de Taiwán y Hong Kong lo llama _Xu Gong Gai_: "Xu" es `B3 5C`, "gong" es `A5 5C`, y "Gai" es `BB 5C`; tres caracteres comunes escritos juntos como un nombre de persona.[^5] El profesor adjunto también enumeró "Jia Ye Cheng Zhen Gong", donde el segundo byte colisiona con `[` , `]` , `{` , `}` , `\`, e introdujo la herramienta de escaneo `b5tm`.[^2] Un _bug_ tomó un nombre, generalmente porque aparecía con suficiente frecuencia como para que una generación tuviera que señalarlo y hablar sobre él.

En 2015, el autor del blog "Dark Thread" cambió a Visual Studio 2015. Los antiguos archivos `.cs` seguían guardándose en BIG5. Después de que el compilador cambiara a Roslyn, los _Xu Gong Gai_ dentro de los archivos se convirtieron en errores de compilación.

Dos días después, un colega le dijo que ellos también habían tenido problemas durante mucho tiempo y finalmente rastrearon su artículo. Un usuario tenía miles de archivos, convirtió uno y todavía quedaban muchos, "por lo que tuvo que decir adiós a VS2015". Luego escribió una pequeña herramienta para convertir lotes a UTF-8 porque no podía guardarlos manualmente.[^7]

Esto no es lo mismo que el `split('/')` anterior. Uno es un supuesto moderno sobre cómo debe lucir una ruta. El otro es un símbolo viviendo dentro del cuerpo de un carácter después de elegir dos bytes hace cuarenta años. Los mecanismos son diferentes, pero la factura a menudo llega junta en la misma máquina cp950. La parte de entrada (cómo se envía el carácter a la computadora) se ve en [métodos de entrada de caracteres de Asia Oriental](/es/technology/east-asian-input-methods/). Aquí hablamos de cuando el carácter ya está en el disco y si la cadena de herramientas lo reconoce.

## El valor predeterminado no creó una rama para esta máquina

Git tiene activado por defecto `core.quotePath`. Los nombres de archivo con bytes mayores a `0x80` se muestran como secuencias de escape octales, como `\344\270\255`, en `git status`. El nombre del archivo chino sigue ahí; tú solo no entiendes lo que dice tu repositorio cada día.[^3] Escapa los bytes altos de UTF-8. El `0x5C` de Big5 es otra línea. Parecen ser la misma barra invertida, pero las causas son diferentes.

En Python 3, si `open()` en Windows no especifica `encoding='utf-8'`, puede usar la localización del sistema por defecto. Un archivo UTF-8 idéntico se lee correctamente en Linux, pero al ser decodificado con cp950 en esta máquina, los signos de puntuación o las notas sonarán mal.[^4] Yo lo experimenté una vez: usé `Get-Content | Set-Content` de PowerShell 5.1 para convertir un archivo a UTF-8, y el guion largo se convirtió en `??` en el _diff_. Eso también fue un impuesto predeterminado, no el segundo tema.

Cuando la información de estado lleva emojis, esta consola cp950 colapsa directamente. El conjunto de caracteres no tiene esos símbolos; Python no puede imprimirlos, y la excepción explota en el nivel superior. El CI de Linux no detecta esto porque no se ejecuta en esta máquina.

Git, Python, y los ejemplos de rutas del CI como `$HOME/project/src`, no crearon una rama separada para Windows zh-TW.

En 2015, el profesor adjunto Hong fue entrevistado por iThome sobre qué formato usar para abrir archivos gubernamentales y cuánto durarían. La reportaje resumió su significado: si el gobierno solo usa productos de Microsoft para abrir datos de archivos, es como confiar en que la vida útil de Microsoft será más larga que la de la República de China (Taiwán).[^6] Esa frase hablaba del formato del archivo y la antigüedad de la conservación. Los datos están atados a un conjunto de herramientas predeterminadas; cuando el tiempo se alarga, se convierte en quién puede seguir leyéndolo. La colaboración _open source_ está atada al entorno predeterminado de cierto tipo de máquina. La tensión entre la tecnología ciudadana y los formatos de archivos gubernamentales se ve en [la comunidad open source y g0v](/es/technology/open-source-and-g0v/). Los desarrolladores de Taiwán han absorbido culturalmente esta disparidad durante mucho tiempo, como se ve en [el espíritu abierto de Taiwán](/es/technology/taiwan-open-source-spirit/).

El separador de rutas, la codificación de la terminal y el `$HOME` del ejemplo del CI no crearon una rama secundaria para esta máquina. El día que 4546 rutas fueron clasificadas por error, ninguna línea de código reportó un error. El conteo parecía normal hasta que te sentaste frente a esta máquina.

## Lecturas relacionadas

- [El espíritu abierto de Taiwán](/es/technology/taiwan-open-source-spirit): La cultura y el contexto con el que los desarrolladores de Taiwán participan en _open source_.
- [Métodos de entrada de caracteres de Asia Oriental](/es/technology/east-asian-input-methods): Cómo se teclea un carácter, desde la tabla de códigos hasta el teclado.
- [La comunidad open source y g0v](/es/technology/open-source-and-g0v): La colaboración entre datos abiertos y formatos gubernamentales.

## Referencias

[^1]: [Microsoft Learn: Formato de ruta de sistema Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — La documentación .NET explica que los archivos DOS tradicionales usan barra invertida como separador de directorios, y la barra diagonal se convierte en barra invertida.

[^2]: [Hong Chao-gui: Problemas con códigos Big5 al programar](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — La página de enseñanza enumera caracteres comunes cuyo segundo byte cae en la zona peligrosa de ASCII (Jia Ye Cheng Zhen Gong) e introduce la herramienta de escaneo b5tm. No se menciona el cargo en el pie de página. En 2015, iThome lo llamó profesor adjunto. Yo trabajé en Chaoyang en su sitio web desde 1997 hasta 2023 y me jubilé en agosto de 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — La documentación oficial explica que por defecto, los nombres de archivo con bytes mayores a 0x80 se muestran como secuencias de escape octales.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — La descripción de la función indica que si no se especifica `encoding`, puede usar la localización del sistema como codificación predeterminada.

[^5]: [Wikipedia: Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Enumera "gong" 0xA55C, "Xu" 0xB35C y "Gai" 0xBB5C, y explica que este problema se llama _Xu Gong Gai_.

[^6]: [iThome: Entrevista a Hong Chao-gui](https://www.ithome.com.tw/news/93606) — Entrevista de 2015; el artículo lo menciona como profesor adjunto del Departamento de Administración de Sistemas de la Universidad Tecnológica de Chaoyang. La página original a menudo devolvía 403, por lo que solo se citan los resúmenes visibles en los resultados de búsqueda y no se consideran citas textuales.

[^7]: [Dark Thread: Shielded Machine - Solución al problema de compatibilidad BIG5 de archivos VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Documenta el error de compilación causado por _Xu Gong Gai_ al compilar código fuente BIG5 en Visual Studio 2015. El artículo menciona "tuvo que decir adiós a VS2015".

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Fusión el 26/07/2026. Antes de la corrección, en Windows, las categorías solo mostraban `root: 4546`; después de corregir Technology zh: 59. Se eliminaron los emojis que hacían colapsar la consola cp950.
