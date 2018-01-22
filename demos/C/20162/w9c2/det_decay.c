#include <stdio.h>
#include <math.h>

int main(){

	float lambda = 1.0/5.0;
	float N0 = 10.0;
	float dt = 0.001;

	float t_total = 3.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = N0*exp(-lambda*t);
	
	printf("%f %f\n", t, n);
	
	for(i=0;i<n_points;i++){
		t += dt;
		n = N0*exp(-lambda*t);
		printf("%f %f\n", t, n);
	}

	return 0;
}

