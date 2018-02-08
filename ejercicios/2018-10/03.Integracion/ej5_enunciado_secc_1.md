Escriba en python una implementación del algoritmo del trapecio para integrar
la función `exp(x)` en el intervalo 0 a 1.

```python
import numpy as np

def trapecio(f, a, b, N):
    h = (b-a)/(N-1)
    suma = 0.0
    for i in range(N-1):
        x = a + i * h 
        suma += 0.5 * (f(x) + f(x+h)) * h
    return suma
```



