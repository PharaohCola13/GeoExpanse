# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Small Stellated Dodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor):


	points = array([[0, 	0.5, -((sqrt(5) - 1)/4)],
					[0, 	0.5, ((sqrt(5) - 1)/4)],
					[0, 	-0.5, -((sqrt(5) - 1)/4)],
					[0, 	-0.5, ((sqrt(5) - 1)/4)],
					[0.5, 	-((sqrt(5) - 1)/4), 0],
					[-0.5, 	-((sqrt(5) - 1)/4), 0],
					[0.5, 	((sqrt(5) - 1)/4), 0],
					[-0.5, 	((sqrt(5) - 1)/4), 0],
					[-((sqrt(5) - 1)/4),0, 0.5],
					[-((sqrt(5) - 1)/4),0, -0.5],
					[((sqrt(5) - 1)/4),0, 0.5],
					[((sqrt(5) - 1)/4),0, -0.5],
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
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	verts = [	[Z[0], Z[2],  Z[7],  Z[11], Z[5]],
				   	[Z[0], Z[5],  Z[1],  Z[9],  Z[8]],
					[Z[0], Z[8],  Z[6],  Z[7],  Z[10]],
					[Z[1], Z[3],  Z[6],  Z[8],  Z[4]],
					[Z[1], Z[4],  Z[0],  Z[10], Z[11]],
					[Z[1], Z[11], Z[7],  Z[6],  Z[9]],
					[Z[2], Z[0],  Z[4],  Z[9],  Z[6]],
					[Z[2], Z[6],  Z[3],  Z[11], Z[10]],
					[Z[2], Z[10], Z[5],  Z[4],  Z[8]],
					[Z[3], Z[1],  Z[5],  Z[10], Z[7]],
					[Z[3], Z[7],  Z[2],  Z[8],  Z[9]],
					[Z[3], Z[9],  Z[4],  Z[5],  Z[11]]
				]
	
	ssdod = Poly3DCollection(verts)

	ssdod.set_edgecolor(edge_c)
	ssdod.set_linewidth(edge_w)
	ssdod.set_alpha(alpha)
	ssdod.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(ssdod)
