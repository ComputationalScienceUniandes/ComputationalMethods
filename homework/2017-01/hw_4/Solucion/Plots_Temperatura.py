import numpy as np
from glob import glob
import matplotlib.pyplot as plt

boundaries = ["closed", "opened", "periodic"]
sources = ["constant", "initial"]

for source in sources:
    for boundary in boundaries:
        fig, axes = plt.subplots(1, 3)
        files = sorted(glob("%s_%s*.dat"%(source, boundary)))
        data = [np.genfromtxt(file) for file in files]
        for (ax, matrix, file) in zip(axes, data, files):
            plot = ax.imshow(matrix)
            name = file.split('_')
            ax.set_axis_off()
            ax.set_title("$t=%s$s"%name[-1].split('.')[0])
            plot.set_clim(vmin=50, vmax=100)


        cbar = fig.colorbar(plot, orientation='horizontal')
        fig.tight_layout()
        fig.subplots_adjust(wspace=0.1)
        filename = "_".join(name[:-1])
        plt.savefig("%s.png"%filename,  bbox_inches='tight', dpi = 300)
