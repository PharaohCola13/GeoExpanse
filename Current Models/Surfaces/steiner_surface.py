# A Steiner's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
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

    stein_surf.set_alpha(alpha)  # Transparency of figure
    stein_surf.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    stein_surf.set_linewidth(edge_w)  # Line width of the edges
    stein_surf.set_facecolor(color)  # General color of the figure
