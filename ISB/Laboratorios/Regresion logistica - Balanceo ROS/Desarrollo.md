# Laboratorio 10

### Fecha: 7 de junio de 2023



## Tabla de contenidos
 1. [Objetivos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#objetivos)
 2. [Materiales](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#materiales)
 3. [Procedimientos](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#procedimientos)
 4. [Resultados](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#resultados-del-ploteo-de-la-se%C3%B1al-en-python)
 5. [Discusión](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#discusi%C3%B3n)
 6. [Bibliografía](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/Desarrollo.md#bibliograf%C3%ADa)

## Objetivos

* Extraer características de la base de datos.
* Entrenamiento del modelo de Regresión Logistica.
* Evaluar las métricas del modelo entrenado. 
* Balanceo del conjunto de datos y posteriormente evaluar las métricas.

## Materiales

### Dataset (Base de datos)

Se utilizó una base de datos de 7 variables independientes y de 1 variable dependiente . La base de datos se adapta para utilizar en un modelo de machine learning de clasificación.

Variables in dependientes : [C, Rp, Dif_vol, V_in, V_out, P_ventilador, PIP]   </p>
Variable dependiente : Error_aceptable   </p>
Muestras de la base de datos : 

### Código 

[Descargar código de Python](https://github.com/MateoPortal/IntroSenales/blob/main/Documentaci%C3%B3n/Laboratorio5/py.txt)

## Discusión

### Modelo a utilizar



### Procesamiento de datos

Para efectuar un procesamiento de datos adecuado, es esencial iniciar con la eliminación de aquellas muestras que carecen de variables significativas, también conocidas como variables independientes. Una vez realizado este paso, procedemos a determinar cuáles de estas variables se incorporarán en el conjunto de entrenamiento. Es relevante mencionar que si una variable en el conjunto de datos resulta ser constante (posee una única categoría), no se tomará en cuenta o, de lo contrario, no tendría influencia sobre el entrenamiento.

En la etapa posterior, evaluamos la distribución de la variable dependiente, con el objetivo de identificar cualquier posible desbalance en los datos. Este análisis es crucial para asegurar la precisión y eficacia del modelo de aprendizaje automático que se está construyendo.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/balanceo1.png" alt="2hilo" width="50%">
  </p>

La selección de las variables a utilizar en el modelo de aprendizaje automático es una fase crucial del proceso. Este paso se realizará mediante un procedimiento aleatorio, lo que garantiza una representación equitativa y no sesgada de todas las posibles variables presentes.

Posteriormente, procedemos a dividir nuestros datos en dos conjuntos distintos: uno de entrenamiento y uno de prueba. La proporción utilizada para esta partición es tal que el (75%) de los datos se asignarán para entrenamiento y el (25%) restante se reservará para pruebas.


### Estandarización de caracteristicas




### Entrenamiento del modelo



### Métricas del modelo



### Balanceo ROS


## Bibliografía
[1] “BITalino (r)evolution Lab Guide.” Revisado en: Abril 19, 2023. [Online]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[2] Rayi A, Murr N. Electroencephalogram. [Updated 2022 Oct 3]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2023 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK563295/

[3] Y. Zhu, Q. Wang, and L. Zhang, “Study of EEG characteristics while solving scientific problems with different mental effort,” Scientific Reports, vol. 11, no. 1, 2021. 

[4] X. Zeng, X. Zhao, S. Wang, J. Qin, J. Xie, X. Zhong, J. Chen, and G. Liu, “Affection of facial artifacts caused by micro-expressions on Electroencephalography signals,” Frontiers in Neuroscience, vol. 16, 2022. 
