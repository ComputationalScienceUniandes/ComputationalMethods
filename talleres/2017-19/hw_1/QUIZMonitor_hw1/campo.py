import numpy as np
import matplotlib.pyplot as plt

r, potential = np.genfromtxt('pot.dat').T

h = r[1] - r[0]
field = np.zeros_like(potential)
field[1:-1] = 0.5*(potential[2:] - potential[:-2])
field[0] = potential[1] - potential[0]
field[-1] = potential[-1] - potential[-2]

field = -field/h

plt.plot(r, abs(field), "o")
plt.xlabel('$r$')
plt.ylabel('$|E|$')
plt.savefig('campo.pdf')
