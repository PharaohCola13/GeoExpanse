# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Cuboctahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2):


	points = array([[0,0,0],
					[-1, 0, 0],
					[-0.5, -0.5, -1/sqrt(2)],
					[-0.5, -0.5, 1/sqrt(2)],
					[-0.5, 0.5, -1/sqrt(2)],
					[-0.5, 0.5, 1/sqrt(2)],
					[0, -1, 0],
					[0,1,0],
					[0.5, -0.5, -1/sqrt(2)],
					[0.5, -0.5, 1/sqrt(2)],
					[0.5, 0.5, -1/sqrt(2)],
					[0.5, 0.5, 1/sqrt(2)],
					[1, 0, 0]
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

	plt.axis("on")
	plt.axis('equal')

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	verts_cuboc = [[Z[4], Z[10], Z[8],  Z[2]],
				  [Z[3],  Z[9],  Z[11], Z[5]],
				  [Z[9],  Z[6],  Z[8],  Z[12]],
				  [Z[3],  Z[1],  Z[2],  Z[6]],
				  [Z[5],  Z[7],  Z[4],  Z[1]],
				  [Z[11], Z[12], Z[10], Z[7]],
				]
	cuboc_three = [
				  [Z[12], Z[11], Z[9]],
				  [Z[3],  Z[5],  Z[1]],
				  [Z[6],  Z[9],  Z[3]],
				  [Z[5],  Z[11], Z[7]],
				  [Z[8],  Z[10], Z[12]],
				  [Z[1],  Z[4],  Z[2]],
				  [Z[2],  Z[8],  Z[6]],
				  [Z[7],  Z[10], Z[4]]
				  ]

	cuboc = Poly3DCollection(verts_cuboc)

	cuboc.set_edgecolor(edge_c)
	cuboc.set_linewidth(edge_w)
	cuboc.set_alpha(alpha)
	cuboc.set_facecolor(color)

	cuboc1 = Poly3DCollection(cuboc_three)

	cuboc1.set_edgecolor(edge_c)
	cuboc1.set_linewidth(edge_w)
	cuboc1.set_alpha(alpha)
	cuboc1.set_facecolor(color2)

	# Plot Surfaces
	ax.add_collection3d(cuboc)
	ax.add_collection3d(cuboc1)
