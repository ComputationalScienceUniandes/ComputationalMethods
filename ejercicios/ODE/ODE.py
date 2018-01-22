import numpy as np
import matplotlib.pyplot as plt

def y_prime(y,t):
    return -y

def y_solution(t):
    return np.exp(-t)

def Euler(y_prime, y_0=0.0, t_0=0.0, t_f=1.0, N=10):
    t = np.linspace(t_0,t_f,N)
    delta_t = t[1] - t[0]
    y = np.zeros(N)
    y[0] = y_0
    for i in range(1,N):
        k1 = y_prime(y[i-1],t[i-1])
        y[i] = y[i-1] + k1 * delta_t 
    return y, t

def LeapFrog(y_prime, y_0=0.0, t_0=0.0, t_f=1.0, N=10):
    t = np.linspace(t_0,t_f,N)
    delta_t = t[1] - t[0]
    y = np.zeros(N)
    y[0] = y_0
    y[1] = y[0] + delta_t * y_prime(y[0],t[0])
    for i in range(2,N):
        k1 = y_prime(y[i-1],t[i-1])
        y[i] = y[i-2] + k1 * delta_t * 2.0
    return y, t

def RK2(y_prime, y_0=0.0, t_0=0.0, t_f=1.0, N=10):
    t = np.linspace(t_0,t_f,N)
    delta_t = t[1] - t[0]
    y = np.zeros(N)
    y[0] = y_0
    for i in range(1,N):
        k1 = y_prime(y[i-1],t[i-1])
        k2 = y_prime(y[i-1] + k1 * delta_t*0.5, t[i-1] + delta_t*0.5)
        y[i] = y[i-1] + k2 * delta_t 
    return y, t


def RK4(y_prime, y_0=0.0, t_0=0.0, t_f=1.0, N=10):
    t = np.linspace(t_0,t_f,N)
    delta_t = t[1] - t[0]
    y = np.zeros(N)
    y[0] = y_0
    for i in range(1,N):
        k1 = y_prime(y[i-1],t[i-1])
        k2 = y_prime(y[i-1] + k1 * delta_t*0.5, t[i-1] + delta_t*0.5)
        k3 = y_prime(y[i-1] + k2 * delta_t*0.5, t[i-1] + delta_t*0.5)
        k4 = y_prime(y[i-1] + k3 * delta_t, t[i-1] + delta_t)
        k_average = (k1 + 2*k2 + 2*k3 + k4)/6.0
        y[i] = y[i-1] + k_average * delta_t 
    return y, t

y_E, t = Euler(y_prime, y_0=1.0, t_0=0.0, t_f=5.0, N=40)
y_LF, t = LeapFrog(y_prime, y_0=1.0, t_0=0.0, t_f=5.0, N=40)
y_RK2, t = RK2(y_prime, y_0=1.0, t_0=0.0, t_f=5.0, N=40)
y_RK4, t = RK4(y_prime, y_0=1.0, t_0=0.0, t_f=5.0, N=40)
y_sol = y_solution(t)


plt.rc('font', family='serif', size=16)
plt.plot(t,y_E,label='Euler')
plt.plot(t,y_LF,label='LeapFrog')
plt.plot(t,y_RK2,label='Runge-Kutta2')
plt.plot(t,y_RK4,label='Runge-Kutta4')
plt.legend()
plt.ylabel('y')
plt.xlabel('tiempo')
plt.title('$y^{\prime} = -y$')
plt.savefig('ODE_solutions.pdf')
plt.clf()

delta_t = t[1]-t[0]
plt.plot(t,np.abs((y_sol - y_E)/y_sol),label='Euler')
plt.plot(t,np.abs((y_sol - y_LF)/y_sol),label='LeapFrog')
plt.plot(t,np.abs((y_sol - y_RK2)/y_sol),label='Runge-Kutta2')
plt.plot(t,np.abs((y_sol - y_RK4)/y_sol),label='Runge-Kutta4')
plt.legend(loc=2)
plt.yscale('log', nonposy='clip')
plt.ylabel('differencia porcentual con la solucion analitica')
plt.xlabel('tiempo')
plt.savefig('ODE_differences.pdf')
