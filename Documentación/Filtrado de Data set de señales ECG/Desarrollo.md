# Filtrado de Data set de señales ECG
Laboratorio 7

### Fecha: 3 de mayo de 2023

## Objetivo 🎯
En una sesión anterior (Laboratorio 6), se realizó la creación del Data set de señales ECG obtenidas en otra sesión (Laboratorio 4). En esta oportunidad, realizamos el filtrado de estas señales. Utilizamos los tipos de filtro IIR(Infinite Impulse Response) y FIR(Finite Impulse Response) para las señales ECG en reposo, durante la exhalación e inhalación y posterior a realizar actividad física.

## ¿Qué es un filtro? 
En el campo del procesamiento de señales, un filtro es un dispositivo o proceso cuyo objetivo es suprimir, total o parcialmente, componentes o características no deseadas de una señal. Esto generalmente significa eliminar algunas frecuencias para suprimir las señales de interferencia y reducir el ruido de fondo.
A pesar que la tarea de los filtros es bastante simple, representan una pieza fundamental en el procesamiento de señales en la electrónica actual [1].

En esta sesión, trabajaremos con los filtros digitales IIR y FIR.

Filtro FIR:
Este tipo de filtro genera una respuesta de impulso finito de un sistema dinámico. En otras palabras, la respuesta de impulso proporcionada por el filtro es de duración finita en este caso.
En los filtros FIR, la retroalimentación no está presente, por lo que estos filtros operan solo con valores de entrada actuales y pasados. Consecuentemente, la salida es la suma de una cantidad finita de muestras finitas de valores de entrada. Esto los hace sumamente estables[2].

Filtro IIR:
Este filtro digital está diseñado para generar una respuesta de impulso infinita de un sistema dinámico. Presenta un mecanismo de retroalimentación interno, por lo que el filtro opera por un período de tiempo indefinido. Los filtros IIR son utilizados por los sistemas que generan una respuesta infinita.
El filtro IIR funciona de manera que no solo se tienen en cuenta las entradas actuales y pasadas, sino también la muestra de salida pasada [2].

## Dataset filtrado 

## Referencias
[1] DEWESoft d.o.o, “Signal filtering, Signal suppression, Signal processing | Dewesoft,” Dewesoft.com, 2023. https://training.dewesoft.com/online/course/filters#fir-and-iir-filters (accessed May 04, 2023).
[2] Roshni Y, “Difference Between FIR Filter and IIR Filter (with Comparison chart) - Circuit Globe,” Circuit Globe, Mar. 24, 2020. https://circuitglobe.com/difference-between-fir-filter-and-iir-filter.html#Definition (accessed May 04, 2023).
