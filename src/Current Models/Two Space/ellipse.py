import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Ellipse"
def shape(fig, edge_c, edge_w, grid, radiusm, radiusa):
	plt.clf()
	def x_(t):
		x = a * cos(t)
		return x

	def y_(t):
		y = b * sin(t)
		return y


	a = radiusm
	b = radiusa

	t = linspace(-pi,pi, 100)

	x = x_(t)
	y = y_(t)

	ax = plt.subplot(111)
	ax.patch.set_facecolor("black")
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)
	plt.axis('equal')

	plt.plot(x, y, color=edge_c, linewidth=edge_w)