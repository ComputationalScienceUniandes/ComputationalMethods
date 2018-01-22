#include <stdlib.h>
#include <stdio.h>

int main()
{
  FILE *pipe_gp = popen("gnuplot", "w");

  fputs("set terminal png\n", pipe_gp);
  fputs("plot '-' u 1:2\n", pipe_gp);

  int i;
  for (i=0; i<1000; ++i) {
    double x = i/100.0;
    fprintf(pipe_gp, "%f %f\n", x, x*x);
  }
  fputs("e\n", pipe_gp);
  pclose(pipe_gp);

  return 0;
}