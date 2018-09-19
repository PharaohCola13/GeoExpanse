# Breather's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Breather's-Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
# Definition of x
    def x_(u, v):
        x = (-u + (2. * w * cosh(b*u) * sinh(b*u) / (b * ((w * cosh(b * u))**2 + (b * sin(w * v))**2))))
        return x

# Definition of y
    def y_(u, v):
        y = (2. * w * cosh(b * u) * (-1 * (w * cos(v) * cos(w * v)) - sin(v) * sin(w * v)) / (b * ((w * cosh(b * u))**2 + (b * sin(w * v))**2)))
        return y


# Definition of z
    def z_(u, v):
        z = (2. * w * cosh(b * u) * (-(w * sin(v) * cos(w * v)) + cos(v) * sin(w * v))) / (b * ((w * cosh(b * u))**2 + (b * sin(w * v))**2))
        return z

    b = 0.4
    r = 1. - b**2
    w = sqrt(r)
# Value of the angles
    u = linspace(-13.2,  13.2, 75)
    v = linspace(-37.4, 37.4, 75)

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
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

# Surface Plot
    breath_surf = ax.plot_surface(x, y, z)

    breath_surf.set_alpha(alpha)  # Transparency of figure
    breath_surf.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    breath_surf.set_linewidth(edge_w)  # Line width of the edges
    breath_surf.set_facecolor(color)  # General color of the figure