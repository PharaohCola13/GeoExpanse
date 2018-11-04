# A Sphere, brough to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from fractions import Fraction


name = "Henneberg's Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
# Definition of x
	def x_(u,v):
			x = 2 * sinh(u) * cos(v) - Fraction(2,3) * sinh(3 * u) * cos(3 * v)
			return x

	# Definition of y
	def y_(u,v):
			y = 2 * sinh(u) * sin(v) + Fraction(2,3) * sinh(3 * u) * sin(3 * v)
			return y

	# Definition of z
	def z_(u,v):
			z  = 2 * cosh(2 * u) * cos(2 * v)
			return z

	# Number of edges on the base
	s = sides
	# Values of the angles
	u = linspace(-pi/4, pi/4, s + 1)
	v = linspace(-pi/2, pi/2, edges)

	u, v = meshgrid(u, v)

	# Symbolic Representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

	# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

	# Axis Limits
#        ax.set_xlim(-10,10)
#        ax.set_ylim(-10,10)
#        ax.set_zlim(-10,10)

	# Surface Plot
	henne = ax.plot_surface(x, y, z)

	henne.set_alpha(alpha) # Transparency of figure
	henne.set_edgecolor(edge_c) # Edge color of the lines on the figure
	henne.set_linewidth(edge_w) # Line width of the edges
	henne.set_facecolor(color) # General color of the figure


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

