import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *


name = "Line"

def shape(fig, edge_c, edge_w, grid, slope, a, b, figcolor):
	plt.clf()
	def x_(y, slope):
		x = slope*y
		return x

	y = linspace(a, b, 100)

	x = x_(y, slope)

	ax = plt.subplot(111)
	ax.patch.set_facecolor(figcolor)
	ax.set_facecolor(figcolor) # Figure background turns black
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)
	plt.axis('equal')



	line = plt.plot(x,y,  color=edge_c, linewidth=edge_w)