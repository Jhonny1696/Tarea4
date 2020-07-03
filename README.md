# Tarea4

## 1. Esquema de modulación BPSK
En el esquema BPSK se cambia la fase de la onda portadora ante el valor del bit que se quiera transmitir. Como onda portadora se utilizó una función senoidal con la siguiente forma: 

<p align="center">
<img src="portadora.png" width="550" />
<br>
</p> 

Ante la llegada de un bit 0 le corresponde un desfase de 0 grados y  ante la llegada de un bit 1 el desfase correspondiente es de 180 grados. Matemáticamente:

<img src="https://latex.codecogs.com/svg.latex?\small&space;s_0(t)&space;=&space;sen(2\pi&space;f&space;t)" title="\small s_0(t) = sen(2\pi f t)" />
<img src="https://latex.codecogs.com/svg.latex?\small&space;s_1(t)&space;=&space;sen(2\pi&space;f&space;t&space;&plus;&space;\pi)&space;=&space;-sen(2\pi&space;f&space;t)" title="\small s_1(t) = sen(2\pi f t + \pi) = -sen(2\pi f t)" />


Con los primeros 15 bits del archivo `bits10k.csv`, se obtiene la señal modulada con la siguiente forma:

<p align="center">
<img src="Tx.png" width="550" />
<br>
</p>

Para obtener este resultado se procedió de la siguiente forma. Se cargó los bits proporcionados en un obketo iterable utilizando el metodo `genfromtext()`, se definió la frecuencia de la onda portadora en 5 kHz y la frecuencia de muestreo en 250 kHz. Para crear la señal, se definieron estos parámetros y se creó un objeto iterable de tipo linspace que se ajusta a los mismos con 0 en todos sus elementos. Luego, en cada espacio de un periodo se sumó la señal sinusoidal asociada al bit correspondiente.

## 2. Potencia promedio de la señal modulada generada
## 3. Canal ruidoso del tipo AWGN con una relación señal a ruido (SNR) desde -2 hasta 3 dB

<p align="center">
<img src="Rx_-1.png" width="550" />
<br>
</p>

<p align="center">
<img src="Rx_0.png" width="550" />
<br>
</p>

<p align="center">
<img src="Rx_1.png" width="550" />
<br>
</p>

<p align="center">
<img src="Rx_2.png" width="550" />
<br>
</p>

<p align="center">
<img src="Rx_3.png" width="550" />
<br>
</p>

## 4. Densidad espectral de potencia de la señal con el método de Welch, antes y después del canal ruidoso

<p align="center">
<img src="densidadEspectral.png" width="550" />
<br>
</p>

<p align="center">
<img src="DensidadEspectral con-1.png" width="550" />
<br>
</p>

<p align="center">
<img src="DensidadEspectral con0.png" width="550" />
<br>
</p>

<p align="center">
<img src="DensidadEspectral con1.png" width="550" />
<br>
</p>

<p align="center">
<img src="DensidadEspectral con2.png" width="550" />
<br>
</p>

<p align="center">
<img src="DensidadEspectral con3.png" width="550" />
<br>
</p>


## 5. Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits
## 6. Grafica BER versus SNR

<p align="center">
<img src="berrVsSnr.png" width="550" />
<br>
</p>
