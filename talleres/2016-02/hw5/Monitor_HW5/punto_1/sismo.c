#include <time.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N = 1000000;
double v = 5.0;
double sigma = 0.1;
double delta_x = 0.1;
double delta_y = 0.1;

double* open_file(char* name, int size);
double residual(double *data, double x, double y);
void step(double* data, double* x, double* y);

int main()
{
	srand(time(NULL)); // random seed
	
	
	double* x = malloc(N*sizeof(double));
	double* y = malloc(N*sizeof(double));
	
	x[0] = 0;
	y[0] = 0;
	
	// initial state
	int n = 0;
	int size = 6*3;
	
	
	FILE *output;
    output = fopen("output.dat", "w"); // output file
	
	double* data = open_file("coordinates.dat", size); // read data from file
	
	while (n < N)
	{
		double x_temp = x[n];
		double y_temp = y[n];
		
		step(data, &x_temp, &y_temp);
		
		x[n+1] = x_temp;
		y[n+1] = y_temp;
		
		fprintf(output, "%f %f\n", x[n], y[n]);
		n += 1;
	}
	fclose(output);
	return 0;
}

double residual(double* data, double x, double y)
{
	/*
	 * calculates the residual
	 */
	double sum = 0;
	for (int i = 0; i < 6; i++)
	{
		double dx = x - data[i*3];
		double dy = y - data[i*3 + 1];
		double d = pow(dx*dx + dy*dy, 0.5);
		sum += pow(d/v - data[i*3 + 2], 2);
	}
	return sum/(2*pow(sigma, 2));
}

void step(double* data, double* x, double* y)
/*
 * single step in chain
 */
{
	double x_rand = ((double)rand())/RAND_MAX;
	double y_rand = ((double)rand())/RAND_MAX;
	double x_new = *x + (2*x_rand - 1)*delta_x;
	double y_new = *y + (2*y_rand - 1)*delta_y;
	
	double sum1 = residual(data, *x, *y);
	double sum2 = residual(data, x_new, y_new);
	
	double a = exp((sum1-sum2)/(2*sigma));
	if (a > 1)
	{
		a = 1;
	}
	
	double u = ((double)rand())/RAND_MAX;
	
	if (u < a)
	{
		*x = x_new;
		*y = y_new;
	}
}

double* open_file(char* name, int size)
/*
 * reads numbers from a plain text file and returns an array
 */
{
	double* data = malloc(sizeof(double)*size);
	int i = 0;
	
	FILE *file;
	file = fopen(name, "r");
	if (file)
	{
		const size_t line_size = 100;
		char* line = malloc(line_size);		
		while (fgets(line, line_size, file) != NULL) // reads each line
		{
			char *token = strtok(line, " "); // first argument is the string to split, second is the delimiter.
			while (token != NULL)
			{
				double temp = strtod(token, NULL); // stores each splitted value in temp. strtod changes type from char* to double.
				data[i] = temp;
				token = strtok(NULL, " ");
				i += 1;
			}
		}
		free(line); 
		fclose(file);
	}
	return data;
}
