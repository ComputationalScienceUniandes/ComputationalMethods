#include <stdlib.h>
#include <stdio.h>
#define USAGE "./a.out valor"

int main(int argc, char **argv){
  float valor;

  if(argc!=2){
    printf("USAGE: %s\n", USAGE);
    exit(1);
  }
  
  valor = atof(argv[1]);
  printf("Valor de entrada: %f\n", valor);

  return 0;
}
