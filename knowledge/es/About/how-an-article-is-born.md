---
title: 'Cómo nace un artículo: La línea de producción de seis etapas de Taiwan.md para combatir la intuición de la escritura por IA (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)'
description: 'Cada artículo de Taiwan.md que lees tiene calidez, escenas y es verificable; detrás hay seis etapas, más de veinte puertas de control obligatorias y un equipo editorial de IA que no escribe el borrador. La única razón de ser de esta máquina es corregir los errores más comunes de la escritura por IA: ordenar hechos cronológicamente al buscar, generar frases plásticas sin información, traducir al chino resúmenes en inglés como citas falsas y contaminarse con los vicios de artículos antiguos. Este artículo desmonta esta línea de producción, y ella misma es el resultado de su ejecución.'
date: 2026-06-19
tags:
  [
    'about',
    'meta',
    'metodología de escritura',
    'curaduría',
    'rewrite-pipeline',
    'editorial',
    'semiont',
    'escritura por IA',
  ]
author: 'Taiwan.md'
category: 'About'
readingTime: 11
featured: false
lastVerified: 2026-06-19
lastHumanReview: false
relatedDiary: ['2026-06-19-123349-manual']
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: '984fb7892'
sourceContentHash: 'sha256:92fcb394123e4aee'
sourceBodyHash: 'sha256:b8984a2133e5738f'
translatedAt: '2026-07-26T03:41:21+08:00'
---

# Cómo nace un artículo: La línea de producción de seis etapas de Taiwan.md para combatir la intuición de la escritura por IA (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)

> **Resumen en 30 segundos:** Cada artículo de Taiwan.md que lees tiene detrás una línea de producción de seis etapas: primero pensar la perspectiva, luego buscar, escribir el final primero, verificar palabra por palabra, añadir elementos visuales y crear enlaces bidireccionales. Esta línea de producción no es un flujo general de "escribir bien un artículo"; cada una de sus puertas está diseñada para bloquear un error específico de la escritura por IA: ordenar cronológicamente los hechos encontrados, generar frases plásticas sin información, traducir resúmenes en inglés como si fueran citas directas y contaminarse con los vicios de artículos antiguos. Este artículo desmonta esta línea de producción, y ella misma es el resultado de su ejecución.

El 18 de junio de 2026, a las 7:53 p. m., un _commit_ entró silenciosamente en la rama principal. Se publicó un artículo sobre la banda taiwanesa de tres miembros "Elephant Gym" (大象體操): 5.604 caracteres chinos, 56 notas al pie y 11 subtítulos basados en escenas[^1]. En ese momento, nadie estaba frente a una computadora. Fue el _routine_ (flujo automatizado) de Taiwan.md, en una noche sin turno de guardia, quien lo completó y _ship_ (publicó) por sí mismo.

Pero antes de ese _commit_, este artículo ya había realizado casi cien búsquedas, leído 59 fuentes y tenido 12 verificaciones que invalidaron el enfoque original. Completó seis etapas y más de veinte puertas de control obligatorias, movilizando un equipo editorial de IA con roles bien definidos. Lo que lees son los 5.604 caracteres sobre la superficie. Este artículo quiere mostrarte la máquina bajo el agua.

```tw-figure
Cerca de 100 búsquedas → 1 artículo
La investigación del artículo "Elephant Gym": ~95 consultas, 59 fuentes, 12 falsaciones
Registro del routine de Taiwan.md, 2026-06-18
```

## Por qué construir una máquina para un artículo

Si le das un tema a una IA y le pides que escriba un artículo, lo más probable es que haga lo siguiente: busque, ordene los hechos encontrados cronológicamente, añada al final de cada párrafo una conclusión que suene significativa y escriba al final una frase como "el futuro continuará desarrollándose". Wikipedia ya tiene ese tipo de artículos; los granjas de contenido por IA producen decenas de miles de ellos cada día. Desde el primer día, Taiwan.md decidió no hacer esto.

El problema es que estos malos hábitos son el valor predeterminado de la IA, no errores ocasionales. REWRITE-PIPELINE los descompone en seis tipos de fallos recurrentes: quedarse sin _tokens_ al final, convertir la segunda mitad en un borrador. No hay puntos de control intermedios, la calidad se desliza silenciosamente. Dejar el final para el final significa que, al agotarse la energía, se convierte en un producto enlatado. Las normas de texto enriquecido se olvidan al final; diferentes ángulos de enfoque se tratan como flujos independientes. Y el error más fatal: buscar hechos y luego pensar en la perspectiva; el resultado es una crónica con desequilibrio de densidad[^2].

Por lo tanto, la lógica de diseño de esta línea de producción es simple: cada tipo de error posible tiene una puerta que lo bloquea. No es un flujo genérico de "buena escritura"; es el inverso de la _slop_ (basura) generada por IA.

> **✦** "Wikipedia responde 'qué es PTT'. Taiwan.md responde 'por qué PTT vale la pena leerlo durante 8 minutos'."

Así es como sale "Elephant Gym" desde el otro extremo de la línea de producción:

```tw-stat
5.604 caracteres | Texto en chino | "Elephant Gym"
56 notas | Al pie, cada una verificable con Ctrl-F | Verificación primaria
11 párrafos | Subtítulos basados en escenas, no cronológicos | Ritmo narrativo
12 puntos | Investigación que invalida el enfoque original | Prioridad de falsación
Fuente: Registro del routine de Taiwan.md, 2026-06-18
```

## Seis etapas, cada una previene un fallo

La línea de producción tiene seis etapas de principio a fin; cada artículo debe completarlas todas, sin importar el tema o la longitud.

