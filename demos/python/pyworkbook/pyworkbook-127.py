#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 09-Jun-2015

print "#"*40
print "Exercise 127: The Sieve of Eratosthenes"
print "#"*40

limit=10000
sieve=range(limit)
sieve[1]=0
p=2
while p<limit:
	for i in range(2*p,limit,p):
		sieve[i]=0
	p+=1
for i in sieve:
	if i!=0:
		print i,
		