# A Icosahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *


option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:

# Points on the object
	p = (1 + sqrt(5))/2
	points = array([
					[p**2, 0, p**3], 	#2		#0 
					[-p**2, 0, p**3],	#6		#1 
					[0, p**3,  p**2],	#12		#2 
					[0, -p**3, p**2], 	#17		#3 
					[p**3, p**2, 0], 	# 27	#4 #
					[-p**3, p**2, 0], 	# 31	#5
					[-p**3, -p**2, 0], 	# 33	#6
					[p**3, -p**2, 0], 	# 37	#7
					[0, p**3, -p**2],	# 46	#8 
					[0, -p**3, -p**2], 	# 51	#9 
					[p**2, 0, -p**3], 	# 54	#10 
					[-p**2, 0, -p**3], 	#58		#11 
])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
		]

	I = zeros((12,3))

	for i in range(12):
		I[i,:] = dot(points[i,:],P)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black
	
# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-5, 5)
	ax.set_ylim(-5, 5)
	ax.set_zlim(-5, 5)

# Radius
	r = [-1 ,1]

# Definition of x and y
	X, Y = np.meshgrid(r, r)

# The edges of the object
	verts = [
			[I[0], I[1], I[3]],
			[I[0], I[2], I[1]],
			[I[0], I[3], I[7]],
			[I[0], I[7], I[4]],
			[I[0], I[4], I[2]],
			[I[7], I[10], I[4]],
			[I[4], I[10], I[8]],
			[I[4], I[8], I[2]],
			[I[2], I[8], I[5]],
			[I[2], I[5], I[1]],
			[I[1], I[5], I[6]],
			[I[1], I[6], I[3]],
			[I[3], I[6], I[9]],
			[I[7], I[9], I[10]],
			[I[11], I[10], I[9]],
			[I[11], I[8], I[10]],
			[I[11], I[5], I[8]],
			[I[11], I[6], I[5]],
			[I[11],	I[9], I[6]],
			[I[3], I[9], I[7]],
			]

# Surface plot
	icosa = Poly3DCollection(verts)

	icosa.set_edgecolor('white')
	icosa.set_linewidth(1)
	icosa.set_alpha(0.3)
	icosa.set_facecolor('deepskyblue')

	icosahedron = ax.add_collection3d(icosa)


# Defintions for animations
	def init():
	    return icosahedron,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=0, azim= 4 * i)
	    return icosahedron,

# Smooth-ish transition @ elev=90+i, azim=4 * 1, .., frames=550

# Animate
	#ani = FuncAnimation(fig, animate, init_func=init,
	#                   frames=550, interval=2, blit=False, repeat=True)

#Saving to Icosahedron.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# ani.save('Icosahedron.mp4', writer=writer)

	plt.show() # Shows Figure
	option = int(input('Run again? (0) Yes, (1) No\n>> '))
