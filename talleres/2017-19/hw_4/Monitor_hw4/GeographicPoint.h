int posX(int x);
double longitude(int x);
double latitude(int y);
void freeData(int **data);
void MCMC(int **data, int N);
double min(double var1, double var2);
void print(int *xs, int *ys, int *rs, int N);

int calcRadious(int **data, int x0, int y0);
int **readData(const char *name, const char *del);

void position(int x, int y, int *x_new, int *y_new);
void newCoor(int **data, int *x, int *y, int xstep, int ystep);
