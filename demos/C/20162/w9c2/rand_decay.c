#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float delta_n_step(float n, float lambda, float dt);
void single_decay(float N0, float lambda, float dt);

int main(){

	float N_0 = 100.0;
	float Lambda = 1.0/2.0;
	float Dt = 0.001;

	srand48(1);
	
	single_decay(N_0, Lambda, Dt);
		
	return 0;
}

float delta_n_step(float n, float lambda, float dt){
	
	float rand_num = drand48();
	if(rand_num < lambda*n*dt){
		return -1.0;
	} else {
		return 0.0;
	}
}
	
void single_decay(float N0, float lambda, float dt){

	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = N0;
	
	printf("%f %f\n", t, n);
	
	for(i=0;i<n_points;i++){
	
		t += dt;
		float delta_n = delta_n_step(n, lambda, dt);
		n +=delta_n;
		
		printf("%f %f\n", t, n);		
	}
}
