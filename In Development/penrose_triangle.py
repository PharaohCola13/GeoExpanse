# A pen_tri, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Penrose Triangle"


def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
          edges, multi_pi, radius):
    points = array([[0.09, 2.761, 0], #0
                    [-2.66, -2.19, 0], #1
                    [3.284, -2.19, 0], #2
                    [6.315, -2.189, 0], #3
                    [-1.505, 5.229, 0], #4
                    [-8.328, -6.883, 0], #5
                    [9.254, -6.89, 0], #6
                    [10.685, -4.45, 0], #7
                    [1.227, 10.022, 0], #8
                    [-1.563, 10.022, 0], #9
                    [-9.804, -4.602, 0], #10
                    [-3.916, -4.449, 0], #11
                    ])

    # Scaling Matricies
    P = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

    Z = zeros((12, 3))

    for i in range(12):
        Z[i, :] = dot(points[i, :], P)

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')

    plt.axis(grid)
    plt.axis('equal')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(0, 0)
    ax.view_init(elev=90, azim=0)

    # Side Configuration for pen_tri
    verts_pen_tri = [#[Z[0], Z[1], Z[2]],
                  [Z[1], Z[3]],
                  [Z[3], Z[9]],
                  [Z[9], Z[10], Z[5], Z[6], Z[7], Z[8]],
                  [Z[2], Z[4]],
                  [Z[4], Z[5]],
                  [Z[0], Z[11]],
                  [Z[11],Z[7]],
                  ]

    # pen_tri Proprties
    pen_tri = Poly3DCollection(verts_pen_tri)

    pen_tri.set_edgecolor(edge_c)
    pen_tri.set_linewidth(edge_w)
    pen_tri.set_alpha(alpha)
    pen_tri.set_facecolor(color)

    # Plot Surfaces
    ax.add_collection3d(pen_tri)
