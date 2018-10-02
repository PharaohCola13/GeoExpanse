# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Cube"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):	


	points = array([[0,0,0],
		            [-1, 1/4 * (-3 - sqrt(5)), 1/4 * (-7-3*sqrt(5))],
					[-1, 1/4 * (-3 - sqrt(5)), 1/4 * (7+3*sqrt(5))],
					[-1, 1/4 * (3 + sqrt(5)), 1/4 * (-7-3*sqrt(5))],
					[-1, 1/4 * (3 + sqrt(5)), 1/4 * (7+3*sqrt(5))],
					[-1/2, -1/2, -3/2 - sqrt(5)],
					[-1/2, -1/2, 3/2 + sqrt(5)],
					[-1/2, 1/2, -3/2 - sqrt(5)],
					[-1/2, 1/2, 3/2 + sqrt(5)],
					[-1/2, -3/2 - sqrt(5),-1/2],
					[-1/2, -3/2 - sqrt(5),1/2],
					[-1/2, -1- sqrt(5)/2,-2 - sqrt(5)/2],
					[-1/2, -1 - sqrt(5)/2, 1/2 * (4 + sqrt(5))],
					[-1/2, 3/2 + sqrt(5), -1/2],
					[-1/2, 3/2 + sqrt(5), 1/2],
					[-1/2, 1/2 8 (2 + sqrt(5)), -2 - sqrt(5)/2],
					[-1/2, 1/2 * (2 + sqrt(5)), 1/2 * (4 + sqrt(5))],
					[1/2, -1/2, -3/2 - sqrt(5)],
					[1/2, -1/2, 3/2 + sqrt(5)],
					[1/2, 1/2, -3/2 - sqrt(5)],
					[1/2, 1/2, 3/2 + sqrt(5)],
					[1/2, -3/2- sqrt(5), -1/2],
					[1/2, -3/2 - sqrt(5), 1/2],
					[1/2, -1 - sqrt(5)/2, -2 - sqrt(5)/2],
					[1/2, -1 - sqrt(5)/2, 1/2 * (4 + sqrt(5))],
					[1/2, 3/2 + sqrt(5), -1/2],
					[1/2, 3/2 + sqrt(5), 1/2],
					[1/2, 1/2 * (2 + sqrt(5)), -2 - sqrt(5)/2],
					[1/2, 1/2 * (2 + sqrt(5)), 1/2 * (4 + sqrt(5))],
					[1, 1/4 * (-3 - sqrt(5)), 1/4 * (-7 - (3 * sqrt(5)))],
					[1, 1/4 * (-3 - sqrt(5)), 1/4 * (7 + (3 * sqrt(5))],
					[1, 1/4 * (3 + sqrt(5)), 1/4 * (-7 - (3 * sqrt(5)))],
					[1, 1/4 * (3 + sqrt(5)), 1/4 * (7 + (3 * sqrt(5)))],
					[1/4 * (-7 - (3 * sqrt(5))), -1,  1/4 * (-3 - sqrt(5))],
					[1/4 * (-7 - (3 * sqrt(5))), -1,  1/4 * (3 + sqrt(5))],
					[1/4 * (-7 - (3 * sqrt(5))), 1,  1/4 * (-3 - sqrt(5))],
					[1/4 * (-7 - (3 * sqrt(5))), 1,  1/4 * (3 + sqrt(5))],
					[1/4 * (-5 - (3 * sqrt(5))), 1/4 * (-5 - sqrt(5)), 1/2 * (-1 - sqrt(5))],
					[1/4 * (-5 - (3 * sqrt(5))), 1/4 * (-5 - sqrt(5)), 1/2 * (1 + sqrt(5))],
					[1/4 * (-5 - (3 * sqrt(5))), 1/4 * (5 + sqrt(5)), 1/2 * (-1 - sqrt(5))],
					[1/4 * (-5 - (3 * sqrt(5))), 1/4 * (5 + sqrt(5)), 1/2 * (1 + sqrt(5))],
					[1/4 * (-5 - sqrt(5)), 1/2 * (-1 - sqrt(5)), 1/4 * (-5 - (3 * sqrt(5)))],
					[1/4 * (-5 - sqrt(5)), 1/2 * (-1 - sqrt(5)), 1/4 * (5 + (3 * sqrt(5)))],
					[1/4 * (-5 - sqrt(5)), 1/2 * (1 + sqrt(5)), 1/4 * (-5 - (3 * sqrt(5)))],
					[1/4 * (-5 - sqrt(5)), 1/2 * (1 + sqrt(5)), 1/4 * (5 + (3 * sqrt(5)))],
					[1/4 * (-3 - sqrt(5)), 1/4 * (-7 - (3 * sqrt(5))), -1],
					[1/4 * (-3 - sqrt(5)), 1/4 * (-7 - (3 * sqrt(5))), 1],
					[1/4 * (-3 - sqrt(5)), -3/4 * (1 + sqrt(5)), 1/2 * (-3 - sqrt(5))],
					[1/4 * (-3 - sqrt(5)), -3/4 * (1 + sqrt(5)), 1/2 * (3 + sqrt(5))],
					[1/4 * (-3 - sqrt(5)), 3/4 * (1 + sqrt(5)), 1/2 * (-3 - sqrt(5))],
					[1/4 * (-3 - sqrt(5)), 3/4 * (1 + sqrt(5)), 1/2 * (3 + sqrt(5))],
					[1/4 * (-3 - sqrt(5)), 1/4 * (7 + (3 * sqrt(5))), -1],
					[1/4 * (-3 - sqrt(5)), 1/4 * (7 + (3 * sqrt(5))), 1],	
					[1/2 * (-3 - sqrt(5)), 1/4 * (-3 - sqrt(5)), -3/4 * (1 + sqrt(5))],				
					[1/2 * (-3 - sqrt(5)), 1/4 * (-3 - sqrt(5)), 3/4 * (1 + sqrt(5))],	
					[1/2 * (-3 - sqrt(5)), 1/4 * (3 + sqrt(5)), -3/4 * (1 + sqrt(5))],
					[1/2 * (-3 - sqrt(5)), 1/4 * (3 + sqrt(5)), 3/4 * (1 + sqrt(5))],
					[-3/2 - sqrt(5), -1/2, -1/2],				
					[-3/2 - sqrt(5), -1/2, 1/2],
					[-3/2 - sqrt(5), 1/2, -1/2],
					[-3/2 - sqrt(5), 1/2, 1/2],
					[1/2 * (-1 - sqrt(5)), 1/4 * (-5 - (3 * sqrt(5))), 1/4 * (-5 - sqrt(5))],					
					[1/2 * (-1 - sqrt(5)), 1/4 * (-5 - (3 * sqrt(5))), 1/4 * (5 + sqrt(5))],
					[1/2 * (-1 - sqrt(5)), 1/4 * (5 + (3 * sqrt(5))), 1/4 * (-5 - sqrt(5))],
					[1/2 * (-1 - sqrt(5)), 1/4 * (5 + (3 * sqrt(5))), 1/4 * (5 + sqrt(5))],
					[-2 - sqrt(5)/2, -1/2, -1 - sqrt(5)/2],
					[-2 - sqrt(5)/2, -1/2, 1/2 * (2 + sqrt(5)],
					[-2 - sqrt(5)/2, 1/2, -1 - sqrt(5)/2],
					[-2 - sqrt(5)/2, 1/2, 1/2 * (2 + sqrt(5)],
					[-1 - sqrt(5)/2, -2 - sqrt(5)/2, -1/2],
					[-1 - sqrt(5)/2, -2 - sqrt(5)/2, 1/2],
					[-1 - sqrt(5)/2, 1/2 * (4 + sqrt(5)), -1/2],
					[-1 - sqrt(5)/2, 1/2 * (4 + sqrt(5)), 1/2],
					[-3/4 * (1 + sqrt(5)), 1/2
								
])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((13, 3))

	for i in range(13):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	#fig = plt.figure(figsize=(5, 5))
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


	verts_cube = []

	cube = Poly3DCollection(verts_cube)

	cube.set_edgecolor("white")
	cube.set_linewidth(0.5)
	cube.set_alpha(0.5)
	cube.set_facecolor("blue")

	# Plot Surfaces
	ax.add_collection3d(cube)
