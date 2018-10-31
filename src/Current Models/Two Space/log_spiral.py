import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *

name = "Log Spiral"
def shape(fig, edge_c, edge_w, grid, radiusm, radiusa):
	plt.clf()
	def r_(u):
		r = a * exp(b * u)
		return r

	a = float(radiusm)
	b = float(radiusa)

	u = linspace(0, 4 * pi,1000)
	r = r_(u)

	ax = plt.subplot(111, projection='polar')

	ax.patch.set_facecolor("black")
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)

	plt.plot(u, r, color=edge_c, linewidth=edge_w)
