# A Pair of screws, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Steinbach Screw"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()

	# Definition of x
	def x_(u,v):
		x = u * cos(v)
		return x

	# Definition of y
	def y_(u,v):
		y = u * sin(v)
		return y

	# Definition of z
	def z_(u,v):
		z = v * cos(u)
		return z

	# Value of the angles
	u = linspace(-4, 4, sides + 1)
	v = linspace(0, 6.25, edges)

	u, v = np.meshgrid(u, v)

	# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

	# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

	# Surface Plot
	screw = ax.plot_surface(x, y, z)

	screw.set_alpha(alpha) # Transparency of figure
	screw.set_edgecolor(edge_c) # Edge color of the lines on the figure
	screw.set_linewidth(edge_w) # Line width of the edges
	screw.set_facecolor(color) # General color of the figure

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

