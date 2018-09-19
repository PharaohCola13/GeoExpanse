# A Klein Bottle, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Klein Bottle"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
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
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-5, 5)
	ax.set_ylim(-5, 5)
	ax.set_zlim(0,10)

# Surface Plot
	klein_bottle = ax.plot_surface(x, y, z)

	klein_bottle.set_alpha(alpha) # Transparency of figure
	klein_bottle.set_edgecolor(edge_c) # Edge color of the lines on the figure
	klein_bottle.set_linewidth(edge_w) # Line width of the edges
	klein_bottle.set_facecolor(color) # General color of the figure
