Escriba tres scripts de python para resolver los siguientes ejercicios.

1. Haga una gráfica de la espiral de arquímedes (https://en.wikipedia.org/wiki/Archimedean_spiral)

```python
import numpy as np
import matplotlib.pyplot as plt

n_points = 10000
n_vueltas = 4

theta = np.linspace(0.0, n_vueltas * 2.0 * np.pi, n_points)
r = 1.0 + theta

x = r * np.sin(theta)
y = r * np.cos(theta)

plt.plot(x,y)
plt.savefig('espiral.png')
```

2. En un juego de cara y sello donde se que la probabilidad de sacar cara es 0.49 y la de sacar sello es 0.51 decido apostar
con mi contrincante 1 peso por cada ves que yo saque sello. Es decir, si sale sello el me da 1 peso, si sale cara yo le doy 1 peso.
El juego termina si uno de los dos queda con cero pesos. Ambos empezamos con 100 pesos. La funcion de python debe calcular el dinero que tengo luego de tirar la moneda 'n' veces y al final
hacer una gráfica de la cantida de dinero en función de `n` para `1<n<200`. 

```python
import numpy as np
import matplotlib.pyplot as plt

mi_plata = 100
n_apuestas = 0

plata = []
apuestas = []
while (n_apuestas < 200 and mi_plata >0 and mi_plata <=200 ):
    n_apuestas += 1 
    r = np.random.random()
    if(r<=0.51):
        mi_plata +=1
    else:
        mi_plata -=1
    print(n_apuestas)
    plata.append(mi_plata)
    apuestas.append(n_apuestas)

plt.plot(apuestas, plata)
plt.savefig('apuestas.png')
```

3. Calcule la probabilidad de que al menos 2 personas cumplan años el mismo día entre un grupo de `n` personas.
y al final haga una gráfica de esta probabilidad como función de `n` para `2<n<100`.

 
