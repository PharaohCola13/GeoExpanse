# A Pair of corksurfs, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Corkscrew Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges):

	# Definition of x
	def x_(u,v):
		x = a * cos(u) * cos(v)
		return x

	# Definition of y
	def y_(u,v):
		y = a * sin(u) * cos(v)
		return y

	# Definition of z
	def z_(u,v):
		z = a * sin(v) + (b * u)
		return z

	a = 2
	b = 2

	# Value of the angles
	u = linspace(0, 2 * pi, sides + 1)
	v = linspace(0, 2 * pi, edges)

	u, v = np.meshgrid(u, v)

	# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

	# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

	# Surface Plot
	corksurf = ax.plot_surface(x, y, z)

	corksurf.set_alpha(alpha) # Transparency of figure
	corksurf.set_edgecolor(edge_c) # Edge color of the lines on the figure
	corksurf.set_linewidth(edge_w) # Line width of the edges
	corksurf.set_facecolor(color) # General color of the figure
