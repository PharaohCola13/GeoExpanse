# A Truncated Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform


name = "Truncated Cuboctahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, color3, figcolor, rotation, rotmagt, rotmagp, save):

	C0 = (1 + sqrt(2))/2
	C1 = (1 + 2 * sqrt(2)) / 2

	points = array([
					[  C0,  0.5,   C1],
					[  C0,  0.5,  -C1],
					[  C0, -0.5,   C1],
					[  C0, -0.5,  -C1],
					[ -C0,  0.5,   C1],
					[ -C0,  0.5,  -C1],
					[ -C0, -0.5,   C1],
					[ -C0, -0.5,  -C1],
					[  C1,   C0,  0.5],
					[  C1,   C0, -0.5],
					[  C1,  -C0,  0.5],
					[  C1,  -C0, -0.5],
					[ -C1,   C0,  0.5],
					[ -C1,   C0, -0.5],
					[ -C1,  -C0,  0.5],
					[ -C1,  -C0, -0.5],
					[ 0.5,   C1,   C0],
					[ 0.5,   C1,  -C0],
					[ 0.5,  -C1,   C0],
					[ 0.5,  -C1,  -C0],
					[-0.5,   C1,   C0],
					[-0.5,   C1,  -C0],
					[-0.5,  -C1,   C0],
					[-0.5,  -C1,  -C0],
					[ 0.5,   C0,   C1],
					[ 0.5,   C0,  -C1],
					[ 0.5,  -C0,   C1],
					[ 0.5,  -C0,  -C1],
					[-0.5,   C0,   C1],
					[-0.5,   C0,  -C1],
					[-0.5,  -C0,   C1],
					[-0.5,  -C0,  -C1],
					[  C1,  0.5,   C0],
					[  C1,  0.5,  -C0],
					[  C1, -0.5,   C0],
					[  C1, -0.5,  -C0],
					[ -C1,  0.5,   C0],
					[ -C1,  0.5,  -C0],
					[ -C1, -0.5,   C0],
					[ -C1, -0.5,  -C0],
					[  C0,   C1,  0.5],
					[  C0,   C1, -0.5],
					[  C0,  -C1,  0.5],
					[  C0,  -C1, -0.5],
					[ -C0,   C1,  0.5],
					[ -C0,   C1, -0.5],
					[ -C0,  -C1,  0.5],
					[-C0,  -C1, -0.5],
	])

	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]
		 ]
	Z = zeros((48,3))

	for i in range(48):
		Z[i, :] = dot(points[i, :], P)


	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-2, 2)
	ax.set_ylim(-2, 2)
	ax.set_zlim(-2, 2)

	verts = [
			[Z[ 0], Z[24], Z[28], Z[ 4], Z[ 6], Z[30], Z[26], Z[ 2]],
			[Z[ 1], Z[ 3], Z[27], Z[31], Z[ 7], Z[ 5], Z[29], Z[25]],
			[Z[ 8], Z[32], Z[34], Z[10], Z[11], Z[35], Z[33], Z[ 9]],
			[Z[12], Z[13], Z[37], Z[39], Z[15], Z[14], Z[38], Z[36]],
			[Z[16], Z[40], Z[41], Z[17], Z[21], Z[45], Z[44], Z[20]],
			[Z[18], Z[22], Z[46], Z[47], Z[23], Z[19], Z[43], Z[42]],
			[Z[ 0], Z[32], Z[ 8], Z[40], Z[16], Z[24]],
			[Z[ 1], Z[25], Z[17], Z[41], Z[ 9], Z[33]],
			[Z[ 2], Z[26], Z[18], Z[42], Z[10], Z[34]],
			[Z[ 3], Z[35], Z[11], Z[43], Z[19], Z[27]],
			[Z[ 4], Z[28], Z[20], Z[44], Z[12], Z[36]],
			[Z[ 5], Z[37], Z[13], Z[45], Z[21], Z[29]],
			[Z[ 6], Z[38], Z[14], Z[46], Z[22], Z[30]],
			[Z[ 7], Z[31], Z[23], Z[47], Z[15], Z[39]],
			[Z[ 0], Z[ 2], Z[34], Z[32]],
			[Z[ 1], Z[33], Z[35], Z[ 3]],
			[Z[ 4], Z[36], Z[38], Z[ 6]],
			[Z[ 5], Z[ 7], Z[39], Z[37]],
			[Z[ 8], Z[ 9], Z[41], Z[40]],
			[Z[10], Z[42], Z[43], Z[11]],
			[Z[12], Z[44], Z[45], Z[13]],
			[Z[14], Z[15], Z[47], Z[46]],
			[Z[16], Z[20], Z[28], Z[24]],
			[Z[17], Z[25], Z[29], Z[21]],
			[Z[18], Z[26], Z[30], Z[22]],
			[Z[19], Z[23], Z[31], Z[27]],
	]

	fc = []

	for i in range(len(verts)):
		if i in range(0,6):
			fc.append(color)
		elif i in range(6,14):
			fc.append(color2)
		else:
			fc.append(color3)

	sdode = Poly3DCollection(verts)

	sdode.set_edgecolor(edge_c)
	sdode.set_linewidth(edge_w)
	sdode.set_alpha(alpha)
	sdode.set_facecolor(fc)

	ax.add_collection3d(sdode)

	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		if save == "MP4":
			# Animate
			ani = FuncAnimation(fig, animate, frames=500,
								interval=100, save_count=50)  # frames=100)#, repeat=True)

			Writer = writers['ffmpeg']
			writer = Writer(fps=30, bitrate=1800)
			ani.save('{}.mp4'.format(name), writer=writer)
		else:
			#save = None
			# Animate
			ani = FuncAnimation(fig, animate,
								interval=1, save_count=50)  # frames=100)#, repeat=True)
			pass


		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass