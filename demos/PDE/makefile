solucion.pdf:	salida.dat simple_matplotlib.py
	python simple_matplotlib.py

salida.dat : burgers
	./burgers > salida.dat

wave : solve_wave.o array.o solver.o
	cc solve_wave.o array.o solver.o -lm -o wave

burgers: solve_burgers.o array.o solver.o 
	cc solve_burgers.o array.o solver.o -lm -o burgers

clean: 
	rm -f wave burgers salida.dat solucion.pdf *.o
