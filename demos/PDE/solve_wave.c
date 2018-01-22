//#include <stdio.h>
//#include <stdlib.h>
#include "vars.h"
#include "array.h"
#include "solver.h"

int main(){
  FLOAT *u_initial;
  FLOAT *u_past;
  FLOAT *u_present;
  FLOAT *u_future;
  int n_points=1000;
  int n_time=1000;
  FLOAT delta_t=0.0005;
  FLOAT delta_x=1.0/n_points; 
  FLOAT r=delta_t / delta_x;
  int j;
  u_initial = reserva(n_points);
  u_past = reserva(n_points);
  u_present = reserva(n_points);
  u_future = reserva(n_points);
  set_initial(u_initial, n_points, delta_x);
  first_iteration(u_future, u_initial, n_points, r);

  copy(u_initial, u_past, n_points);
  copy(u_future, u_present, n_points);

  for(j=1;j<n_time;j++){
    iteration(u_future, u_present, u_past, n_points, r);
    copy(u_present, u_past, n_points);
    copy(u_future, u_present, n_points);
  }
    print_array(u_future, n_points, delta_x);

  return 0;
}

