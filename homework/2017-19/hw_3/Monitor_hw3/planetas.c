#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include "planetas.h" // headers

#define Np 10
#define dt 0.02
#define G 4*9.87

int Nt;

// pragma sentences are computed using parallel computing

int main(void)
{
    int i;

    Nt = 265/dt;

    planet *planetas = load_initial(); // loads data from .csv to planet structure

    simulate(planetas); // solves the differential equation for Nt instants of time
    print_planetas(planetas); // prints the planets information x, y, z,
                            // vx, vy, vz for every simulated instant of time

    // gives back the memory each planet used
    #pragma omp parallel for
    for (i = 0; i < Np; i++)
    {
        free_planet(planetas[i]);
    }
    free(planetas); // gives back the memory of the container of the Nt planets

    return 0;
}

planet *init_planetas(void)
{
    int i;
    planet *planeta = malloc(sizeof(planet)); // space for the planeta temporal planet pointer
    planet *planetas = malloc(Np*sizeof(planet)); // "list" of planetas

    for(i = 0; i< Np; i++)
    {
        // space for each "attribute" of a planet
        planeta->x = malloc(Nt*sizeof(DOUBLE));
        planeta->y = malloc(Nt*sizeof(DOUBLE));
        planeta->z = malloc(Nt*sizeof(DOUBLE));
        planeta->vx = malloc(Nt*sizeof(DOUBLE));
        planeta->vy = malloc(Nt*sizeof(DOUBLE));
        planeta->vz = malloc(Nt*sizeof(DOUBLE));
        planetas[i] = *planeta; // adds the planet to the "list" of planetas
    }
    free(planeta); // gives back the memory used by the temporal pointer
    return planetas;
}

planet *load_initial(void)
{
    int i = 0, j = 0, length = 300; // i for row, j for column

    char line_buffer[length]; // prepares a list of length chars to store a single line of the document
    char *split_buffer; // prepares a pointer of chars to store a single word or number in the line_buffer

    FILE *dataFile;
    dataFile = fopen("coordinates.csv", "r");

    planet *planetas = init_planetas(); // prepares a list of planets with memory already reserved

    DOUBLE matrix[Np][7];

    if (dataFile == NULL)
    {
        // verifies the file exists
        printf("Error Reading File\n");
        exit(0);
    }

    while(fgets(line_buffer, length, dataFile) != NULL) // reads up to length characters of the dataFile and stores them at the line_buffer
    {
        j = 0;
        split_buffer = strtok(line_buffer, ","); // first word of the line
        while (split_buffer != NULL)
        {
            if(j == 0) // first column is name
            {
                strcpy(planetas[i].name,  split_buffer);
            }
            else
            {
                matrix[i][j-1] = atof(split_buffer); // changes a char representation of a number to the float/double representation
            }
            split_buffer = strtok(NULL, ",");
            j += 1;
        }
        i += 1;
    }

    for(i = 0; i<Np; i++)
    {
        planetas[i].m = matrix[i][0]/matrix[0][0];
        planetas[i].x[0] = matrix[i][1];
        planetas[i].y[0] = matrix[i][2];
        planetas[i].z[0] = matrix[i][3];
        planetas[i].vx[0] = matrix[i][4];
        planetas[i].vy[0] = matrix[i][5];
        planetas[i].vz[0] = matrix[i][6];
    }

    fclose(dataFile);
    return planetas;
}

void calc_acceleration(planet *planetas, int t)
{
    int i, j; // indexs for planets
    DOUBLE x, y, z, ratio; // temp variables

    #pragma omp parallel for private(i, j, x, y, z, ratio)
    for (i = 0; i < Np; i++)
    {
        // start with cero acceleration
        planetas[i].ax = 0;
        planetas[i].ay = 0;
        planetas[i].az = 0;
        for (j = 0; j < Np; j++)
        {
            if(i != j)
            {
                x = planetas[j].x[t] - planetas[i].x[t];
                y = planetas[j].y[t] - planetas[i].y[t];
                z = planetas[j].z[t] - planetas[i].z[t];
                ratio = G*planetas[j].m/pow(x*x + y*y + z*z, 1.5); // factor applied to each component of the acceleration
                planetas[i].ax += ratio*x;
                planetas[i].ay += ratio*y;
                planetas[i].az += ratio*z;
            }
        }
    }
}

void simulate(planet *planetas)
{
    int t, i;

    DOUBLE *vhx, *vhy, *vhz; // pointers to store the half speeds of each planet
    // add space to them
    vhx = malloc(Np*sizeof(DOUBLE));
    vhy = malloc(Np*sizeof(DOUBLE));
    vhz = malloc(Np*sizeof(DOUBLE));

    // symplectic leapfrog integration
    calc_acceleration(planetas, 0);
    for (t = 0; t < Nt-1; t++)
    {
        #pragma omp parallel for
        for(i = 0; i<Np; i++)
        {
            // calculate the speed at the middle of the interval
            vhx[i] = planetas[i].vx[t] + 0.5*planetas[i].ax*dt;
            vhy[i] = planetas[i].vy[t] + 0.5*planetas[i].ay*dt;
            vhz[i] = planetas[i].vz[t] + 0.5*planetas[i].az*dt;

            // moves all planets to their next position in time
            planetas[i].x[t+1] = planetas[i].x[t] + vhx[i]*dt;
            planetas[i].y[t+1] = planetas[i].y[t] + vhy[i]*dt;
            planetas[i].z[t+1] = planetas[i].z[t] + vhz[i]*dt;
        }
        calc_acceleration(planetas, t+1); // calculates the new acceleration due
                                        // to the change in positions

        #pragma omp parallel for
        for(i = 0; i<Np; i++)
        {
            // updates their next velocity
            planetas[i].vx[t+1] = vhx[i] + 0.5*planetas[i].ax*dt;
            planetas[i].vy[t+1] = vhy[i] + 0.5*planetas[i].ay*dt;
            planetas[i].vz[t+1] = vhz[i] + 0.5*planetas[i].az*dt;
        }
    }
    // gives back memory
    free(vhx);
    free(vhy);
    free(vhz);
}

void print_planetas(planet *planetas)
{
    int i, t;
    char filename[20]; // to store the filename
    for (i = 0; i < Np; i++)
    {
        strcpy(filename, planetas[i].name); // copies the planets name to filename
        strcat(filename, ".dat"); // adds the extension

        FILE *file;
        file = fopen(filename, "w");
        for (t = 0; t < Nt; t++)
        {
            // prints to file the positions and speeds at every simulated instant of time
            fprintf(file, "%f %f %f %f %f %f\n", planetas[i].x[t], planetas[i].y[t],
                    planetas[i].z[t], planetas[i].vx[t], planetas[i].vy[t], planetas[i].vz[t]);
        }
        fclose(file);
    }
}

void free_planet(planet planeta)
{
    // frees the memory used by each planet
    free(planeta.x);
    free(planeta.y);
    free(planeta.z);
    free(planeta.vx);
    free(planeta.vy);
    free(planeta.vz);
}