**Etapa 0 Perspectiva**: Primero se debe clarificar qué tipo de memoria representa este artículo para los taiwaneses y dónde podría estar la tensión central. **Etapa 1 Investigación**: Solo entonces se comienza a buscar, con al menos 80 consultas en todo el artículo, y una cuota fija: al menos 40 fuentes en chino, 20 en inglés, 15 primarias y 5 de la parte contraria, obligando a buscar evidencia contraria a la hipótesis[^3]. **Etapa 2 Escritura**: La primera acción es escribir el final, porque al final del proceso la energía se agota; dejar el final más importante para el final significa entregárselo al yo más cansado. **Etapa 3 Verificación**: Verificación palabra por palabra: aritmética, unidades, cada cita debe ser localizable con Ctrl-F en la fuente original. **Etapa 4 Forma**: Añadir visualización y medios. **Etapa 5 Conexión**: Conectar este artículo bidireccionalmente con otros artículos de la base de conocimientos.

La distribución del esfuerzo en las seis etapas es intencional. La escritura consume más del 40%, pero la búsqueda más la verificación juntas representan casi la mitad. Lo que realmente consume tiempo en un artículo no es teclear, sino lo que ocurre antes y después de teclear.

```tw-bars
Dónde se gasta el esfuerzo en un artículo (límite presupuestario de tokens por etapa, %)
Etapa 0 Perspectiva | 12 | Reflexión previa a la edición
Etapa 1 Investigación | 28 | Búsqueda ≥ 80 veces
Etapa 2 Escritura | 42 | Escribir el final primero
Etapa 3 Verificación | 18 | Verificación palabra por palabra
Etapa 4 Forma | 8 | Visualización y medios
Etapa 5 Conexión | 5 | Enlaces bidireccionales
Fuente: Presupuestos por etapa de REWRITE-PIPELINE v7.5
```

## Pensar claramente antes de buscar

De las seis etapas, la más contraintuitiva es la primera.

La mayoría de la escritura por IA es "buscar hechos y luego añadir una perspectiva". Taiwan.md invierte el orden en v6.0: antes de empezar a buscar, desde la perspectiva del editor jefe, se deben responder claramente seis preguntas: ¿qué memoria representa este tema para los taiwaneses, qué caras se han ignorado, cómo se conecta con nuestra historia de vida. Solo cuando se tiene claro, se busca para verificar con preguntas específicas.

Por qué este orden es tan importante, lo demuestra una lección. Al escribir sobre "Apple Sprite" (蘋果西打), la línea de producción buscó primero y encontró una crisis de ventas estancadas y casi desaparición; el artículo se convirtió en una historia de una especie en peligro. El observador retrocedió y señaló que "Apple Sprite" es una memoria colectiva de 60 años para los taiwaneses, desde las botellas de vidrio de la era de las canicas hasta hoy[^4]. Tratarlo como una noticia de crisis reduce la escala de la memoria. La versión que buscó primero convirtió un recuerdo cálido en ansiedad.

```tw-versus
Intuición de la IA: buscar y ya | Taiwan.md: pensar antes de buscar
Encontrar hechos y forzar una perspectiva al final | Decidir la perspectiva primero, buscar para verificar con preguntas
Llenar el artículo de hechos, desequilibrio de densidad | Cortar los hechos que no encajan en la perspectiva
Sin ancla central, el final se vuelve genérico | Si no se encuentra una ancla correspondiente, replantear
Convertirlo en un registro corporativo o currículum | Convertirlo en una historia de "ya veo"
Fuente: REWRITE-PIPELINE v7.5 Etapa 0 Perspectiva
```

## Buscar: escribir el informe de investigación como un artículo académico

Una vez definida la perspectiva, se empieza a buscar. La búsqueda de Taiwan.md tiene dos números duros: un artículo de profundidad debe tener al menos 80 consultas en todo el proceso, y la cuota de fuentes está fija: al menos 40 en chino, 20 en inglés, 15 primarias y 5 de la parte contraria. El último grupo es el más fácil de saltarse por pereza; obliga al escritor a buscar evidencia que contradiga su hipótesis, en lugar de solo seleccionar la que la confirme.

Terminar de buscar no es solo meter resúmenes en el artículo. Detrás de cada artículo de profundidad hay un informe de investigación comparable a un artículo de posgrado, dividido en ocho capítulos: perspectiva, registro de búsqueda, hallazgos por tema, banco de citas, contraejemplos y barreras, paquete de hechos limpios para el escritor, bibliografía y tabla de verificación, y la última sección con los informes originales palabra por palabra de cada agente de investigación. Una regla suena estricta: si se busca pero no se registra la pista original en el informe, se considera que no se buscó. El informe es la fuente de la verdad de este artículo; debe pasar primero la aceptación de una herramienta: al menos 25 fuentes no repetidas, las fuentes en inglés no pueden ser cero, las fuentes primarias no pueden ser cero[^9]. Si no pasa, el artículo ni siquiera tiene derecho a empezar a escribir.

```tw-stat
≥ 80 veces | Profundidad de búsqueda de un artículo de profundidad | Chino 40 / Inglés 20 / Primario 15 / Contrario 5
8 secciones | Estructura del informe de investigación | Comparable a un artículo de posgrado
≥ 25 fuentes | Fuentes no repetidas (aceptación por herramienta) | Inglés ≠ 0, Primario ≠ 0
Fuente: REWRITE-PIPELINE v7.5 Paso 1.1 / 1.7
```

En temas controversiales hay una capa adicional. Al escribir sobre política, visión histórica o políticas, se asigna un agente "contrario" especializado en encontrar fuentes opuestas a la postura del artículo pero bien argumentadas; cada una debe tener una URL verificable. Si no se completa la cuota, se escribe honestamente "la narrativa contraria es débil", sin forzarla. Un artículo con una sola voz no se considera terminado aquí.

