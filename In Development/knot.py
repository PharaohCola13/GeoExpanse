# Some Knots, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Knot"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi):
    def x_(u,v):
        x = sin(v) + 2 * sin(2 * v)
        return x

    def y_(u,v):
        y = cos(v) - 2 * cos(2 * v)
        return y

    def z_(u,v):
        z = -sin(u)
        return z

    u = linspace(0, 4 * pi, 100)
    v = linspace(0, 2 * pi, 100)

    u,v = np.meshgrid(u,v)

    x = x_(u,v)
    y = y_(u,v)
    z = z_(u,v)

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')

    plt.axis(grid)
    plt.axis('equal')

    # ax.set_xlim(-5,5)
    # ax.set_ylim(-5,5)
    ax.set_zlim(-5,5)

    # Surface plot
    k = ax.plot_surface(x, y, z, rstride=10, cstride=10)

    k.set_linewidth(edge_w)
    k.set_edgecolor(edge_c)
    k.set_alpha(alpha)
    k.set_facecolor(color)
