import numpy as np

iterations = 20
N = 10000
average = np.zeros(iterations)

for i in range(iterations):
    x = np.random.random(N)*np.pi
    average[i] = np.sin(x).mean()*np.pi

print('el valor de la integral es %.3f'%average.mean())
    