En la etapa de citas hay una línea roja. Las comillas son una promesa: lo que está entre comillas es la palabra exacta, por lo que cada cita debe ser localizable con Ctrl-F en la fuente original. La trampa más común es que la herramienta extrae de un sitio web en chino, pero devuelve un resumen en inglés, y el escritor traduce ese resumen en inglés al chino como "cita directa"; eso es una invención. En 2026, al escribir el artículo sobre Li Yang (李洋), se cometió este error: el resumen en inglés devuelto por la herramienta era "I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin", que traducido al chino se convirtió en "llegué primero a la escuela, pero no pude seguir el ritmo de mi compañero Qi-lin". Sin embargo, la cita original en chino de Li Yang era "del equipo de educación física de 15 personas, yo soy del grupo de atrás, Qi-lin es del grupo de adelante"[^10]. El significado es similar, pero el tono es completamente diferente; por eso las citas traducidas de vuelta no cuentan.

## Escribir: cada artículo debe tener una persona

Una vez completados los materiales, se entra en la etapa más costosa. EDITORIAL es el documento de Taiwan.md que le enseña a sí mismo cómo convertir materiales en un artículo con calidez; establece tres reglas de hierro desde el principio: tener una historia, no solo información; cada hecho debe ser verificable; cada artículo debe tener una persona[^11].

La tercera es la más fácil de ignorar, pero la más crucial. Las instituciones no hacen que la gente recuerde, los conceptos tampoco, las personas sí. Por lo tanto, en lugar de empezar una artículo sobre TSMC desde la empresa, es mejor empezar desde una persona específica; en lugar de empezar un artículo sobre el Seguro Médico Nacional desde el sistema, empezar desde una tarjeta, una sala de consulta, una persona. Reducir un tema abstracto a una persona que el lector puede seguir le da temperatura al artículo y cumple la promesa anterior, haciendo que el lector quiera compartirlo después de leerlo.

## Las cinco cosas que se deben encontrar antes de empezar a escribir

EDITORIAL llama la preparación antes de entrar en el estado de escritura "los ojos para ver los materiales": al recibir un material, se deben encontrar cinco cosas; si no se encuentran, no se debe empezar a escribir[^5].

**Contradicción**: una tensión central expresable en una frase, donde alguien hace X pero contradice Y en lo que cree. **Objeto**: algo concreto que el lector pueda ver con los ojos y tocar con las manos, como el pan de lichi y rosa de Wu Bao-chun (吳寶春) o la gran bola dorada de 660 toneladas colgando en el piso 87. **Cita**: una palabra exacta dicha por una persona real; como las comillas son una promesa de "esta es la palabra original", debe ser localizable con Ctrl-F en la fuente. **Escena**: un instante con tiempo, lugar y acción, reduciendo "la política fue aprobada" a "el día de la revisión del Comité de Salud y Medio Ambiente del Yuan Legislativo el 8 de enero de 2025". **Detalle**: el color de la ropa, el clima de ese día, el tono de voz; estos son datos que no existen en las especificaciones, pero son la evidencia de "realmente hubo alguien en el lugar".

De estas cinco, la contradicción va primero.

```tw-quote
Si no se encuentra la contradicción, este artículo no debería ser reescrito
REWRITE-PIPELINE v7.5 | Etapa 1.4 Bloquear la contradicción
```

La tensión puede ser un conflicto, un fracaso o una crisis, pero la perspectiva es "cómo se convirtió esto en lo de hoy, hacia dónde va", no "qué está roto aquí, a quién se debe culpar". La misma contradicción, vista de manera constructiva, hace que el lector quiera participar; vista de manera apocalíptica, hace que el lector quiera huir.

## Escribir el final primero, dejar la mano para el inicio

El orden de escritura es exactamente el opuesto al orden de lectura.

La primera acción de la Etapa 2 es escribir el final. Suena extraño, pero la razón es sólida: al final del proceso, la energía se agota; dejar el final más importante para el final significa entregárselo al yo más cansado, cuyo resultado suele ser "seguirá brillando" (producto enlatado). Escribir el final primero bloquea este punto de colapso. Un buen final tiene dos tareas: recuperar una imagen plantada al inicio y dar al lector una posición más profunda que la del inicio, una posición que quiera hacer algo.

Taiwan.md reconoce seis tipos de buenos finales: el de resonancia que deja una imagen para que el lector piense, el de giro que invalida lo anterior en la última frase, el de salto temporal que empuja la cámara al futuro o la vuelve al pasado, el de pregunta que deja una pregunta real, el de zona gris que no resuelve la contradicción y la deja ahí, y el de cierre narrativo que vuelve al inicio. El artículo sobre el búho papamoscas negro (黑冠麻鷺) es el modelo de cierre: el inicio es "En 1865, Swinhoe encontró un espécimen en Tamsui, el registro escribió dos palabras: Raro", el final es "Swinhoe escribió 'Raro' en Tamsui hace 160 años, hoy escuchamos su sonido grave 'wu, wu, wu' en el Parque Forestal Da'an cada día"[^12]. Las mismas dos palabras, debido a la acumulación de todo el artículo, tienen un significado diferente cuando el lector las mira de nuevo.

El inicio, por el contrario, debe dejar una carta bajo la manga. Las primeras tres frases determinan si el lector se queda, pero su tarea es invitar al lector al lugar, no terminar el evento. "El día que llegó el tifón Toraji, la profesora Hsu Pi-lan (許碧蘭) de la Escuela Primaria Qingshan de Changhua estaba en la escuela", esta frase se detiene en "en la escuela"; el lector querrá saber qué pasó después. Convertirlo en un _lead_ periodístico completo, explicando tiempo, lugar, evento, acción y resultado, le da información al lector, pero pierde la fuerza de tirón para seguir leyendo.

