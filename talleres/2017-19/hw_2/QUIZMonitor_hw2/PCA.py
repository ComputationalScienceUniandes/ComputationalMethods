import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("room-temperature.csv", delimiter=",", skip_header=1, usecols=range(1,5)).T

normed = np.zeros_like(data)
for i in range(data.shape[0]):
    normed[i] = (data[i] - data[i].mean())/data[i].std()

cov = np.cov(normed)
values, vectors = np.linalg.eig(cov)

pos = values.argsort()[::-1]
values = values[pos]
vectors = vectors[:, pos]

a, b = vectors[:, :2].T

print("PC1 es %s y PC2 es %s"%(a, b))

for i, (x, y) in enumerate(vectors[:, :2]):
    plt.scatter(x, y, label = "T%d"%(i+1))
plt.ylabel("Com 2")
plt.xlabel("Com 1")
plt.legend()
plt.savefig("Agrupaciones.pdf")
