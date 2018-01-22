#!/bin/bash
# Este fue el script usado para cifrar el mensaje.
cp $1 ciphered.txt
for i in {1..10}
	do
	j=97
	for i in $(cat permu)
		do
		letter=$(printf "\x$(printf %x $j)")
		#echo $letter "<->" $i
		./flip.sh $letter $i ciphered.txt > ciphered0.txt
		mv ciphered0.txt ciphered.txt
		j=$(( j + 1 ))
		#head ciphered.txt
		done
	done
cat ciphered.txt
rm ciphered.txt