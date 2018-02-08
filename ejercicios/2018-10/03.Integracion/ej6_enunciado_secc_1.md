Escriba en python una implementación del algoritmo de Simpson para integrar una funcion arbitraria.


```python
import numpy as np

def simpson(f, a, b, N):
    x = np.linspace(a, b, N)
    y = f(x)
    suma = 0.0
    for i in range(1,N-1,2):
        suma += (1.0/3.0) * (y[i-1] + 4*y[i] + y[i+1]) * (x[i+1] -x[i])
    return suma
```

Escriba una funcion que pueda elegir entre el algoritmo del trapecio o Simpson para hacer una integral.

```python
def integra(f, a, b, N, algo="trapecio"):
    if algo == "trapecio":
        return trapecio(f,a,b,N)
    elif algo == "simpson":
        return simpson(f,a,b,N)
```

Para la integral de exp(x) entre 0 y 1 haga una grafica del error fraccional como funcion del numero de puntos. Tanto el error como el numero de puntos deben variar en escala logaritmica.



    

