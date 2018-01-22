#!/bin/bash
# Primero cambio la primera letra a un caracter que asumo ausente en el archivo, luego intercambio las dos letras, y finalmente cambio el carater utilizado en el primer reemplazo para llevar a su estado final a la otra letra.
sed -e "s/$1/*/g" -e "s/$2/$1/g" -e "s/\*/$2/g" $3