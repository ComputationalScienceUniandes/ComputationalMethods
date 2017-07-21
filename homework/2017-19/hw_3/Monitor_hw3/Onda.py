import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Nx = 300
Ny = 300

Lx = 30.0
Ly = 30.0

dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

alpha = 0.5
c = 1.0
dt = alpha * min(dx, dy) / c

Nt = int(60 / dt)

psi = np.zeros((Nt, Ny, Nx))

psi[0, Ny//3, Nx//2] = -0.5

width_half = 2//dx
xh = Nx//2
mask = np.ones_like(psi[0])
mask[int(Ny - Ny//3), : int(xh - width_half)] = 0.0
mask[int(Ny - Ny//3), int(xh + width_half) : ] = 0.0

rx = (c * dt / dx)**2
ry = (c * dt / dy)**2

for t in range(1, Nt-1):
    x = psi[t, 1:-1, 2:] -2*psi[t, 1:-1, 1:-1] + psi[t, 1:-1, :-2]
    y = psi[t, 2:, 1:-1] -2*psi[t, 1:-1, 1:-1] + psi[t, :-2, 1:-1]


    psi[t+1, 1:-1, 1:-1] = 2*psi[t, 1:-1, 1:-1] - psi[t-1, 1:-1, 1:-1] \
                            + rx*x + ry*y

    psi[t+1] = psi[t+1]*mask

psi = psi + 2.0 # deep

vmin = psi[Nt//10:].min()
vmax = psi[Nt//10:].max()

fig = plt.figure()

mask_plot = plt.imshow(1-mask, cmap = "Greys", extent=[-15, 15, 15, -15])

wave = plt.imshow(np.zeros((Ny, Nx)), cmap="jet", extent=[-15, 15, 15, -15],
                                        vmin=vmin, vmax=vmax, alpha=0.7)

time = plt.text(-10, -10, "")

cbar = plt.colorbar(wave)
cbar.solids.set_edgecolor("face")
cbar.set_label("Deep (cm)")

wave.set_array(psi[Nt//2])
fig.savefig("30.png", dpi = 300)
wave.set_array(psi[-1])
fig.savefig("60.png", dpi = 300)

wave.set_array(psi[0])
def animate(i):
    wave.set_array(psi[i])
    time.set_text("Time: %.3f s"%(dt*i))
    return wave, time,

ani = FuncAnimation(fig, animate, frames=Nt, interval = 25, blit=True)
# ani.save("Onda.mp4")
