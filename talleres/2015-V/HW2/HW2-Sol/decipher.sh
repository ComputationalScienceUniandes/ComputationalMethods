#!/bin/bash
cat $1 > deciphered.txt
# permu es un archivo de texto que guarda las letras a intercambiar
for i in {1..10}
	do
	j=122
	for i in $(tail -r permu)
		do
		# La forma en la que se usa printf a continuación convierte un código ASCii en la letra correspondiente
		letter=$(printf "\x$(printf %x $j)")
		#echo $letter "<->" $i
		./flip.sh $letter $i deciphered.txt > deciphered0.txt
		mv deciphered0.txt deciphered.txt
		j=$(( j - 1 ))
		done
	done
cat deciphered.txt
rm deciphered.txt