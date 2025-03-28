import matplotlib.pyplot as plt
import numpy as np

def graphique(chemin, tab, f):
    x = np.linspace(tab[0], tab[1], tab[2])
    if f == "x²":
        y = np.square(x)
    elif f == "cos(x)":
        y = np.cos(x)
    elif f == "sin(x)":
        y = np.sin(x)
    elif f == "racine carrée de x":
        y = x**0.5
    elif f == "x":
        y = x
    plt.plot(x, y)
    plt.savefig(chemin)

if __name__=="__main__":
    graphique([0, 2*np.pi, 60], "sin(x)")
