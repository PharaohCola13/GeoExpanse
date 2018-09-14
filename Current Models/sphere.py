# A Sphere, brough to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides):
# Definition of x
	def x_(u,v):
    		x = cos(u) * sin(v)
    		return x

# Definition of y
	def y_(u,v):
    		y = sin(u) * sin(v)
    		return y

# Definition of z
	def z_(u,v):
    		z  = cos(v)
    		return z

# Number of edges on the base
	s = sides

# Values of the angles
	u = linspace(0, pi, s + 1)
	v = linspace(0, 2 * pi, 1000)

	u, v = meshgrid(u, v)

# Symbolic Representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

# Figure Properties

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1,1)
	ax.set_ylim(-1,1)
	ax.set_zlim(-1,1)

# Surface Plot
	sphere = ax.plot_surface(x, y, z)

	sphere.set_alpha(alpha) # Transparency of figure
	sphere.set_edgecolor(edge_c) # Edge color of the lines on the figure
	sphere.set_linewidth(edge_w) # Line width of the edges
	sphere.set_facecolor(color) # General color of the figure
