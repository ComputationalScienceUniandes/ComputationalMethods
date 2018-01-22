#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "wave.h"

int Nt;
DOUBLE dt, c = 1.0, dx, dy;

int main(int argc, char const *argv[])
{
    int i, j;
    int bary, opening=10, width=5;

    dx = Lx/(Nx - 1.0);
    dy = Ly/(Ny - 1.0);
    if (dx < dy)
    {
        dt = alpha*dx/c;
    }
    else
    {
        dt = sqrt(alpha)*dy/c;
    }
    Nt = 60/dt;

    DOUBLE ***psi = createData();
    DOUBLE **mask = createMatrix(1.0);

    psi[0][Ny/3][Nx/2] = -0.5; //initial_condition
    psi[1][Ny/3][Nx/2] = -0.5;

    bary = Ny*2/3;
    for(i = bary - width; i< bary + width; i++)
    {
        for(j = 0; j < Nx/2 - opening; j++)
        {
            mask[i][j] = 0.0;
        }
        for(j =  Nx/2 + opening; j < Nx; j++)
        {
            mask[i][j] = 0.0;
        }
    }

    FILE *file;
    file = fopen("mask.dat", "w");
    printMatrix(file, mask);
    fclose(file);

    finiteDifferences(psi, mask);
    addDeep(psi, 2.0);
    printData(psi, 10);

    freeData(psi);
    freeMatrix(mask);
    return 0;
}

DOUBLE **createMatrix(DOUBLE base)
{
    int i, j;
    DOUBLE **matrix;

    matrix = malloc(Ny*sizeof(DOUBLE *));
    for(i = 0; i < Ny; i++)
    {
        matrix[i] = malloc(Nx*sizeof(DOUBLE));
        for (j = 0; j < Nx; j++)
        {
            matrix[i][j] = base;
        }
    }
    return matrix;
}

DOUBLE ***createData(void)
{
    int i, j, k;

    DOUBLE ***data;
    data = malloc(Nt*sizeof(DOUBLE **));
    for(i = 0; i < Nt; i++)
    {
        data[i] = createMatrix(0.0);
    }
    return data;
}

void freeMatrix(DOUBLE **data)
{
    int i;
    for(i = 0; i < Ny; i++)
    {
        free(data[i]);
    }
    free(data);
}

void freeData(DOUBLE ***data)
{
    int i, j;
    for(i = 0; i<Nt; i++)
    {
        freeMatrix(data[i]);
    }
    free(data);
}

void finiteDifferences(DOUBLE ***data, DOUBLE **mask)
{
    int i, j, k;
    DOUBLE rx, ry;
    rx = pow(c*dt/dx, 2.0);
    ry = pow(c*dt/dy, 2.0);
    for(i = 1; i < Nt-1; i++)
    {
        for(j = 1; j < Ny-1; j++)
        {
            for(k = 1; k < Nx-1; k++)
            {
                data[i+1][j][k] = mask[j][k]*(2*data[i][j][k] - data[i-1][j][k]
                + rx*(data[i][j][k+1] - 2*data[i][j][k] + data[i][j][k-1])
                + ry*(data[i][j+1][k] - 2*data[i][j][k] + data[i][j-1][k]));
            }
        }
    }
}

void addDeep(DOUBLE ***data, DOUBLE deep)
{
    int i, j, k;
    for(i = 0; i < Nt; i++)
    {
        for(j = 0; j < Ny; j++)
        {
            for(k = 0; k < Nx; k++)
            {
                data[i][j][k] = data[i][j][k] + deep;
            }
        }
    }
}

void printMatrix(FILE *file, DOUBLE **data)
{
    int i, j;
    for(i = 0; i < Ny; i++)
    {
        for(j = 0; j < Nx; j++)
        {
            fprintf(file, "%f ", data[i][j]);
        }
        fprintf(file, "\n");
    }
}

void printData(DOUBLE ***data, int skip)
{
    int i, j=0;
    FILE *file;
    char number[3];
    char filename[20];
    char *prefix = "time_";
    for(i = 0; i < Nt; i++)
    {
        if(i % skip == 0)
        {
            sprintf(number, "%d", j);
            strcpy(filename, prefix);
            strcat(filename, number);
            strcat(filename, ".dat");
            file = fopen(filename, "w");
            printMatrix(file, data[i]);
            fclose(file);
            j += 1;
        }
    }
}
