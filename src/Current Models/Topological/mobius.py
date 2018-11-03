# A Mobius Band, brought to you by PharaohCola13

# triangulate in the underlying parametrization
from matplotlib.tri import Triangulation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers
from matplotlib import cm

name = "Mobius Strip"
def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor):

    # Mobius Band components
    theta = np.linspace(0, 2 * np.pi, 30)

    w = np.linspace(-0.25, 0.25, 8)
    w, theta = np.meshgrid(w, theta)

    phi = 0.5 * theta

    # radius in x-y plane
    r = 1 + w * np.cos(phi)

    x = np.ravel(r * np.cos(theta))
    y = np.ravel(r * np.sin(theta))
    z = np.ravel(w * np.sin(phi))

    tri = Triangulation(np.ravel(w), np.ravel(theta))

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor(figcolor)

    plt.axis(grid)
    plt.axis('equal')

    # Axis Limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)


    # Mobius Band
    mb = ax.plot_trisurf(x, y, z, triangles=tri.triangles)

    mb.set_linewidth(edge_w)
    mb.set_edgecolor(edge_c)
    mb.set_alpha(alpha)
    mb.set_facecolor(color)
