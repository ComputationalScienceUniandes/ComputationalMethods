#include <stdio.h>
#include <math.h>

#define PI 3.141592

int main(){

	float r1 = 2.0;
	float r2 = 3.0;
	
	float a1 = PI*pow(r1,2.0);
	float v2 = PI*pow(r2,3.0);
	
	printf("%f area1=%f\n",r1,a1);
	printf("%f volume1=%f\n",r2,v2);
		
	return 0;
}
