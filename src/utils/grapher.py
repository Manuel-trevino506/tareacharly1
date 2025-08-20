import matplotlib.pyplot as plt

def continuous_plotter(t, x, title="Señal continua"):
    plt.figure()
    plt.plot(t, x)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.title(title)
    plt.grid(True)
    plt.show()

def discrete_plotter(n, x, title="Señal discreta"):
    plt.figure()
    plt.stem(n, x, basefmt=" ")
    plt.xlabel("n (muestras)")
    plt.ylabel("Amplitud")
    plt.title(title)
    plt.grid(True)
    plt.show()
