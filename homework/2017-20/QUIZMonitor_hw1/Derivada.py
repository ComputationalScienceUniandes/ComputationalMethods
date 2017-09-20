import numpy as np
import matplotlib.pyplot as plt

def forward(data, dt):
	return (data[1:] - data[:-1])/dt

def central(data, dt):
	return 0.5*(data[2:] - data[:-2])/dt

balon = np.genfromtxt("Balon.dat", skip_header = 1)
piedra = np.genfromtxt("Piedra.dat", skip_header = 1)

data = balon
#data = piedra

dt = data[1, 0] - data[0, 0]

plt.plot(data[:-1, 0], forward(data[:, 1], dt), label = "$v_f(t)$/(m/s)")
plt.plot(data[1:-1, 0], central(data[:, 1], dt), label = "$v_c(t)$/(m/s)")

plt.plot(data[:, 0], data[:, 1], label = "$x(t)$/m")

plt.xlabel("$t$ (s)")
plt.legend()

plt.savefig("Derivada.pdf")
#plt.savefig("Velocidad.pdf")
