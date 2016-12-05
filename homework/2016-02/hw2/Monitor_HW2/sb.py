import numpy as np
import sympy as spy
from scipy.constants import h, c, k

'''
Symbolic calculation so that the maximum happens at z = 1/2.
Not that important, other values work as well
'''
z, alpha = spy.symbols("z a", real = True, positive = True)

f = (z**3/(1-z)**5)/(spy.exp(z*alpha/(1-z))-1) # function
temp = f.diff(z).subs([(z, 0.5)]) # df/dz evaluated at z=0.5
alpha = float(spy.solve(temp, alpha)[0]) # solves the system

def intensity(z):
    '''
    Planck's law modified
    '''
    exp = np.exp(z*alpha/(1-z))
    coeff = (z**3)/(1-z)**5
    return coeff/(exp-1)

def simpson(f, a, b, n):
    '''
    Numerical integration
    '''
    if n%2 == 1:
        n += 1
    h = (b-a)/n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4*f(a + i*h)
    for i in range(2, n-1, 2):
        result += 2*f(a + i*h)
    result *= h/3.
    return result

result = simpson(intensity, 0.001, 0.99, 1000)

sigma = 2*np.pi*alpha**4*k**4/(c**2*h**3)
sigma *= result
np.savetxt("s.dat", [sigma], fmt='%e')