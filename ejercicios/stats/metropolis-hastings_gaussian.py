import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

N = int(1e5)

x = np.zeros(N)

delta = 0.2
sigma = 1

x[0] = random()

def gaussian(x):
    return np.exp(-x**2/(2*sigma**2))/(sigma * np.sqrt(2*np.pi))

for i in range(1, N):
    x_new = x[i-1] + delta*(random()-0.5)*2
    alpha = min(1, gaussian(x_new)/gaussian(x[i-1]))
    
    u = random()
    if (u < alpha):
        x[i] = x_new
    else:
        x[i] = x[i-1]
        
plt.hist(x, bins = 50, normed = True)
plt.show()
