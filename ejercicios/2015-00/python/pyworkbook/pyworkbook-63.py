#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 09-Jun-2015
print "#"*40
print "Exercise 63: Temperature Conversion Table"
print "Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit."
print "#"*40
print '  {:8s}{:7s}'.format("C","F")
for i in range(10):
	c=10*i
	f=1.8*c + 32
	#print "%.1f %.1f" % (c, f)
	print '{:7.2f} {:7.2f}'.format(c,f)