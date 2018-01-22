#!/opt/local/bin/gnuplot
# 02-Jun-2015
# Script to show Kepler's third law using data from Jupiter's moons
set title "Kepler's third on Jupiter"
set xlabel "a**3"
set ylabel "T**2"
unset key
cube(x) = x**3
square(x) = x**2
set datafile separator ","
set term dumb
plot "joviansatellites.csv" using (cube($2)):(square($3))
