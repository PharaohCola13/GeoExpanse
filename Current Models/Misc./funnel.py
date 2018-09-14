# A Funnel, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Funnel"

def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides):
    # Definition of x
	def x_(u, v):
		x = u * cos(v)
		return x

	# Definition of y
	def y_(u, v):
		y = u * sin(v)
		return y


	# Definition of z
	def z_(u, v):
		z = h * log1p(u)
		return z

	# Determines the total height of the funnel
	h = 1

	# Defines the radius of the hole
	r = 1

	# Value of the angles
	u = linspace(r, pi, 25)
	v = linspace(0, 2 * pi, 25)

	u, v = meshgrid(u, v)

	# Symbolic representation
	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

	# Figure Properties
	fig = plt.figure(figsize=(8, 8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')  # Figure background turns black

	# Axis Properties
	plt.axis(griid)  # Turns off the axis grid
	plt.axis('equal')

	# Axis Limits
	ax.set_xlim(-r - h , r + h)
	ax.set_ylim(-r - h, r + h)
	ax.set_zlim(0, 2 * h)

	# Surface Plot
	funnel = ax.plot_surface(x, y, z)

	funnel.set_alpha(alpha)  # Transparency of figure
	funnel.set_edgecolor(edge_c)  # Edge color of the lines on the figure
	funnel.set_linewidth(edge_w)  # Line width of the edges
	funnel.set_facecolor(color)  # General color of the figure

