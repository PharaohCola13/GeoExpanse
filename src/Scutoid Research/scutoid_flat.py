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


X_hex = [0.0, 1.0, 2.0, 3.0, 4.0, 4.9935]
Y_hex = [2.5, 2.5, 2.5, 2.5, 2.5, 2.3781]

X_pent = [0, 1, 2, 3, 3.9925, 4.9855]
Y_pent = [0, 0, 0, 0, -0.121, -0.24]

X_edge = [0.0, 0.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.43137, 3.99245, 4.9935]
Y_edge = [0.0, 2.5, 0.0, 2.5, 0.0, 2.5, 0.0, 2.5, 0.0, 0.47921, 2.37813, -0.24]

Z = [0,0,0,0,0,0,0,0,0,0,0,0,0]

edges_hex  = [(0,1), (1,2), (2,3), (3,4), (4,5)]
edges_pent = [(0,1), (1,2), (2,3), (3,4), (4,5)]
edges_edge = [(0,1), (2,3), (4,5), (6,7),(8,9),(9,10), (9,11)]

xy_hex = list(zip(X_hex, Y_hex, Z))
segments_hex = [(xy_hex[s], xy_hex[t]) for s, t in edges_hex]

xy_pent = list(zip(X_pent, Y_pent, Z))
segments_pent = [(xy_pent[s], xy_pent[t]) for s, t in edges_pent]

xy_edge = list(zip(X_edge, Y_edge, Z))
segments_edge = [(xy_edge[s], xy_edge[t]) for s, t in edges_edge]


# Produces the Figure space
fig = plt.figure(figsize=(5,5))
ax  = p3.Axes3D(fig)

# Figure Properties
ax.set_facecolor('white')

plt.axis('off')
plt.axis('equal')

# Axis Limits
ax.set_xlim(0,5)
ax.set_ylim(0,5)
#ax.set_zlim(0,1)

ax.scatter(X_hex, Y_hex,
           marker   =   'o',
           s        =   64,
           c        =   'blue'
           )
edge_hex = Line3DCollection(segments_hex)
edge_hex.set_linewidth(1.0)
edge_hex.set_color('black')

ax.scatter(X_pent, Y_pent,
           marker   =   'o',
           s        =   64,
           c        =   'red'
           )
edge_pent = Line3DCollection(segments_pent)
edge_pent.set_linewidth(1.0)
edge_pent.set_color('black')

edge_edge = Line3DCollection(segments_edge)
edge_edge.set_linewidth(1.0)
edge_edge.set_color('black')


ax.add_collection3d((edge_hex))
ax.add_collection3d((edge_pent))
ax.add_collection3d((edge_edge))

# Turns off plt.show()'s GUI coordinate display
ax.format_coord = lambda x, y: ""


plt.show()
