# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Cuboctahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
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
	ax.set_facecolor(figcolor)

	plt.axis(grid)
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
	#				]
	#	cuboc_three = [
				  [Z[12], Z[11], Z[9]],
				  [Z[3],  Z[5],  Z[1]],
				  [Z[6],  Z[9],  Z[3]],
				  [Z[5],  Z[11], Z[7]],
				  [Z[8],  Z[10], Z[12]],
				  [Z[1],  Z[4],  Z[2]],
				  [Z[2],  Z[8],  Z[6]],
				  [Z[7],  Z[10], Z[4]]
				  ]

	verts = verts_cuboc	
	cuboc = Poly3DCollection(verts)
	fc = [color if i in range(0,6) else color2 for i in range(len(verts_cuboc))]

	cuboc.set_edgecolor(edge_c)
	cuboc.set_linewidth(edge_w)
	cuboc.set_alpha(alpha)
	cuboc.set_facecolor(fc)

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


