# Something, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

def shape(fig, alpha, color, edge_c, rot_elev, rot_azim, grid):
	def x_(u,v):
		x = cos(u) * sin(v)
		return x

	def y_(u,v):
		y = sin(u) * sin(v)
		return y

	def z_(u,v):
		z = cos(v) + log1p(tan(2 + v)**2)
		return z

	u = linspace(0.001, 2 * pi, 25)
	v = linspace(0, 2 * pi, 25)

	u, v = meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	#fig = plt.figure(figsize=(8,8))

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	#plt.axis('equal')

	# Surface Plot
	interest = ax.plot_surface(x, y, z)

	interest.set_alpha(alpha)
	interest.set_edgecolor(edge_c)
	interest.set_linewidth(0.5)
	interest.set_facecolor(color)

	#def animate(i):
#     # azimuth angle : 0 deg to 360 deg
#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
#     # azim = i * n --> rotates object around the z axis with a magnitude of n
#     # For top view elev = 90
#     # For side view elev = 0
#
	#	ax.view_init(elev=(rot_elev * i), azim=(rot_azim * i))

	#ani = FuncAnimation(fig, animate,
     #  	 frames=550, interval=2, blit=False, repeat=True)
