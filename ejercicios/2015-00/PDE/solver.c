#include <math.h>
#include "vars.h"

void iteration(FLOAT *u_future, FLOAT *u_present, FLOAT *u_past, int n_puntos, FLOAT r){
  int i;
  for(i=1;i<(n_puntos-1);i++){
    u_future[i] = (2.0*(1.0-r*r))*u_present[i] 
      - u_past[i] + (r*r)*(u_present[i+1] +  u_present[i-1]);
  }

  u_future[0] = (2.0*(1.0-r*r))*u_present[0] 
    - u_past[0] + (r*r)*(u_present[1] +  u_present[n_puntos-1]);

  u_future[n_puntos-1] = (2.0*(1.0-r*r))*u_present[n_puntos-1] 
    - u_past[n_puntos-1] + (r*r)*(u_present[0] +  u_present[n_puntos-2]);

}

void first_iteration(FLOAT *u_future, FLOAT *u_initial, int n_puntos, FLOAT r){
  int i;  
  for(i=1;i<(n_puntos-1);i++){
    u_future[i] = u_initial[i] + 
      (r*r/2.0) * (u_initial[i+1] - 2.0 * u_initial[i] + u_initial[i-1]);
  }

  u_future[0] = u_initial[0] + 
    (r*r/2.0) * (u_initial[1] - 2.0 * u_initial[0] + u_initial[n_puntos-1]);


  u_future[n_puntos-1] = u_initial[n_puntos-1] + 
    (r*r/2.0) * (u_initial[0] - 2.0 * u_initial[n_puntos-1] + u_initial[n_puntos-2]);
}
void set_initial(FLOAT *array, int n_puntos, FLOAT delta_x){
  int i;
  FLOAT x;
  for(i=0;i<n_puntos;i++){
    x = i * delta_x;
    array[i] = exp(-((x-0.3)*(x-0.3))/0.01);
  }
  array[0] = 0.0;
  array[n_puntos-1] = 0.0;
}

void set_initial_sin(FLOAT *array, int n_puntos, FLOAT delta_x){
  int i;
  FLOAT x;
  for(i=0;i<n_puntos;i++){
    x = i * delta_x;
    array[i] = sin(x);
  }
}


void iteration_burgers(FLOAT *u, FLOAT *u_past, int n_puntos, FLOAT dt, FLOAT dx, FLOAT nu, FLOAT alpha){
  int i;
 for(i=0;i<(n_puntos-1);i++){
    u[i] = u_past[i] - 
      u_past[i]*dt/dx*(u_past[i]-u_past[i-1]) + 
      (nu * alpha * (u_past[i+1] -2.0*u_past[i]+u_past[i-1]));
  }
  u[n_puntos-1] =  u_past[n_puntos-1] - 
    u_past[n_puntos-1]*dt/dx*(u_past[n_puntos-1]-u_past[n_puntos-2]) 
    + (nu * alpha * (u_past[0] -2.0*u_past[n_puntos-1]+u_past[n_puntos-2]));


  u[0] = u_past[0] - 
    u_past[0]*dt/dx*(u_past[0]-u_past[n_puntos-1]) + 
    (nu * alpha * (u_past[1] -2.0*u_past[0]+u_past[n_puntos-2]));
}

