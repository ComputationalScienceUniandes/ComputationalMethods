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

para imprimir algo podemos utilizar `print`

```python
>>> print("Hola Mundo!")
Hola Mundo!
>>> b="Hola Mundo!"
>>> print(b)
Hola Mundo!
>>> a=1
>>> print(a)
1
```

## 2.1 Variables

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

## 2.2 Aritmética

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

### Pregunta

* Escriba en el intérprete una línea de código que calcule el volumen de una esfera de radio `r`.

## 2.3 Listas

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

Así podemos quitar elementos de la lista

```python
>>> del a[1]
>>> a
[1, 'gato']
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

Una función util para crear listas de enteros es `range()`

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> 
```
```python
>>> list(range(1,10,3))
[1, 4, 7]
>>> 
```

### Pregunta

* Después de definir `p = "Universidad de los Andes"`, escriba las líneas de código para que el intérprete devuelva
  * `Universidad`
  * `Andes`

* Utilizando la función `range()`, escriba las líneas de código necesarias para crear una lista con los primeros 5 múltiplos de 3.



## 2.4 Diccionarios

Los diccionarios son otra estructura poderosa de python. 
Al igual que las listas hay dos maneras de inicializarlos.


La primera crea un diccionario vacío y luego añade los elementos
```python
>>> d = dict()
>>> d[1] = "enero"
>>> d[12] = "diciembre"
>>> d[3] = "marzo"
>>> d
{1: 'enero', 12: 'diciembre', 3: 'marzo'}
```

La segunda inicializa todos los elementos
```python
>>> d = {1: 'enero', 12: 'diciembre', 3: 'marzo'}
>>> d
{1: 'enero', 12: 'diciembre', 3: 'marzo'}
```

En ambos casos estamos listos para usar el diccionario
```python
>>> d[1]
'enero'
>>> d[12]
'diciembre'
>>> d[3]
'marzo'
```

Así podemos quitar elementos del diccionario
```python
>>> del d[3]
>>> d
{1: 'enero', 12: 'diciembre'}
```

Los valores de la izquierda se conocen como `keys` y los valores de la derecha como `values`. Podemos sacarlos en forma de lista de la siguiente manera:

```python
>>> list(d.keys())
[1, 12, 3]
>>> list(d.values())
['enero', 'diciembre', 'marzo']
```

### Pregunta

Habiendo definido `d = {1: 'enero', 12: 'diciembre', 3: 'marzo'}`, escriba las líneas de código para 
* Añadir entradas para `abril` y `mayo`.
* Borrar la entrada del mes de `enero`.

## 2.5 Iteración

La construcción `for` se puede utilizar para hacer iteraciones de la siguiente manera


```python
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
```

```python
>>> palabra = "Universidad"
>>> for letra in palabra:
...     print(letra)
... 
U
n
i
v
e
r
s
i
d
a
d
```

```python
>>> zoo = ['tigre', 'loro', 'elefante', 'jirafa']
>>> for animal in zoo:
...     print(animal)
... 
tigre
loro
elefante
jirafa
```

```python
>>> d = {1: 'enero', 12: 'diciembre', 3: 'marzo'}
>>> for k in list(d.keys()):
...     print(k)
... 
1
12
3
>>> for v in list(d.values()):
...     print(v)
... 
enero
diciembre
marzo
>>> for k in list(d.keys()):
...     print(d[k])
... 
enero
diciembre
marzo
```

### Pregunta

Habiendo definido `nombres = ['enero', 'febrero', 'marzo', 'abril', 'mayo']`, escriba las líneas de código necesarias para crear el diccionario `d = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo'}` usando un bucle `for`.

## 2.6 Control de flujo

El flujo del programa se puede controlar con programas `if`, `else`, `elif` y `while`.

```python
#if sencillo con variable booleana
value = True #variable booleana
if(value):
    print('La variable es verdades')
```

El número cero es equivalente de `False`.
```python
if(0):
    print('Esto nunca se va a imprimir')
```

Se puede incluir una variación con `else`
```python
a = 10
b = 4
if(a>b):
    print('a>b: a=', a, ',b=', b)
else:
    print('a<=b, a=', a, ',b=', b)
```


Para más de dos opciones se utiliza `elif`

```python
numero = 2

if(numero == 0):
    print('Nada')
elif(numero==1):
    print('Algo')
else:
    print('Infinito')
```

Finalmente, tenemos al `while` para un condicional que va cambiando a medida que se ejecuta el codigo

```python
print('Cuenta Regresiva')
n=10
while n > 0:
    print(n)
    n = n-1
print('Despegue!')
```

### Pregunta
* Escriba el código necesario para contar el número de vocales en una cadena de caracteres.

## 2.7 Funciones



Es posible crear una función que no tenga ningún parámetro de entrada y que no devuelva ningún valor.

```python
def hola():
 print('Hola')
```
 
También la podemos modificar para tomar de entrada un parámetro
 
```python
def hola(nombre):
 print('Hola ', nombre)
```
Las funciones pueden devolver al menos un valor

```python
def volume(radius):
 vol = (4.0/3.0) * 3.14159 * radius**3
 return vol
```

También es posible crear funciones con varios parámetros de entrada

```python
def multiplica(a, b, c):
    return a*b*c
```

Las funciones también pueden devolver varios valores

```python
def palabras(a):
    m = ['Palabra']
    n = ['Repetida']
    return a*n, a*m
```

También existe la posibilidad de definir valores de entrada de parámetros.
En este caso si no hay valores de entrada se toman los valores en la definición de la función.

```python
def multiplica(a, b=5, c=7):
    return a*b*c
```


### Pregunta 
* Cuál es resultado de `palabra(4)`?

### Pregunta
* Cuál es el resultado de `multiplica(2)`, `multiplica(2,3)`, `multiplica(2,3,8)`?


## 2.8 Objetos


Los objetos sirven como contenedores de variables y funciones aplicables al mismo objeto.

Esta es la definición de un objeto de la clase rectángulo.
```python
class rectangulo():
    def __init__(self, a=1.0, b=2.0):
        self.a = a
        self.b = b
        self.__area = a * b
    def set_area(self):
        self.__area = self.a * self.b
    def print_object(self):
        print("a", self.a)
        print("b", self.b)
        print("area", self.__area)
```

Para crear el objeto podemos escribir

```python
A = rectangulo()
```

### Pregunta
* Cual va a ser el resultado luego de la siguiente secuencia? 

```python
A = rectangulo()
A.print_object()

A.a = 5.0
A.print_object()

A.__area = 18.0
A.print_object()

A.set_area()
A.print_object()
```

### Pregunta

* Cree una clase llamada `Libreta` para guardar nombres, apellidos y número de teléfono. La clase debe tener la capacidad de funcionar de la siguiente forma:


```python
L = Libreta() # crea la libreta
L.nueva_entrada("Diana Lucia", "Hernandez Perez", 876626) #incluye una nueva entrada
L.nueva_entrada("Daniel", "Forero Hernandez", 2471425)
L.nueva_entrada("Ana", "Diaz", 4068585)
L.nueva_entrada("Pony", "Malta", 3449040)
L.busca_apellido("Hernandez") #imprime todos las entradas con un "Hernandez" en el apellido
L.borra_entrada("Diana Lucia", "Hernandez Perez") # Borra la entrada correspondiente
L.imprime_todo() # imprime todos los regristros

```
