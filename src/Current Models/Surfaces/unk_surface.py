# Something, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Unk Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()

	def x_(u,v):
		x = cos(u) * sin(v)
		return x

	def y_(u,v):
		y = sin(u) * sin(v)
		return y

	def z_(u,v):
		z = cos(v) + log1p(tan(2 + v)**2)
		return z

	u = linspace(0.001, multi_pi * pi, 1 + sides)
	v = linspace(0, 2 * pi, edges)

	u, v = meshgrid(u, v)

	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	#plt.axis('equal')

	# Surface Plot
	interest = ax.plot_surface(x, y, z)

	interest.set_alpha(alpha)
	interest.set_edgecolor(edge_c)
	interest.set_linewidth(edge_w)
	interest.set_facecolor(color)


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

