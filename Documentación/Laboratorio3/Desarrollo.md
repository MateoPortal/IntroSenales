# LABORATORIO 3: USO DE BITALINO PARA EMG Y ECG
 
## Tabla de contenidos
 1. [Objetivos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Desarrollo.md#Objetivos)
 2. [Materiales](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Desarrollo.md#Materiales)
 3. [Procedimientos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Desarrollo.md#Procedimientos)
 4. [Resultados](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Desarrollo.md#resultados-del-ploteo-de-la-se%C3%B1al-en-python)

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

 
 
#Video del experimento 
En el siguiente video, observamos cómo cambia la señal del Bitalino dependiendo si el músculo en cuestión permanece en reposo o realiza flexión.
"https://www.youtube.com/embed/UmX4kyB2wfg"
 

### Ploteo de la señal
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/reposo.jpeg" alt="1" width="100%">
<p align="center">
 Ploteo del músculo en relajación</em>
  </p>
  
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/activo.jpeg" alt="1" width="100%">
 <p align="center">
 Ploteo del músculo en flexión</em>
  </p>

Resumen de la señal:

En la figura se observa la colocación de los electrodos en el músculo bíceps, utilizados con la finalidad de obtener una señal durante el reposo y flexión del músculo en cuestión. En el estado de reposo,  las señales ploteadas adquiridas son las que presentan una muy baja amplitud en mV . Por el otro lado, cuando se realiza la flexión se puede apreciar que la señal adquiere un mayor valor de voltaje. La amplitud y duración de cada pico varía, lo que indica distintos niveles de fuerza. Por otro lado, también se aprecia en la grafica [Grafica de frecuencias vs dB] la presencia de bajas frecuencias en la señal, esto se debe probablemente a la interferencia de músculos cercanos con alta actividad o de las fuentes eléctricas cercanas, esto último explicaría el pico presente en la señal en aproximadamente 60 Hz. En general, la señal es una representación clara y bien definida del cambio de actividad del músculo, con un detalle suficiente como para una análisis e interpretación.


<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/brazo_reposo.jpeg" width="40%"> 
 <p align="center">
 Brazo en relajación</em>
  </p>
  
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/brazo_flexion.jpeg" width="40%"> 
 <p align="center">
 Brazo en flexion</em>
  </p>
  
# Archivo de datos de la señal ploteada
[Descargar raw data del EMG](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/emg.txt)

### Codigo en Python

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
```
```python
f = open("signal1.txt","r")
raw_data = f.readline()  # con f.read() leemos todo el contenido
f.close()

raw_data
```




    'Fs=400\n'




```python

x = re.findall("[0-5][0-9]\d", raw_data)

print(x)
```

    ['400']
    


```python
Fs = float(x[0])
Ts=1/Fs

print(f" Fs={Fs} hz\n Ts={Ts} s")
```

     Fs=400.0 hz
     Ts=0.0025 s
    

#### Leemos el archivo excluyendo las 3 primeras filas del archivo

```python
array = np.genfromtxt("./emg.txt", delimiter="\t",skip_header = 3)
array
```




    array([[  0.,   0.,   0., ...,   0., 476.,  nan],
           [  1.,   0.,   0., ...,   0., 487.,  nan],
           [  2.,   0.,   0., ...,   0., 493.,  nan],
           ...,
           [ 15.,   0.,   0., ...,   0., 479.,  nan],
           [  0.,   0.,   0., ...,   0., 482.,  nan],
           [  1.,   0.,   0., ...,   0., 494.,  nan]])




```python
array[:,-2]
data_mV = (array[:,-2])*(3.3/1023) #resolucion*Vref/1023 segun el puerto A1 para EMG
n=np.arange(0,len(data_mV)) #numero de muestras
print(n)
t=n/1000 #tiempo
print(t)
```

    [    0     1     2 ... 22047 22048 22049]
    [0.0000e+00 1.0000e-03 2.0000e-03 ... 2.2047e+01 2.2048e+01 2.2049e+01]
    


```python
plt.figure(figsize=(20,20))
plt.suptitle("Señal EMG en el tiempo y en el dominio discreto");
plt.subplot(3,2,1);plt.plot(t,data_mV),plt.ylabel("mV"),plt.xlabel("Tiempo (s)"),plt.title("Señal completa de EMG de superficie en músculo biceps")
plt.subplot(3,2,2);plt.plot(np.arange(len(data_mV)),data_mV),plt.ylabel("mV"),plt.xlabel("Número de muestras [n]"),plt.title("Señal completa de EMG de superficie en músculo biceps")

t1=np.arange(0,len(data_mV[:14000]))/1000
plt.subplot(3,2,3);plt.plot(t1,data_mV[:14000]),plt.ylabel("mV"),plt.xlabel("Tiempo (s)"),plt.title("EMG de superficie en músculo biceps: reposo-contracción 1-reposo")
plt.subplot(3,2,4);plt.plot(np.arange(len(data_mV[:14000])),data_mV[:14000]),plt.ylabel("mV"),plt.xlabel("Número de muestras [n]"),plt.title("EMG de superficie en músculo biceps: reposo-contracción 1-reposo")

t2=np.arange(0,len(data_mV[14000:]))/1000
plt.subplot(3,2,5);plt.plot(t2,data_mV[14000:]),plt.ylabel("mV"),plt.xlabel("Tiempo (s)"),plt.title("EMG de superficie en músculo biceps: reposo-contracción 2-reposo")
plt.subplot(3,2,6);plt.plot(np.arange(len(data_mV[14000:])),data_mV[14000:]),plt.ylabel("mV"),plt.xlabel("Número de muestras [n]"),plt.title("EMG de superficie en músculo biceps: reposo-contracción 2-reposo")
```




    ([<matplotlib.lines.Line2D at 0x1c971c5f310>],
     Text(0, 0.5, 'mV'),
     Text(0.5, 0, 'Número de muestras [n]'),
     Text(0.5, 1.0, 'EMG de superficie en músculo biceps: reposo-contracción 2-reposo'))


#### Ploteamos la lectura


```python
plt.plot(array[:,2], array[:], label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.show()
```


```python
N = 2**10                                     # 10 bits, 0-1023
Fs=1000
signal1 = array[:,-2]

signal_fft = np.fft.fft(signal1, N)           # fft magtinud
signal_fft = np.round(np.abs(signal_fft),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
signal_aux = signal_fft/signal_fft.max()     # hallamos el maximo para pasar la magnitud a escala db

with np.errstate(divide='ignore'):
    signal_fft_db = 10*np.log10(signal_aux)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

F_list = np.linspace(0,Fs/2, N//2)
F = np.round(F_list[np.argmax(signal_fft_db)], 1)   # argmax, encuentra el argumento max en un array

plt.plot(F_list, signal_fft_db)  #10 * np.log10(P / Pref) , decibelios
plt.text(F,0, f"{F}Hz")
plt.grid(linestyle=":")
plt.ylabel("Magnitud (db)")
plt.xlabel("Frecuencias (Hz)")
plt.title("FFT en el decibelios")
#plt.xlim([0,20])
#plt.xticks(np.arange(0,200,10))
plt.show()
```
   
    
# Resultados del ploteo de la señal en Python
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/plot1.jpeg" alt="1" width="100%">
  </p>
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/plot2.jpeg" alt="1" width="100%">
  </p>
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/plot3.jpeg" alt="1" width="100%">
  </p>
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio3/Pictures/Frequency.jpeg" alt="1" width="100%">
  </p>
