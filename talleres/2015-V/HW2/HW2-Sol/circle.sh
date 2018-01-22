#!/bin/bash
# Este script produce un círculo en la terminal
gnuplot << EOF
	set term dumb
	set parametric
	set xrange [-1:1]
	set yrange [-1:1]
	unset xtics
	unset ytics
	unset key
	unset border
	set size ratio 0.5
	r=$1
	plot r*cos(t),r*sin(t)
EOF
