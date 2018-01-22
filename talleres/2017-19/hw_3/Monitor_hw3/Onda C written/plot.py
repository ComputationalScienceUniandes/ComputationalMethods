import numpy as np
from glob import glob
from matplotlib.cm import jet
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mask = np.genfromtxt("mask.dat")
data = []
dat_files = glob("*.dat")
N = len(dat_files) - 1

for i in range(N):
    data.append(np.genfromtxt("time_%d.dat"%i))

fig = plt.figure()
deep = data[0].mean()
masked = np.ma.masked_where(mask == 0, np.ones_like(mask)*deep)

wave = plt.imshow(masked, cmap = jet, vmin=data[-1].min(), vmax=data[-1].max(), extent=[-15, 15, -15, 15])
plt.xlabel("X")
plt.ylabel("Y")

plt.colorbar(wave).set_label("Deep")

jet.set_bad("k", 1.0)

def animate(i):
    wave.set_array(np.ma.masked_where(mask == 0, data[i]))
    return wave,

ani = FuncAnimation(fig, animate, frames=N, interval = 50)
plt.show()
