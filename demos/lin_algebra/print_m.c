/*
  Performs basic matrix operations such as: Initalization,
  Identity, Transposition, with appropriate checks for memory allocation.
*/


#include <stdio.h>
#include <stdlib.h>
void transpose(float * m, int n_x, int n_y);
void print_matrix(float * m, int n_x, int n_y);
void malloc_fn(float * m, int n_x, int n_y);
void identity(float * m, int n_x, int n_y);

int main(void){
  float *I;
  int n_x=5;
  int n_y=5;
  int pos;
  int i,j;

  malloc_fn(I, n_x, n_y);


  /*Initialization*/
  for(i=0;i<n_x;i++){
    for(j=0;j<n_y;j++){
      pos = j + (n_y * i);/*position in the array*/	
      I[pos] = pos;
    }
  }

  print_matrix(I, n_x, n_y);

  transpose(I, n_x, n_y);

  print_matrix(I, n_x, n_y);

  identity(I,n_x,n_y);

  print_matrix(I, n_x, n_y);

  return 0;
}


void malloc_fn(float * m, int n_x, int n_y){
	if(!(m = malloc(sizeof(float)*n_x *n_y))){
      fprintf(stderr, "Problem with memory allocation");
      exit(1);
  }
}

void print_matrix(float * m, int n_x, int n_y){
  int i,j,pos;

  fprintf(stdout, "\n");
  /*Prints to screen*/
  for(i=0;i<n_x;i++){
    for(j=0;j<n_y;j++){
      pos = j + (n_x * i);/*position in the array*/
      fprintf(stdout, " %f ",m[pos]);
    }
    fprintf(stdout, "\n");
  }
  fprintf(stdout, "\n");
}

void transpose(float * m, int n_x, int n_y){
  int i,j,pos_ij, pos_ji;
  float tmp;
  /*Prints to screen*/
  for(i=0;i<n_x;i++){
    for(j=i;j<n_y;j++){
      pos_ij = i + (n_x * j);
      pos_ji = j + (n_x * i);

      tmp = m[pos_ij];
      m[pos_ij] = m[pos_ji];
      m[pos_ji] = tmp;      
    }
  }

}

void identity(float * m, int n_x, int n_y){
	int i,j,pos;
	for(i=0;i<n_x;i++){
    for(j=0;j<n_y;j++){
      pos = j + (n_y * i) ;/*position in the array*/	
      if(i==j){					
	m[pos]=1.0;
      }else{
	m[pos]=0.0;
      }
    }
  }
}



