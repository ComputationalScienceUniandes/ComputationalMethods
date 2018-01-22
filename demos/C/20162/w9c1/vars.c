#include <stdio.h>

int main(){
	int a = 2;
	int b = 10;
	int c = a/b;
	int d = b/a;
	
	float e = 1.0;
	float f = 4.0;
	float g = e/f;
	float h = e*f;
	
	/*
	printf("%d %d %d %d\n",a,b,c,d);
	printf("%f %f %f %f\n",e,f,g,h);
	*/
	
	/*Los muestra alineados a la derecha con 6 espacios, para los float con 6 espacios*/
	printf("%6d %6d %6d %6d\n",a,b,c,d);
	printf("%6.2f %6.2f %6.2f %6.2f\n",e,f,g,h);
	
	printf("a=%2d b=%2d c=%2d d=%2d\n",a,b,c,d);
	printf("e=%6.2f f=%6.2f g=%6.2f h=%6.2f\n",e,f,g,h);

	return 0;
}
