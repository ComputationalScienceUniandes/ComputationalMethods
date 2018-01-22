import numpy as np
from corner import corner

data = np.genfromtxt("output.dat", delimiter = " ")

fig = corner(data,labels=["$x$ (km)", "$y$ (km)", r"$\Gamma \, [\mathrm{parsec}]$"], show_titles = True ,title_kwargs={"fontsize": 12})
fig.savefig("plot.pdf")
