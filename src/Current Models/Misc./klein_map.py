# A Klein Map, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Klein Map"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
	points = array([
[  513,  -513,  2337],
[  513,   513, -2337],
[ -513,   513,  2337],
[ -513,  -513, -2337],
[ 2337,  -513,   513],
[ 2337,   513,  -513],
[-2337,   513,   513],
[-2337,  -513,  -513],
[  513, -2337,   513],
[  513,  2337,  -513],
[ -513,  2337,   513],
[ -513, -2337,  -513],
[ 2337, -2337,  2337],
[ 2337,  2337, -2337],
[-2337,  2337,  2337],
[-2337, -2337, -2337],
[  342,    57,  1539],
[  342,   -57, -1539],
[ -342,   -57,  1539],
[ -342,    57, -1539],
[ 1539,   342,    57],
[ 1539,  -342,   -57],
[-1539,  -342,    57],
[-1539,   342,   -57],
[   57,  1539,   342],
[   57, -1539,  -342],
[  -57, -1539,   342],
[  -57,  1539,  -342],
[  209,   209,   855],
[  209,  -209,  -855],
[ -209,  -209,   855],
[ -209,   209,  -855],
[  855,   209,   209],
[  855,  -209,  -209],
[ -855,  -209,   209],
[ -855,   209,  -209],
[  209,   855,   209],
[  209,  -855,  -209],
[ -209,  -855,   209],
[ -209,   855,  -209],
[  549,   141,   549],
[  549,  -141,  -549],
[ -549,  -141,   549],
[ -549,   141,  -549],
[  549,   549,   141],
[  549,  -549,  -141],
[ -549,  -549,   141],
[ -549,   549,  -141],
[  141,   549,   549],
[  141,  -549,  -549],
[ -141,  -549,   549],
[ -141,   549,  -549],
[  342,  -342,   342],
[  342,   342,  -342],
[ -342,   342,   342],
[ -342,  -342,  -342],
					])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((56, 3))

	for i in range(56):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-3000, 3000)
	ax.set_ylim(-3000, 3000)
	ax.set_zlim(-3000, 3000)

	verts_cuboc = [
[Z[12], Z[16], Z[42], Z[30], Z[11], Z[8], Z[26]],
[Z[12], Z[26], Z[49], Z[37], Z[5],  Z[4], Z[21]],
[Z[12], Z[21], Z[44], Z[32], Z[2],  Z[0], Z[16]],
[Z[13], Z[17], Z[43], Z[31], Z[10], Z[9], Z[27]],
[Z[13], Z[27], Z[48], Z[36], Z[4], Z[ 5], Z[20]],
[Z[13], Z[20], Z[45], Z[33], Z[3], Z[ 1], Z[17]],
[Z[14], Z[18], Z[40], Z[28], Z[9], Z[10], Z[24]],
[Z[14], Z[24], Z[51], Z[39], Z[7], Z[ 6], Z[23]],
[Z[14], Z[23], Z[46], Z[34], Z[0], Z[ 2], Z[18]],
[Z[15], Z[19], Z[41], Z[29], Z[8], Z[11], Z[25]],
[Z[15], Z[25], Z[50], Z[38], Z[6], Z[ 7], Z[22]],
[Z[15], Z[22], Z[47], Z[35], Z[1], Z[ 3], Z[19]],
[Z[52], Z[40], Z[18], Z[ 2], Z[32], Z[33], Z[45]],
[Z[52], Z[45], Z[20], Z[ 5], Z[37], Z[38], Z[50]],
[Z[52], Z[50], Z[25], Z[11], Z[30], Z[28], Z[40]],
[Z[53], Z[41], Z[19], Z[ 3], Z[33], Z[32], Z[44]],
[Z[53], Z[44], Z[21], Z[ 4], Z[36], Z[39], Z[51]],
[Z[53], Z[51], Z[24], Z[10], Z[31], Z[29], Z[41]],
[Z[54], Z[42], Z[16], Z[ 0], Z[34], Z[35], Z[47]],
[Z[54], Z[47], Z[22], Z[ 7], Z[39], Z[36], Z[48]],
[Z[54], Z[48], Z[27], Z[ 9], Z[28], Z[30], Z[42]],
[Z[55], Z[43], Z[17], Z[ 1], Z[35], Z[34], Z[46]],
[Z[55], Z[46], Z[23], Z[ 6], Z[38], Z[37], Z[49]],
[Z[55], Z[49], Z[26], Z[ 8], Z[29], Z[31], Z[43]],
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


