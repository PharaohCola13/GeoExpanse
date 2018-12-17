# A Truncated Icosahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform


name = "Truncated Icosahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()


	C0 =  (1 + sqrt(5)) / 4
	C1 =  (1 + sqrt(5)) / 2
	C2 =  (5 + sqrt(5)) / 4
	C3 =  (2 + sqrt(5)) / 2
	C4 = 3 * (1 + sqrt(5)) / 4

	points = array([
					[ 0.5,  0.0,   C4],
					[ 0.5,  0.0,  -C4],
					[-0.5,  0.0,   C4],
					[-0.5,  0.0,  -C4],
					[  C4,  0.5,  0.0],
					[  C4, -0.5,  0.0],
					[ -C4,  0.5,  0.0],
					[ -C4, -0.5,  0.0],
					[ 0.0,   C4,  0.5],
					[ 0.0,   C4, -0.5],
					[ 0.0,  -C4,  0.5],
					[ 0.0,  -C4, -0.5],
					[ 1.0,   C0,   C3],
					[ 1.0,   C0,  -C3],
					[ 1.0,  -C0,   C3],
					[ 1.0,  -C0,  -C3],
					[-1.0,   C0,   C3],
					[-1.0,   C0,  -C3],
					[-1.0,  -C0,   C3],
					[-1.0,  -C0,  -C3],
					[  C3,  1.0,   C0],
					[  C3,  1.0,  -C0],
					[  C3, -1.0,   C0],
					[  C3, -1.0,  -C0],
					[ -C3,  1.0,   C0],
					[ -C3,  1.0,  -C0],
					[ -C3, -1.0,   C0],
					[ -C3, -1.0,  -C0],
					[  C0,   C3,  1.0],
					[  C0,   C3, -1.0],
					[  C0,  -C3,  1.0],
					[  C0,  -C3, -1.0],
					[ -C0,   C3,  1.0],
					[ -C0,   C3, -1.0],
					[ -C0,  -C3,  1.0],
					[ -C0,  -C3, -1.0],
					[ 0.5,   C1,   C2],
					[ 0.5,   C1,  -C2],
					[ 0.5,  -C1,   C2],
					[ 0.5,  -C1,  -C2],
					[-0.5,   C1,   C2],
					[-0.5,   C1,  -C2],
					[-0.5,  -C1,   C2],
					[-0.5,  -C1,  -C2],
					[  C2,  0.5,   C1],
					[  C2,  0.5,  -C1],
					[  C2, -0.5,   C1],
					[  C2, -0.5,  -C1],
					[ -C2,  0.5,   C1],
					[ -C2,  0.5,  -C1],
					[ -C2, -0.5,   C1],
					[ -C2, -0.5,  -C1],
					[  C1,   C2,  0.5],
					[  C1,   C2, -0.5],
					[  C1,  -C2,  0.5],
					[  C1,  -C2, -0.5],
					[ -C1,   C2,  0.5],
					[ -C1,   C2, -0.5],
					[ -C1,  -C2,  0.5],
					[ -C1,  -C2, -0.5],
	])

	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]
		 ]
	Z = zeros((60,3))

	for i in range(60):
		Z[i,:] = dot(points[i,:], P)


	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-2, 2)
	ax.set_ylim(-2, 2)
	ax.set_zlim(-2, 2)

	verts = [
			[Z[0], Z[ 2], Z[18], Z[42], Z[38], Z[14]],
			[Z[1], Z[ 3], Z[17], Z[41], Z[37], Z[13]],
			[Z[2], Z[ 0], Z[12], Z[36], Z[40], Z[16]],
			[Z[3], Z[ 1], Z[15], Z[39], Z[43], Z[19]],
			[Z[4], Z[ 5], Z[23], Z[47], Z[45], Z[21]],
			[Z[5], Z[ 4], Z[20], Z[44], Z[46], Z[22]],
			[Z[6], Z[ 7], Z[26], Z[50], Z[48], Z[24]],
			[Z[7], Z[ 6], Z[25], Z[49], Z[51], Z[27]],
			[Z[8], Z[ 9], Z[33], Z[57], Z[56], Z[32]],
			[Z[9], Z[ 8], Z[28], Z[52], Z[53], Z[29]],
			[Z[10], Z[11], Z[31], Z[55], Z[54], Z[30]],
			[Z[11], Z[10], Z[34], Z[58], Z[59], Z[35]],
			[Z[12], Z[44], Z[20], Z[52], Z[28], Z[36]],
			[Z[13], Z[37], Z[29], Z[53], Z[21], Z[45]],
			[Z[14], Z[38], Z[30], Z[54], Z[22], Z[46]],
			[Z[15], Z[47], Z[23], Z[55], Z[31], Z[39]],
			[Z[16], Z[40], Z[32], Z[56], Z[24], Z[48]],
			[Z[17], Z[49], Z[25], Z[57], Z[33], Z[41]],
			[Z[18], Z[50], Z[26], Z[58], Z[34], Z[42]],
			[Z[19], Z[43], Z[35], Z[59], Z[27], Z[51]],
			[Z[0], Z[14], Z[46], Z[44], Z[12]],
			[Z[1], Z[13], Z[45], Z[47], Z[15]],
			[Z[2], Z[16], Z[48], Z[50], Z[18]],
			[Z[3], Z[19], Z[51], Z[49], Z[17]],
			[Z[4], Z[21], Z[53], Z[52], Z[20]],
			[Z[5], Z[22], Z[54], Z[55], Z[23]],
			[Z[6], Z[24], Z[56], Z[57], Z[25]],
			[Z[7], Z[27], Z[59], Z[58], Z[26]],
			[Z[8], Z[32], Z[40], Z[36], Z[28]],
			[Z[9], Z[29], Z[37], Z[41], Z[33]],
			[Z[10], Z[30], Z[38], Z[42], Z[34]],
			[Z[11], Z[35], Z[43], Z[39], Z[31]],
	]

	fc = [color if i in range(0,20) else color2 for i in range(len(verts))]

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
			# save = None
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