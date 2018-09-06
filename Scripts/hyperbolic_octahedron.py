# A Hyperbolic Octahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:
# Definition of x
	def x_(u,v):
		x = (cos(u) * cos(v))**3
		return x

# Definition of y
	def y_(u,v):
		y = (sin(u) * cos(v))**3
		return y

# Definition of z
	def z_(u,v):
		z = sin(v)**3
		return z

# Value of the angles
	u = linspace(-pi/2, pi/2, 25)
	v = linspace(-pi, pi, 25)

	u, v = meshgrid(u, v)

# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1,1)
	ax.set_ylim(-1,1)
	ax.set_zlim(-1,1)

# Surface Plot
	hyper_octa = ax.plot_surface(x, y, z)

	hyper_octa.set_alpha(1) # Transparency of figure
	hyper_octa.set_edgecolor('w') # Edge color of the lines on the figure
	hyper_octa.set_linewidth(1) # Line width of the edges
	hyper_octa.set_facecolor('deepskyblue') # General color of the figure

# Definitions for animation
	def init():
		return hyper_octa,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

		ax.view_init(elev=29, azim=i*4)
		return hyper_octa,

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
                   frames=100, interval=20, blit=False, repeat=True)

# Saving to Hyperbolic_Octahedron.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# ani.save('Hyperbolic_Octahedron.mp4', writer=writer)
	
	plt.show() # Shows Figure
	option = int(input('Run again? (0) Yes, (1) No\n>> '))
