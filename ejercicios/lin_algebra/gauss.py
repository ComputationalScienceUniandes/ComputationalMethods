# Ejercicio del libro Computational Physics de Mark Newmann

import numpy as np

def eliminacion_gaussiana(A, b):    
    A = np.float_(A)
    b = np.float_(b)
    n = len(b)
    for i in range(n):
        #unos en la diagonal
        a = A[i,i]
        A[i,:] = A[i,:] / a
        b[i] = b[i]/ a

        # resta bajando
        for ii in range(i+1,n):
            a = A[ii,i]
            A[ii,:] = A[ii,:] - a * A[i,:]
            b[ii] = b[ii] - a * b[i]

    # reemplaza hacia arriba
    x = b.copy()
    for i in range(n-1,-1,-1):
        for ii in range(i+1,n):
            x[i] = x[i] - A[i,ii]*x[ii]
    return x

A = np.array([[ 2,  1,  4,  1 ],
              [ 3,  4, -1, -1 ],
              [ 1, -4,  1,  5 ],
              [ 2, -2,  1,  3 ]])
b = np.array([ -4, 3, 9, 7 ])

#nuestra solucion
x = eliminacion_gaussiana(A.copy(), b.copy())
print(x)

#verifica solucion con linalg
x_bis = np.linalg.solve(A.copy(),b.copy())
print(x_bis)
