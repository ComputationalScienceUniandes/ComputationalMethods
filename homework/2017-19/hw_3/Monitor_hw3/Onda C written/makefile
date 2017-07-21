ani : plot.py *.dat
	python plot.py

*.dat : a.out
	./a.out

a.out : wave.c wave.h
	gcc wave.c -g -lm

clean :
	rm -r -f a.out *.dat
