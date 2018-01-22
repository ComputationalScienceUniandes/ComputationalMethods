import numpy as np
import matplotlib.pyplot as plt

t, q = np.genfromtxt('CircuitoRC.txt').T

def equation(R, C):
    global t
    V0 = 10
    return V0*C*(1-np.exp(-t/(R*C)))

def error(small_q):
    global q
    return np.sum((q - small_q)**2)

def chain(steps = 1000, dr = 0.1, dc = 0.1):
    R = np.zeros(steps)
    C = np.zeros(steps)
    R[0] = np.random.random()*dr
    C[0] = np.random.random()*dc

    last_error = error(equation(R[0], C[0]))
    for i in range(steps-1):
        r = abs((2*np.random.random()-1)*dr + R[i])
        c = abs((2*np.random.random()-1)*dc + C[i])

        alpha = np.exp(error(equation(R[i], C[i])) -  error(equation(r, c)))
        alpha = min(1, alpha)
        if alpha > np.random.random():
            R[i+1] = r
            C[i+1] = c
        else:
            R[i+1] = R[i]
            C[i+1] = C[i]
    return R, C

R, C = chain()
Q = equation(R[500:].mean(), C[500:].mean())

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(t, q, label = "Real")
ax1.plot(t, Q, label = "Best")
ax1.set_xlabel('$t$')
ax1.set_ylabel('$q(t)$')
ax1.legend()

ax2.plot(R, label = "$R$")
ax2.plot(C, label = "$C$")
ax2.set_ylabel('Value')
ax2.set_xlabel('Iteration')
ax2.legend()
plt.savefig("CircuitoRC.png")
