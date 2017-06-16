import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return np.cos(x)

def f_prime(x):
    return -np.sin(x)

def forward(fun, x, h):
    return (fun(x+h) - fun(x))/h

def backward(fun, x, h):
    return (fun(x) - fun(x-h))/h

def centered(fun, x, h):
    return (fun(x+h*0.5) - fun(x-h*0.5))/h

def extrapolated(fun, x, h):
    return (4.0*centered(fun, x, h*0.5) - centered(fun, x, h))/3

def error(numeric, analytic):
    return abs(numeric - analytic)

epsilon = 1e-3

x = np.linspace(0 + epsilon, 2*np.pi - epsilon)
h = np.logspace(0, -10)

X, H = np.meshgrid(x, h)

fig = plt.figure()
ax = fig.gca(projection='3d')


analytic = f_prime(X)
methods = [forward, backward, centered, extrapolated]
labels = ["Forward", "Backward", "Centered", "Extrapolated"]
colors = ["blue", "red", "green", "orange"]
fakelines = [mpl.lines.Line2D([0],[0], linestyle="none", c=color, marker = 'o') for color in colors]


for i in range(4):    
    Z = error(methods[i](f, X, H), analytic)
    ax.plot_surface(X, np.log10(H), np.log10(Z), cstride = 5, rstride = 5, facecolor=colors[i])

ax.legend(fakelines, labels, numpoints = 1)

plt.show()