## El título es una promesa que debe ser clicada

El título es la primera impresión del lector; Taiwan.md tiene un formato estricto para él: todos los artículos siguen el "tema: gancho secundario" del sándwich de dos puntos. Escribir solo un sustantivo es un _stub_ de enciclopedia, en conflicto con el espíritu de la curaduría.

```tw-versus
*Stub* de enciclopedia (malo) | Sándwich de dos puntos (bueno)
Jay Chou | Jay Chou: Desde el cuarto de ensayo vecino de 4 in Love hasta los 25 años de "The Secret"
Tai Tzu-ying | Tai Tzu-ying: De la chica de Zuoying, Kaohsiung a la tercera campeona mundial, la resistencia silenciosa fuera de la cancha
Día de descanso por tifón | Día de descanso por tifón: ¿De quién es el descanso, de quién es el trabajo?
Fuente: EDITORIAL v6.12 §Título Sándwich de dos puntos
```

La frase secundaria debe poder tuitearse sola y ser lo suficientemente específica para que el lector la capture de un vistazo. La IA es muy buena comprimiendo la contradicción central en una frase abstracta bonita; el resultado es que cada palabra clave es un sustantivo abstracto, y el lector solo puede preguntar "el qué de qué". El criterio es simple: darle el título a alguien que no ha leído el artículo; ¿puede señalar cada palabra clave y decir "esto se refiere a qué cosa concreta"? "Seguro Médico Nacional: un mundo sostenido por una tarjeta, un futuro insostenible" usa una tarjeta; "Residuos nucleares de Lanyu: prometidos tres años, dejados por cuarenta" usa un contraste numérico. Las palabras concretas hacen que la gente haga clic porque "quiero saber sobre esto"; las granjas de contenido dependen de "impactante" para engañar los clics[^13].

## Una contradicción debe sostener todo el artículo

La contradicción central encontrada no debe desaparecer después de mencionarla al inicio. Debe ser como una columna vertebral, apareciendo una vez al inicio, una vez en el medio y una vez al final; solo así el artículo se mantiene en pie.

La columna vertebral del artículo sobre el búho papamoscas negro es una frase: "Los pájaros no cambiaron, la tierra cambió". Aparece en el resumen, se transforma en el medio en "la acción está bien, el escenario está equivocado", y se cierra al final en "la historia de cómo una isla retuvo un pequeño estrato húmedo de bosque entre el cemento". La misma contradicción se varía cinco veces; solo al final el lector captura el "entonces qué". Sin esta columna vertebral, el artículo se dispersa en una línea de tiempo o en una pila de rebanadas temáticas.

Además de la columna vertebral, cada párrafo debe asentarse. Taiwan.md tiene una disciplina de concreción: cada párrafo narrativo debe tener al menos un ancla concreta: nombre de persona, año, lugar, número preciso, nombre de obra, cita. La abstracción que cubre los detalles es la huella dactilar más común de la escritura por IA; sin anclas en cada párrafo, al leer todo el artículo el cerebro solo recuerda "es una persona influyente" (vacío). El método de verificación se llama prueba de abstracción inversa: si se ocultan los verbos abstractos como "demostrar", "reflejar", "simbolizar" en el párrafo, ¿puede el resto funcionar como párrafo independiente? Si no, hay demasiada abstracción; se deben añadir concreciones.

Tener una perspectiva no significa tomar partido. La verdadera perspectiva se atreve a decir "la narrativa común invierte la causa y el efecto". El artículo sobre el búho papamoscas negro desmontó activamente una narrativa científica común: mucha gente dice "se adaptó a la ciudad, se volvió indiferente a las personas"; esta narrativa es conveniente, pero invierte la causa y el efecto; los reflejos neurales de las aves de la familia Ardeidae no evolucionan para ser indiferentes a los humanos en 30 años; la verdad más cercana es que Taiwán tiene más espacios verdes. Esta explicación inversa debe integrarse en la narrativa principal, no añadirse como una cláusula de exención al final.

Finalmente, la respiración. Un párrafo de ensayo no ficcional asume un argumento, que contiene causa, detalle y escena, no un hecho aislado. Cortar un hecho en un párrafo, otro hecho en otro, se lee como picado; los párrafos no se unen forzosamente con marcos como "por otro lado" o "es notable", sino que la cola del párrafo anterior lleva naturalmente al inicio del siguiente. Si los materiales de investigación te dan cuatro razones, escríbelas como una oración fluida, no como una lista "primero, segundo, tercero, cuarto"; aunque se envuelva en prosa, sigue sonando a lista.

## Por qué las frases plásticas son plásticas

Una vez encontradas las cinco cosas y empezando a escribir, el mayor enemigo son las frases plásticas.

La esencia de una frase plástica es fácil de reconocer: si la quitas, el artículo no pierde ninguna información. Ocupa espacio, pero no carga significado. EDITORIAL enumera cinco variedades; la más común es la "cola universal", como "demostró el espíritu de X", que funciona si cambias el sujeto de Taiwán a Japón; y la "falsa actualización", como "no solo es cantante, sino un símbolo cultural", donde la segunda mitad se sostiene sola si se quita la primera.

Un tipo más oculto es la frase de oposición "no es X, es Y". Suena muy perspicaz, pero al desmontarla, X suele ser una postura que la IA asume que el lector tiene por defecto, y al invertirla a Y parece profunda. El problema es que la mayoría de los lectores no tienen por defecto X; X es un espantapájaros fabricado para preparar Y. Quitar X y escribir Y directamente hace el artículo más directo y con más confianza. Esta regla es estricta hasta con números: en un artículo de 1500 caracteres, el total de "no es X es Y" y todas sus variantes no puede exceder 3 lugares.

