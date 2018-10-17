#{u, Sin[v]*(u^3+2u^2-2u+2)/5, Cos[v]*(u^3+2u^2-2u+2)/5}

# A Vase, brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Vase"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi):
    # Definition of x
    def x_(u, v):
        x = u
        return x

    # Definition of y
    def y_(u, v):
        y = sin(v) * (u**3 + 2* u**2 - (2 * u + 2))/5
        return y


    # Definition of z
    def z_(u, v):
        z = cos(v) * (u**3 + 2 * u**2 - (2 * u +2))/5
        return z

    # Value of the angles
    u = linspace(0, 1, 25)
    v = linspace(0, 2 * pi, 25)

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
    #ax.set_xlim(-5, 5)
    #ax.set_ylim(-5, 5)
    #ax.set_zlim(-5, 5)

    # Surface Plot
    vase = ax.plot_surface(x, y, z)

    vase.set_alpha(alpha)  # Transparency of figure
    vase.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    vase.set_linewidth(edge_w)  # Line width of the edges
    vase.set_facecolor(color)  # General color of the figure
