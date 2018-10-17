# A Octohedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Octahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid):

# Points on the object
	points = array([
				   [1, 0, 0],
				   [0, 1, 0],
				   [0, 0, 1],
				   [-1, 0, 0],
				   [0, -1, 0],
				   [0, 0, -1]
				   ])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
	    [0, 1, 0],
	    [0, 0, 1]
		]

	Z = zeros((6,3))


	for i in range(6):
		Z[i,:] = dot(points[i,:],P)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black
	
# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

# The edges of the object
	verts = [
			[Z[0], Z[1], Z[3], Z[4], Z[0]],
			[Z[0], Z[2], Z[1]], 
			[Z[1], Z[2], Z[3]],
			[Z[3], Z[2], Z[4]],
			[Z[4], Z[2], Z[0]],
			[Z[0], Z[5], Z[1]], 
			[Z[1], Z[5], Z[3]],
			[Z[3], Z[5], Z[4]],
			[Z[4], Z[5], Z[0]]	
			]

# Surface plot
	octa = Poly3DCollection(verts)

	octa.set_edgecolor(edge_c)
	octa.set_linewidth(edge_w)
	octa.set_alpha(alpha)
	octa.set_facecolor(color)

	octahedron = ax.add_collection3d(octa)
