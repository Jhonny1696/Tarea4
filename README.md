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

Para hallar la potencia promedio se basa en la formula 

<img src="https://latex.codecogs.com/svg.latex?\small&space;P_{sin}&space;=&space;\frac{1}{2T}\int_{T}^{-T}&space;x(t)^2dt" title="\small P_{sin} = \frac{1}{2T}\int_{T}^{-T} x(t)^2dt" />

A nivel de código, se utilizó el metodo `integrate.trapz` para integrar la variable de la señal al cuadrado. El resultado es <img src="https://latex.codecogs.com/svg.latex?\inline&space;\small&space;P_{sin}&space;=&space;0,49" title="\small P_{sin} = 0,49" />.
## 3. Canal ruidoso del tipo AWGN con una relación señal a ruido (SNR) desde -2 hasta 3 dB

Para simular el canal ruidoso se utiliza una distribución normal definida por la media <img src="https://latex.codecogs.com/svg.latex?\inline&space;\small&space;\mu&space;=&space;0" title="\small \mu = 0" /> y por la desviación estandard 

<img src="https://latex.codecogs.com/svg.latex?\small&space;\sigma&space;=&space;\sqrt{P_{n}}" title="\small \sigma = \sqrt{P_{n}}" />
donde 

<img src="https://latex.codecogs.com/svg.latex?\small&space;P_s&space;=&space;\frac{P_{sin}}{10&space;^\frac{SNR}{10}}" title="\small P_s = \frac{P_{sin}}{10 ^\frac{SNR}{10}}" />

Teniendo el modelo del canal ruidoso, se definió un lista con los valores de SNR requeridos (-2 a 3) y con eso se realizó la simulación, se le sumó el ruido a la señal que se había definido y se grafíco. A continuación se presentan las formas de la señal Rx resibida para cada nivel de SNR:

<p align="center">
<img src="Rx_-2.png" width="550" />
<br>
</p>

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

Se observa como con un nivel de SNR de -2 el ruido es mayor que con un nivel de 3, pues para valores más grandes de SNR el ruido se hace cada vez más despreciable en relaión con la señal original.

## 4. Densidad espectral de potencia de la señal con el método de Welch, antes y después del canal ruidoso

Se utilizó el método `welch` para obener la densidad espectral de la potencia de las señales.

<p align="center">
<img src="densidadEspectral (1).png" width="550" />
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

se utliza el producto interno de dos funciones, en este caso la primera función es la señal transmitida y la segunda es la señal portadora. 
Por defición el producto interno de dos funciones es igual a 

<img src="https://latex.codecogs.com/svg.latex?\small&space;(f,g)&space;=&space;\int_{a}^{b}f(t)g(t)dt" title="\small (f,g) = \int_{a}^{b}f(t)g(t)dt" />

de esta forma, cuando el bit transmitido es 1

<img src="https://latex.codecogs.com/svg.latex?\small&space;f(t)g(t)=&space;sen^2(2\pi&space;f&space;t)" title="\small f(t)g(t)= sen^2(2\pi f t)" />

y cuando el bit transmitido es 0 

<img src="https://latex.codecogs.com/svg.latex?\small&space;f(t)g(t)=&space;-sen^2(2\pi&space;f&space;t)" title="\small f(t)g(t)= -sen^2(2\pi f t)" />

Así cuando se resiva un 1 el producto interno será positivo y cuando llega un cero el producto interno es negativo. Por esta razón se escoge un humbral igual a 0 para la decodificación de los bits.

## 6. Grafica BER versus SNR
Se realizó la demulación para cada nivel de SNR y se calculó el error al comparar los bits transmitdos con los resividos. La gráfica del error contra el SNR se muestra a continuación:

<p align="center">
<img src="berrVsSnr.png" width="550" />
<br>
</p>

Se observa como el nivel del error se mantiene en cero para los diferentes niveles de SNR, por lo que se puede decir que le humbral escogido es correcto.
