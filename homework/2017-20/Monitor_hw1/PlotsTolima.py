import numpy as np
import matplotlib.pyplot as plt

GRF = np.genfromtxt("GRF_vs_EQ.txt")
march = np.genfromtxt("DatosMarzo.txt")

plt.plot(GRF[:, 2], GRF[:, 1], "o", ms = 1, color = "k", label="GRF")
plt.plot(march[:, 2], march[:, 1], "o", ms = 10, color = "g", label="Marzo")

plt.xlabel("Largest Earthquake")
plt.ylabel("Glacier & Rockfall")
plt.legend()
plt.savefig("PlotTolima.pdf")
