# A Hyperbolic Octahedron, brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Hyperbolic-Octahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi):
	global name
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
	s = sides
	u = linspace(-pi/2, pi/2, s + 1)
	v = linspace(-pi, pi, edges)

	u, v = meshgrid(u, v)

	# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

	# Axis Properties
	plt.axis(grid)
	plt.axis('equal')

	# Axis Limits
	ax.set_xlim(-1,1)
	ax.set_ylim(-1,1)
	ax.set_zlim(-1,1)

	# Surface Plot
	hyper_octa = ax.plot_surface(x, y, z)

	hyper_octa.set_alpha(alpha) # Transparency of figure
	hyper_octa.set_edgecolor(edge_c) # Edge color of the lines on the figure
	hyper_octa.set_linewidth(edge_w) # Line width of the edges
	hyper_octa.set_facecolor(color) # General color of the figure
