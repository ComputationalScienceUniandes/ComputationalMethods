# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:34:47 2016

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

names = ['data_A.txt', 'data_B.txt', 'data_C.txt']      # names of files
datas = [np.genfromtxt(name) for name in names]         # loads the data

names = [name.split(".txt", 1)[0] + ".pdf" for name in names]       # changes extention for plotting

cov_matrixes = [np.cov(data.T) for data in datas]       # gets the covariance matrix

for (cov, data, name) in zip(cov_matrixes, datas, names):
    values, vectors = np.linalg.eig(cov)        # gets the eigenvalues and eigenvectors of cov
    
    dimention = len(values)         # dimention of data
    sort_perm = values.argsort()        # ordered positions

    values[sort_perm]       # sorts eigenvalues following sort_perm positions
    vectors = vectors[:, sort_perm]         # sorts eigenvectors following sort_perm positions
    
    if dimention == 2:
        x, y = data[:,0], data[:,1]
        second, principal = np.dot(data, vectors).T         # change of basis
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))
        
        ax1.plot(x, y, "o")
        ax1.axis('equal')       # makes x and y lims equal
        ax1.grid()
        ax1.set_xlabel('$x$')
        ax1.set_ylabel('$y$')
        
        ax2.plot(principal, second, "o")
        ax2.axis('equal')
        ax2.grid()
        ax2.set_xlabel('1st Principal Component')
        ax2.set_ylabel('2nd Principal Component')

    elif dimention == 3:
        x, y, z = data[:,0], data[:,1], data[:,2]
        third, second, principal = np.dot(data, vectors).T      # change of basis
        
        fig = plt.figure(figsize=(10,4))
        ax1 = fig.add_subplot(121, projection='3d')
        
        ax1.scatter(x, y, z)
        ax1.set_xlabel('$x$')
        ax1.set_ylabel('$y$')
        ax1.set_zlabel('$z$')
        
        ax2 = fig.add_subplot(122, projection='3d')
        
        ax2.scatter(principal, second, third)
        
        min_principal = min(principal)
        max_principal = max(principal)
        ax2.set_ylim(min_principal, max_principal)      # makes x, y and z lims equal
        ax2.set_zlim(min_principal, max_principal)
        
        ax2.set_xlabel('1st Principal Component', fontsize=10)
        ax2.set_ylabel('2nd Principal Component', fontsize=10)
        ax2.set_zlabel('3rd Principal Component', fontsize=10)
        
    fig.tight_layout()      # improves spacing
    fig.savefig(name)
    
    plt.close()