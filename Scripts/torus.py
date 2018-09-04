# A Family of Torus, brought to you by PharaohCola13

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
    		x = 2 * ((c + a * cos(u)) * cos(v))
    		return x

# Definition of y
	def y_(u, v):
    		y = 2 * ((c + a * cos(u)) * sin(v))
    		return y

# Definition of z
	def z_(u, v):
    		z = 2 * (a * sin(u))
    		return z

# Radius 
	radius = input('What is the radius?\n>> ')
	c = radius
	
# Radius of the tube
	radius_tube = input('What is the radius of the tube?\n>> ')
	a = radius_tube

# Values of the angles
	n = 100
	u = linspace(0, 2 * pi, n)
	v = linspace(0, 2 * pi, n)

	u, v = meshgrid(u,v)

# Symbolic Representation
	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

# Figure Properties
	fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis('off') # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-5,5)
	ax.set_ylim(-5,5)
	ax.set_zlim(-5,5)

# Surface Plot
	torus = ax.plot_surface(x, y, z,  rstride=5, cstride=5)

	torus.set_alpha(1) # Transparency of figure
	torus.set_edgecolor('w') # Edge color of the lines on the figure
	torus.set_linewidth(1) # Line width of the edges
	torus.set_facecolor('deepskyblue') # General color of the figure

# Defintions for animations	
	def init():
	    return torus,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=50, azim= 4 * i)
	    return torus,


# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
    	               frames=36, interval=1, blit=False, repeat=True)

# Saving to torus.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)
	
	# if c > a:
	#	name = 'Ring-Torus'
	# elif c == a:
	#	name = 'Horn-Torus'
	#elif c < a:
	#	name = 'Spindle-Torus'
	
	# ani.save('%s.mp4' % name, writer=writer)
	
	plt.show() # Shows Figure
	option = input('Run again? (0) Yes, (1) No\n>> ')
