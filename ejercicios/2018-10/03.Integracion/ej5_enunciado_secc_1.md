Escriba en python una implementación del algoritmo del trapecio para integrar
la función `exp(x)` en el intervalo 0 a 1.

```python

def simpson(f, a, b, N):
    x = np.linspace(a, b, N)
    y = f(x)
    suma = 0.0
    for i in range(1,N-1,2):
        suma += (1.0/3.0) * (y[i-1] + 4*y[i] + y[i+1]) * (x[i+1] -x[i])
    return suma
```



