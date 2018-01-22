import numpy as np
from scipy.constants import h, c, k

def intensity(f):
    '''
    Planck's law
    '''
    exp = np.exp(h*f/(k*T))
    coeff = 2*h*f**3/c**2
    return coeff/(exp-1)
    
def derivative(freq, func = intensity, diff = 10e4):
    '''
    Central difference derivative method
    '''
    return (func(freq + diff) - func(freq - diff))/(2*diff)

def bisection(f, a, b, precision = 1.0e-8):   
    '''
    Bisection method to find roots
    '''
    if f(a)*f(b) > 0:       # test for convergence 
        print("Method does not converge")
        return
        
    n = 0       # number of iterations needed
    middle = (a+b)/2.0      # middle point
    
    while abs(b-a)/2.0 > precision:
        if f(middle) == 0:
            return middle            
        if f(a)*f(middle) < 0:
            b = middle            
        else:
            a = middle
            
        middle = (a+b)/2.0
        n += 1
        
    return middle
    
N = 10
temperatures = np.logspace(1, 8, N)
freq = np.logspace(8, 20, 1000)

roots = np.zeros(N)

for (i, T) in enumerate(temperatures): 
    exponent = "10e%d"%int(np.log10(T) + 12)
    exponent = eval(exponent)
    roots[i] = bisection(derivative, 10e8, exponent)

b = np.mean(roots/temperatures)*1e-9
np.savetxt("b.dat", [b], fmt='%f')