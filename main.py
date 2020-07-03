import numpy as np
import csv
from scipy import stats
from scipy import signal
from scipy import integrate
from numpy import genfromtxt
import matplotlib.pyplot as plt

'''
Punto #1: Esquema de modulación BPSK
'''

# Los bits a transmitir obtenidos del bits10k.csv
bits = genfromtxt("bits10k.csv", delimiter = ',')


# Número de bits
N = len(bits)

# Se define la frecuencia de la onda portadora
f = 5000

# Periodo de símbolo
T = f**(-1)

# Cantidad de muestras a tomar por periodo
p = 50

# Puntos de muestreo
tp = np.linspace(0, T, p)

# Onda portadora
sinus = np.sin(2*np.pi * f * tp)

# Se grafica la portadora
plt.figure(figsize=(8, 5))
plt.plot(tp, sinus, color = 'black')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de portadora')
plt.title('Onda portadora')
plt.savefig('portadora.png')

# Frecuencia de muestreo
fs = p/T # 250 kHz

# Creación de la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal
senal = np.zeros(t.shape)

# Creación de la señal modulada BPSK
for k, b in enumerate(bits):
    senal[k*p:(k+1)*p] = sinus if b else -sinus

# Se grafica los primeros bits modulados
pb = 15
tp = np.linspace(0, pb*T, pb*p)
plt.figure(figsize=(8, 5))
plt.plot(tp, senal[0:pb*p])
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud de la señal")
plt.title('Señal modulada')
plt.savefig('Tx.png')

'''
Punto 2: Potencia promedio de la señal modulada
'''
# Potencia instantánea
Pinst = senal**2

# Potencia promedio (W)
Ps = integrate.trapz(Pinst, t) / (N * T)

print('Potencia promedio: ', Ps)

'''
Punto 3: Simulación del canal ruidoso tipo AWGN 
'''
# Relaciones señal a ruido solicitadas
rango_SNR = [-2, -1, 0, 1, 2, 3]

for SNR in rango_SNR:
  # Potencia del ruido para SNR y potencia de la señal dadas
  Pn = Ps / (10**(SNR / 10))

  # Desviación estándar del ruido
  sigma = np.sqrt(Pn)

  # Crear ruido (Pn = sigma^2)
  ruido = np.random.normal(0, sigma, senal.shape)

  # Simular "el canal": señal recibida
  Rx = senal + ruido

  # Visualización de los primeros bits recibidos
  plt.figure()
  plt.plot(Rx[0:pb*p], color = 'black')
  plt.xlabel("Tiempo (s)")
  plt.ylabel("Amplitud de la señal")
  plt.title("Rx para SNR = " + str(SNR) + " dB")
  plt.savefig('Rx_' + str(SNR)+ '.png')
  


"""
Punto 4: Grafica de la densidad espectral de potencia de la señal con el método de Welch
"""
# Se grafica la densidad espectral antes del canal ruidoso
frecuencia_w, PSD = signal.welch(senal, fs)
plt.figure()
plt.semilogy(frecuencia_w, PSD, color = 'black')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig("densidadEspectral.png")


'''
Punto 5: Demulación y codificación
'''
vector_BER = []

# Relación señal-a-ruido deseada
for SNR in rango_SNR:

    # Potencia del ruido para SNR y potencia de la señal dadas
    Pn = Ps / (10**(SNR / 10))

    # Desviación estándar del ruido
    sigma = np.sqrt(Pn)

    # Crear ruido (Pn = sigma^2)
    ruido = np.random.normal(0, sigma, senal.shape)

    # Simular "el canal": señal recibida
    Rx = senal + ruido

    # Pseudo-energía de la onda original
    Es = np.sum(sinus**2)

    # Inicialización del vector de bits recibidos
    bitsRx = np.zeros(bits.shape)

    # Decodificación de la señal por detección de energía
    for k, b in enumerate(bits):
        # Producto interno de dos funciones
        Ep = np.sum(Rx[k*p:(k+1)*p] * sinus)
        if Ep > 0:
          bitsRx[k] = 1

        else:
          bitsRx[k] = 0
    
    # Se grafica densidad espectral despues del canal ruidoso
    fw, PSD = signal.welch(Rx, fs)
    plt.figure()
    plt.semilogy(fw, PSD, color = 'black')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Densidad espectral de potencia')
    plt.title("Densidad espectral de potencia con SNR de " + str(SNR) + " dB")
    plt.savefig("DensidadEspectral con" + str(SNR) + ".png")

    # err es la cantidad de bits erróneros en la señal recibida con respecto a la transmitida
    err = np.sum(np.abs(bits - bitsRx))
    vector_BER.append(err/N)

'''
Punto 6: Grafica de BER vs SNR
'''

# Graficación de BER vs SNR
plt.figure()
plt.plot(rango_SNR, vector_BER, color = 'black')
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title('BER vs SNR')
plt.savefig('berrVsSnr')