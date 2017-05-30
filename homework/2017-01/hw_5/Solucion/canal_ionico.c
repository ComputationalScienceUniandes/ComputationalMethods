#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define R0 1.0
#define CHAIN_LENGTH 1000

void MC(char *_name);
double _random(void);
int number_lines(void);
double probability(double r);
double single_step(double r_last);
void load_data(double *x, double *y);
double *get_radious(double *x, double *y);

int N;
char *name;
double *radious;
double delta = 1, X0, Y0;

int main(void)
{
    N = 10;

    MC("Canal_ionico");
    MC("Canal_ionico1");

    return 0;
}

void MC(char *_name)
{
    int i;
    double r;
    double *x, *y;
    char buffer[100];

    sprintf(buffer, "%s%s", _name, ".txt");
    name = buffer;

    N = number_lines();
    x = malloc(N*sizeof(double));
    y = malloc(N*sizeof(double));

    load_data(x, y);
    radious = get_radious(x, y);

    sprintf(buffer, "%s%s", _name, "_out.dat");
    FILE *file = fopen(buffer, "w");

    fprintf(file, "%f %f \n", X0, Y0);

    r = 0;
    for(i=0; i<CHAIN_LENGTH; i++)
    {
        r = single_step(r);
        fprintf(file, "%f\n", r);
    }
    fclose(file);
}

double probability(double r)
{
    int i, broken = 0;
    double suma = 0, diff;
    for(i = 0; i<N; i++)
    {
        diff = radious[i] - r;
        if(diff < 0)
        {
            broken = 1;
            break;
        }
        suma += pow(diff, 2);
    }
    if(broken)
    {
        return 1;
    }
    return -suma;
}

double single_step(double r_last)
{
    int i;
    double r_new, p_new, p_last, alpha;
    r_new = fabs(r_last + (2*_random() -1)*delta);
    p_new = probability(r_new);
    p_last = probability(r_last);
    if(p_new > 0)
    {
        alpha = 0;
    }
    else
    {
        alpha = exp((p_new - p_last));
    }

    if(alpha > 1)
    {
        alpha = 1;
    }
    if(alpha > _random())
    {
        return r_new;
    }
    return r_last;
}

double _random(void)
{
    return (double) rand()/RAND_MAX;
}

double *get_radious(double *x, double *y)
{
    int i;
    double *radious = malloc(N*sizeof(double));
    double center_x, center_y;
    for(i = 0; i<N; i++)
    {
        center_x += x[i];
        center_y += y[i];
    }
    X0 = center_x/N;
    Y0 = center_y/N;

    for(i = 0; i<N; i++)
    {
        radious[i] = pow(pow(x[i] - X0, 2.0) + pow(y[i] - Y0, 2.0), 0.5) - R0;
    }
    return radious;
}

int number_lines(void)
{
    int lines = 0, ch;
    FILE *file = fopen(name, "r");
    while(!feof(file))
    {
        ch = fgetc(file);
        if(ch == '\n')
        {
            lines++;
        }
    }
    return lines;
}

void load_data(double *x, double *y)
{
    int i = 0;
    double number;
    FILE *file = fopen(name, "r");

    while(fscanf(file, "%lf", &number)==1)
    {
        if(i%2==0)
        {
            x[i/2] = number;
        }
        else
        {
            y[i/2] = number;
        }
        i += 1;
    }
}
