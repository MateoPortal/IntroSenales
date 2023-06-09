# Addressing Detection of Left Bundle Branch Block by Means of Electrocardiogram's Signals using Machine Learning Algorithms

|                |           |                    |
|:---------------------:|:-----------------------:|:-------------------------------:|
|   Alessandra Aldave <br>  Biomedical Engineering  <br> alessandra.aldave@upch.pe    |  José Huaylinos   <br>  Biomedical Engineering <br> jose.huaylinos@upch.pe   | Mateo Luis Portal von Hesse <br> Biomedical Engineering <br> mateo.portal@upch.pe        |
|     Rosmy Postigo    <br>  Biomedical Engineering <br> rosmy.postigo@upch.pe    | Tayel Saavedra   <br>  Biomedical Engineering <br>   tayel.saavedra@upch.pe | Diego Salvatierra <br> Biomedical Engineering <br> diego.salvatierra@upch.pe       |


#### Abstract
In this study, we addressed the detection of left bundle branch block (LBBB) through the analysis of electrocardiogram (ECG) signals using Machine Learning algorithms. LBBB is a cardiovascular disease that affects the heart's electrical conduction system and may indicate the presence of underlying diseases. Early detection of LBBB is crucial for assessing the patient's prognosis and taking preventive measures. To this end, we acquired datasets of ECGs from patients with LBBB, healthy patients, and patients with atrial fibrillation; we also acquired ECG signals from a volunteer suffering from LBBB through BITalino (r)evolution Plugged kit platform. We performed signal preprocessing, feature extraction, and classification using Support Vector Machine (SVM) and Random Forest (RF) algorithms. Accuracy of classification of 82.54\% and 89.14% are obtained for SVM and RF, respectively. F1 score of 97.99% and 97.12% are obtain for prediction of LBBB with SVM and RF, respectively. Our results demonstrate the effectiveness of these algorithms in accurately detecting LBBB from ECG signals. This approach could improve the detection and treatment of cardiovascular diseases related to LBBB.

#### Index Terms
ECG, LBBB, Machine Learning, Detection, SVM, Random Forest.
## I. INTRODUCCIÓN

Cada año, el número de muertes por enfermedades cardiovasculares (ECV) supera a cualquier otra causa, siendo más del 75\% de estas muertes relacionadas con cardiopatías y accidentes cerebrovasculares en países de ingresos medianos y bajos [1]. Es más, la Organización Mundial de la Salud (OMS) ha informado que cada año se pierden 17,9 millones de vidas por ECV [2]. 

El bloqueo de rama izquierda (BRI) es una enfermedad cardiovascular (ECV), el cual representa un trastorno común en el sistema de conducción eléctrica del corazón que provoca una contracción descoordinada de los ventrículos[3]. 
Es importante destacar que el BRI se observa con mayor frecuencia en la práctica de cardiología, tanto en situaciones agudas como en el contexto de un infarto de miocardio o miocarditis, como en enfermedades y afecciones cardíacas crónicas que incluyen enfermedad de las arterias coronarias, hipertensión y miocardiopatías [4]. Asimismo, también está generalmente asociado con insuficiencia cardíaca subyacente, enfermedad de las válvulas cardíacas, agrandamiento o debilitamiento del músculo cardíaco (miocardiopatía), ataque cardíaco, defectos cardíacos congénitos y ciertos medicamentos para el ritmo cardíaco. Por lo tanto, la detección automática temprana es vital [3].

El BRI se suele encontrar en asociación con enfermedad cardíaca orgánica, aunque en ocasiones puede ser un hallazgo incidental en individuos asintomáticos y con corazones aparentemente normales [5]. En un estudio realizado en una muestra aleatoria de 855 hombres que fueron seguidos durante 30 años, se observó que la prevalencia de bloqueo de rama aumentó del 1  a los 50 años al 17  a los 80 años[5]. Otro estudio realizado en una población seleccionada al azar reveló que la prevalencia de BRI fue del 0,43  en hombres y del 0,28  en mujeres de mediana edad[5].

A nivel económico, vale recalcar que la detección del BRI requiere que el paciente se someta a pruebas de electrocardiograma (ECG). En Perú, el costo aproximado de esta prueba es de 180 soles, lo cual puede considerarse un monto elevado [6]. Además, es importante tener en cuenta que si se confirma el diagnóstico de BRI, es posible que se necesiten adquirir medicamentos correspondientes para su tratamiento.

