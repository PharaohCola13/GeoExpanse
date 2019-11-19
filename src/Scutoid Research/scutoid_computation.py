# A computational model of a Scutoid, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

# Used to generate the labels
class Annotation3D(Annotation):
    '''Annotate the point xyz with text s'''

    def __init__(self, s, xyz, *args, **kwargs):
        Annotation.__init__(self,s, xy=(0,0), *args, **kwargs)
        self._verts3d = xyz

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.xy=(xs,ys)
        Annotation.draw(self, renderer)

def annotate3D(ax, s, *args, **kwargs):
    '''add anotation text s to to Axes3d ax'''

    tag = Annotation3D(s, *args, **kwargs)
    ax.add_artist(tag)


# Definition of x,y,z coordinates of the Hexagonal Face
X_hex       = [cos(pi/3), cos(2*pi/3), cos(pi), cos(4*pi/3), cos(5*pi/3), cos(2*pi)]
Y_hex       = [sin(pi/3), sin(2*pi/3), sin(pi), sin(4*pi/3), sin(5*pi/3), sin(2*pi)]
Z_hex       = [1,         1,           1,       1,           1,           1]

# Definition of x,y,z coordinates of the Pentagonal Face
X_pent      = [0, -sin(2*pi/5), -sin(pi/5), sin(pi/5), sin(2*pi/5)]
Y_pent      = [1, cos(2*pi/5),  -cos(pi/5), -cos(pi/5), cos(2*pi/5)]
Z_pent      = [0, 0,            0,          0,          0]

# Definition of x,y,z coordinates of the Triangle
X_tri       = [0.5,     0.0,    -0.5]
Y_tri       = [0.866,   1.0,    0.866]
Z_tri       = [1.0,     0.5,    1.0]

# Definition of x,y,z coordinates of the connecting edges
X           = [0.0, 0.0,  cos(pi),  -sin(2*pi/5),  cos(4*pi/3),  -sin(pi/5), cos(5*pi/3), sin(pi/5),  cos(2*pi), sin(2*pi/5)]
Y           = [1.0, 1.0,  sin(pi),  cos(2*pi/5),   sin(4*pi/3),  -cos(pi/5), sin(5*pi/3), -cos(pi/5), sin(2*pi), cos(2*pi/5)]
Z           = [0.5, 0.0,  1.0,      0.0,           1.0,           0.0,       1.0,         0.0,        1.0,       0.0]

# The edges
edges_hex   = [(0,1), (1,2), (2,3), (3,4), (5,4), (5,0)]
edges_pent  = [(0,1), (1,2), (2,3), (3,4), (4,0)]
edges_tri   = [(0,1), (1,2)]
edges       = [(0,1), (2,3), (4,5), (6,7), (8,9)]

# Produces the segments for the Hexagonal Face
xyz_hex         = list(zip(X_hex, Y_hex, Z_hex))
segments_hex    = [(xyz_hex[s], xyz_hex[t]) for s, t in edges_hex]

# Produces the segments for the Pentagonal Face
xyz_pent        = list(zip(X_pent, Y_pent, Z_pent))
segments_pent   = [(xyz_pent[s], xyz_pent[t]) for s, t in edges_pent]

# Produces the segments for the Triangle
xyz_tri         = list(zip(X_tri, Y_tri, Z_tri))
segments_tri    = [(xyz_tri[s], xyz_tri[t]) for s, t in edges_tri]

# Produces the segments for the connecting edges
xyz             = list(zip(X, Y, Z))
segments        = [(xyz[s], xyz[t]) for s, t in edges]

# Produces the Figure space
fig = plt.figure(figsize=(5,5))
ax  = p3.Axes3D(fig)

# Figure Properties
ax.set_facecolor('white')

plt.axis('off')
plt.axis('equal')

# Axis Limits
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.set_zlim(0,1)

# Plots the individual points
## (s) defines the size of the marker
## (c) defines the color of the marker

ax.scatter(X_hex,   Y_hex,  Z_hex,
           marker   =   'o',
           s        =   128,
           c        =   'blue'
           )

ax.scatter(X_pent,  Y_pent, Z_pent,
           marker   =   'o',
           s        =   128,
           c        =   'red'
           )

ax.scatter(X_tri,   Y_tri,  Z_tri,
           marker   =   'o',
           s        =   128,
           c        =   'green'
           )

# Plots the edges of the Hexagonal Face
edge_hex   = Line3DCollection(segments_hex)
edge_hex.set_linewidth(1.0)
edge_hex.set_color('black')

# Plots the edges of the Pentagonal Face
edge_pent  = Line3DCollection(segments_pent)
edge_pent.set_linewidth(1.0)
edge_pent.set_color('black')

# Plots the edges of the Triangle
edge_tri   = Line3DCollection(segments_tri)
edge_tri.set_linewidth(1.0)
edge_tri.set_color('black')

# Plots the edges of the connecting edges
edges      = Line3DCollection(segments)
edges.set_linewidth(1.0)
edges.set_color('black')

# Visualizes via plt.show()
ax.add_collection3d(edge_hex)
ax.add_collection3d(edge_pent)
ax.add_collection3d(edge_tri)
ax.add_collection3d(edges)

# Produces the labels and arrows of the Hexagonal Face
for j, xyz_ in enumerate(xyz_hex):
   hex = annotate3D(ax,
               s                    =   (j, round(X_hex[j], 3), round(Y_hex[j], 3)),
               xyz                  =   xyz_,
               fontsize             =   8,
               xytext               =   (-3,3),
               textcoords           =   'offset points',
               horizontalalignment  =   'right',
               verticalalignment    =   'bottom',
               arrowprops           =   dict(arrowstyle='<-', connectionstyle="arc3, rad=0.5")
                    )

# Produces the labels and arrows of the Pentagonal Face
for j, xyz_ in enumerate(xyz_pent):
    pent = annotate3D(ax,
                s                   =   ((j), round(X_pent[j], 3), round(Y_pent[j], 3)),
                xyz                 =   xyz_,
                fontsize            =   8,
                xytext              =   (-1, 1),
                textcoords          =   'offset points',
                horizontalalignment =   'right',
                verticalalignment   =   'bottom',
                arrowprops          =   dict(arrowstyle='<-', connectionstyle="arc3, rad=0.5")
                      )

# Turns off plt.show()'s GUI coordinate display
ax.format_coord = lambda x, y: ""

# Shows plot
plt.show()