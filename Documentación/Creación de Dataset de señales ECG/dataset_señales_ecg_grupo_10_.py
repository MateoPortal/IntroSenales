# -*- coding: utf-8 -*-
"""Dataset señales ECG Grupo 10 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y_k-jRrEQuGMlYbnqkQVtUhxpz9e1Yxn
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import sys

"""## Leemos el archivo excluyendo las 2 primeras filas del archivo"""

#Lectura de documento txt con tabulación (/t) como delimitador
array = np.genfromtxt("ECG_reposo.txt", delimiter="\t",comments='#',skip_header = 3)
array
array1 = np.genfromtxt("ECG_respirar.txt", delimiter="\t",comments='#',skip_header = 3)
array1
array2 = np.genfromtxt("ECG_deporte.txt", delimiter="\t",comments='#',skip_header = 3)
array2

data_mV_ECG_reposo = (array[:,-2])*(3.3/1023) #resolucion*Vref/1023 segun el puerto A2 para ECG
data_mV_ECG_respiracion = (array1[:,-2])*(3.3/1023) #resolucion*Vref/1023 segun el puerto A2 para ECG
data_mV_ECG_deporte = (array[:,-2])*(3.3/1023) #resolucion*Vref/1023 segun el puerto A2 para ECG

"""# **Particion de la data para señales ECG durante Reposo**"""

indices_segmentos = [0, 700, 1700, 2600, 3570, 4550]

# Crear los 5 vectores segmentados
vectores = []
for i in range(len(indices_segmentos) - 1):
    inicio = indices_segmentos[i]
    fin = indices_segmentos[i + 1]
    segmento = data_mV_ECG_reposo[inicio:fin]
    vectores.append(segmento)

# Encontrar el tamaño máximo de los vectores y rellenar con ceros si es necesario
tamanio_maximo = max([len(vector) for vector in vectores])

vectores_rellenos = []
for vector in vectores:
    elementos_faltantes = tamanio_maximo - len(vector)
    vector_relleno = np.concatenate((vector, np.zeros(elementos_faltantes)))
    vectores_rellenos.append(vector_relleno)

# Crear un array concatenando los vectores rellenos
array_concatenado = np.concatenate(vectores_rellenos)

# Cambiar la forma del array para obtener una matriz con 5 filas y columnas del tamaño del vector más largo
filas = 5
matriz = array_concatenado.reshape((filas, tamanio_maximo))

np.set_printoptions(edgeitems=10, linewidth=200, threshold=sys.maxsize)
print(matriz)#Se imprime la matriz

"""## Tamaño de la matriz"""

matriz.shape

"""## Graficación de datos"""

for i in range(filas):
    # Crear una máscara para eliminar los ceros al momento de graficar
    mascara = matriz[i] != 0
    plt.plot(matriz[i][mascara])
    plt.show()

"""# **Particion de la data para señales ECG durante realización de Respiración**"""

#Nos quedamos con el dato del sensor, tomamos cierta cantidad limitada de data pues se considero que durante los primeros segundos la informacion no fue consistente.
d_sensor = array1[:,-2]
d_sensor_2 = d_sensor[8000:80000]
print(len(d_sensor_2))

"""# Graficación de datos"""

#Ploteo de un fragmento de la señal
plt.plot(d_sensor_2)
plt.xlim(0,5000)

"""# Especificar la Frecuencia de Muestreo"""

Fs = 1000 #Frecuencia de muestreo del dispositivo de adquisición
Ts=1/Fs
n = np.arange(0,d_sensor_2.shape[0])  # t = n*Ts
t = n*Ts

#Ploteamos la señal en el tiempo
plt.figure(figsize=(13,2)) #Modificamos el tamaño de la gráfica
plt.plot(t, d_sensor_2)

"""# Pasando el array a pandas para trabajarlo como series de tiempo"""

#Pasamos las observaciones a filas correspondientes a una variable t y d_sensor
st_sensor = np.concatenate((t.reshape(-1,1),  d_sensor_2.reshape(-1,1)), axis=1)

#Creamos el data frame con las varibles t y d_sensor
df = pd.DataFrame(st_sensor, columns=["t","d_sensor"])
df.head()

#Establecemos t como index 
df = df.set_index("t")
df.head()

#Ploteamos la señal

df.plot(figsize=(10,3))
plt.xlim(0,1)

"""# Pasando a data tabular estilo Sklearn"""

df.index.max()/1
df.shape[0]/72
#Creamos una matriz con las observaciones como fila y como columna las muestras que lo constituyen. Se estimo que el periodo de cada muestra es de 0.8 segundos, 
#por lo que el numero de muestras en cada observacion sera de 800 muestras puesto que la frecuencia de muestreo que se utilizo durante la adquisicion fue de 1000 Hz.
d_obs = df[["d_sensor"]].values.reshape(90,800)
d_obs

