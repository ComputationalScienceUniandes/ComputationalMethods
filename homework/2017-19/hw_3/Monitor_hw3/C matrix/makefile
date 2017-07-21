result.png : plot.py output.dat
	python plot.py

output.dat : a.out
	./a.out

a.out : matrix.c
	gcc matrix.c
