all : *.pdf

*.pdf : Param.py obs_data.dat
	python Param.py

clean :
	rm *.pdf
