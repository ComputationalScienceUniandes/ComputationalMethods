import numpy as np
import matplotlib.pyplot as plt

class Carga():
    def __init__(self, q, x0, y0):
        self.q = q
        self.x = x0
        self.y = y0
    
    def potential(self, x, y, k = 0.2306, epsilon = 0.01): # [k] = kg nm3/(s2 e2)
        return k*self.q/((x - self.x)**2 + (y - self.y)**2 + epsilon)**0.5

def gradient(charges, x, y):
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    Dx = np.zeros((y.shape[0], x.shape[0]))
    Dy = np.zeros_like(Dx)
    for i in range(y.shape[0]):
        for j in range(x.shape[0]):
            for charge in charges:
                Dx[i, j] += charge.potential(x[j] + dx, y[i]) \
                             - charge.potential(x[j] - dx, y[i])
                Dy[i, j] += charge.potential(x[j], y[i] + dy) \
                            - charge.potential(x[j], y[i] - dy)
    return 0.5*Dx/dx, 0.5*Dy/dy


q1 = Carga(1, 0.5, 0.5)
q2 = Carga(1, -0.5, -0.5)
q3 = Carga(-1, 0.5, -0.5)
q4 = Carga(-1, -0.5, 0.5)

charges = [q1, q2, q3, q4]

x = y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

V = np.zeros_like(X)
for charge in charges:
    V = V + charge.potential(X, Y)

dx, dy = gradient(charges, x, y)

pot = plt.imshow(V, origin='lower', cmap='jet', extent=[-1, 1, -1, 1])
color = plt.colorbar(pot)
color.set_label(r'$[V] = \left[\frac{kgnm^2}{s^2e^2}\right]$')
plt.streamplot(X, Y, -dx, -dy)
plt.xlabel('$x$ (nm)')
plt.ylabel('$y$ (nm)')
plt.savefig('cargas.pdf')
