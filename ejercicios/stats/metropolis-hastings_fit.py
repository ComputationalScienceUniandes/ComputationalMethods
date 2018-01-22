import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

N = int(1e5)

x, y = np.genfromtxt('data_trend.dat').T

sigma = 1

m = np.zeros(N)
b = np.zeros(N)

m[0] = 2
b[0] = 8

delta_m = 0.01
delta_b = 0.001

m_max = 10
b_max = 10

def p_calculator(m, b):

    y_obs = m*x + b
    
    temp = np.sum((y_obs - y)**2)/2
    p_obs = np.exp(-temp)
    
    p_m = 0
    if m >= 0 and m < m_max:
        p_m = 1
    
    p_b = 0
    if b >= 0 and b < b_max:
        p_b = 1
        
    return p_obs*p_m*p_b

for i in range(1, N):
    m_new = m[i-1] + delta_m*(random()-0.5)*2
    b_new = b[i-1] + delta_b*(random()-0.5)*2
    
    p_new = p_calculator(m_new, b_new)
    p_old = p_calculator(m[i-1], b[i-1])
    
    alpha = min(1, p_new/p_old)
    
    if random() < alpha:
        m[i] = m_new
        b[i] = b_new
        
    else:
        m[i] = m[i-1]
        b[i] = b[i-1]

plt.plot(m, b, 'o', alpha  = 0.5)
plt.xlabel('$m$')
plt.ylabel('$b$')
plt.grid()
plt.show()
