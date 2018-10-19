import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *


name = "Polygons"
def shape(fig, edge_c, edge_w, grid, sides, edges, multi_pi):
	
	def r_(u):
		r = 1/(cos((m/n) *arcsin(sin((n/o)*u+p))))
		return r

	n = sides
	m = edges
	o = edge_w
	p = 0.79


	u = linspace(0,2 * pi, multi_pi+1)

	r = r_(u)

	ax = plt.subplot(111, projection='polar')
	#ax.patch.set_facecolor("black")
	#ax.xaxis.set_tick_params(color="white", labelcolor="white")
	#ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)


	delt = plt.plot(u, r, color=edge_c, linewidth=2)
