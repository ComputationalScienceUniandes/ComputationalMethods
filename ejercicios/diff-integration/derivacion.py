import matplotlib.pyplot as plt
import math
import numpy as np

def f(x):
    return np.cos(x)

def f_prima(x):
    return -np.sin(x)

def forward(fun, x, h):
    return (fun(x+h) - fun(x))/h

def centered(fun, x, h):
    return (fun(x+h*0.5) - fun(x-h*0.5))/h

def extrapolated(fun, x, h):
    return (4.0*centered(fun, x, h*0.5) - centered(fun, x, h))/3

n_points = 20
h = np.logspace(-12, -1, n_points)
err_forward = np.ones(n_points)
err_centered = np.ones(n_points)
err_extrapolated = np.ones(n_points)

x = 0.24
for i in range(n_points):
    err_forward[i] = abs((forward(f, x, h[i]) - f_prima(x))/f_prima(x))
    err_centered[i] = abs((centered(f, x, h[i]) - f_prima(x))/f_prima(x))
    err_extrapolated[i] = abs((extrapolated(f, x, h[i]) - f_prima(x))/f_prima(x))


fig = plt.figure()
plt.rc('text', usetex=True,)
plt.rc('font', family='serif', size=20)


plt.plot(np.log10(h), np.log10(err_forward), label="Forward")
plt.plot(np.log10(h), np.log10(err_centered), label="Centered")
plt.plot(np.log10(h), np.log10(err_extrapolated), label="Extrapolated")


ax = plt.axes()
ax.set_title("Error en la derivada de ${}$, $x={}$".format("\cos(x)", x))
ax.set_xlabel("$\log_{10} h$")
ax.set_ylabel("$\log_{10} \mathrm{error}$")
ax.set_xlim([-12.0,-1.0])
ax.set_ylim([-14.0,0.0])
plt.legend(loc=2, fontsize=15)


plt.savefig('derivadas.pdf', transparent=True)

