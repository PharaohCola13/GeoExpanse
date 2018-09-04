# A Klein Bottle, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

option = input('Run? (0) Yes, (1) No\n>> ')

while option == 0:
# Definition of x
	def x_(u, v):
    		x = -2 + 2 * cos(v) - cos(u)
    		x[v < 3 * pi] = -2 + (2 + cos(u[v < 3 * pi])) * cos(v[v < 3 * pi])
    		x[v < 2 * pi] = cos(u[v < 2 * pi]) * (2.5 - 1.5 * cos(v[v < 2 * pi]))
    		return x

# Definition of y
	def y_(u, v):
    		y = sin(u)
    		y[v < 2 * pi] = sin(u[v < 2 * pi]) * (2.5 - 1.5 * cos(v[v < 2 * pi]))
	    	return y
	
# Definition of z
	def z_(u, v):
    		z = -3 * v + 12 * pi
    		z[v < 3 * pi] = (2 + cos(u[v < 3 * pi])) * sin(v[v < 3 * pi]) + 3 * pi
    		z[v < 2 * pi] = 3 * v[v < 2 * pi] - 3 * pi
    		z[v < pi] = -2.5 * sin(v[v < pi])
	    	return z

# Values of the angles
	u = linspace(0, 2 * pi, 10)
	v = linspace(0, 4 * pi, 38)

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
	ax.set_xlim(-5, 5)
	ax.set_ylim(-5, 5)
	ax.set_zlim(0,10)

# Surface Plot
	klein_bottle = ax.plot_surface(x, y, z)

	klein_bottle.set_alpha(1) # Transparency of figure
	klein_bottle.set_edgecolor('w') # Edge color of the lines on the figure
	klein_bottle.set_linewidth(1) # Line width of the edges
	klein_bottle.set_facecolor('deepskyblue') # General color of the figure


# Definitions for animations

	def init():
    		return klein_bottle,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    	ax.view_init(elev=0, azim=i*10)
	    	return klein_bottle,

# Smooth tranisition azim=i*10, frames=36, interval=1

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
	                    frames=36, interval=1, blit=False, repeat=True)

# Saving to Klein-Bottle.mp4

	#Writer = writers['ffmpeg']
	#writer = Writer(fps=15, bitrate=1800)

	#ani.save('Klein-Bottle.mp4', writer=writer)

	plt.show() # Shows Figure
	option = input('Run again? (0) Yes, (1) No\n>> ')
