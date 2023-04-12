# Laboratorio 4

### Fecha: 12 de abril de 2023

## Objetivos
* Adquirir señales biomédicas de EMG y ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolutio

# Tabla de contenidos
 1. [Objetivos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Desarrollo.md#objetivos-1)
 2. [Materiales](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Desarrollo.md#materiales)
 3. [Procedimientos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Desarrollo.md#procedimientos)
 4. [Resultados](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Desarrollo.md#resultados-del-ploteo-de-la-se%C3%B1al-en-python)
 5. [Bibliografía](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Desarrollo.md#bibliograf%C3%ADa)

## Objetivos:
  1. Generar 3 señales sinusoidales con cierta frecuencia y amplitud.
  2. Guardar las señales adquiridas en el osciloscopio en archivo CSV y las adquiridas en ARDUINO mediante el ploteo por el código en ARDUINO IDLE.
  3. Comparar una señal leída de un osciloscopio y el arduino Nano 33 IoT.

## Materiales
### BITalino

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/503321ac6b98dd412af11dc4987800b30d8a27e1/Documentaci%C3%B3n/Laboratorio3/Pictures/Bitalino.jpeg" alt="bitalino" width="45%">
  </p>

### Cable de 2 hilos
Se utiliza para conectar BITalino a dispositivos externos, como sensores, actuadores, etc. Está compuesto por dos hilos que permiten la transmisión de datos y energía.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/503321ac6b98dd412af11dc4987800b30d8a27e1/Documentaci%C3%B3n/Laboratorio3/Pictures/cable2hilos.jpeg" alt="2hilo" width="25%">
  </p>



### Cable de 3 hilos
Se utiliza para conectar BITalino a los electrodos. Está compuesto por tres hilos: uno para la transmisión de datos, otro para la transmisión de energía y un tercero para la conexión a tierra.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/503321ac6b98dd412af11dc4987800b30d8a27e1/Documentaci%C3%B3n/Laboratorio3/Pictures/cable3hilos.jpeg" alt="2hilo" width="25%">
  </p>


### 5 electrodos
Son sensores que se colocan en el cuerpo para medir la actividad eléctrica de los músculos, el corazón, el cerebro, entre otros. En el kit BITalino se incluyen cinco electrodos para poder realizar mediciones en distintas partes del cuerpo.

<p align="center">
  <img src="https://cdn.shopify.com/s/files/1/0146/9569/4436/products/Electrodo_Backvolt_Circular_2_800x.png?v=1565294606" alt="2hilo" width="25%">
  </p>

### 1 Bateria
Es la fuente de energía para BITalino. La batería incluida en el kit es recargable y tiene una capacidad de 700mAh.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/b369fe5e0d1f1d11d12c900606117ab97e5308a4/Documentaci%C3%B3n/Laboratorio3/Pictures/BATERIA.jpeg" alt="2hilo" width="25%">
  </p>
 
### Conexion Final

<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/b369fe5e0d1f1d11d12c900606117ab97e5308a4/Documentaci%C3%B3n/Laboratorio3/Pictures/conexion_final.jpeg" alt="2hilo" width="25%">
 </p>
 
### 1 Guia de inicio rapido
Es un manual que explica cómo configurar y utilizar BITalino. Incluye información sobre cómo conectar los electrodos, cómo cargar la batería, cómo configurar el software, entre otros aspectos relevantes. La guía de inicio rápido es fundamental para utilizar BITalino de forma efectiva y segura.
- Para EMG se utilizó: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf 

- Para ECG se utilizó: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

## Procedimientos

### Fotos de conexion
Utilizamos la entrada ECG de Bitalino. Dos de los electrodos fueron colocados en el músculo Bisceps y un tercero en un hueso ubicado en la zona de la muñeca, este funciona como "tierra"


 
 
#Video del experimento 
En el siguiente video, observamos cómo cambia la señal del Bitalino dependiendo si el músculo en cuestión permanece en reposo o realiza flexión.

 

### Ploteo de la señal

Resumen de la señal:




<p align="center">
  <img src="IMAGENLINK" alt="1" width="40%">
<p align="center">
 Ploteo en OpenSignals del músculo en relajación</em>
  </p>
  
<p align="center">
  <img src="IMAGENLINK" alt="1" width="40%">
 <p align="center">
 Ploteo en OpenSignals del músculo en contracción</em>
  </p>




<p align="center">
  <img src="IMAGENLINK" width="40%"> 
 <p align="center">
 Brazo en relajación</em>
  </p>
  
<p align="center">
  <img src="IMAGENLINK" width="40%"> 
 <p align="center">
 Brazo en flexion</em>
  </p>
  
# Archivo de datos de la señal ploteada
[Descargar raw data del ECG](LINKPARA DESCARGAR)

### Codigo en Python


# Resultados del ploteo de la señal en Python
<p align="center">
  <img src="IMAGENLINK" alt="1" width="100%">
  </p>
<p align="center">
  <img src="IMAGENLINK" alt="1" width="100%">
  </p>
<p align="center">
  <img src="IMAGENLINK" alt="1" width="100%">
  </p>
<p align="center">
  <img src="IMAGENLINK" alt="1" width="100%">
  </p>

# Bibliografía
