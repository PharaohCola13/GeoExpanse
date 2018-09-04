# A Dodecahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *


option = input('Run? (0) Yes, (1) No\n>> ')

while option == 0:

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

	Z = zeros((20,3))


	for i in range(20):
		Z[i,:] = dot(points[i,:],P)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black
	
# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-4, 4)
	ax.set_ylim(-4, 4)
	ax.set_zlim(-4, 4)

# Radius
	radius = input('What is the radius?\n>> ')
	r = radius
	r = [-1 * r,r]

# Definition of x and y
	X, Y = np.meshgrid(r, r)

# The edges of the object
	verts = [
			[Z[0],  Z[1],  Z[2],  Z[3],  Z[4]], 
	        [Z[0],  Z[5],  Z[10], Z[6],  Z[1]],
	        [Z[1],  Z[6],  Z[11], Z[7],  Z[2]],
	        [Z[2],  Z[7],  Z[12], Z[8],  Z[3]],
	        [Z[3],  Z[8],  Z[13], Z[9],  Z[4]],
	      	[Z[4],  Z[9],  Z[14], Z[5],  Z[0]],
	      	[Z[15], Z[10], Z[5],  Z[14], Z[19]],
	      	[Z[16], Z[11], Z[6],  Z[10], Z[15]],
	      	[Z[17], Z[12], Z[7],  Z[11], Z[16]],
	      	[Z[18], Z[13], Z[8],  Z[12], Z[17]],
	      	[Z[19], Z[14], Z[9],  Z[13], Z[18]],
	      	[Z[19], Z[18], Z[17], Z[16], Z[15]]
		    ]

# Surface plot
	dodeca = Poly3DCollection(verts)

	dodeca.set_edgecolor('aqua')
	dodeca.set_linewidth(2)
	dodeca.set_alpha(0.1)
	dodeca.set_facecolor('skyblue')

	dodecahedron = ax.add_collection3d(dodeca)


# Defintions for animations
	def init():
	    return dodecahedron,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=0, azim= 4 * i)
	    return dodecahedron,

# Smooth-ish transition @ elev=90+i, azim=4 * 1, .., frames=550

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
	                   frames=550, interval=2, blit=False, repeat=True)

#Saving to Dodecahedron.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# ani.save('Dodecahedron.mp4', writer=writer)

	plt.show() # Shows Figure
	option = input('Run again? (0) Yes, (1) No\n>> ')