A nivel de las enfermedades cardiovasculares, el impacto económico  puede ser considerable, especialmente cuando se requieren procedimientos quirúrgicos de alto costo. Algunos ejemplos de estos procedimientos incluyen derivaciones coronarias, angioplastia con globo, reparaciones y sustituciones valvulares, trasplante cardíaco e implantación de corazones artificiales [7]. En Estados Unidos, el costo promedio anual por paciente con insuficiencia cardíaca es de $24,383, pero los cargos reportados suelen ser mucho más altos, alcanzando un promedio de $98,599, especialmente cuando se incluyen las readmisiones [8]. Además, la enfermedad de las arterias coronarias implica costos significativos en el manejo terapéutico de eventos coronarios, especialmente en pacientes sin diagnóstico previo ni tratamiento [9]. Según un estudio en Colombia, el costo promedio anual total de un evento coronario es de COP$23,454,569.95 (S/. 20446.65) [9]. Por otro lado, la hipertensión arterial también tiene un impacto económico significativo. De acuerdo con un estudio realizado en el Perú en 2021, el costo del tratamiento anual de la hipertensión arterial fue de $14,842 USD (S/ 25,885), siendo los medicamentos el rubro principal (81.72), seguido del diagnóstico (8.96) y el seguimiento ambulatorio (5.75)[10].

Recordando que el BRI es diagnosticado con la ayuda de un ECG, cabe resaltar que, usualmente, el paciente descubre que tiene un bloqueo de rama izquierda cuando se le hace un ECG por alguna otra razón [11].
Para este diagnóstico, las derivaciones a tomar en cuenta son la  I, V5 y V6 [12]; además, se tienen ciertos criterios a seguir, los cuales son [12]: Una duración de QRS superior a 120 milisegundos, cuya forma del QRS se ensancha y se desvía hacia abajo en la derivación V1. Ausencia de la onda Q en las derivaciones I, V5 y V6. Una onda R monomórfica en I, V5 y V6. Desplazamiento de las ondas ST y T frente a la mayor deflexión del QRS [12].

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/lbbb.png" alt="IMAGEN DE BIENVENIDA" width="25%">
  </p>
<p align="center">
  <em>Imagen1.ECG de bloqueo de la rama izquierda</em>
</p>



## II. PLANTEAMIENTO DEL PROBLEMA
Detectar el bloqueo de la rama izquierda (BRI) resulta fundamental debido a que puede alertar sobre la presencia de enfermedades cardiovasculares subyacentes, como la enfermedad arterial coronaria o la hipertensión [3][4]. El BRI se ha asociado con un mayor riesgo de eventos cardiovasculares adversos y puede influir en las decisiones terapéuticas. Al identificar el BRI, los médicos pueden evaluar el pronóstico del paciente, tomar medidas preventivas para reducir el riesgo de complicaciones y realizar un seguimiento adecuado de la función cardíaca [13][14].
Como ya ha sido previamente mencionado, la detección de BRI depende fundamentalmente de una lectura de ECG, tomando en consideración las derivaciones I, V5 y V6. Consecuentemente, esta prueba es imprescindible para este fin. 
Asimismo, ya hemos observado que la evidencia nos muestra que la edad está directamente relacionada con una mayor prevalencia de BRI; siendo, naturalmente, la población de adultos mayores a 60 años la más afectada [5][15]. Adicionalmente, los datos anteriormente presentados sobre el impacto económico demuestran la necesidad de abordar tanto los aspectos clínicos como los económicos en la prevención y tratamiento de las enfermedades cardiovasculares relacionadas al Bloque de la rama izquierda [8][9][10].

## III. PROPUESTA DE SOLUCIÓN

Una vez identificada la importancia del diagnóstico oportuno del Bloqueo de la rama izquierda, establecemos los puntos claves en los cuales se basa nuestra propuesta de solución.  

La propuesta de solución se basa fundamentalmente en las siguientes etapas (ver Figura 1): Adquisición de datasets de ECGs y del ECG de una paciente voluntaria mediante el uso de un Kit BITalino (BITalino (r)evolution Plugged kit), el preprocesamiento de las señales adquiridas, la extracción de características y la clasificación de las señales de interés.


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

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/mami_ale.jpg" width="25%">
  </p>
<p align="center">
  <em>Imagen2. Adquisión con BITalino</em>
</p>


La señal electrocardiográfica adquirida mediante BITalino (r)evolution Plugged kit fue adquirida por defecto a una frecuencia de muestreo de 1000 Hz; sin embargo, la información de los tres datasets presentaba una frecuencia de muestreo de 500 Hz, por lo que se decidió decimar la señal por un factor entero igual a 2
### b) Preprocesamiento
#### Decimación de la se ̃nal adquirida mediante BITal-ino (r)evolution Plugged kit 
La señal electrocardiográfica adquirida mediante BITalino (r)evolution Plugged kit fue adquirida por defecto a una frecuencia de muestreo de 1000 Hz; sin embargo, la información de los tres datasets presentaba una frecuencia de muestreo de 500 Hz, por lo que se decidió decimar la señal por un factor entero igual a 2.

