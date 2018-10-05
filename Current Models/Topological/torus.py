# A Family of Torus, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Torus"


def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radius):

    # Definition of x
    def x_(u, v):
        x = 2 * ((c + a * cos(u)) * cos(v))
        return x

    # Definition of y
    def y_(u, v):
        y = 2 * ((c + a * cos(u)) * sin(v))
        return y

    # Definition of z
    def z_(u, v):
        z = 2 * (a * sin(u))
        return z

    # Radius
    c = radius

    # Radius of the tube
    a = edges

    # Values of the angles
    s = sides
    u = linspace(0, 2 * pi, s + 1)
    v = linspace(0, 2 * pi, edges)

    u, v = meshgrid(u, v)

    # Symbolic Representation
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
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.set_zlim(-50, 50)

    # Surface Plot
    torus = ax.plot_surface(x, y, z, rstride=5, cstride=5)

    torus.set_alpha(alpha)  # Transparency of figure
    torus.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    torus.set_linewidth(edge_w)  # Line width of the edges
    torus.set_facecolor(color)  # General color of the figure

# if c > a:
#	name = 'Ring-Torus'
# elif c == a:
#	name = 'Horn-Torus'
# elif c < a:
#	name = 'Spindle-Torus'
