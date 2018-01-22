#include <stdio.h>
#include <math.h>

// 18-Jun-2015
// Exercise 2-1 from Beginning C by Horton
// Write a program that prompts the user to enter a distance in inches and then outputs that distance in yards, feet and inches.

int main(void)
{
	// Declarar las variables a emplear
	float allinch, yards, feet, inches;
	printf("#################################################################\n");
	printf("The Fantastic Inches to Yards-Feets-Inches Conversion Program\n");
	printf("#################################################################\n");
	printf("Input length = ");
	scanf("%f", &allinch);
	printf("(conversion) %.2f'' = ", allinch);
	// Calcular yardas pies y pulgadas
	yards = (allinch - fmod(allinch, 36.))/36.;
	allinch = allinch - yards*36.;
	feet= (allinch - fmod(allinch, 12.))/12.;
	allinch = allinch - feet*12.;
	inches = allinch;
	// Ahora imprimir el resultado evitando imprimir ceros
	if(yards > 0.)
	printf("%.0f yd. %.0f' %.2f''\n", yards, feet, inches);
	
	else if ( feet > 0. )
	printf("%.0f feet %.2f inches\n", feet, inches);
	
	else
	printf("%.2f in.\n", inches);
	
	printf("#################################################################\n");
	return 0;
}