#!/bin/bash
# ------------------------------------------------------------------
# Title			atomicclock
# Description	A simple clock using curl, grep, tail, sed, sleep and figlet
# Author		Juan David Lizarazo
# Creation Date	Jun 2, 2015
# ------------------------------------------------------------------

while (true)
	do 
	time=$(curl -s http://time.is/ | grep "clock0" | tail -1 | sed 's/.*twd">//g' | sed 's/<.*//g')
	clear
	echo "#########################################"
	figlet $time
	echo "#########################################"
	sleep 1
	done