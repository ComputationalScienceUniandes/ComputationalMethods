import numpy as np
import matplotlib.pyplot as plt

def plot_file(name):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    x, y = np.genfromtxt("%s.txt"%name).T
    chain = np.genfromtxt('%s_out.dat'%name, skip_header = 1)
    constants = open('%s_out.dat'%name).readline()
    X0, Y0 = constants.split(' ')[:2]
    X0, Y0 = float(X0), float(Y0)

    x = x
    y = y
    ax1.plot(x, y, 'o')
    theta = np.linspace(0, 2*np.pi, 100)

    r = chain.mean()
    x = r*np.cos(theta) + X0
    y = r*np.sin(theta) + Y0

    ax1.plot(x, y)
    ax1.plot([X0], [Y0], "o")
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')
    ax1.set_title('$r = %.3f$, $x_0 = %.3f$, $y_0 = %.3f$'%(r, X0, Y0))
    ax2.hist(chain)
    ax1.axis("equal")
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('$r$')
    plt.tight_layout()

    plt.savefig("%s.png"%name)


plot_file('Canal_ionico')
plot_file('Canal_ionico1')
