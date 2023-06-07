# Laboratorio 10

### Fecha: 7 de junio de 2023



# Tabla de contenidos
 1. [Objetivos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#objetivos)
 2. [Materiales](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#materiales)
 3. [Procedimientos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#procedimientos)
 4. [Resultados](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#resultados-del-ploteo-de-la-se%C3%B1al-en-python)
 5. [Discusión](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#discusi%C3%B3n)
 6. [Bibliografía](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#bibliograf%C3%ADa)

## Objetivos

* Extraer características de la base de datos.
* Entrenamiento del modelo de Regresión Logistica.
* Evaluar las métricas del modelo entrenado. 

## Materiales

### Dataset (Base de datos)

Se utilizó una base de datos de 7 variables independientes y de 1 variable dependiente . La base de datos se adapta para utilizar en un modelo de machine learning de clasificación.

Variables in dependientes : [C, Rp, Dif_vol, V_in, V_out, P_ventilador, PIP]
Variable dependiente : Error_aceptable
Muestras de la base de datos : 

### Código 

[Descargar código de Python](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/py.txt)

## Discusión

<p align="center">
 El encefalograma es un examen médico que permite realizar la medición de los potenciales eléctricos absolutos generados por las neuronas [2].
 </p>
En el presente laboratorio, de las señales obtenidas en ambos sujetos de prueba, se observa que existe un incremento de la actividad eléctrica producida por el cerebro cuando ellos se encontraban resolviendo mentalemente el set de 2 ejercicios simples y el set de 2 ejercicios complejos en los que se les plantearon preguntas acerca de cálculos aritméticos. Además, según la revisión de la literatura, se conoce que la actividad cerebral representada a través de los ritmos alfa y theta es sensitiva a este tipo de procesamiento cognitivo de la información en el que se requiere un gran esfuerzo mental [3]. Esto es evidente al observar las señales de EEG en el dominio de la frecuencia, de cuando se les dictó las preguntas complejas, y compararlas con el estado basal del sujeto de prueba.

Por otro lado, es necesario mencionar que la señal de EEG obtenida usando la interfaz Ultracortex Mark IV, así como la señal adquirida con BITalino en las posiciones Frontopolar 1 (Fp1) y Frontopolar 2 (Fp2) presentan artefactos musculares, los cuales hacen referencia a la contaminación de una señal de EEG debido a la actividad muscular facial [4]. Además, según lo reportado por Soleymain et al., los artefactos musculares faciales afectan de manera significativa a la señal de EEG, especialmente a aquellos electrodos que se ubican en las regiones frontal, parietal y occipital; y que tales artefactos mencionados se observan de manera más pronunciada en las frecuencias altas, es decir, en los ritmos beta y gamma [4]. En particular, durante los experimentos realizados durante el Laboratorio 5, en ambos sujetos de prueba, debido a que las respuestas a las preguntas realizadas las dieron de forma verbal, se evidenció el uso de músculos involucrados en el habla como actividad voluntaria.

Adicionalmente, el origen del ruido presente en las señales grabadas podría ser atribuido a la presencia de distintos estímulos durante el desarrollo del experimento. Durante toda la grabación de la señal para ambos sujetos de prueba, hubo un permanente ruido debido a las voces de todos los participantes de la sesión de laboratorio. Asimismo, una de las limitaciones identificadas en lo que duró el desarrollo de la experiencia usando la interfaz Ultracortex Mark IV, es que debido al corto intervalo de tiempo, los últimos 5 minutos de la sesión, que se tuvo para hacer uso de ella, no se tuvo en cuenta el evitar los estímulos visuales, pues el sujeto de prueba mantuvo los ojos abiertos a lo largo de toda la grabación de la señal; además, en el video adjunto se puede observar cómo el sujeto de prueba no mantiene la mirada en un punto fijo, sino que observa diferentes puntos.
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/Screenshot%202023-04-19%20112220.png" width="75%">
  </p>
<p align="center">
  <i>Funciones de los lóbulos del cerebro [a]</i>
  </p>



# Bibliografía
[1] “BITalino (r)evolution Lab Guide.” Revisado en: Abril 19, 2023. [Online]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[2] Rayi A, Murr N. Electroencephalogram. [Updated 2022 Oct 3]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2023 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK563295/

[3] Y. Zhu, Q. Wang, and L. Zhang, “Study of EEG characteristics while solving scientific problems with different mental effort,” Scientific Reports, vol. 11, no. 1, 2021. 

[4] X. Zeng, X. Zhao, S. Wang, J. Qin, J. Xie, X. Zhong, J. Chen, and G. Liu, “Affection of facial artifacts caused by micro-expressions on Electroencephalography signals,” Frontiers in Neuroscience, vol. 16, 2022. 
