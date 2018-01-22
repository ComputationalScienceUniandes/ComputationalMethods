import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

image = np.genfromtxt("map_data.txt")
xs, ys, rs = np.genfromtxt("results.dat").T

Ny = image.shape[0]
Nx = image.shape[1]

fig, ax = plt.subplots(figsize=(16, 9))

extent = [-180, 180, -90, 90]

ax.imshow(image, cmap="Greys", extent=extent)

nbins = 50
xbins = np.linspace(-180, 180, nbins)
ybins = np.linspace(-90, 90, nbins//2)

density, xbar, ybar = np.histogram2d(xs, ys, bins=(xbins, ybins))

density = density[:, ::-1]
density_plot = ax.imshow(np.log10(density.T + 1), cmap="jet", interpolation="quadric", alpha = 0.8,
                        extent = extent)

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
cbar = plt.colorbar(density_plot, cax=cax)
cbar.set_label("Point density")
cbar.set_alpha(1)
cbar.draw_all()

pos = rs.argmax()
xmax, ymax, rmax = xs[pos], ys[pos], rs[pos]

dx = 360.0/Nx
dy = 180.0/Ny

theta = np.linspace(0, 2*np.pi)

x = rmax*dx*np.cos(theta) + xmax
y = rmax*dy*np.sin(theta) + ymax

ax.plot(xs, ys, "-o", alpha = 0.5)

ax.plot(x, y, c="r")
ax.plot(xs[0], ys[0], "o", c="g", label="Initial")
ax.plot(xmax, ymax, "o", c="r", label="Furthest")

ax.text(xmax, 1.8*ymax, "$x=%.1f^\circ$\n$y=%.1f^\circ$\n$r=%.1f^\circ$"%(xmax, ymax, rmax))

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()

plt.savefig("PuntoNemo.pdf")
# plt.show()
