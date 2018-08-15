# A Tesseract, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

points = np.array([[-1, -1, -1],
                   [1, -1, -1 ],
                   [1, 1, -1],
                   [-1, 1, -1],
                   [-1, -1, 1],
                   [1, -1, 1 ],
                   [1, 1, 1],
                   [-1, 1, 1]])

# Scaling Matricies
P = [[2, 0, 0],
     [0, 2, 0],
     [0, 0, 2]]

Q = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

Z = np.zeros((8,3))
V = np.zeros((8,3))

for i in range(8): 
	Z[i,:] = np.dot(points[i,:],P)

for i in range(8):
	V[i,:] = np.dot(points[i,:],Q)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-4,4)

# Interval
r = [-1,1]

X, Y = np.meshgrid(r, r)

# Outer Region Configuration
verts_outer = [[Z[0],V[0], V[1], Z[1]],
	       [Z[1],V[1],V[5],Z[5]], 
	       [Z[0],V[0],V[4],Z[4]], 
	       [Z[4],V[4],V[5],Z[5]], 
	       [Z[5],V[5],V[6],Z[6]],
	       [Z[1],V[1],V[2],Z[2]], 
	       [Z[2],V[2],V[6],Z[6]],
	       [Z[2],V[2],V[3],Z[3]],
	       [Z[6],V[6],V[7],Z[7]],
	       [Z[7],V[7],V[3],Z[3]],
	       [Z[0],V[0],V[3],Z[3]],
	       [Z[4],V[4],V[7],Z[7]]]

# Inner Cube Configuration
verts_inner = [[V[0],V[1],V[2],V[3]],
	       [V[4],V[5],V[6],V[7]],
	       [V[0],V[4],V[5],V[1]],
	       [V[1],V[5],V[6],V[2]],
	       [V[2],V[6],V[7],V[3]],
	       [V[3],V[7],V[4],V[0]]]

# Outside Region
outer_region = Poly3DCollection(verts_outer)

outer_region.set_edgecolor('white')
outer_region.set_linewidth(1)
outer_region.set_alpha(0.2)
outer_region.set_facecolor('blue')

# Inside Cube
inside_cube = Poly3DCollection(verts_inner)

inside_cube.set_edgecolor('white')
inside_cube.set_linewidth(1)
inside_cube.set_alpha(0.5)
inside_cube.set_facecolor('purple')


# Plot Surfaces
o = ax.add_collection3d(outer_region)
i = ax.add_collection3d(inside_cube)

# Defintions for animations
def init():
    return o,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=i, azim= 4 * i)
    return o,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                   frames=88, interval=1, blit=False, repeat=True)

#Saving to Tesseract.mp4
#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Tesseract.mp4', writer=writer)

plt.show()
