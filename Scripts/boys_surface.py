#  (Cos[u]*((1/3)*Sqrt[2]*Cos[u]*Sin[2*v] -
#  (2/3)*Sin[u]*Sin[v]))/ (1 - Sqrt[2]*Sin[u]*Cos[u]*Sin[3*v]),
#  (Cos[u]*Cos[u])/(1 - Sqrt[2]*Sin[u]*Cos[u]*Sin[3*v]) - 1},
# {u, 0, π}, {v, 0, π}]

# A Boy's Surface, brought to you by PharaohCola13

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
        x = (cos(u) * ((1/3)*sqrt(2)*cos(u)*cos(2*v) + (2/3) * sin(u) * cos(v))) / (1 - sqrt(2)*sin(u) * cos(u)*sin(3 * v))
        return x

    # Definition of y
    def y_(u, v):
        y = (cos(u) * ((1/3)*sqrt(2)*cos(u)*sin(2*v) - (2/3) * sin(u) * sin(v))) / (1 - sqrt(2)*sin(u) * cos(u)*sin(3 * v))
        return y


    # Definition of z
    def z_(u, v):
        z = cos(u)**2 / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v)) - 1
        return z

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
    boys_surf = ax.plot_surface(x, y, z)

    boys_surf.set_alpha(1)  # Transparency of figure
    boys_surf.set_edgecolor('w')  # Edge color of the lines on the figure
    boys_surf.set_linewidth(0.5)  # Line width of the edges
    boys_surf.set_facecolor('deepskyblue')  # General color of the figure


    # Definitions for animation
    def init():
        return boys_surf,


    def animate(i):
        # azimuth angle : 0 deg to 360 deg
        # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        # azim = i * n --> rotates object around the z axis with a magnitude of n
        # For top view elev = 90
        # For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return boys_surf,


    # Animate
    #ani = FuncAnimation(fig, animate, init_func=init,
     #                   frames=100, interval=20, blit=False, repeat=True)

    # Saving to Boy's-Surface.mp4

    # Writer = writers['ffmpeg']
    # writer = Writer(fps=15, bitrate=1800)

    # ani.save('Boy's-Surface.mp4', writer=writer)

    plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))
