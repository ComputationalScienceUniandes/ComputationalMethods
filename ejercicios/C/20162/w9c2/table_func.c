#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592
#define R_MAX 10

float area(float r);
float volume(float r);
void print_table();

int main(){
	
	print_table();
	
	return 0;
}

float area(float r){
	return 4*PI*pow(r,2.0);
}

float volume(float r){
	return 4.0/3.0*PI*pow(r,3.0);
}

void print_table(){
	
	int i;
	for(i=1;i<=R_MAX;i++){
		printf("%d %f %f\n", i, area((float)i),volume((float)i));
	}
}
