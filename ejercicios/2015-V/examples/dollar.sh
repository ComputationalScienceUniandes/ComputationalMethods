#!/bin/bash
# ------------------------------------------------------------------
# Title			dollar
# Description	curl and gnuplot example with the dollar exchange rate
# Author		Juan David Lizarazo
# Creation Date	Jun 1, 2015
# ------------------------------------------------------------------

# Data taken from http://www.exchange-rates.org/history/COP/USD/T

curl -s http://www.exchange-rates.org/history/COP/USD/T | grep Sunday | sed 's/<\/td><\/tr><tr><td>/\
/g' | sed 's/COP.*//g' | sed 's/<\/td><td>[a-zA-Z]*/-/g' | sed 's/--/,/g' | sed 's/.*<tr><td>//g' | sed '$d' > dollar.csv

gnuplot << EOF
	set xdata time
	set timefmt "%m/%d/%Y"
	set format x "%m/%d/%y"
	set datafile separator ","
	set title "Tasa de cambio del dólar"
	set xlabel "Fecha"
	set ylabel "Pesos"
	set key off 
	plot 'dollar.csv' using 1:2 w linesp
EOF