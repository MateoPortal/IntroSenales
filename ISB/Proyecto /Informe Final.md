# Addressing Detection of Left Bundle Branch Block by Means of Electrocardiogram's Signals using Machine Learning Algorithms

|                |           |                    |
|:---------------------:|:-----------------------:|:-------------------------------:|
|   Alessandra Aldave <br>  Biomedical Engineering  <br> alessandra.aldave@upch.pe    |  José Huaylinos   <br>  Biomedical Engineering <br> jose.huaylinos@upch.pe   | Mateo Luis Portal von Hesse <br> Biomedical Engineering <br> mateo.portal@upch.pe        |
|     Rosmy Postigo    <br>  Biomedical Engineering <br> rosmy.postigo@upch.pe    | Tayel Saavedra   <br>  Biomedical Engineering <br>    @upch.pe | Diego Salvatierra <br> Biomedical Engineering <br> diego.salvatierra@upch.pe       |


#### Abstract
Abstract text goes here.

#### Index Terms
Index terms go here.

## I. INTRODUCCIÓN

Cada año, el número de muertes por enfermedades cardiovasculares (ECV) supera a cualquier otra causa, siendo más del 75\% de estas muertes relacionadas con cardiopatías y accidentes cerebrovasculares en países de ingresos medianos y bajos [1]. Es más, la Organización Mundial de la Salud (OMS) ha informado que cada año se pierden 17,9 millones de vidas por ECV [2]. 

El bloqueo de rama izquierda (BRI) es una enfermedad cardiovascular (ECV), el cual representa un trastorno común en el sistema de conducción eléctrica del corazón que provoca una contracción descoordinada de los ventrículos[3]. 
Es importante destacar que el BRI se observa con mayor frecuencia en la práctica de cardiología, tanto en situaciones agudas como en el contexto de un infarto de miocardio o miocarditis, como en enfermedades y afecciones cardíacas crónicas que incluyen enfermedad de las arterias coronarias, hipertensión y miocardiopatías [4]. Asimismo, también está generalmente asociado con insuficiencia cardíaca subyacente, enfermedad de las válvulas cardíacas, agrandamiento o debilitamiento del músculo cardíaco (miocardiopatía), ataque cardíaco, defectos cardíacos congénitos y ciertos medicamentos para el ritmo cardíaco. Por lo tanto, la detección automática temprana es vital [3].

El BRI se suele encontrar en asociación con enfermedad cardíaca orgánica, aunque en ocasiones puede ser un hallazgo incidental en individuos asintomáticos y con corazones aparentemente normales [5]. En un estudio realizado en una muestra aleatoria de 855 hombres que fueron seguidos durante 30 años, se observó que la prevalencia de bloqueo de rama aumentó del 1 \% a los 50 años al 17 \% a los 80 años[5]. Otro estudio realizado en una población seleccionada al azar reveló que la prevalencia de BRI fue del 0,43 \% en hombres y del 0,28 \% en mujeres de mediana edad[5].

A nivel económico, vale recalcar que la detección del BRI requiere que el paciente se someta a pruebas de electrocardiograma (ECG). En Perú, el costo aproximado de esta prueba es de 180 soles, lo cual puede considerarse un monto elevado [6]. Además, es importante tener en cuenta que si se confirma el diagnóstico de BRI, es posible que se necesiten adquirir medicamentos correspondientes para su tratamiento.

A nivel de las enfermedades cardiovasculares, el impacto económico  puede ser considerable, especialmente cuando se requieren procedimientos quirúrgicos de alto costo. Algunos ejemplos de estos procedimientos incluyen derivaciones coronarias, angioplastia con globo, reparaciones y sustituciones valvulares, trasplante cardíaco e implantación de corazones artificiales [7]. En Estados Unidos, el costo promedio anual por paciente con insuficiencia cardíaca es de \$24,383, pero los cargos reportados suelen ser mucho más altos, alcanzando un promedio de \$98,599, especialmente cuando se incluyen las readmisiones [8]. Además, la enfermedad de las arterias coronarias implica costos significativos en el manejo terapéutico de eventos coronarios, especialmente en pacientes sin diagnóstico previo ni tratamiento [9]. Según un estudio en Colombia, el costo promedio anual total de un evento coronario es de COP\$23,454,569.95 (S/. 20446.65) [9]. Por otro lado, la hipertensión arterial también tiene un impacto económico significativo. De acuerdo con un estudio realizado en el Perú en 2021, el costo del tratamiento anual de la hipertensión arterial fue de \$14,842 USD (S/ 25,885), siendo los medicamentos el rubro principal (81.72\%), seguido del diagnóstico (8.96\%) y el seguimiento ambulatorio (5.75\%)[10].

Recordando que el BRI es diagnosticado con la ayuda de un ECG, cabe resaltar que, usualmente, el paciente descubre que tiene un bloqueo de rama izquierda cuando se le hace un ECG por alguna otra razón [11].
Para este diagnóstico, las derivaciones a tomar en cuenta son la  I, V5 y V6 [12]; además, se tienen ciertos criterios a seguir, los cuales son [12]:
-Una duración de QRS superior a 120 milisegundos, cuya forma del QRS se ensancha y se desvía hacia abajo en la derivación V1.
-Ausencia de la onda Q en las derivaciones I, V5 y V6.
-Una onda R monomórfica en I, V5 y V6.
-Desplazamiento de las ondas ST y T frente a la mayor deflexión del QRS.

