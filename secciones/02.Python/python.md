# 2. Python


Desde una terminal se puede llamar al intérprete de python con el siguiente comando

```
forero@solaris$python
Python 3.6.0 |Anaconda custom (x86_64)| (default, Dec 23 2016, 13:19:00) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

De ahora en adelante el símbolo `>>>` indica al intérprete de python listo par recibir instruccines. Después de cada instrucción el intérprete muestra el resultado. Por ejemplo.

```python
>>> 1
1
```

```python
>>> 1+1
2
```

### Variables

No es necesario declarar el tipo de variable antes de utilizarlas; es suficiente con inicializarlas. Las tipos de variables más comunes son las siguientes:

```python
>>> a=1
>>> b=10.0
>>> c="computo"
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
```

### Aritmética

Las operaciones básicas de aritmética están disponibles

```python
>>> a=1.0
>>> b=3.0
>>> c=10.0
>>> a*b + c
13.0
>>> c/a - b
7.0
>>> c**b
1000.0
```

Funciones especiales como raíz cuadrada o logaritmos deben utilizarse de la siguiente manera

```python
>>> import math
>>> math.log10(c)
1.0
>>> math.exp(b)
20.085536923187668
>>> math.log(b)
1.0986122886681098
>>> math.sqrt(c)
3.1622776601683795

```

Otras funciones

### Listas

Uno de los tipos de estructuras más útiles en python son las listas.
Hay dos maneras de inicializar una lista

La primera crea una lista vacía y añada los elementos uno por uno
```python
>>> a = list()
>>> type(a)
<class 'list'>
>>> a.append(1)
>>> a.append(3)
>>> a.append("gato")
>>> a
[1, 3, 'gato']
```

La segunda inicializa todos los elementos 
```python
>>> a = [1,3,'gato']
>>> a
[1, 3, 'gato']
```

De una lista podemos conocer su longitud

```python
>>> len(a)
3

```

Podemos extraer elementos uno a uno teniendo en cuenta que los índices empiezan en cero,
```python
>>> a[0], a[1], a[2]
(1, 3, 'gato')
>>> a[0]
1
>>> a[1]
3
>>> a[2]
'gato'
```

y viendo que índices negativos también son posibles.
```python
>>> a[-1]
'gato'
>>> a[-2]
3
>>> a[-3]
1
```

Las cadenas de caracteres también son listas

```python
>>> p = "Universidad de los Andes"
>>> p[0]
'U'
>>> p[-1]
's'
>>> len(p)
24
```

Es posible sacar "tajadas" de una lista (slicing en inglés)

```python
>>> p[0:4]
'Univ'
>>> p[-4:]
'ndes'
>>> p[0:]
'Universidad de los Andes'
>>> p[:]
'Universidad de los Andes'
>>> p[10:12]
'd '
```

```python

```
```python

```

### Diccionarios

```python

```