#### Eliminación del componente continuo
A diferencia de los tres datasets adquiridos de la base de datos [a1], las señales de la paciente voluntaria captadas a través de BITalino (r)evolution Plugged kit, al ser inspeccionadas visualmente, evidenciaron presentar un offset o componente de corriente continua (CC) indeseado, por lo cual se eliminó dicho componente CC.
#### Conversión DAC
Los valores correspondientes a la señal adquirida de la paciente voluntaria con BRI, leídos a partir del formato Matlab (MAT) fueron convertidos al valor analógico correspondiente en unidades de milivoltios multiplicando dichos valores por el voltaje de referencia usado, en este caso, 3.3 V y divididos por la resolución del puerto por el cual se captan las señales electrocardiográficas, es decir, por el puerto A2, el cual cuenta con 10 bits de resolución

$Voltaje_{out}=\frac{3.3 Valor_{dig}}{2^{10} -1}$

#### Filtrado de ruido de las señales
Tras realizar una inspección visual de las 100 señales de los pacientes sanos, de las 100 señales de los pacientes con BRI y de las 100 señales de los pacientes con FA, se determinó utilizar un filtro pasa banda como un filtro pasa bajos en cascada con un filtro pasa altos para eliminar el ruido presente, limitar la señal de ECG a 50 Hz y mejorar la precision del algoritmo de detección del complejo QRS[19].

La implementación de ambos filtros se realizó mediante filtros digitales de respuesta infinita al impulso (IIR) de aproximación Butterworth para obtener la respuesta más plana posible en la banda de paso. El diseño de los filtros presenta las siguiente características: 3 dB de pérdida máxima en la banda de paso, 40 dB de atenuación mínima en la banda de rechazo, 35 Hz como frecuencia de borde de la banda de paso y 50 Hz como frecuencia de borde para la banda de rechazo.


#### Deteccioón del complejo QRS
La detección del complejo QRS de la señal correspondiente a cada paciente de cada clase o cardiopatía se realizó siguiendo el algoritmo de Pan-Tomkins, el cual contempla un (1) filtro pasabanda para el rechazo de ruido, (2) un filtro derivativo cuya función es obtener información de la pendiente del complejo QRS, (3) una función que eleva al cuadrado la señal para amplificar la señal, (4) la integración de una ventana en movimiento cuya finalidad es obtener información de las características de las señales, (5) fiducial mark y (6) un ajuste de umbrales [19].

#### Segmentación  de la señal
Conociendo el inicio y el final del complejo QRS a través del algoritmo Pan-Tompkins, se determinó la ubicación de valor máximo de la onda R. A partir de dicha ubicación, de tomó 100 muestras hacia la derecha y 99 muestras hacia la izquierda para finalmente extraer cada latido que formaba parte de la señal ECG de un paciente.
Las señales y/o latidos que no aportaron información relevante para la posterior etapa de procesamiento fueron eliminadas manualmente.
### c) Extracción de características
La extracción de características se hizo a partir de una descomposición y análisis a través de la Transformada Wavelet. 
#### Transformada Wavelet Discreta
Transformada Wavelet Discreta (DWT) es una herramienta matemática empleada para el análisis de señales no estacionarias como un electrocardiograma [20]. Esta transformada descompone una señal en una serie de coeficientes de aproximación y coeficientes de detalle que describen la evolución de la señal de interés [21]. 
Dado que la Transformada Wavelet Discreta (DWT) será usada sobre un electrocardiograma, la elección de la familia de wavelet madre corresponde a la familia Daubechies, la cual, de todas las familias disponibles, presenta mayor similitud con los beats que se observan en la señal de interés. Asimismo, a partir de la revisión de la literatura [20][22], se determinó que el orden para realizar este análisis es igual a cuatro. 

