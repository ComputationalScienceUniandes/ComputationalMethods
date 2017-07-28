PuntoNemo.pdf : Plots.py results.dat
	python Plots.py

results.dat : a.out map_data.txt
	./a.out

a.out : GeographicPoint.c
	gcc $< -lm -O2

clean :
	rm a.out PuntoNemo.pdf results.dat
