#{u, Sin[v]*(u^3+2u^2-2u+2)/5, Cos[v]*(u^3+2u^2-2u+2)/5}

# A Vase, brought to you by PharaohCola13
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Vase"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp, save):
	# Definition of x
	def x_(u, v):
		x = cos(v) * (u**3 + 2 * u**2 - 2 * u + 2)/5
		return x

	# Definition of y
	def y_(u, v):
		y = sin(v) * (u**3 + 2 * u**2 - 2 * u + 2)/5
		return y


	# Definition of z
	def z_(u, v):
		z = u
		return z

	# Value of the angles
	u = linspace(-2.3, 1.3, edges)
	v = linspace(0, 2 * pi, sides + 1)

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

	# Surface Plot
	vase = ax.plot_surface(x, y, z)

	vase.set_alpha(alpha)  # Transparency of figure
	vase.set_edgecolor(edge_c)  # Edge color of the lines on the figure
	vase.set_linewidth(edge_w)  # Line width of the edges
	vase.set_facecolor(color)  # General color of the figure

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
			# save = None
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
