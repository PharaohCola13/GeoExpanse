#{u, Sin[v]*(u^3+2u^2-2u+2)/5, Cos[v]*(u^3+2u^2-2u+2)/5}

# A Funnel, brought to you by PharaohCola13

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
        x = u * cos(v)
        return x

    # Definition of y
    def y_(u, v):
        y = u * sin(v)
        return y


    # Definition of z
    def z_(u, v):
        z = h * log1p(u)
        return z

# Determines the total height of the funnel
    height = float(input('What is the height of the funnel?\n>> '))
    h = height

# Defines the radius of the hole
    radius = float(input('What is the radius of the hole?\n>> '))
    r = radius

    # Value of the angles
    u = linspace(r, pi, 25)
    v = linspace(0, 2 * pi, 25)

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
    ax.set_xlim(-r-h , r+h)
    ax.set_ylim(-r-h, r+h)
    ax.set_zlim(0, 2 * h)

    # Surface Plot
    funnel = ax.plot_surface(x, y, z)

    funnel.set_alpha(1)  # Transparency of figure
    funnel.set_edgecolor('w')  # Edge color of the lines on the figure
    funnel.set_linewidth(1)  # Line width of the edges
    funnel.set_facecolor('deepskyblue')  # General color of the figure


    # Definitions for animation
    def init():
        return funnel,


    def animate(i):
        # azimuth angle : 0 deg to 360 deg
        # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        # azim = i * n --> rotates object around the z axis with a magnitude of n
        # For top view elev = 90
        # For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return funnel,


    # Animate
    #ani = FuncAnimation(fig, animate, init_func=init,
     #                   frames=100, interval=20, blit=False, repeat=True)

    # Saving to Funnel.mp4

    # Writer = writers['ffmpeg']
    # writer = Writer(fps=15, bitrate=1800)

    # ani.save('Funnel.mp4', writer=writer)

    plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))
