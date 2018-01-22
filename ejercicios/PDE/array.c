#include <stdlib.h>
#include <stdio.h>
#include "vars.h"

FLOAT *reserva(int n_puntos){
  FLOAT *array;
  int i;
  if(!(array = malloc(n_puntos * sizeof(FLOAT)))){
    printf("Problema en reserva\n");
    exit(1);
  }
  for(i=0;i<n_puntos;i++){
    array[i] = 0.0;
  }
  return array;
}

void print_array(FILE *stream, FLOAT * array, int n_puntos, FLOAT delta_x){
  int i;
  for(i=0;i<n_puntos;i++){
    fprintf(stream, "%g %g\n", delta_x*i, array[i]);
  }
}



void copy(FLOAT *origen, FLOAT *destino, int n_puntos){
  int i;
  for(i=0;i<n_puntos;i++){
    destino[i] = origen[i];
  }
}
