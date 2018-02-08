Escriba en python una implementación del algoritmo del trapecio para integrar
la función `exp(x)` en el intervalo 0 a 1.

```python
import numpy as np

def trapecio(f, a, b, N):
    x = np.linspace(a, b, N)
    y = f(x)
    suma = 0.0
    for i in range(N-1):
        suma += (y[i] + y[i+1]) * (x[i+1] -x[i])
    return suma
```



