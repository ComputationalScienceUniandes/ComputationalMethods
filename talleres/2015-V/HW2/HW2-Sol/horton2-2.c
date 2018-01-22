#include <stdio.h>
#include <math.h>

// 18-Jun-2015
// Exercise 2-2 from Beginning C by Horton
// Write a program that prompts for input of the length and width of a room in feet and inches, and then calculates and outputs the floor area in square yards with two decimal places after the decimal point.

int main(void)
{
	float leninch, lenfeet, lenyard;
	float widinch, widfeet, widyard;
	printf("#################################################################\n");
	printf("The Fantastic Area calculator\n");
	printf("#################################################################\n");
	printf("           _________l________\n          |                  |\n          |                  |\n          w                  |\n          |                  |\n          |                  |\n           ~~~~~~~~~~~~~~~~~\n");
	printf("Please input feet in l = ");
	scanf("%f", &lenfeet);
	printf("Please input inches in l = ");
	scanf("%f", &leninch);
	printf("Please input feet in w = ");
	scanf("%f", &widfeet);
	printf("Please input inches in w = ");
	scanf("%f", &widinch);
	// Calculate yards in length and width
	lenyard=leninch/36. + lenfeet / 3.;
	widyard=widinch/36. + widfeet / 3.;
	printf("Area = %.2f yd^2\n", lenyard * widyard);
	printf("#################################################################\n");
	return 0;
}
