# Análisis de señales ECG
Laboratorio 8

### Fecha: 24 de mayo de 2023

## Objetivo 🎯
En una sesión anterior (Laboratorio 4), se obtuvieron señales ECG a través de un BITalino. Estas señales fueron adquiridas en diferentes contextos: en reposo, durante la exhalación e inhalación y durante la realización de actividad física. En esta oportunidad, analizaremos estas muestras mediante la aplicación de un algoritmo para la detección de los complejos QRS [1].

## ¿Qué es un complejo QRS?
El llamado Complejo QRS es el registro del movimiento de los impulsos elécttricos a través de las cavidades inferiores del corazón (ventrículos) [2].

El vector del complejo QRS puede dividirse en 3 derivadas distintas [3]:

-1er vector: corresponde a la despolarización del tabique interventricular, produciendo un pequeño vector que se dirige hacia abajo y a la derecha

-2do vector: Los siguientes en despolarizaarse son el ventrículo izquierdo y parte del ventrículo derecho, generando un gran vector que se dirige hacia abajo y a la izquierda.

-3er vector: el último en despolarizarse es la parte basal del ventrículo derecho, originando un pequeño vector que se dirige hacia atrás, hacia arriba y a la derecha.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/An%C3%A1lisis%20de%20se%C3%B1ales%20ECG/imagenes/qrs.jpg" width="60%">
  </p>
<p align="center">
  <i> Distribución impulso cardiaco y ondas e intervalos del electrocardiograma [3]</i>
  </p>
 
## Aplicación del Algoritmo
A continuación, presentamos nuestras señales ECG con el algoritmo aplicado:

**Señales ECG durante reposo**

**Señales ECG después exhalación e inhalación**

**Señales ECG después del realizar ejercicio**

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/An%C3%A1lisis%20de%20se%C3%B1ales%20ECG/imagenes/deporte_filtrado1.jpg" width="60%">
  </p>
<p align="center">
  <i> Señales ECG filtradas (Amplitud Vs. Tiempo (s))</i>
  </p>

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/An%C3%A1lisis%20de%20se%C3%B1ales%20ECG/imagenes/threshold.jpg" width="60%">
  </p>
<p align="center">
  <i> Análisis de Threshold (Amplitud Vs. Muestras[n])</i>
  </p>
  
 <p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/An%C3%A1lisis%20de%20se%C3%B1ales%20ECG/imagenes/deporte_filtrado.jpg" width="60%">
  </p>
<p align="center">
  <i>  (Amplitud Vs. Muestras[n])</i>
  </p>


## Referencias
[1] J. Pan and W. J. Tompkins, “A Real-Time QRS Detection Algorithm,” vol. BME-32, no. 3, pp. 230–236, Mar. 1985, doi: https://doi.org/10.1109/tbme.1985.325532.

‌[2] “Componentes e intervalos en un electrocardiograma (ECG) | Cigna,” Cigna.com, 2022. https://www.cigna.com/es-us/knowledge-center/hw/componentes-e-intervalos-en-un-electrocardiograma-zm2308 (accessed May 24, 2023).

[3] SEIC, “Complejo QRS,” Ecocardio.com, 2018. https://ecocardio.com/documentos/biblioteca-preguntas-basicas/preguntas-al-cardiologo/1046-complejo-qrs.html (accessed May 24, 2023).
‌
