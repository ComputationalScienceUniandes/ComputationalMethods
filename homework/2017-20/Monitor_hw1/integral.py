import numpy as np

def function(x, y):
    return (x + np.cos(y) * x)**3

def simpson2d(func, a, b, c, d, Nx = 1001, Ny = 1001):
    if ((not Nx%2) or (not Ny%2)):
        raise(Exception("Odd numbers required."))

    x = np.linspace(a, b, Nx)
    y = np.linspace(c, d, Ny)

    weights = np.ones((Nx, Ny))

    even_row = np.array([16 if i%2 else 8 for i in range(Ny)])
    even_row[0] = 4; even_row[-1] = 4
    odd_row = even_row/2
    first_row = odd_row/2

    weights[2:-1:2] = odd_row
    weights[1:-1:2] = even_row
    weights[0] = first_row
    weights[-1] = first_row

    X, Y = np.meshgrid(x, y)
    integral = (weights * func(X, Y).T).sum()
    
    return integral * (x[1] - x[0]) * (y[1] - y[0]) / 9

def montecarlo(func, a, b, c, d, N = int(1e6)):
    dx = (b - a)
    dy = (d - c)
    x = dx*np.random.random(N) + a
    y = dy*np.random.random(N) + c

    return dx*dy*func(x, y).mean()

simp = simpson2d(function, 0, np.pi, 0, 1, 21, 21)
mont = montecarlo(function, 0, np.pi, 0, 1)

print("el valor de la integral con el metodo Simpson es %f y con el metodo Montecarlo es %f"%(simp, mont))
