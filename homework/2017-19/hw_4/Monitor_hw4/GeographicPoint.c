#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "GeographicPoint.h"

#define Nx 744
#define Ny 500
#define dx 200
#define dy 200
#define PI acos(-1)

int main(void)
{
    time_t t;
    srand((unsigned) time(&t));

    int **map = readData("map_data.txt", " ");

    MCMC(map, 10000);

    freeData(map);
    return 0;
}

void MCMC(int **data, int N)
{
    int i;

    int *xs, *ys, *rs;
    xs = malloc(N*sizeof(int));
    ys = malloc(N*sizeof(int));
    rs = malloc(N*sizeof(int));

    int x_new, y_new;
    int r_new;

    double alpha;

    xs[0] = rand()%Nx;
    ys[0] = rand()%Ny;

    newCoor(data, &(xs[0]), &(ys[0]), Nx, Ny);

    rs[0] = calcRadious(data, xs[0], ys[0]);

    for (i = 0; i < N-1; i++)
    {
        x_new = xs[i];
        y_new = ys[i];
        newCoor(data, &x_new, &y_new, dx, dy);
        r_new = calcRadious(data, x_new, y_new);
        alpha = exp((r_new - rs[i]));

        if(alpha > rand()/(double) RAND_MAX)
        {
            xs[i+1] = x_new;
            ys[i+1] = y_new;
            rs[i+1] = r_new;
        }
        else
        {
            xs[i+1] = xs[i];
            ys[i+1] = ys[i];
            rs[i+1] = rs[i];
        }
    }

    print(xs, ys, rs, N);
    free(xs);
    free(ys);
    free(rs);
}

void print(int *xs, int *ys, int *rs, int N)
{
    int i;
    double lat, lon;
    double maxlat, maxlong, maxr;

    maxr = rs[0];
    maxlat = ys[0];
    maxlong = xs[0];

    FILE *file = fopen("results.dat", "w");

    for(i = 1; i < N; i++)
    {
        lat = latitude(ys[i]);
        lon = longitude(xs[i]);
        fprintf(file, "%f %f %d\n", lon, lat, rs[i]);

        if(rs[i] > maxr)
        {
            maxr = rs[i];
            maxlat = lat;
            maxlong = lon;
        }
    }
    printf("las coordenadas del punto mas alejado son %.1f, %.1f\n", maxlong, maxlat);
    fclose(file);
}

void newCoor(int **data, int *x, int *y, int xstep, int ystep)
{
    int tx, ty;
    int px, py;

    while(1)
    {
        tx = *x + 2*(RAND_MAX - rand())%xstep;
        ty = *y + 2*(RAND_MAX - rand())%ystep;

        position(tx, ty, &px, &py);

        if(data[py][px] == 0)
        {
            break;
        }
    }
    *x = px;
    *y = py;
}

int calcRadious(int **data, int x0, int y0)
{
    int i, j, rmax, py, px;

    // int rmax2, value, v1, v2, v3, v4;

    int perimeter;
    double dtheta, theta;

    for(rmax = 1; rmax < Ny/2; rmax++)
    {
        // rmax2 = rmax*rmax;
        // for(i = 0; i <= rmax; i++)
        // {
        //     for(j = 0; j <= rmax; j++)
        //     {
        //         if(i*i + j*j <= rmax2)
        //         {
        //             position(x0 + j, y0 + i, &px, &py);
        //             v1 = data[py][px];
        //             position(x0 + j, y0 - i, &px, &py);
        //             v2 = data[py][px];
        //             position(x0 - j, y0 + i, &px, &py);
        //             v3 = data[py][px];
        //             position(x0 - j, y0 - i, &px, &py);
        //             v4 = data[py][px];
        //             value = v1 + v2 + v3 + v4;
        //             if (value > 0)
        //             {
        //                 return rmax-1;
        //             }
        //         }
        //     }
        // }

        perimeter = 2*PI*rmax;
        dtheta = 2*PI/(perimeter-1);
        for(theta = 0; theta <= 2*PI; theta += dtheta)
        {
            i = rmax * sin(theta);
            j = rmax * cos(theta);

            position(x0 + j, y0 + i, &px, &py);

            if(data[py][px] == 1)
            {
                return rmax-1;
            }
        }
    }
    return rmax;
};

double min(double var1, double var2)
{
    if(var1 >= var2)
    {
        return var2;
    }
    else
    {
        return var1;
    }
}

void position(int x, int y, int *x_new, int *y_new)
{
    if(y < 0)
    {
        *y_new = -(y+1)%Ny;
        *x_new = posX(x + Nx/2);
    }
    else if(y >= Ny)
    {
        *y_new = (y-1)%Ny;
        *x_new = posX(x + Nx/2);
    }
    else
    {
        *x_new = posX(x);
        *y_new = y;
    }
}

int posX(int x)
{
    if(x >= 0)
    {
        return x%Nx;
    }
    else
    {
        return Nx + x%Nx;
    }
}

double longitude(int x)
{
    return (x / (double) Nx - 0.5)*360;
}

double latitude(int y)
{
    return (0.5 - y / (double) Ny)*180;
}

int **readData(const char *name, const char *del)
{
    int i = 0, j = 0;
    int length = Nx*3;

    char line_buffer[length];
    char *split_buffer;

    int **matrix;
    matrix = malloc(sizeof(int *)*Ny);

    FILE *dataFile;
    dataFile = fopen(name, "r");

    if (dataFile == NULL)
    {
        printf("Error Reading File\n");
        exit(0);
    }

    i = 0;
    while(fgets(line_buffer, length, dataFile) != NULL)
    {
        j = 0;
        matrix[i] = malloc(sizeof(int)*Nx);
        split_buffer = strtok(line_buffer, del);

        while (split_buffer != NULL)
        {
            matrix[i][j] = atoi(split_buffer);
            split_buffer = strtok(NULL, del);
            j += 1;
        }
        i += 1;
    }

    fclose(dataFile);
    return matrix;
}

void freeData(int **data)
{
    int i;
    for (i = 0; i < Ny; i++)
    {
        free(data[i]);
    }
    free(data);
}
