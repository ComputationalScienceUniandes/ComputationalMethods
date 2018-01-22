#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log10
print "#"*40
print "Exercise 10: Arithmetic"
print "Create a program that reads two integers, a and b, from the user and displays in return the sum, the difference (a-b), the product, the quotient when a is divided by b, the remainder when a is divided by b, the result of log_10a, and the result of a^b"
print "#"*40
a=int(raw_input("a="))
b=int(raw_input("b="))
print "a+b =", a + b
print "a-b =", a - b
print "a*b =", a * b
print "a/b =", a / b
print "a%b =", a % b
print "log_10(a) =",log10(float(a))
print "a^b =", a ** b