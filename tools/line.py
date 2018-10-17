import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *


name = "Line"

def shape(fig, slope, a, b):

		def x_(y):
			x = 2*y
			return x

		y = linspace(a, b, 100)
		#y = meshgrid(y)

		x = x_(y)
		plt.axis(grid)
		plt.axis('equal')

		line = plt.plot(x,y)
	
		#line.set_edgecolor(edge_c) # Edge color of the lines on the figure
		#line.set_linewidth(edge_w) # Line width of the edges
