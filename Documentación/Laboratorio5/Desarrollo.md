# Laboratorio 5

### Fecha: 19 de abril de 2023

## Objetivos
* Adquirir señales biomédicas de EEG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EEG del software OpenSignals (r)evolution

# Tabla de contenidos
 1. [Objetivos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#objetivos)
 2. [Materiales](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#materiales)
 3. [Procedimientos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#procedimientos)
 4. [Resultados](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#resultados-del-ploteo-de-la-se%C3%B1al-en-python)
 5. [Discusión](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#discusi%C3%B3n)
 6. [Bibliografía](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#bibliograf%C3%ADa)

## Objetivos:
  1. Generar 3 señales sinusoidales con cierta frecuencia y amplitud.
  2. Guardar las señales adquiridas en el osciloscopio en archivo CSV y las adquiridas en ARDUINO mediante el ploteo por el código en ARDUINO IDLE.
  3. Comparar una señal leída de un osciloscopio y el arduino Nano 33 IoT.

## Materiales
### BITalino
De igual forma que en el laboratorio 3, utilizamos la plataforma BITalino para el presente entregable

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/bitalino%20y%20bateria.jpg" alt="bitalino" width="45%">
  </p>


### Cable de 3 hilos
Se utiliza para conectar BITalino a los electrodos. Está compuesto por tres hilos: uno para la transmisión de datos, otro para la transmisión de energía y un tercero para la conexión a tierra.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/electrodo%203%20hilos.jpg" alt="2hilo" width="25%">
  </p>


### 3 electrodos
Son sensores que se colocan en el cuerpo para medir la actividad eléctrica de los músculos, el corazón, el cerebro, entre otros. En el kit BITalino se incluyen cinco electrodos para poder realizar mediciones en distintas partes del cuerpo. En esta oportunidad utilizamos la entrada para EEG.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/diodos%20separados.jpg" alt="2hilo" width="25%">
  </p>

### 1 Bateria
Es la fuente de energía para BITalino. La batería incluida en el kit es recargable y tiene una capacidad de 700mAh.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/bitalino%20y%20bateria.jpg" alt="2hilo" width="25%">
  </p>
 

## Procedimientos

### Fotos de conexion
Para el presente laboratorio, realizamos una conexión muy parecida a la sesión pasada; pero en esta oportunidad, como ya mencionamos, utilizamos la entrada EEG de Bitalino en vez de la entrada ECG. 

<p align="center">
 <img src="linkdelaimagen" alt="2hilo" width="40%">
 </p>
 
 Los electrodos fueron ubicados tomando como referencia la distribución proporcionada por la guía de laboratorio de BITalino.
 
<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/Screenshot%202023-04-19%20121008.png" alt="2hilo" width="40%">
 </p>
<p align="center">
  <i>Referencia de colocación de los electrodos [1]</i>
  </p>
 
<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/Screenshot%202023-04-19%20121008.png" alt="2hilo" width="40%">
 </p>
<p align="center">
  <i>Colocación de los electrodos</i>
  </p> 
 
### Video del experimento 

En los siguientes videos, se presentan las señales adquiridas mediante los electrodos del dispositivo BITalino, los cuales fueron ubicados en la clavícula del individuo sometido a prueba.

Debido al tamaño de los videos (mayor a 10 MB, lo cual no admite GitHub), se decidió insertar los links correspondientes a cada video grabado.

- link
- link
- link


### Ploteo de la señal

<p align="center">
  <img src="linkdelaimagen" width="60%">
  </p>
<p align="center">
  <i>Señal ECG en OpenSignals, reposo</i>
  </p>
 
# Archivo de datos de la señal ploteada
[Descargar raw data del EEG](linkdedescarga)

### Codigo en Python
[Visualizar código de procesamiento de las señales en Python](linkparaver)

# Resultados del ploteo de la señal en Python
Ploteamos la señal EEG en milivoltios versus tiempo en los 3 casos que realizamos durante el laboratorio: en reposo, durante inhalación y exhalación y posterior a realizar actividad física.

<p align="center">
 <img src="linkdelaimagen" width="100%">
 </p>
 
Además, también se realizó el ploteo de la señal ECG en el dominio de la frecuencia, de igual manera en cada uno de los 3 casos ya mencionados.

<p align="center">
  <img src="linkdelaimagen" width="100%">
  </p>
<p align="center">
  <i>Señal ECG en reposo</i>
  </p>
  
<p align="center">
  <img src="linkdelaimagen" width="100%">
  </p>
<p align="center">
  <i>Señal ECG respiración profunda</i>
  </p>

<p align="center">
  <img src="linkdelaimagen" width="100%">
  </p>
<p align="center">
  <i>Señal EEG después de actividad física</i>
  </p>

# Discusión

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Im%C3%A1genes/Screenshot%202023-04-19%20112220.png" width="75%">
  </p>
<p align="center">
  <i>Funciones de los lóbulos del cerebro [a]</i>
  </p>



# Bibliografía
[1] “BITalino (r)evolution Lab Guide.” Revisado en: Abril 19, 2023. [Online]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf
[2] 
[3] 
[4] 
[5]
[6] 
[7] 
