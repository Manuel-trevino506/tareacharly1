import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth
from src.utils.grapher import graficar_continua_y_discreta

def graficar_senales():
    f = 2  # Frecuencia recomendada
    t = np.linspace(-1, 5, 1000)
    Ts = 0.01
    n = np.arange(0, int((5 + 1) / Ts))
    tn = n * Ts - 1

    # Señal 1: Sinusoidal
    x1_cont = np.sin(2 * np.pi * f * t)
    x1_disc = np.sin(2 * np.pi * f * tn)

    # Señal 2: Exponencial con escalón
    x2_cont = np.exp(-2 * t) * (t >= 0)
    x2_disc = np.exp(-2 * tn) * (tn >= 0)

    # Señal 3: Triangular periódica
    x3_cont = sawtooth(2 * np.pi * f * t, 0.5)
    x3_disc = sawtooth(2 * np.pi * f * tn, 0.5)

    # Señal 4: Cuadrada
    x4_cont = square(2 * np.pi * f * t)
    x4_disc = square(2 * np.pi * f * tn)

    fig, axs = plt.subplots(4, 1, figsize=(10, 12))
    fig.suptitle("Tarea 1 - Señales continuas y discretas", fontsize=16)

    graficar_continua_y_discreta(axs[0], t, x1_cont, tn, x1_disc, "Señal sinusoidal")
    graficar_continua_y_discreta(axs[1], t, x2_cont, tn, x2_disc, "Señal exponencial con escalón")
    graficar_continua_y_discreta(axs[2], t, x3_cont, tn, x3_disc, "Señal triangular")
    graficar_continua_y_discreta(axs[3], t, x4_cont, tn, x4_disc, "Señal cuadrada")

    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.show()