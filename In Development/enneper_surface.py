# Enneper Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Enneper Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
    def x_(u,v):
        x = u - (u**3/3) + (u * v**2)
        return x

    def y_(u,v):
        y = v - (v**3/3) + (v * u**2)
        return y

    def z_(u,v):
        z = u**2 - v**2
        return z

    u = linspace(-pi,pi, 100)
    v = linspace(-pi,pi, 100)

    u, v = meshgrid(u, v)

    x = x_(u,v)
    y = y_(u,v)
    z = z_(u,v)

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')

    plt.axis(grid)
    plt.axis('equal')

    # Surface Plot
    interest = ax.plot_surface(x, y, z)

    interest.set_alpha(alpha)
    interest.set_edgecolor(edge_c)
    interest.set_linewidth(edge_w)
    interest.set_facecolor(color)