La implementación de la Transformada Wavelet Discreta (DWT) en el presente estudio se dio a través de la función pywt.wavedec() utilizando el primer nivel de descomposición; debido a que caracterizaba mejor los latidos segementados.
#### Extracción de características
A partir de la descomposición wavelet, se calcularon 16 parámetros estadísticos tanto para los coeficientes de aproximación como para los coeficientes de detalle. 
Estos parámetros estadísticos constituyen, en adelante, los vectores de entrada de características correspondientes a cada clase de latidos (Normal, BRI y FA) para los métodos de aprendizaje supervisado Support Vector Machine y Random Forest.
Los parámetros calculados son los siguientes: la Desviación media absoluta, Percentil 50, Cuantil 0.5, Coeficiente de correlación de Pearson, Matriz de covarianza, Rango de valores, Curtosis,Skewness, Desviación estándar, Varianza, Media, Valor mínimo, Valor máximo, Distancia Manhattan, Distancia euclidiana y Raíz de la media cuadrática.
### d) Clasificación
El aprendizaje automático (o Machine learning en inglés) está ganando popularidad en diversos campos, incluyendo el cuidado de la salud, donde muchos investigadores y profesionales destacan las ventajas del diagnóstico de enfermedades basado en este tipo de proceso, el cual resulta económico y eficiente en términos de tiempo [23]. 
Los algoritmos de clasificación se basan en un método de aprendizaje automático supervisado en el que el modelo intenta predecir la etiqueta correcta de unos datos de entrada determinados [24]. Para nuestra aplicación de diagnóstico, estos algoritmos resultan de considerable ayuda.
#### Clasificación a través de Support Vector Machine (SVM)
La máquina de vectores de soporte o (SVM por sus siglas en inglés), es un método de aprendizaje supervisado cuyo objetivo es maximizar la separación posible que pueda existir entre dos o más clases [25] al construir un hiperplano o una serie de hiperplanos en un espacio, que pueden ser usados para realizar tareas de clasificación, de regresión o de valores atípicos [26].
La formulación más simple de SVM es la formulación lineal, en la cual los hiperplanos toman la siguiente forma [27]: 
\[f(x)=wx+b\] 
Y los subconjuntos del espacio de Hilbert con kernel (k) reproducible son definidos como en la ecuación siguiente [27]:
\[{f:||f||_k ^2 \leq A^2}\]

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/svmHiperplanoEspacio.jpg" width="25%">
  </p>
<p align="center">
  <em>Imagen3. Decisión para un problema de dos clases separables linealmente mediante un hiperplano [25].</em>
</p>

En el presente artículo, dado que son 3 clases las que se van a clasificar, la implementación de la clasificación se implementa mediante el clasificador "one-versus-one" de SVM, el cual construye tres clasificadores y donde cada uno de ellos entrena data de dos clases diferentes
## Conclusión

#### Clasificación a través de Random Forest
El algoritmo Random forest es un modelo de aprendizaje automático que se puede utilizar tanto para problemas de clasificación como de regresión. Se basa en el concepto de aprendizaje conjunto, que combina múltiples clasificadores para resolver un problema complejo y mejorar el rendimiento del modelo. El modelo crea múltiples árboles de decisión y los fusiona para obtener una predicción más precisa y estable. Los árboles se entrenan con el método bagging, lo que significa que cada árbol se entrena en un subconjunto aleatorio de los datos para reducir el sobreajuste y mejorar la precisión del modelo. Además de ello el algoritmo es flexible y fácil de usar que produce buenos resultados incluso sin ajuste de hiperparámetros. Es también uno de los algoritmos más utilizados por su sencillez y versatilidad [28]
Para un problema de clasificación, la predicción final \( \hat{y} \) para una nueva observación \( x \) es obtenida por votación mayoritaria de cada árbol de decisión \( h \) en el bosque:\[\hat{y} = moda( h_1(x), h_2(x), ..., h_n(x))\]
donde \( h_n(x) \) es la predicción del n-ésimo árbol.
Para un problema de regresión, la predicción final es la media de las predicciones de cada árbol de decisión:
\[\hat{y} = \frac{1}{n} \sum_{i=1}^{n} h_i(x)\]
donde \( h_i(x) \) es la predicción del i-ésimo árbol.
Los hiperparámetros a utilizar fueron los siguientes: 
\begin{itemize}
\item \n_estimators}: Este parámetro define el número de árboles en el bosque. Cuanto mayor sea el número de árboles, mayor será la robustez del modelo, aunque puede llevar a un mayor tiempo de cálculo. Se utilizó el número de 1000.
\item \ramdon\_states: Asegura que los resultados del algoritmo sean reproducibles. Si se utiliza el mismo valor, el algorimo producirá exactamente el mismo valor cada vez que se ejecute con los mismos datos de entrada, de lo contrario mostrará resultados diferentes. Para este modelo se utilizó el número 42.


### e) Diseño de PCB

La PCB (Printed circuit board o placa de circuito impreso en español) se compone del chip ESP32 WROOM 32E, un microcontrolador de alto rendimiento y bajo consumo de energía, junto con el AD8232, un amplificador de instrumentación utilizado para adquirir señales de ECG en tiempo real (Figura 6). El diseño de la PCB se ha adaptado para alojar tanto el chip ESP32 como el AD8232, además de otros componentes necesarios para su funcionamiento. Se optó por desarrollar la PCB desde cero con el objetivo de reducir el tamaño final del producto y eliminar componentes innecesarios presentes en el kit de desarrollo devkit. Además de evitar el ruido y las capacitancias parásitas. La PCB incluye conectores y pines específicos para garantizar una conexión segura entre el ESP32 y el AD8232, un puerto Jack para la conexión de los electrodos y un puerto micro USB para la carga de programas y algoritmos en el microcontrolador, así como para permitir la comunicación con una computadora .
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/placaplano.jpeg" width="25%">
  </p>
