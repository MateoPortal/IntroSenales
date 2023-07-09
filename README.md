# Addressing detection of left bundle branch block by means of electrocardiogram’s signals using Machine Learning algorithms
Authors: Aldave A., Huaylinos J., Portal M., Postigo R., Saavedra T. y Salvatierra D.
## Resumen
En el presente proyecto, abordamos la detección de la izquierda bloqueo de rama la rama izquierda (BRI) a través del análisis de señales de  electrocardiograma (ECG) utilizando algoritmos de aprendizaje automático.
El BRI es una enfermedad cardiovascular que afecta el sistema de conducción eléctrica del corazón y puede indicar la presencia de enfermedades subyacentes. La detección temprana de BRI es crucial para evaluar el pronóstico del paciente y tomar medidas preventivas. Con este fin, adquirimos conjuntos de datos de ECG de pacientes con BRI, pacientes sanos y pacientes con fibrilación auricular. Realizamos el preprocesamiento de la señal, la extracción de características y la clasificación utilizando los algoritmos Support Vector Machine (SVM) y Random Forest (RF).
Nuestros resultados demuestran la efectividad de estos algoritmos para detectar con precisión el BRI de las señales de ECG. Este enfoque podría mejorar la detección y el tratamiento de enfermedades cardiovasculares relacionadas con el BRI.
<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Proyecto%20/Im%C3%A1genes/lbbb.png" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen1. Electrocardiograma del bloqueo de rama izquierda</em>
</p>

## Motivación
La principal motivación de nuestro estudio es, al utilizar técnicas de aprendizaje automático, automatizar y agilizar el proceso de detección del Bloqueo de la rama izquierda (BRI), lo que puede conducir a un diagnóstico más temprana, un tratamiento más efectivo y una mejora en los resultados clínicos de los pacientes. De manera secundaria, esta investigación puede llevar a mejorar el diagnóstico y el tratamiento de las enfermedades cardiovasculares, particularmente aquellas relacionadas con el BRI. Además, al utilizar algoritmos de clasificación como SVM y Random Forest, se busca desarrollar un modelo preciso y confiable para la detección de LBBB a partir de las señales del ECG, lo que puede tener un impacto significativo en la práctica clínica y en la salud cardiovascular en general.
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
--------------------------------------------------------------------------------------------------------------------------
# Introducción a Señales Biomédicas - Equipo 10

Bienvenidos al repositorio del Equipo 10 del curso "Introducción a Señales Biomédicas" del ciclo 2023-1✨

## Tabla de contenidos

 1. [Contenido del curso](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#contenido-del-curso)
 2. [¿Qué es una bioseñal?](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#qu%C3%A9-es-una-biose%C3%B1al)
 3. [Señal de Interés](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#se%C3%B1al-de-inter%C3%A9s)
 4. [Temática del proyecto](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#tem%C3%A1tica-del-proyecto)
 5. [Materiales](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#materiales)
 6. [Metodología](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#metodolog%C3%ADa)
 7. [Docentes del curso](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#docentes-del-curso)
 8. [Miembros del equipo](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#miembros-del-equipo-e10)
 9. [Referencias](https://github.com/MateoPortal/IntroSenales/blob/main/README.md#referencias)


## Contenido del curso

<p align="center">
  <img src="https://user-images.githubusercontent.com/70663170/227679635-0451f4bf-2ef3-4582-98ab-ae85d2c239d6.png" alt="IMAGEN DE BIENVENIDA" width="25%">
  </p>
<p align="center">
  <em>Imagen1. Animación de una Onda P</em>
</p>



<p align="justify">
Este curso desarrollará los conocimientos necesarios para el tratamiento de señales provenientes de dispositivos médicos. Se abordaron temas como: el estudio de los sensores, la tecnología de adquisición, los procesos clínicos en los que se dan y protocolos que se usan para compartir la información entre los diferentes equipos que brindan señales. Las clases se desarrollarán en un laboratorio donde se complementará la teoría brindada con simulaciones en computadora utilizando programas desarrollados en Python y kits de desarrollo para la adquisición de bioseñales.
</p>

## ¿Qué es una bioseñal?
<p align="justify">
Se define como una señal producida por la actividad eléctrica que surge de una actividad biológica, la cual toma lugar en diferentes tejidos y órganos dentro del cuerpo humano [1]. 
Las bioseñales proveen información útil sobre el estado fisiológico, patofisiológico y emocional de un individuo, jugando un rol fundamental en el monitoreo de la salud y en los diagnósticos clínicos.
El procesamiento y el análisis de estas señales son manejados por un área interdisciplinaria y dinámica, contando con ciencias como biología, física, medicina, ingeniería y ciencias de la computación [2].
Entre los tipos de métodos más comunes para registrar este tipo de señales en el ámbito clínico está la Electroencefalografía (EEG), la Magnetoencefalografía (MEG), la Electrocardiogra (EMG), el Electrocardiograma (ECG o EKG), entre otros [1].
</p>

## Señal de interés: 
### __Electrocardiograma (ECG)__
<p align="justify">
Es una prueba médica que registra la actividad eléctrica del corazón usando electrodos colocados en la piel. Se utiliza para diagnosticar y monitorear diversas afecciones cardíacas, como arritmias, ataques cardíacos e insuficiencia cardíaca. La máquina de ECG registra los impulsos eléctricos generados por el corazón y proporciona una representación visual de la actividad del corazón en forma de gráfico. Un ECG se puede realizar en un consultorio médico, clínica u hospital y es un procedimiento no invasivo e indoloro.
</p>
<p align="center">
  <img src="Documentación/Images/importancia-del-electrocardiograma.jpg" alt="ecg" width="50%">
</p>
<p align="center">
 <em>Imagen2. Onda P</em>
</p>

## Temática del proyecto
<p align="justify">
Por desarrollar durante el semestre.
</p>


## Materiales
<p align="justify">
Por desarrollar durante el semestre.
</p>

## Metodología
<p align="justify">
Por desarrollar durante el semestre.
</p>


## Docentes del curso: 
- De la Cruz Rodriguez, Lewis - umbert.de.la.cruz@upch.pe
- Meza Rodriguez, Moises - moises.meza@upch.pe
- Roman Gonzalez, Avid - avid.roman-gonzalez@ieee.org
- Venancio Huerta, Julissa - julissa.venancio@upch.pe
- Cáceres del Aguila, Jose Alonso - jo.alonsok@gmail.com


## Miembros del equipo E10:
- Aldave Javier, Alessandra Mercedes - alessandra.aldave@upch.pe
- Huaylinos Guerrero, Jose Augusto Modesto - jose.huaylinos@upch.pe
- Portal Von Hesse, Mateo Luis - mateo.portal@upch.pe
- Postigo Yauce, Rosmy Leyla - rosmy.postigo@upch.pe
- Saavedra Barboza, Tayel Christian - tayel.saavedra@upch.pe
- Salvatierra Guillermo, Diego Paul - diego.salvatierra@pucp.edu.pe




## Referencias
[1] V. C. Pezoulas, T. P. Exarchos, and D. I. Fotiadis, “Types and sources of medical and other related data,” *Medical Data Sharing, Harmonization and Analytics*, pp. 19–65, 2020, doi: https://doi.org/10.1016/b978-0-12-816507-2.00002-5.

[2] “Signals,” *Mdpi.com*, 2023. https://www.mdpi.com/journal/signals/special_issues/Biosignals_Processing_Analysis_Biomedicine (accessed Mar. 25, 2023).
