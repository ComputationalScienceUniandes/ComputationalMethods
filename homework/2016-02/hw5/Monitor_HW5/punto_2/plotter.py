import numpy as np
from corner import corner

data = np.genfromtxt("output.dat", delimiter = " ")

fig = corner(data,labels=[r"$\alpha$", "$\log_{10} M$", r"$\Gamma \, [\mathrm{parsec}]$"], show_titles = True ,title_kwargs={"fontsize": 12})
fig.savefig("plot.pdf")
