import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("output.dat")

plt.imsave("result.png", data)
