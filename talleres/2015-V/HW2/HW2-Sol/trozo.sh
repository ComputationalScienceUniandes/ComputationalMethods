#!/bin/bash
# Una forma poco elegante de hacerlo, lo mejor es utilizar una herramienta ya disponible llamada cut
sed -E 's/(.)/\1\
/g' $3 | head -$2 | tail -$(($2 - $1 + 1)) | sed -E 's/\n//g' | tr '\n' ' ' | sed 's/ //g'