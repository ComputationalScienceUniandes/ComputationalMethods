#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int Nx;
int Ny;

double **Matrix(void);
void freePointer(double **matrix);

int main(void)
{
    int i, j;

    Nx = Ny = 1500;

    // double matrix[Ny][Nx];
//
    double **matrix = Matrix();

    for (i = 0; i < Ny; i++)
    {
        for (j = 0; j < Nx; j++)
        {
            matrix[i][j] = (double) rand()/RAND_MAX;
        }
    }

    FILE *file;
    file = fopen("output.dat", "w");
    for (i = 0; i < Ny; i++)
    {
        for (j = 0; j < Nx; j++)
        {
            fprintf(file, "%f ", matrix[i][j]);
        }
        fprintf(file, "\n");
    }
    fclose(file);

    // freePointer(matrix);
    return 0;
}

double **Matrix(void)
{
    int i;
    double **matrix;
    matrix = malloc(Ny*sizeof(double *));

    for(i = 0; i < Ny; i++)
    {
        matrix[i] = malloc(Nx*sizeof(double));
    }

    return matrix;
}

void freePointer(double **matrix)
{
    int i;
    for(i = 0; i<Ny; i++)
    {
        free(matrix[i]);
    }
    free(matrix);
}
