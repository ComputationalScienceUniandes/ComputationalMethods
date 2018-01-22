#include <stdio.h>
#include <stdlib.h>
#include "array.h"
#include "solver.h"
#define PI 3.141592653589793

int main(int argc, char **argv){
  FLOAT *u;
  FLOAT *u_past;
  int n_points = 100;
  int n_time=0;
  FLOAT nu = 0.01;
  FLOAT sigma = 0.02; //this is a parameter to ensure alpha * nu < 0.5
  FLOAT delta_x = 2.0*PI/n_points; 
  FLOAT delta_t = sigma * delta_x * delta_x/nu;
  FLOAT alpha = delta_t / (delta_x * delta_x);
  FLOAT total_time = 1.0;
  int j;


  if(argc!=2){
    fprintf(stderr, "USAGE: ./burgers total_time\n");
    exit(1);
  }
  total_time = atof(argv[1]);
  n_time = (int) (total_time / delta_t);
  fprintf(stderr, "Runing %d steps. Total time %f. Delta_t %f\n", 
	  n_time, total_time, delta_t);

  u = reserva(n_points);
  u_past = reserva(n_points);

  set_initial_sin(u, n_points, delta_x);
  for(j=0;j<n_time;j++){
    copy(u, u_past, n_points);
    iteration_burgers(u, u_past, n_points, delta_t, delta_x, nu, alpha);
  }
  print_array(stdout, u, n_points, delta_x);

  return 0;
}

