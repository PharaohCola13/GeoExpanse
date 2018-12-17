# A Icosidodecahedron

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform


name = "Icosidodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()

	C0 = (1 + sqrt(5))/4
	C1 = (3 + sqrt(5))/4
	C2 = (1 + sqrt(5))/2

	points = array([
					[ 0.0,  0.0,   C2],
					[ 0.0,  0.0,  -C2],
					[  C2,  0.0,  0.0],
					[ -C2,  0.0,  0.0],
					[ 0.0,   C2,  0.0],
					[ 0.0,  -C2,  0.0],
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
					[ -C0,  -C1, -0.5],
	])

	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]
		 ]
	Z = zeros((30,3))

	for i in range(30):
		Z[i, :] = dot(points[i, :], P)

	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)


	verts = [
			[Z[0], Z[ 8], Z[16], Z[14], Z[ 6]],
			[Z[0], Z[10], Z[18], Z[20], Z[12]],
			[Z[1], Z[ 7], Z[15], Z[17], Z[ 9]],
			[Z[1], Z[13], Z[21], Z[19], Z[11]],
			[Z[2], Z[15], Z[23], Z[22], Z[14]],
			[Z[2], Z[16], Z[24], Z[25], Z[17]],
			[Z[3], Z[18], Z[26], Z[27], Z[19]],
			[Z[3], Z[21], Z[29], Z[28], Z[20]],
			[Z[4], Z[23], Z[ 7], Z[11], Z[27]],
			[Z[4], Z[26], Z[10], Z[ 6], Z[22]],
			[Z[5], Z[24], Z[ 8], Z[12], Z[28]],
			[Z[5], Z[29], Z[13], Z[ 9], Z[25]],
			[Z[0], Z[ 6], Z[10]],
			[Z[0], Z[12], Z[ 8]],
			[Z[1], Z[ 9], Z[13]],
			[Z[1], Z[11], Z[ 7]],
			[Z[2], Z[14], Z[16]],
			[Z[2], Z[17], Z[15]],
			[Z[3], Z[19], Z[21]],
			[Z[3], Z[20], Z[18]],
			[Z[4], Z[22], Z[23]],
			[Z[4], Z[27], Z[26]],
			[Z[5], Z[25], Z[24]],
			[Z[5], Z[28], Z[29]],
			[Z[6], Z[14], Z[22]],
			[Z[7], Z[23], Z[15]],
			[Z[8], Z[24], Z[16]],
			[Z[9], Z[17], Z[25]],
			[Z[10], Z[26], Z[18]],
			[Z[11], Z[19], Z[27]],
			[Z[12], Z[20], Z[28]],
			[Z[13], Z[29], Z[21]],
	]

	fc = [color if i in range(0, 12) else color2 for i in range(len(verts))]

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
