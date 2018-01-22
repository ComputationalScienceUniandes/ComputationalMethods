#!/bin/bash
# ------------------------------------------------------------------
# Title			supergit.sh
# Description	Creates a sequence of git commits
# Author		Juan David Lizarazo
# Creation Date	Jun 13, 2015
# ------------------------------------------------------------------

for i in {1..10}
	do
	for j in {1..100}
		do
		echo $j >> $i.dat
		done
	git add $i.dat
	git commit -m "commit$i"
	done
