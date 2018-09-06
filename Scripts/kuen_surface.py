# {2*Cosh[v]*(Cos[u] + u*Sin[u]),
# 2*Cosh[v]*(-u*Cos[u] + Sin[u]),
# v - (2*Sinh[v]*Cosh[v])} / (Cosh[v]^2 + u^2)

# A Kuen Surface, brought to you by PharaohCola13

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
        x = 2 * cosh(v) * (cos(u) + u* sin(u)) / (cosh(v)**2 + u**2)
        return x

    # Definition of y
    def y_(u, v):
        y = 2 * cosh(v) * (-u * cos(u) + sin(u)) / (cosh(v)**2 + u**2)
        return y


    # Definition of z
    def z_(u, v):
        z = v - (2 * sinh(v) * cosh(v)) / (cosh(v)**2 + u**2)
        return z

    # Value of the angles
    u = linspace(-4, 4, 50)
    v = linspace(-3.75, 3.75, 50)

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
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    # Surface Plot
    kuen = ax.plot_surface(x, y, z)

    kuen.set_alpha(1)  # Transparency of figure
    kuen.set_edgecolor('w')  # Edge color of the lines on the figure
    kuen.set_linewidth(0.5)  # Line width of the edges
    kuen.set_facecolor('deepskyblue')  # General color of the figure


    # Definitions for animation
    def init():
        return kuen,


    def animate(i):
        # azimuth angle : 0 deg to 360 deg
        # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        # azim = i * n --> rotates object around the z axis with a magnitude of n
        # For top view elev = 90
        # For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return kuen,


    # Animate
    #ani = FuncAnimation(fig, animate, init_func=init,
     #                   frames=100, interval=20, blit=False, repeat=True)

    # Saving to Kuen-Surface.mp4

    # Writer = writers['ffmpeg']
    # writer = Writer(fps=15, bitrate=1800)

    # ani.save('Kuen-Surface.mp4', writer=writer)

    plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))
