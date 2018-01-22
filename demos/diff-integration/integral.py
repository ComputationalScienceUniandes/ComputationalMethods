# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:21:42 2016

@author: Juan
"""
import numpy as np
import matplotlib.pyplot as plt


lower_limit = 0.0
upper_limit = 1.0

# function being integrated
def function(x):
    return np.exp(-x)

# exact integrator
def exact(x):
    return -np.exp(-x)
    
# calculates the error
def error(real, calculated):
    return abs((real-calculated)/real)

    
# calculates integral using montecarlo
def montecarlo(f, a, b, n):    
    x = np.random.random(n)
    f_eval = f(x)
    result = f_eval.mean()
    return np.log10(n), result

# calculates integral using trapezoid method
def trapezoid(f, a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b-a)/n
    result = 0
    for i in range(n+1):
        if i == 0 or i == n:
            weight = h/2.
        else:
            weight = h
        result += f(x[i])*weight
    return np.log10(n), result
        
# calculates integral using Simpson method
def simpson(f, a, b, n):
    if n%2 == 1:
        n += 1
    h = (b-a)/n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4*f(a + i*h)
    for i in range(2, n-1, 2):
        result += 2*f(a + i*h)
    result *= h/3.
    n = np.log10(n)
    return n, result
            
# calculates integral using Simpson 3/8 method
def simpson38(f, a, b, n):
    if n%3 != 0:
        n += 3 - n%3            
    h = (b-a)/n
    result = f(a) + f(b)
    for i in range(1, n, 3):
        result += 3*f(a + i*h)
    for i in range(2, n, 3):
        result += 3*f(a + i*h)
    for i in range(3, n, 3):
        result += 2*f(a + i*h)
    result *= 3*h/8.
    
    return np.log10(n), result
        
# calculates an integral
def integrate(func, a, b, n):
    # calls functions
    montecarlo_results = montecarlo(func, a, b, n)
    trapezoid_results = trapezoid(func, a, b, n)
    simpson_results = simpson(func, a, b, n)
    simpson38_results = simpson38(func, a, b, n)
    
    # returns log10 of numbers used as a list, and integrals values as another list
    results = [montecarlo_results, trapezoid_results, simpson_results, simpson38_results]
    numbers = [item[0] for item in results]
    results = [np.log10(error(exact_value, item[1])) for item in results]
    return numbers, results


exact_value = exact(upper_limit) - exact(lower_limit)
points = 20
numbers = np.logspace(0, 6, points)
values_buffer = [[],[],[],[]]
numbers_buffer = [[],[],[],[]]
names = ["MonteCarlo","Trapezoid", "Simpson", "Simpson 3/8"]

# unifies methods values
for n in numbers:
    numbers, results = integrate(function, lower_limit, upper_limit, int(n))
    for (values_list, numbers_list, number, result) in zip(values_buffer, numbers_buffer, numbers, results):
        values_list.append(result)
        numbers_list.append(number)
        
# plots
for (values_list, numbers_list, name) in zip(values_buffer, numbers_buffer, names):
    plt.plot(numbers_list, values_list, "-o", label=name)

plt.legend(loc=3)
plt.xlabel("$\log_{10}n$")
plt.ylabel("$\log_{10}\epsilon$")
plt.grid()
plt.savefig("integrators.pdf")
