import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Ny = 500//6
Nx = 744//6

x0 = Nx//2
y0 = Ny//2

matrix = np.zeros((Ny, Nx))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

def polar(r):
    perimeter = 2*np.pi*r
    theta = np.linspace(0, 2*np.pi, round(2*perimeter))
    xs = np.round(r*np.cos(theta)).astype(int)
    ys = np.round(r*np.sin(theta)).astype(int)

    matrix = np.zeros((Ny, Nx))

    for (x, y) in zip(xs, ys):
        matrix[y+y0, x+x0] = 1

    return matrix

def cartesian(r, square = True):
    matrix = np.zeros((Ny, Nx))
    for i in range(0, r+1):
        for j in range(0, r+1):
            if (i**2 + j**2) <= r**2:
                matrix[y0+i, x0+j] = 1.0
                matrix[y0-i, x0+j] = 1.0
                matrix[y0+i, x0-j] = 1.0
                matrix[y0-i, x0-j] = 1.0

    if square:
        matrix[y0-r:y0+r+1, x0-r] = -1.0
        matrix[y0-r:y0+r+1, x0+r] = -1.0
        matrix[y0-r, x0-r:x0+r] = -1.0
        matrix[y0+r, x0-r:x0+r] = -1.0
    return matrix

def animate(r):
    text1.set_text("r = %d"%r)
    text2.set_text("r = %d"%r)
    polar_plot.set_array(polar(r))
    cartesian_plot.set_array(cartesian(r))
    return polar_plot, cartesian_plot,

polar_plot = ax1.imshow(matrix, cmap = "jet", vmin = -1, vmax = 1)
cartesian_plot = ax2.imshow(matrix, cmap = "jet", vmin = -1, vmax = 1)
text1 = ax1.text(Nx//10, Ny//10, "")
text2 = ax2.text(Nx//10, Ny//10, "")

fig.tight_layout()
ax1.set_axis_off()
ax2.set_axis_off()

ax1.set_title("Polares")
ax2.set_title("Cartesianas")

ani = FuncAnimation(fig, animate, frames = Ny//2, interval = 150)
# ani.save("circles.gif", writer="imagemagick")
plt.show()
