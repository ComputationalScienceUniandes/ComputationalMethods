Escriba las líneas de código de python para hacer las siguientes tareas

1. Imprimir los primeros 100 números divisibles por 3.

```python
>>> for i in range(1,101):
...     print(i*3)
```

2. Imprimir una cuenta regresiva del 10 hasta el 0.

```python
>>> for i in range(10,-1,-1):
...     print(i)
```

3. Crear un diccionario con el número de mes y su nombre correspondiente.

```python
>>> calendario = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
```

4. Imprimir en orden los nombres de los meses del año a partir del diccionario del punto 3.

```python
>>> for i in range(12):
...     print(calendario[i+1])
```

5. Sea `a` una cadena de caracteres compuesta por palabras separadas por espacis (i.e. a="una frase cualquiera"). Utilizando los resultados de a.split() imprima en orden las palabras que se encuentran en `a`.

```python
>>> for palabra in a.split():
...     print(palabra)
```

6. Calcular e imprimir el factorial de un número entero `n`.

```python
>>> n = 5
>>> fact = 1
>>> for i in range(n):
...     fact = fact * (i+1)
... 
>>> print(fact)
```

7. Calcular e Imprimir los primeros `n` elementos de la serie de Fibonacci.

```python
>>> fibo = [0,1]
>>> n = 20
>>> for i in range(2,n+1):
...     fibo.append(fibo[i-2]+fibo[i-1])
... 
>>> print(fibo)
```