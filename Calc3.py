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
X_hex       = [1, 5, 2]
Y_hex       = [2, 1, 3]
Z_hex       = [3, 5, 3]

# The edges
edges_hex   = [(0,1), (1,2), (2,0)]

# Produces the segments for the Hexagonal Face
xyz_hex         = list(zip(X_hex, Y_hex, Z_hex))
segments_hex    = [(xyz_hex[s], xyz_hex[t]) for s, t in edges_hex]

# Produces the Figure space
fig = plt.figure(figsize=(5,5))
ax  = p3.Axes3D(fig)

# Figure Properties
ax.set_facecolor('white')

#plt.axis('off')
plt.axis('equal')

# Axis Limits
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(0,5)

# Plots the individual points
## (s) defines the size of the marker
## (c) defines the color of the marker

ax.scatter(X_hex,   Y_hex,  Z_hex,
           marker   =   'o',
           s        =   128,
           c        =   'blue'
           )

# Plots the edges of the Hexagonal Face
edge_hex   = Line3DCollection(segments_hex)
edge_hex.set_linewidth(1.0)
edge_hex.set_color('black')


# Visualizes via plt.show()
ax.add_collection3d(edge_hex)

# Produces the labels and arrows of the Hexagonal Face
for j, xyz_ in enumerate(xyz_hex):
   hex = annotate3D(ax,
               s                    =   (j, X_hex[j], Y_hex[j]),
               xyz                  =   xyz_,
               fontsize             =   8,
               xytext               =   (-3,3),
               textcoords           =   'offset points',
               horizontalalignment  =   'right',
               verticalalignment    =   'bottom',
               arrowprops           =   dict(arrowstyle='<-', connectionstyle="arc3, rad=0.5")
                    )


# Turns off plt.show()'s GUI coordinate display
ax.format_coord = lambda x, y: ""

# Shows plot
plt.show()