import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import discrete_plotter

def dft(x):
    """Implementación propia de la DFT (no usar np.fft)."""
    N = len(x)
    X = []
    for k in range(N):
        s = 0
        for n in range(N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    return np.array(X)

def run():
    # Parámetros
    fs = 256
    T = 6
    N = fs * T
    t = np.arange(N) / fs

    f1, f2 = 8, 20
    x_clean = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

    # Ruido ajeno (ejemplo: 50 Hz)
    f_noise = 50
    noise = 0.7 * np.sin(2 * np.pi * f_noise * t)
    x_noisy = x_clean + noise

    # DFT
    X_clean = dft(x_clean)
    X_noisy = dft(x_noisy)
    freqs = np.arange(N) * fs / N

    # Solo mitad positiva
    freqs_pos = freqs[:N//2]
    Xc_mag = np.abs(X_clean[:N//2])
    Xn_mag = np.abs(X_noisy[:N//2])

    delta_f = fs / N
    print(f"Resolución en frecuencia Δf = {delta_f:.4f} Hz")

    # --- Gráficas ---
    fig1, ax1 = plt.subplots()
    ax1.plot(t, x_clean)
    ax1.set_title("Señal discreta limpia")
    ax1.set_xlabel("Tiempo [s]")
    ax1.set_ylabel("Amplitud")
    ax1.grid(True)

    fig2, ax2 = plt.subplots()
    ax2.stem(freqs_pos, Xc_mag, basefmt=" ")
    ax2.set_title("Espectro - Señal limpia")
    ax2.set_xlabel("Frecuencia [Hz]")
    ax2.set_ylabel("|X[k]|")
    ax2.grid(True)

    fig3, ax3 = plt.subplots()
    ax3.plot(t, x_noisy)
    ax3.set_title("Señal discreta con ruido")
    ax3.set_xlabel("Tiempo [s]")
    ax3.set_ylabel("Amplitud")
    ax3.grid(True)

    fig4, ax4 = plt.subplots()
    ax4.stem(freqs_pos, Xn_mag, basefmt=" ")
    ax4.set_title("Espectro - Señal con ruido")
    ax4.set_xlabel("Frecuencia [Hz]")
    ax4.set_ylabel("|X[k]|")
    ax4.grid(True)

    fig5, ax5 = plt.subplots()
    ax5.stem(freqs_pos, Xc_mag, linefmt="b-", markerfmt="bo", basefmt=" ", label="Limpia")
    ax5.stem(freqs_pos, Xn_mag, linefmt="r-", markerfmt="ro", basefmt=" ", label="Con ruido")
    ax5.set_title("Comparación de espectros")
    ax5.set_xlabel("Frecuencia [Hz]")
    ax5.set_ylabel("|X[k]|")
    ax5.legend()
    ax5.grid(True)

    # Picos espectrales
    threshold = max(Xn_mag) * 0.1
    peaks = [(freqs_pos[i], Xn_mag[i]) for i in range(len(Xn_mag)) if Xn_mag[i] > threshold]

    print("Picos espectrales (señal con ruido):")
    for f, A in peaks:
        print(f"  f = {f:.2f} Hz, A = {A:.3f}")

