import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Parabola"
def shape(fig, edge_c, edge_w, grid, radiusm, figcolor):
	plt.clf()
	def x_(t):
		x = a * t**2
		return x

	def y_(t):
		y = 2 * a * t
		return y


	a = radiusm
	t = linspace(-5,5, 100)
	x = x_(t)
	y = y_(t)

	ax = plt.subplot(111)

	ax.patch.set_facecolor(figcolor)
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)
	plt.axis('equal')

	plt.plot(x, y, color=edge_c, linewidth=edge_w)
