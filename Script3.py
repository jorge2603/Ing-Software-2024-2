from matplotlib import pyplot as plt
import numpy as np


def funcioncuadratica():
    x=np.linspace(-10, 10, 100)
    plt.plot(x, x**2)
    plt.title("Funcion cuadratica")
    plt.show()

if __name__ == "__main__":
    funcioncuadratica()