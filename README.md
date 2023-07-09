# Addressing detection of left bundle branch block by means of electrocardiogram’s signals using Machine Learning algorithms
# Abordaje de la detección de Bloqueo de la rama izquierda por medio de señales de electrocardiograma utilizando algoritmos de Machine Learning
Aldave A., Huaylinos J., Portal M., Postigo R., Saavedra T. y Salvatierra D.
## Resumen
En el presente proyecto, abordamos la detección de la izquierda bloqueo de rama la rama izquierda (BRI) a través del análisis de señales de  electrocardiograma (ECG) utilizando algoritmos de aprendizaje automático.
El BRI es una enfermedad cardiovascular que afecta el sistema de conducción eléctrica del corazón y puede indicar la presencia de enfermedades subyacentes. La detección temprana de BRI es crucial para evaluar el pronóstico del paciente y tomar medidas preventivas. Con este fin, adquirimos conjuntos de datos de ECG de pacientes con BRI, pacientes sanos y pacientes con fibrilación auricular. Realizamos el preprocesamiento de la señal, la extracción de características y la clasificación utilizando los algoritmos Support Vector Machine (SVM) y Random Forest (RF).
Nuestros resultados demuestran la efectividad de estos algoritmos para detectar con precisión el BRI de las señales de ECG. Este enfoque podría mejorar la detección y el tratamiento de enfermedades cardiovasculares relacionadas con el BRI.
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/lbbb.png" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 1. Electrocardiograma del bloqueo de rama izquierda</em>
</p>

## Motivación
La principal motivación de nuestro estudio es, al utilizar técnicas de aprendizaje automático, automatizar y agilizar el proceso de detección del Bloqueo de la rama izquierda (BRI), lo que puede conducir a un diagnóstico más temprana, un tratamiento más efectivo y una mejora en los resultados clínicos de los pacientes. De manera secundaria, esta investigación puede llevar a mejorar el diagnóstico y el tratamiento de las enfermedades cardiovasculares, particularmente aquellas relacionadas con el BRI. Además, al utilizar algoritmos de clasificación como SVM y Random Forest, se busca desarrollar un modelo preciso y confiable para la detección de LBBB a partir de las señales del ECG, lo que puede tener un impacto significativo en la práctica clínica y en la salud cardiovascular en general.
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/anciano_preview_rev_1.png" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 2. Motivación del proyecto </em>
</p>

## Principales hallazgos
### Cantidad de datos utilizados
La segmentación de la derivación bipolar I de 100 pacientes sanos (Normal), de 100 pacientes con BRI y de 100 pacientes con FA resultó en 781 latidos pertenecientes a pacientes sanos, 746 latidos de pacientes con BRI y 1007 latidos de pacientes con FA. Adicionalmente, 30 latidos fueron segmentados a partir de la señal de la paciente voluntaria con BRI, ver la siguiente tabla.
| Clase | Número de latidos | 
|-----------|-----------|
| Normal   | 871   | 
|  BRI  | 746 | 
|  FA  | 1007   | 
|  BRI (voluntaria)  | 30   | 
### Métricas resultantes de clasificación con Support Vector Machine y Random Forest
A continuación, presentamos una tabla comparativa entre ambos métodos de aprendizaje supervisado que utilizamos para la detección de BRI
|  | Métricas | Normal | BRI | FA | Promedio |
|-----------|-----------|-----------|-----------|-----------|-----------|
| SVM   | Accuracy (%)   | -   | -   | -   | 82.54 |
|    |  Preccision (%) | 75.20 | 98.39 | 75.66 | 82.59 |
|    | Recall (%)   | 71.21 | 97.6 | 79.86 | 82.54 |
|    | F1 Score (%)   | 73.15 | 97.99 | 77.70 | 82.53 |
| RF  | Accuracy (%)  | -  | -  | -  | 89.14  |
|   | Preccision (%)  | 85.11 | 95.93 | 87.03 | 89.06 |
|   | Recall (%) | 84.15 | 98.33 | 86.15 | 89.14 |
|   | F1 Score (%)  | 84.63 | 97.12  | 86.59 | 89.10 |

## Sobre el equipo
Puede visualizar la información sobre el equipo (entregable 1) en el siguiente [enlace](https://github.com/MateoPortal/IntroSenales/tree/main/ISB)

