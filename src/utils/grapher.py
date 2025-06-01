def graficar_continua_y_discreta(ax, t, x_cont, tn, x_disc, titulo):
    ax.plot(t, x_cont, label="Señal continua", color='blue')
    ax.stem(tn, x_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label="Muestreada", use_line_collection=True)
    ax.set_title(titulo)
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud")
    ax.grid(True)
    ax.legend()