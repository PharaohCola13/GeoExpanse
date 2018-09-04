# A Cross-Cap, brought to you by PharaohCola13

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
    		x = cos(u) * sin(2 * v)
		return x

# Definition of y
	def y_(u,v):
    		y = sin(u) * sin(2 * v)
    		return y

# Definition of z
	def z_(u,v):
    		z = -1 * (cos(v)**2 - (cos(u)**2 * sin(v)**2))
    		return z


# Values of the angles
	u = linspace(0, 2 * pi, 28)
	v = linspace(0, pi/2, 28)

	u, v = np.meshgrid(u, v)

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
	#ax.set_xlim(-5,5)
	#ax.set_ylim(-5,5)
	#ax.set_zlim(-5,5)

# Surface Plot
	cross_cap = ax.plot_surface(x,y,z, rstride=1, cstride=1)

	cross_cap.set_alpha(1) # Transparency of figure
	cross_cap.set_edgecolor('w') # Edge color of the lines on the figure
	cross_cap.set_linewidth(1) # Line width of the edges
	cross_cap.set_facecolor('deepskyblue') # General color of the figure

# Definitions for animation
	def init():
	    return cross_cap,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=0, azim=i*10)
	    return cross_cap,

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
    	                frames=36, interval=1, blit=False, repeat=True)

# Saving to Cross-Cap.mp4
	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# ani.save('Cross-Cap.mp4', writer=writer)

	plt.show() # Shows Figure
	option = input('Run again? (0) Yes, (1) No\n>> ')
