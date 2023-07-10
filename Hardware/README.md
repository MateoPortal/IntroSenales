# Hardware desarrollado
## PCB
La PCB (Printed circuit board o placa de circuito impreso en español) se compone del chip ESP32 WROOM 32E, un microcontrolador de alto rendimiento y bajo consumo de energía, junto con el AD8232, un amplificador de instrumentación utilizado para adquirir señales de ECG en tiempo real (Figura 6). El diseño de la PCB se ha adaptado para alojar tanto el chip ESP32 como el AD8232, además de otros componentes necesarios para su funcionamiento. Se optó por desarrollar la PCB desde cero con el objetivo de reducir el tamaño final del producto y eliminar componentes innecesarios presentes en el kit de desarrollo devkit. Además de evitar el ruido y las capacitancias parásitas. La PCB incluye conectores y pines específicos para garantizar una conexión segura entre el ESP32 y el AD8232, un puerto Jack para la conexión de los electrodos y un puerto micro USB para la carga de programas y algoritmos en el microcontrolador, así como para permitir la comunicación con una computadora.

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Hardware/placaplano.jpeg" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 1. Diseño de la PCB en EasyEda</em>
</p>

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Hardware/placa3d.jpeg" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 2. Diseño de la PCB en 3D</em>
</p>

## Diseño 3D del wearable
Se realizó un diseño 3D del wearable en formato CAD con el uso de \textit{Autodesk Inventor}. El diseño se dividió en dos partes: la carcasa y la tapa. La carcasa, de medidas 120 x 80 x 23.5 mm, es donde irán todos los componentes del dispositivo y cuenta con dos aperturas, la primera para el posicionamiento del \textit{switch} de encendido/apagado y la segunda para la permitir el posicionamiento de los electrodos y la conexión de estos al circuito, ya que este está diseñado para ser usado en el brazo debajo del músculo deltoides. La tapa, por su parte, de dimensiones 120 x 80 x 3.5 mm, se diseñó con una apertura en el centro para el posicionamiento y visualización de la pantalla TFT. Las vistas del diseño pueden verse en las figuras 8-10. 

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Hardware/frontal_assembly_señales.png" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 3. Diseño de la PCB en 3D</em>
</p>

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Hardware/lateral_assembly_señales.png" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 4. Diseño de la PCB en 3D</em>
</p>

<p align="center">
  <img src="https://github.com/MateoPortal/IntroSenales/blob/main/Hardware/isometrica_assembly_señales.png" alt="IMAGEN DE BIENVENIDA" width="35%">
  </p>
<p align="center">
  <em>Imagen 5. Diseño de la PCB en 3D</em>
</p>