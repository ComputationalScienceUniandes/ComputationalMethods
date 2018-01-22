#include <stdio.h>
#include <stdlib.h>

#define N_MAX 20

int main(){

	srand48(1.0);
	
	int i;
	
	for(i=0; i<N_MAX; i++){
		
		float random_num = drand48();
		printf("%f\n",random_num);
	}

	return 0;
}
