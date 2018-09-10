# A Octohedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *

import argparse
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import * 

name = "Octahedron"

parser = argparse.ArgumentParser()
parser.add_argument("-Y", "--run", help="Runs program", action="store_true")
parser.add_argument("-c", "--color", help="Defines Color", action="store")
parser.add_argument("-a", "--alpha", help="Defines Transparency", action="store", type=float)
parser.add_argument("-r", "--rotate", help="Rotates Figure", action="store_true")
parser.add_argument("-s", "--save", help="Saves Figure as mp4", action="store_true")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


if args.run:

# Points on the object
	points = array([
				   [1, 0, 0],
				   [0, 1, 0],
				   [0, 0, 1],
				   [-1, 0, 0],
				   [0, -1, 0],
				   [0, 0, -1]
				   ])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
	    [0, 1, 0],
	    [0, 0, 1]
		]

	Z = zeros((6,3))


	for i in range(6):
		Z[i,:] = dot(points[i,:],P)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black
	
# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

# Radius
	r = [-1 ,1]

# Definition of x and y
	X, Y = np.meshgrid(r, r)

# The edges of the object
	verts = [
			[Z[0], Z[1], Z[3], Z[4], Z[0]],
			[Z[0], Z[2], Z[1]], 
			[Z[1], Z[2], Z[3]],
			[Z[3], Z[2], Z[4]],
			[Z[4], Z[2], Z[0]],
			[Z[0], Z[5], Z[1]], 
			[Z[1], Z[5], Z[3]],
			[Z[3], Z[5], Z[4]],
			[Z[4], Z[5], Z[0]]	
			]

# Surface plot
	octa = Poly3DCollection(verts)

	octa.set_edgecolor('blue')
	octa.set_linewidth(2)
	octa.set_alpha(0.3)
	octa.set_facecolor('skyblue')

	octahedron = ax.add_collection3d(octa)


# Defintions for animations
	def init():
	    return octahedron,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=0, azim= 4 * i)
	    return octahedron,

# Smooth-ish transition @ elev=90+i, azim=4 * 1, .., frames=550

# Animate
	#ani = FuncAnimation(fig, animate, init_func=init,
	#                   frames=550, interval=2, blit=False, repeat=True)

#Saving to Octahedron.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# ani.save('Octahedron.mp4', writer=writer)

	plt.show() # Shows Figure
