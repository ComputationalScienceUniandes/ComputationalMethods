#include <stdio.h>
#include <math.h>

// 18-Jun-2015
// Exercise 2-4. Write a program that prompts for the user's weekly pay in dollars and the hours worked to be entered through the keyboard as floating-pointv alues. The program should then calculate and output the average pay per hour in the following form:
// Your average hourly pay rate is 7 dollars and 54 cents


int main(void)
{
	float pay, work_hours, av_hourly_pay;
	float dollars, cents;
	printf("#################################################################\n");
	printf("Average Hourly Pay Calculator\n");
	printf("#################################################################\n");
	// Pedirle la información al usuario
	printf("What is your weekly pay? ");
	scanf("%f", &pay);
	printf("How many hours worked? ");
	scanf("%f", &work_hours);
	// Calculate average hourly pay
	av_hourly_pay = pay/work_hours;
	// Calculate dollars and cents
	cents=fmod(av_hourly_pay,1.)*100.;
	dollars=av_hourly_pay-cents/100.;
	printf("Your average hourly pay rate is %.0f dollars and %.0f cents.\n", dollars, cents);
	return 0;
}
