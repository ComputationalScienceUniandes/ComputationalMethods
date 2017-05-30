data_targets = Canal_ionico_out.dat Canal_ionico1_out.dat
image_targets = Canal_ionico.png Canal_ionico1.png

Resultados_hw5.pdf : Resultados_hw5.tex $(image_targets) CircuitoRC.png
	pdflatex $< && rm *.aux *.log

CircuitoRC.png : CircuitoRC.py
	python $<

$(image_targets) : plots_canal_ionico.py $(data_targets)
	python $<

$(data_targets) : a.out
	./a.out

a.out : canal_ionico.c
	gcc -lm -g canal_ionico.c

clean :
	rm *.dat *.png a.out *.pdf
