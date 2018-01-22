#include <stdio.h>
#include <math.h>

#define R_MAX 7
#define PI 3.141592

int main(){

	int i;
	
	for(i=0;i<R_MAX;i++){
		
		float area = PI*pow(i,2.0);
		printf("%d %f\n", i, area);
	}
	
	return 0;
	
}