<p align="center">
  <em>Imagen4. Diseño de la PCB en EasyEda}</em>
</p>
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/placa3d.jpeg" width="25%">
  </p>
<p align="center">
  <em>Imagen5. Animación de una Onda P</em>
</p>

### f) Diseño 3D del wearable
Se realizó un diseño 3D del wearable en formato CAD con el uso de Autodesk Inventor. El diseño se dividió en dos partes: la carcasa y la tapa. La carcasa, de medidas 120 x 80 x 23.5 mm, es donde irán todos los componentes del dispositivo y cuenta con dos aperturas, la primera para el posicionamiento del switch de encendido/apagado y la segunda para la permitir el posicionamiento de los electrodos y la conexión de estos al circuito, ya que este está diseñado para ser usado en el brazo debajo del músculo deltoides. La tapa, por su parte, de dimensiones 120 x 80 x 3.5 mm, se diseñó con una apertura en el centro para el posicionamiento y visualización de la pantalla TFT. Las vistas del diseño pueden verse en las figuras 8-10. 
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/frontal_assembly_se%C3%B1ales.png" width="25%">
  </p>

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/frontal_se%C3%B1ales.png" width="25%">
  </p>

</p>
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/frontal_tapa_se%C3%B1ales.png" width="25%">
  </p>
<p align="center">
  <em>Imagen6,7,8.Vistas del diseño 3d</em>
</p>
A. Cantidad de datos utilizados
La segmentación de la derivación bipolar I de 100 pacientes sanos (Normal), de 100 pacientes con BRI y de 100 pacientes con FA resultó en 781 latidos pertenecientes a pacientes sanos, 746 latidos de pacientes con BRI y 1007 latidos de pacientes con FA. Adicionalmente, 30 latidos fueron segmentados a partir de la señal de la paciente voluntaria con BRI, ver Tabla I

B. Métricas resultantes de clasificación con Support Vector Machin} y textit{Random Forest} En la tabla 2 se muestran los resultados obtenidos con los distintos algoritmos de Machine Learning para la clasificación de ECGs. La exactitud refiere a la repetibilidad de losSVM y 89 para RF. La diferencia de precisión entre la clase Normal y la clase FA, más pronunciada en comparación a la clase BRI puede ser explicada por las formas de los EGCs. La forma del ECG de BRI difiere mucho de un ECG normal y de un ECG de FA debido a la presencia de un complejo QRS muy prolongado o ancho, por lo que resultaba más sencillo realizar la clasificación y ello explica la alta precisión obtenida, mientras que el patrón del latido de clase FA se asemeja al de clase Normal porque la duración del complejo QRS es más corta de lo normal.

Por otro lado, las diferencias entre los electrocardiogramas de la clase normal y la clase FA no son tan notorias como en el caso de BRI ya que las alteraciones en el ECG por FA son principalmente de frecuencia, ritmo y forma en el intervalo PR, segmento ST y onda T. Además, en la segmentación por latidos de los ECGs se pudo observar que, para el caso de FA, la similitud entre las segmentaciones no era tan alta como en el caso de las otras dos clases, principalmente debido a la presencia o ausencia de onda P que no era una característica fija y quedó evidenciado en la obtención de coeficientes de la transformada wavelet de las señales. Esto terminó perjudicando a la precisión obtenida; sin embargo, podría ser mejorada si se consideraran más parámetros para la clasificación de las señales y si se complementa el análisis con más  de una derivación puesto que existen caracteristicas mas definidas que diferencian con mayor enfasis el BRI y la FA [20] [21]. Consideramos que mejorar la presicion aumentando la cantidad de derivaciones podria ser el paso a seguir en futuros estudios. 

