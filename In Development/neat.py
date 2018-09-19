# Some Knots, brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Neat"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
    def x_(u,v):
        x = 0.5 * (v * cos(u))
        return x

    def y_(u,v):
        y = 0.5 * (u * sin(v))
        return y

    def z_(u,v):
        z = u
        return z

    u = linspace(-2 * pi, 2 * pi, 25)
    v = linspace(-2 * pi, 2 * pi, 25)

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
    N = ax.plot_surface(x, y, z, rstride=1, cstride=1)


    N.set_linewidth(edge_w)
    N.set_edgecolor(edge_c)
    N.set_alpha(alpha)
    N.set_facecolor(color)