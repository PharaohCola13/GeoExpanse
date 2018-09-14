# A Hyperbolic Octahedron, brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Hyperbolic-Octahedron"

def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid):
	global name
	# Definition of x
	def x_(u,v):
		x = (cos(u) * cos(v))**3
		return x

	# Definition of y
	def y_(u,v):
		y = (sin(u) * cos(v))**3
		return y

	# Definition of z
	def z_(u,v):
		z = sin(v)**3
		return z

	# Value of the angles
	u = linspace(-pi/2, pi/2, 25)
	v = linspace(-pi, pi, 25)

	u, v = meshgrid(u, v)

	# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

	# Axis Properties
	plt.axis(grid)
	plt.axis('equal')

	# Axis Limits
	ax.set_xlim(-1,1)
	ax.set_ylim(-1,1)
	ax.set_zlim(-1,1)

	# Surface Plot
	hyper_octa = ax.plot_surface(x, y, z)

	hyper_octa.set_alpha(alpha) # Transparency of figure
	hyper_octa.set_edgecolor(edge_c) # Edge color of the lines on the figure
	hyper_octa.set_linewidth(edge_w) # Line width of the edges
	hyper_octa.set_facecolor(color) # General color of the figure

	def animate(i):
		global rot_elev, rot_azim
	#     # azimuth angle : 0 deg to 360 deg
	#     # elev = i * n --> rotates object about the xy-plane with a magnitude of n
	#     # azim = i * n --> rotates object around the z axis with a magnitude of n
	#     # For top view elev = 90
	#     # For side view elev = 0
	#
		ax.view_init(elev=rot_elev * i, azim=rot_azim * i)

	ani = FuncAnimation(fig, animate,
		   	frames=1000000, interval=1000, blit=False, repeat=True)
