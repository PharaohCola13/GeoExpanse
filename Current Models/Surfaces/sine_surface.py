# A Sphere, brough to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *


name = "Sine Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi):
    # Definition of x
    def x_(u,v):
            x = a * sin(u)
            return x

    # Definition of y
    def y_(u,v):
            y = a * sin(v)
            return y

    # Definition of z
    def z_(u,v):
            z  = a * sin(u + v)
            return z

    a = 1 #
    # Values of the angles
    u = linspace(0, 2 * pi, 50)
    v = linspace(0, 2 * pi, 50)

    u, v = meshgrid(u, v)

    # Symbolic Representation
    x = x_(u,v)
    y = y_(u,v)
    z = z_(u,v)

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black') # Figure background turns black

    # Axis Properties
    plt.axis(grid) # Turns off the axis grid
    plt.axis('equal')

    # Axis Limits
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)

    # Surface Plot
    sine = ax.plot_surface(x, y, z)

    sine.set_alpha(alpha) # Transparency of figure
    sine.set_edgecolor(edge_c) # Edge color of the lines on the figure
    sine.set_linewidth(edge_w) # Line width of the edges
    sine.set_facecolor(color) # General color of the figure