## IV. RESULTADOS
### A. Cantidad de datos utilizados
La segmentación de la derivación bipolar I de 100 pacientes sanos (Normal), de 100 pacientes con BRI y de 100 pacientes con FA resultó en 781 latidos pertenecientes a pacientes sanos, 746 latidos de pacientes con BRI y 1007 latidos de pacientes con FA. Adicionalmente, 30 latidos fueron segmentados a partir de la señal de la paciente voluntaria con BRI, ver Tabla I.
### B.Métricas resultantes de clasificación con Support Vector Machine y Random Forest
En la tabla 2 se muestran los resultados obtenidos con los distintos algoritmos de Machine Learning para la clasificación de ECGs. La exactitud refiere a la repetibilidad de los resultados, la precisión a la cercanía de los resultados al valor real.
## V. Discusión
El algoritmo de *Support Vector Machine* alcanzó una exactitud de 82.54% y el *Random Forest* de 89.14%. Esto nos quiere decir que, por cada 100 ECGs clasificados, aproximadamente 83 fueron clasificadas correctamente para SVM y 89 para RF. La diferencia de precisión entre la clase Normal y la clase FA, más pronunciada en comparación a la clase BRI puede ser explicada por las formas de los EGCs. La forma del ECG de BRI difiere mucho de un ECG normal y de un ECG de FA debido a la presencia de un complejo QRS muy prolongado o ancho, por lo que resultaba más sencillo realizar la clasificación y ello explica la alta precisión obtenida, mientras que el patrón del latido de clase FA se asemeja al de clase Normal porque la duración del complejo QRS es más corta de lo normal.

Por otro lado, las diferencias entre los electrocardiogramas de la clase normal y la clase FA no son tan notorias como en el caso de BRI ya que las alteraciones en el ECG por FA son principalmente de frecuencia, ritmo y forma en el intervalo PR, segmento ST y onda T. Además, en la segmentación por latidos de los ECGs se pudo observar que, para el caso de FA, la similitud entre las segmentaciones no era tan alta como en el caso de las otras dos clases, principalmente debido a la presencia o ausencia de onda P que no era una característica fija y quedó evidenciado en la obtención de coeficientes de la transformada wavelet de las señales. Esto terminó perjudicando a la precisión obtenida; sin embargo, podría ser mejorada si se consideraran más parámetros para la clasificación de las señales y si se complementa el análisis con más  de una derivación puesto que existen características más definidas que diferencian con mayor énfasis el BRI y la FA [20] [21]. Consideramos que mejorar la precisión aumentando la cantidad de derivaciones podría ser el paso a seguir en futuros estudios.
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/imag%201.JPG" width="25%">
  </p>
<p align="center">
  <em>Imagen9. Gráfico de frontera de decisión con SVM</em>
</p>
## VI. Conclusiones

La detección y clasificación de arritmias, como el BRI, a partir de señales de ECG presenta desafíos debido a la alta variabilidad entre los pacientes del dataset disponible [16]. En este estudio, se utilizó un conjunto de datos de ECG con una amplia variedad de casos y señales clasificadas, lo que permitió que los algoritmos tradicionales de aprendizaje, como SVM, lograran una clasificación satisfactoria. Sin embargo, la duración variable de las señales (de 6 a 60 segundos) representó un desafío, ya que pueden aparecer eventos de arritmia que duren solo unos segundos. Estos eventos a veces pueden confundirse con segmentos ruidosos, lo que dificulta la clasificación precisa de toda la señal. A pesar de estas dificultades se logró implementar un algoritmo que alcanzó una alta precisión y con una correcta optimización pueda ser implementado en un dispositivo de bajo costo y dimensiones reducidas. Esto se realizaría exportando el modelo entrenado utilizando una biblioteca de serialización e integrándolo al ESP32 a través de un entorno de desarrollo adecuado. Lo cual facilitará la detección oportuna de BRI en lugares con recursos limitados y sin acceso a dispositivos con mayor poder de procesamiento.

### Bibliography

