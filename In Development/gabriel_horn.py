#{u, Sin[v]*(u^3+2u^2-2u+2)/5, Cos[v]*(u^3+2u^2-2u+2)/5}

# A Gaberial's Horn, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:
    # Definition of x
    def x_(u, v):
        x = u
        return x

    # Definition of y
    def y_(u, v):
        y = (a * cos(v)) / u
        return y


    # Definition of z
    def z_(u, v):
        z = (a * sin(v)) /u
        return z

    a = 1 # changes width of tube

    # Value of the angles
    u = linspace(0.9, 2 * pi, 25)
    v = linspace(1, 2 * pi, 25)

    u, v = meshgrid(u, v)

    # Symbolic representation
    x = x_(u, v)
    y = y_(u, v)
    z = z_(u, v)

    # Figure Properties
    fig = plt.figure(figsize=(8, 8))

    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')  # Figure background turns black

    # Axis Properties
    plt.axis('off')  # Turns off the axis grid
    plt.axis('equal')

    # Axis Limits
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)

    # Surface Plot
    horn = ax.plot_surface(x, y, z)

    horn.set_alpha(1)  # Transparency of figure
    horn.set_edgecolor('w')  # Edge color of the lines on the figure
    horn.set_linewidth(1)  # Line width of the edges
    horn.set_facecolor('deepskyblue')  # General color of the figure


    # Definitions for animation
    def init():
        return horn,


    def animate(i):
        # azimuth angle : 0 deg to 360 deg
        # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        # azim = i * n --> rotates object around the z axis with a magnitude of n
        # For top view elev = 90
        # For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return horn,


    # Animate
    #ani = FuncAnimation(fig, animate, init_func=init,
     #                   frames=100, interval=20, blit=False, repeat=True)

    # Saving to Gaberial's-Horn.mp4

    # Writer = writers['ffmpeg']
    # writer = Writer(fps=15, bitrate=1800)

    # ani.save('Gaberial's-Horn.mp4', writer=writer)

    plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))
