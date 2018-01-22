#include <stdio.h>
#include <math.h>

// 18-Jun-2015
// Exercise 2-3. You're selling a product that's available in two versions: type 1 is a standard version priced at $3.50, and type 2 is a deluxe version priced at $5.50. Write a program using only what you've learned up to now that prompts for the user to enter the product type and a quantity, and then calculates and outputs the price for the quantity entered.

int main(void)
{
	float price1=3.5, price2=5.5;
	int quant, election=0;
	// El usuario tiene que elegir una opción correcta
	while( election != 1 && election !=2 )
	{
	printf("Deluxe(1) or standard(2) version? ");
	scanf("%d", &election);
	}

	printf("How many items? ");
	scanf("%d", &quant);
	printf("Amount due = ");
	if(election == 1)
	{
		printf("$%.2f\n", quant * price1);
	}
	else if (election == 2)
	{
		printf("$%.2f\n", quant * price2);
	}
	else
	{
		printf("Wrong choice!");
	}
	return 0;
}
