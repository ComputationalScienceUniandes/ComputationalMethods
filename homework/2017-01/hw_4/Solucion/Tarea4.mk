Resultados_hw4.pdf : Resultados_hw4.tex *.png
	pdflatex $<

*.png : *.dat Plots_Temperatura.py
	python Plots_Temperatura.py

*.dat : a.out
	./a.out

a.out : DifusionTemperatura.c
	gcc -lm DifusionTemperatura.c

clean :
	rm *.dat *.png *.log *.aux a.out
