#!/bin/bash
# ------------------------------------------------------------------
# Title			stardate
# Description	calculates the position of starlight arriving from a given year
# Author		Juan David Lizarazo
# Creation Date	May 28, 2015
# ------------------------------------------------------------------
echo "############################################"
figlet "StarDate"
echo "############################################"
figlet $1
awk -v year=$1 -F"\t" '{if ($1 == year) printf "%-20s\n", $2}' worldhistory.tsv
lydist=$(( 2015 - $1))
echo ""
echo "############################################"
echo "LOOK AT THE FOLLOWING STARS:"
printf "%-7s %-7s %s\n" "RA/º" " DEC/º" "  HIP No."
awk -v dist=$lydist -F"," '{if ($10 > dist && $10 < dist + 1) printf  "%-7.2f %-7.2f %-5s %s\n", $8, $9, $2, $7}' hyg.csv | head -5
echo "############################################"
echo ""