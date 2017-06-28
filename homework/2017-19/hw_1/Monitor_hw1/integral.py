import numpy as np
import matplotlib.pyplot as plt

def function(args):
    return sum(args)**3.0
    
def montecarlo(func, a, b, n=10000):
    dim = 10
    ys = np.zeros(n)
    for i in range(n):
        xs = [(b-a)*np.random.rand()+a for j in range(dim)]
        ys[i] = func(xs)
    return ys.mean()*(b-a)**dim

def prom20(func, a, b, n=10000):
    ys = np.zeros(20)
    for i in range(20):
        ys[i] = montecarlo(func, a, b, n)
    return ys.mean()

print("Literal 1: %.3f"%prom20(function, 0, 2))

exponents = np.arange(1, 14)
N = 2**exponents
values = np.array([prom20(function, 0, 2, n) for n in N])
analytic = 1126400
error = abs(values - analytic)/analytic

plt.plot(N, values)
plt.xlabel('N')
plt.ylabel(r'$\int \cdots \int f(x_1, \cdots, x_{10}) dx_1 \cdots dx_{10}$')
plt.tight_layout()
plt.savefig('num_integral.pdf')
plt.close()

plt.plot(1/N**0.5, error)
plt.xlabel(r'$1/\sqrt{N}$')
plt.ylabel('Error')
plt.savefig('err_integral.pdf')
