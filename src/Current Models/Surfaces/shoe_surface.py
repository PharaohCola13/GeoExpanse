# A Pair of shoesurfs, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Shoe Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()

	# Definition of x
	def x_(u,v):
		x = u
		return x

	# Definition of y
	def y_(u,v):
		y = v
		return y

	# Definition of z
	def z_(u,v):
		z = (1./3.) * u**3 - (1./2.) * v**2
		return z

	# Value of the angles
	u = linspace(-2 * pi, 2 * pi, sides + 1)
	v = linspace(-2 * pi, 2 * pi, edges)

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
	shoesurf = ax.plot_surface(x, y, z)

	shoesurf.set_alpha(alpha) # Transparency of figure
	shoesurf.set_edgecolor(edge_c) # Edge color of the lines on the figure
	shoesurf.set_linewidth(edge_w) # Line width of the edges
	shoesurf.set_facecolor(color) # General color of the figure

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