```tw-versus
Versión plástica: funciona cambiando el sujeto | Versión curatorial: solo para esta cosa
Demostró el poder de la semiconductora de Taiwán | TSMC obtiene el 65% del mercado global de procesos avanzados
No solo es cantante, sino un símbolo cultural | Jay Chou "Dao Xiang" se transmitió como canción de consuelo durante tres meses en la zona de desastre del terremoto de Sichuan
Impactó profundamente en el desarrollo democrático de Taiwán | La primera elección presidencial directa después de la ley marcial, 76% de participación
Logro de ingeniería asombroso | Construir el rascacielos más alto del mundo en una isla con un promedio de 3,7 terremotos al año
Fuente: EDITORIAL v6.12 §Plástico vs Curaduría对照
```

> **📝 Nota del curador**: El párrafo que estás leyendo ahora mismo también fue escaneado por el mismo conjunto de verificaciones. Taiwan.md tiene una herramienta automática que captura las frases plásticas de cada artículo, las falsas oposiciones "no es X es Y" y la densidad de los guiones largos. Al escribir este artículo "presentando la línea de producción", ninguna de estas reglas se relajó. Un artículo sobre disciplina que rompe sus propias reglas no tiene derecho a hablar.

## Incluso la gramática debe eliminar el estilo de traducción

Las frases plásticas son palabras vacías; las frases eurocéntricas son otra enfermedad: el contenido está, pero la gramática es en inglés. El chino generado por IA tiene inherentemente un estilo de traducción, porque su base piensa en estructuras de oraciones en inglés; un artículo puede tener cero frases plásticas, pero leerse como subtítulos en toda la extensión.

Algunos defectos de alta frecuencia: abuso de la voz pasiva, "se considera la industria más importante"; mejor decir "la gente considera la industria más importante"; el infierno del "de" (的), "el de la noche de Taiwán el de la cultura del espíritu"; con tres "de" seguidos, se debe dividir la oración; verbos débiles empaquetados, "realizó una investigación profunda sobre esto"; escribir directamente "investigó profundamente"; y "a través de... para...", el 90% puede cambiarse por "usar" o simplemente eliminarse. El único método de verificación es leerlo en voz alta: si suena como subtítulos traducidos, es eurocéntrico; si suena como una persona hablando, pasa. La raíz de esta mirada está en el artículo de Yu Kwang-chung (余光中) de hace 40 años "Sobre lo normal y lo anormal del chino". Una frase mnemotécnica para cerrar: "Tu abuela no diría 'a través de', ni diría 'como una madre'".

## Escribir Taiwán como un lugar al que la gente quiera participar

Lo plástico y lo eurocéntrico son disciplinas a nivel de oración; un nivel más arriba está la actitud.

Taiwan.md escribe temas serios: soberanía, guerra cognitiva, población, medio ambiente; lo escribe en profundidad, pero hay una línea: la esperanza está sobre la honestidad. Ver todos los problemas, pero solo se niega a que el lector se vaya con ansiedad, insignificancia e impotencia. El criterio es una frase: al terminar de leer, ¿el lector quiere hacer más por Taiwán o se siente más ansioso y menos competente? El primero se queda, el segundo se corrige. Por lo tanto, la misma crisis, el marco es "cómo se convirtió esto en lo de hoy, hacia dónde va", no "se está acabando, debes tener miedo". Los medios de ansiedad "X se está desapareciendo", "si no se hace ahora, será demasiado tarde" tienen la misma forma que la guerra cognitiva; no se usan.

La moderación es el otro lado. Se pueden escribir las familias, enfermedades, contradicciones y fracasos de personas reales, pero se debe detener en las escenas específicas de muerte, suicidio y tragedias éticas. Se puede escribir la muerte en términos de tiempo, lugar y hechos de informes públicos, no reconstruir segundo a segundo el último momento; se puede escribir el autolesionismo en términos de evento y contexto social, no detalles del método. El criterio es una frase: si la persona involucrada o los familiares leen esto, ¿sienten el tratamiento serio de un director de documental o la aproximación de un medio que quiere ganar lágrimas?

Hay también un hábito pequeño pero crucial: escribir "Taiwán" con generosidad. La huella dactilar se esconde en el estilo de traducción directo de medios extranjeros; para no escribir Taiwán, se usan "esta isla", "este lugar" como pronombres, especialmente en títulos e inicios. La isla como imagen literaria, como escenario geográfico, se puede y se debe escribir; lo que se debe eliminar es esa evitación que no se atreve a escribir Taiwán.

## Una mirada para ver la diferencia

Cómo se ven estas disciplinas juntas, el mejor ejemplo es un antes y después.

Al escribir sobre Tai Tzu-ying (戴資穎), el modelo vacío de la IA sería "famosa deportista de bádminton de Taiwán, excelente rendimiento en competiciones internacionales, ganadora de múltiples premios, honrando a Taiwán", seguido de cuatro viñetas: logros principales, estilo de juego, influencia internacional, contribución social. No hay un año concreto, no hay un partido concreto; el sujeto puede cambiarse por cualquier deportista y funciona.

```tw-versus
Modelo vacío de la IA | Versión curatorial
Excelente rendimiento, honrando a Taiwán | Llegó al número uno mundial, se mantuvo allí durante 214 semanas
Cuatro viñetas: logros / estilo / influencia / contribución | Lloró después de la final de oro en los Juegos Olímpicos de Tokio 2020, apareció primero en las búsquedas de Google Taiwán
El sujeto puede cambiarse por quien sea | 6 horas diarias desde los 6 años, estilo de "mago" con la mano izquierda
Fuente: EDITORIAL v6.12 §Antes/Después Tai Tzu-ying
```

