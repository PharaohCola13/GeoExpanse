# A Pair of hyperhels, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "General"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, x_entry, y_entry, z_entry, figcolor):

	# Value of the angles
	u = linspace(-2 * pi, 2 * pi, sides + 1)
	v = linspace(-2 * pi, 2 * pi, edges)

	u, v = np.meshgrid(u, v)
#	print(x_entry)

	# Symbolic representation
	x = x_entry
	y = y_entry
	z = z_entry

	print(x,y,z)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

	# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

	# Surface Plot
	#hyperhel = ax.plot_surface(x, y, z)

	#hyperhel.set_alpha(alpha) # Transparency of figure
	#hyperhel.set_edgecolor(edge_c) # Edge color of the lines on the figure
	#hyperhel.set_linewidth(edge_w) # Line width of the edges
	#hyperhel.set_facecolor(color) # General color of the figure
