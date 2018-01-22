#include <stdio.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#define USAGE "./random_gauss.x n_points"

int main(int argc, char **argv){
  int i;
  int n_points;
  float random;

  const gsl_rng_type * T;
  gsl_rng * r;
  gsl_rng_env_setup();
  T = gsl_rng_default;
  r = gsl_rng_alloc (T);

  n_points = atoi(argv[1]);
  if(argc!=2){
    fprintf(stderr, "USAGE %s\n", USAGE);
    exit(1);
  }

  for (i=0;i<n_points;i++){
    random = gsl_ran_gaussian(r, 0.1);
    printf("%f\n", random);
  }

  gsl_rng_free (r);
  return 0;
}
