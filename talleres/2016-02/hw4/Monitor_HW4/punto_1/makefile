v.png: plotter.py output.txt
	python plotter.py
#	rm -f output.txt placas

output.txt: placas
	./placas > output.txt

placas: placas.c
	gcc placas.c -o placas -fopenmp

clean:
	rm -f output.txt placas
