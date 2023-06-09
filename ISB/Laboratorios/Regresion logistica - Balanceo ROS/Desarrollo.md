# Laboratorio 10

### Fecha: 7 de junio de 2023



## Tabla de contenidos
 1. [Objetivos]
 2. [Materiales]
 3. [Resultados]
 4. [Discusión]
 5. [Bibliografía]

## Objetivos

* Extraer características de la base de datos.
* Entrenamiento del modelo de Regresión Logistica.
* Evaluar las métricas del modelo entrenado. 
* Balanceo del conjunto de datos y posteriormente evaluar las métricas.

## Materiales

### Dataset (Base de datos)

Se utilizó una base de datos de 7 variables independientes y de 1 variable dependiente . La base de datos se adapta para utilizar en un modelo de machine learning de clasificación.

Variables independientes : [C, Rp, Dif_vol, V_in, V_out, P_ventilador, PIP]   </p>
Variable dependiente : Error_aceptable   </p>



<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/muestradedatos.JPG" alt="2hilo" width="40%">
  </p>

 <p align="center">
 Figura 1. Muestras de la base de datos : </em>
  </p>


### Código 

[Libro Jupyter](https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Balanceo_ROS(2).ipynb)

## Discusión

### Modelo a utilizar

La regresión logística es uno de los métodos estadisticos mas utilizado para la clasificación y el más sencillo.  Es una técnica basada en el análisis de regresión estadística utilizada para modelar la relación entre una variable dependiente binaria y una o más variables independientes. Se usa generalmente cuando la variable dependiente representa un resultado binario, como por ejemplo de tipo Si/No, enfermo/sano, etc. La función logística, también conocida como función sigmoidea, asigna cualquier número de valor real a un valor entre 0 y 1, que representa la probabilidad de que ocurra el evento. Esta es una gran ventaja con respecto a otros modelos pues los resultados se muestran como una probabilidad de pertenecer a una de dos categorías. Para llegar a ello, este modelo estima los coeficientes de las variables independientes, que representan el cambio en las probabilidades logarítmicas de la variable dependiente asociada con un cambio de una unidad en la variable independiente correspondiente, suponiendo que todas las demás variables se mantienen constantes. El valor de estas variables se estima usualmente con el método de máxima verosimilitud.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/Imag1.JPG" alt="2hilo" width="40%">
  </p>

<p align="center">
 Figura 2. Matriz de confusión del modelo creado  </em>
</p>


### Procesamiento de datos

Para efectuar un procesamiento de datos adecuado, es esencial iniciar con la eliminación de aquellas muestras que carecen de variables significativas, también conocidas como variables independientes. Una vez realizado este paso, procedemos a determinar cuáles de estas variables se incorporarán en el conjunto de entrenamiento. Es relevante mencionar que si una variable en el conjunto de datos resulta ser constante (posee una única categoría), no se tomará en cuenta o, de lo contrario, no tendría influencia sobre el entrenamiento.

En la etapa posterior, evaluamos la distribución de la variable dependiente, con el objetivo de identificar cualquier posible desbalance en los datos. Este análisis es crucial para asegurar la precisión y eficacia del modelo de aprendizaje automático que se está construyendo.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/balanceo1.png" alt="2hilo" width="40%">
  </p>

La selección de las variables a utilizar en el modelo de aprendizaje automático es una fase crucial del proceso. Este paso se realizará mediante un procedimiento aleatorio, lo que garantiza una representación equitativa y no sesgada de todas las posibles variables presentes.

Posteriormente, procedemos a dividir nuestros datos en dos conjuntos distintos: uno de entrenamiento y uno de prueba. La proporción utilizada para esta partición es tal que el (75%) de los datos se asignarán para entrenamiento y el (25%) restante se reservará para pruebas.

### Entrenamiento del modelo

Se realizó el conjunto el entranamiento del modelo con las muestras anteriormente seleccionadas. Para ello, se utilizó la libreria sckit-learn. 

Luego del entrenamiento se realiza un análisis de los coeficientes utilizando la libreria statsmodels para evaluar si efectivamente las variables son óptimas para el modelo. Para determinar si son óptimas se debe tener en cuenta que el p-value de cada variable debe ser menor a 0.05. 

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/Captura.JPG" alt="2hilo" width="40%">
  </p>

<p align="center">
 Figura 3. Análisis del p- value de los coeficientes  </em>
  </p>

Se observa que en este caso, en una variable no se logra obtener un p-value deseado. 

### Métricas del modelo y Matriz de Confusión

Analizaremos algunas métricas del modelo de regresión logística, principalmente la precisión y el recall.

La precisión es una métrica que indica cuán exactas son las predicciones positivas del modelo. En este caso, la precisión general es del 83%, lo que significa que el modelo predijo correctamente el 83% de las veces. Si desglosamos por clases, tenemos una precisión del 75% para la clase 0 y del 86% para la clase 1.

