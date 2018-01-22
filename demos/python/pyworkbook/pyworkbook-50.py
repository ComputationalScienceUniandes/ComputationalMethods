#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 09-Jun-2015
from math import sqrt
print "#"*40
print "Exercise 50: Roots of a Quadratic Function"
print "Create a program which gives the roots of a quadradic function."
print "#"*40
a=float(raw_input("a="))
b=float(raw_input("b="))
c=float(raw_input("c="))
# Calcular el discriminante
d= b**2 - 4*a*c
if d>0:
	print "El polinomio tiene dos raíces:"
	print "root1 =", (-b + sqrt(d))/2./a
	print "root2 =", (-b - sqrt(d))/2./a
elif d==0:
	print "Una sola raíz doble:"
	print "root =", -b/2./a
else:
	print "No se tiene raíces reales."