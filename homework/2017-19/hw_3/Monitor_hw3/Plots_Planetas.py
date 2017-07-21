import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation

files =["Sun.dat", "Mercury.dat", "Earth.dat", "Mars.dat", "Jupiter.dat",
    "Saturn.dat", "Uranus.dat", "Neptune.dat", "Pluto.dat"]

N = len(files)
planet_data = []
dots = []
skip = 100

fig = plt.figure()
ax = p3.Axes3D(fig)

for file in files:
    data = np.genfromtxt(file)
    data = data[::skip]
    planet_data.append(data)
    plot = ax.plot(data[:, 0], data[:, 1], data[:, 2], lw=1)[0]
    dot = ax.plot([], [], [], "o", color = plot.get_color(), label=file[:-4])[0]
    dots.append(dot)

def animate(i):
    for j in range(N):
        x = planet_data[j][i, 0]
        y = planet_data[j][i, 1]
        z = planet_data[j][i, 2]
        dots[j].set_data([x], [y])
        dots[j].set_3d_properties([z])

    return tuple(dots)

ax.set_xlabel('$x$ (AU)')
ax.set_ylabel('$y$ (AU)')
ax.set_zlabel('$z$ (AU)')

plt.legend()

fig.savefig("planets.png")

ani = FuncAnimation(fig, animate, planet_data[0].shape[0])

plt.show()
