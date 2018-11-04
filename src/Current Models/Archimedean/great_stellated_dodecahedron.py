# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Great Stellated Dodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
	P1 = (3-sqrt(5))/4
	P2 = (sqrt(5)-1)/4

	points = array([
					[0.5,  0, P1],
					[0.5,  0, -P1],
					[-0.5, 0, P1],
					[-0.5, 0, -P1],
					[0,	   P1, 0.5],
					[0,	   P1, -0.5],
					[0,	  -P1, 0.5],
					[0,	  -P1, -0.5],
					[P1,  0.5, 0],
					[-P1, 0.5, 0],
					[P1, -0.5, 0],
					[-P1, -0.5, 0],
					[-P2, -P2, -P2],
					[-P2, -P2, P2],
					[P2, -P2, -P2],
					[P2, -P2, P2],
					[-P2, P2, -P2],
					[-P2, P2, P2],
					[P2,  P2, -P2],
					[P2,  P2, P2],
])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((20, 3))

	for i in range(20):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	verts = [ 
				[Z[0],  Z[2], Z[14],  Z[4], Z[12]],
				[Z[0],  Z[12], Z[8],  Z[10], Z[16]],
				[Z[0],  Z[16], Z[6],  Z[18], Z[2]],
				[Z[7],  Z[6],  Z[16], Z[18], Z[2]],
				[Z[7],  Z[17], Z[1],  Z[3], Z[19]],
				[Z[9],  Z[11], Z[19], Z[3], Z[15]],
				[Z[9],  Z[15], Z[5],  Z[4], Z[14]],
				[Z[9],  Z[14], Z[2],  Z[18], Z[11]],
				[Z[13], Z[1],  Z[17], Z[10], Z[8]],
				[Z[13], Z[8],  Z[12], Z[4], Z[5]],
				[Z[13], Z[5],  Z[15], Z[3], Z[1]],
	]



	gsdod = Poly3DCollection(verts)

	gsdod.set_edgecolor(edge_c)
	gsdod.set_linewidth(edge_w)
	gsdod.set_alpha(alpha)
	gsdod.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(gsdod)

	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		# Animate
		ani = FuncAnimation(fig, animate,
							interval=1, save_count=50)  # frames=100)#, repeat=True)

		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass

