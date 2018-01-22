import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

file_name = sys.argv[1]
init = np.genfromtxt(file_name, delimiter='\n', dtype=str)

'''
data loading
'''
parse = []
for item in init:
    temp = item.split()
    if len(temp) == 1:
        parsed = float(temp[0])
    else:
        parsed = np.array(temp, dtype = float)
        
    parse.append(parsed)
    
N = int(parse[0])
y0 = np.zeros(N+2)
v0 = np.zeros_like(y0)

T = parse[1]
m = parse[2]
a = parse[3]
y0[1:-1] = parse[4]
v0[1:-1] = parse[5]

Tau = 8*np.pi/np.sqrt(T/(m*a))
steps = 100

def force(y):
    '''
    calculates the force of every mass
    '''
    F = np.zeros_like(y)
    for i in range(1, N+1):
        F[i] = 2*y[i] - y[i+1] - y[i-1]
    return -T*F/(m*a)

def leapfrog(y_n, v_n, h = 4*Tau/steps):
    v_half = v_n + 0.5*h*force(y_n)
    y_n += h*v_half
    v_n = v_half + 0.5*h*force(y_n)
    return y_n, v_n

'''
plotting
'''
fig = plt.figure()

plt.ylim(-max(y0)-max(v0), max(y0)+max(v0))
plt.xlim(0, N+2)
plt.xlabel('N')
plt.ylabel('y')

points = plt.plot([], [], "-o")[0]
x = np.arange(0, N+2)

y_n = y0
v_n = v0

E = np.zeros(steps)

def animation(i):
    global y_n, v_n
    
    E[i] = np.sum(m*v_n[1:-1]**2 + T/a*(y_n[1:-1] - y_n[:-2])**2)/2.0
    
    y_n, v_n = leapfrog(y_n, v_n)
    
    points.set_data(x, y_n)
    
anim = FuncAnimation(fig, animation, frames = np.arange(steps), interval=1)
anim.save('movimiento.gif', writer='imagemagick')

plt.close()

t = np.linspace(0, 4*Tau, steps)
plt.plot(t, abs(E-E[0])/E[0])
plt.savefig("energia.pdf")
