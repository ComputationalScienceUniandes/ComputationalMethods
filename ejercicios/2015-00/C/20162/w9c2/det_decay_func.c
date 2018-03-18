#include <stdio.h>
#include <math.h>

float n_t(float t, float N0, float lambda);
void single_decay(float N0, float lambda, float dt);

int main(){

	float Lambda = 1.0/2.0;
	float N_0 = 100.0;
	float Dt = 0.001;

	single_decay(N_0, Lambda, Dt);
		
	return 0;
}

float n_t(float t, float N0, float lambda){
	return N0*exp(-lambda*t);
}

void single_decay(float N0, float lambda, float dt){

	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = n_t(t, N0, lambda);
	printf("%f %f\n", t, n);
	
	for(i=0;i<n_points;i++){
		t += dt;
		n = n_t(t, N0, lambda);
		printf("%f %f\n", t, n);
	}
}
