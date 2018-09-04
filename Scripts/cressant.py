# A Pair of Cressants, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

option = input('Run? (0) Yes, (1) No\n>> ')

while option == 0:
# Definition of x
	def x_(u,v):
		x = (2 + sin(2 * pi * v) * sin(2 * pi * u)) * sin(3 * pi * v)
		return x

# Definition of y
	def y_(u,v):
		y = sin(2 * pi * v) * cos(2 * pi * u) + 4 * v - 2
		return y

# Definition of z
	def z_(u,v):
		z = (2 + sin(2 * pi * v) * sin(2 * pi * u)) * cos(3 * pi * v)
		return z

# Value of the angles
	u = linspace(0, 1, 50)
	v = linspace(0, 1, 50)

	u, v = np.meshgrid(u, v)

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
	#ax.set_xlim(-1,1)
	#ax.set_ylim(-1,1)
	#ax.set_zlim(-10,10)

# Surface Plot
	cressant = ax.plot_surface(x, y, z)

	cressant.set_alpha(1) # Transparency of figure
	cressant.set_edgecolor('w') # Edge color of the lines on the figure
	cressant.set_linewidth(0.5) # Line width of the edges
	cressant.set_facecolor('deepskyblue') # General color of the figure

# Definitions for animation
	def init():
		return cressant,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

   		ax.view_init(elev=29, azim=90)
		return cressant,

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
                   frames=100, interval=1, blit=False, repeat=True)

# Saving to Cressant.mp4

	#Writer = writers['ffmpeg']
	#writer = Writer(fps=15, bitrate=1800)

	#ani.save('Cressant.mp4', writer=writer)

	plt.show()
	option = input('Run again? (0) Yes, (1) No\n>> ')
