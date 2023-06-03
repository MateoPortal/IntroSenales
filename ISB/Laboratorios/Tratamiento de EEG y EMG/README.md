# Tratamiento de señales EEG y EMG
Laboratorio 9

### Fecha: 3 de junio de 2023

## Objetivo 🎯
En sesiones anteriores (Laboratorios 3 y 5), se obtuvieron señales EMG y EEG a través de un BITalino. Estas señales fueron adquiridas en diferentes contextos. Para el caso de EMG, fueron los siguientes: músculo Bíceps en reposo y flexionado. Para el caso de EEG, estos fueron: en estado basal, respondiendo tanto dos preguntas simples como dos preguntas complejas, recordando una secuencia de palabras y mencionando la misma. 

En esta oportunidad, analizaremos estas muestras de EMG y EEG mediante la aplicación de un algoritmo para la detección de la actividad muscular y para el análisis básico de la señal, respectivamente [1].

## Aplicación de los algoritmos
### EMG
A continuación, presentamos nuestras señales EMG del músculo Bíceps con el algoritmo aplicado:

**Señal EMG en reposo**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_EMG_reposo.png" width="80%">
  </p>
<p align="center">
  <i> Señal EMG y de activación en reposo (Amplitud Vs. Tiempo (s))</i>
  </p>

**Señal EMG en flexión**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_EMG_flexion.png" width="80%">
  </p>
<p align="center">
  <i> Señal EMG y de activación en flexión (Amplitud Vs. Tiempo (s))</i>
  </p>

### EEG
A continuación, presentamos nuestras señales EEG con el algoritmo aplicado:

**Señal EEG en estado basal**
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_estado_basal.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG en estado basal (Amplitud Vs. Tiempo (s))</i>
  </p>
  

**Señal EEG en la pregunta simple 1**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_pregunta_simple_1.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG en la pregunta simple 1 (Amplitud Vs. Tiempo (s))</i>
  </p>

**Señal EEG en la pregunta simple 2**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_pregunta_simple_2.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG en la pregunta simple 2 (Amplitud Vs. Tiempo (s))</i>
  </p>


**Señal EEG en la pregunta compleja 1**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_pregunta_compleja_1.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG en la pregunta compleja 1 (Amplitud Vs. Tiempo (s))</i>
  </p>

**Señal EEG en la pregunta compleja 2**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_pregunta_compleja_2.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG en la pregunta compleja 2 (Amplitud Vs. Tiempo (s))</i>
  </p>  

**Señal EEG mencionándole una secuencia de palabras**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_escuchando_secuencia.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG mencionándole una secuencia de palabras (Amplitud Vs. Tiempo (s))</i>
  </p>
  
**Señal EEG recordando la secuencia de palabras**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/plot_recordando_secuencia.png" width="80%">
  </p>
<p align="center">
  <i> Señal EEG recordando la secuencia de palabras (Amplitud Vs. Tiempo (s))</i>
  </p>

## Discusión
### *Señales EMG*

**Importancia del procesamiento de señales EMG**

La detección de señales EMG con metodologías potentes y avanzadas se está convirtiendo en un requisito muy importante en la ingeniería biomédica. Un área particularmente interesada en esta tecnología es el campo de la gestión y rehabilitación de la discapacidad motora; debido a que las formas y las tasas de activación de los potenciales de acción de la Unidad motora en las señales EMG proporcionan una importante fuente de información para el diagnóstico de trastornos neuromusculares. 

La aplicación de algoritmos y métodos apropiados para el análisis de señales EMG resulta fundamental para poder comprender adecuadamente la naturaleza y características de la señal en cuestión y, de esta manera, realizar implementaciones de hardware para diversas aplicaciones relacionadas con señales EMG [2].

**Adquisición de señales EMG**

Los electrodos que fueron utilizados son los llamados electrodos de superficie, los cuales tienen la peculiaridad de que los registros obtenidos mediante ella muestran actividad poblacional de las unidades motoras, esto es debido a que los electrodos, al estar en la superficie del músculo, no son capaces de captar la señal de una sola unidad motora, sino que por el contrario, captan la información de varias unidades motoras [3].

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Tratamiento%20de%20EEG%20y%20EMG/Im%C3%A1genes/muapt.jpg" width="30%">
  </p>
<p align="center">
  <i> Diagrama de descomposición de señales electromiográficas de superficie. [3]</i>
  </p>

**Detección de la actividad muscular**

La detección de actividad muscular tiene como objetivo obtener tanto el inicio como el final de la actividad EMG. El inicio se define como el comienzo de una contracción o extensión muscular, mientras que el segundo representa el final de estas acciones.

Como utilizamos en el presente algoritmo, la mayoría de los métodos de detección automática de actividad muscular se basan en un umbral. Estos métodos detectan el momento del evento comparando la media de las señales EMG en una ventana deslizante con un cierto umbral [4].

### *Señales EEG*

## Referencias
[1] Pluxbiosignals, “pluxbiosignals/biosignalsnotebooks: biosignalsnotebooks project includes a set of Jupyter Notebooks explaining some processing tasks which have been specially designed for biosignalsplux and OpenSignals users. A Python package is also present, containing some functions to support biosignalsnotebooks notebooks or to be used independently.,” GitHub, Dec. 12, 2022. https://github.com/pluxbiosignals/biosignalsnotebooks (accessed Jun. 03, 2023).

[2] M. Mamun, M. Mahmood Hussain, and Faisal Mohd-Yasin, “Techniques of EMG signal analysis: detection, processing, classification and applications,” vol. 8, no. 1, pp. 11–35, Mar. 2006, doi: https://doi.org/10.1251/bpo115.

[3] G. Orellana, J. Jacob, and C. Nilo, “FACULTAD DE INGENIERÍA ESCUELA DE INGENIERÍA CIVIL MECATRÓNICA DISEÑO E IMPLEMENTACIÓN DE SISTEMA PARA DETECCIÓN DE SEÑALES ELECTROMIOGRÁFICAS Memoria para optar al Título de Ingeniero Civil Mecatrónico Profesor Guía,” 2018. Available: http://dspace.utalca.cl/bitstream/1950/12299/3/tutcur-20180011.pdf

[4] K.-M. Kang, K. Rhee, and H.-C. Shin, “Event Detection of Muscle Activation Using an Electromyogram,” Aug. 2020, doi: https://doi.org/10.3390/app10165593.
‌
