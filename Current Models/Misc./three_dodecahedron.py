# A Dodecahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Embedded-Dodecahedron"


def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides):

# Points on the object
	points = array([
				[1.21412, 	0, 			1.58931],		#0
				[0.375185, 	1.1547, 	1.58931],		#1
				[-0.982247, 	0.713644, 	1.58931],		#2
				[-0.982247, 	-0.713644, 	1.58931],		#3
				[0.375185, 	-1.1547, 	1.58931],		#4
				[1.96449, 	0, 			0.375185],		#5
				[0.607062, 	1.86835, 	0.375185],		#6
				[-1.58931, 	1.1547, 	0.375185],		#7
				[-1.58931, 	-1.1547, 	0.375185],		#8
				[0.607062, 	-1.86835, 	0.375185],		#9
				[1.58931, 	1.1547, 	-0.375185],		#10
				[-0.607062, 	1.86835, 	-0.375185],		#11
				[-1.96449, 	0, 			-0.375185],		#12
				[-0.607062, 	-1.86835, 	-0.375185],		#13
				[1.58931, 	-1.1547, 	-0.375185],		#14
				[0.982247, 	0.713644, 	-1.58931],		#15
				[-0.375185, 	1.1547, 	-1.58931],		#16
				[-1.21412, 	0, 			-1.58931],		#17
				[-0.375185, 	-1.1547, 	-1.58931],		#18
   			    [0.982247, 	-0.713644, 	-1.58931]		#19
				])

# Scaling Matricies
# 100%
	P = [[1, 0, 0],
    	 [0, 1, 0],
   		 [0, 0, 1]]

# 75%
	Q = [[0.75, 0, 0],
    	 [0, 0.75, 0],
    	 [0, 0, 0.75]]

# 50%
	R = [[0.5, 0, 0],
    	 [0, 0.5, 0],
    	 [0, 0, 0.5]]

	Z = zeros((20,3))

	M = zeros((20,3))

	N = zeros((20,3))


	for i in range(20):
		Z[i,:] = dot(points[i,:],P)

	for i in range(20):
		M[i,:] = dot(points[i,:],Q)

	for i in range(20):
		N[i,:] = dot(points[i,:],R)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-4,4)
	ax.set_ylim(-4,4)
	ax.set_zlim(-4,4)

# Radius
	r = [-1,1]

	X, Y = np.meshgrid(r, r)


# magenta, thistle | gold, lemonchiffon | deepskyblue, skyblue

# Outside Region
	verts = [[Z[0], Z[1], Z[2], Z[3], Z[4]],
         [Z[0], Z[5], Z[10], Z[6], Z[1]],
         [Z[1], Z[6], Z[11], Z[7], Z[2]],
         [Z[2], Z[7], Z[12], Z[8], Z[3]],
         [Z[3], Z[8], Z[13], Z[9], Z[4]],
      	 [Z[4], Z[9], Z[14], Z[5], Z[0]],
      	 [Z[15], Z[10], Z[5], Z[14], Z[19]],
      	 [Z[16], Z[11], Z[6], Z[10], Z[15]],
      	 [Z[17], Z[12], Z[7], Z[11], Z[16]],
      	 [Z[18], Z[13], Z[8], Z[12], Z[17]],
      	 [Z[19], Z[14], Z[9], Z[13], Z[18]],
      	 [Z[19], Z[18], Z[17], Z[16], Z[15]]
		]

	dodeca = Poly3DCollection(verts)

	dodeca.set_edgecolor('aqua')
	dodeca.set_linewidth(2)
	dodeca.set_alpha(0.1)
	dodeca.set_facecolor('skyblue')

	hedron = ax.add_collection3d(dodeca)

# Middle Region
	verts_75 = [[M[0], M[1], M[2], M[3], M[4]],
			 [M[0], M[5], M[10], M[6], M[1]],
			 [M[1], M[6], M[11], M[7], M[2]],
			 [M[2], M[7], M[12], M[8], M[3]],
			 [M[3], M[8], M[13], M[9], M[4]],
			 [M[4], M[9], M[14], M[5], M[0]],
			 [M[15], M[10], M[5], M[14], M[19]],
			 [M[16], M[11], M[6], M[10], M[15]],
			 [M[17], M[12], M[7], M[11], M[16]],
			 [M[18], M[13], M[8], M[12], M[17]],
			 [M[19], M[14], M[9], M[13], M[18]],
			 [M[19], M[18], M[17], M[16], M[15]]
	]

	dodeca_75 = Poly3DCollection(verts_75)

	dodeca_75.set_edgecolor('dodgerblue')
	dodeca_75.set_linewidth(2)
	dodeca_75.set_alpha(0.2)
	dodeca_75.set_facecolor('deepskyblue')

	hedron_75 = ax.add_collection3d(dodeca_75)


	# Inner most Region
	verts_50 = [[N[0], N[1], N[2], N[3], N[4]],
			 [N[0], N[5], N[10], N[6], N[1]],
			 [N[1], N[6], N[11], N[7], N[2]],
			 [N[2], N[7], N[12], N[8], N[3]],
			 [N[3], N[8], N[13], N[9], N[4]],
			 [N[4], N[9], N[14], N[5], N[0]],
			 [N[15], N[10], N[5], N[14], N[19]],
			 [N[16], N[11], N[6], N[10], N[15]],
			 [N[17], N[12], N[7], N[11], N[16]],
			 [N[18], N[13], N[8], N[12], N[17]],
			 [N[19], N[14], N[9], N[13], N[18]],
			 [N[19], N[18], N[17], N[16], N[15]]
	]

	dodeca_50 = Poly3DCollection(verts_50)

	dodeca_50.set_edgecolor('slateblue')
	dodeca_50.set_linewidth(2)
	dodeca_50.set_alpha(0.3)
	dodeca_50.set_facecolor('royalblue')

	hedron_50 = ax.add_collection3d(dodeca_50)
