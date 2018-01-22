#include <stdio.h>
#include <stdlib.h>

int main(){

	float a = 2.0;
	float b = 10.0;
	
	char mes_agb[30] = "a es mayor que b";
	char mes_alb[30] = "a es menor que b";
	char mes_eq[30] = "a es igual a b";
	
	if(a > b){
		printf("%s\n",mes_agb);
	} else if (a < b){
		printf("%s\n",mes_alb);
	} else {
		printf("%s\n",mes_eq);
	}
	
	while(a<b){
		printf("%f %f\n",a,b);
		a++;
	}
	
	return 0;
	
}
