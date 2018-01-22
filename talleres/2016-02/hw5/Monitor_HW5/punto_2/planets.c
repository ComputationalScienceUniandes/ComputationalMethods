#include <time.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N = 1000000;
double AU =  149597870700;
double seconds = 365.25*24*60*60;
double sigma = 1;
double delta_m = 0.1;
double delta_b = 1;
double G = -10.175608591905032;

double* open_file(char* name, int size);
double residual(double *V, double* R, double m, double b);
void step(double* V, double*R, double* m, double* b);

int main()
{
	srand(time(NULL)); // variable seed
	
	
	double* M = malloc(N*sizeof(double));
	double* B = malloc(N*sizeof(double));
	
	FILE *output;
    output = fopen("output.dat", "w"); 	// output file
	
	M[0] = 0; 	// initial states
	B[0] = 0;
	
	int n = 0;
	int size = 8*6; 	// number of points in data
	double* data = open_file("coordinates.dat", size); 	// reads file with data
	
	double* V = malloc(8*sizeof(double)); 	// log of V
	double* R = malloc(8*sizeof(double)); 	// log of R
	
	for(int i = 0; i < 8; i++)
	{
		double v = 0;
		double r = 0;
		for(int j = 0; j < 3; j++)
		{
			// magnitude of each physical quantity
			r += pow(data[6*i + j], 2);
			v += pow(data[6*i + j + 3], 2);
		}
		V[i] = log10(pow(v, 0.5)*AU);
		R[i] = log10(pow(r, 0.5)*AU/seconds);	
	}
	
	while (n < N) // chain with N steps
	{
		double m_temp = M[n];
		double b_temp = B[n];
		
		step(V, R, &m_temp, &b_temp);
		
		M[n+1] = m_temp;
		B[n+1] = b_temp;
		
		fprintf(output, "%f %f\n", 1 - 2*M[n], B[n] - G); // saves each line in file
		n += 1;
	}
	fclose(output);
	return 0;
}

double residual(double* V, double* R, double m, double b)
/*
 * calculates the residual
 */
{
	double sum = 0;
	for (int i = 0; i < 8; i++)
	{
		double y = m*R[i] + b;
		sum += pow(y - V[i], 2);
	}
	return sum/(2*pow(sigma, 2));
}

void step(double* V, double* R, double *m, double* b)
/*
 * single step in chain
 */
{
	double m_rand = ((double)rand())/RAND_MAX;
	double b_rand = ((double)rand())/RAND_MAX;
	double m_new = *m + (2*m_rand - 1)*delta_m;
	double b_new = *b + (2*b_rand - 1)*delta_b;
	
	double sum1 = residual(V, R, *m, *b);
	double sum2 = residual(V, R, m_new, b_new);
	
	double a = exp((sum1-sum2)/(2*sigma));
	if (a > 1)
	{
		a = 1;
	}
	
	double u = ((double)rand())/RAND_MAX;
	
	if (u < a)
	{
		*m = m_new;
		*b = b_new;
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
