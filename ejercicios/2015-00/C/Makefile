all: lista.dat

lista.dat: random_gauss.x
	./random_gauss.x 100 > lista.dat

random_gauss.x : random_gauss.c
	cc random_gauss.c  -lgsl -lgslcblas -lm -o random_gauss.x

clean:
	rm -f random_gauss.x lista.dat
