import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Deltiod"
def shape(fig, edge_c, edge_w, grid, radius):
	def x_(t):
		x = 2 * a *cos(t) *(1 + cos(t)) - a
		return x
	def y_(t):
		y = 2 * a *sin(t) *(1 - cos(t))
		return y

	a = radius
	t = linspace(0, 2 *pi, 100)

	x = x_(t)
	y = y_(t)

	ax = plt.subplot(111)
	ax.patch.set_facecolor("black")
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)
	plt.axis('equal')

	delt = plt.plot(x, y, color=edge_c, linewidth=edge_w)
