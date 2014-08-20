__author__ = 'arajendran'

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import main

#function that takes frame rate n and dimensions r,c
def animate(n,r,c):
    #generate figure and initial array
    fig = plt.figure()
    Z = main.genarray(r,c)
    #set image object
    im = plt.imshow(Z,cmap=plt.get_cmap('jet'))

    #define function that updates the figure, by evolving Z and setting image array to new Z
    def updatefig(*args):
        global Z
        Z = main.evolve(Z)
        im.set_array(Z)
        return im,

    #animate by updating Z at frame rate n
    ani = animation.FuncAnimation(fig,updatefig,interval=n,blit=True)
    plt.show()
    return