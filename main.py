__author__ = 'arajendran'

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#create demo array
Z = np.random.randint(0,2,(256,512))

def genarray(r,c):
    return np.random.randint(0,2,(r,c))

def neighbors(Z):
    N = np.zeros(Z.shape, dtype=int)
    N[1:-1,1:-1] += (Z[:-2, :-2] + Z[ :-2,1:-1] + Z[:-2,2:] +
                     Z[1:-1, :-2] + Z[1:-1,2:] +
                     Z[2:, :-2] + Z[2:,1:-1] + Z[2:,2:])
    return N

def evolve(Z):
    N = neighbors(Z)
    birth = (N == 3) & (Z == 0)
    survive = ((N == 3) | (N == 2)) & (Z == 1)
    Z = np.zeros(Z.shape, dtype = int)
    Z[1:-1,1:-1][birth[1:-1,1:-1] | survive[1:-1,1:-1]] = 1
    return Z

def iterate(Z,n):
    for i in range(n):
        Z = evolve(Z)
    return Z

def display(Z):
    plt.imshow(Z,interpolation='none')
    plt.show()





