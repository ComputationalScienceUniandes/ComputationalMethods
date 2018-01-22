#!/bin/bash
# ------------------------------------------------------------------
# Title			bruno
# Description	analize Kepler's data
# Author		Juan David Lizarazo
# Creation Date	May 28, 2015
# ------------------------------------------------------------------

# Contar el ´número de líneas
figlet "KEPLER"
numlines=$(awk -F"," '{print $0}' kepler.csv | wc -l | sed 's/  //g')
echo "El catálogo tiene $(( numlines - 1 )) planetas."
# Determinar el número de planetas con una masa menor a la de Júpiter
numplanets=$(awk -F"," '{if ($2 > 0 && $2 < 0.01) print $1","$2}' kepler.csv | wc -l | sed 's/ //g')
echo "Se encuentran $numplanets planetas con masa menor a una centésima de masas jovianas y son los siguientes:"

awk -F"," '{if ($2 >= 0 && $2 < 0.01) print "- "$1}' kepler.csv
# Ahora determinar el planeta con el menor periodo orbital
sort --field-separator="," --key=6 -n kepler.csv | head -2 | tail -1 | awk -F"," '{print "El planeta con el menor periodo orbital es **"$1"** con una órbita de " $6" días."}'