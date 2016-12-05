import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from genetica import *

N = 20
names = ["r_histograma.pdf", "p_histograma.pdf"]
data = ["r_poblacion.dat", "p_poblacion.dat"]

for i in range(N):
    expresion = Expresion()
    expresion.resuelve()
    r = expresion.rt[-1]
    p = expresion.pt[-1]
    results = [r, p]
    
    for (result, item) in zip(results, data):
        with open(item, 'a') as f:
            style = ", %d"
            if i == 0:
                style = "%d"
            f.write(style%result)

for (item, name) in zip(data, names):
    result = np.genfromtxt(item, delimiter = ",")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(result, normed = True)
    if name == "r_histograma.pdf":
        result = np.sort(result)
        coeff = expresion.kr/expresion.gamma_r
        factorial = gamma(result+1)
        p = coeff**result*np.exp(-coeff)/factorial
        ax.plot(result, p, "-o")
    ax.set_xlabel("Final amount")
    ax.set_ylabel("Relative frequency")
    fig.savefig(name)
    plt.close()