## II. PLANTEAMIENTO DEL PROBLEMA
Detectar el bloqueo de la rama izquierda (BRI) resulta fundamental debido a que puede alertar sobre la presencia de enfermedades cardiovasculares subyacentes, como la enfermedad arterial coronaria o la hipertensión [3][4]. El BRI se ha asociado con un mayor riesgo de eventos cardiovasculares adversos y puede influir en las decisiones terapéuticas. Al identificar el BRI, los médicos pueden evaluar el pronóstico del paciente, tomar medidas preventivas para reducir el riesgo de complicaciones y realizar un seguimiento adecuado de la función cardíaca [13][14].
Como ya ha sido previamente mencionado, la detección de BRI depende fundamentalmente de una lectura de ECG, tomando en consideración las derivaciones I, V5 y V6. Consecuentemente, esta prueba es imprescindible para este fin. 
Asimismo, ya hemos observado que la evidencia nos muestra que la edad está directamente relacionada con una mayor prevalencia de BRI; siendo, naturalmente, la población de adultos mayores a 60 años la más afectada [5][15]. Adicionalmente, los datos anteriormente presentados sobre el impacto económico demuestran la necesidad de abordar tanto los aspectos clínicos como los económicos en la prevención y tratamiento de las enfermedades cardiovasculares relacionadas al Bloque de la rama izquierda [8][9][10].

## III. PROPUESTA DE SOLUCIÓN

MENCIONAR POR ACÁ MACHIN LEARNING
Una vez identificada la importancia del diagnóstico oportuno del Bloqueo de la rama izquierda, establecemos los puntos claves en los cuales se basa nuestra propuesta de solución.  

La propuesta de solución se basa fundamentalmente en las siguientes etapas (ver Figura X): Adquisición de datasets de XXXXX y de una paciente voluntaria mediante el uso de un Kit BITalino (BITalino (r)evolution Plugged kit), el preprocesamiento de las señales adquiridas, la extracción de características y la clasificación de las señales de interés.


### a) Adquisición
Tanto la data de entrenamiento como la data de prueba son de vital importancia para nuestra aplicación. Ambos conjuntos de datos fueron adquiridos de dos fuentes distintas.

#### Datasets
Los datasets utilizados en nuestro proyecto fueron obtenidos a partir de The China Physiological Signal Challenge (CPSC) 2018 que tuvo lugar en la 7ma Conferencia Internacional sobre Ingeniería Biomédica y Biotecnología (ICBEB 2018) en Nanjing, China [a1].

El objetivo de nuestro estudio es evaluar la detección de Bloqueo de rama izquieda (BRI); sin embargo, con la finalidad de mejorar la robustez del algoritmo se requirió seleccionar una cardiopatía adicional y contar con un control negativo. Por ello, de todos los ECGs disponibles de 12 derivaciones que componen el \textit{dataset} de la fuente mencionada líneas arriba, se hizo únicamente uso de ECGs de 100 pacientes con Bloqueo de rama izquierda (BRI), de 100 pacientes sanos (Normal) y de 100 pacientes con Fibrilación auricular (FA) [a1]. 

La elección del dataset de pacientes con Fibrilacion auricular como dataset de la cardiopatía adicional a considerar se debe a que se trata de una enfermedad cuyo diagnostico requiere ser confirmador mediante electrocardiograma, además de tratarse de la arritmia más frecuente en adultos [a2]

Asímismo, los electrocardiogramas de pacientes sanos fueron considerados como control negativo para el presente estudio.



Todas las grabaciones de ECGs disponibles presentaban una frecuencia de muestreo de 500 Hz y se encontraron disponibles en extensión .mat o formato Matlab (MAT) [].

De las 12 derivaciones disponibles en los 3 datasets seleccionados (Normal, BRI, FA), se decidió utilizar exclusivamente la derivación bipolar I Lead I debido a que la clasificación a realizar se contrastaría con la data de la paciente voluntaria adquirida a través del BITalino (r)evolution Plugged kit, el cual únicamente es capaz de captar derivaciones bipolares (I, II y III).

Finalmente, se trabajó con 3 datasets: El primer dataset corresponde a la primera derivación bipolar de 100 pacientes normales, el segundo dataset corresponde a la primera derivación bipolar de 100 pacientes con BRI y el último, a la primera derivación bipolar de 100 pacientes con FA.

#### Reccolección de datos

Dispusimos, de manera voluntaria, del consentimiento y colaboración de una mujer de 61 años diagnosticada con Bloqueo de la Rama Izquierda (BRI). A través de la plataforma BITalino (r)evolution Plugged kit), se llevó a cabo la recolección de señales de electrocardiograma (ECG) que presentan características específicas asociadas a esta condición médica. Empleamos tres electrodos para la captación de señales eléctricas en las derivaciones I, II y III.

La señal electrocardiográfica adquirida mediante BITalino (r)evolution Plugged kit fue adquirida por defecto a una frecuencia de muestreo de 1000 Hz; sin embargo, la información de los tres datasets presentaba una frecuencia de muestreo de 500 Hz, por lo que se decidió decimar la señal por un factor entero igual a 2
### b) Procesamiento

#### Decimación de la se ̃nal adquirida mediante BITal-ino (r)evolution Plugged kit

#### Eliminación del componente continuo

#### Conversión DAC

#### Filtrado de ruido de las señales

#### Deteccioón del complejo QRS

#### Segmentación  de la señal

### c) Extracción de características

#### Transformada Wavelet Discreta

#### Extracción de características

### d) Clasificación

#### Clasificación a través de Support Vector Machine (SVM)

#### Clasificación a través de Random Forest

### e) Diseño de PCB


### f) Diseño de wearable

## IV. RESULTADOS
Resultados text goes here.

## V. CONCLUSIONES
Conclusiones text goes here.


## Referencias

## VI. Biografía de autores
