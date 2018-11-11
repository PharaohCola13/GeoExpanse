# A Pair of corksurfs, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Corkscrew Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
	# Definition of x
	def x_(u,v):
		x = a * cos(u) * cos(v)
		return x

	# Definition of y
	def y_(u,v):
		y = a * sin(u) * cos(v)
		return y

	# Definition of z
	def z_(u,v):
		z = a * sin(v) + (b * u)
		return z

	a = 2
	b = 2

	# Value of the angles
	u = linspace(0, 2 * pi, sides + 1)
	v = linspace(0, 2 * pi, edges)

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
	corksurf = ax.plot_surface(x, y, z)

	corksurf.set_alpha(alpha) # Transparency of figure
	corksurf.set_edgecolor(edge_c) # Edge color of the lines on the figure
	corksurf.set_linewidth(edge_w) # Line width of the edges
	corksurf.set_facecolor(color) # General color of the figure

	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		if save == "MP4":
			# Animate
			ani = FuncAnimation(fig, animate, frames=500,
								interval=100, save_count=50)  # frames=100)#, repeat=True)

			Writer = writers['ffmpeg']
			writer = Writer(fps=30, bitrate=1800)
			ani.save('{}.mp4'.format(name), writer=writer)
		else:
			#save = None
			# Animate
			ani = FuncAnimation(fig, animate,
								interval=1, save_count=50)  # frames=100)#, repeat=True)
			pass


		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass

