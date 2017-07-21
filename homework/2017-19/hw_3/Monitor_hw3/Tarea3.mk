WAVE = 30.png 60.png
PLANETS = planets.png
erase = rm -r -f *.dat a.out *.png *.aux *.log *.mp4

Resultados_hw3.pdf : Resultados_hw3.tex $(WAVE) $(PLANETS)
	pdflatex $<
	$(erase)

$(WAVE) : Onda.py
	python $<

$(PLANETS) : *.dat
	python Plots_Planetas.py

*.dat : a.out
	./a.out

a.out : planetas.c planetas.h
	gcc planetas.c -lm -fopenmp -O2

clean :
	$(erase) *.pdf
