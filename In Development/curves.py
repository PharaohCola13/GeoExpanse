# A Family of curve, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Curves"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,edges, multi_pi, radius): 

	x = linspace(-1, 1, 50)
	y = linspace(-1, 1, 50)
	Z,Y = meshgrid(x,y)
	X = Z**2 - 4
	print(Y)
	#Y = (X**2/16) + (Z**2/36)
# Figure Properties
	#fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
# Axis Limits

# Surface Plot
	curve = ax.plot_surface(X,Y,Z)

	curve.set_alpha(alpha) # Transparency of figure#
	curve.set_edgecolor(edge_c) # Edge color of the lines on the figure
	curve.set_linewidth(edge_w) # Line width of the edges
	curve.set_facecolor(color) # General color of the figure

	#plt.draw()
	#plt.show()

# Saving to curve.mp4


	# if c > a:
	#	name = 'Ring-curve'
	# elif c == a:
	#	name = 'Horn-curve'
	#elif c < a:
	#	name = 'Spindle-curve'
	
