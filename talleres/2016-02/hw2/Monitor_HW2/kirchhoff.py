import sys
import numpy as np

file_name = sys.argv[1]

N, R1, R2, V1, V2 = np.loadtxt(file_name)

def eliminacion_gaussiana(A, b):    
    n = len(b)
    for i in range(n):
        # unos en la diagonal
        a = A[i,i]
        A[i,:] = A[i,:]/a
        b[i] = b[i]/a

        # resta bajando
        for ii in range(i+1,n):
            a = A[ii,i]
            A[ii,:] = A[ii,:] - a * A[i,:]
            b[ii] = b[ii] - a * b[i]

    # reemplaza hacia arriba
    for i in range(n-1,-1,-1):
        for ii in range(i+1,n):
           b[i] = b[i] - A[i,ii]*b[ii]
    return b

def circuit(N, R1, R2, V1, V2):
    '''
    Creates the system of equations and solves it
    '''
    N = int(N)
    equation_system = np.zeros((N, N))
    solution = np.zeros(N)
    
    if N == 1:
        equation_system[0] = 2.0*R1 + R2
        solution[0] = V1 - V2
        return eliminacion_gaussiana(equation_system, solution)
    
    # Creates system of equations
    for i in range(N):
        if i%2 == 0:
            R_D = 2.0*R1 + R2
            R_left = -R1
            R_right = -R2
            V = V1 - V2
        else:
            R_D = 2.0*R2 + R1
            R_left = -R2
            R_right = -R1
            V = V2 - V1
        if i == 0:
            equation_system[i, i:i+2] = np.array([R_D, R_right])
        elif i < N-1:
            equation_system[i, i-1:i+2] = np.array([R_left, R_D, R_right])
        else:
            equation_system[i, i-1:i+1] = np.array([R_left, R_D])
        solution[i] = V
    return eliminacion_gaussiana(equation_system, solution)

results = circuit(N, R1, R2, V1, V2)
np.savetxt("corrientes.dat", results)