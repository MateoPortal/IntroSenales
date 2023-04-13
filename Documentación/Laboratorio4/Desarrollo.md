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
 

### 1 Guia de inicio rapido
Es un manual que explica cómo configurar y utilizar BITalino. Incluye información sobre cómo conectar los electrodos, cómo cargar la batería, cómo configurar el software, entre otros aspectos relevantes. La guía de inicio rápido es fundamental para utilizar BITalino de forma efectiva y segura.
- Para EMG se utilizó: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf 

- Para ECG se utilizó: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

## Procedimientos

### Fotos de conexion
Para el presente laboratorio, utilizamos la entrada ECG de Bitalino. 

<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/conexion_final.jpeg" alt="2hilo" width="40%">
 </p>
 
 Dos de los electrodos(el positivo y el negativo) fueron colocados en cada una de las muñecas y el tercero(el electrodo de referencia), en la cresta iliaca
 
<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/conexion_diego.jpeg" alt="2hilo" width="40%">
 </p>
 
 Sin embargo, las lecturas que adquirimos de este primer arreglo no resultó la esperada. Consecuentemente, se decidió a cambiar de ubicación al electrodo positivo y al negativo.
 
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/electrodos_posicion.jpg" width="40%">
  </p>
<p align="center">
  <i>Colocación de los electrodos [3]</i>
  </p>
 
### Video del experimento 

En el siguiente video, observamos cómo cambia la señal del Bitalino dependiendo si el músculo en cuestión permanece en reposo o realiza flexión.

 

### Ploteo de la señal

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/" width="100%">
  </p>
<p align="center">
  <i>Señal ECG en OpenSignals</i>
  </p>
 
# Archivo de datos de la señal ploteada
[Descargar raw data del ECG](LINKPARA DESCARGAR)

### Codigo en Python


# Resultados del ploteo de la señal en Python
Ploteamos la señal ECG en milivoltios versus tiempo en los 3 casos que realizamos durante el laboratorio: en reposo, durante inhalación y exhalación y posterior a realizar actividad física.

<p align="center">
 <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/ecg_time.jpg" width="100%">
 </p>
 
Además, también se realizó el ploteo de la señal ECG en el dominio de la frecuencia, de igual manera en cada uno de los 3 casos ya mencionados.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/frec_reposo.jpg" width="100%">
  </p>
<p align="center">
  <i>Señal ECG en reposo</i>
  </p>
  
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/frec_resp.jpg" width="100%">
  </p>
<p align="center">
  <i>Señal ECG respiración profunda</i>
  </p>

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/frec_ejercicio.jpg" width="100%">
  </p>
<p align="center">
  <i>Señal ECG después de actividad física</i>
  </p>

# Discusión


# Bibliografía
[1] “ELECTROCARDIOGRAMA DEFINICION.” Disponible en: http://www.areasaludplasencia.es/wasp/pdfs/7/711091.pdf<br>
[2] J. Gallo-Villegas, Medicina y Laboratorio. pp. 63–84, 2015. https://docs.bvsalud.org/biblioref/2021/04/907752/prueba-de-esfuerzo.pdf
[3] "Using BITalino Mini with Electrocardiography (ECG) Sensor Application Notes". Disponible en:https://www.bitalino.com/storage/uploads/media/bitalino-application-notes---bitalino-mini-solo-ecg.pdf
