#include "vars.h"
void set_initial(FLOAT *array, int n_puntos, FLOAT delta_x);
void first_iteration(FLOAT *u_future, FLOAT *u_initial, int n_puntos, FLOAT r);
void iteration(FLOAT *u_future, FLOAT *u_present, FLOAT *u_past, int n_puntos, FLOAT r);
void set_initial_sin(FLOAT *array, int n_puntos, FLOAT delta_x);
void iteration_burgers(FLOAT *u, FLOAT *u_past, int n_puntos, FLOAT dt, FLOAT dx, FLOAT nu, FLOAT alpha);
