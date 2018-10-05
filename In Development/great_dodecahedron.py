# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Great Dodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid):

	points = array([
		            [0.5,       0, 0.809],
		            [0.5,       0, -0.809],
		            [-0.5, 0, 0.809],
		            [-0.5, 0, -0.809],
		            [0.809, 0.5, 0],
		            [0.809, -0.5, 0],
		            [-0.809, 0.5, 0],
		            [-0.809, -0.5, 0],
		            [0, 0.809, 0.5],
		            [0, 0.809, -0.5],
		            [0, -0.809, 0.5],
		            [0, -0.809, -0.5]
		            ])
	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((12, 3))

	for i in range(12):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	fig = plt.figure(figsize=(8, 8))
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-4, 4)
	ax.set_ylim(-4, 4)
	ax.set_zlim(-4, 4)

	# Interval
	r = [-1, 1]

	X, Y = np.meshgrid(r, r)

	# Side Configuration for Cube
	# Cube Properties
	verts_cube = [[Z[0],Z[2],Z[7],Z[11],Z[5]],
		          [Z[0],Z[5],Z[1],Z[9],Z[8]],
		          [Z[0],Z[8],Z[6],Z[7],Z[10]],
		          [Z[1],Z[3],Z[6],Z[8],Z[4]],
		          [Z[1],Z[4],Z[0],Z[10],Z[11]],
		          [Z[1],Z[11],Z[7],Z[6],Z[9]],
		          [Z[2],Z[0],Z[4],Z[9],Z[6]],
		          [Z[2],Z[6],Z[3],Z[11],Z[10]],
		          [Z[2],Z[10],Z[5],Z[4],Z[8]],
		          [Z[3],Z[1],Z[5],Z[10],Z[7]],
		          [Z[3],Z[7],Z[2],Z[8],Z[9]],
		          [Z[3],Z[9],Z[4],Z[5],Z[11]],
		           ]

	cube = Poly3DCollection(verts_cube)

	cube.set_edgecolor(edge_c)
	cube.set_linewidth(edge_w)
	cube.set_alpha(alpha)
	cube.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(cube)
