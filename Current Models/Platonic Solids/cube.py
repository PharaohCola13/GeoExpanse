# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Cube"

def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides):
	points = array([[-1, -1, -1],
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


	Z = zeros((8,3))

	for i in range(8): 
		Z[i,:] = dot(points[i,:],P)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')
	
	plt.axis(grid)
	plt.axis('equal')
	
	ax.set_xlim(-4,4)
	ax.set_ylim(-4,4)
	ax.set_zlim(-4,4)

# Interval
	r = [-1,1]

	X, Y = np.meshgrid(r, r)

# Side Configuration for Cube
	verts_cube = [[Z[0],Z[1],Z[2],Z[3]],
				[Z[4],Z[5],Z[6],Z[7]], 
				[Z[0],Z[1],Z[5],Z[4]], 
				[Z[2],Z[3],Z[7],Z[6]], 
				[Z[1],Z[2],Z[6],Z[5]],
				[Z[4],Z[7],Z[3],Z[0]], 
				[Z[2],Z[3],Z[7],Z[6]]]


# Cube Properties
	cube = Poly3DCollection(verts_cube)

	cube.set_edgecolor(edge_c)
	cube.set_linewidth(edge_w)
	cube.set_alpha(alpha)
	cube.set_facecolor(color)

# Plot Surfaces
	ax.add_collection3d(cube)
