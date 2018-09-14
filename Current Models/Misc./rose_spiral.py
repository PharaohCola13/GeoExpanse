# A Rose Spiral, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides):
    # Definition of x
    def x_(u, v):
        x = r * cos(u) * sin(v)
        return x

    # Definition of y
    def y_(u, v):
        y = r * sin(u) * sin(v)
        return y


    # Definition of z
    def z_(u, v):
        z = r * cos(v)
        return z

    # Value of the angles
    u = linspace(0, 2* pi, 100)
    v = linspace(0, pi, 100)

    u, v = meshgrid(u, v)

    r = 2 + sin(7 * u + 5 * v)

    # Symbolic representation
    x = x_(u, v)
    y = y_(u, v)
    z = z_(u, v)

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')  # Figure background turns black

    # Axis Properties
    plt.axis(grid)  # Turns off the axis grid
    plt.axis('equal')

    # Axis Limits
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

    # Surface Plot
    rose = ax.plot_surface(x, y, z)

    rose.set_alpha(alpha)  # Transparency of figure
    rose.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    rose.set_linewidth(edge_w)  # Line width of the edges
    rose.set_facecolor(color)  # General color of the figure


    # Definitions for animation
    def animate(i):
        # azimuth angle : 0 deg to 360 deg
        # elev = i * n --> rotates object about the xy-plane with a magnitude of n
        # azim = i * n --> rotates object around the z axis with a magnitude of n
        # For top view elev = 90
        # For side view elev = 0

        ax.view_init(elev=29, azim=i * 4)
        return rose,


    # Animate
    ani = FuncAnimation(fig, animate,
                       frames=100, interval=20, blit=False, repeat=True)

    # Saving to Rose-Spiral.mp4

    # Writer = writers['ffmpeg']
    # writer = Writer(fps=15, bitrate=1800)

    # ani.save('Rose-Spiral.mp4', writer=writer)