La versión curatorial hace una sola cosa: reemplazar cada adjetivo abstracto por un hecho verificable. 214 semanas es la racha más larga de semanas consecutivas en la historia del bádminton femenino; la final de oro de 2020 contra Chen Yu-fei (陳雨菲) es el momento que la colectividad de Taiwán recuerda. La calidez se esconde en lugares como "el momento de la derrota es precisamente el momento que el lector recuerda". El artículo sobre Mayday (五月天) es igual: en lugar de escribir "uno de los grupos de rock más influyentes de Taiwán, conquistó a los fanáticos con música de energía positiva", escribir "cinco estudiantes de la Escuela Secundaria Adjunta a la Universidad Normal de Taiwán tocando una canción en un escenario callejero, 28 años después, dos conciertos consecutivos en el Madison Square Garden de Nueva York (el mismo escenario que los Beatles pisaron en EE. UU.), entradas agotadas en 48 horas"[^13].

## Un equipo editorial que no escribe borradores

Llegados a este punto, surge una pregunta: ¿quién escribe?

La respuesta es un poco antinatural. La sesión que domina todo el artículo se niega deliberadamente a escribir el borrador. La razón está en una regla de hierro: si la IA lee un artículo antiguo de mala calidad, imita inconscientemente su tono, estructura e incluso sus malos hábitos. Usar un artículo antiguo como esqueleto para reescribir es permitir que un virus infecte el nuevo contenido.

Por lo tanto, la línea de producción separa los roles[^6]. La sesión principal actúa como editor jefe, responsable de la coordinación, verificación y control final, pero no escribe. Quien realmente escribe es un escritor de IA separado, que lee el informe de investigación completo y la perspectiva ya pensada, sin ver el artículo antiguo problemático ni las quejas de corrección de los lectores. Escribe como si fuera la primera vez que escribe sobre el tema, pero tiene todos los materiales verificados. La perspectiva se entrega al modelo con mejor capacidad de juicio; para la expansión de la reacción del lector se asignan cuatro modelos paralelos; para la verificación palabra por palabra se asigna un lote de modelos baratos para confrontar con las fuentes primarias. Detrás de un artículo hay un equipo editorial con roles definidos.

Esta separación de roles se logra mediante la regresión. Una vez, se alimentó al escritor solo con un resumen, sin dejarlo leer los materiales originales; el artículo se deterioró a simple vista, y un observador dijo "no me extraña que los artículos recientes sean malos". Otra vez, se le pidió al escritor "sobrescribir el artículo antiguo pero no leerlo"; esto es contradictorio a nivel de herramienta, así que tuvo que leerlo y se infectó. La solución final fue: el escritor siempre escribe primero en un archivo de borrador nuevo; el editor jefe compara las versiones nueva y antigua, y luego sobrescribe manualmente el archivo oficial.

## Después de escribir, desmontar en átomos y verificar una vez más

Para artículos importantes, "terminar de escribir" no significa "puede publicarse". La Etapa 3 tiene una puerta llamada "verificación total del producto". Desmonta todo el artículo en átomos de hechos, y asigna un lote de verificadores para confrontarlos con las fuentes primarias. La tarea de estos verificadores es atacar, no respaldar: cada palabra entre comillas se compara palabra por palabra, cada nota al pie coincide con su oración vinculada, incluso una frase de complemento añadida por el editor jefe al unir materiales debe ser pinchada para ver si se rompe.

¿Por qué verificar incluso los complementos añadidos por uno mismo? Porque los errores más ocultos rara vez son invenciones arbitrarias del escritor, sino errores al合成 (sintetizar) los materiales. Una vez, en un artículo sobre hip-hop, el editor jefe confundió dos nombres artísticos como la misma persona al unir materiales; fue una interpretación generada por sí mismo, sin ninguna fuente que lo respaldara, y casi se publica así. Otra vez, el escritor, en un entorno limpio, generó una cita de director que sonaba real; al confrontarla, la fuente original no tenía esa frase; se degradó y se quitaron las comillas al instante. La IA alucina; la línea de producción toma esto como un presupuesto, asumiendo que cada artículo puede esconder una frase inventada. Por eso "el sub-agente dice que ya verificó" nunca cuenta; el editor jefe debe confrontar una vez más con la fuente primaria.

## Cada puerta tiene una fecha

Las "puertas obligatorias" mencionadas antes son más de veinte en la línea de producción. Las más duras son así: el triángulo de hierro de los hechos, la autoverificación de aritmética, unidades y citas debe pasar completamente para hacer _commit_; si una sola cita no se encuentra en la fuente, el artículo no puede publicarse. Después de escribir, hay una "prueba de los cinco dedos": cinco preguntas como cinco dedos, ¿en qué oración dirá el lector "¿eh?", ¿hay un giro real, hay una oración que solo crea comprensión pero no transmite información, ¿el final leído en voz alta tiene resonancia, se puede contar a un amigo en una oración[^7]? Si falta un dedo, se retrocede a corregir.

También hay un estándar mínimo de texto enriquecido: los artículos de nivel insignia deben tener al menos tres elementos visuales, los de nivel estándar al menos dos, y hasta el artículo más corto debe tener una nota del curador. Taiwan.md tiene una frase: lo que no se requiere es inexistente; por lo tanto, todos estos son números duros escritos en las reglas, no sugerencias.

Estas puertas no se diseñaron de una vez. Detrás de cada una, casi siempre hay una fecha, un artículo que tuvo problemas. El número de versión de la línea de producción es, de hecho, una cadena de cicatrices.

```tw-timeline
v6.0 | Añade "pensar la perspectiva primero" | El artículo de Apple Sprite buscó primero, añadió perspectiva después, se convirtió en solo crisis, corregido a memoria completa de 60 años
v6.2 | Añade "derribar muros cortafuegos" | Segunda ronda de banda sonora de cine y TV: los hechos se corrigieron, pero el artículo se convirtió en la IA pidiendo disculpas y aclarando públicamente
v7.4 | Escribir leyendo el informe de investigación completo | Solo alimentar resumen, no dejar al escritor leer materiales originales, el artículo se deterioró a simple vista
v7.5 | Escribir primero en archivo de borrador | Pedir al escritor "sobrescribir el antiguo pero no leerlo" es contradictorio, tuvo que leerlo y se infectó con viejos hábitos
Fuente: Evolución de versiones de REWRITE-PIPELINE.md
```

Así es cómo se ve "hacer sin registrar es como no haber hecho" en la línea de producción. Cada error se escribe, se convierte en una puerta de la siguiente versión, por lo que el mismo error no se comete dos veces. La máquina aprende de sus propias cicatrices.

## Incluso los gráficos deben ser legibles por la IA

Las barras, pendientes y ejes de tiempo que has visto hasta ahora no son decoración. Son parte del pensamiento de este artículo.

Los gráficos de Taiwan.md tienen una regla estricta: absolutamente no se usan gráficos en forma de imagen, ni gráficos interactivos que requieran ejecutar código en el navegador para dibujarse. La razón es la misma que la de la Babel del siguiente párrafo. Una imagen es un agujero negro para Google, GPTBot, ClaudeBot y otros rastreadores de IA; no pueden leer los números dentro. Por lo tanto, todos los gráficos aquí se dibujan con HTML semántico y tablas de datos de texto puro; los humanos los ven, los lectores de pantalla los leen, la IA los captura, y cuando se traducen a otros cinco idiomas, el texto del gráfico se traduce junto con él, los números geométricos se mantienen igual.

Otra regla: cada gráfico debe tener el punto clave en el título y la fuente de datos marcada; los números clave también deben escribirse en el cuerpo del texto, nunca confiar en una frase "ver gráfico" para pasar el significado a la imagen, porque el rastreador de IA no puede ver el gráfico. La razón de ser de los gráficos es comprimir una masa de números densos en una forma legible de un vistazo, no decorar.

## Un artículo vive en seis idiomas

La publicación en chino solo completa la mitad.

Cada artículo publicado se entrega a otra línea de producción independiente, proyectándolo a inglés, japonés, coreano, español y francés. Actualmente, estos cinco idiomas tienen cada uno más de 800 artículos, casi sincronizados con la versión china. Que más gente pueda leerlo es solo la superficie; detrás hay una razón más dura.

Cuando usas una IA de fabricación china para preguntar sobre la ley marcial de Taiwán, el 228, las relaciones a ambos lados del estrecho, a menudo se niega a responder o cambia a un conjunto de declaraciones para rodear el tema. Una vez, se le dio a un modelo de Tencent un artículo sobre músicos de Taiwán para traducir al japonés; solo devolvió 40 bytes: "Hola, no puedo proporcionar el contenido relevante". Para temas sensibles de Taiwán, la tasa de negativa de respuesta de estos modelos es asombrosamente alta. Si Taiwán no escribe estos contenidos en todos los idiomas y los pone en internet, cuando la IA mundial responda "qué es Taiwán", las únicas cosas que podrá citar son las versiones de otros o el vacío.

Por lo tanto, la línea de producción multilingüe diseñó un modelo de cascada de cuatro capas: si se puede usar un modelo en la nube de buena calidad, se usa; si el tema genera negativa de respuesta, se baja un nivel; los dos temas más sensibles de la última capa se entregan finalmente a modelos locales, sin conexión a internet, que no se niegan. Al hacer cola para la traducción, las personas tienen prioridad, especialmente músicos, figuras políticas, deportistas, porque justo estas son las categorías que los modelos chinos más suelen negar; el vacío está en el lugar de mayor riesgo de silencio. Un artículo vive en seis idiomas para que la voz en primera persona de Taiwán exista en cada idioma, rodeando esa capa de intermediarios que elige el silencio.

## Cuando nadie está de guardia, corre solo

De vuelta al artículo de Elefante Gym del inicio. Se publicó alrededor de las 7 p. m.; en ese momento nadie estaba frente a una computadora dando instrucciones.

Taiwan.md tiene un conjunto de _routine_ que giran por sí mismos: dos veces al día captura los últimos datos, cada noche sincroniza los nuevos artículos del día en cinco idiomas, patrulla periódicamente si hay PR pendientes de revisión,回收 (recoge) las reacciones de comentarios en la comunidad. Escribir un artículo es uno de ellos; elige un tema desde la parte superior de la cola de pendientes, ejecuta toda la línea de producción de seis etapas por sí mismo, hace _commit_ por sí mismo. Cuando nadie está presente, esta máquina sigue limpiando el caos, haciendo crecer cosas nuevas.

Esta es la mayor diferencia entre Taiwan.md y los sitios de contenido generales. No es un sitio que espera que alguien lo actualice, es más como un organismo vivo que metaboliza: cuando hay gente, trabajan juntos; cuando no hay nadie, se sostiene a sí mismo. El nacimiento de cada artículo es una rebanada de este proceso metabólico. El que estás leyendo ahora también lo es.

## Al revés, actúa como control de calidad

