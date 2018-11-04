# A Family of Pyramids, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Pyramid"

def shape(fig, alpha, color, edge_c, edge_w, grid,
		  sides, edges, multi_pi, radiusm, height, figcolor,rotation, rotmagt, rotmagp):
	plt.clf()
# Definition of x
	def x_(u,v):
	    x = ((h - u) / h) * r * cos(v)
	    return x

# Definition of y
	def y_(u,v):
	    y = ((h - u)/h) * r * sin(v)
	    return y

# Definition of z
	def z_(u,v):
	    z = u
	    return z

# Height
	h = height

# Radius
	r = radiusm

# Number of edges on the base
	s = sides

# Value of the angles
	u = linspace(0, h, edges)
	v = linspace(0, 2 * pi,s + 1)

	u, v = meshgrid(u, v)

# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

# Figure Properties

	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1 * r,r)
	ax.set_ylim(-1 * r,r)
	ax.set_zlim(0,h)

# Surface Plot
	pyramid = ax.plot_surface(x,y,z)

	pyramid.set_alpha(alpha) # Transparency of figure
	pyramid.set_edgecolor(edge_c) # Edge color of the lines on the figure
	pyramid.set_linewidth(edge_w) # Line width of the edges
	pyramid.set_facecolor(color) # General color of the figure


	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		# Animate
		ani = FuncAnimation(fig, animate,
							interval=1, save_count=50)

		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass