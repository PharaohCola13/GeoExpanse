# A Dodecahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Three Dodecahedron"


def shape(fig, alpha, color, edge_c, edge_w, grid, color2, color3, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()

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
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-4,4)
	ax.set_ylim(-4,4)
	ax.set_zlim(-4,4)


	# magenta, thistle | gold, lemonchiffon | deepskyblue, skyblue
	verts = ['verts0', 'verts1', 'verts2']
	for n in Z,M,N:
		for m in range(len(verts)):
			verts[m] = [[n[0], n[1], n[2], n[3], n[4]],
				 [n[0], n[5], n[10], n[6], n[1]],
				 [n[1], n[6], n[11], n[7], n[2]],
				 [n[2], n[7], n[12], n[8], n[3]],
				 [n[3], n[8], n[13], n[9], n[4]],
				 [n[4], n[9], n[14], n[5], n[0]],
				 [n[15], n[10], n[5], n[14], n[19]],
				 [n[16], n[11], n[6], n[10], n[15]],
				 [n[17], n[12], n[7], n[11], n[16]],
				 [n[18], n[13], n[8], n[12], n[17]],
				 [n[19], n[14], n[9], n[13], n[18]],
				 [n[19], n[18], n[17], n[16], n[15]]
				]

			dodeca = Poly3DCollection(verts[m])

			dodeca.set_edgecolor(edge_c)
			dodeca.set_linewidth(edge_w)
			dodeca.set_alpha(alpha)
			dodeca.set_facecolor(color)

			hedron = ax.add_collection3d(dodeca)

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

