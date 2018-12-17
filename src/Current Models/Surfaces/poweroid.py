# A Family of Poweriods, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Poweroid"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, power, figcolor, rotation, rotmagt, rotmagp, save):

	# Definition of x

	# Value of the angles
	a = power
	x = linspace(-10, 10, sides + 1)
	y = linspace(-10, 10, edges)

	x, y = meshgrid(x, y)


	z = a * ((sqrt(x**2 + y**2))/a)**a

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

	# Axis Properties
	plt.axis(grid) # Turns off the axis grid

	# Surface Plot
	poweriod = ax.plot_surface(x, y, -z)

	poweriod.set_alpha(alpha) # Transparency of figure
	poweriod.set_edgecolor(edge_c) # Edge color of the lines on the figure
	poweriod.set_linewidth(edge_w) # Line width of the edges
	poweriod.set_facecolor(color) # General color of the figure
