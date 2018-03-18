#!/opt/local/bin/gnuplot
# simple script to make a circle
set parametric
set trange [0:2*pi]
set size ratio 1 # make it look circly
set key off # no legend
plot cos(t),sin(t)
