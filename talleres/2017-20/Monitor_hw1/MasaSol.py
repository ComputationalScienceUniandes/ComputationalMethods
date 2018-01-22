import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G, au
from mpl_toolkits.mplot3d import Axes3D

earth = np.genfromtxt("EarthOrbit.dat")
mars = np.genfromtxt("MarsOrbit.dat")

yeartoseconds = 60 * 60 * 24 * 365.25

def secondDerivative(data, dt):
    return (data[:-2] - 2*data[1:-1] + data[2:])/dt**2

def calculateSolarMass(planet_data):
    dt = planet_data[1, 0] - planet_data[0, 0]

    acc_planet = secondDerivative(planet_data[:, 1:], dt)

    norm_acc_planet = np.sum(acc_planet**2, axis = 1)**0.5
    distance_planet = np.sum(planet_data[:, 1:]**2, axis = 1)[1:-1]**0.5

    non_SI_G = 4*np.pi**2
    solar_masses = norm_acc_planet * (distance_planet**2) / non_SI_G

    non_SI_G *= au**3 * yeartoseconds**-2 # distance and time in international units

    return solar_masses.mean() * non_SI_G / G # mass in kg

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(earth[:, 1], earth[:, 2], earth[:, 3], color = "k", label = "Earth")
ax.plot(mars[:, 1], mars[:, 2], mars[:, 3], color = "b", label = "Mars")

ax.set_xlabel("$x$ (AU)")
ax.set_ylabel("$y$ (AU)")
ax.set_zlabel("$z$ (AU)")

fig.savefig("Orbitas.pdf")

sun_earth = calculateSolarMass(earth)
sun_mars = calculateSolarMass(mars)
print("La masa del Sol obtenida a partir de las posiciones de la Tierra es %e kg y la obtenida a partir de las posiciones de Marte es %e kg"%(sun_earth, sun_mars))
