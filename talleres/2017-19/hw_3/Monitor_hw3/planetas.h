#define DOUBLE float // easy change of float precision, float/double

// Defines the planet structure, which contains its positions, speeds, mass, acceleration and name
typedef struct planet_str
{
    DOUBLE *x;
    DOUBLE *y;
    DOUBLE *z;
    DOUBLE *vx;
    DOUBLE *vy;
    DOUBLE *vz;
    DOUBLE m;
    DOUBLE ax;
    DOUBLE ay;
    DOUBLE az;
    char name[20];
} planet;

// Header of functions
planet *init_planetas(void);
planet *load_initial(void);
void simulate(planet *planetas);
void free_planet(planet planeta);
void print_planetas(planet *planetas);
void calc_acceleration(planet *planetas, int t);
