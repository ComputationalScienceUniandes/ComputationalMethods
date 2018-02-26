import numpy as np
import matplotlib.pyplot as plt
import math

def radio_maximo(p):

	l = 0.0
	for i in range(len(p)):

		p[i]=np.abs(p[i])
		l= l + p[i]**4
		
	distancia_maxima = max(p)
	radiomaximo = l/2-distancia_maxima

	return radiomaximo

#Ejemplo:
#print radio_maximo([1.0,2.0,5.0])