#Se plotea algunas de las observaciones.
plt.figure(figsize=(13,2))
plt.plot(d_obs[15])
plt.figure(figsize=(13,2))
plt.plot(d_obs[16])
plt.figure(figsize=(13,2))
plt.plot(d_obs[17])
plt.figure(figsize=(13,2))
plt.plot(d_obs[18])
plt.figure(figsize=(13,2))
plt.plot(d_obs[19])

d_obs.shape

"""## **Particion de la data para señales ECG durante realización de Deporte**

"""

plt.figure(figsize=(40,10))
plt.figure(figsize=(40,10))
t=np.arange(0,len(data_mV_ECG_deporte))/1000
plt.plot(t,data_mV_ECG_deporte),plt.ylabel("mV"),plt.xlabel("Tiempo (s)"),plt.title(" ECG Tras realizar ejercicio físico")

plt.figure(figsize=(40,10))
t1=np.arange(0,len(data_mV_ECG_deporte))
plt.plot(t1,data_mV_ECG_deporte),plt.ylabel("mV"),plt.xlabel("Muestras [n]"),plt.title("ECG Tras realizar ejercicio físico")

#De la data graficada en el entregable en el que se realizo la adquisicion de señales ECG, se determino que el periodo era de aproximadamente 0,6s, por lo que a una frecuencia de muestreo de 1000 Hz, equivale a 600 muestras en 1 periodo
#Primero, se determino la data util, es decir, se retiran los extremos con picos poco caracteristicos de la señal. La particion realizada a continuacion se hizo considerando un numero de muestras que sea multiplo de 600 y que no contengan los picos no deseados de la señal
#DATA UTIL PARA PARTICIONAR
plt.figure(figsize=(40,10))
t2=np.arange(0,len(data_mV_ECG_deporte[6000:60000]))
plt.plot(t2,data_mV_ECG_deporte[6000:60000]),plt.ylabel("mV"),plt.xlabel("Muestras [n]"),plt.title("ECG Tras realizar ejercicio físico") #para visualizar la señal

data_util_ECG_deporte = data_mV_ECG_deporte[6000:60000]
#print(data_util_ECG_deporte)
print(np.shape(data_util_ECG_deporte))


#De las 54000 muestras en total, se busca tener sets de 600 muestras, por lo que se redimensiona a (600,90)
#DATA UTIL AHORA EN 1 FILA Y 54000 COLUMNAS
data_util_ECG_deporte_reshapeada = np.reshape(data_util_ECG_deporte,(1,54000))
print(np.shape(data_util_ECG_deporte_reshapeada))

#DATA UTIL AHORA EN 90 FILA Y 600 COLUMNAS
data_util_ECG_deporte_reshapeada2 = np.reshape(data_util_ECG_deporte_reshapeada,(90,600))
print(np.shape(data_util_ECG_deporte_reshapeada2))

'''
#Solo para plotear
#DATA UTIL AHORA EN 600 FILA Y 90 COLUMNAS
data_util_ECG_deporte_reshapeada3 = np.reshape(data_util_ECG_deporte_reshapeada2,(600,90))
print(np.shape(data_util_ECG_deporte_reshapeada3))
plt.figure(figsize=(40,10))
t3=np.arange(0,len(data_util_ECG_deporte_reshapeada3))
plt.plot(t3,data_util_ECG_deporte_reshapeada3)
'''
#Se obtienen todas las observaciones a partir de la data total
observaciones = data_util_ECG_deporte_reshapeada2[:]
print(observaciones)
print(np.shape(observaciones))

for i in range(len(observaciones)): #Visualizacion de todos los sets de 600 muestras
    plt.figure()
    plt.plot(observaciones[i])

#Se eliminan los sets de datos que no muestren las ondas PQRST de forman definida y completa a partir de la inspeccion de los 90 plots obtenidos previamente
sets_utiles=[0,12,13,14,15,24,25,26,27,28,35,36,37,38,52,63,64,65,66,67,76,77,78,79,88,89]
sets_eliminar=[1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,23,29,30,31,32,33,34,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,57,58,59,60,61,62,68,69,70,71,72,73,74,75,80,81,82,83,84,85,86,87]
observaciones_validas = np.delete(observaciones, sets_eliminar, axis=0)
print(np.shape(sets_eliminar))
print(np.shape(observaciones_validas))

for j in range(len(observaciones_validas)):
    plt.figure()
    plt.plot(observaciones_validas[j])

