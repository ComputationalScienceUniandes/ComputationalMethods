import numpy as np
import matplotlib.pyplot as plt

N = 1000
dm = 0.1
db = 0.1

x, y = np.genfromtxt("obs_data.dat").T

ms = np.zeros(N)
bs = np.zeros(N)

error_last = np.sum((ms[0] * x + bs[0] - y)**2)

for i in range(N-1):
    m = ms[i] + (0.5 - np.random.random())*2*dm
    b = bs[i] + (0.5 - np.random.random())*2*db

    y_ = m * x + b
    error = sum((y_ - y)**2)

    alpha = np.exp(0.5*(error_last - error))

    if alpha > np.random.random():
        ms[i+1] = m
        bs[i+1] = b
        error_last = error

    else:
        ms[i+1] = ms[i]
        bs[i+1] = bs[i]

plt.plot(ms)
plt.savefig("Param_m.pdf")
plt.close()

plt.plot(bs)
plt.savefig("Param_b.pdf")
plt.close()

m = ms.mean()
b = bs.mean()

plt.plot(x, y)
plt.plot(x, m*x + b)
plt.savefig("Modelo.pdf")
