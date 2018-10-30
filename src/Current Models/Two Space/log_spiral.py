import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Log Spiral"
def shape(fig, edge_c, edge_w, grid, radiusm):
	plt.clf()
	def r_(u):
		r = exp(a *u)
		return r

	a = radiusm
	u = linspace(-5 *pi, pi,1000)
	r = r_(u)

	ax = plt.subplot(111)
	ax.projection='polar'

	ax.patch.set_facecolor("black")
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)
	plt.axis('equal')

	plt.plot(u, r, color=edge_c, linewidth=edge_w)
