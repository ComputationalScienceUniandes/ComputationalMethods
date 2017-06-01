import numpy as np
import matplotlib.pyplot as plt

def plot_file(name):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    x, y = np.genfromtxt("%s.txt"%name).T
    xs, ys, r = np.genfromtxt('%s_out.dat'%name).T
    constants = open('%s_out.dat'%name).readline()

    ax1.plot(x, y, 'o')
    theta = np.linspace(0, 2*np.pi, 100)

    pos = r.argmax()
    r_ = r[pos].mean()
    X0 = xs[pos]
    Y0 = ys[pos]
    x = r_*np.cos(theta) + X0
    y = r_*np.sin(theta) + Y0

    ax1.plot(x, y)
    ax1.plot([X0], [Y0], "o")
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')
    ax1.set_title('$r = %.3f$, $x_0 = %.3f$, $y_0 = %.3f$'%(r_, X0, Y0))
    ax2.hist(r)
    ax1.axis("equal")
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('$r$')
    plt.tight_layout()

    plt.savefig("%s.png"%name)


plot_file('Canal_ionico')
plot_file('Canal_ionico1')
