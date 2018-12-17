# A Snub Dodecahedron

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform


name = "Truncated Octahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()


	C0 = sqrt(2)/2
	C1 = sqrt(2)

	points = array([
					[ C0, 0.0,  C1],
					[ C0, 0.0, -C1],
					[-C0, 0.0,  C1],
					[-C0, 0.0, -C1],
					[ C1,  C0, 0.0],
					[ C1, -C0, 0.0],
					[-C1,  C0, 0.0],
					[-C1, -C0, 0.0],
					[0.0,  C1,  C0],
					[0.0,  C1, -C0],
					[0.0, -C1,  C0],
					[0.0, -C1, -C0],
					[0.0,  C0,  C1],
					[0.0,  C0, -C1],
					[0.0, -C0,  C1],
					[0.0, -C0, -C1],
					[ C1, 0.0,  C0],
					[ C1, 0.0, -C0],
					[-C1, 0.0,  C0],
					[-C1, 0.0, -C0],
					[ C0,  C1, 0.0],
					[ C0, -C1, 0.0],
					[-C0,  C1, 0.0],
					[-C0, -C1, 0.0],
	])

	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]
		 ]
	Z = zeros((24,3))

	for i in range(24):
		Z[i, :] = dot(points[i, :], P)

	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)


	verts = [
			[Z[0], Z[14], Z[10], Z[21], Z[5], Z[16]],
			[Z[1], Z[13], Z[9], Z[20], Z[4], Z[17]],
			[Z[2], Z[12], Z[8], Z[22], Z[6], Z[18]],
			[Z[3], Z[15], Z[11], Z[23], Z[7], Z[19]],
			[Z[4], Z[20], Z[8], Z[12], Z[0], Z[16]],
			[Z[5], Z[21], Z[11], Z[15], Z[1], Z[17]],
			[Z[7], Z[23], Z[10], Z[14], Z[2], Z[18]],
			[Z[6], Z[22], Z[9], Z[13], Z[3], Z[19]],
			[Z[0], Z[12], Z[2], Z[14]],
			[Z[1], Z[15], Z[3], Z[13]],
			[Z[4], Z[16], Z[5], Z[17]],
			[Z[6], Z[19], Z[7], Z[18]],
			[Z[8], Z[20], Z[9], Z[22]],
			[Z[10], Z[23], Z[11], Z[21]],
	]

	fc = [color if i in range(0, 8) else color2 for i in range(len(verts))]

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