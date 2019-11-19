# A Tesseract, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Tesseract"

def shape(fig, alpha, color, edge_c, edge_w, grid, color2, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
# Points on the object
	points = array([
				   [-1,	-1,	-1],
    	           [ 1,	-1, -1],
    	           [ 1,	 1, -1],
    	           [-1,	 1, -1],
    	           [-1, -1,  1],
    	           [ 1,	-1,  1],
    	           [ 1,  1,  1],
    	           [-1,	 1,	 1]
				   ])
 
# Scaling Matricies
# 200%
	P = [
		[2, 0, 0],
		[0, 2, 0],
		[0, 0, 2]
		]

# 100%
	Q = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
		]

	Z = zeros((8,3))
	
	V = zeros((8,3))

	for i in range(8):
		Z[i,:] = dot(points[i,:],P)

	for i in range(8):
		V[i,:] = dot(points[i,:],Q)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-4,4)
	ax.set_ylim(-4,4)
	ax.set_zlim(-4,4)

# Outer Region Configuration
	verts = [
				  [Z[0], V[0], V[1], Z[1]],
				  [Z[1], V[1], V[5], Z[5]], 
				  [Z[0], V[0], V[4], Z[4]], 
				  [Z[4], V[4], V[5], Z[5]], 
				  [Z[5], V[5], V[6], Z[6]],
				  [Z[1], V[1], V[2], Z[2]], 
				  [Z[2], V[2], V[6], Z[6]],
				  [Z[2], V[2], V[3], Z[3]],
				  [Z[6], V[6], V[7], Z[7]],
				  [Z[7], V[7], V[3], Z[3]],
				  [Z[0], V[0], V[3], Z[3]],
				  [Z[4], V[4], V[7], Z[7]],

			 	  [V[0],V[1],V[2],V[3]],
				  [V[4],V[5],V[6],V[7]],
				  [V[0],V[4],V[5],V[1]],
				  [V[1],V[5],V[6],V[2]],
				  [V[2],V[6],V[7],V[3]],
				  [V[3],V[7],V[4],V[0]]
				  ]

# Outside Region
	fc = [color if i in range(0, 12) else color2 for i in range(len(verts))]

	region = Poly3DCollection(verts)

	region.set_edgecolor(edge_c)
	region.set_linewidth(edge_w)
	region.set_alpha(alpha)
	region.set_facecolor(fc)

# Plot Surfaces
	ax.add_collection3d(region)


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

