ani : plot.py *.dat
	python $<

*.dat : a.out
	./$<

a.out : wave.c wave.h
	gcc $< -g -lm

clean :
	rm -r -f a.out *.dat
