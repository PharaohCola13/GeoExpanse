# Something Strange, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Something Strange"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi):
# x: t*s*cos(u) * cos(v)
# y: t*s*cos(u) * sin(v)
# z: t * s * sin(v)

	def x_(u,v):
		x = t*s*cos(u) * cos(v)
		return x

	def y_(u,v):
		y = t * s * cos(u) * sin(v)
		return y

	def z_(u,v):
		z = t * s* sin(v)
		return z

	s = sides
	t = linspace(0, pi, 20)

	u = linspace(0, 2 * pi, 20)
	v = linspace(0, 2 * pi, 20)

	u, v = np.meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	ax.set_xlim(-50,50)
	ax.set_ylim(-50,50)
	ax.set_zlim(-50,50)

	# Surface Plot
	strange = ax.plot_surface(x, y, z)

	strange.set_alpha(alpha)
	strange.set_edgecolor(edge_c)
	strange.set_linewidth(edge_w)
	strange.set_facecolor(color)
