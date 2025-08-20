import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import continuous_plotter, discrete_plotter

def run():
    # Parámetros
    fm = 0.5   # Hz
    fc = 8.0   # Hz
    m = 0.5
    fs = 64    # Frecuencia de muestreo (Hz)
    N = 256    # Número de muestras

    t = np.arange(N) / fs
    x_t = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

    # Gráfica continua y discreta
    continuous_plotter(t, x_t, title="Señal Continua x(t)")
    discrete_plotter(t, x_t, title="Señal Muestreada x[n]")

    # Cálculo de la DFT
    Xk = np.fft.fft(x_t, N)
    freqs = np.fft.fftfreq(N, 1/fs)

    # Solo la mitad positiva del espectro
    Xk_magnitude = np.abs(Xk)[:N//2]
    freqs_pos = freqs[:N//2]

    # Resolución en frecuencia
    delta_f = fs / N
    print(f"Resolución en frecuencia Δf = {delta_f:.4f} Hz")

    # Mostrar espectro
    plt.figure()
    plt.stem(freqs_pos, Xk_magnitude, basefmt=" ")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|X[k]|")
    plt.title("Espectro de Magnitud de la Señal")
    plt.grid(True)
    plt.show()

    # Identificar picos espectrales
    threshold = max(Xk_magnitude) * 0.1
    peaks = [(freqs_pos[i], Xk_magnitude[i]) for i in range(len(Xk_magnitude)) if Xk_magnitude[i] > threshold]

    print("Picos espectrales (frecuencia, amplitud relativa):")
    for f, A in peaks:
        print(f"  f = {f:.2f} Hz, A = {A:.3f}")
