import numpy as np
import matplotlib.pyplot as plt

def loadData(name):
    data = []
    with open(name) as file:
        for line in file:
            line = line.replace('\n', '')
            between = False
            new_line = ""
            for letter in line:
                if letter == '"':
                    between = not between
                if not (letter == "," and between):
                    new_line += letter
            temp = new_line.split(',')
            data.append(temp)

    return np.array(data, dtype=str)

def plotMultiple(data, var):
    n = len(var)
    size = 2.5*n
    fig, axes = plt.subplots(n, n, figsize=(size, size))
    for i in range(n):
        for j in range(n):
            if i == j:
                axes[i, j].hist(data[i])
            else:
                axes[i, j].scatter(data[j], data[i], s = 1)
            if j == 0:
                axes[i, j].set_ylabel(var[i])
            if i == n-1:
                axes[i, j].set_xlabel(var[j])
    fig.tight_layout()
    return fig

def covariance(data):
    N = min(data.shape)
    cov = np.zeros((N, N))
    for i in range(N):
        mu1 = data[i].mean()
        for j in range(N):
            mu2 = data[j].mean()
            cov[i, j] = ((data[i] - mu1)*(data[j] - mu2)).mean()
    return cov

data_complete = loadData('DatosBancoMundial5.csv')
numeric = data_complete[1:, 5:].astype(float)

var = data_complete[1:, 3]

mean = numeric.mean(axis=1)
std = numeric.std(axis=1)
normed = np.zeros_like(numeric)
for i in range(numeric.shape[0]):
    normed[i] = (numeric[i] - mean[i])/std[i]

plotMultiple(normed, var)
plt.savefig('ExploracionDatos.pdf')

cov = covariance(normed)

values, vectors = np.linalg.eig(cov)

pos = values.argsort()[::-1]
values = values[pos]
vectors = vectors[:, pos]
a, b = vectors[:, :2].T
print("el componente principal es: %s, el segundo componente principal es: %s"%(a, b))

new = np.dot(vectors.T, normed)

fig = plt.figure()
plt.scatter(new[0], new[1])
plt.xlabel('Com 1')
plt.ylabel('Com 2')
plt.savefig("PCAdatos.pdf")

fig = plt.figure()
for i, value in enumerate(vectors[:, :2]):
    plt.scatter(value[0], value[1], label = var[i])

plt.ylabel("Com 2")
plt.xlabel("Com 1")
plt.legend()
fig.savefig("PCAvariables.pdf")

positions = abs(vectors[:, :2] - vectors.max()) < 0.1
on1, on2 = positions.T
on1 = ", ".join(var[on1])
on2 = ", ".join(var[on2])

print("las variables que estan correlacionadas son (%s) y (%s)"%(on1, on2))
