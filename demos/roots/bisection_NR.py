# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 07:37:40 2016

@author: juan
"""
import numpy as np

# functions
def f1(x):
    return x**3 + x -1
    
def f2(x):
    return np.cos(2*x) - x


def bisection(f, a, b, precision = 1.0e-8):    
    if f(a)*f(b) > 0:       # test for convergence 
        print("Method does not converge")
        return
        
    n = 0       # number of iterations needed
    middle = (a+b)/2.0      # middle point
    
    while abs(b-a)/2.0 > precision:
        if f(middle) == 0:
            return n, middle            
        elif f(a)*f(middle) < 0:
            b = middle            
        else:
            a = middle
            
        middle = (a+b)/2.0
        n += 1
        
    return n, middle
    
def newtonRaphson(f, a, b, precision = 1.0e-8):
    if f(a)*f(b) > 0:       # test for convergence
        print("Method does not converge")
        return
        
    n = 0       # number of iterations needed
    middle = (a+b)/2.0      # middle point
    
    while abs(b-a)/2.0 > precision:
        derivative = (f(middle+precision)-f(middle))/precision      # calculates derivative in middle point
        
        try:
            middle += - f(middle)/derivative        # sets new middle point 
        except ZeroDivisionError:       # if derivative == 0
            return
            
        if f(middle) == 0:
            return n, middle            
        elif f(a)*f(middle) < 0:
            b = middle            
        else:
            a = middle
            
        n += 1

    return n, middle
        
operations = [f1, f2]
for operation in operations:
    bisec = bisection(operation, -1, 1)
    newton = newtonRaphson(operation, -1, 1)
    print(bisec, newton)
