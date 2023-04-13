# Laboratorio 4

### Fecha: 12 de abril de 2023

## Objetivos
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolutio

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
De igual forma que en el laboratorio 3, utilizamos la plataforma BITalino para el presente entregable

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/503321ac6b98dd412af11dc4987800b30d8a27e1/Documentaci%C3%B3n/Laboratorio3/Pictures/Bitalino.jpeg" alt="bitalino" width="45%">
  </p>


### Cable de 3 hilos
Se utiliza para conectar BITalino a los electrodos. Está compuesto por tres hilos: uno para la transmisión de datos, otro para la transmisión de energía y un tercero para la conexión a tierra.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/503321ac6b98dd412af11dc4987800b30d8a27e1/Documentaci%C3%B3n/Laboratorio3/Pictures/cable3hilos.jpeg" alt="2hilo" width="25%">
  </p>


### 3 electrodos
Son sensores que se colocan en el cuerpo para medir la actividad eléctrica de los músculos, el corazón, el cerebro, entre otros. En el kit BITalino se incluyen cinco electrodos para poder realizar mediciones en distintas partes del cuerpo.

<p align="center">
  <img src="https://cdn.shopify.com/s/files/1/0146/9569/4436/products/Electrodo_Backvolt_Circular_2_800x.png?v=1565294606" alt="2hilo" width="25%">
  </p>

### 1 Bateria
Es la fuente de energía para BITalino. La batería incluida en el kit es recargable y tiene una capacidad de 700mAh.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/b369fe5e0d1f1d11d12c900606117ab97e5308a4/Documentaci%C3%B3n/Laboratorio3/Pictures/BATERIA.jpeg" alt="2hilo" width="25%">
  </p>
 

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
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/electrodos.jpg" width="60%">
  </p>
<p align="center">
  <i>Colocación de los electrodos [3]</i>
  </p>
 
### Video del experimento 

En los siguientes videos, se presentan las señales adquiridas mediante los electrodos del dispositivo BITalino, los cuales fueron ubicados en la clavícula del individuo sometido a prueba.

Debido al tamaño de los videos(mayor a 10mb, lo cual no admite github), se decidió insertar links en youtube.

https://youtu.be/ww7lRXT72hk <br/>
https://youtu.be/EzKz_8wJHfU <br/>
https://youtu.be/BDQO8avbaoo <br/>


### Ploteo de la señal

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio4/Im%C3%A1genes/ecg_reposo.png" width="60%">
  </p>
<p align="center">
  <i>Señal ECG en OpenSignals, reposo</i>
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

El electrocardiograma (ECG) es una herramienta esencial en la evaluación de la actividad eléctrica del corazón y su funcionamiento [4]. Mediante la observación de las variaciones en las señales del ECG, es posible obtener información crucial sobre la salud cardíaca y el bienestar general del individuo en distintas condiciones, como en estado de reposo, durante la respiración profunda y después de realizar ejercicio físico intenso.

Bajo circunstancias normales, el ECG en reposo presenta una señal regular y estable, lo que refleja una frecuencia cardíaca dentro de un rango normal [5]. Las ondas P, QRS y T del ECG están claramente definidas, proporcionando información sobre la contracción y relajación del corazón. En adultos, la frecuencia cardíaca promedio en reposo oscila entre 60 y 100 latidos por minuto, y la señal del ECG debería situarse dentro de esos límites.

Al realizar respiraciones profundas, el cuerpo experimenta varios cambios fisiológicos que afectan la señal del ECG. Estas variaciones se deben a la modificación de la frecuencia cardíaca y la amplitud de las ondas [6]. Durante la inspiración, la frecuencia cardíaca puede disminuir, mientras que durante la espiración puede incrementarse. Además, pueden presentarse alteraciones en las ondas P, QRS y T debido a los cambios en la presión intratorácica.

Tras una actividad física intensa, la señal del ECG puede experimentar cambios significativos [7]. El corazón trabaja más arduamente durante el ejercicio y requiere bombear mayor cantidad de sangre para satisfacer las demandas metabólicas del cuerpo. En consecuencia, la frecuencia cardíaca aumenta, y la señal del ECG puede mostrar un incremento en la amplitud de las ondas, una reducción del intervalo P-R y un acortamiento del intervalo Q-T. Posteriormente, la frecuencia cardíaca disminuye gradualmente a medida que el cuerpo se recupera, y la señal del ECG retorna a un estado similar al del reposo.



# Bibliografía
[1] “ELECTROCARDIOGRAMA DEFINICION.” Disponible en: http://www.areasaludplasencia.es/wasp/pdfs/7/711091.pdf<br>
[2] J. Gallo-Villegas, Medicina y Laboratorio. pp. 63–84, 2015. https://docs.bvsalud.org/biblioref/2021/04/907752/prueba-de-esfuerzo.pdf
[3] "Using BITalino Mini with Electrocardiography (ECG) Sensor Application Notes". Disponible en:https://www.bitalino.com/storage/uploads/media/bitalino-application-notes---bitalino-mini-solo-ecg.pdf<br>
[4] L. B. Andersen, N. Maffulli, J. A. Casajús, F. Pigozzi, and Y. P. Pitsiladis, "The future of electrocardiograms in pre-participation screening: a call to action," The Physician and Sportsmedicine, vol. 46, no. 1, pp. 1-3, 2018.<br>
[5] M. Buchheit, M. Lacome, and Y. Cholley, "The use of GPS-based data in soccer: challenges and opportunities from an athlete and coach perspective," International Journal of Sports Physiology and Performance, vol. 14, no. 3, pp. 1-27, 2019.<br>
[6] A. L. Goldberger, V. K. Le, and M. Lahiri, "Is the normal heart rate 'chaotic' due to respiration?" Chaos: An Interdisciplinary Journal of Nonlinear Science, vol. 28, no. 8, 085711, 2018.<br>
[7] L. Sarlabous, A. Torres, J. A. Fiz, J. Gea, J. M. Martínez-Llorens, J. Morera, and R. Jané, "Influence of diaphragmatic motion on the efficiency of cough in supine and lateral decubitus positions: a dynamic MRI study," Respiratory Physiology & Neurobiology, vol. 247, pp. 24-30, 2018.<br>
