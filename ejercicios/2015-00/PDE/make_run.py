import numpy as np
import os
import matplotlib.pyplot as plt

command = 'rm output*.dat'
os.system(command)
command = 'rm output*.jpg'
os.system(command)

n_times = 10
times = np.linspace(0,1.0, n_times)
print('{}'.format(times))

fileout_list = []
figure_list = ''
for i in range(n_times):
    fileout = 'output_{}.dat'.format(i)
    figure_name = fileout.replace('dat','jpg') 
    print(fileout)
    fileout_list.append(fileout)
    command = './burgers {} > {}'.format(times[i], fileout)
    print command
    os.system(command)
    
    data = np.loadtxt(fileout)
    plt.figure()
    plt.plot(data[:,0], data[:,1])
    plt.savefig(figure_name)
    plt.close()
    figure_list = figure_list + ' {} '.format(figure_name)

command = 'convert -delay 10 -loop 0 {} animation.gif'.format(figure_list)
os.system(command)
command = 'rm output*.dat'
os.system(command)
command = 'rm output*.jpg'
os.system(command)
