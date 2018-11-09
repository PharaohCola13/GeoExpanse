# A Icsohedral Toroid, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Icosohedral Toroid"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
	C0 = (sqrt(2) - 1) / 4
	C1 = sqrt(3) / 2
	C2 = (3 + sqrt(2)) / 4
	C3 = (1 + sqrt(2)) / 2
	C4 = (sqrt(3) + sqrt(6)) / 2
	C5 = 1 + sqrt(2)
	points = array([[1.0, 0.0,  C2],
					[-1.0, 0.0, -C2],
					[-0.5,  C1,  C2],
					[ 0.5,  C1, -C2],
					[-0.5, -C1,  C2],
					[ 0.5, -C1, -C2],
					[C5, 0.0,  C0],
					[-C5, 0.0, -C0],
					[-C3,  C4,  C0],
					[C3,  C4, -C0],
					[-C3, -C4,  C0],
					[C3, -C4, -C0],

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
	plt.axis('equal')

	ax.set_xlim(-2, 2)
	ax.set_ylim(-2, 2)
	ax.set_zlim(-2, 2)

	verts_cuboc = [ 
[Z[0],Z[2],Z[3]],
[Z[0],Z[3],Z[5]],
[Z[0],Z[5],Z[4]],
[Z[0],Z[4],Z[11]],
[Z[0],Z[11],Z[6]],
[Z[0],Z[6],Z[9]],
[Z[0],Z[9],Z[2]],
[Z[1],Z[2],Z[4]],
[Z[1],Z[4],Z[5]],
[Z[1],Z[5],Z[10]],
[Z[1],Z[10],Z[7]],
[Z[1],Z[7],Z[8]],
[Z[1],Z[8],Z[3]],
[Z[1],Z[3],Z[2]],
[Z[2],Z[9],Z[8]],
[Z[2],Z[8],Z[7]],
[Z[2],Z[7],Z[4]],
[Z[3],Z[8],Z[9]],
[Z[3],Z[9],Z[6]],
[Z[3],Z[6],Z[5]],
[Z[4],Z[7],Z[10]],
[Z[4],Z[10],Z[11]],
[Z[5],Z[6],Z[11]],
[Z[5],Z[11],Z[10]],
]

	verts = verts_cuboc	
	cuboc = Poly3DCollection(verts)
	cuboc.set_edgecolor(edge_c)
	cuboc.set_linewidth(edge_w)
	cuboc.set_alpha(alpha)
	cuboc.set_facecolor(color)

	ax.add_collection3d(cuboc)

	#	if grid == "on":
		# Produces the labels and arrows of the Hexagonal Face
		# for j, xyz_ in enumerate(points):
		#    hex = annotate3D(ax,
		# 		       s                    =   (j),
		# 		       xyz                  =   xyz_,
		# 		       fontsize             =   13,
		# 		       xytext               =   (-3,3),
		# 		       textcoords           =   'offset points',
		# 		       horizontalalignment  =   'right',
		# 		       verticalalignment    =   'bottom',
		# 		       arrowprops           =   dict(arrowstyle='<-', connectionstyle="arc3, rad=0.5")
		# 		            )
		# if grid == "off":
		# 	ax.clear()
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


