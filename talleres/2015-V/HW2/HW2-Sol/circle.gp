#!/opt/local/bin/gnuplot	
#set term dumb
	set parametric
	set xrange [-1:1]
	set yrange [-1:1]
	unset xtics
	unset ytics
	unset key
	unset border
	set size ratio 1
	r=1
	do for [i=1:10000]{
	r=cos(i/50.*3.14)**2
	plot r*cos(t),r*sin(t)
	pause 0.05
	#plot cos(t),sin(t)
	}
