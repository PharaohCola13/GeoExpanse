# A Curve, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Spiral"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
	def x_(u,v):
		x = u * cos(u) * (4 + cos(v + u))
		return x

	def y_(u,v):
		y = u * sin(u) * (4 + cos(v + u))
		return y

	def z_(u,v):
		z = 0.25 * (u * sin(v + u))
		return z

	u = linspace(0, 4 * pi, 25)
	v = linspace(0, 2 * pi, 25)

	u, v = np.meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	plt.axis('equal')

	#ax.set_xlim(-1,1)
	#ax.set_ylim(-1,1)
	ax.set_zlim(-10,10)

	# Surface Plot
	curve = ax.plot_surface(x, y, z)

	curve.set_alpha(alpha)
	curve.set_edgecolor(edge_c)
	curve.set_linewidth(edge_w)
	curve.set_facecolor(color)
	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		# Animate
		ani = FuncAnimation(fig, animate,
							interval=1, save_count=50)  # frames=100)#, repeat=True)

		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass

