---
title: 'Pagos móviles en Taiwán: ¿Por qué la gente sigue llevando efectivo aunque tenga varios métodos de pago en el móvil?'
description: 'En la tercera temporada de 2024, un estudio de muestra web de MIC (Taiwan Economic Research Institute) mostró que el 92% había usado y el 84% usaba pagos móviles. Sin embargo, otra encuesta nacional del Banco Central indicó que el 73.8% aún mezcla efectivo y no efectivo. Este artículo desglosa las herramientas, contratos y procesos de confirmación detrás del pago con móvil, respondiendo por qué la alta adopción no implica la eliminación total del efectivo.'
date: 2026-09-01
category: 'Technology'
tags:
  [
    'Pagos móviles',
    'pagos electrónicos',
    'TWQR',
    'Pay en Taiwán',
    'Código QR',
    'Efectivo',
    'tecnología financiera',
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
translatedAt: '2026-09-13T00:44:01+08:00'
---

# Pagos móviles en Taiwán: ¿Por qué la gente sigue llevando efectivo aunque tenga varios métodos de pago en el móvil?

![Tienda con terminal de pago móvil en una entrevista oficial de TWQR](/article-images/technology/taiwan-mobile-payments-merchant-2026.webp)
_Imagen de muestra de una tienda en una entrevista oficial de TWQR, utilizada solo para análisis promocional del sistema. La imagen representa únicamente a la tienda entrevistada y no debe considerarse evidencia de campo independiente sobre el uso en pequeñas tiendas de todo Taiwán. Imagen: Taiwan Financial Information Co., Ltd. (Sitio web oficial de TWQR), uso razonable en comentarios._

> **Resumen de 30 segundos:** En una muestra web realizada por MIC en la tercera temporada de 2024, el 92% había usado pagos móviles. Sin embargo, una encuesta encargada por el Banco Central mostró que el 73.8% de los adultos aún usa efectivo y no efectivo juntos. Los dos conjuntos de datos miden poblaciones y preguntas diferentes, pero ambos apuntan a lo mismo: usar el pago móvil, completar transacciones en cualquier lugar y no llevar efectivo con tranquilidad son tres umbrales distintos. Múltiples aplicaciones complementan las lagunas de infraestructura o ofrecen funciones de recompensas y membresía. TWQR está integrando un Código QR común, pero aún no ha consolidado todas las fuentes de fondos, los contratos comerciales y los escenarios de fallo en un único pago.

En septiembre de 2025, el analista sénior de la industria de MIC publicó una encuesta sobre consumidores de pagos móviles. Observó que los usuarios activos instalaban cinco o más herramientas "principalmente para poder usar pagos móviles en diferentes canales".[^1] Esta frase se asemeja a lo que mucha gente hace frente a una caja registradora: primero mira qué logotipos hay pegados en el cristal o el mostrador, y luego decide con qué aplicación desbloquear. Si no encuentra un logotipo familiar, levanta la vista y pregunta: "¿Aquí aceptan cuál?".

Hay cada vez más opciones en el móvil, pero todavía quedan algunos billetes en la cartera. Esta imagen coexistente se interpreta fácilmente como un mercado de pagos demasiado fragmentado en Taiwán, o también como una simple elección promocional. Ambas interpretaciones capturan parte de la verdad. La fricción del sistema para aceptar y ser interoperable hace que la gente instale muchas herramientas y conserve efectivo; las recompensas, membresías, transferencias, hábitos, preferencias personales y resiliencia ante fallos actúan simultáneamente. Para entender esto claramente, hay que desglosar los tres umbrales: si la persona lo adopta, si la transacción es genérica entre escenarios, y si se puede recuperar en caso de fallo para que el usuario no tenga miedo de dejar el último billete en casa.

## Usar el móvil no significa que hoy solo basta con llevar el teléfono

El 92% "haber usado" y el 84% "usar habitualmente", publicados por MIC, provienen de una muestra web de dos meses durante la tercera temporada de 2024. La página pública no enumera completamente el marco de muestreo, el rango de edad ni los métodos de ponderación; por lo tanto, estas dos proporciones solo pueden describir esa muestra web y no se pueden escribir directamente como la tasa de adopción de toda la población de Taiwán.[^2] Incluso manteniendo esta limitación, sí indica que dentro del grupo de consumidores que completan encuestas en línea, el pago móvil ha superado la etapa de tecnología desconocida.

Otra encuesta realizada por el Banco Central a través del Instituto Económico de Taiwán preguntó cómo usan los ciudadanos mayores de 18 años el efectivo y lo no efectivo en su vida diaria. La encuesta se centró en dialectos locales, teléfonos móviles y complementó con internet, abarcando 22 municipios, y ponderó según la estructura demográfica, resultando en una muestra efectiva de 4,234 respuestas. El resultado fue que el 73.8% usa efectivo y no efectivo simultáneamente, el 25% solo usa efectivo y solo el 1.2% solo usa lo no efectivo.[^3] Aquí, "lo no efectivo" incluye tarjetas de crédito, tarjetas financieras y tarjetas recargables; esto no puede usarse como cuota de mercado del pago móvil, pero es adecuado para describir la forma de la cartera actual.

```tw-waffle
La mezcla es el día a día de la mayoría (%)
Usa efectivo y lo no efectivo | 73.8
Solo usa efectivo | 25
Solo usa lo no efectivo | 1.2
Fuente: Encuesta de herramientas de pago encargada por el Banco Central, publicada en 2024
```

Por lo tanto, no hay contradicción en que alguien use la detección móvil en una cafetería de cadena por la mañana, escanee un código para acumular puntos durante el almuerzo y pague con efectivo en el mercado por la tarde. Ha superado el primer umbral de "la gente usa", pero aún debe cambiar de herramienta según el lugar, la tienda y el equipo. El "sigue llevando efectivo" del título solo puede entenderse como una reserva para escenarios a gran escala, no como algo necesario para cada taiwanés todos los días.

Los hábitos de pago han cambiado, pero las excepciones de escenario siguen en la carretera. Instalar varias aplicaciones parece rellenar todas las excepciones, pero para entender por qué lo hacen, primero hay que reconocer que esas aplicaciones no son cosas iguales. El momento en que abres el móvil es similar, pero el camino que sigue la transacción puede ser completamente diferente.

## Varios apps parecen pagar, pero siguen caminos distintos detrás de escena

El manual del Ministerio de Finanzas clasifica los pagos móviles por herramientas vinculadas, tecnología y regulaciones aplicables: tarjetas de crédito móviles, tarjetas financieras móviles, escaneo de códigos QR, instituciones de pago electrónico y vales electrónicos.[^4]

Lo que el consumidor hace en la parte frontal puede ser solo un toque, un escaneo o una confirmación; pero lo que sucede en la parte trasera puede estar completado por diferentes herramientas vinculadas, tecnologías, puntos de cobro y reglas. Aunque paguen con el móvil, algunos utilizan tarjetas vinculadas y otros utilizan cuentas de pago electrónico. El punto de cobro y las especificaciones aceptadas por la tienda determinarán qué combinaciones son utilizables. Por lo tanto, LINE Pay, Street, Apple Pay, Chunghwa Payment y Taiwan Pay no pueden ser solo cinco carteras homogéneas representadas por su logotipo. Algunos compiten entre sí, algunos cooperan en capas dentro de una misma transacción, y otros complementan diferentes canales.

Para ver cómo plataformas como PChome, Shopee y Coupang cambian el escenario de compras en línea, puedes leer más sobre [Ecosistema de comercio electrónico y pagos digitales en Taiwán](/es/technology/e-commerce-and-digital-payment-ecosystem). Este artículo solo se centra en la última milla del pago físico.

Así que, si un móvil tiene una marca, solo responde si el usuario ha obtenido la herramienta; no puede responder directamente si la tienda acepta el punto de cobro compatible. Ver el mismo Código QR no significa que todos los tipos de aplicaciones, direcciones de escaneo y fuentes de fondos puedan completar la transacción. Al saltar directamente desde el icono del móvil a "disponible en todo Taiwán", se omiten al menos tres capas: las herramientas vinculadas, los contratos comerciales y las especificaciones de la transacción.

La cantidad de aplicaciones también necesita corregirse respecto a la exageración de "promedio de cinco". La muestra web de MIC de 2024 mostró que el 86% usa cinco o menos, del cual el 61% usa tres o menos, y el 14% usa seis o más. Los datos públicos no proporcionan promedios ni medianas, ni la distribución completa de una a cinco aplicaciones.[^5] Esto soporta el uso múltiple, pero no puede crear un "usuario típico" que tenga exactamente cinco.

La tabla mensual del Ministerio de Finanzas de junio de 2026 suma los registros de instituciones de pago electrónico a 41.129 millones. Esta es una suma total de instituciones, no la cantidad natural después de desduplicar entre instituciones. Mide una instantánea contractual y no puede responder cuántas herramientas tiene un usuario típico.[^6]

> **📝 Nota del curador**
> El logotipo en el mostrador es la marca; lo que se muestra en el móvil es la interfaz; lo acumulado en la tabla del Ministerio de Finanzas son contratos de cuentas pendientes. Llamar a estos tres "número de usuarios" aplasta el nivel más importante para entender el mercado de pagos.

La apariencia frontal es similar, pero las diferencias surgen cuando la transacción llega al otro extremo. Por mucho que un usuario descargue aplicaciones, no puede completar la solicitud, confirmación y conciliación por la tienda. El segundo umbral está detrás del mostrador.

## Lo que ve el consumidor es un escaneo; lo que debe armar la tienda es todo el proceso

Para aceptar Taiwan Pay, una tienda debe solicitar primero a la institución financiera de cobro que se convierta en una tienda con contrato, obtener el código de la institución receptora, el código de la tienda y el código del terminal, y completar el registro del servicio.[^7] Una vez iniciado el cobro, el equipo y la red deben funcionar; el dependiente debe saber cómo confirmar la notificación, procesar devoluciones y realizar la conciliación en segundo plano. Para las pequeñas tiendas, mostrar el código de pago es solo el comienzo, seguido de un proceso operativo que debe cerrarse a diario.

La sección de preguntas frecuentes (FAQ) de Taiwan Pay describe con gran detalle el momento más fácil de ser cubierto por un Código QR: cuando el dispositivo está fuera de línea, la tienda aún puede generar un Código QR sin monto en la página de inicio para que el consumidor lo escanee, pero el móvil de la tienda no recibe la notificación de transacción.[^8] La pantalla del cliente muestra que se ha pagado, pero el punto de cobro carece de notificación inmediata; por lo tanto, la caja debe decidir si liberar el producto o dónde verificar esa transacción. El escaneo es solo el punto de partida; la confirmación en el momento y la conciliación posterior son lo que hace que la transacción realmente se concrete.

Taiwan Pay fija las tarifas mediante un contrato entre la tienda y la institución receptora; la explicación oficial es que "la tarifa de procesamiento de transacciones se establece según el contrato mutuo entre la tienda (receptor) y la institución receptora (banco)". Las soluciones públicas, las negociaciones de cadenas comerciales y las diferentes fuentes de pago de otras plataformas tienen sus propios términos.[^9] La comisión entra en la decisión de la tienda; el tiempo de desembolso, las devoluciones, la red, el equipo, el cliente, el aprendizaje y la conciliación también influyen.

Un estudio académico sobre tiendas del distrito comercial de Tainan descubrió incluso que la usabilidad percibida, la facilidad de uso, la adopción por parte del consumidor, la compatibilidad y la disposición a adoptar están correlacionadas positivamente, mientras que el costo percibido no mostró una relación significativa en esa muestra.[^10] Esto también indica que las tiendas no solo asumen costos, sino que también evalúan si la herramienta es útil y si el cliente ya la ha adoptado. Este estudio local no se puede extrapolar a todo Taiwán, pero sí evita la única explicación de "la tienda no cobra por la tarifa".

La encuesta encargada por el Banco Central dio una magnitud al diferencial de aceptación. De 611 muestras de vendedores ambulantes, el 76.1% solo acepta efectivo. De 1,436 muestras de tiendas, esta proporción es del 46.8%. El informe relaciona la mayor proporción de los vendedores con el lugar, el equipo y la escala.[^11] Aquí, "solo acepta efectivo" se refiere a todos los métodos no efectivos; no puede extrapolarse como tasa de aceptación de pagos móviles ni usarse para criticar al vendedor por falta de voluntad de mejora.

```tw-bars
Condiciones de aceptación en puestos y tiendas (solo efectivo, %)
Muestra de vendedores | 76.1 | 611 muestras
Muestra de tiendas | 46.8 | 1,436 muestras
Fuente: Encuesta de herramientas de pago encargada por el Banco Central, publicada en 2024
```

La universalidad del pago debe ser completada por ambos lados: el consumidor tiene la herramienta y la tienda tiene un proceso continuo para cobrar, confirmar, reembolsar y conciliar. La fricción del sistema aquí ya tiene una forma, pero solo explica parte de la coexistencia de múltiples aplicaciones y efectivo. El siguiente tipo de aplicación es a veces un repuesto, y otras veces parece más una tarjeta de membresía.

## Instalar otra app: A veces para poder usarla, otras veces por querer mejorar

En la encuesta del Banco Central sobre las dificultades con los pagos móviles, el 18.9% eligió que la tienda no lo aceptara, el 12.0% eligió que la tienda no aceptara su herramienta habitual, y solo el 7.6% fue porque había demasiados tipos en el mercado. La mala señal de red representó el 6.5%, y la batería baja del móvil el 3.4%.[^12] Estas son autodeclaraciones múltiples y no pueden ser proporciones causales para las transacciones en efectivo, pero sí muestran que existe una brecha entre "tener una aplicación" y "esta aplicación funciona".

El "diferente canal" mencionado por Hu Zili corresponde exactamente a este motivo de complemento. Si una tienda no acepta la herramienta habitual, el usuario puede instalar otra. Para una reunión de amigos que requiere dividir cuentas o para un familiar que quiere transferir puntos como regalo, también se puede conservar otra opción. Una encuesta similar de MIC indicó que el 57% de los usuarios ha utilizado servicios financieros distintos del consumo; el más común es la división y transferencia de cuentas, con un 38%.[^13] Estas funciones hacen que las aplicaciones de pago entren en la vida social y de membresía, y la razón para tenerlas ya supera si la caja puede escanear o no.

En una investigación transregional encargada por Visa en 2022, se entrevistó a 1,000 participantes taiwaneses de entre 18 y 55 años; el 40% rastrea regularmente los puntos de consumo, y el 22% calcula meticulosamente para obtener la mejor recompensa.[^14] Estos datos no pueden estimar "cuántas personas instalan aplicaciones por las recompensas", solo muestran que algunos encuestados rastrean puntos y calculan ofertas por las recompensas. El ecosistema de membresía minorista también desarrolla sus propias herramientas de pago. Para ver cómo PX Mart pasa de la red de tiendas a una plataforma de vida de alta frecuencia, consulta [PX Mart Welfare Center](/es/economy/pxmart-supermarket); aquí no se reescribe la historia corporativa ni las controversias.

La encuesta del Ministerio de Economía sobre el sector minorista ofrece un cambio más largo. Calculando los montos de pago en la muestra que reportó, la proporción de uso de pagos móviles por parte del consumidor aumentó del 0.6% en 2017 al 11.2% en 2023, mientras que el efectivo bajó del 41.1% al 23.0%. El gobierno atribuye parcialmente este cambio en la venta minorista general y de productos farmacéuticos al ecosistema de membresía y a las herramientas de pago creadas por los propios comerciantes.[^15] La expansión de la proporción de pagos móviles coincide con la disminución de la proporción de efectivo. La competencia de múltiples marcas también crea opciones. Si solo se diagnostica el uso de múltiples aplicaciones como un fallo del sistema, esta trayectoria ascendente y la preferencia activa del usuario se omiten.

```tw-slope
Proporción del monto de pago minorista: Pagos móviles en alza, efectivo a la baja (%)
2017 | 2023
*Pagos móviles | 0.6 | 11.2
Efectivo | 41.1 | 23.0
Fuente: Oficina de Estadísticas del Ministerio de Economía, Encuesta sobre el estado operativo de la industria mayorista, minorista y de restaurantes
```

Los múltiples tipos de herramientas desempeñan dos roles: uno complementa las lagunas en aceptación y fuentes de fondos, y otro soporta descuentos, puntos, membresías y transferencias. La cantidad de aplicaciones por sí sola no puede medir la distancia a la adopción, la universalidad o el uso de efectivo. Una vez que la competencia y el complemento están entrelazados, el problema radica en qué nivel se ha logrado la integración.

## TWQR integra un Código QR común, pero no consolida todos los pagos en uno

TWQR es una respuesta sustancial a "demasiados estándares de pago y demasiadas pancartas comerciales". Este estándar de Código QR común conecta las instituciones financieras y las instituciones de pago electrónico participantes. A finales de 2025, los datos del Banco Central enumeraron 44 instituciones financieras, 10 instituciones de pago electrónico y 678,000 tiendas asociadas. En 2025, se realizaron 146.73 millones de transacciones por un total de 713.6 mil millones.[^16] "El pago QR en Taiwán no es totalmente interoperable" ya no refleja la realidad.

![Ilustración oficial del sistema de pago múltiple de TWQR](/article-images/technology/taiwan-mobile-payments-single-contract-2026.webp)
_Material promocional del sistema TWQR "Un contrato, pagos múltiples", que muestra el método de conexión de comerciantes alegado por Taiwan Financial Information Co., Ltd. Esta es una ilustración promocional del sistema y no puede probar independientemente la actividad de cada tienda asociada, el éxito de cada transacción o si todas las fuentes de pago son compatibles. Imagen: Taiwan Financial Information Co., Ltd. (Sitio web oficial de TWQR), uso razonable en comentarios._

El Código QR común resolvió un aspecto importante, pero la página de cobro de la cooperativa también muestra que hay límites. La lista de "escaneo principal" enumera 11 herramientas como Taiwan Pay, Street, Chunghwa Payment, YouYouFu e EasyCard. La lista de "escaneado" es más corta y está limitada por las especificaciones de QR Auth. Chunghwa Payment, AiJin Card y QuanYing Payment aparecen en la lista principal de escaneo, pero no están en la lista de escaneo de esa página.[^17] La dirección del escaneo, las especificaciones y la participación institucional cambian la combinación utilizable; las tiendas aún deben solicitar TWQR a la institución receptora.

Los 678,000 son el número de tiendas asociadas; los datos públicos del Banco Central no proporcionan cuántas de estas tiendas están activas continuamente ni qué porcentaje representa en todo el mercado o la tasa de éxito en el lugar. El Código QR común tampoco unifica automáticamente las fuentes de fondos como tarjetas de crédito o cuentas, los puntos de membresía, las recompensas, los contratos comerciales, las tarifas y los procesos de reembolso. Mueve las pancartas y las especificaciones de transacción hacia un nivel común, pero no borra el mundo comercial de cada aplicación.

> **📝 Nota del curador**
> El logro más digno de mención de TWQR se encuentra en el alcance de la palabra "común": el Código QR común y la información interinstitucional han formado una base a gran escala; la activación diaria de las tiendas asociadas, cada fuente de fondos y cada conjunto de reglas de membresía siguen siendo determinados por otros niveles. La universalidad se está construyendo capa tras capa.

El umbral de interoperabilidad ha avanzado, pero el número de tiendas asociadas no garantiza que todos puedan usarlo en cada transacción o con cada fuente de fondos. Mientras la ingeniería de integración sigue en curso, el efectivo tiene otra explicación.

## El efectivo no prueba un fallo del pago móvil; generalmente no se pregunta primero si es utilizable

Para que una herramienta sea universal, al menos debe ser obtenida por el usuario, reconocida y confirmada por la tienda, y completada la transacción; también debe haber un método de recuperación predecible en caso de batería baja, red inestable o fallo de notificación. Esto significa que ambas partes saben dónde consultar, cuándo reintentar y qué camino tomar después del fallo. La capacidad de ambas partes para verificar el mismo registro después de completar la transacción es parte de la recuperación.

Con esta vara, los pagos móviles han acortado el pago en muchas transacciones pequeñas cara a cara, pero aún no pueden proporcionar un camino idéntico para cada escenario. En la mayoría de las transacciones pequeñas presenciales, el efectivo se entrega y confirma sin registro ni dispositivo, sirviendo como la interfaz común más básica. También tiene costos de cambio, custodia e inventario; aquí se compara el umbral de aceptación y fallo, no el costo operativo total.

La encuesta encargada por el Banco Central introdujo las diferencias humanas en el papel del efectivo: los usuarios mayores de 40 años y los de áreas remotas tienen una mayor proporción de solo usar efectivo. Los datos apoyan la diferencia direccional, pero no se pueden extrapolar a un único perfil de todos los ancianos o residentes rurales.[^18] Esta ronda de investigación tampoco tiene suficientes datos para asignar proporciones o voz a menores, personas con discapacidades, trabajadores migrantes y turistas de corta estancia. Las herramientas populares son convenientes para algunos, pero eso no significa que todos puedan tener la misma cuenta, tarjeta, móvil o red.

Los usuarios intensivos en tiendas de cadena familiares pueden realmente evitar los billetes durante mucho tiempo. Otra persona conserva efectivo puede ser simplemente un hábito, una preferencia de privacidad o un control del gasto, y no necesariamente un fallo previo en el pago. La fricción del sistema, la aceptación de la tienda, las recompensas, la membresía, el hábito, la preferencia y la resiliencia ante fallos actúan conjuntamente; las investigaciones existentes no pueden asignarles una única clasificación causal.

El umbral de adopción pregunta cuánta gente usa. El umbral de universalidad pregunta si diferentes personas y tiendas pueden completar escenarios cruzados. Y llevar efectivo todavía tiene que preguntar: ¿se puede recuperar después del fallo? Cuanto más avanzado estén los dos primeros umbrales, menos gente usará efectivo, pero cuándo se va el último billete de la cartera depende de si las excepciones son tan pocas como para no merecer una reserva.

A continuación, se presenta un escenario hipotético basado en las limitaciones fuera de línea del FAQ oficial, y no es un caso real: el móvil de la tienda está fuera de línea, pero la página de inicio aún muestra un Código QR sin monto. El cliente escanea el código, pero la tienda no recibe la notificación de depósito. Ambos miran sus pantallas respectivas; la transacción se queda atascada entre "puede pagar" y "puede confirmar en el momento". El cliente finalmente guarda su móvil y saca un billete. Ese billete no juzga al tecnológico; simplemente, en este escenario, no hay que preguntar primero: "¿Aquí aceptan cuál?".

## Lectura extendida

- [Ecosistema de comercio electrónico y pagos digitales en Taiwán](/es/technology/e-commerce-and-digital-payment-ecosystem) — Revisando la batalla de plataformas y logística del comercio electrónico taiwanés durante veinte años.
- [Desarrollo de tecnología financiera en Taiwán](/es/economy/taiwan-fintech-development) — Colocando el caso de pago dentro del desarrollo de la tecnología financiera taiwanesa en diez años entre apertura y control de riesgos.
- [PX Mart Welfare Center](/es/economy/pxmart-supermarket) — Ver cómo PX Mart pasa de la red de tiendas a una plataforma de vida de alta frecuencia.

## Fuentes de imágenes

- Imagen principal: Taiwan Financial Information Co., Ltd. (Sitio web oficial de TWQR), [Fuente original](https://www.twqr.com.tw/), comentario editorial de uso justo. La imagen original era una miniatura del video oficial "La historia en la mente del jefe | Rizak de carne y pescado", este artículo se utiliza solo para comentar el sistema promocional de TWQR.
- Imagen dentro del texto: Taiwan Financial Information Co., Ltd. (Sitio web oficial de TWQR), [Fuente original](https://www.twqr.com.tw/), comentario editorial de uso justo. La imagen original era una ilustración oficial del sistema "Un contrato, pagos múltiples".

## Referencias

[^1]: [Taiwan Economic Research Institute MIC: Encuesta de consumidores de pagos móviles 2025](https://mic.iii.org.tw/research.aspx?id=730) — Hu Zili explica que los usuarios activos instalan más herramientas para diferentes canales y publica el método de la encuesta, las tasas de adopción y el rango de cantidades.

[^2]: [Taiwan Economic Research Institute MIC: Encuesta de consumidores de pagos móviles 2025](https://mic.iii.org.tw/research.aspx?id=730) — Los datos se recopilaron en la tercera temporada de 2024 mediante una encuesta web con 5,000 muestras efectivas. El 92% que había usado y el 84% que usaba habitualmente están limitados a esa muestra.

[^3]: [Banco Central: Resultados de la encuesta encargada sobre CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Descripción del método de la encuesta, la muestra y la ponderación, y los resultados del 73.8% que mezcla, el 25% que solo usa efectivo y el 1.2% que solo usa lo no efectivo.

[^4]: [Sitio web de inteligencia financiera: Manual de pagos móviles](https://moneywise.fsc.gov.tw/uploaddowndoc?file=financeroom%2F202001131202240.pdf&filedisplay=%E6%96%B0%E5%A2%9E%E6%95%99%E6%9D%90PPT-+%E8%A1%8C%E5%8B%95%E6%94%AF%E4%BB%98-%E5%AE%9A%E7%A8%BF.pdf&flag=doc) — Clasifica las tarjetas de crédito móviles, tarjetas financieras móviles, escaneo de códigos QR, instituciones de pago electrónico y vales electrónicos según la herramienta vinculada, la tecnología y la regulación.

[^5]: [Taiwan Economic Research Institute MIC: Encuesta de consumidores de pagos móviles 2025](https://mic.iii.org.tw/research.aspx?id=730) — Distribución pública del rango de cinco o menos, tres o menos y seis o más en 2024, sin publicar promedios ni medianas.

[^6]: [Oficina Bancaria del Ministerio de Finanzas: Información importante sobre cuentas de pago electrónico de junio de 2026](https://www.fsc.gov.tw/userfiles/file/BB-1156_%E9%9B%BB%E5%AD%90%E6%94%AF%E4%BB%98%E5%B8%B3%E6%88%B6%E9%87%8D%E8%A6%81%E8%B3%87%E8%A8%8A%E6%8F%AD%E9%9C%B2.pdf) — Se suma un total de 41.128 millones; la nota a pie define el número de usuarios que han abierto y no han terminado contratos en cada institución.

[^7]: [Pagos móviles en Taiwán: Preguntas frecuentes sobre operaciones de tiendas especializadas](https://www.twmp.com.tw/Faq?n=95c7608a1dfc4fa1834f4467d41a32d1) — Explica que la tienda debe contratar con la institución financiera receptora y obtener los códigos de la institución, la tienda y el terminal.

[^8]: [Pagos móviles en Taiwán: Preguntas frecuentes de cobro para comercios](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Explica que incluso si el dispositivo está fuera de línea, se puede generar un Código QR sin monto, pero no se puede iniciar sesión ni recibir la notificación de transacción.

[^9]: [Pagos móviles en Taiwán: Preguntas frecuentes de cobro para comercios](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — La explicación oficial indica que la tarifa de procesamiento de transacciones se establece mediante el contrato mutuo entre la tienda y el banco receptor, lo que no puede extrapolarse a una tarifa uniforme del mercado.

[^10]: [Universidad Nacional de Cheng Kung: Estudio sobre la adopción de pagos móviles en tiendas del distrito comercial de Tainan](https://researchoutput.ncku.edu.tw/en/studentTheses/what-factors-affect-stores-willingness-to-adopt-mobile-payment-de/) — El resumen de la tesis doctoral enumera los factores significativos y no significativos para la disposición a adoptar, limitado a la muestra del distrito comercial de Tainan.

[^11]: [Banco Central: Resultados de la encuesta encargada sobre CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Muestra de 611 vendedores ambulantes y 1,436 tiendas, relacionando la diferencia de solo efectivo con el lugar, el equipo y la escala.

[^12]: [Banco Central: Encuesta de herramientas de pago en el informe de estabilidad financiera](https://www.cbc.gov.tw/tw/dl-207586-2f35d674d8a34ee09d1d1c0fd68a6fea.html) — El gráfico enumera las dificultades múltiples de la tienda por no aceptar, no aceptar su herramienta habitual, demasiados tipos, señal y batería del móvil.

[^13]: [Taiwan Economic Research Institute MIC: Encuesta de consumidores de pagos móviles 2025](https://mic.iii.org.tw/research.aspx?id=730) — La encuesta enumera servicios financieros distintos del consumo, siendo la división y transferencia de cuentas el tipo más común.

[^14]: [Visa Taiwán: Estudio de consumidores de billeteras móviles y pagos electrónicos de 2022](https://www.visa.com.tw/about-visa/newsroom/press-releases/nr-tw-230310.html) — Revela los datos de 1,000 muestras taiwanesas de entre 18 y 55 años sobre el seguimiento de recompensas y el cálculo de ofertas.

[^15]: [Oficina de Estadísticas del Ministerio de Economía: PDF de la encuesta de pago minorista](https://www.moea.gov.tw/Mns/populace/news/wHandNews_File.ashx?file_id=116845) — La proporción del monto de pago en la industria mayorista, minorista y de restaurantes para 2017 y 2023, e interpretación del ecosistema de membresía.

[^16]: [Banco Central: Informe anual de 2025](https://www.cbc.gov.tw/tw/dl-225165-b56d9b5e547843a4822acd679cb4868e.html) — Enumera las instituciones participantes de TWQR, las tiendas asociadas a finales de 2025, y el número y monto total de transacciones durante todo el año.

[^17]: [Cooperativa: Servicio de cobro interinstitucional de TWQR](https://www.tcb-bank.com.tw/company-banking/credit-card/special-store/twqr) — Clasifica las instituciones principales de escaneo y secundarias, las especificaciones de QR Auth y los métodos de solicitud de la tienda, mostrando una estratificación por dirección y especificación.

[^18]: [Banco Central: Resultados de la encuesta encargada sobre CBDC](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — El informe presenta diferencias direccionales por edad y región; este artículo no inventa proporciones o voces específicas basándose en esto.
