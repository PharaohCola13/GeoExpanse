# A Hyperbolic Cylinder, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Hyperbolic Cylinder"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,edges, multi_pi, radiusm, height):
	# Definition of x
	def x_(u, v):
		x = a * sinh(u)
		return x


	# Definition of y
	def y_(u, v):
		y = b * cosh(u)
		return y


	# Definition of z
	def z_(u, v):
		z = v
		return z

# Magnitude of the x-direction
	a = radiusm
# Magnitude of the y-direction
	b = height

	# Value of the angles
	u = linspace(-pi, pi, sides + 1)
	v = linspace(-pi, pi, edges)

	u, v = meshgrid(u, v)

	# Symbolic representation
	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')  # Figure background turns black

	# Axis Properties
	plt.axis(grid)  # Turns off the axis grid
	plt.axis('equal')

	# Axis Limits
	ax.set_xlim(-50 * a, 50 * a)
	ax.set_ylim(-50 * b, 50 * b)
	ax.set_zlim(-10, 10)

	# Surface Plot
	hyper_cylin = ax.plot_surface(x, y, z)

	hyper_cylin.set_alpha(alpha)  # Transparency of figure
	hyper_cylin.set_edgecolor(edge_c)  # Edge color of the lines on the figure
	hyper_cylin.set_linewidth(edge_w)  # Line width of the edges
	hyper_cylin.set_facecolor(color)  # General color of the figure
