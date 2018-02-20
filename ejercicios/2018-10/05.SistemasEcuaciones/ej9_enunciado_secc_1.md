* Escriba en python un programa que encuentre la parábola que mejor ajusta los datos en `tendencia.dat`.

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('tendencia.dat')

t = data[:,0]
y = data[:,1]
n_points = len(t)

A = np.transpose(np.array([t**2, t, np.ones(n_points)])) # ahora es 100 x 3
y = np.transpose(y) # ahora es 100 x 1

new_A = np.dot(np.transpose(A), A)
new_y = np.dot(np.transpose(A), y)
solucion = np.linalg.solve(new_A, new_y)

best_t = np.linspace(t.min(), t.max(), 100)
best_y = solucion[0] * t ** 2 + solucion[1] * t + solucion[2]


plt.scatter(t, y, alpha=0.5, label="Datos")
plt.plot(t, best_y, label="Fit")
plt.grid()
plt.legend()
plt.xlabel('Tiempo (s)')
plt.ylabel('Posicion (m)')
plt.savefig('fit.png')


```

![fit](fit.png)




