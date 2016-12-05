plot.pdf : plotter.py output.dat
	python plotter.py
	rm -f output.dat sismo

output.dat : sismo
	./sismo

sismo : sismo.c
	gcc -o sismo sismo.c -lm
