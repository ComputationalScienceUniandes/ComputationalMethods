Escriba los comandos para: 

1. Crear el directorio `mi_usuario/ejercicios/01.Unix' en su directorio `home`.

```bash
mkdir -p mi_usuario/ejercicios/01.Unix
```
   
2. Bajar los archivos `calificaciones.dat` y `enunciado.md` a el directorio que acaba de crear.

```bash
cd mi_usuario/ejercicios/01.Unix
wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionales/master/ejercicios/2018-10/01.Unix/calificaciones.dat
wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionales/master/ejercicios/2018-10/01.Unix/enunciado.md
```

Las columnas de `calificaciones.dat` corresponden de ese archivo corresponden a cuatro calificaciones de los estudiantes de un curso. El porcentaje se indica en el encabezado.

Escriba los comandos para:

3. Encontrar el numero total de estudiantes en el curso.

```bash
wc -l calificaciones.dat #en realidad da el número de estudiantes más uno.
```


4. Calcular las notas definitivas por cada estudiante.

```bash
awk < calificaciones.dat '{print $1*0.2 + $2*0.2 + $3*0.25 + $4*0.35}'
```

5. Guardar las notas definitivas en un archivo llamado `definitivas.dat`

```bash
awk < calificaciones.dat '{print $1*0.2 + $2*0.2 + $3*0.25 + $4*0.35}' > definitivas.dat
```

6. Calcular cuantos estudiantes pasaron el curso.

```bash
awk < definitivas.dat '{if($1>=60) print $0 }'  |wc -l
```

7. Crear un solo archivo con las calificaciones y la definitiva.
```bash
paste calificaciones.dat definitivas.dat > todo.dat
```

8. Calcular cuantos estudiantes perdieron el primer parcial y pasaron el curso.

```bash
awk < todo.dat '{if ($5>=60 && $1<60.0)print $0}' |wc -l
```

9. Calcular cuantos estudiantes perdieron al menos un parcial y pasaron el curso.
```bash
awk < todo.dat '{if ($5>=60 && ($1<60.0||$2<60 || $3<60 ||$4<60))print $0}'  |wc -l
```

10. Crear el archivo `avance_dia_1.tar` con los contenidos del directorio donde ha venido trabajando hasta ahora.

```bash
tar -cvf avance_dia_1.tar ./*
```
