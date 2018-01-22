#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 09-Jun-2015

from random import randint

def passgen():
	passwd=""
	long=randint(7,10)
	for i in range(long):
		rand=randint(33,126)
		passwd+=chr(rand)
	return passwd

def main():
	print "#"*40
	print "Exercise 94: Random Password"
	print "Write a function that generates a random password. The password should have a random length of between 7 and 10 characters. Each character should be randomly selected from positions 33 to 126 in the ASCII table. Your function will not take any parameters. It will return the randomly generated password as its only result. Display the randomly generated password in your file’s main program. Your main program should only run when your solution has not been imported into another file. "
	print "#"*40
	print "password =", passgen()

if __name__ == "__main__":
	main()