\[1\] "Cardiovascular diseases - PAHO/WHO | Pan American Health Organization," Paho.org, 2018. [Online]. Available: [link](https://www.paho.org/en/topics/cardiovascular-diseases) (accessed Jul. 01, 2023).

\[2\] World Health Organization, "World health statistics 2018: monitoring health for the SDGs, sustainable development goals," Who.int, 2018, doi: [link](https://doi.org/9789241565585).

\[3\] B. Al-Naami, H. Fraihat, H. Abu Owida, K. Al-Hamad, R. de Fazio, and P. Visconti, "Automated Detection of Left Bundle Branch Block from ECG Signal Utilizing the Maximal Overlap Discrete Wavelet Transform with ANFIS," vol. 11, no. 6, pp. 93–93, Jun. 2022, doi: [link](https://doi.org/10.3390/computers11060093).

\[4\] O. A. Smiseth and J. M. Aalen, "Mechanism of harm from left bundle branch block," vol. 29, no. 6, pp. 335–342, Aug. 2019, doi: [link](https://doi.org/10.1016/j.tcm.2018.10.012).

\[5\] T. Hardarson, A. Arnason, G. Elíasson, K. Pálsson, K. Eyjolfsson, and N. Sigfússon, "Left bundle branch block: prevalence, incidence, follow-up and outcome," vol. 8, no. 10, pp. 1075–1079, Oct. 1987, doi: [link](https://doi.org/10.1093/oxfordjournals.eurheartj.a062172).

\[6\] "Riesgo Quirúrgico (Incluye Electrocardiograma) - Multilab - Qué es, precio, preparación," Riesgo Quirúrgico (Incluye Electrocardiograma) - Multilab - Qué es, precio, preparación, Jan. 22, 2023. [Online]. Available: [link](https://www.multilab.com.pe/examen/901/riesgo-quirurgico?gclid=CjwKCAjwv8qkBhAnEiwAkY-ahjjGlAQoTQ4nEJKM7NxCkpPmRlUXfGybMjSgTsu2feIvjNxXhr-fghoC-xgQAvD_BwE) (accessed Jun. 28, 2023).

\[7\] "Cardiovascular diseases (CVDs)," Who.int, Jun. 11, 2021. [Online]. Available: [link](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)) (accessed Jul. 01, 2023).

\[8\] M. Urbich, K. Pantiri, M. M. Heisen, C. Bennison, H. S. Wirtz, and Tanna, "A Systematic Review of Medical Costs Associated with Heart Failure in the USA (2014–2020)," vol. 38, no. 11, pp. 1219–1236, Aug. 2020, doi: [link](https://doi.org/10.1007/s40273-020-00952-0).

\[9\] M. Romero, E. M. Vásquez, F. Acero, and L. M. Huerfano, "Estimación de los costos directos de los eventos coronarios en Colombia," vol. 25, no. 6, pp. 373–379, Nov. 2018, doi: [link](https://doi.org/10.1016/j.rccar.2018.05.010).

\[10\] Hernández et al., "Costo de la hipertensión arterial pulmonar en el Perú," vol. 21, no. 3, pp. 580–587, Jan. 2021, doi: [link](https://doi.org/10.25176/rfmh.v21i3.3905).

\[11\] "Left Bundle Branch Block | Cedars-Sinai," Cedars-sinai.org, 2022. [Online]. Available: [link](https://www.cedars-sinai.org/health-library/diseases-and-conditions/l/left-bundle-branch-block.html#:~:text=How\%20is\%20left\%20bundle\%20branch,done\%20for\%20some\%20other\%20reason) (accessed Jun. 21, 2023).

\[12\] B. Al-Naami, H. Fraihat, H. Abu Owida, K. Al-Hamad, R. de Fazio, and P. Visconti, "Automated Detection of Left Bundle Branch Block from ECG Signal Utilizing the Maximal Overlap Discrete Wavelet Transform with ANFIS," vol. 11, no. 6, pp. 93–93, Jun. 2022, doi: [link](https://doi.org/10.3390/computers11060093).

\[13\] P. Gaba, D. M. Pedrotty, C. V. DeSimone, A. R. Bonikowske, T. G. Allison, and S. Kapa, "Mortality in Patients With Right Bundle‐Branch Block in the Absence of Cardiovascular Disease," vol. 9, no. 19, Oct. 2020, doi: [link](https://doi.org/10.1161/jaha.120.017430).

\[14\] D. Varvarousis et al., "Cardiac arrhythmias in arterial hypertension," vol. 22, no. 8, pp. 1371–1378, Aug. 2020, doi: [link](https://doi.org/10.1111/jch.13989).

\[15\] C. Clinic, "Left Bundle Branch Block: Causes, Symptoms & Treatment - Cleveland Clinic," Cleveland Clinic, 2022. [Online]. Available: [link](https://my.clevelandclinic.org/health/diseases/23287-left-bundle-branch-block#:~:text=If\%20you're\%20over\%2065,or\%20after\%20a\%20heart\%20attack) (accessed Jun. 28, 2023).

\[16\] "The China Physiological Signal Challenge 2018," Icbeb.org, 2018. [Online]. Available: [link](http://2018.icbeb.org/Challenge.html) (accessed Jul. 07, 2023).

\[17\] CDC, "Atrial Fibrillation

," Centers for Disease Control and Prevention, Oct. 14, 2022. [Online]. Available: [link](https://www.cdc.gov/heartdisease/atrial_fibrillation.htm#:~:text=Atrial\%20fibrillation\%2C\%20often\%20called\%20AFib,or\%20in\%20an\%20irregular\%20way) (accessed Jul. 07, 2023).

\[18\] Rohde, "Captura de señales de electrocardiogramas pequeñas en aplicaciones médicas," Rohde-schwarz.com, 2023. [Online]. Available: [link](https://www.rohde-schwarz.com/lat/aplicaciones/captura-de-se-ales-de-electrocardiogramas-peque-as-en-aplicaciones-m-dicas-ficha-de-aplicacion_56279-152385.html) (accessed Jul. 07, 2023).

\[19\] J. Pan and W. J. Tompkins, "A Real-Time QRS Detection Algorithm," IEEE Transactions on Biomedical Engineering, vol. BME-32, no. 3, pp. 230–236, Mar. 1985, doi: [link](https://doi.org/10.1109/tbme.1985.325532).

\[20\] S. Faziludeen and P. Sabiq, "ECG beat classification using wavelets and SVM," Apr. 2013, doi: [link](https://doi.org/10.1109/cict.2013.6558206).

\[21\] M. Hosseinzadeh, "Robust control applications in biomedical engineering: Control of depth of hypnosis," pp. 89–125, Jan. 2020, doi: [link](https://doi.org/10.1016/b978-0-12-817461-6.00004-4).

\[22\] A. Rabee and I. Barhumi, "ECG signal classification using support vector machine based on wavelet multiresolution analysis," IEEE Xplore, Jul. 01, 2012. [Online]. Available: [link](https://ieeexplore.ieee.org/document/6310497) (accessed Jun. 27, 2021).

\[23\] M. Ahsan, S. A. Luna, and Z. Siddique, "Machine-Learning-Based Disease Diagnosis: A Comprehensive Review," vol. 10, no. 3, pp. 541–541, Mar. 2022, doi: [link](https://doi.org/10.3390/healthcare10030541).

\[24\] Z. Keita, "Classification in Machine Learning: An Introduction," Datacamp.com, Sep. 21, 2022. [Online]. Available: [link](https://www.datacamp.com/blog/classification-machine-learning) (accessed Jul. 07, 2023).

\[25\] "Support Vector Machine (SVM)," la.mathworks.com. [Online]. Available: [link](https://la.mathworks.com/discovery/support-vector-machine.html) (accessed Jul. 08, 2023).

\[26\] scikit learn, "1.4. Support Vector Machines — scikit-learn 0.20.3 documentation," Scikit-learn.org, 2018. [Online]. Available: [link](https://scikit-learn.org/stable/modules/svm.html).

\[27\] T. Evgeniou and M. Pontil, "Support Vector Machines: Theory and Applications," Machine Learning and Its Applications, pp. 249–257, 2001, doi: [link](https://doi.org/10.1007/3-540-44673-7\_12).

\[28\] H. Zhang, D. Nettleton and Z. Zhu, "Regression-Enhanced Random Forests," arXiv preprint arXiv:1904.10416, 2019. [Online]. Available: [link](https://arxiv.org/pdf/1904.10416.pdf). [Accessed: 07-Jul-2023].

### Author's Biography

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/ale2.jpg" width="25%">
  </p>
**Alessandra Aldave**  
Ninth-semester undergraduate student of Biomedical Engineering at Pontifical Catholic University of Peru - Cayetano Heredia University. Currently, she is engaged in nanobody research as part of her internship at the Molecular Biotechnology and Cell Signaling Laboratory. Her research interest lies in Kidney Tissue Engineering and Biomaterials.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/jose_bw.jpg" width="25%">
  </p> 
**Jose Huaylinos**  
He is a Biomedical Engineering student with a focus on healthcare management and the application of AI in patient care. Currently, he serves as a JCI coordinator at the San Pablo Group in Lima, Peru, ensuring their services meet international standards.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/mateo.jpeg" width="25%">
  </p>
**Mateo Portal**  
Ninth-semester undergraduate student of Biomedical Engineering at Pontifical Catholic University of Peru - Cayetano Heredia University. He is currently interested in Clinical Engineering and his goal is to improve the health sector in Peru and people's quality of life.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/RP.jpg" width="25%">
  </p> 
**Rosmy Postigo**  
Seventh-semester undergraduate student of Biomedical Engineering at Pontifical Catholic University of Peru - Cayetano Heredia University. Her areas of interest are Biomaterials and Tissue Engineering. She aims to work on and develop alternative toxicology testing methods to replace the traditional methods currently used.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/tayell.JPG" width="25%">
  </p>
**Tayel Saavedra**  
Seventh-semester undergraduate student studying Biomedical Engineering at Pontifical Catholic University of Peru - Cayetano Heredia University. His current focus is on Biomaterials and Tissue Engineering, and he aspires to innovate the health sector by applying the characteristics of advanced biomaterials.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/diego1.jpg" width="25%">
  </p> 
**Diego Salvatierra**  
Peruvian biomedical engineering student at PUCP and UPCH. He would like to specialize in the field of medical signal processing because it offers tremendous potential for improving healthcare outcomes and advancing medical research. Medical signal processing involves the analysis, interpretation, and manipulation of signals obtained from various physiological processes in the human body, such as electrocardiograms (ECGs), electroencephalograms (EEGs), and medical imaging data.