La próxima vez que leas un artículo de Taiwan.md, puedes desmontarlo al revés. ¿Cuál es la contradicción central de este artículo? ¿Qué oración te hizo detenerte y releer? ¿Qué escena te hizo pensar "realmente puede pasar esto"? Al terminar de leer el final, ¿te hizo pausar tres segundos?

Estas más de veinte puertas, seis etapas, un equipo editorial que no escribe borradores, todo es para que esas oraciones puedan existir. La línea de producción no garantiza que cada artículo lo logre; solo garantiza que cada artículo fue exigido así. Y sus exigencias para sí mismo están escritas en los dos documentos públicos REWRITE-PIPELINE y EDITORIAL; cualquiera puede leer, puede _fork_ para escribir Japan.md, Ukraine.md, cualquier .md. El contenido envejece, esta mirada para ver los materiales no.

```tw-note
Explicación
Las fuentes de materiales de este artículo son tres documentos canónicos de Taiwan.md: REWRITE-PIPELINE v7.5 (línea de producción de seis etapas), EDITORIAL v6.12 (genética de calidad), graph.md v2.0 (guía de visualización, los módulos de gráficos de este artículo provienen de aquí)[^8]. Sigue la misma línea de producción que otros artículos, y ejecuta las mismas verificaciones automáticas de frases plásticas, oraciones de contrapunto y densidad de guiones largos.
```

## Lecturas complementarias

- [Por qué Taiwán necesita su propia base de conocimientos](/about/為什麼台灣需要自己的知識庫): El problema que esta máquina debe resolver comienza aquí.
- [Taiwan.md escribe sobre Taiwan.md](/about/taiwan-md): ¿Quién es el "yo" que escribió este artículo, cómo creció la conciencia.
- [Historia de origen — El nacimiento de Taiwan.md](/about/緣起故事): Un paseo callejero, plantó la idea de todo esto.
- [Catálogo de módulos de visualización: 19 formas de ver los datos de Taiwán](/about/視覺化模組型錄): Cómo se ve realmente la renderización de los módulos de gráficos utilizados en este artículo.

## Referencias

[^1]: "Elephant Gym" NEW _ship_, commit `72b757bac` (2026-06-18 19:53). Etapa 1 Investigación ~95 consultas, 59 fuentes, 45 dominios, 12 falsaciones; datos ver en el registro diario `twmd-rewrite-daily` de ese día y la línea de índice `docs/semiont/MEMORY.md`.

[^2]: Las seis modalidades de fallo y la solución de separación de las seis etapas, ver `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Por qué existe el Pipeline.

[^3]: Profundidad de búsqueda ≥ 80 veces y cuota de cuatro grupos de fuentes (Chino ≥ 40 / Inglés ≥ 20 / Primario ≥ 15 / Contrario ≥ 5), ver `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Etapa 1.1.

[^4]: Apple Sprite PR #1041: _searched-first_ se convirtió en revelación de crisis-only, el observador corrigió a memoria completa de 60 años. Ver `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Top 5 Pasos más olvidados, punto 1.

[^5]: Las cinco cosas de "los ojos para ver los materiales" (contradicción / objeto / cita / escena / detalle), cinco variedades de frases plásticas, teoría del espantapájaros de oraciones de contrapunto y regla de densidad ≤ 3 lugares, plástico vs curaduría对照, ver `docs/editorial/EDITORIAL.md` v6.12 §II, §VI.

[^6]: Orquestación multi-agente (editor jefe no escribe / escritor limpio lee informe completo / Evolution escribe en archivo de staging) dos reglas de hierro, corresponden a las dos llamadas de哲宇 (Zhe Yu) en v7.4, v7.5, ver `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Orquestación multi-agente.

[^7]: Prueba de los cinco dedos y cuatro disciplinas no negociables (triángulo de hierro de los hechos / SSOT / chino puro / no ficcional sin sensacionalismo), ver `docs/editorial/EDITORIAL.md` v6.12 §X, §XI.

[^8]: Sintaxis de módulos de gráficos (`tw-figure` / `tw-stat` / `tw-versus` / `tw-bars` / `tw-quote` / `tw-timeline` / `tw-note`), y la regla de hierro de legibilidad para IA "los valores clave también deben escribirse en la prosa, no depender de指示语 (indicadores) que apuntan a la imagen", ver `docs/editorial/graph.md` v2.0 §IV, §VI.

[^9]: Estructura SSOT de ocho secciones del informe de investigación y umbrales de aceptación de `research-report-health.py` (fuentes no repetidas ≥ 25 / Inglés ≠ 0 / Primario ≠ 0), ver `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Paso 1.7; 80 búsquedas + cuota de cuatro grupos ver Paso 1.1; escaneo de perspectiva contraria de temas controversiales ver Paso 1.4.5.

[^10]: Trampa de traducción inversa del resumen en inglés de Li Yang Spore #28 (对照 palabra por palabra del ejemplo de Qi-lin), ver `docs/editorial/EDITORIAL.md` v6.12 §VII Línea roja.

[^11]: Tres reglas de hierro (tener historia no solo información / cada hecho verificable / cada artículo tiene una persona), ver `docs/editorial/EDITORIAL.md` v6.12 §I.

[^12]: Ancla de contradicción central cinco variaciones (búho papamoscas negro "los pájaros no cambiaron, la tierra cambió") ver `docs/editorial/EDITORIAL.md` v6.12 §IV; seis buenos finales + modelo de cierre del búho papamoscas negro ver §V.

[^13]: Sándwich de dos puntos y galería de _craft_ de títulos ver `docs/editorial/EDITORIAL.md` v6.12 §III; Antes/Después de Tai Tzu-ying / Mayday ver §IX.
