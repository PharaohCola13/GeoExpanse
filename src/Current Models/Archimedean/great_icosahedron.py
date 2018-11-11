# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Great Icosahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
	points = array([[0,0,0],
					[0, 0, -0.5 * sqrt(0.5 * (5 - sqrt(5)))],
					[0, 0, 0.5 * sqrt(0.5 * (5 - sqrt(5)))],
					[sqrt(((1./8.)+(1/(8 *sqrt(5))))), -1/(1 +sqrt(5)), -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[sqrt(((1./8.) + (1/(8 * sqrt(5))))), 1/(1 + sqrt(5)), -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-sqrt(((1./8.) + (1/(8 * sqrt(5))))), -1/(1 + sqrt(5)), 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-sqrt(((1./8.) + (1/(8 * sqrt(5))))), 1/(1 + sqrt(5)), 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[sqrt(0.1 * (5 - sqrt(5))),0, 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-sqrt(0.1 * (5 - sqrt(5))), 0, -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
					[-0.5 *sqrt(1 - (2/sqrt(5))), -0.5, -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
		            [-0.5 *sqrt(1 - (2/sqrt(5))), 0.5, -0.5 * sqrt(0.1 * (5 - sqrt(5)))],
		            [0.5 *sqrt(1 - (2/sqrt(5))), -0.5, 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
		            [0.5 *sqrt(1 - (2/sqrt(5))), 0.5, 0.5 * sqrt(0.1 * (5 - sqrt(5)))],
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

	ax.set_xlim(-0.5, 0.5)
	ax.set_ylim(-0.5, 0.5)
	ax.set_zlim(-0.5, 0.5)

	# Side Configuration for Cube
	verts_grico = [[Z[1], Z[7], Z[5]],
				  [Z[6], Z[7], Z[1]],
				  [Z[1], Z[5], Z[12]],
				  [Z[11], Z[6], Z[1]],
				  [Z[12], Z[11], Z[1]],
				  [Z[2], Z[8], Z[3]],
				  [Z[4], Z[8], Z[2]],
				  [Z[2], Z[3], Z[10]],
				  [Z[9], Z[4], Z[2]],
				  [Z[10], Z[9], Z[2]],
				  [Z[12], Z[3], Z[8]],
				  [Z[8], Z[4], Z[11]],
				  [Z[8], Z[11], Z[12]],
				  [Z[10], Z[5], Z[7]],
				  [Z[7], Z[6], Z[9]],
				  [Z[7], Z[9], Z[10]],
				  [Z[3], Z[5], Z[10]],
				  [Z[12], Z[5], Z[3]],
				  [Z[9], Z[6], Z[4]],
				  [Z[4], Z[6], Z[11]]
				  ]
	# Cube Properties

	grico = Poly3DCollection(verts_grico)

	grico.set_edgecolor(edge_c)
	grico.set_linewidth(edge_w)
	grico.set_alpha(alpha)
	grico.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(grico)

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


