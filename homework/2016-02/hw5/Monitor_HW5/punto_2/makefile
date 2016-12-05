plot.pdf : plotter.py output.dat
	python plotter.py
	rm -f output.dat planets

output.dat : planets
	./planets

planets : planets.c
	gcc -o planets planets.c -lm
