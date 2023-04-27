# Creación de Dataset de señales ECG
Laboratorio 6

### Fecha: 26 de abril de 2023

## Objetivo 🎯
En una sesión anterior (Laboratorio 4), se obtuvieron señales ECG a través de un BITalino. Estas señales fueron adquiridas en diferentes contextos: en reposo, durante la exhalación e inhalación y durante la realización de actividad física. En esta oportunidad, se creó el dataset de estas señales ya obtenidas.

## Recordando sobre la adquisición de las señales ECG 🔙
### Imágenes de la colocación de electrodos
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/electrodos.jpg" width="60%">
  </p>
<p align="center">
  <i>Colocación de los electrodos [1]</i>
  </p>

### Ploteo de la señal

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/ecg_reposo.png" width="60%">
  </p>
<p align="center">
  <i>Señal ECG en OpenSignals, reposo</i>
  </p>
  
### Resultados del ploteo de la señal en Python
Ploteamos la señal ECG en milivoltios versus tiempo en los 3 casos que realizamos durante el laboratorio: en reposo, durante inhalación y exhalación y posterior a realizar actividad física.

<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/ecg_time.jpg" width="100%">
 </p>
 
 # Archivo de datos de la señal ploteada
[Descargar raw data del ECG](https://github.com/MateoPortal/IntroSenales/tree/main/Documentaci%C3%B3n/Laboratorio4/ECG_RawData)

 ## Importancia del Procesamiento de señales
 ¿Qué es? El procesamiento de señales se puede describir desde diferentes perspectivas. Para un especialista en acústica, es una herramienta para convertir las señales medidas en información útil. Para un diseñador de sonar, es una parte de un sistema de sonda. Para un ingeniero eléctrico, a menudo se limita a la digitalización, el muestreo, el filtrado y la estimación espectral [2].

¿Cómo se realiza? En la actualidad, el procesamiento de señales digitales se realiza principalmente en sofware, este puede ejecutarse en el procesador o trajeta gráfica de alguna computadora o dispositivo inteligente. En aplicaciones más complejas y exigentes, se ejecuta en DSP dedicados (o procesadores de señales digitales en castellano), ASIC (circuitos integrados específicos de aplicaciones) o FPGA (matrices de puertas programables en campo) y en potentes mainframes de computadora [3].
 
 ## Dataset de las señales ECG
 
 [Descargar dataset del ECG](https://github.com/MateoPortal/IntroSenales/tree/main/Documentaci%C3%B3n/Creación%20de%20Dataset%20de%20señales%20ECG/dataset_señales_ecg_grupo_10_.py)
 
 ## Referencias
 [1] "Using BITalino Mini with Electrocardiography (ECG) Sensor Application Notes". Disponible en:https://www.bitalino.com/storage/uploads/media/bitalino-application-notes---bitalino-mini-solo-ecg.pdf
 [2] D. A. Abraham, “Signal Processing,” Jan. 2017, doi: https://doi.org/10.1016/b978-0-12-811240-3.00011-4.
 [3] “¿Qué es el procesamiento de señales?,” Soluciones de Adquisición de Datos (DAQ), Mar. 14, 2023. https://dewesoft.com/es/blog/que-es-procesamiento-de-senal (accessed Apr. 27, 2023).
 
 
 
