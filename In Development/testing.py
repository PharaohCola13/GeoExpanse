# Something, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Testing"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
	def x_(u,v):
		x = cos(u) * sin(v)
		return x

	def y_(u,v):
		y = sin(u) * sin(v)
		return y

	def z_(u,v):
		z = cos(v) + log1p(tan(2+v)**2)
		return z

	u = linspace(0.001, 2 * pi, 25)
	v = linspace(0, 2 * pi, 25)

	u, v = meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black')

	plt.axis(grid)
	plt.axis('equal')

	# Figure Properties
	#ax.set_xlim(-1,1)
	#ax.set_ylim(-1,1)
	#ax.set_zlim(-1,1)

	# Surface Plot

	interest = ax.plot_surface(x, y, z)

	interest.set_alpha(alpha)
	interest.set_edgecolor(edge_c)
	interest.set_linewidth(edge_w)
	interest.set_facecolor(color)

#
# # Definitions for animation
# def init():
#  	return interest,
# #
# def animate(i):
# #     # azimuth angle : 0 deg to 360 deg
# #     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
# #     # azim = i * n --> rotates object around the z axis with a magnitude of n
# #     # For top view elev = 90
# #     # For side view elev = 0
# #
#     ax.view_init(elev=20, azim=i*4)
#     return interest
#
# # Animate
# #ani = FuncAnimation(fig, animate, init_func=init,
# #                  frames=200, interval=50, blit=False, repeat=True)
#
# # Saving to Interesting.mp4
#
# #Writer = writers['ffmpeg']
# #writer = Writer(fps=25, bitrate=1800)
#
# #ani.save('Interesting.mp4', writer=writer)
#
# plt.show()