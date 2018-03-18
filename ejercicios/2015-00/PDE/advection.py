import numpy as np
import matplotlib.pyplot as plt


def upwind(u_now, alpha, N_t):
    u_new = u_now.copy()
    N_x = len(u_now)
    for j in range(N_t):
        for i in range(N_x):
            u_new[i] = u_now[i] - alpha * (u_now[i] - u_now[i-1])

        u_now = u_new.copy()
    return u_now

def lax_wendroff(u_now, alpha, N_t):
    u_new = u_now.copy()
    N_x = len(u_now)
    a = (alpha/2.0)*(alpha+1.0)
    b = 1.0 -alpha**2
    c = (alpha/2.0)*(alpha-1.0)

    for j in range(N_t):
        for i in range(N_x):
            u_new[i] = a * u_now[i-1] + b * u_now[i] + c * u_now[(i+1)%N_x]

        u_now = u_new.copy()
    return u_now

def inicial(L=10.0, T=10.0, delta_x=0.1, delta_t=0.05, c=0.5):
    alpha = c * delta_t/delta_x
    print('alpha = {}'.format(alpha))
    N_x = int(L/delta_x + 1)
    N_t = int(T/delta_t + 1)
    x = np.linspace(0,L,N_x)
    u = np.exp(-(2.0-x)**2)
    return x, u, alpha, N_t


x, u, alpha, N_t = inicial()
plt.plot(x,u, label='inicial')

u = upwind(u, alpha, N_t)
plt.plot(x,u, label='Upwind scheme')

x, u, alpha, N_t = inicial()
u = lax_wendroff(u, alpha, N_t)
plt.plot(x,u, label='Lax-Wendroff scheme')

plt.legend(loc=3)
plt.xlabel('x')
plt.ylabel('u')
plt.savefig('advection.pdf')
