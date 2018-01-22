#define Nx 300
#define Ny 300
#define alpha 0.5
#define Lx 30
#define Ly 30

#define DOUBLE float

DOUBLE ***createData(void);
DOUBLE **createMatrix(DOUBLE base);
void freeMatrix(DOUBLE **data);
void freeData(DOUBLE ***data);
void printMatrix(FILE *file, DOUBLE **data);
void printData(DOUBLE ***data, int skip);
void finiteDifferences(DOUBLE ***data, DOUBLE **mask);
void addDeep(DOUBLE ***data, DOUBLE deep);
