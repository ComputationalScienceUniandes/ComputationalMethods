#!/opt/local/bin/gnuplot
# gnuplot scatter plot example with Hubble expansion data, an example of a fit is given also
# Creation Date	Jun 1, 2015
set key off # no legend
set terminal dumb # love this!
set datafile separator "," # Do right by the csv
set xlabel "d/kPc"
set ylabel "v/km/s"
set title "Ley de Hubble"
y(x) = m*x+c; fit y(x) 'galaxies.csv' using 2:3 via m, c # make a linear fit
plot 'galaxies.csv' using 2:3, y(x) # The first column has the galaxy' name