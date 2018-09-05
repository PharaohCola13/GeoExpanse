# {Sqrt[2]*Cos[2*u]*Cos(v)^2+Cos[u]*Sin[2*v]/(2-(b*Sqrt[2]*Sin[3*u]*Sin[2*v])),

#  Sqrt[2]*Sin[2*u]*Cos(v)^2-Sin[u]*Sin[2*v]/(2-(b*Sqrt[2]*Sin[3*u]*Sin[2*v])),

#  3*[Cos[v]]^2/(2-(b*Sqrt[2]*Sin[3*u]*Sin[2*v]))-1}

# A Steiner's Surface, brought to you by PharaohCola13

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
        x = sqrt(2) * cos(2 * u) * cos(v)**2 + cos(u) * sin(2 * v) / (2 - (b * sqrt(2) * sin(3 * u) * sin(2 * v)))
        return x

    # Definition of y
    def y_(u, v):
        y =  sqrt(2) * sin(2 * u) * cos(v)**2 - sin(u) * sin(2 * v) / (2 - (b * sqrt(2) * sin(3 * u) * sin(2 * v)))
        return y


    # Definition of z
    def z_(u, v):
        z = 3 * (cos(v)**2 / (2 - (b * sqrt(2) * sin(3 * u) * sin(2 * v)))) - 1
        return z

    b = linspace(0, 1, 75)
    # Value of the angles
    u = linspace(0, pi, 75)
    v = linspace(0, pi, 75)

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
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    # Surface Plot
    stein_surf = ax.plot_surface(x, y, z)

    stein_surf.set_alpha(1)  # Transparency of figure
    stein_surf.set_edgecolor('w')  # Edge color of the lines on the figure
    stein_surf.set_linewidth(0.5)  # Line width of the edges
    stein_surf.set_facecolor('deepskyblue')  # General color of the figure


    # Definitions for animation
    def init():
        return stein_surf,


    def animate(i):
        # azimuth angle : 0 deg to 360 deg
        # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        # azim = i * n --> rotates object around the z axis with a magnitude of n
        # For top view elev = 90
        # For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return stein_surf,


    # Animate
    #ani = FuncAnimation(fig, animate, init_func=init,
     #                   frames=100, interval=20, blit=False, repeat=True)

    # Saving to Steiner's-Surface.mp4

    # Writer = writers['ffmpeg']
    # writer = Writer(fps=15, bitrate=1800)

    # ani.save('Steiner's-Surface.mp4', writer=writer)

    plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))
