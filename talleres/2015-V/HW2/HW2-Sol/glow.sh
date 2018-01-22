#!/bin/bash
# Este script produce un círculo pulsante en la terminal
i=1
while (true)
	do
	radius=$(echo "c($i/100*3.14)^2" | bc -l)
	clear
	./circle.sh $radius
	sleep 0.1
	i=$(($i + 1 ))
	done