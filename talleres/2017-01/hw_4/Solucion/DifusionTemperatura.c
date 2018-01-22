#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 100
#define nu 1.0
#define OPEN 0
#define CLOSED 1
#define PERIODIC 2
#define INITIAL 0
#define CONSTANT 1

#define T_WHOLE 50.0
#define T_SPOT 100.0

double dx, dt, coeff;

int position(int i, int j);
void init_problem(double *grid);
char* build_prefix(int boundary, int caso);
void print_grid(const char *name, double *grid);
void step(int i, int j, double *grid, double *temp_grid, int boundary);
void next_state(double *grid, double *temp_grid, int boundary, int caso);
void solve(double *grid, double *temp_grid, double t0, double t1, int boundary, int caso);

int main(void)
{
    double *T_grid = malloc(N*N*sizeof(double));
    double *T_grid_temp = malloc(N*N*sizeof(double));

    dx = 100.0/N;
    dt = dx*dx*0.25*nu;
    coeff = dt*nu/(dx*dx);

    init_problem(T_grid);
    solve(T_grid, T_grid_temp, 0, 2500, OPEN, CONSTANT);
    init_problem(T_grid);
    solve(T_grid, T_grid_temp, 0, 2500, CLOSED, CONSTANT);
    init_problem(T_grid);
    solve(T_grid, T_grid_temp, 0, 2500, PERIODIC, CONSTANT);
    init_problem(T_grid);
    solve(T_grid, T_grid_temp, 0, 2500, OPEN, INITIAL);
    init_problem(T_grid);
    solve(T_grid, T_grid_temp, 0, 2500, CLOSED, INITIAL);
    init_problem(T_grid);
    solve(T_grid, T_grid_temp, 0, 2500, PERIODIC, INITIAL);
    return 0;
}

char* build_prefix(int boundary, int caso)
{
    static char buffer[100];
    char prefix_boundary[100];
    if (boundary == CLOSED)
    {
        sprintf(prefix_boundary, "closed");
    }
    else if (boundary == OPEN)
    {
        sprintf(prefix_boundary, "opened");
    }
    else if (boundary == PERIODIC)
    {
        sprintf(prefix_boundary, "periodic");
    }
    if (caso == CONSTANT)
    {
        sprintf(buffer, "constant_%s", prefix_boundary);
    }
    else
    {
        sprintf(buffer, "initial_%s", prefix_boundary);
    }
    return buffer;
}

void solve(double *grid, double *temp_grid, double t0, double t1, int boundary, int caso)
{
    char name[100];
    char* prefix = build_prefix(boundary, caso);
    while(t0 <= t1)
    {
        if (t0 == 0)
        {
            sprintf(name, "%s_%.0f.dat", prefix, t0);
            print_grid(name, grid);
        }
        else if (t0 == 100)
        {
            sprintf(name, "%s_%.0f.dat", prefix, t0);
            print_grid(name, grid);
        }
        else if (t0 == 2500)
        {
            sprintf(name, "%s_%.0f.dat", prefix, t0);
            print_grid(name, grid);
        }
        next_state(grid, temp_grid, boundary, caso);
        t0 += 1;
    }
}

void step(int i, int j, double *grid, double *temp_grid, int boundary)
{
    int index;
    double up, down, left, right;

    index = position(i, j);
    if (i < N-1)
    {
        down = grid[position(i+1, j)];
    }
    if (i > 0)
    {
        up = grid[position(i-1, j)];
    }
    if (j < N-1)
    {
        right = grid[position(i, j+1)];
    }
    if (j > 0)
    {
        left = grid[position(i, j-1)];
    }

    if ((j > 0) && (j < N-1) && (i > 0) && (i < N-1))
    {
        temp_grid[index] = grid[index] + \
                coeff*(up + down + left + right - 4*grid[index]);
    }

    // boundaries
    else if (boundary == CLOSED)
    {
        temp_grid[index] = 50;
    }
    else if (boundary == PERIODIC)
    {
        if (i == N-1)
        {
            down = grid[position(0, j)];
        }
        else if (i == 0)
        {
            up = grid[position(N-1, j)];
        }
        if (j == N-1)
        {
            right = grid[position(i, 0)];
        }
        else if (j == 0)
        {
            left = grid[position(i, N-1)];
        }
        temp_grid[index] = grid[index] + \
                coeff*(up + down + left + right - 4*grid[index]);
    }
    else if (boundary == OPEN)
    {
        if (i == N-1)
        {
            down = grid[index];
        }
        else if (i == 0)
        {
            up = grid[index];
        }
        if (j == N-1)
        {
            right = grid[index];
        }
        else if (j == 0)
        {
            left = grid[index];
        }
        temp_grid[index] = grid[index] + \
                coeff*(up + down + left + right - 4*grid[index]);
    }
}

void next_state(double *grid, double *temp_grid, int boundary, int caso)
{
    int i, j, index;
    int width = 20/dx, height_half = 5/dx;
    int i_half = N*0.5, j_half = 0.20*N;
    for(i = 0; i < N; i++)
    {
        for(j = 0; j< N; j++)
        {
            step(i, j, grid, temp_grid, boundary);
            if (caso == CONSTANT)
            {
                if((j < j_half + width) && (j > j_half))
                {
                    if((i < i_half + height_half) && (i > i_half - height_half))
                    {
                        grid[position(i, j)] = T_SPOT;
                    }
                }
            }
        }
    }

    for(i = 0; i < N; i++)
    {
        for(j = 0; j < N; j++)
        {
            index = position(i, j);
            grid[index] = temp_grid[index];
        }
    }
}

void init_problem(double *grid)
{
    int width = 20/dx, height_half = 5/dx;

    int i, j, index;
    int i_half = N*0.5, j_half = 0.20*N;

    for(i = 0; i < N; i++)
    {
        for(j = 0; j < N; j++)
        {
            index = position(i, j);
            grid[index] = T_WHOLE;
            if((j < j_half + width) && (j > j_half))
            {
                if((i < i_half + height_half) && (i > i_half - height_half))
                {
                    grid[index] = T_SPOT;
                }
            }
        }
    }
}

int position(int i, int j)
{
    return i + j*N;
}

void print_grid(const char *name, double *grid)
{
    int i, j, index;
    FILE *file = fopen(name, "w");
    for(i = 0; i < N; i++)
    {
        for(j = 0; j < N; j++)
        {
            index = position(i, j);
            fprintf(file, "%f ", grid[index]);
        }
        fprintf(file, "\n");
    }
    fclose(file);
}
