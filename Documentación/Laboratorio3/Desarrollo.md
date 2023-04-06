# LABORATORIO 3: USO DE BITALINO PARA EMG Y ECG
 
## Tabla de contenidos
 1. [Objetivos]
 2. [Materiales]
 3. [Procedimientos]
 4. [Resultados]


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


## Procedimientos

### Fotos de conexion
Utilizamos la entrada EMG de Bitalino. Dos de los electrodos fueron colocados en el músculo Bisceps y un tercero en un hueso ubicado en la zona de la muñeca, este funciona como "tierra"

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/d6cd5bdafd6c2734a6577b80e178de1b1586cadd/Documentaci%C3%B3n/Laboratorio3/Pictures/electrodos_en_biceps.jpeg" alt="1" width="40%">
  </p>
 
 <p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/d6cd5bdafd6c2734a6577b80e178de1b1586cadd/Documentaci%C3%B3n/Laboratorio3/Pictures/electrodo_en_mu%C3%B1eca.jpeg" alt="1" width="40%">
  </p>

 
 
### Video de señal
En el siguiente video, observamos cómo cambia la señal del Bitalino dependiendo si el músculo en cuestión permanece en reposo o realiza flexión.
<iframe
    width="640"
    height="480"
    src="https://www.youtube.com/embed/UmX4kyB2wfg"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen
>
</iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/UmX4kyB2wfg" frameborder="0" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/LxSqwbDHh7I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="<iframe width="560" height="315" src="https://www.youtube.com/embed/LxSqwbDHh7I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>" frameborder="0" allowfullscreen></iframe>


### Ploteo de la señal
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/senal_bitalino.jpeg" alt="1" width="100%">
  </p>

### Resumen de la señal 
Se realizó la secuencia relajación-flexión-relajación-flexión. Observamos que durante la etapa de relajación o reposo, las señales ploteadas adquiridas son las que presentan una muy baja amplitud en mV. En este caso, la amplitud de la señal es mucho menor a comparación de cuando el músculo realiza flexión, o en otras palabras, cuando el bíceps se contrae.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/brazo_reposo.jpeg" width="40%"> 
 Brazo en relajación</em>
  </p>
  
### Archivo de datos de la señal ploteada

### Ploteo de la señal en Python

## Resultados