Por otro lado, el recall indica qué proporción de casos positivos reales fueron identificados correctamente por el modelo. El recall para la clase 0 es del 60%, lo que quiere decir que el modelo identificó correctamente el 60% de los casos de esta clase. Para la clase 1, el recall es del 92%, es decir, el modelo identificó correctamente el 92% de los casos de esta clase.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/metricasmodelo.JPG" alt="2hilo" width="50%">
  </p>


<p align="center">
 Figura 4. Análisis de las métricas del modelo  </em>
  </p>

La matriz de confusión es una herramienta útil para entender el rendimiento de un modelo de clasificación. 

En la primera fila, 3 representa los Verdaderos Positivos (TP), es decir, los casos que fueron correctamente identificados como positivos (clase 1). Luego, 2 representa los Falsos Positivos (FP), los casos que fueron incorrectamente identificados como positivos (clase 1) aunque en realidad son negativos (clase 0).

En la segunda fila, 1 representa los Falsos Negativos (FN), es decir, los casos que fueron incorrectamente identificados como negativos (clase 0) aunque son en realidad positivos (clase 1). Finalmente, 12 son los Verdaderos Negativos (TN), los casos que fueron correctamente identificados como negativos (clase 0).

Por lo tanto, el modelo ha predicho correctamente la mayoría de los casos, con solo 3 errores (2 Falsos Positivos y 1 Falso Negativo). Esto muestra que el modelo tiene un buen desempeño, aunque tiende a clasificar incorrectamente los casos negativos como positivos un poco más a menudo.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/matrizconfusion1.png" alt="2hilo" width="60%">
</p>

<p align="center">
 Figura 5. Matriz de confusión del modelo creado  </em>
</p>


### Balanceo ROS

Dado que el conjunto de entrenamiento consta de 51 muestras (11 negativas y 40 positivas), es necesario realizar un balanceo mediante el método de sobremuestreo aleatorio (Random OverSampling, ROS) para abordar el problema del desequilibrio de clases.

Este desequilibrio puede llevar a que el modelo de aprendizaje automático aprenda más sobre la clase dominante (en este caso, la positiva), lo que podría resultar en un sesgo hacia esa clase. Esto significa que el modelo puede no ser tan efectivo para detectar la clase minoritaria (en este caso, la negativa) ya que ha tenido menos datos para aprender sobre ella.

### Métricas del modelo y Matriz de Confusión con el Modelo ROS

Después de aplicar el balanceo mediante ROS, se revisan los p-values de las variables nuevamente. Los nuevos p-values para las variables V_dif y PIP son 0.037976 y 0.005582 respectivamente, ambos valores por debajo del umbral estándar de 0.05. Por lo tanto, las variables son estadísticamente significativas y aportan información útil para el modelo.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/coeficientes2.JPG" alt="2hilo" width="40%">
  </p>


<p align="center">
 Figura 6. Análisis de p value de los coeficientes luego del ROS  </em>
  </p>

Posteriormente, se analizan las métricas del modelo con el conjunto de datos balanceado. La tabla de métricas es la siguiente:

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/metricas2.JPG" alt="2hilo" width="40%">
  </p>


<p align="center">
 Figura 7. Análisis de métricas luego del ROS  </em>
  </p>

Para la clase 0, se observa un incremento notable en el recall, llegando al 100%, aunque la precisión ha disminuido a 62%. La clase 1 mantiene una precisión perfecta, pero su recall ha disminuido al 77%. En general, la precisión y el recall promedio ponderado para el modelo son 90% y 83% respectivamente, mostrando una mejora en comparación con el modelo anterior sin balancear.

Estos resultados sugieren que el balanceo de los datos ha permitido al modelo mejorar en la identificación de la clase minoritaria, a costa de algunas predicciones incorrectas en la clase mayoritaria. Esta es una compensación común en la clasificación, y la elección entre precisión y recall depende del problema específico que se esté resolviendo.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/matrizconfusionfinal.png" alt="2hilo" width="60%">
  </p>


<p align="center">
 Figura 8. Matriz de confusión luego del ROS  </em>
  </p>


## Bibliografía


[1] Heras, J. M. Regresión Logística para Clasificación - IArtificial.net. 2020. Available from: https://www.iartificial.net/regresion-logistica-para-clasificacion/

[2] Horacio Chitarroni. La regresión logística. Diciembre, 2002. Available from: https://racimo.usal.edu.ar/83/1/Chitarroni17.pdf

[3] González, J. R. 6 Regresión logística | Aprendizaje Automático. vol 1. 2021 Nov. Available from: https://isglobal-brge.github.io/Aprendizaje_Automatico_1/regresi%C3%B3n-log%C3%ADstica.html


[def]: ttps://github.com/MateoPortal/IntroSenales/blob/main/ISB/Laboratorios/Regresion%20logistica%20-%20Balanceo%20ROS/Imagenes/balanceo1.jp
[def2]: def
