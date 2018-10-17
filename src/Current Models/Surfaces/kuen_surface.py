# A Kuen Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Kuen Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges):    
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
    u = linspace(-4, 4,  sides + 1)
    v = linspace(-3.75, 3.75, edges)

    u, v = meshgrid(u, v)

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
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    # Surface Plot
    kuen = ax.plot_surface(x, y, z)

    kuen.set_alpha(alpha)  # Transparency of figure
    kuen.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    kuen.set_linewidth(edge_w)  # Line width of the edges
    kuen.set_facecolor(color)  # General color of the figure
