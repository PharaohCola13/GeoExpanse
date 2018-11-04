# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Tetrahemihexahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
	points = array([[0, 0, sqrt(2)/2],
					[0, 0, -sqrt(2)/2],
					[sqrt(2)/2, 0, 0],
					[-sqrt(2)/2, 0, 0],
					[0, sqrt(2)/2, 0],
					[0, -sqrt(2)/2, 0],
					[0,0,0]

	])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((7, 3))

	for i in range(7):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	verts = [[Z[0], Z[4], Z[3]],
			  [Z[0], Z[2], Z[5]],
			  [Z[1], Z[2], Z[4]],
			  [Z[1], Z[3], Z[5]],

			  [Z[0], Z[6], Z[4]],
			  [Z[0], Z[6], Z[3]],
			  [Z[4], Z[6], Z[3]],

			  [Z[0], Z[6], Z[2]],
			  [Z[0], Z[6], Z[5]],
			  [Z[2], Z[6], Z[5]],

			  [Z[1], Z[6], Z[2]], 
			  [Z[1], Z[6], Z[4]],
			  [Z[2], Z[6], Z[4]],

			  [Z[1], Z[6], Z[3]], 
			  [Z[1], Z[6], Z[5]],
			  [Z[3], Z[6], Z[5]],
			  
	]
	fc = [color if i in range(0,4) else color2 for i in range(len(verts))]
	tetra = Poly3DCollection(verts)

	tetra.set_edgecolor(edge_c)
	tetra.set_linewidth(edge_w)
	tetra.set_alpha(alpha)
	tetra.set_facecolor(fc)


	# Plot Surfaces
	ax.add_collection3d(tetra)

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

