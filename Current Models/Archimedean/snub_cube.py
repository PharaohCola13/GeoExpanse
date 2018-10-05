# A Snub cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Snub Cube"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, color3):


	C0 = sqrt(3 * (4 - cbrt(17  + 3 * sqrt(33)) - cbrt(17  - 3 * sqrt(33)))) / 6
	C1 = sqrt(3 * (2 + cbrt(17  + 3 * sqrt(33)) + cbrt(17  - 3 * sqrt(33)))) / 6
	C2 = sqrt(3 * (4 + cbrt(199 + 3 * sqrt(33)) + cbrt(199 - 3 * sqrt(33)))) / 6

	points = array([[C1,   C0,  C2], #0
		            [C1,  -C0, -C2], #1
		            [-C1, -C0,  C2], #2
		            [-C1,  C0, -C2], #3
		            [C2,   C1,  C0], #4
		            [C2,  -C1, -C0], #5
		            [-C2, -C1,  C0], #6
		            [-C2,  C1, -C0], #7
		            [C0,   C2,  C1], #8
		            [C0,  -C2, -C1], #9
		            [-C0, -C2,  C1], #10
		            [-C0,  C2, -C1], #11
		            [C0,  -C1,  C2], #12
		            [C0,   C1, -C2], #13
		            [-C0,  C1,  C2], #14
		            [-C0, -C1, -C2], #15
		            [C2,  -C0,  C1], #16
		            [C2,   C0, -C1], #17
		            [-C2,  C0,  C1], #18
		            [-C2, -C0, -C1], #19
		            [C1,  -C2,  C0], #20
		            [C1,   C2, -C0], #21
		            [-C1,  C2,  C0], #22
		            [-C1, -C2, -C0], #23
		            ])
	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((24, 3))

	for i in range(24):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	# Interval
	r = [-1, 1]

	X, Y = np.meshgrid(r, r)

	# Side Configuration for scube
	verts_scube = [ [Z[2],Z[12],Z[0],Z[14]],
		            [Z[3],Z[13],Z[1],Z[15]],
		            [Z[4],Z[16],Z[5],Z[17]],
		            [Z[7],Z[19],Z[6],Z[18]],
		            [Z[8],Z[21],Z[11],Z[22]],
		            [Z[9],Z[20],Z[10],Z[23]],
					]
	verts_tri =   [
		            [Z[0],  Z[8],  Z[14]],
		            [Z[1],  Z[9],  Z[15]],
		            [Z[2],  Z[10], Z[12]],
		            [Z[3],  Z[11], Z[13]],
		            [Z[4],  Z[0],  Z[16]],
		            [Z[5],  Z[1],  Z[17]],
		            [Z[6],  Z[2],  Z[18]],
		            [Z[7],  Z[3],  Z[19]],
		            [Z[8],  Z[4],  Z[21]],
		            [Z[9],  Z[5],  Z[20]],
		            [Z[10], Z[6],  Z[23]],
		            [Z[11], Z[7],  Z[22]],
		            [Z[12], Z[16], Z[0]],
		            [Z[13], Z[17], Z[1]],
		            [Z[14], Z[18], Z[2]],
		            [Z[15], Z[19], Z[3]],
		            [Z[16], Z[20], Z[5]],
		            [Z[17], Z[21], Z[4]],
		            [Z[18], Z[22], Z[7]],
		            [Z[19], Z[23], Z[6]],
		            [Z[20], Z[12], Z[10]],
		            [Z[21], Z[13], Z[11]],
		            [Z[22], Z[14], Z[8]],
		            [Z[23], Z[15], Z[9]],
		            [Z[8],  Z[0],  Z[4]],
		            [Z[9],  Z[1],  Z[5]],
		            [Z[10], Z[2],  Z[6]],
		            [Z[11], Z[3],  Z[7]],
		            [Z[12], Z[20], Z[16]],
		            [Z[13], Z[21], Z[17]],
		            [Z[14], Z[22], Z[18]],
		            [Z[15], Z[23], Z[19]],
		           ]

	scube = Poly3DCollection(verts_scube)

	scube.set_edgecolor(edge_c)
	scube.set_linewidth(edge_w)
	scube.set_alpha(alpha)
	scube.set_facecolor(color)

	scube1 = Poly3DCollection(verts_tri)

	scube1.set_edgecolor(edge_c)
	scube1.set_linewidth(edge_w)
	scube1.set_alpha(alpha)
	scube1.set_facecolor(color2)

	ax.add_collection3d(scube)
	ax.add_collection3d(scube1)
