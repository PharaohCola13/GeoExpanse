# A Gabriel's Horn, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Gabriel's Horn"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, height, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
	# Definition of x
	def x_(u, v):
		x = u
		return x

	# Definition of y
	def y_(u, v):
		y = (a * cos(v)) / u
		return y


	# Definition of z
	def z_(u, v):
		z = (a * sin(v)) /u
		return z

	a = radiusm # changes radius of the entire thing

	h = height

	# Value of the angles
	s = sides
	u = linspace(1, h, edges)
	v = linspace(0, 2 * pi, s + 1)

	u, v = meshgrid(u, v)

	# Symbolic representation
	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)  # Figure background turns black

	# Axis Properties
	plt.axis(grid)  # Turns off the axis grid
	plt.axis('equal')

	# Axis Limits
	ax.set_xlim(-2 * a, 2 * a)
	ax.set_ylim(-2 * a, 2 * a)
	ax.set_zlim(-a, a)

	# Surface Plot
	horn = ax.plot_surface(x, y, z)

	horn.set_alpha(alpha)  # Transparency of figure
	horn.set_edgecolor(edge_c)  # Edge color of the lines on the figure
	horn.set_linewidth(edge_w)  # Line width of the edges
	horn.set_facecolor(color)  # General color of the figure

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

