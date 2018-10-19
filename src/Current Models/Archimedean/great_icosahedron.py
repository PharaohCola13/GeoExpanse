# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Great Icosahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid):

	points = array([[0,0,0],
					[0, 0, -0.5 * sqrt(0.5 * (5 - sqrt(5)))],
					[0, 0, 0.5 * sqrt(0.5 * (5 - sqrt(5)))],
					[sqrt(((1./8.)+(1/(8 *sqrt(5))))), -1/(1 +sqrt(5)), -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[sqrt(((1./8.) + (1/(8 * sqrt(5))))), 1/(1 + sqrt(5)), -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-sqrt(((1./8.) + (1/(8 * sqrt(5))))), -1/(1 + sqrt(5)), 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-sqrt(((1./8.) + (1/(8 * sqrt(5))))), 1/(1 + sqrt(5)), 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[sqrt(0.1 * (5 - sqrt(5))),0, 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-sqrt(0.1 * (5 - sqrt(5))), 0, -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-0.5 *sqrt(1 - (2/sqrt(5))), -0.5, -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
		            [-0.5 *sqrt(1 - (2/sqrt(5))), 0.5, -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
		            [0.5 *sqrt(1 - (2/sqrt(5))), -0.5, 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
		            [0.5 *sqrt(1 - (2/sqrt(5))), 0.5, 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((13, 3))

	for i in range(13):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-0.5, 0.5)
	ax.set_ylim(-0.5, 0.5)
	ax.set_zlim(-0.5, 0.5)

	# Side Configuration for Cube
	verts_grico = [[Z[1], Z[7], Z[5]],
				  [Z[6], Z[7], Z[1]],
				  [Z[1], Z[5], Z[12]],
				  [Z[11], Z[6], Z[1]],
				  [Z[12], Z[11], Z[1]],
				  [Z[2], Z[8], Z[3]],
				  [Z[4], Z[8], Z[2]],
				  [Z[2], Z[3], Z[10]],
				  [Z[9], Z[4], Z[2]],
				  [Z[10], Z[9], Z[2]],
				  [Z[12], Z[3], Z[8]],
				  [Z[8], Z[4], Z[11]],
				  [Z[8], Z[11], Z[12]],
				  [Z[10], Z[5], Z[7]],
				  [Z[7], Z[6], Z[9]],
				  [Z[7], Z[9], Z[10]],
				  [Z[3], Z[5], Z[10]],
				  [Z[12], Z[5], Z[3]],
				  [Z[9], Z[6], Z[4]],
				  [Z[4], Z[6], Z[11]]
				  ]
	# Cube Properties

	grico = Poly3DCollection(verts_grico)

	grico.set_edgecolor(edge_c)
	grico.set_linewidth(edge_w)
	grico.set_alpha(alpha)
	grico.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(grico)
