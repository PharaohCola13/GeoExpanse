# A Hyperbolic Tetrahedron, Brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Hyperbolic Tetrahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid,
		  sides, edges, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()

	def x_(u, v):
		x = ((2 * cos(u) + 2 * cos(u)**2 - 1)  * (1 - v)**2)
		return x


	def y_(u, v):
		y = (2*sin(u) - 2*sin(u)*cos(u)) * (1 - v)**2
		return y


	# Definition of z
	def z_(u, v):
		z = cos(v)**3
		return z

	u = linspace(-pi, pi, sides +1)
	v = linspace(0,1, edges)

	u, v = meshgrid(u, v)

	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	# Axis Limits
	ax.set_zlim(0, 1)
	ax.set_xlim(-2,2)
	ax.set_ylim(-2,2)

	# Surface plot
	hy_tetra = ax.plot_surface(x, y, z)

	hy_tetra.set_linewidth(edge_w)
	hy_tetra.set_edgecolor(edge_c)
	hy_tetra.set_alpha(alpha)
	hy_tetra.set_facecolor(color)
