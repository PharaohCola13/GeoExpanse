# A Cross-Cap, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Cross Cap"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
# Definition of x
	def x_(u,v):
			x = cos(u) * sin(2 * v)
			return x

# Definition of y
	def y_(u,v):
    		y = sin(u) * sin(2 * v)
    		return y

# Definition of z
	def z_(u,v):
    		z = -1 * (cos(v)**2 - (cos(u)**2 * sin(v)**2))
    		return z


# Values of the angles
	s = sides
	u = linspace(0, 2 * pi, s + 1)
	v = linspace(0, pi/2, edges)

	u, v = meshgrid(u, v)

# Symbolic Representation
	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Surface Plot
	cross_cap = ax.plot_surface(x,y,z, rstride=1, cstride=1)

	cross_cap.set_alpha(alpha) # Transparency of figure
	cross_cap.set_edgecolor(edge_c) # Edge color of the lines on the figure
	cross_cap.set_linewidth(edge_w) # Line width of the edges
	cross_cap.set_facecolor(color) # General color of the figure


	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		# Animate
		ani = FuncAnimation(fig, animate,
							interval=1, save_count=50)

		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()


	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass
